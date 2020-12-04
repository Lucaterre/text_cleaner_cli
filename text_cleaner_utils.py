#!/usr/bin/env python3
"""
CLI UTILS
Date : 04/12/2020
"""

import re
import string

import click

def report_log(message: str, type_log='I'):
    if type_log == 'I': # Info
        click.secho(message)
    elif type_log == "W":  # Warning
        click.secho(f'[WARNING :] {message}',
                    fg='yellow',
                    bold=True)
    elif type_log == "E":  # Error
        click.secho(f'[ERROR :] {message}',
                    fg='red',
                    bold=True)
    elif type_log == "S":  # Success
        click.secho(message,
                    fg='green',
                    bold=True)
    elif type_log == "V":
        click.secho(message,
                    fg='blue',
                    bold=True)  # Verbose
    else:
        # unknown color parameter, treated as "normal" text
        click.secho(message)

def write_text(filename:str, sequence: str):
    with open(f'{filename}.txt', 'w') as f:
        f.write(str(sequence))

"""
Cleaning missy text lambda functions collection
-----------------------------------------------
"""

lower_clean = lambda sequence: \
    sequence.lower()
punctuation_clean = lambda sequence: \
    re.sub(r"[^\w\d\s]+", '', sequence)
punctuation_clean_except_apos = lambda sequence: \
    re.sub(r"[^\w\d'\s]+", '', sequence)
digits_clean = lambda sequence: \
    sequence.translate(str.maketrans('', '', string.digits))
whitespace_clean = lambda sequence: \
    sequence.translate(str.maketrans('', '', string.whitespace))
linebreak_clean = lambda sequence: \
    re.sub(r'([\r\n]+?)+', r'\n', sequence)

def clean_processing(lower: bool,
                punctuation: bool,
                punctuation_e_apos: bool,
                digits: bool,
                whitespace: bool,
                linebreak: bool,
                sequence: str):
    if lower:
        sequence = lower_clean(sequence)
    if punctuation:
        sequence = punctuation_clean(sequence)
    if punctuation_e_apos:
        sequence = punctuation_clean_except_apos(sequence)
    if digits:
        sequence = digits_clean(sequence)
    if whitespace:
        sequence = whitespace_clean(sequence)
    if linebreak:
        sequence = linebreak_clean(sequence)
    if lower == False \
            and punctuation == False \
            and digits == False \
            and whitespace == False \
            and linebreak == False:
        report_log("NO CLEANING OPTIONS WERE SELECTED.\n", type_log = 'W')

    return sequence
