# Time Trader

This is a little python-based web app built with flask and meant to be deployed with OpenShift.

It allows people to ask for help, such as dog wlking for a shelter, volunteering at a fundtion for a good cause, or helping to distribute meals for homeless people.

On the other hand it will ask you a couple of basic things, such as physical fitness, and then show you possibilities for investing some of your free time for a good cause.

## Deelopment setup

* clone or copy the files in this repo
* make sure you have Python 3.5 or above
* (optional) create a virtual env
* do `pip install -r requirements.txt`
* run `python3 app.py`

## OpenShift setup

* install and setup Docker and OpenShift/oc
* after running `oc cluster up` navgiate to the gui and log in
* create a new project with python and give it the URL of this repo
* builde
* enjoy!
