#!/usr/bin/env python3
"""
CLI CONTROL
Date : 04/12/2020
"""

import time
import os
import glob
import sys

import click
import pyfiglet
from tqdm import tqdm

from text_cleaner_utils import *

# Constants
ascii_logo_textcleaner = pyfiglet.figlet_format("| Text Cleaner |", font='slant')

@click.command()
@click.option('-pt', '--path_text_file',
              help='Indicate the relative/absolute path to your text file to be processed.')
@click.option('-pb', '--path_batch_text',
              help='Indicate the relative/absolute path to the directory containing several text files for batch processing.')
@click.option('-s', '--sequence',
              help='Indicate a sequence of characters to be processed on the fly.')

@click.option('-loc', '--lower_clean',
              default=False,
              show_default=True,
              type=click.BOOL,
              help='Make everything in sentence/text lowercase.')
@click.option('-puc', '--punctuation_clean',
              default=False,
              show_default=True,
              type=click.BOOL,
              help='Remove all punctuation in sentence/text.')
@click.option('-peac', '--punctuation_clean_except_apos',
              default=False,
              show_default=True,
              type=click.BOOL,
              help='Remove all punctuation in sentence/text except apostrophes.')
@click.option('-digc', '--digits_clean',
              default=False,
              show_default=True,
              type=click.BOOL,
              help='Remove all digits in sentence/text.')
@click.option('-wic', '--whitespace_clean',
              default=False,
              show_default=True,
              type=click.BOOL,
              help='Remove all whitespace in sentence/text.')
@click.option('-lic', '--linebreak_clean',
              default=False,
              show_default=True,
              type=click.BOOL,
              help='Remove all line break and carriage in sentence/text.')

def head(path_text_file: str,
         path_batch_text: str,
         sequence: str,
         lower_clean: bool,
         punctuation_clean: bool,
         punctuation_clean_except_apos: bool,
         digits_clean: bool,
         whitespace_clean: bool,
         linebreak_clean: bool):
    """---|Text Cleanner CLI |---

        Small CLI to clean text files in sequence or in batch.

        you can either send a text file, a batch of texts or
        a sequence of characters of your choice. Then you just
        have to choose the desired cleaning options.

        See below for more details.
    """
    report_log(ascii_logo_textcleaner, type_log='V')
    report_log('@ LucaTerre - 2020\n')
    time.sleep(3)
    if path_text_file:
        filename = os.path.basename(os.path.splitext(path_text_file)[0])
        try:
            with open(path_text_file, 'r', encoding='utf-8') as f:
                clean_text = clean_processing(lower_clean, punctuation_clean,
                                              punctuation_clean_except_apos,
                                              digits_clean, whitespace_clean,
                                              linebreak_clean, f.read())
            write_text(f'{filename}_output_clean', clean_text)
            report_log(f'\n1 file {filename}_output_clean generated', type_log='S')
        except:
            e = sys.exc_info()[0]
            report_log(f'cannot process this file. type : {e}', type_log='E')
    elif sequence:
        try:
            clean_sequence = clean_processing(lower_clean, punctuation_clean,
                                              punctuation_clean_except_apos,
                                              digits_clean, whitespace_clean,
                                              linebreak_clean, sequence)
            user_resp = input('Do you want to create a file for this sequence? [O/n] : ')
            if user_resp.lower() == 'o':
                write_text('output_sequence', clean_sequence)
                report_log('\n1 file output_sequence.txt generated', type_log='S')
            else:
                report_log(f'\nYOUR CLEAN SEQUENCE :\n {clean_sequence}')
        except:
            e = sys.exc_info()[0]
            report_log(f'cannot process this sequence. type : {e}', type_log='E')
    elif path_batch_text:
        path_to_files_list = glob.glob(path_batch_text + f"/*txt")
        list_files = [file for file in path_to_files_list]
        report_log('** List of files ** \n')
        for file in list_files:
            report_log(f'+ {os.path.basename(file)}')
        number_of_files = len(list_files)
        report_log(f'\nNumber of files :  {number_of_files}')
        report_log('*'*32 + '\n')
        if click.confirm(report_log('Do you want continue ?')):
            os.system('clear')
            collect = []
            clean_text =""
            for file in tqdm(list_files, ascii=True, desc=f'In progress ...'):
                with open(file, 'r', encoding='utf-8') as f:
                    for sequence in f.read():
                        clean_sequence = clean_processing(lower_clean, punctuation_clean,
                                                  punctuation_clean_except_apos,
                                                  digits_clean, whitespace_clean,
                                                  linebreak_clean, sequence)
                        clean_text += clean_sequence
                    collect.append(clean_text)
                    write_text(f'{os.path.basename(file)}_output_clean', clean_text)

            report_log(f'PROCESSING {len(collect)} FILES IN DIRECTORY DONE', type_log='S')

if __name__ == '__main__':
    head()

