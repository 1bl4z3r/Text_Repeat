# TEXT_REPEAT

![Python](https://www.python.org/static/community_logos/python-powered-w-70x28.png)

Hi! This is a help file-cum-user manual for the script **Text_Repeat**. You need to know something before you go totally bonkers with it. So, take your sweet time to read through.

Seriously, read whole of this stuff. Download can wait.

[Download](https://github.com/1bl4z3r/Text_Repeat/archive/download.zip)

## Why do I need this?

Good question, why do you need this. Let me see... you do not need this. Have a life, enjoy it.

On more serious note, if you are like me, sending wishes over WhatsApp (because I condem human interaction), to people whom you never talk in real life, and enjoy your beauty sleep whilst your device is sending thousands of messages. OR, You are are a in a relationship and your girl is mad at you, time to send 1000 messages, OR, You like disturbing people from their normal peaceful routine, with random useless messages.

>Good Luck, Chuck (For last one)

_Now, a Disclaimer_

1. Don't cry if your best friend blocked you as you didn't knew when to stop.
2. I am not responsible if the recipient breaks your phone or bones.
3. Don't try on your crushes, seriously never try.


## Files

When you download Text_Repeat, you will be presented with

> **dev.zip** : This contains all the unmodified files for those who like tinkering. You need to have python >= *3.0* installed.

This zip contains:
- Readme
- message.txt
- numbers.txt
- Text_Repeat.py

## How to run this damn thing?

0. You need to download webdrivers. Go to `"Readme"` and follow the links for downloading appropriate webdrivers for Chrome/Firefox. For reference, I am lising those URLs here too.

    >Chrome Webdriver: [https:/chromedriver.chromium.org/downloads](https:/chromedriver.chromium.org/downloads)
    
    >Firefox Webdriver: [https://github.commozilla/geckodriver/releases](https:/github.com/mozilla/geckodriver/releases)

1. You must have all the files in a single folder/directory. Failing which the script/software will not execute.
    - message.txt
    - numbers.txt
    - Text_Repeat.py
    - Chrome's Webdriver or Firefox's Webdriver

2. In `"numbers.txt"`, enter the numbers of your recipient in list-order; without `'-'` or `spaces`. If you fail to do so, or enter a number that isn't in your contact list, the script will fail. An example is shown below.

        1234567890  
        1122334450

    >**Tip :** I initally thought to enter names, but since more than one person can have same name in contact list and whole system is automated, I decided against it. However, you can enter names in place of numbers; but I don't gurantee it will work perfectly.

3. In `"message.txt"`, you are required to write the message that you wish to send. Every new line is a new message. So,

        This is first message
        This is second message

    >**To-Do :** I will add a check to see if file is empty. If it is, then it will send blank message. But, I have to make sure it works before deploying, and so you have to wait.

4. Run: `Text_Repeat.py`

## Now, How to Run

1. The script will check for internet connectivity first, failing which it will exit immediately.
2. It will ask if you want to see online manual (this online manual). If you press any button on qwerty keyboard apart from 'y', it will start executing.
3. It will then check existance of `numbers.txt` & `message.txt`, failing which script will exit.
4. It will then present you on how many times you want to send a particular message to your recipients. Completing which it will show your choices.
5. It will ask you which browser you choose and check for webdrivers in the folder. Loading which it will fireup existing browser and load up `web.whatsapp.com`.
6. It will then ask you to scan QR code and press any key to continue.
7. Now everything is automated, sit back and enjoy. And, don't mess up the browser window on which this script is working. 

## License

This is under GNU Affero General Public License v3.0

## Contribution

If any one out there actually likes to contribute (which I don't know why one should do, unless you have loads of free time), feel free to remix it, or make a GUI (coz I suck at this).

## Thanks
- All the members of StackOverflow
- Developers behind Python and its libraries
- Electricity, Internet and basic amenities of mankind
