#!/usr/bin/env python
# coding: utf-8

# # selenium获取教师页面链接

# 厦门大学是学部--学院--系--（教授，副教授，助理教授。。。）的结构，因此教师信息页面特别多

# In[18]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import json
import re
from collections import defaultdict
from lxml import etree
from selenium.webdriver.common.action_chains import ActionChains
from tqdm import tqdm
#放chromedriver的文件路径加文件名
CHROME_DRIVER = './chromedriver.exe'

# 创建chrome参数对象
opt = webdriver.ChromeOptions()
opt.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度
#options=opt)
#chrome_options = Options()
#chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=CHROME_DRIVER,options = opt)


# In[34]:


# 根据城市和时间范围构筑连接列表
urls =[]
for city in ['beijing','shanghai','wuhan']:
    for year in [2012,2013,2014,2015,2016,2017,2018,2019]:
        for month in ['01','02','03','04','05','06','07','08','09','10','11','12']:
            urls.append('http://lishi.tianqi.com/{}/{}{}.html'.format(city,year,month))


# In[35]:


result = []
for url in tqdm(urls):
    driver.get(url)
    # 点击查看更多
    driver.find_element_by_class_name('lishidesc2').click()
    # 获取天气表格
    table = driver.find_element_by_xpath('//ul[@class="thrui"]')
    trs = table.find_elements_by_xpath('li')
    # 
    for i in trs:
        a = []
        tr = i.find_elements_by_xpath('div')
        for td in tr:
            a.append(td.text)
        result.append(a)


# In[36]:


df=pd.DataFrame(result)
df.to_csv('weather1.csv',index=False,encoding='gbk')

