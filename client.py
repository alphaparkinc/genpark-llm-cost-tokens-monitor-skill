class LLMCostTokensMonitorClient:
    def estimate(self, input_tokens: int, output_tokens: int) -> dict:
        return {"estimated_cost_usd": round((input_tokens * 0.000005) + (output_tokens * 0.000015), 5)}