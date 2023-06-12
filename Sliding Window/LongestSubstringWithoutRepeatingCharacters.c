// https://leetcode.com/problems/longest-substring-without-repeating-characters/

int lengthOfLongestSubstring(char *s)
{
    int length;
    int left;
    int right;
    int maxLength;
    left = 0;
    right = 1;
    length = 1;
    maxLength = 1;
    if (strlen(s) == 0)
    {
        return 0;
    }
    for (int i = 1; i < strlen(s); i++)
    {
        if ((s[i] - 'a') != (s[i - 1] - 'a'))
        {
            length = 1;
            for (int j = i - 1; j >= left; j--)
            {
                if ((s[i] - 'a') == (s[j] - 'a'))
                {
                    left = j + 1;
                    break;
                }
                else
                {
                    length++;
                }
            }
            if (maxLength < length)
            {
                maxLength = length;
            }
            right++;
        }
        else
        {
            left = right;
            right++;
        }
    }
    return maxLength;
}
