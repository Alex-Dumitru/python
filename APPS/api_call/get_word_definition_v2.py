#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
import argparse
import logging
import sys

class oxfordConnector(object):
    def __init__(self, user_id, user_key):
        self.user_id = user_id
        self.user_key = user_key
        logger.debug("Using following apiKey authentication credentials:")
        logger.debug("ID: {}".format(my_id))
        logger.debug("KEY: {}".format(my_key))

    
    def define_word(self, word, lang='en'):
        self.lang = lang
        self.word = word
        url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/{lang}/{word}'.format(lang=self.lang, word=word.lower())
        logger.debug("Calling URI: {}".format(url))
        logger.debug("Retrieving definition for word: {}".format(self.word))
        logger.debug("language used: {}".format(self.lang))
        r = requests.get(url, headers = {'app_id' : my_id, 'app_key' : my_key})
        output = []
        if r.status_code != 200:
                logger.debug("Return code is: {}".format(r.status_code))
                logger.warning("Word '{}' not found! Check the word and try again.".format(word_id))
                return None
        else:
            entries = [a['entries'] for a in r.json()['results'][0]['lexicalEntries']]
            for entry in entries:
                for item in entry:
                    for elem in item['senses']:
                        if 'definitions' in elem.keys():
                            output.append(elem['definitions'])

        if output:
            return output

def set_logger(logging_level):
    global logger
    logger = logging.getLogger('Oxford_Dictionary')
    logger.setLevel(logging_level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extracting word definitions from Oxford Dictionary.')
    parser.add_argument('word', type=str, nargs=1, help='word to search in Oxford Dictionary.')
    parser.add_argument('output', nargs='?', type=argparse.FileType('w'), default=sys.stdout, help='name of the output file. Defaults to standard output')
    parser.add_argument('--first_only', action='store_true', help='Retrieve only the first definition found for the given word.')
    parser.add_argument('--debug', action='store_true', help='enables debugging messages to be displayed.')

    args = parser.parse_args()

    logging_level = logging.DEBUG if args.debug else logging.INFO
    set_logger(logging_level)

    my_id = 'b9dba52d'
    my_key = '5c6ef63eaa447fc38ec4e0e1c34f8f97'
    word_id = args.word[0]

    oxf = oxfordConnector(my_id, my_key)
    output = oxf.define_word(word_id)
    if output:
        if args.first_only:
            output = output[0]
        if args.output.name == '<stdout>':
            logger.debug("Writing output to console")
            logger.info("Following definitions were found: ")
            for nr, definition in enumerate(output):
                print("{} - {}".format(nr+1,''.join(definition)))
        else:
            logger.info("Writing output to file: {}".format(args.output.name))
            output_to_file = ""
            for definition in output:
                output_to_file = output_to_file + ''.join(definition).replace(',',';') + ','
            args.output.write(output_to_file)