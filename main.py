from selenium import webdriver
import time
from csv import reader

'''
Note this is not reliable way to send data on WhatsApp.
They change the class and id of the tags time to time.
If possible use API
'''

contact_list = []

# Open contacts.csv file and store the data in contact_list
with open('contact.csv', 'r') as f:
    scanner = reader(f)
    for data in scanner:
        contact_list.append(data[0])

driver = webdriver.Chrome("C:/Chrome/chromedriver.exe")
driver.get("https://web.whatsapp.com/")
input("Scan QR code and after scanning press any key")

for i in range(0, len(contact_list)):
    try:
        # Used to find the new message icon on the browser
        new_chat = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[2]/div/span')
        new_chat.click()

        # Used to search the contact name on the browser
        search = driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/div/div[2]')
        search.send_keys(contact_list[i])
        time.sleep(2)

        # Get the person and open the chat window
        person = driver.find_element_by_xpath("//span[@title='{}']".format(contact_list[i]))
        person.click()

        # Searching the text field
        text_box = driver.find_element_by_class_name('DuUXI')
        time.sleep(2)

        text = "Wish you a very happy new year *{}*❤, Hope you a wonderful year ahead ❣ ".format(contact_list[i])

        # Inserting the data in the text field
        text_box.send_keys(text)
        time.sleep(2)

        # Clicking on the send button
        sendBtn = driver.find_element_by_class_name('_2Ujuu')
        sendBtn.click()
        time.sleep(2)
    except Exception as e:
        print(e)
        pass
    time.sleep(2)
