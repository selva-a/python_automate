from selenium import webdriver


def get_drvier():
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  a = webdriver.Chrome(options=options)
  a.get("https://www.selenium.dev/documentation/webdriver/")
  return a


def main():
  a = get_drvier()
  # Find all h1 elements on the page
  #elements = a.find_elements_by_xpath("//h1")
  elements = a.find_elements(by="xpath", value="//li")
  # Extract text from each h1 element and store in a list
  h1_texts = [element.text for element in elements]
  return h1_texts


print(main())
