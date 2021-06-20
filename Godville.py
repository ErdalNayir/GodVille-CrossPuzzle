# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 17:04:56 2021

@author: erdal
"""
#%% importing libaries

from selenium import webdriver

import _sqlite3

import time

#%%
artifacts=[]
monsters=[]
equipments=[]
skills=[]
pets=[]


def Data_collect():

    browser=webdriver.Firefox(executable_path=r'C:\Users\erdal\OneDrive\Masaüstü\Web Kazıma\geckodriver.exe')

    url="https://godvillegame.com/"

    browser.get(url)

    time.sleep(4)

    username=browser.find_element_by_name("username")
    password=browser.find_element_by_name("password")

    username.send_keys("EMAİL IS HERE")
    password.send_keys("PASSWORD IS HERE")

    LoginButton=browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/form/div[5]/input")

    LoginButton.click()

    time.sleep(5)



    urls={"artifacts":"https://wiki.godvillegame.com/List_of_Artifacts",
      "monsters":"https://wiki.godvillegame.com/List_of_Monsters",
      "equipments":"https://wiki.godvillegame.com/List_of_Equipment",
      "skills":"https://wiki.godvillegame.com/List_of_Skills",
      "pets":"https://wiki.godvillegame.com/Pets"}


    global artifacts
    global monsters
    global equipments
    global skills
    global pets




    for name,Url in urls.items():

        if name=="artifacts":

            for i in range(3,36):

                browser.get(Url)

                xpath="//*[@id='mw-content-text']/div/table[{}]/tbody/tr/td[1]/a".format(i)

                elements=browser.find_elements_by_xpath(xpath)

                for i in elements:

                    i=i.text

                    artifacts.append(i)

        elif name=="monsters":

            for i in range(3,32):

                browser.get(Url)

                xpath="//*[@id='mw-content-text']/div/table[{}]/tbody/tr/td[1]/a".format(i)

                elements=browser.find_elements_by_xpath(xpath)

                for i in elements:

                    i=i.text

                    monsters.append(i)


        elif name=="equipments":

            for i in range(3,32):

                browser.get(Url)

                xpath="//*[@id='mw-content-text']/div/table[{}]/tbody/tr/td[1]/a".format(i)

                elements=browser.find_elements_by_xpath(xpath)

                for i in elements:

                    i=i.text

                    equipments.append(i)


        elif name=="skills":

            for i in range(2,23):

                browser.get(Url)

                xpath="//*[@id='mw-content-text']/div/table[{}]/tbody/tr/td[1]/a".format(i)

                elements=browser.find_elements_by_xpath(xpath)

                for i in elements:

                    i=i.text

                    skills.append(i)


        elif name=="pets":

            browser.get(Url)

            xpath="//*[@id='mw-content-text']/div/table[3]/tbody/tr/td[1]/a"

            elements=browser.find_elements_by_xpath(xpath)

            for i in elements:

                i=i.text

                pets.append(i)




    browser.close()

#Data_collect() /Once you run this function,You can comment it
#%%

artifacts_new=[]
monsters_new=[]
equipments_new=[]
skills_new=[]
pets_new=[]
towns_new=[]

def new_lists(): # I cant find a way to get data from internet automatically so I have coded it by my own

    towns=["godville","simpletown","bumchester","last resort","next station","beerburgh","heisenburg",
       "healiopolis","monsterdam","trollbridge","herowin","los demonos","el herado","unsettlement",
       "tradeburg","quirkytown","los adminos","nothingham","bosswell","san satanos","egopolis",
       "godvillewood","herolympus","dogville","anville","monstro city","bad gateway","deville",
       "lostway","unspecifiedistan","dessertown","herostan","newland"]

    global artifacts_new
    global monsters_new
    global equipments_new
    global skills_new
    global pets_new
    global towns_new




    def düzenle(liste):

        new=[]

        for kelime in liste:

            kelime=str(kelime)

            kelime=kelime.replace("-"," ")

            kelime=kelime.upper()

            new.append(kelime)

        return new




    for i in düzenle(artifacts):

        artifacts_new.append(i)



    for i in düzenle(monsters):

        monsters_new.append(i)



    for i in düzenle(equipments):

        equipments_new.append(i)



    for i in düzenle(skills):

        skills_new.append(i)



    for i in düzenle(pets):

        pets_new.append(i)



    for i in düzenle(towns):

        towns_new.append(i)


#new_lists()
#%%

class Godville_Database():

    def __init__(self,isim):

        self.isim=isim
        self.create_connection() # initianlize function

    def create_connection(self):

        self.con = _sqlite3.connect("Godville_v2.db")
        self.cursor = self.con.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS {}(Items TEXT)".format(self.isim))
        self.con.commit()

    def cut_connection(self):
        self.con.close()

    def Add_items(self,item):

        item=str(item)
        item=item.upper()

        self.cursor.execute("INSERT INTO {} VALUES(?)".format(self.isim),(item,))
        self.con.commit()

    def Search_items(self,word_parts):

        self.cursor.execute("Select Items From {}".format(self.isim))
        items = self.cursor.fetchall()

        if len(items)==0:
            print("There is nothing in database")

        else:
            for item in items:
                if word_parts in item[0]:

                    itm=str(item[0])
                    print(itm)


#create tables in Godville_v2 Database
tbl_Artifacts=Godville_Database("Artifacts")
tbl_Monsters=Godville_Database("Monsters")
tbl_Equipments=Godville_Database("Equipments")
tbl_Skills=Godville_Database("Skills")
tbl_Pets=Godville_Database("Pets")
tbl_Towns=Godville_Database("Towns")

#%% Adding items into tables

def add():
    for i in artifacts_new:

        tbl_Artifacts.Add_items(i)

    for i in monsters_new:

        tbl_Monsters.Add_items(i)

    for i in equipments_new:

        tbl_Equipments.Add_items(i)

    for i in skills_new:

        tbl_Skills.Add_items(i)

    for i in pets_new:

        tbl_Pets.Add_items(i)

    for i in towns_new:

        tbl_Towns.Add_items(i)

#add()
#%%


def ara():
    while True:

        try:

            print("""
                  0-Çıkış
                  1-Artifacts'lar içinde ara
                  2-Monsters'lar içinde ara
                  3-Equipments'lar içinde ara
                  4-Skills'ler içinde ara
                  5-Pets'ler içinde ara
                  6-Towns'lar içinde ara
                  """)

            seçim=int(input("Bir işlem seçiniz: "))

            if seçim==0:
                print("Yine Bekleriz.")
                break

            elif seçim==1:

                print("Artifacts'lar içinden arama yapacaksınız...\n\n")
                harfler_boşluklar=str(input("Verilen bir tri-gramı ya da di-gramı Giriniz: "))

                harfler_boşluklar=harfler_boşluklar.upper()

                tbl_Artifacts.Search_items(harfler_boşluklar)

            elif seçim==2:

                print("Monsters'lar içinden arama yapacaksınız...\n\n")
                harfler_boşluklar=str(input("Verilen bir tri-gramı ya da di-gramı Giriniz: "))

                harfler_boşluklar=harfler_boşluklar.upper()
                tbl_Monsters.Search_items(harfler_boşluklar)


            elif seçim==3:

                print("Equipments'lar içinden arama yapacaksınız...\n\n")
                harfler_boşluklar=str(input("Verilen bir tri-gramı ya da di-gramı Giriniz: "))

                harfler_boşluklar=harfler_boşluklar.upper()
                tbl_Equipments.Search_items(harfler_boşluklar)

            elif seçim==4:

                print("Skills'ler içinden arama yapacaksınız...\n\n")
                harfler_boşluklar=str(input("Verilen bir tri-gramı ya da di-gramı Giriniz: "))

                harfler_boşluklar=harfler_boşluklar.upper()
                tbl_Skills.Search_items(harfler_boşluklar)


            elif seçim==5:

                print("Pets'ler içinden arama yapacaksınız...\n\n")
                harfler_boşluklar=str(input("Verilen bir tri-gramı ya da di-gramı Giriniz: "))

                harfler_boşluklar=harfler_boşluklar.upper()
                tbl_Pets.Search_items(harfler_boşluklar)

            elif seçim==6:

                print("Towns'lar içinden arama yapacaksınız...\n\n")
                harfler_boşluklar=str(input("Verilen bir tri-gramı ya da di-gramı Giriniz: "))

                harfler_boşluklar=harfler_boşluklar.upper()
                tbl_Towns.Search_items(harfler_boşluklar)

            else:
                print("Böyle bir işlem yoktur.")

        except ValueError:
            print("Yanlızca Sayı girebilirsiniz.")


#%%

ara()




#%%





#%%
