using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
    class Program
    {

        static void Main(string[] args)
        {
            for (long i = 1; i <= long.MaxValue; i++)
            {
                if (i%i == 0 && i%1 == 0)
                {
                    Console.WriteLine(i + " is a prime number.");
                    
                }
            }
           
            Console.ReadKey();
        }
    }
}
