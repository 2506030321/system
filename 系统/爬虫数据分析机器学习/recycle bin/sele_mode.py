from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 定义类
class LianJia(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        # 打开页面
        self.driver.get('https://cs.fang.lianjia.com/loupan/')

    def clear_driver(self):
        # 关闭驱动
        self.driver.close()
        self.driver.quit()
	
	# 代码核心部分
    def scroll(self):
        while True:
            # 滑动之前的页面高度
            document = self.driver.execute_script('return document.body.scrollHeight;')
            time.sleep(2)
            # 滑动页面
            self.driver.execute_script(f'window.scrollTo(0,{document})')
            time.sleep(2)
            # 滑动之后的页面高度
            document2 = self.driver.execute_script('return document.body.scrollHeight;')
            # 比较滑动前与滑动后的高度
            if document == document2:
                break
	# 定义翻页函数
    def up_page(self):
        time.sleep(1)
        # 点击下一页
        self.driver.find_element(By.XPATH,'//*[text()="下一页"]').click()

	# 定义保存页面源码函数
    def save_page(self, n=1):
        time.sleep(2)
        # 保存数据
        with open(f'第{n}页.html', 'w', encoding='utf-8') as f:
            f.write(self.driver.page_source)

	# 定义总的执行函数
    def run(self):
        try:
            self.save_page()  # 第一页
            for n in range(2, 6):  # 第二三四五页
                self.scroll()
                self.up_page()
                self.save_page(n)
        except Exception as e:
            print(e)
        finally:
            self.clear_driver()


if __name__ == '__main__':
    lianjia = LianJia()
    lianjia.run()