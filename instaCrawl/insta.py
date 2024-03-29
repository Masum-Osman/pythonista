from selenium import webdriver
import time
import urllib.request

driver = webdriver.Chrome()
# driver.get("https://www.instagram.com/knyazeva_anastasiya_official/")
driver.get("https://www.instagram.com/frayaoka/")
# driver.get("https://www.instagram.com/masum_osman_khan/")

lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount==lenOfPage:
        match=True

posts = []
links = driver.find_elements_by_tag_name('a')
for link in links:
    post = link.get_attribute('href')
    if '/p/' in post:
      posts.append( post )

# print( posts )

download_url = ''
for post in posts:
  driver.get( post )
  shortcode = driver.current_url.split("/")[-2]
  type = driver.find_element_by_xpath('//meta[@property="og:type"]').get_attribute('content')
  if type == 'video':
      download_url = driver.find_element_by_xpath("//meta[@property='og:video']").get_attribute('content')
      urllib.request.urlretrieve( download_url , 'SanjanaFreya_{}.mp4'.format( shortcode ))
  else:
      download_url = driver.find_element_by_xpath("//meta[@property='og:image']").get_attribute('content')
      urllib.request.urlretrieve(download_url, 'SanjanaFreya_{}.jpg'.format(shortcode))
  time.sleep( 5 )

print("Done")
driver.close()