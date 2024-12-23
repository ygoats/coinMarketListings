#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 19:29:56 2021

@ygoats
"""

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import telegram_send
from time import sleep
from datetime import datetime

ticker_list = []
contract_list = []

googleList = []

def Main():
    try:
        googleList = []
        
        now = datetime.now()
        t = now.strftime("%m/%d/%Y, %H:%M:%S")
    
        url = 'https://coinmarketcap.com/new/'
        
        #print(url)
        
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        
        page_soup = soup(webpage, "html.parser")
        
        containers = page_soup.findAll("p", "sc-1eb5slv-0 iJjGCS")
        #print(containers)
        ticker = str(containers[0])
        
        tickerD = ticker.replace("""<p class="sc-1eb5slv-0 iJjGCS" color="text" font-size="1" font-weight="semibold">""", "")
        tickerDD = tickerD.replace('</p>', '')
        tickerDDD = tickerDD.replace(' ', '-')
        
        ticker_list.append(tickerDDD)
        
        #print(tickerR)
        
        url = str("https://coinmarketcap.com/currencies/"+str(ticker_list[0]))
        
        #print(url)
        
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        
        webpage = urlopen(req).read()
        
        page_soup = soup(webpage, "html.parser")

        containers1 = page_soup.findAll("a", "cmc-link") #####################################################

        contract = containers1[20]["href"]
        contract = contract.replace("https://bscscan.com/token/", "")
        
        contract_list.append(contract)
        
        startProcess = True
        
    except Exception as e:
        print(e)
        startProcess = True

    while startProcess == True:
        sleep(3)
        try:
            url = 'https://coinmarketcap.com/new/'
        
            #print(url)
            
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req).read()
            
            page_soup = soup(webpage, "html.parser")
            
            containers = page_soup.findAll("p", "sc-1eb5slv-0 iJjGCS")
            #print(containers)
            ticker = str(containers[0])
            
            tickerD = ticker.replace("""<p class="sc-1eb5slv-0 iJjGCS" color="text" font-size="1" font-weight="semibold">""", "")
            tickerDD = tickerD.replace('</p>', '')
            tickerDDD = tickerDD.replace(' ', '-')
            tickerR = tickerDDD
            #print(tickerR)
            
            sleep(3)
            
            url = str("https://coinmarketcap.com/currencies/"+str(tickerR))
            
            #print(url)
            
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req).read()
            
            page_soup = soup(webpage, "html.parser")
            
            containers1 = page_soup.findAll("a", "cmc-link") 
            contract = containers1[20]["href"]
            checkChain = containers1[20]
            contract = contract.replace("https://bscscan.com/token/", "")
                
            if tickerR not in ticker_list:
                ticker_list.append(tickerR)
                try:
                    contract_list.append(contract)
                except IndexError as e:
                    print(e)
                    contract_list.append('NULL')
                    
                print('ticker ' + str(tickerR))
                print('contract ' + str(contract))
                print('chain ' + str(checkChain))
                
                if "Binance Smart Chain" in str(checkChain):
                    telegram_send.send(conf='channel3.conf',messages=["CoinmarketCap Listing Added" + "\n" + "\n" + \
                                                           str(tickerR) + "\n" + "\n" + \
                                                           "Contract Number" + "\n" + \
                                                           str(contract) + "\n" + "\n" + \
                                                           "https://www.dextools.io/app/pancakeswap/pair-explorer/" + str(contract)])
 
                elif "Ethereum" in str(checkChain):
                    telegram_send.send(conf='channel3.conf',messages=["CoinmarketCap Listing Added" + "\n" + "\n" + \
                                                           str(tickerR) + "\n" + "\n" + \
                                                           "Contract Number" + "\n" + \
                                                           str(contract) + "\n" + "\n" + \
                                                           "https://www.dextools.io/app/uniswap/pair-explorer/" + str(contract)])
                    
                elif "Polygon" in str(checkChain):
                    telegram_send.send(conf='channel3.conf',messages=["CoinmarketCap Listing Added" + "\n" + "\n" + \
                                                           str(tickerR) + "\n" + "\n" + \
                                                           "Contract Number" + "\n" + \
                                                           str(contract) + "\n" + "\n" + \
                                                           "https://www.dextools.io/app/quickswap/pair-explorer/" + str(contract)])
                elif "Solana" in str(checkChain):
                    telegram_send.send(conf='channel3.conf',messages=["CoinmarketCap Listing Added" + "\n" + "\n" + \
                                                           str(tickerR) + "\n" + "\n" + \
                                                           "Contract Number" + "\n" + \
                                                           str(contract)])
                        
                googleList.append(tickerR)
            
            lengthGoogle = len(googleList)
            if lengthGoogle > 0:
                f = open('coinmarketcapCoins.txt', 'a')
                f.write(str(tickerR) + ", ")
                f.close()
                googleList = []
        except Exception as e:
            print(e)
            print(contract_list)
            continue
            
if __name__ == '__main__':
    Main()
