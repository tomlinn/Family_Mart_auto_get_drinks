# [全家飲料自動抽_Family_Mart_auto_get_drinks]
# Note:
it's not a crack tool! it's just a tool to help me click a button!
# Feature: 
 網頁載入時,立即抽獎<br>
 Auto get drinks when the website load.

### 為何要用? 甚麼時候要用這個小工具呢?
### Why I need this?

是當你有5個帳號時,你又覺得天天抽獎很麻煩,還要每天還要切換帳號, 還要點擊抽獎按鈕時, 這讓你一天至少省了15分鐘!!!<br>
 Like me, I have 5 accounts and I'm tired to login and logout each account everyday.<br>Therefore I used a simple code to help me!!!


# To use:
## 1. 先去手機app取得你帳號的link:
## 1. Get your personal game's link:

##### 照這下面的影片做 (活動列表/長按後按Get links)
##### To the list of games and click hard to get links

![image](https://github.com/tomlinn/Family_Mart_auto_get_drinks/blob/master/to_get_link.gif?raw=true)
## 2. 保存你的link在google chrome的書籤
## 2. keep this link in your google chrome book mark.
(it don't need to login in all the time, so keep your links carefully)
# ![image](https://github.com/tomlinn/Family_Mart_auto_get_drinks/blob/master/turtorial-2.PNG?raw=true)

## 3. 把我的code放到 Tampermonkey 中
## 3. put my code in Tampermonkey
# ![image](https://github.com/tomlinn/Family_Mart_auto_get_drinks/blob/master/turtorial-1.PNG?raw=true)

## 4. 快完成了!!!
## 4. Almost Done!

## 5. 如果你像我一樣有五個帳號, 就會像下面一樣 每個link分別是一個帳號
## 5. if you have many accounts (like 5), it would look like this
# ![image](https://github.com/tomlinn/Family_Mart_auto_get_drinks/blob/master/turtorial-2.PNG?raw=true)

## 6. 當每天需要抽獎時,右鍵按"開啟全部5個書籤",就一鍵抽飲料了!!
## 6. and you just need to open all website at one time, then you get your drinks.
# ![image](https://github.com/tomlinn/Family_Mart_auto_get_drinks/blob/master/turtorial-3.PNG?raw=true)

## 7. 成果!
## 7. result - one click to get 5 accounts' drinks 
# ![image](https://github.com/tomlinn/Family_Mart_auto_get_drinks/blob/master/turtorial-4.gif?raw=true)


## 8.如果你懂python, 用個簡單的爬蟲就能顯示這些帳號的獎項了!!
## 8.if you know about python, it can show all rewards in these accounts
```python
#list_drinks.py
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
```
# ![image](https://github.com/tomlinn/Family_Mart_auto_get_drinks/blob/master/result_list_1.png?raw=true)
