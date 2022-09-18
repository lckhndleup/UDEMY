from selenium import webdriver
import time
#from userInfo import username , password (create userInfo and write username and password)
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Instagram:
    chrome_driver_path="//Users/mehmetaliyildiz/Drivers/chromedriver"
    def __init__(self,username, password):
        self.username = username
        self.password = password
        self.browser  = webdriver.Chrome(Instagram.chrome_driver_path)

    def signIn(self): #otomatik giriş yapacak.
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(4)
        usernameInput = self.browser.find_element(By.NAME, 'username')
        passwordInput = self.browser.find_element(By.NAME, 'password')

        usernameInput.send_keys(username)
        passwordInput.send_keys(password)

        passwordInput.send_keys(Keys.ENTER)
        time.sleep(4)

        if self.browser.find_element(By.CLASS_NAME, 'cmbtv'):
            element = self.browser.find_element(By.CLASS_NAME, 'cmbtv')
            element.find_element(By.TAG_NAME, 'button').click()
        
        time.sleep(4)

        if self.browser.find_element(By.CLASS_NAME, '_a9-z'):
            simdi = self.browser.find_element(By.CLASS_NAME, '_a9-z')
            simdi.find_element(By.TAG_NAME, 'button').click()
            







    def getFollowers(self): #kullanıcıları getir.
        self.browser.get("https://www.instagram.com/{userInfo.username}/")
        time.sleep(3)
        

        buttons = self.browser.find_elements(By.CSS_SELECTOR, '._aa_5')

        followersbutton = buttons[2]
        followersbutton.click()
        time.sleep(5)

        jscommand = """
        followers = document.querySelector("._aano") ;
        followers.scrollTo(0, followers.scrollHeight) ;
        var lenOfPage = followers.scrollHeight;
        return lenOfPage;
        """
        lenOfPage = self.browser.execute_script(jscommand)
        match=False
        while(match==False):
            lastCount = lenOfPage
            time.sleep(1)
            lenOfPage = self.browser.execute_script(jscommand)
            if lastCount == lenOfPage:
                match=True
        time.sleep(5)
        

        followersList = []

        followers = self.browser.find_elements(By.CSS_SELECTOR, '.qi72231t.nu7423ey.n3hqoq4p.r86q59rh.b3qcqh3k.fq87ekyn.bdao358l.fsf7x5fv.rse6dlih.s5oniofx.m8h3af8h.l7ghb35v.kjdc1dyq.kmwttqpk.srn514ro.oxkhqvkx.rl78xhln.nch0832m.cr00lzj9.rn8ck1ys.s3jn8y49.icdlwmnq.notranslate._a6hd')

        for follower in followers:
            followersList.append(follower.text)
        
        with open("followers.txt","w",encoding="UTF-8") as file:
            for follower in followersList:
                file.write(follower +"\n")

        self.browser.close()

        
        

        







app = Instagram(username,password)

app.signIn()
app.getFollowers()
#app.followUser("abc")
#app.unFollowUser("abc")

