# coding=utf-8
"""
LANGS
Loads Pyconfs langs.

Author: Pablo Pizarro @ppizarror
Date: 2017.
Licence: GPLv2
"""

# Library imports
from __future__ import print_function
from _path import DIR_LANG
import math


# noinspection PyBroadException
class LangLoader(object):
    """
    Loads a lang file.
    """

    def __init__(self, language):
        """
        Constructor.

        :param language: Language to load.
        :type language: str

        :return: void
        :rtype: None
        """
        language = str(language).upper()
        try:
            langfile = open(DIR_LANG + language)
        except:
            raise _UnknownLangFile(
                'Lang {0} does not exist or cant be loaded'.format(language))
        self.lang = {}
        for line in langfile:
            line = line.strip().replace('\ufeff', '').split(' // ')
            if '\xef\xbb\xbf' in line[0]:
                line[0] = line[0][3:]
            if line[0] == '':
                line[0] = '10'
            self.lang[int(line[0].replace('\ufeff', ''))] = line[1].replace(
                '|', ' ')
        langfile.close()
        self.langname = language

    # noinspection PyUnresolvedReferences
    def get(self, index, *args, **kwargs):
        """
        Returns string associated to <index> value.

        :param index: String index.
        :type index: int, string
        :param args: Arguments
        :type args: list
        :param kwargs: Parameters
        :type kwargs: list

        :return: String associated with index.
        :rtype: str
        """
        if str(index).isdigit():
            try:
                if kwargs.get('noformat') or len(args) == 0:
                    return self.lang[index]
                else:
                    return self.lang[index].format(*args)
            except:
                raise _LangBadIndex('Index {0} does not exist'.format(index))
        else:
            raise AssertionError('Index {0} must be numerical'.format(index))

    def print_all(self):
        """
        Prints all elements.

        :return: void
        :rtype: None
        """

        def _totalspaces(index):
            """
            Return total spaces in a String.

            :param index: Índice
            :type index: int

            :return: Cantidad de espacios
            :rtype: int
            """
            return int(round(math.log(index, 10), 2) + 1) * ' '

        print('Entry:\n\tID     STRING')
        for key in self.lang.keys():
            print('\t{0}{1}=> {2}'.format(str(key), _totalspaces(key),
                                          self.lang[key]))


class _LangBadIndex(Exception):
    """
    Lang index does not exist.
    """
    pass


class _UnknownLangFile(Exception):
    """
    Exception raised when lang file does not exist.
    """
    pass
