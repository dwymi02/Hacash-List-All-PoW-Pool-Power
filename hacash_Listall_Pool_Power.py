#/***
#+-----------------------------------------------------------------------------------------------------------------------------------------------+
#| RE              : hacash_Listall_Pool_Power.py
#|                   Displays the Hacash Pool Power for all known pools
#| DATE			   : Jun-05-2021
#| NOTES           : Parses the pool explorer web page, extracting the [Period PoW Worth] for all clients, providing a summary of all clients
#|                   The URL was obtained from [https://miningpoolstats.stream/hacash]
#| KNOWN PROBLEMS  : N/A
#|
#| CHANGE LOG      : Version       Date                                              Description of code change
#|                   -------    -----------    --------------------------------------------------------------------------------------------------
#|                   0.1.0      Jun-05-2021    Initial inception
#+-----------------------------------------------------------------------------------------------------------------------------------------------+
#*/

#!/usr/bin/env python3

import urllib.request
#from pprint import pprint
from html_table_parser.parser import HTMLTableParser


def url_get_contents(url):
    """ Opens a website and read its binary contents (HTTP Response Body) """
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)

    return f.read()


def strip_out_header_data(html_table):
    """ Handles embedded lists; strips out header data """
    copylist = []

    for inner_p in html_table:
        for inner_p_ofp in inner_p:
            for item in inner_p_ofp:
                if item == '#' or item == 'Address' or item == 'Clients' or item == 'PeriodPowWorth' or item == 'FindBlocks/Coins' or item == 'CompleteRewards' or item == 'DeservedRewards' or item == 'UnconfirmedRewards':
                    continue
                else:
                    copylist.append(item)

    return copylist


def sum_period_pow_worth(copylist):
    """ Parse list; Sum Period PoW Worth """
    strslash      = "/"
    j             = 0
    totalpowworth = 0
    #tmp           = ""

    for item in copylist:

        if (item.__contains__(strslash)):
            tmp = copylist[j-1]
            totalpowworth += int(copylist[j-1])
            j += 1
        else:
            j += 1
            continue

    return totalpowworth


def main():
    allhacpoolslist = ['http://95.165.168.191:3340', 'http://182.92.163.225:3340', 'http://3.101.62.234:3340', 'http://163.123.181.77:3340', 'http://104.217.254.247:3340', 'http://65.21.94.113:3340']

    for urlitem in allhacpoolslist:
        url = urlitem
        xhtml = url_get_contents(url).decode('utf-8')

        p = HTMLTableParser()
        p.feed(xhtml)

        copylist = strip_out_header_data(p.tables)

        totalpowworth = 0

        totalpowworth = sum_period_pow_worth(copylist)

        print("Total PoW Power for Pool [" + urlitem + "]:")

        """ Print totalpowworth without formatting """
        #print(totalpowworth)

        print(str(("{:,}".format(totalpowworth))))

if __name__ == '__main__':
    main()

# End of code hacash_eu_Hacash_Pool_Power.py