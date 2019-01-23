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
            List<int> leapYears = new List<int>();
            Console.WriteLine("Enter the current year: ");
            int year = Convert.ToInt32(Console.ReadLine());

            do
            {
                if (year%400 == 0)
                {
                    leapYears.Add(year);
                    
                }
                else if (year%4 == 0 && year%100 != 0)
                {
                    leapYears.Add(year);
                }
                year++;
                

            }
            while (leapYears.Count() < 20);
            foreach (var years in leapYears)
            {
                Console.WriteLine("The next 20 leap years are: " + years);
            }
            Console.ReadKey();
        }
    }
}
