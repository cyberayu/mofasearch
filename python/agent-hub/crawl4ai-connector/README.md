
# Crawl4AI Connector

Crawl4AI Connector 是一个基于 Mofa Agent 框架的网页爬取代理，专门用于抓取复杂网页内容。

## 功能说明

这个代理主要用于：
- 抓取需要JavaScript渲染的动态网页内容
- 自动处理等待页面加载的情况（默认等待3秒）
- 模拟真实用户行为，避免被反爬
- 提供可选的HTML清理功能，去除JavaScript和样式代码

## 参数说明

### 输入参数
| 参数名 | 类型 | 描述 | 必填 |
|--------|------|------|------|
| url | string | 需要爬取的目标URL | 是 |

### 输出结果
| 参数名 | 类型 | 描述 |
|--------|------|------|
| crawl4ai_connector_result | string | 爬取到的HTML内容 |

### 环境变量
- `CLEAN_HTML`: 设置此环境变量以启用HTML清理功能（可选）

## 依赖项
- crawl4ai
- beautifulsoup4
- pyarrow >= 5.0.0

## 注意事项
1. 该代理会自动处理页面加载和渲染
2. 默认开启了用户行为模拟和导航器覆盖
3. 如果启用了CLEAN_HTML，将会自动清理HTML中的script和style标签
```

