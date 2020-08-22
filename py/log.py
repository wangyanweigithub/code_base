import logging
from logging import StreamHandler
import sys

def a():
    
    a = logging.getLogger('a')
    h = StreamHandler()
    a.setLevel(logging.INFO)
    a.addHandler(h)
    a.info('aaa')
    a.info('aaa')
    a.warning('warning')
    a.info('aaa')
    a.info('aaa')


def b():
    log = logging.getLogger('b')
    h = StreamHandler()
    log.addHandler(h)
    log.setLevel(logging.WARN)
    log.info('bbb')
    log.warning('warning')
    log.info('bbb')
    log.info('bbb')
    log.info('bbb')
    log.info('bbb')


a()
b()
