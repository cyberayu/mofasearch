from firecrawl import FirecrawlApp

# Initialize the client
firecrawl = FirecrawlApp(api_key="fc-e9135315fc1141dabc81c7e990c5bf0a")

# Define research parameters
params = {
    "maxDepth": 2,  # Number of research iterations
    "timeLimit": 180,  # Time limit in seconds
    "maxUrls": 6  # Maximum URLs to analyze
}

# Set up a callback for real-time updates
def on_activity(activity):
    print(f"[{activity['type']}] {activity['message']}")

# Run deep research
results = firecrawl.deep_research(
    query="各行业岗位技能组合的模块化分解方法",
    params=params,
    on_activity=on_activity
)

# Access research findings
print(f"Final Analysis: {results['data']['finalAnalysis']}")
print(f"Sources: {len(results['data']['sources'])} references") 