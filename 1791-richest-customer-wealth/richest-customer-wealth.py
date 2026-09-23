class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth = 0
        for cust in accounts:
            current_wealth=0
            for money in cust:
                current_wealth += money
            if current_wealth > max_wealth:
                max_wealth = current_wealth 
        return max_wealth