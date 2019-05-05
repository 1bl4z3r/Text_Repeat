import gc
import os
import webbrowser
from socket import create_connection
from sys import exit,path
from time import sleep
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def repeat():
    while True:
        browser = int(input("\nSelect browser\n1-Chrome 2-Firefox: "))
        if browser == 1:
            input("\nWe will download and run drivers for this. Do you permit?")
            print("\nStarting Chrome")
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.set_window_size(1024, 600)
            break
        elif browser == 2:
            input("\nWe will download and run drivers for this. Do you permit?")
            print("\nStarting Firefox")
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            driver.set_window_size(1024, 600)
            break
        else:
            print("Wrong Input, Enter again")

    driver.get("https://web.whatsapp.com")
    input("\nScan QR code and press any key to continue...")

    while True:
        while True:
            print("Do you want to send a:\n1- Blank Message, or\n2- Text Message? ")
            msg = int(input("\nEnter Choice: "))
            if msg == 1:
                message = "ຸ"
                break
            elif msg == 2:
                message = input("\nEnter Message: ")
                break
            else:
                print("Wrong choice, Try again")

        loop = int(input("\nHow many times do you want message to be sent (MAX = 100)? "))
        if loop > 100:
            print("\nMessage quantity limited to 100")
            loop = 100

        name = input("\nEnter name or number of the recipient: ")
        driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[2]").click()
        sleep(5)
        driver.find_element_by_xpath(
            "//*[@id='app']/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/input").send_keys(name)

        contact = input("\nDid the {} show up correctly? (y/n): ".format(name))
        if contact.lower() == 'n':
            print("\nMost probably the contact is not on your contact list.")
            driver.quit()
            return None
        elif contact.lower() != 'n' and contact.lower() != 'y':
            print("\nWrong Input, you are inattentive.")
            driver.quit()
            return None
                

        driver.find_element_by_xpath(
            "//*[@id='app']/div/div/div[2]/div[1]/span/div/span/div/div[2]/div/div/div/div[2]/div/div").click()

        text = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")

        input("\nPress Enter to Start Bombing...\n")

        pbar = tqdm(total=loop, ascii=True, desc='Bombing', dynamic_ncols=True, unit='M')

        for _ in range(loop):
            pbar.update()
            text.send_keys(message)
            text.send_keys(Keys.RETURN)
            sleep(1)
        pbar.close()

        ch = input("\nDo you want to continue(y/n)? ")
        if ch.lower() == 'y':
            continue
        else:
            break

    driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[3]/div").click()
    driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[3]/span/div/ul/li[6]/div").click()
    sleep(5)
    driver.quit()


def abt():
    web = input("\nLook up online?(y/n): ")
    if aliveconn() == 1 and web.lower() == 'y':
        webbrowser.open('https://github.com/1bl4z3r/Text_Repeat/blob/Download/About.md')

def aliveconn():
    try:
        create_connection(("www.google.com", 80))
        return(1)
    except OSError:
        pass
        print("\nYou are not connected to Internet. Connect to Internet.\n")


if __name__ == "__main__":
    print("___  ___     ___      __   ___  __   ___      ___ \n"
          " |  |__  \_/  |      |__) |__  |__) |__   /\   |  \n"
          " |  |___ / \  |  ___ |  \ |___ |    |___ /~~\  |  \n"
          "\t\t\t\tVersion 1.0\n\nEducational Tool. Don't use it for malicious purposes, ThankYou")

    while True:
        print("\n1- Send Text\n2- About/Help\n3- Exit")
        c = int(input("\nEnter Your Choice: "))
        if c == 1:
            if aliveconn() == 1:
                print("\nDevice connected to internet. Continuing>>>\n")
                repeat()
        elif c == 2:
            abt()
        elif c == 3:
            gc.collect()
            exit()
        else:
            print("Wrong Input, Try Again")