# AllergyAlarm

To run commands, you need a terminal open in the outermost ALLERGYALARM folder. In VSCode, there's a terminal tab at the top to start one.
If you need local test data, run the command "python resetDatabase.py". If you already have local data saved, this will erase it.
To start server locally (see the website), run "python manage.py runserver", then control click the http link in the terminal.
runall.py contains some other occasionally necessary commands, like collecting css files in the proper place, changing SQL tables, and ensuring our superuser exists. Can just run that when needed.

SQL is used for our database - django has custom syntax for managing it
chart.js is used for plotting (a javascript library)
I have bleak code snippets in here as examples of reading bluetooth data. We might use pybluez code though.

urls.py defines our webpages and their corresponding views
Views are functions in views.py that contain python/django code. html templates contain html, css, and javascript code.
Each html page (in templates) has a view in views.py and a url in urls.py. There is additionally a view, chart_data, which returns a json file rather than an html page, and it is used by chart.html to read data from our SQL database each time data is plotted.



Tasks left to complete:

Users/Data:
Need user account creation page, accessible from log-in page.
Ensure user authentication is required on all pages (for our convenience, it's currently on none of them)
Plotting data still does it for all users
Additional steps to secure data? Not sure exactly how to do this.

Plotting:
Buttons aren't in fancy bootstrap font.
Need to average data if there's too many points - let's say 500 per plot, max
Need x-axis to start at beginning of specified time frame rather than the earliest point
Gyroscope and Accelerometer data should probably have a magnitude column. Right now I'm just plotting the x.

Transmission:
We need to get data onto here. Bleak or pybluez. text/sensors.txt contains notes on our sensor data from their datasheets.
Each sensor will need its binary decoded into the correct format, then inserted into table. Datetime read at this point. Location read at some point?
We still need to move this project onto a web server. This means code to transmit from laptop to web server then back. Ideally, this would be most convenient with a phone, but I don't think we're going to get to that.

Interpretation:
Save user-specific data, like resting heart rate, average temperature, and location (ethical guidelines with location tracking?). Might have a page to ask them for this stuff.
Calculate intermediary data, such as time spent outside (from temperature)
We could probably interface with weather APIs to get temps in the area
Interface with pollen databases - may not be possible, they seem to overcharge. Super useful though if we can.
Warnings for high pollen coming up
Alerts for abnormal data, such as high heart rates or falls
