from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import random
import string
import requests
import json

f=open('firstname.txt')
firstnames = f.read().splitlines()
f=open('lastname.txt')
lastnames = f.read().splitlines()
f=open('useragent_Android.txt')
useragents=f.read().splitlines()

# r=requests.get("https://api.getproxylist.com/proxy?allowsHttps=1&country[]=US&protocol=http&anonymity[]=high%20anonymity&anonymity[]=transparent&apiKey=ebafc88781ade6aa3f20999a71320189e0fbaf5d")
# proxy=json.loads(r.text)
# print(proxy['protocol'])
# print(proxy['ip'])
# print(proxy['port'])
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server='+str(proxy['protocol'])+'://'+str(proxy['ip'])+':'+str(proxy['port']))
# chrome_options.add_argument("user-agent="+useragents[random.randint(0, len(useragents))])
# driver1 = webdriver.Chrome(options=chrome_options)
while True:
        start=time.time()
        firstname=firstnames[random.randint(0, len(firstnames))]
        lastname=lastnames[random.randint(0, len(lastnames))]
        membername=firstname+lastname+str(random.randint(1000, 1000000))
        password=''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)])
        print(membername+'|'+password)

        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("user-agent="+useragents[random.randint(0, len(useragents))])
        # driver1 = webdriver.Chrome(options=chrome_options)
        driver1 = webdriver.Chrome()
        driver1.implicitly_wait(20) # seconds
        driver1.delete_all_cookies()
        driver1.get('https://outlook.live.com/owa/?nlp=1&signup=1')
        driver1.find_element_by_id('MemberName').send_keys(membername)
        time.sleep(2)
        driver1.find_element_by_id('domainLabel').click()
        time.sleep(2)
        driver1.find_element_by_id('domain1').click()
        time.sleep(2)
        driver1.find_element_by_id('iSignupAction').click()
        time.sleep(2)
        driver1.find_element_by_id('PasswordInput').send_keys(password)
        time.sleep(2)
        driver1.find_element_by_id('iSignupAction').click()
        time.sleep(2)
        driver1.find_element_by_id('FirstName').send_keys(firstname)
        time.sleep(2)
        driver1.find_element_by_id('LastName').send_keys(lastname)
        time.sleep(2)
        driver1.find_element_by_id('iSignupAction').click()
        time.sleep(2)
        optionlist=driver1.find_element_by_id('BirthMonth').find_elements_by_tag_name("option")
        optionlist[random.randint(1, 11)].click()
        time.sleep(2)
        driver1.find_element_by_id('BirthDay').send_keys(str(random.randint(1,28)))
        time.sleep(2)
        driver1.find_element_by_id('BirthYear').send_keys(str(random.randint(1985,2000)))
        time.sleep(2)
        driver1.find_element_by_id('iSignupAction').click()
        response = requests.get(driver1.find_element_by_css_selector("#hipTemplateContainer img").get_attribute("src"))
        r = requests.post('http://poster.de-captcher.com', data={'function': 'picture2', 'username': 'thanhnambeo', 'password': '4affhvpna','pict_type':'0'}, files={'pict': response.content})
        driver1.find_element_by_css_selector('#hipTemplateContainer input').send_keys(r.text.split('|')[-1].replace(' ',''))
        time.sleep(2)
        driver1.find_element_by_id('iSignupAction').click()
        driver1.find_element_by_class_name('nextButton').click()
        driver1.implicitly_wait(1) # seconds
        for i in range(20):
                try:
                        driver1.find_element_by_class_name('nextButton').click()
                except:
                        break
        driver1.implicitly_wait(20) # seconds
        driver1.find_element_by_css_selector('button.primaryButton').click()
        time.sleep(2)
        driver1.execute_script("window.open();")
        driver1.switch_to_window(driver1.window_handles[1])
        driver1.get('https://mail.protonmail.com/create/new?language=en')
        driver1.find_element_by_id('username').send_keys(membername)
        driver1.find_element_by_id('password').send_keys(password)
        driver1.find_element_by_id('passwordc').send_keys(password)
        driver1.find_element_by_id('notificationEmail').send_keys(membername+'@hotmail.com')
        time.sleep(1)
        driver1.find_element_by_class_name('signUpProcess-btn-create').click()
        time.sleep(2)
        driver1.find_element_by_id('id-signup-radio-email').click()
        time.sleep(1)
        driver1.find_element_by_id('emailVerification').send_keys(membername+'@hotmail.com')
        time.sleep(1)
        driver1.find_element_by_class_name('codeVerificator-btn-send').click()
        time.sleep(1)
        driver1.switch_to_window(driver1.window_handles[0])
        driver1.get('https://outlook.live.com/mail/inbox')
        driver1.implicitly_wait(5) # seconds
        try:
                driver1.find_element_by_css_selector("button[id*='-Tab1']").click()
        except:
                print("Cannot find Tab1")
        driver1.implicitly_wait(30) # seconds
        verifycode=driver1.find_element_by_css_selector("div[aria-label*='Your Proton verification code is: ']").get_attribute("aria-label")
        driver1.switch_to_window(driver1.window_handles[1])
        driver1.find_element_by_id('codeValue').send_keys(verifycode[-6:])
        driver1.find_element_by_class_name('humanVerification-completeSetup-create').click()
        driver1.find_element_by_id('confirmModalBtn').click()
        driver1.quit()
        f = open("listmail.txt", "a")
        f.write(membername+'|'+password+'\n')
        f.close()
        print(time.time()-start)
        time.sleep(120-int(time.time()-start))






