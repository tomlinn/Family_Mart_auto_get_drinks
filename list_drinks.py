#coding=utf-8

from bs4 import BeautifulSoup
import requests
import time
account=[
      'link01',
      'link02',
      'link03',
      'link04',
      'link05',
      ]

with requests.Session() as s:
	for i in range(0,len(account)):
		
		page = s.get(account[i])
		soup = BeautifulSoup(page.content, 'lxml')
		all_page=(page.text)
		items_title=all_page.split("<h3>")
		items_reward=all_page.split("<p class=\"desc\">")
		items_username=all_page.split("會員")[1][2:14]
		print(items_username)
		for x in range(1,len(items_title)):
			if("飲料抽抽樂" in items_title[x].split("</h3>")[0] and "已參加" not in items_reward[x].split("<")[0].replace("&lt;","\n")):
				print(items_title[x].split("</h3>")[0])
				print(items_reward[x].split("<")[0].replace("&lt;",""))
		print("\n")



	
