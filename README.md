![Screenshot of webpage](https://github.com/cjuang/sendoff-to-space/blob/master/screenshot.PNG?raw=true "Main page")

# Sendoff to Space

Welcome to Sendoff to Space, a small website that informs visitors of the next launch to space and gives them the opportunity to write 
a small message to the spacecraft. All messages are posted on this site for everyone to view.

The backend of the website is coded in Python, SQL, and Flask. The frontend uses HTML, CSS, and Jinja. Twitter Bootstrap was used for formatting.

This website was created by Caroline Juang for an Intro to Computer Programming class at Harvard University, December 2016. Send all questions to carolinejuang@gmail.com.

Video link: https://youtu.be/tpi-F1knv84

# Vision
In 2015 alone, a total of 87 orbital rockets were launched worldwide into space. This number is likely to continue to grow in both 
the public and private sectors as it has been in the past several years as more countries enter the space market. On average there 
is something on a mission to exit the Earth’s atmosphere roughly every four days. It's exciting that so many satellites/spacecrafts 
launch frequently; Sendoff to Space is designed to channel that excitement in a single location by giving people a platform to express
themselves directly* to the spacecrafts that are flying up.

*the spacecrafts will not actually receive the message, unless they visit this website

# Website Features
- View the date, name of mission, launch time, and launch location of the next mission to space
- Write a message to the departing spacecraft
- View all messages written to the spacecraft and to previous launches

# Requirements
When running this website, the lxml and requests libraries are necessary. Use the following commands to install:
```
sudo pip3 install lxml
sudo pip3 install requests
```
# Running the Website in CS50 IDE

Change directories if necessary by running `cd (directoryname)` in the command prompt, where (directoryname) is the folder containing 
all of the files.

After installing the required libraries, run `flask run` in the command prompt to view the Web Server.

See the SQL table of written notes from users by running `phpliteadmin messages.db` in the command prompt.

The website should be set-up and available for use. Try inputting a message by clicking the "Write a Message" tab in the menu bar. When 
you click on the "Send" button, the website will redirect you to the main page. Your new message will appear at the top of the table. 

![Screenshot of webpage](https://github.com/cjuang/sendoff-to-space/blob/master/screenshot2.PNG?raw=true "Write a Message")

# Features to Implement in the Future to Strengthen the Website
Below are ideas that I would have liked to implement for this project, but did not due to time constraints. You can find some beginnings 
of code for these ideas commented-out throughout application.py and helpers.py.

- Maximum string lengths for the To, From, and Message form inputs
- Prevent the from from submitting if there is nothing entered in the form
- Delete messages older than 30 days from the SQL table
- Google newsfeed to alert visitors about current launch information
- Wikipedia summary of the launch

# Questions and Answers

##### When will the page reload when the next launch will be?
The page will refresh the next launch when a user reloads the page. The website is scraped every single time the `index` function is 
called in `application.py`.

##### What website does the launch information come from?
Currently, the website automatically scrapes data from http://spaceflightnow.com/launch-schedule/ to give you the most current launch. 

##### On the home page, where do the messages come from?
The messages are read from a SQL table named `messages` on a database named `messages`. They are not taken from outside websites.
