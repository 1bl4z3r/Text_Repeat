import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def repeat():

    while True:
        browser = input("\nSelect browser\n1-Chrome 2-Firefox: ")
        if browser == "1":
            driver = webdriver.Chrome(sys.path.append(os.path.realpath('Preferences/chromedriver/chromedriver.exe')))
            driver.set_window_size(1024, 600)
            print("\nStarting Chrome")
            break
        elif browser == "2":
            driver = webdriver.Firefox(sys.path.append(os.path.realpath('Preferences/geckodriver/geckodriver.exe')))
            driver.set_window_size(1024, 600)
            print("\nStarting Firefox")
            break
        else:
            print("Wrong Input, Enter again")
    
    driver.get("https://web.whatsapp.com")
    input("\nScan QR code and press any key to continue...")

    while True:
        while True:
            msg = input("Do you want to send a: 1- Blank Message or 2- Text Message? ")
            if msg == "1":
                message = "ຸ"
                break
            elif msg == "2":
                message = input("\nEnter Message: ")
                break
            else:
                print("Wrong choice, Try again")

        loop = int(input("\nHow many times do you want message to be sent (MAX = 100)? "))
        if loop > 100:
            loop = 100

        name = input("\nEnter name or number of the recipient: ")

        driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[2]").click()
        time.sleep(5)

        driver.find_element_by_xpath(
            "//*[@id='app']/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/input").send_keys(name)
        input("\nDid the person show up correctly? If yes, press Enter")

        driver.find_element_by_xpath(
            "//*[@id='app']/div/div/div[2]/div[1]/span/div/span/div/div[2]/div/div/div/div[2]/div/div").click()

        txtbx = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")

        input("\nPress Enter to Start Bombing...\n")
        x = 1
        while x <= loop:
            txtbx.send_keys(message)
            txtbx.send_keys(Keys.RETURN)
            print("Sending " + str(x) + " Message out of " + str(loop), end="\r")
            time.sleep(1)
            x += 1

        if x - 1 == loop:
            print("\n\nBombing Complete\n\n")

        ch = input("\nDo you want to continue(y/n)? ")
        if ch.lower() == 'y':
            continue
        else:
            break

    print("\n\n\tDeveloped by bl4z3r, with ♥ and privacy.")
    input("\nPress Enter to exit")
    driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[3]/div").click()
    driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[3]/span/div/ul/li[6]/div").click()
    time.sleep(5)
    driver.quit()


if __name__ == "__main__":
    print("Text_Repeat\t\t\tVersion 0.1\n\nEducational Tool. Don't use it for malicious purposes, ThankYou\n\n")
    repeat()
