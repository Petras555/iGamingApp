# Introduction
- Add your project logo.
- Write a short introduction to the project.
- If you are using badges, add them here.

## Index

- [About](#about)
- [Usage](#usage)
  - [Installation](#installation)
  - [Commands](#commands)
- [Development](#development)
  - [Pre-Requisites](#pre-requisites)
  - [Developmen Environment](#development-environment)
  - [File Structure](#file-structure)
  - [Build](#build)  
  - [Deployment](#deployment)  
- [Community](#community)
  - [Contribution](#contribution)
  - [Branches](#branches)
  - [Guideline](guideline)  
- [FAQ](#faq)
- [Resources](#resources)
- [Gallery](#gallery)
- [Credit/Acknowledgment](#creditacknowledgment)
- [License](#license)

## About
Simple iGaming "application" which connects to MySQL database where user can create accounts and make transactions with them to virtual wallet. Database holds information about every account(userID, username, password) and every transaction that was made with each account(transaction ID, username, amount, transaction type:deposit or withdrawal and date). The project allows to build data within database which could be used for following tasks:
*List all users having 3 deposits or more
*List all users having only 1 withdrawal
*List 3 users that have made the highest deposits
*List all deposits for users. Display UserId, UserName, DepositDate, DepositAmount
*Calculate balances of all users
## Usage
Project is build from multiple files:
-launcher.py a file which should be firstly used by user to navigate through project.
-createdatabase.py file creates database and mandatory tables within database (1st selection within launcher.py).
-database.py has functions for connecting to database, which are used in other scripts.
-gamemenu.py game file for creating accounts, doing deposits and withdrawals, and checking list of all accounts within database(2nd selection within launcher.py).
-task.py file for operatings tasks from [About](#about) section. (3rd selection within launcher.py).
-classes.py separate file for classes, currently contains single class for user.
-requirements.txt file for installing dependencies.

### Requirements 
Python 3
MySQL Workbench

```


### Installation
- First of all MySQL database is mandatory. It can be downloaded via: 
  * https://dev.mysql.com/downloads/workbench/ (Windows)
  * 
- Be very detailed here, For example, if you have tools which run on different operating systems, write installation steps for all of them.

```
$ add installations steps if you have to.
```

### Commands
- Commands to start the project.

## Development
If you want other people to contribute to this project, this is the section, make sure you always add this.

### Pre-Requisites
List all the pre-requisites the system needs to develop this project.
- A tool
- B tool

### Development Environment
Write about setting up the working environment for your project.
- How to download the project...
- How to install dependencies...


### File Structure
Add a file structure here with the basic details about files, below is an example.

| No | File Name | Details 
|----|------------|-------|
| 1  | index | Entry point

### Build
Write the build Instruction here.

### Deployment
Write the deployment instruction here.

## Community

If it's open-source, talk about the community here, ask social media links and other links.

### Contribution

 Your contributions are always welcome and appreciated. Following are the things you can do to contribute to this project.

 1. **Report a bug** <br>
 If you think you have encountered a bug, and I should know about it, feel free to report it [here]() and I will take care of it.

 2. **Request a feature** <br>
 You can also request for a feature [here](), and if it will viable, it will be picked for development.  

 3. **Create a pull request** <br>
 It can't get better then this, your pull request will be appreciated by the community. You can get started by picking up any open issues from [here]() and make a pull request.

 > If you are new to open-source, make sure to check read more about it [here](https://www.digitalocean.com/community/tutorial_series/an-introduction-to-open-source) and learn more about creating a pull request [here](https://www.digitalocean.com/community/tutorials/how-to-create-a-pull-request-on-github).


### Branches

 I use an agile continuous integration methodology, so the version is frequently updated and development is really fast.

1. **`stage`** is the development branch.

2. **`master`** is the production branch.

3. No other permanent branches should be created in the main repository, you can create feature branches but they should get merged with the master.

**Steps to work with feature branch**

1. To start working on a new feature, create a new branch prefixed with `feat` and followed by feature name. (ie. `feat-FEATURE-NAME`)
2. Once you are done with your changes, you can raise PR.

**Steps to create a pull request**

1. Make a PR to `stage` branch.
2. Comply with the best practices and guidelines e.g. where the PR concerns visual elements it should have an image showing the effect.
3. It must pass all continuous integration checks and get positive reviews.

After this, changes will be merged.


### Guideline
coding guidelines or other things you want people to follow should follow.


## FAQ
You can optionally add a FAQ section about the project.

##  Resources
Add important resources here

##  Gallery
Pictures of your project.

## Credit/Acknowledgment
Credit the authors here.

##  License
Add a license here, or a link to it.
