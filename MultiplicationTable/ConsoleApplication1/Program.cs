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
            for (int i = 1; i <= 12; i++)
            {
                Console.WriteLine("Table for " + i + " times. \n" );
                for (int j = 1; j <= 12; j++)
                {
                    Console.WriteLine(i + " x " + j + " = " + i * j);
                }
                
            }
        }
        static void Main(string[] args)
        {
            Program.Multiplier();
            Console.ReadKey();
        }
    }
}
