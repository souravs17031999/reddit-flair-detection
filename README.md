# reddit-flair-detection
The following repo contains scripts detecting flairs from reddit posts with real time hosted flask server.

# Project Objective: 
The objectives of this task is divided into five parts :   
* Part - I : Collecting and Building Reddit data
* Part - II : Exploratory Data Analysis for Collected data
* Part - III : Processing and Modelling using various Algorithms
* Part - IV : Building WEB-APP
* Part - V : Deploying WEB-APP on Heroku

# Approach :     
* I first collected and builded Reddit India data by Scraping data using three methods :     
  1. Using [requests](https://requests.readthedocs.io/en/master/) module  
  2. Using [PRAW](https://praw.readthedocs.io/en/latest/) wrapper module      
  3. Using [PushShift](https://github.com/pushshift/api) wrapper module        
  
* [Sample of data] :  
![df1](/images/data_1.JPG)      
![df2](/images/data_2.JPG)     


* Then i build my Data Intuition around the collected data analysing last four months data - Jan, Feb, Mar, Apr 2020 and digging various points out of them using various charts.    
* Then, analyszing comments of various threads , average intuitions.     
* Some of the samples of various charts and graphs are shown below :  

* January data :     

![df2](/images/jan.JPG)      

![df2](/images/jan_cloud.JPG)       

* February data : 

![df2](/images/feb.JPG)        

![df2](/images/feb_cloud.JPG)         

* March data

![df2](/images/mar.JPG)           

![df2](/images/mar_cloud.JPG)          

* April data     

![df2](/images/april.JPG)        

![df2](/images/apr_cloud.JPG)   

* Frequency of words occuring more often :       

![df2](/images/freq_words.JPG)      

* Comments sentiments :      

![df2](/images/comments_senti.JPG)         

* Comments polarity :   

![df2](/images/comments_polar.JPG)          

* After that , i processed the text data using following  : 
1. Applied [CountVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html)
2. Applied [TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)
3. Constructed a Pipeline in scikit-learn for training and testing algorithms.

* After that analyszed cross validated scores on testing samples :     

![df2](/images/models.JPG)                

* Build the webapp and created API for testing on POST request.   
Ex.  
```
files = {'upload_file': open('file.txt','rb')}
r = requests.post('http://flair-reddit-predict.herokuapp.com/automated_testing', files=files)
```

* Now deployment of WEB-APP               

### Real time Flask server hosted on Heroku:      
* Log on to following URL hosted on pythonanywhere.com using flask server :    

## [LIVE WEBSITE](https://flair-reddit-predict.herokuapp.com/)    

# Getting started :     
### FLASK solution : 
* Run the cmd (terminal).     
* Download the project files using following command in the directory from where you need to run the script :       
```  
git clone https://github.com/souravs17031999/reddit-flair-detection   
```      
* Move to the project main directory where the project is downloaded.
* Move to directory ```reddit_app```.  
* Now run following :     
(for windows)     
> set FLASK_APP=app.py    
> python -m flask run       

(for other termials)          

> $ export FLASK_APP=object.py      
> $ flask run       

[Other troubleshooting issues related to flask server](https://flask.palletsprojects.com/en/1.1.x/quickstart/#what-to-do-if-the-server-does-not-start)    

* Now the local server should start, log on to : [local url port] shown on terminal.     
(Most probably it will be http://127.0.0.1:5000/ , or maybe any other port)          

# Navigating Project Directory : 
* File containing Data collection and building - [Notebook1](https://github.com/souravs17031999/reddit-flair-detection/blob/master/REDDIT_PART_1.ipynb)     
* File containing EDA - [Notebook2](https://github.com/souravs17031999/reddit-flair-detection/blob/master/REDDIT_PART_2.ipynb)    
* File containing Modelling - [Notebook3](https://github.com/souravs17031999/reddit-flair-detection/blob/master/REDDIT_PART_3.ipynb)    
* Scripts for Flask APP - [WebApp](https://github.com/souravs17031999/reddit-flair-detection/tree/master/reddit_app)   
* Training Data - [Data](https://github.com/souravs17031999/reddit-flair-detection/blob/master/reddit_india_classifier_combined_data.csv)    
* Other data for analysing - [OtherData](https://github.com/souravs17031999/reddit-flair-detection/tree/master/Other%20data)     
* Pre-trained Model - [Model](https://github.com/souravs17031999/reddit-flair-detection/blob/master/reddit_app/model.pkl)     

# Sample runs with outputs :     

      
