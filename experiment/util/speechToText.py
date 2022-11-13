#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import locale
import logging

from aiy.board import Board, Led
from util.cloudspeech import CloudSpeechClient

def get_hints(language_code):
    if language_code.startswith('ko_'):
        return ('응', '먹었어', '아니', '비타안녕', '잘가')
    return None

def locale_language():
    language, _ = locale.getdefaultlocale()
    return language

def listen():
    logging.basicConfig(level=logging.DEBUG)

    parser = argparse.ArgumentParser(description='Assistant service example.')
    parser.add_argument('--language', default=locale_language())
    args = parser.parse_args()

    logging.info('Initializing for language %s...', args.language)
    hints = get_hints('ko_KR')
    client = CloudSpeechClient()
    with Board() as board:
        while True:
            if hints:
                logging.info('Say something, e.g. %s.' % ', '.join(hints))
            else:
                logging.info('Say something.')
            text = client.recognize(language_code='ko_KR',
                                    hint_phrases=hints)
            if text is None:
                logging.info('You said nothing.')
                continue

            logging.info('You said: "%s"' % text)
            return text
