#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A demo of the Google CloudSpeech recognizer."""
# -*- coding: utf-8 -*-
import argparse
import locale
import logging

from aiy.board import Board, Led
from cloudspeech import CloudSpeechClient

def get_hints(language_code):
    if language_code.startswith('ko_'):
        return ('응', '아니', '비타안녕', '잘가')
    return None

def locale_language():
    language, _ = locale.getdefaultlocale()
    return language

def speechToText():
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
            if '응' in text:
                return 'yes'
            elif '아니' in text:
                return 'no'
            elif '비타안녕' in text:
                return 'hello'
            elif '잘가' in text:
                return 'bye'
            else:
                print('undefined')
