"""

"""
import os
import unittest
from lxml import etree

import norsecorpus.reader as ncr
from norsecorpus import PACKDIR

__author__ = ["Clément Besnier <clemsciences@aol.com>", ]


class TestMain(unittest.TestCase):
    """

    """
    def setUp(self) -> None:
        self.filename = "volsunga.xml"
        self.volsunga_path = os.path.join(PACKDIR, "data", "heimskringla", "Völsunga_saga", "tei")

    def test_root(self):
        root = ncr.get_xml_root(self.filename, self.volsunga_path)
        self.assertEqual(type(root), etree._Element)

    def test_read_tei_chapter(self):
        target = "Hér hefr upp ok segir frá þeim manni, er Sigi er nefndr ok kallaðr, at héti sonr Óðins. Annarr maðr"
        volsunga = ncr.read_tei_chapters(self.filename, self.volsunga_path)
        hundred_characters = volsunga[0][0]
        self.assertEqual(target, hundred_characters.text[:100].strip())

    def test_read_tei_paragraph(self):
        target = "Hér hefr upp ok segir frá þeim manni, er Sigi er nefndr ok kallaðr, at héti sonr Óðins. Annarr maðr "
        volsunga = ncr.read_tei_paras(self.filename, self.volsunga_path)
        self.assertEqual(target, volsunga[0][0][:100])

    def test_read_tei_sentence(self):
        target = "Hér hefr upp ok segir frá þeim manni, er Sigi er nefndr ok kallaðr, at héti sonr Óðins."
        volsunga = ncr.read_tei_sentences(self.filename, self.volsunga_path)
        self.assertEqual(target, volsunga[0][0][0])

    def test_read_tei_word(self):
        target = ["Hér",  "hefr", "upp", "ok", "segir", "frá", "þeim", "manni", ",", "er", "Sigi", "er", "nefndr", "ok",
                  "kallaðr", ",", "at", "héti", "sonr", "Óðins", "."]
        volsunga = ncr.read_tei_words(self.filename, self.volsunga_path)
        self.assertEqual(target, volsunga[0][0][0])
