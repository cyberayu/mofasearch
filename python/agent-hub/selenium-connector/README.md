# Selenium Connector

Selenium Connector 是一个基于 Mofa Agent 框架的网页爬取代理，使用 Selenium WebDriver 实现浏览器自动化抓取。

## 功能说明

这个代理主要用于：
- 抓取需要JavaScript渲染的动态网页内容
- 支持完整的浏览器环境，可以处理复杂的网页交互
- 自动等待页面加载完成
- 提供可选的HTML清理功能，去除JavaScript和样式代码
- 默认使用无头模式（headless）运行Chrome浏览器

## 参数说明

### 输入参数
| 参数名 | 类型 | 描述 | 必填 |
|--------|------|------|------|
| url | string | 需要爬取的目标URL | 是 |

### 输出结果
| 参数名 | 类型 | 描述 |
|--------|------|------|
| selenium_connector_result | string | 爬取到的HTML内容 |

### 环境变量
- `CLEAN_HTML`: 设置此环境变量以启用HTML清理功能（可选）
- `TIMEOUT`: 设置页面加载超时时间，默认为3秒

## 依赖项
- selenium
- webdriver_manager
- beautifulsoup4
- pyarrow >= 5.0.0

## 注意事项
1. 需要本地安装Chrome浏览器
2. 默认使用无头模式和禁用GPU加速
3. 自动管理ChromeDriver，无需手动下载
4. 如果启用了CLEAN_HTML，将会自动清理HTML中的script和style标签
