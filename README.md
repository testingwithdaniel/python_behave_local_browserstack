# Python Behave Local BrowserStack
Python Behave framework to run test on a local browser or BrowserStack.

# Prerequisites
python 2.7

# Installation
1. Download the repo as zip file or type
```git clone https://github.com/mukeshtiwari1987/python_behave_local_browserstack```
2. In the command prompt type
```pip install -r requirements.txt```

# Structure
![Folder Structure Image](https://i.ibb.co/cyBmmPT/Screen-Shot-2019-02-05-at-1-55-54-AM.png)

# How to run test on local machine in Chrome
1. Download Chrome Driver and provide the location of file in ```config/local.json```

# How to run test on BrowserStack
1. Sign up for a free trial account on [BrowserStack](https://www.browserstack.com/).
2. Make a note of your __Username__ and __Access Key__
3. Place Username and Access Key in ```config/browserstack.json```

# How to integrate test with Travis
1. Sign up for an account on [Travis CI](https://travis-ci.org/).
2. Ensure you have Ruby installed on your machine.
3. In the command prompt type
```gem install travis```
4. In the command prompt type ```travis encrypt access_key="BROWSERSTACK_ACCESS_KEY"``` and make the note of output.
5. Place the output in under secure in .travis.yml.