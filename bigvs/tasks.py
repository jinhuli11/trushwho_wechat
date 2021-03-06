# coding: utf-8
'''
Created on 2016年5月19日

@author: likun
'''
from django.db.models.aggregates import Count
from django.core.cache import cache
from celery import task
from xpinyin import Pinyin
from multiprocessing.dummy import Pool

from articles.models import ArticlePostedResults, Judgement
from bigvs.models import BigVs
from common.utils import debug
from common.constants import BIGVS_ALL_KEY
import time


@task
def build_words_weight():
    st = time.time()
    bigvs = BigVs.objects.all()
    def _build(b):
        data = ArticlePostedResults.active_objects.filter(bigv__v_id=b.v_id, is_correct__in=(0, 1)).values('is_correct').annotate(count=Count('is_correct')).order_by('is_correct')
        sum_c , w, c = 0, 0, 0
        for d in data:
            if d['is_correct'] == 1:
                c = d['count']
            sum_c += d['count']
        if sum_c:
            w = c * 1.0 / sum_c
            c = w * 200
            sum_c = 200
        data = Judgement.objects.filter(article__bigv=b, judge__isnull=False).values('judge').annotate(count=Count('judge')).order_by('judge')
        for d in data:
            if d['judge'] == 'right':
                c += d['count']
            sum_c += d['count']
        if sum_c:
            w = int(round(c * 1.0 / sum_c * 100))
            b.words_weight = w
            b.save()
            print b.name, c, sum_c, w
    pool = Pool(8)
    pool.map(_build, bigvs)
    pool.close()
    pool.join()
    ed = time.time()
    debug('build_words_weight', ed - st)
  

@task
def build_pinyin_for_name():
    st = time.time()
    bigvs = BigVs.objects.filter(isdefault=0)
    p = Pinyin()
    def _build(bv):
        if bv.name and not bv.initials:
            bv.pinyin = p.get_pinyin(bv.name, u'')
            bv.initials = p.get_initials(bv.name, u'')
            bv.save()
    pool = Pool(8)
    pool.map(_build, bigvs)
    pool.close()
    pool.join()
    ed = time.time()
    debug('build_pinyin_for_name', ed - st)
    

@task
def cache_bigv_():
    st = time.time()
    bigvs = BigVs.objects.values('v_id', 'name', 'words_weight')
    res = {}
    map(lambda x: res.update({x['v_id']: x}), bigvs)
    cache.set(BIGVS_ALL_KEY, res)
    ed = time.time()
    debug('cache_bigv', ed - st)

