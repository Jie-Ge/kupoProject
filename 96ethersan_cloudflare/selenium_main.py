'''
获取此网站中的判例库中的数据: https://aml.zklatech.com/
保存至html文件
'''

from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait


class Spider(object):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='D:/Downloads/chromedriver_win32/chromedriver.exe')

        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
          "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => false
            })
          """
        })
        self.driver.get('https://cn.etherscan.com/address/0x2b74cf42d87ad6ffcc46c29a07cff14149c18b84')
        # time.sleep(8)

    def open_file(self):
        self.f = open('./case.html', 'w', encoding='gb18030')

    def get_content(self):
        self.driver.find_element_by_class_name('home-mask-ok').click()
        time.sleep(2)
        self.driver.find_element_by_class_name('section-case-nav-gzt-large').click()
        time.sleep(2)
        target = self.driver.find_element_by_xpath('//*[@tipname="判例库"]')
        self.driver.execute_script("arguments[0].scrollIntoView();", target)  # 拖动滚动条到可见的元素去
        target.click()
        time.sleep(2)

        page_num = 0
        while page_num < 36:
            page_num += 1
            print(f'正在爬取第{page_num}页.............')
            self.driver.find_element_by_xpath(f'//li[@title="{page_num}"]').click()
            time.sleep(3)  # 这里要等待一下

            spans = self.driver.find_elements_by_class_name("material-card-box")
            for span in spans:
                span.click()
                time.sleep(2)
                handles = self.driver.window_handles  # 窗口句柄
                self.driver.switch_to.window(handles[-1])  # 切换到最后一个窗口

                title = self.driver.find_element_by_xpath('//h2')
                num = self.driver.find_element_by_xpath('//h3')

                self.f.write('<h2>' + title.get_attribute('textContent') + '</h2>')
                self.f.write('<h3>' + num.get_attribute('textContent') + '</h3>')
                print(title.get_attribute('textContent'))  # 获取标签中的文本

                divs = self.driver.find_elements_by_xpath('//div[@class="original"]/child::*')
                for div in divs:
                    content = div.get_attribute('textContent').replace(' ', '')
                    self.f.write('<p>' + content + '</p>')

                self.f.write('-' * 60 + '分割线' + '-' * 60)
                self.driver.close()
                self.driver.switch_to.window(handles[0])

        self.driver.quit()

    def close_file(self):
        self.f.close()

    def main(self):
        spider.open_file()
        spider.get_content()
        spider.close_file()


if __name__ == '__main__':
    spider = Spider()
    # spider.main()
