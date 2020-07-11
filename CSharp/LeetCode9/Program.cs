using System;

namespace LeetCode9
{
    class Program
    {
        static void Main(string[] args)
        {
            int x = 323;
            string numToString = x.ToString();
            char[] stringToCharArr = numToString.ToCharArray();
            Array.Reverse(stringToCharArr);

            string reversedNumToString = new string(stringToCharArr);

            if(numToString == reversedNumToString)
            {
                Console.WriteLine("True");
            }
            else
            {
                Console.WriteLine("Nah mate"); 
            }

        }

        public bool IsPalindrome(int x)
        {
            string numToString = x.ToString();
            char[] stringToCharArr = numToString.ToCharArray();
            Array.Reverse(stringToCharArr);

            string reversedNumToString = new string(stringToCharArr);

            if (numToString == reversedNumToString)
            {
                return true;
            }
            else
            {
                return false;
            }


        }
    }
}
