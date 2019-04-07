# G.I.S.A.

[![Built with ❤](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com/#)

[![made with &hearts in Python](https://img.shields.io/badge/made%20with%20%E2%9D%A4%20in-Python-red.svg)](http://shields.io/#your-badge)

### List of contents

- [What is G.I.S.A.?](#what-is-g.i.s.a.?)
- [Installation](#installation)
- [Contributing](#contributing)

### What is G.I.S.A.?

G.I.S.A. - Gender Identification and Sentimental Analysis is a web application made on [Django](https://www.djangoproject.com/). Basically, a block of text is to be entered in the text box. It gives the output of Sentimental Analysis classified into three parts: positive, negative and neutral. It also identifies the gender of the person by whom the text is written and tells us whether it is mail or female. Both of these is done using Naive Bayes Classifier of [NLTK](https://www.nltk.org/). Presently a lot of applications are available for Sentimental Analysis and Gender Identification, but most of them are either voice based or based on facial features. G.I.S.A. is a text based system, so we just need a block of text written by the person we want to perform analysis on.

#### Why G.I.S.A.?

- Imagine you are not able to decide which book to buy, or which movie to watch. You can simply perform Sentimental Analysis and get out of your confusion within minutes.
- As the use of social media is increasing exponetially, so is the need for online security. We have heard a lot of cases of fake accounts which at first does not seem much of a problem, but with time, it has led to some serious issues. Here's when Gender Identification comes into picture. It does not completely identifies whether the account is fake or not, but atleast we can be 50% sure by knowing the gender.

### Installation

- The very first step is to install git on your PC. CLick [here](https://www.linode.com/docs/development/version-control/how-to-install-git-on-linux-mac-and-windows/) to know how.
- Now you need to fork this repository and clone it in your system by using `git clone https://github.com/<your_username>/G.I.S.A.`
- As this is a web application on Django frame work of Python, Django also needs to be installed. `pip3 install django==2.1.7` will do the work.
- Now open the terminal(or command prompt), navigate to the cloned repository and give this command: `python3 manage.py runserver`

You will see the following:
````
hetal@hetal-HP-Pavilion-Notebook:~/Desktop/GISA$ python3 manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
April 07, 2019 - 09:05:25
Django version 2.1.7, using settings 'GISA.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
````
Now you are ready to go!

### Contributing

Check out the issues if you can solve them. If not, any new feature or a bug fix is great!
