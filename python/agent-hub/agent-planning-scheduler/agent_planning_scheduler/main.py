from mofa.agent_build.base.base_agent import MofaAgent, run_agent

# planning_result =  [{'connector_name': 'crawl4ai-connector', 'urls': ['https://www.deepseek.com', 'https://careers.deepseek.com'],'send_status':True}, {'connector_name': 'selenium-connector', 'urls': ['https://blog.deepseek.com', 'https://github.com/deepseek-ai'],'send_status':True}]
@run_agent
def run(agent:MofaAgent):
    agent_planning_data = agent.receive_parameter('agent_planning_result')
    print('agent_planning_data:',agent_planning_data)
    recive_node_ids = []
    if len(agent_planning_data) >0:
        for send_data in agent_planning_data: recive_node_ids.append(send_data.get('send_node_id'))
    if len(recive_node_ids):
        all_recive_data = agent.receive_parameters(recive_node_ids)
        print('all_recive_data:',all_recive_data)
    agent.send_output('agent_planning_scheduler_result',all_recive_data)


def main():
    agent = MofaAgent(agent_name='agent-planning-agent')
    run(agent=agent)
if __name__ == "__main__":
    main()
