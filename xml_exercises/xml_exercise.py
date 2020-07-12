from bs4 import BeautifulSoup
from pprint import pprint
from statistics import mode

with open("customers.xml") as file_handle:
    soup = BeautifulSoup(file_handle)

# pprint(soup.find_all('balance')[0].text)
# pprint(soup.find_all('firstname')[0].text)


# def mean():
#     balance_list = []
#     for balance in soup.find_all('balance'):
#         balance_list.append(int(balance.text))

#     mean = sum(balance_list)/len(balance_list)
#     return mean

# pprint(mean())


def most_common_firstname():
    # firstnames = {}
    # count, most = 0, ''

    # for firstname in soup.find_all('firstname'):
    #     firstnames[firstname.text] = firstnames.get(firstname.text, 0) + 1
    #     if firstnames[firstname.text] >= count:
    #         count, most = firstnames[firstname.text], firstname.text
    # return most
    return (mode(soup.find_all('firstname')).text)


pprint(most_common_firstname())
