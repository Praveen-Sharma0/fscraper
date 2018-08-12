# ScrapeWeb

The project is written in Python 2.7 , and is still a test-version . A more optimized and extended version of the scraper is planned to be released in coming days .

# Prereqisite Softwares required  (#Windows) :
      1)Python 2.7
      2)Anaconda
      3)Scrapy 
 
# Folder Structure
      fscraper/
      |-----fscraper
      |      |-- spiders
      |      |      |-- __pycache__ /
      |      |      |-- __init__.py
      |      |      |-- monsterbot.py
      |      |
      |      |-- __pycache__/
      |      |
      |      |-- __init__.py
      |      |-- items.py
      |      |-- middlewares.py
      |      |-- pipelines.py
      |      |-- settings.py
      |
      |
      |-- monster.json
      |-- scrapy.cfg
    
 
# Instructions to Execute

1) Run "Anaconda terminal"

2) Clone the repository & move the root folder "fscraper" to the location at which terminal is opened , change the directory to fscraper
      For Ex : If the terminal location is "C:/Users/(YourName)" , then Copy "fscraper" to folder "YourName" , 
               change directory to "fscraper" using : cd fscraper
  
3) Use : "scrapy crawl monsterbot" to crawl the page


Once Done , the result data is stored in  "monster.json"

# Limitations
 The script is only able to scrape the first page , Im working onto fix this 
   
