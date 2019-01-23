using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
    class Program
    {
        public static int SumOfNumbers(int number)
        {
            int sum = 0;
            for (int i = number; i > 0; i--)
            {
                sum = sum + i;
            }
            return sum;
        }

        public static int ProductOfNumbers(int number)
        {
            int product = 1;
            for (int i = number; i > 0; i--)
            {
                product = product * i;
            }
            return product;
        }
        static void Main(string[] args)
        {
            try
            {
                Console.WriteLine("Enter a number: ");
                int number = Convert.ToInt32(Console.ReadLine());
                Console.WriteLine("Enter 'S' to print the sum of all numbers from 1 to the number and 'M' to print the product of all numbers from 1 to the number.");
                string operation = Console.ReadLine();
                if (operation == "S")
                {
                    Console.WriteLine(Program.SumOfNumbers(number));
                }
                else if (operation == "M")
                {
                    Console.WriteLine(Program.ProductOfNumbers(number));
                }
                else
                {
                    Console.WriteLine("Invalid Input");

                }
            }
            catch(Exception e)
            {

            }
            
            Console.ReadKey();
        }
    }
}
