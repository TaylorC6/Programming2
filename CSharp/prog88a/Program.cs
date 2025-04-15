Console.Write("Enter number 1: ");
int num1 = int.Parse(Console.ReadLine());
Console.Write("Enter number 2: ");
int num2 = int.Parse(Console.ReadLine());

int sum = num1 + num2;
int dif = num1 - num2;
int prd = num1 * num2;
double avg = sum / 2.0;
int abs = Math.Abs(dif);
// Math.Max() / Math.Min()
int max, min;

if (num1 > num2)
{
    max = num1;
}   else
    {
    max = num2;
    }

if (num1 <= num2)
    min = num1;
else min = num2;
// else if

Console.WriteLine("Sum: " + sum);
Console.WriteLine("Difference: " + dif);
Console.WriteLine("Product: " + prd);
Console.WriteLine("Average: " + avg);
Console.WriteLine("Absolute value: " + abs);
Console.WriteLine("Maximum: " + max);
Console.WriteLine("Minimum: " + min);
Console.ReadLine();