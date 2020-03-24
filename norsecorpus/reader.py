"""
Readers of texts
"""

import os
import re
from nltk.tokenize import sent_tokenize
from cltk.tokenize.word import WordTokenizer
from lxml import etree

from norsecorpus import PACKDIR

__author__ = ["Clément Besnier <clemsciences@aol.com>", ]

namespaces = {'n': 'http://www.tei-c.org/ns/1.0'}

word_tokenizer = WordTokenizer("old_norse")


def get_corresponding_data(text_name):
    corresponding = []
    for i in os.listdir(os.path.join(PACKDIR, "data")):
        if os.path.isdir(os.path.join(PACKDIR, "data", i)):
            for j in os.listdir(os.path.join(PACKDIR, "data", i)):
                if text_name == j:
                    corresponding.append(os.path.join(PACKDIR, "data", i, j))
    return corresponding


def get_available_texts(text_format="tei", file_format="xml"):
    """
    Provides all the available texts in a given format

    >>> list(get_available_texts().keys())[0]
    'volsunga.xml'

    :param file_format: text standard
    :param text_format: file extension
    :return: dictionary whose keys are file names and values are paths to the file
    """
    filenames = {}
    for path, subdirs, files in os.walk(os.path.join(PACKDIR, "data")):
        if os.path.isdir(path):
            folders = path.split(os.path.sep)
            if len(folders) > 0:
                parent_folder = folders[-1]
                if parent_folder == text_format:
                    for name in files:
                        if os.path.isfile(os.path.join(path, name)) and os.path.join(path, name).endswith(file_format):
                            filenames[name] = os.path.join(path, name)
    return filenames


def normalize(text: str):
    text = text.replace("\n", " ")
    text = re.sub(" +", " ", text)
    return text


def get_xml_root(filename, path=""):
    """

    :param filename:
    :param path:
    :return:
    """
    parser = etree.XMLParser(load_dtd=True, no_network=False)
    tree = etree.parse(os.path.join(path, filename), parser=parser)
    root = tree.getroot()
    return root


def read_tei_chapters(filename, path=""):
    """

    :param filename:
    :param path:
    :return:
    """
    root = get_xml_root(filename, path)
    chapters = root.findall('.//n:div[@type="chapter"]', namespaces=namespaces)
    return chapters


def read_tei_paras(filename, path=""):
    """

    :param filename:
    :param path:
    :return:
    """
    chapters = read_tei_chapters(filename, path)
    paras = [[normalize(para.text) for para in chapter.getchildren()] for chapter in chapters]
    return paras


def read_tei_sentences(filename, path=""):
    """

    :param filename:
    :param path:
    :return:
    """
    paras = read_tei_paras(filename, path)
    sentences = [[sent_tokenize(para) for para in chapter] for chapter in paras]
    return sentences


def read_tei_words(filename, path=""):
    sentences = read_tei_sentences(filename, path)
    words = [[[word_tokenizer.tokenize(sentence) for sentence in para] for para in chapter] for chapter in sentences]
    return words
