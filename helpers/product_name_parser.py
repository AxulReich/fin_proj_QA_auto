if __name__ == '__main__':
    from selenium import webdriver
    from selenium.common.exceptions import NoSuchElementException
    import csv

    prods = []
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("http://selenium1py.pythonanywhere.com/en-gb/catalogue/")
    while True:
        try:
            products = browser.find_elements_by_xpath("//section//li//h3/a")
            for product in products:
                temp_var = {"link": product.get_attribute("href").split('/')[5],
                            "title": product.get_attribute("title")
                            }
                prods.append(temp_var)
            browser.find_element_by_css_selector("li.next>a").click()
        except NoSuchElementException:
            with open('products.txt', "w") as p:
                fieldnames = ['link', 'title']
                writer = csv.DictWriter(p, fieldnames=fieldnames)
                writer.writeheader()
                for pr in prods:
                    writer.writerow(pr)
            break
