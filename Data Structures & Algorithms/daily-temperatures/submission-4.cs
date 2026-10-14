public class Solution {
    public int[] DailyTemperatures(int[] temperatures) {
       int[] res = new int [temperatures.Length];
            Stack<int[]> stack = new();
            for (int day = 0; day < temperatures.Length; day++)
            {
                int t = temperatures[day];
                while (stack.Count > 0 && t > stack.Peek()[0])
                {
                    int[] temp_pair = stack.Pop();
                    res[temp_pair[1]] = day - temp_pair[1];
                }
                stack.Push([t, day]);
            }
            return res; 
    }
}
