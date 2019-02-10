using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
    class Program
    {
        public static bool IsPrime(long number)
        {
            if (number <= 1)
                return false;
            if (number == 2)
                return true;
            if (number % 2 == 0)
                return false;

            var bounds = (int)Math.Floor(Math.Sqrt(number));
            for (int i = 3; i <= bounds; i += 2)
            {
                if (number % i == 0)
                {
                    return false;
                }
            }
            return true;
        }
        static void Main(string[] args)
        {
            for (long number = 1; number <= long.MaxValue; number++)
            {
                if (IsPrime(number) == true)
                {
                    Console.WriteLine(number + " is a prime number.");
                    
                }
            }
           
            Console.ReadKey();
        }
    }
}
