public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> seen = [];
        for(int index = 0; index < nums.Length; index++)
        {
            int current = nums[index];
            int compliment = target - current;
            if (seen.ContainsKey(compliment))
            {
                return [seen[compliment], index];
            }
            seen.Add(current, index);
        }
        return [];
    }
}
