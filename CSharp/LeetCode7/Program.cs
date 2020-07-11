using System;
using System.Linq;

namespace LeetCode7
{
    class Program
    {
        static void Main(string[] args)
        {

            Program test = new Program();

            int x = 123;
            int y = -123;

            int result = test.Reverse(y);

            Console.WriteLine(result);
            Console.ReadLine();
        }

        public int Reverse(int x)
        {

            int reversed = 0;

            //for positive x
            while(x > 0)
            {
                int pop = x % 10;
                x /= 10;
                if (reversed > Int32.MaxValue/10 || (reversed == Int32.MaxValue/10 && pop > 7))
                {
                    return 0;
                }
                
                if (reversed < Int32.MinValue/10 || (reversed == Int32.MinValue/10 && pop < -8))
                {
                    return 0;
                }
                reversed = reversed * 10 + pop;
            }

            //for negative x
            while (x < 0 )
            {
                int pop = x % 10;
                x /= 10;
                if (reversed > Int32.MaxValue / 10 || (reversed == Int32.MaxValue / 10 && pop > 7))
                {
                    return 0;
                }

                if (reversed < Int32.MinValue / 10 || (reversed == Int32.MinValue / 10 && pop < -8))
                {
                    return 0;
                }
                reversed = reversed * 10 + pop;
            }

            return reversed;

        }
    }
}
