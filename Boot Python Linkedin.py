#!/usr/bin/env python
# coding: utf-8

# In[5]:


from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Chrome()

navegador.get("https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Ffeed%2F&fromSignIn=true&trk=cold_join_sign_in")


# In[6]:


#coloca meu email
navegador.find_element_by_xpath('//*[@id="username"]').send_keys(str(input('Seu e-mail: ')))
sleep(1)

#coloca minha senha
navegador.find_element_by_xpath('//*[@id="password"]').send_keys(str(input('Sua senha: ')))
sleep(2)

#clica no botão de entrar
navegador.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button').click()
sleep(1)

#clica no botão de busca
navegador.find_element_by_xpath('//*[@id="global-nav-search"]/div').click()
sleep(1)

#escreve na barra o que quer buscar
navegador.find_element_by_xpath('//*[@id="global-nav-typeahead"]/input').send_keys(str(input('Qual vaga procura: ')))
sleep(1)

#pressiono o enter 
navegador.find_element_by_xpath('//*[@id="global-nav-typeahead"]/input').send_keys(Keys.ENTER)
sleep(3)

#clica em vagas
navegador.find_element_by_xpath('//*[@id="search-reusables__filters-bar"]/ul/li[1]/button').click()


# In[4]:




