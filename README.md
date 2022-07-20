# IND Appointment checker

This is a script to help people in The Netherlands to make an appointment with IND. It will constantly check for free slots in the calendar and notify you when a free slot is available.

**Stack:**

* `Python 3.8+`
* `requests 2.28.0`
* `pywhatkit 5.3`
* `python-dotenv 0.20.0`

#### Why is it there

People wjo deal with IND in The Netherlands always have problems making an early appointment, since it's always busy and they end up making an appointment for like 3 months later. So they either need to refresh the calendar on a web browser constantly to see if anyone has cancelled his/her appointment or use some script to automate the check for them. Hence, this project.

## How does it work

It's a simple script which runs in a shell and in case of finding an available slot in the desired date for the user, will notify the user in the shell by printing a long line of `*` and also is able to send a Whatsapp message to a provided number.

## Getting started

Since maybe people with less or no knowledge about programming try to use it, I'll try to explain with more details.

The first things which need to be installed are `Python3` and `virtualenv`.

To install `python3` check [this great tutorial](https://realpython.com/installing-python/)

After installing `python`, try installing `virtualenv`. Below is explained how to install it in different operating systems.

#### Ubuntu
```commandline
  sudo apt-get update
  sudo apt-get -y upgrade
  sudo apt-get -y install python-virtualenv
```
  
#### MacOS
```commandline
easy_install virtualenv
```

#### Windows
In a command line: [Here's how to open a command line in windows](https://www.howtogeek.com/235101/10-ways-to-open-the-command-prompt-in-windows-10/)
```commandline
pip install virtualenv
```

### Installing Git

The next step is to install `Git` to be able to clone this repository in your local machine. So check [this tutorial](https://www.atlassian.com/git/tutorials/install-git) which explains how to install it in your OS.

### Clone this repository

After installing everything you need, it's time to clone this repository in your local machine. in order to do that, run this command in your terminal (command line):
```commandline
git clone https://github.com/alexjolig/ind_appointment_checker.git
```

Make sure you know where you're cloning this because then you need to change your current directory to the cloned folder:
```commandline
cd path/to/ind_appointment_checker
```

Now you need create a virtual environment in this folder:
```commandline
virtualenv venv
```

Then you need to activate it using this command:
```commandline
source venv/bin/activate
```

You should see something like this before the current path in your terminal:
```
(venv)some_address:
```

the next step is to install the requirements:
```commandline
make requirements
```

### Setup your configurations:
Now it's time to set your own configuration by specifying what kind of appointment you need, for how many persons, etc...

For this, create a file named `.env` in the root folder of the project with following content:

```text
NUMBER_OF_PERSONS = <Number of people to make the appointment>
DESIRED_DEADLINE_DATE_FOR_BIOMETRICS = <You need an appointment for biometrics before this data (format dd-mm-yyyy)>
DESIRED_DEADLINE_DATE_FOR_PICKUP_DOCUMENTS = <You need an appointment for pickup documents before this data (format dd-mm-yyyy)>
BIOMETRICS_CHECK_ACTIVE = <True/False Whether you need this appointment type>
PICKUP_DOCUMENTS_CHECK_ACTIVE = <True/False Whether you need this appointment type>
WHATSAPP_MESSAGE_ACTIVE = <True/False Whether you want to be notified by Whatsapp message>
PHONE_NUMBER_FOR_WHATSAPP_MESSAGE = <A phone number which is active in Whatsapp e.g +31612345678>
TIME_INTERVAL_TO_CHECK_FREE_SLOTS_IN_SECONDS = <Number of seconds to wait before checking for available slots again>
```
Replace the part after `=` with your desired values

### How to run the script

Now everything is ready to run the script. To do that run this command in the terminal where you're in the folder of the project:

```commandline
make run
```

### Participating in the project

If you have any idea to improve this (e.g: adding option to send an email, etc...), I'd be more than happy to get some PRs.
