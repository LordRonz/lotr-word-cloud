from bs4 import BeautifulSoup as BS
import requests

soup = BS(requests.get('https://ae-lib.org.ua/texts-c/tolkien__the_lord_of_the_rings_1__en.htm').text, 'html.parser')

with open('./1_The_Fellowship_Of_The_Ring/The_Fellowship_Of_The_Ring2.txt', 'a') as f:
    for txt in soup.find_all('p'):
        f.write(txt.get_text().lower())
        f.write('\n')

soup = BS(requests.get('https://ae-lib.org.ua/texts-c/tolkien__the_lord_of_the_rings_2__en.htm').text, 'html.parser')

with open('./2_The_Two_Towers/The_Two_Towers2.txt', 'a') as f:
    for txt in soup.find_all('p'):
        f.write(txt.get_text().lower())
        f.write('\n')

soup = BS(requests.get('https://ae-lib.org.ua/texts-c/tolkien__the_lord_of_the_rings_3__en.htm').text, 'html.parser')

with open('./3_The_Return_Of_The_King/The_Return_Of_The_King2.txt', 'a') as f:
    for txt in soup.find_all('p'):
        f.write(txt.get_text().lower())
        f.write('\n')