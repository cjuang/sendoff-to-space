# Design for Sendoff to Space

The basis of the website is designed from CS50 Finance, problem set 8. The website has a Python backend and a HTML, CSS, and Jinja frontend. 
It has been designed in Chrome browsers. The "Write a Message" page is mobile-optimized using Bootstrap, but the main page is not. Both 
pages use Bootstrap for design.

# Python

## application.py - index, website scraping
The backend application.py uses Python 3, Flask, and SQL. It also requires the Python libraries `lxml` and `requests`.

A summary of features
- 'messages' SQL table to hold messages, detailed in `write` in `application.py`
- a form in `write.html` to enable users to insert messages into 'messages'
- display of launch information and previously-submitted messages in `main.html`, scraped using `lxml` and `requests` (detailed in `application.py`)
- other commented-out features

The first part of the code configures `messages.db`, the SQL database used to store the messages that people write on the website to 
spacecrafts. A commented-out part of code that follows is a method of deleting messages older than 30 days; however, the code did not 
recognize `GetDate()` as a function. The code is credited to: http://zarez.net/?p=542.

`@app.route("/")` and `index` build the main page of the website. In order to supply information abou the next launch, the launch date, 
time, name of the mission, and location of the launch were scraped from SpaceflightNow's Launch Schedule webpage 
(http://spaceflightnow.com/launch-schedule/). The website's HTML is structured so that the information I wanted to scrape is 
contained in `div` and `span` classes.

Only the first elements of the schedule were taken instead of the entire list of future 
launches, as defined by
```
launch_date = scrape_date[0]
launch_time = scrape_timeloc[0]
launch_loc = scrape_timeloc[1]
launch_name = satname(scrape_name[0])
```
The function `satname` will be explained in the following section. After scraping for information, the messages in SQL Table "messages" 
are loaded and returned along with the launch information.

Credit for website scraping belongs to http://docs.python-guide.org/en/latest/scenarios/scrape/.

## helpers.py
The `satname` function is used to take the satellite name out of a string from SpaceflightNow. When the website is scraped, 
```
tree.xpath('//span[@class="mission"]/text()')
```
returns a string that contains both the rocket and satellite names, e.g. `'Vega • Gokturk 1'`. I wanted to display only the satellite 
name, so I used `split()` and `strip()` built-in functions to divide each name and the bullet point separating them into elements of an 
array, then removed spaces surrounding the characters. The resulting satellite name is returned.

There is a `lookup` function commented-out, which was a function to look up articles for a satellite using Google News, similar to the 
Google News API used in Problem Set 9, Mashup. However, I was faced with the challenge of my lookup function returning nothing. I suspect
it is because some mission names use special characters that the SpaceflightNow website does not use, making it harder to find relevant 
articles. The code also needs to be modified more so that it does not search for geolocations. The other part of the in-progress code can 
be found in `application.py`, under the `@app.route("/articles").

# application.py - write a message
`@app.route("/write")` uses `POST` and `GET` methods for a form submission. Contents of the form are stored in the SQL table 'messages'. 
`POST` renders the layout `write.html`, which allows visitors to input their name, the name of the mission, and a message to the departing 
spacecraft. Upon submission, the contents of the form are appended to the 'messages' table. The user is then redirected to the 
main page, where a message will flash that they have successfully sent a message. They can also view their new message on the table displayed 
on `main.html`.

# HTML Templates and CSS

## layout.html
The main template is mostly adopted from CS50 Finance. The changes made were the Bootstrap theme, changes to the titles displayed, and 
changes to the main menu links.

Jinja is used to keep a consistent layout to all the pages. The main menu at the top is detailed in this section, and every other layout is an 
extension to `layout.html` so all other pages will all have the same main menu at the top.

## main.html
The layout for `main.html` is built using Twitter Bootstrap. Bootstrap containers are used to make rows and columns on the webpage that 
helps divide the content into different lengths. 

In the top row, the left-hand side was chosen to display all the information 
about mission name and mission launch date and time. 

On the right side of the row is the table listing all of the messages made by visitors. 
A few examples have been inserted by accessing the SQL table directly or by using the online form to submit. The table was designed 
deliberately to display the most recent messages at the top, using Python in `application.py` and SQL to reorder to table by `id`. The 
code to order is below:
```
messages_history = db.execute("SELECT msg_from, msg_to, msg_msg, msg_date FROM messages ORDER BY id DESC")
```
Using `ORDER BY id DESC` orders the entire table in descending order by id number, which is auto-incrementing. This makes the website 
significantly more user-friendly because people do not need to scroll to reach the most recent messages.

To add information to the table, Jinja is used to iterate through each row from the 'messages' SQL table returned from `application.py` 
and print the row's From, To, Message, and Date Sent. The code used is here:
```
<div id="msgcontent">
{% for row in messages %}
<tr>
    <td>{{ row.msg_from }}</td>
    <td>{{ row.msg_to }}</td>
    <td>{{ row.msg_msg }}</td>
    <td>{{ row.msg_date }}</td>
</tr>
{% endfor %}
```
At the bottom of `main.html`, a small 'About' section is added to explain the purpose of the website.

## write.html
`write.html` contains the frontend form that is displayed so that users can input their messages into the 'messages' SQL table. The 
table has labels for each box and an example of what to write in the `placeholder`. When first loading the page, there is `autofocus` 
on the first input box so users can immediately begin typing. Submitting the form will run the `POST` method of the `write` function in 
`application.py`, and redirect the user to `main.html`.

## styles.css
CSS was used minimally to help with aligning text in containers and forms.

The table on `main.html` has been formatted in `styles.css` to have a scrollbar and a fixed height, credits to 
http://stackoverflow.com/questions/21017769/table-with-fixed-height-and-header-and-colum-width-with-bootstrap-3. Fixed height is 
necessary so that the rows of the table do not become too long and diminish user-interactivity.

# Further Questions
Send any questions to Caroline Juang at carolinejuang@gmail.com.
