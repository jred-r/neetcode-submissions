public class Solution {
    public bool hasDuplicate(int[] nums) {
        HashSet<int> hset = new();
        foreach (var item in nums){
            if(hset.Contains(item)){
                return true;
            }
            else{
                hset.Add(item);
            }
        }
        return false;        
    }
}