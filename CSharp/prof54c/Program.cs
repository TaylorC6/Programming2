using static System.Console;

Write("Enter Radius: ");
double rad = double.Parse(ReadLine());

double area = Math.PI * Math.Pow(rad, 2);
double circ = rad * 2.0 * Math.PI;

WriteLine("Area: " + Math.Round(area, 3));
WriteLine("Circumference: " + Math.Round(circ, 3));
ReadKey();