using System;

namespace LeetCode771
{
    class Program
    {
        static void Main(string[] args)
        {

            string j = "aA";
            string s = "aAAbbbb";

            //should output 3

            Program test = new Program();

            Console.WriteLine(test.NumJewelsInStones(j, s));


            Console.WriteLine("Hello World!");
        }

        public int NumJewelsInStones(string J, string S)
        {

            int noOfJewels = 0;

            char[] jChars = J.ToCharArray();
            char[] sChars = S.ToCharArray();
            

            for (int i = 0; i < jChars.Length; i++)
            {
                for (int j = 0; j < sChars.Length; j++)
                {
                    if (jChars[i] == sChars[j])
                    {
                        noOfJewels += 1;
                    }
                    //Console.WriteLine("j: {0}, s: {1}", jChars[i], sChars[j]);
                }
            }

            return noOfJewels;
        }
    }
}
