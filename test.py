from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options


# 打开chrome无头浏览器
edge_options = Options()
edge_options.add_argument('--headless')
edge_options.add_argument('--disable-gpu')

# 反侦测，开启开发者模式
edge_options.add_experimental_option('excludeSwitches', ['enable-automation'])
# 禁用启动Blink运行时功能
edge_options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Edge(options=edge_options)
executor_url = driver.command_executor._url
session_id = driver.session_id

# 将打开的浏览区url和session_id存储起来，提供给下一次应用
# file = open('browserMsg.txt', 'w')
# file.writelines([executor_url, 'n', session_id])
# file.close()
driver.implicitly_wait(20)
driver.set_window_size(1000, 800)

driver.get(
    "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1683777177601_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&dyTabStr=MCwxLDYsMyw0LDUsMiw3LDgsOQ%3D%3D&ie=utf-8&sid=&word=%E6%8E%92%E9%AA%A8")

print(driver.page_source)
elements = driver.find_elements(by=By.CLASS_NAME, value='main_img.img-hover')
print(len(elements))
for element in elements:
    url = element.get_attribute('data-imgurl')
    print(url)