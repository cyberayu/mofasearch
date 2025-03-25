import json
import os
import asyncio
from bs4 import BeautifulSoup
from mofa.agent_build.base.base_agent import MofaAgent, run_agent
from crawl4ai import AsyncWebCrawler
async def load_url_with_crawl4ai(url:str):
    async with AsyncWebCrawler(verbose=True) as crawler:
        wait_for = """() => {
                    return new Promise(resolve => setTimeout(resolve, 3000));
                }"""
        result = await crawler.arun(url=url, magic=True, simulate_user=True, override_navigator=True,wait_fo=wait_for)
        if result.status_code == 200:
            # 如果您需要进一步处理HTML内容，可以在这里进行
            # 例如，使用LLM或其他解析方法
            return result.html
        else:
            raise Exception(f"Error loading URL: {url}")
def clean_html(html_content: str) -> str:
    soup = BeautifulSoup(html_content, 'html.parser')
    for tag in soup(['script', 'style']):
        tag.decompose()
    clean_html = str(soup)
    return clean_html

def load_url(url:str):
    try:
        html = asyncio.run(load_url_with_crawl4ai(url=url))
        if os.getenv('CLEAN_HTML', None) is not None:
            html = clean_html(html_content=html)
        return html
    except Exception as e:
        return f'Error loading URL: {url}' + str(e)
@run_agent
def run(agent:MofaAgent):
    url = agent.receive_parameter('crawl4ai-connector-url')
    all_result = []
    try:
        url = json.loads(url)
        if isinstance(url, list):
            for u in url:
                print('-------- url :',u, type(u))
                all_result.append({u:load_url(url=u)})
        elif isinstance(url,str):
            print('Error loading URL: ', url, type(url))
            all_result.append({url: load_url(url=url)})
    except Exception as e :
        all_result.append({url:load_url(url=url)})
    agent.send_output(agent_output_name='crawl4ai_connector_result',agent_result=all_result)
def main():
    agent = MofaAgent(agent_name='crawl4ai-connector')
    run(agent=agent)
if __name__ == "__main__":
    main()
