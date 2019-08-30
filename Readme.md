# Installation

```
sudo pip install selenium
```

if you are working in jupyter you also need to install. (Depends on your conda installation)
```
sudo conda install selenium
```
# Dependancies 

If you get an error of a missing driver *geckodriver*

You need to go to the following link (https://github.com/mozilla/geckodriver/releases) and get the latest geckdriver.

I move it to my /usr/local/bin and changed it's permission to be excecutable

```
sudo chmod +x /usr/local/bin/geckodriver
```

# Structure

In the exmaple folder you can try to run a simple code (called *test.py* ) that tries to open a FireFox web browser with the ubuntu.com webpage. You can test that your installation is correct by trying to run it.

# Testing

For testing purpouses you might need to turn on the switch to give access to "less secure app acess" (https://myaccount.google.com/lesssecureapps) :heavy_exclamation_mark: . Make sure you switch it back once testing is done.

Also do not :x: hardecode your password in the code. SPECIAL carefull if you push a commit with the hardcoded password

