# Google Trends Scraper
The functionality represents the scraper job interface to interact with [Google Trends service](https://trends.google.com/trends/?geo=HU). 
The job can be parametrized to be invoked each `N hours`. (by default - 4 hours).

# Description
Current interface covers following aspects:
1. Validation of input arguments
2. Validation of input csv file (including emptiness of csv, etc)
3. Abstraction on top of PyTrends API
4. Writing results on local machine within LocalDriver interface  

## Sample invocation
```bash
$ python -m google_trends_scraper.main --input-path /../top-search-keywords.csv 
                                       --output-path /../data-material/output/
                                       --start-year 2022
                                       --end-year 2022
                                       --start-month 5
                                       --end-month 5
                                       --start-day 1
                                       --end-day 1
                                       --start-hour 0  
```

## Sample Output
`file_name: 2022-05-01_20:58:28.329192_toy_sample_search_interest_score.csv`
```bash
date,ncis,blue bloods,yellowstone,jeopardy,mark harmon,elvis presley,john wayne,andy griffith,tom selleck,ncis los angeles,alex trebek,pat sajak,happy days,law & order,wheel fortune,blake shelton,cole hauser,ken jennings,duck dynasty,donnie wahlberg,alaskan bush people,lucille ball,sam elliott,country music,brady bunch,olympics,sadie robertson,law & order svu,little house prairie,ncis new orleans,judy norton,eric christian olsen,gwen stefani,kevin costner,ron howard,american pickers,I love lucy,dolly parton,frank fritz,guest host,michael landon,tim allen,daniela ruah,carrie underwood,henry winkler,man standing,john dutton,beverly hillbillies,priscilla presley,korie robertson,graceland,gilligan island,mariska hargitay,alan jackson,bridget moynahan,rip wheeler,ncis hawai,beth dutton,tim mcgraw,simone biles,vanna white,melissa gilbert,clint eastwood,riley keough,mayim bialik,garth brooks,tokyo olympics,deadliest catch,nick mcglashan,alan alda,emily wickersham,sadie robertson huff,buzzy cohen,ree drummond,kelly clarkson,levar burton,golden girls,reba mcentire,mike wolfe,aaron rodgers,faith hill,george strait,jamie dutton,duck dynasty star,phil robertson,kelly reilly,pioneer woman,desi arnaz,nascar,candace cameron bure,miranda lambert,taylor sheridan,paige spiranac,dukes hazzard,team usa,jenny mccarthy,bloods star,matthew mcconaughey,danny reagan,lucie arnaz
2022-05-01 00:00:00,30,17,92,34,3,39,100,6,10,3,25,20,73,30,88,48,17,16,17,14,1,4,5,41,4,82,1,3,14,7,1,1,29,100,10,4,7,100,0,1,2,5,1,18,4,59,14,75,59,1,52,3,70,92,15,3,0,11,100,21,15,6,100,2,29,100,2,12,0,2,3,1,0,14,66,9,89,59,2,92,14,100,1,0,1,0,2,0,20,1,12,2,3,4,3,31,1,92,1,3
2022-05-01 01:00:00,34,18,100,31,3,39,88,5,11,3,19,10,90,30,80,52,17,14,17,15,1,5,7,40,4,89,3,2,15,9,1,1,28,99,12,4,8,62,0,1,3,7,1,19,6,73,19,97,49,0,50,4,73,100,15,2,1,15,96,17,8,6,90,3,31,94,2,10,0,2,3,0,0,11,65,14,97,57,3,100,16,86,1,0,2,0,2,0,16,1,12,3,3,5,4,26,1,100,1,3
2022-05-01 02:00:00,32,16,92,32,3,38,88,5,10,3,29,21,80,26,100,53,15,15,16,15,1,4,6,36,4,89,3,2,15,9,1,1,28,96,12,3,8,61,0,2,2,5,0,19,5,74,16,90,58,0,47,3,55,90,16,3,0,13,98,22,16,5,84,4,38,94,3,10,0,3,1,0,0,12,69,14,95,55,2,96,14,62,1,0,2,0,1,0,13,1,12,3,3,4,3,32,0,98,1,2
2022-05-01 03:00:00,28,12,83,20,3,34,76,5,9,3,23,9,72,26,70,44,11,13,16,13,0,4,5,31,3,100,2,2,12,5,1,0,26,80,13,2,7,50,0,3,2,5,1,17,5,75,17,83,54,2,46,2,51,78,15,2,0,10,85,15,7,4,84,3,22,89,4,9,0,2,2,0,0,6,60,9,87,53,1,85,13,55,2,0,1,0,1,0,11,1,9,2,3,4,3,26,1,96,0,4
2022-05-01 04:00:00,22,9,60,14,2,28,59,3,6,2,21,7,60,25,68,33,11,11,13,10,1,3,4,23,3,92,2,2,10,5,0,1,22,67,10,2,7,40,0,2,2,4,0,16,3,82,12,45,49,0,34,1,52,63,11,2,0,10,69,15,6,4,55,4,13,87,4,8,0,2,3,0,0,6,61,8,98,37,2,65,14,43,1,0,1,0,1,0,9,0,7,2,2,3,3,24,0,75,1,2
```


## Further Workaround
1. Tests-tests-tests
2. More involved investigations of PyTrends API and covering various response situations (lack of docs)
3. Include more input/output data validations 
4. Potential custom changes within output data format (see models.output) 