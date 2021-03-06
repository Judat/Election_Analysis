# Written Analysis of Election Audit

## Overview of Election Audit 
The election audit was done to get meaningful insight of the election data. The important information that we retreived from the election data is :

 * Total number of votes casted
 * A complete list of candidates who received votes
 * Total number of votes each candidate received
 * Percentage of votes for each candidate
 * The winner of the election based on popular vote
 * The number of votes casted in each county
 * The percentage of votes casted in each county
 * County with largest turnout of votes
 
 ## Resources
 Data Source : Election Results .csv
 Python 3.8.8
 
 ## Election Audit Results 
 The analysis of the election results shows that :
* ### Total number of votes casted
  * A total of 369,711 number of votes were casted in the election ( folloiwng is the code used to calculate total votes)
  ![Vote Count](https://user-images.githubusercontent.com/93050682/142705526-7f2c350e-d0d2-4eeb-a234-1f1545a829c4.PNG)
* ### Countywise Break down 
  * Jefferson had a turnout of 38,855 votes which is 10.5%  of the total votes casted
  * Denver had a turn out  306,055 votes which is 82.8%  of the total votes casted
  * Arapahoe had a turnout 24,801 which is only 6.7% of the total cotes in the precinct 
* ### County with largest turnout
  * Denver had the largest number of votes tournout with 82.8% of total votes.
* ### Canditatewise Break down 
  * Charles Casper Stockham: 23.0% (85,213)
  * Diana DeGette: 73.8% (272,892)
  * Raymon Anthony Doane: 3.1% (11,606)
* ### Winning Candidate Summary
  * Diana DeGette
  * Vote Count: 272,892
  * Percentage: 73.8% of total vote ( folloiwng is the code used to calculate winning candidate )
  ![winner candidate](https://user-images.githubusercontent.com/93050682/142705608-810d1634-39b6-4f47-bbb9-fd900b7702e9.PNG)
  
## Election Audit Summary
This scipt is written very comprehensively keeping inmind that if needed it cover a larger amount of data, more candidates , more counties and increased number of votes casted. 
All you need to do is make a few cahnges to run the code smoothly. 
* 1: You might have to update the path to read the csv file which has the election data of 1 or more precincnts. 
![Modification 1](https://user-images.githubusercontent.com/93050682/142706591-bedf3330-9fbe-4d4e-b341-e5fabe547f82.PNG)

* 2: you need to cgange the index refernce as per the columns of the avaialable dat . in out case the candiate names wer in column 3 so we used the row[index] accordingly.
![Modification 2](https://user-images.githubusercontent.com/93050682/142706713-fa009d26-1d30-4cd5-9b88-5f39aed5c40e.PNG)
Hope this analsysis and code is useful for future election analysis.
thank you

