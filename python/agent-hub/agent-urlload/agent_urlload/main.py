import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from mofa.agent_build.base.base_agent import MofaAgent, run_agent

@run_agent
def run(agent: MofaAgent):
    url = agent.receive_parameter('query')
    result = load(url)
    agent.send_output(agent_output_name='urlload_result', agent_result=result)

def load(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 检查请求是否成功
    except requests.exceptions.RequestException as e:
        print(f"请求页面时出错: {e}")
        return None
    print("=============输出网页内容=============")
    print(response.text)
    # 解析HTML内容
    soup = BeautifulSoup(response.text, 'html.parser')
    base_url = response.url  # 获取基础URL用于处理相对路径

    # with open(f"my_html.txt", 'w', encoding='utf-8') as f:
    #     f.write(f"{response.text}")
    
    # 提取文本内容（去除脚本和样式）
    for script in soup(['script', 'style', 'noscript', 'meta', 'link']):
        script.extract()
    text_content = soup.get_text(separator='\n', strip=True)

    # 提取图片URL
    images = set()
    for img in soup.find_all('img'):
        src = img.get('src')
        if src:
            absolute_url = urljoin(base_url, src)
            images.add(absolute_url)

    # 提取超链接
    links = []
    for a in soup.find_all('a'):
        href = a.get('href')
        if href:
            absolute_url = urljoin(base_url, href)
            link_text = a.get_text(strip=True) or "无文本内容"
            # 过滤非HTTP链接
            if absolute_url.startswith(('http://', 'https://')):
                links.append((link_text, absolute_url))

    return {
        'context': response.text,
        'text': text_content,
        'images': list(images),
        'links': links
    }


def main():
    agent = MofaAgent(agent_name='agent-urlload')
    run(agent=agent)

if __name__ == "__main__":
    main()
