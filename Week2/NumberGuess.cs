using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
    class Program
    {
        static List<int> numberOfGuesses = new List<int>();
        public static int GenerateNumber()
        {
            Random randomNumber = new Random();
            return randomNumber.Next(1,100);
        }

        public string IsLessThanOrGreaterThanOrEqualToNumber(int number, int randomNumber)
        {
            if (number < randomNumber)
            {
                return "Less";

            }
            else if (number > randomNumber)
            {
                return "Greater";
            }
            else if (number == randomNumber)
            {
                return "Equal";
            }
            else
            {
                return "Invalid";
            }
        }
        
        public static List<int> AddToListOfGuessedNumbers(int number)
        {
    
            if (numberOfGuesses.Contains(number) == false)
            {
                numberOfGuesses.Add(number);
            }
            return numberOfGuesses;

        }
        static void Main(string[] args)
        {
            Program program = new Program();
            int guessedNumber = 0;
            int randomNumber = GenerateNumber();
            do
            {
                Console.WriteLine("Make a guess from 1 to 100: ");
                guessedNumber = Convert.ToInt32(Console.ReadLine());
                Program.AddToListOfGuessedNumbers(guessedNumber);
                
                if (program.IsLessThanOrGreaterThanOrEqualToNumber(guessedNumber, randomNumber) == "Less")
                {
                    Console.WriteLine("Wrong Guess! The number is less than correct number.");
                    
                }
                else if (program.IsLessThanOrGreaterThanOrEqualToNumber(guessedNumber, randomNumber) == "Greater")
                {
                    Console.WriteLine("Wrong Guess! The number is greater than correct number.");
                    
                }
                else if(program.IsLessThanOrGreaterThanOrEqualToNumber(guessedNumber, randomNumber) == "Equal")
                {
                    Console.WriteLine("Correct Guess!, You made " + Program.AddToListOfGuessedNumbers(guessedNumber).Count() + "attempts");
                }
            }
            while (program.IsLessThanOrGreaterThanOrEqualToNumber(guessedNumber, randomNumber) == "Less" || program.IsLessThanOrGreaterThanOrEqualToNumber(guessedNumber, randomNumber) == "Greater");
            Console.ReadKey();
        }
    }
}
