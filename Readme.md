# WhatsAppWishesAutomation
This python program will read the names from the .csv file and send a message to the person having same name on your WhatsApp application.

Requirements:
1. You need install selenium.
2. Download chromedriver from  https://chromedriver.chromium.org/downloads extract and store it in C:\Chrome.
3. Keep in mind that 'webdriver.Chrome("location")' location must be your chromedriver.exe location.

After running the code:
1. Wait till the whatsapp web page opens in the browser.
2. Now scan the QR code shown at the page using whatsapp installed in mobile.
3. Press any key at python console.

The python code will scan data from csv file and store it in a list and.
For every name in the list the code will open the chat and type and send the respective message to the respective contact.

*Note you can use any browser like FireFox PhantomJS I have used Chrome because it was easy to use.
