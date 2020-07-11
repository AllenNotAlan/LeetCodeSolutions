using System;

namespace LeetCode1
{
    class Program
    {
        public int[] TwoSum(int[] nums, int target)
        {
            int[] result = new int[2];
            for (int i = 0; i < nums.Length; i++)
            {
                for (int j = i + 1; j < nums.Length; j++)
                {
                    if (nums[i] + nums[j] == target)
                    {
                        result[0] = i;
                        result[1] = j;
                    }
                }
            }
            return result;

        }

        static void Main(string[] args)
        {


            int[] nums = {2, 7, 11, 15};
            int target = 9;

            Program twoSum = new Program();

            
            int[] result = twoSum.TwoSum(nums, target);

            for(int i = 0; i < result.Length; i++)
            {
                Console.WriteLine(result[i]);
            }

            Console.ReadLine();
        }
    }
}
