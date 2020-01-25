from socket import gethostbyname, gethostname
from os import path
from time import sleep
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def file_check():
	
	if path.exists('numbers.txt') and path.exists('message.txt'):
		
		m=open("message.txt","r") 
		message={}
		for each in m:
			t=int(input("\n{} : How many times? ".format(each.rstrip())))
			message[each.rstrip()]=t
		
		print("\nMessage (Number of times)")
		for item,amount in message.items():
			print("{} ({})".format(item,amount))

		while True:
			ch=input("\nBrowser (1-Chrome 2-Firefox): ")
			if ch=="1":
				print("\nStarting Chrome...")
				driver=webdriver.Chrome()
				driver.set_window_size(1024, 600)
				sleep(5)
				break

			elif ch=="2":
				print("\nStarting Firefox...")			
				driver=webdriver.Firefox()	
				driver.set_window_size(1024, 600)
				sleep(5)
				break

			else:
				print("Wrong Input, TRY AGAIN\n")

		driver.get("https://web.whatsapp.com")
		while driver.title != "WhatsApp":
			sleep(5)
		
		input("\nScan QR code and press any key to continue...")

		f=open("numbers.txt","r")
		for aline in f:
			number=int(aline.split('\n')[0])
			repeat(message,driver,number)

		print("\nBombing Complete")
		
		driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[3]/div").click()
		driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[3]/span/div/ul/li[6]/div").click()
		f.close()
		m.close()
		sleep(10)

		print("\nExiting Browser")

		driver.quit()
	else:
		print ("number.txt:"+str(path.exists('numbers.txt'))+"\n"+"message.txt:"+str(path.exists('message.txt'))+'\n')

def repeat(message,driver,number):

	driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[2]").click()
	sleep(5)
	driver.find_element_by_xpath(
		"//*[@id='app']/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/input").send_keys(number)
	sleep(10)
	driver.find_element_by_xpath(
		"//*[@id='app']/div/div/div[2]/div[1]/span/div/span/div/div[2]/div/div/div/div[2]/div/div").click()
	messagebox = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")

	for items,amt in message.items():
		print("Message: {} to {}".format(items,number))
		for x in range(amt):
				messagebox.send_keys(items)
				messagebox.send_keys(Keys.RETURN)
				if x==(amt+1):
					print("Sending {} message out of {}".format(x,amt))
				else:
					print("Sending {} message out of {}".format(x,amt),end="\r")
				sleep(2)
	return None


if __name__ == "__main__":
	if gethostbyname(gethostname())=="127.0.0.1":
		print("You are not connected to INTERNET")
	else:
		print("\t+-++-++-++-++-++-++-++-++-++-++-+\t+-++-++-++-++-+")
		print("\t|T||E||X||T| _ |R||E||P||E||A||T|\t::1bl4z3r::")
		print("\t+-++-++-++-++-++-++-++-++-++-++-+\t+-++-++-++-++-+")
		while True:
			if input("\nDo you want to view manual (y/n)? ").lower()=="y":
				webbrowser.open("https://github.com/1bl4z3r/Text_Repeat/blob/download/README.md",autoraise=True)
			else:
				file_check()
				break
