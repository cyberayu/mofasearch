import json
import os

from bs4 import BeautifulSoup
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait

def load_url_with_selenium(url: str, time_out: int = 3, args=None, **kwargs):
    options = webdriver.ChromeOptions()
    if args is None:
        args = ['--headless', '--disable-gpu', '--start-maximized']
    for arg in args:
        options.add_argument(arg)
    service = Service()
    # 初始化Chrome浏览器
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    wait = WebDriverWait(driver, time_out)
    wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')

    # 获取当前页面的HTML内容
    html = driver.page_source

    # 关闭浏览器
    driver.quit()

    return html
def clean_html(html_content: str) -> str:
    soup = BeautifulSoup(html_content, 'html.parser')
    for tag in soup(['script', 'style']):
        tag.decompose()
    clean_html = str(soup)
    return clean_html

def load_url(url:str):
    try:
        html = load_url_with_selenium(url, time_out=os.getenv('TIMEOUT', 3))
        if os.getenv('CLEAN_HTML', None) is not None:
            html = clean_html(html_content=html)
        return html
    except Exception as e :
        return f'Error loading URL: {url}' + str(e)

@run_agent
def run(agent:MofaAgent):
    url = agent.receive_parameter('selenium-connector-url')
    all_result = []
    try:
        url = json.loads(url)
        if isinstance(url, list):
            for u in url:
                print('-------- url :',u, type(u))
                all_result.append({u:load_url(url=u)})
        elif isinstance(url,str):
            all_result.append({url: load_url(url=url)})
    except Exception as e :
        print('Error loading URL: ',url, type(url))
        all_result.append({url:load_url(url=url)})
    agent.send_output(agent_output_name='selenium_connector_result',agent_result=all_result)
def main():
    agent = MofaAgent(agent_name='selenium-connector')
    run(agent=agent)
if __name__ == "__main__":
    main()
