#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :


import urllib2

from bs4 import BeautifulSoup
from telebot import TeleBot

'''
Simple client web per descarregar FREE LEARNING - FREE TECHNOLOGY EBOOKS

@autor: Oliver Lacambra Rami - 47681213M
'''

class Client(object):
    __url = u"https://www.packtpub.com/packt/offers/free-learning/"

    def get_webpage(self):
        """obtenir la plana web"""
        f = urllib2.urlopen(self.__url)
        result = f.read()
        f.close()
        return result

    def search_data(self, body):
        """buscar dades"""
        bs = BeautifulSoup(body)
        dotd_title_div = bs .find("div", "dotd-title")
        book_name = dotd_title_div.find("h2")
        return book_name.text

if __name__ == "__main__":
    telegram_bot = TeleBot("364217701:AAF3WUE0g9_QBad5ZAKDo-cyM4SwX970NQo")


    @telegram_bot.message_handler(commands=["start"])
    def send_book_name(message):
        cw = Client()
        body = cw.get_webpage()
        book_name = cw.search_data(body)
        telegram_bot.reply_to(message, book_name)
        """imprimir resultats"""
        print book_name




    telegram_bot.polling()
