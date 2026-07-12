from client import LLMCostTokensMonitorClient
client = LLMCostTokensMonitorClient()
print(client.estimate(1000, 500))