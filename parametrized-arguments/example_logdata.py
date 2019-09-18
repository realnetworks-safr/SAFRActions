#!/usr/bin/python

import sys
import logging
from datetime import datetime

logging.basicConfig(filename='app.log', filemode='a',level=logging.DEBUG, format="%(asctime)s - %(message)s")
logging.getLogger().addHandler(logging.StreamHandler())

def convert_array_to_dictionary(arr):
    if len(arr) == 1:
        raise ValueError("No arguments were passed.")
    dictionary = {}
    for i in range(len(arr)):
        if i != 0: # Ignore filename
            val = arr[i].split("=")
            dictionary[val[0]] = val[1]
    return dictionary

def grab_val(dict_args, key):
    val = ""
    try:
        val = dict_args[key]
    except Exception as e:
        logging.arror(e)
    finally:
        return val
        
def process(arr):
    dict_args = convert_array_to_dictionary(arr)
    
    person_name = grab_val(dict_args, '--name')
    person_age = grab_val(dict_args, '--age')
    person_gender = grab_val(dict_args, '--gender')
    
    logging.info('Detected {}, approximately {} years of age and of the {} gender.'.format(person_name, person_age, person_gender))

try:    
    process(sys.argv)
except Exception as e:
    logging.error('An error has ocurred. {}'.format(e))
