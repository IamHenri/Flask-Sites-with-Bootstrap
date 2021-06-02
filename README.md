# Flask-Sites-with-Bootstrap

I really like flask. But I think its use may be improved with Bootstrap. Which I try to demonstrate here. There are obviously a lot of other way to do things I do here, and certainly more elegant. Anyway, the point is to provide a way of making websites with Flask and bootstrap. 

Here you'll find some sets of scripts to build sites with Flask and Bootstrap. For every directory you'll download / clone / copy or whatever, you have to run these two commands to run your site : 

export FLASK_APP=app.py

flask run

visit https://127.0.0.1:5000 and be amazed. 

# First directory 

**01 - One page bootstrap** - Contains twwo file : index.html in the templates directory and the app.py. 

Dowload the content if '01 - One page bootstrap' and in a terminal execute commands above. 

The simplest Bootstrap page with Flask. 

# Second directory 

This second directory lets you use a web site with several pages. A big step has been made.

**02 - Three pages web site Flask + Bootstrap** contains the app.py script to run and in templates you have three files : the website three pages. 

In the navigation bar you have to have variables in the links (the href). If you type the actual relative path, you'll see that your navigation is not optimal. Try it if you  don't beleive me. 

**Nota Bene** : this code is not oprimal. In each page you have the same navigation bar. If you want to update it, you'll have to make it three times. Which is stupid. So the next directory will correct this coding error. 

# Third directory

It is the same as the second one, but with the code optimization about the nav bar. And and the repeated code. 

**03 - N pages website with Flask + Bootstrap + Jinja2** - app.py is the same. The main update is in the templates folder. The main file is base.html, which contains all the stuff which is allways needed / displayed for a web page. And then you hav index.html, apropos.html and contact.html in which you'll find only the content of the page. 

A more elegant way to built a web site using bootstrap than before. Maybe not the best, but quite easy to install and update. 

# Fourth directory
**04 - Flask + Bootstrap + basic Form** : in this directory, the app.py file has three pages : the index : / ; the a propos page, a static page and the result page named resultat.html. This last page doesn't appear in the menu. You only get it when you validate the form. Careful if used on a site in production there is no protection against the data the user main give in the form! 


This form is inspired from here : https://pixees.fr/informatiquelycee/n_site/nsi_prem_flask.html 


# Fifth directory
**05 - form to calculate stuff in flask and Bootstrap** : this directory lets you manage a web site with a form on the homepage, and a dedicated page for the results. all the calculation is made in app.py. The text shown in the result page could be optimized using Jinja2 with conditions etc. The point of these scripts are to providfe a form which makes calculus and giv a conditional result. 


This form helps you calculate the time spent on an activity you would have done during years, every day. The result is the whole time spent. 

# NEVER
Never use these sources for a production site as they are. You must modify the debug parameter to FALSE. 

