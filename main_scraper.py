#!/usr/bin/python3.9
"""Main module of the app. Where all functionalities are accessed from"""
import os
import scrapy
import questionary
from scraper import Scraper
from loguru import logger

fmt = "{time} - {name} - {level} - {message}"
logger.add("spam.log", level="DEBUG", format=fmt)
logger.add("error.log", level="ERROR", format=fmt)


def main():
    """Here we start, sequentially, all the steps needed to create a scraping campaign."""
    rasoura = Scraper(
        "eco",
        "eco_newspaper",
        "/home/mic/python/scraper",
        "https://eco.sapo.pt/2021/08/10/chineses-obrigam-loja-da-xiaomi-em-portugal-a-desistir-de-pagamentos-com-criptomoedas/",
        '//*[@id="post-878113"]/div/div[1]/header/h1/text()',
        '//*[@id="post-878113"]/div/div[1]/header/div[2]/div/div[1]/ul/li[1]/a/text()',
        '//*[@id="post-878113"]/div/div[1]/header/div[2]/div/div[1]/ul/li[2]',
        '//*[@id="post-878113"]/div/div[1]/div[1]/p/text()',
    )

    rasoura.dislocation1()
    rasoura.start_project()
    rasoura.start_spider()
    rasoura.edit_spider_file_clean_file()
    rasoura.edit_spider_file_parse_function()
    rasoura.settings()
    rasoura.crawl()
    rasoura.result()


main()
