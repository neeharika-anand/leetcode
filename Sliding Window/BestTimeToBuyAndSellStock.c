// Link - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
int maxProfit(int *prices, int pricesSize)
{
    int left = 0;
    int right = 1;
    int max = 0;
    int tempmax;

    while (right != pricesSize)
    {
        if (prices[left] < prices[right])
        {
            tempmax = prices[right] - prices[left];
            if (tempmax > max)
            {
                max = tempmax;
            }
            right = right + 1;
        }
        else
        {
            left = right;
            right = right + 1;
        }
    }
    return max;
}
