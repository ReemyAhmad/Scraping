import requests 
from bs4 import BeautifulSoup
import csv


#from website yallakoura
#get date
date = input("Plz enter date like MM/DD//YY : ")
# get page 
page = requests.get(f"https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date={date}")

def main(page):

    src=page.content         # to get all code in page 
    soup=BeautifulSoup(src,'lxml')
    championships=soup.find_all('div',{'class':'matchCard'})
    matches_details=[]           # to store details about every matches like dictionary
    def get_matches_info(champ):
                                                            #title of championship
        championship_title=champ.find('div',{'class':'title'}).find('h2').text.strip()
                                                            #get all matches
        all_matches=champ.find('ul').find_all('li')
        # number of matches
        num_of_allMatch=len(all_matches)
        #loop to get details for every matches 
        for i in range(num_of_allMatch):
            #name team A
            team_A=all_matches[i].find('div',{'class':'teamA'}).text.strip() 
            #name team B
            team_B=all_matches[i].find('div',{'class':'teamB'}).text.strip()
            #get score
            resulte =all_matches[i].find('div',{'class':'MResult'}).find_all('span',{'class':'score'})
            score = f'{resulte[0].text.strip()} - {resulte[1].text.strip()}'
            #get match time 
            time=all_matches[i].find('div',{'class':'MResult'}).find('span',{'class':'time'}).text.strip()
            #adding matches to info matches 
            matches_details.append({
                'اسم البطولة': championship_title
                ,'الفريق الاول':team_A
                ,'لفريق الثانيh':team_B
                ,'النتيجة':score
                ,'التوقيت':time
            })

    # to pass all championships
    for i in range(len(championships)):
        get_matches_info(championships[i])
    
    keys = matches_details[0].keys()
    with open ('match.csv','w',encoding='utf-8') as output_file :
        dict_writer=csv.DictWriter(output_file,keys)                # create object dict_writer ... from class Dictwriter
        dict_writer.writeheader()                # write key in header of table
        dict_writer.writerows(matches_details)
        print('file create')


main(page)


