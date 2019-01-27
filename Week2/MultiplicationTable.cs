using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
    class Program
    {
        public static void Multiplier()
        {
            Console.WriteLine("Multiplication table from 1 to 12 times");
            for (int i = 1; i <= 12; i++)
            {
                Console.WriteLine();
                for (int j = 1; j <= 12; j++)
                {
                    Console.Write("{0}", (i * j).ToString().PadRight(4));

                }
                Console.Write("\n");

            }
        }
        static void Main(string[] args)
        {
            Program.Multiplier();
            Console.ReadKey();
        }
    }
}
