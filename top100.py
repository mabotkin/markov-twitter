from lxml import html
import requests

page = requests.get("http://twittercounter.com/pages/100")
tree = html.fromstring(page.content)

handles = tree.xpath('//span[@itemprop="alternateName"]/text()')

fout = open("accounts.txt","w")
for handle in handles:
	fout.write(handle + "\n")
fout.close()
