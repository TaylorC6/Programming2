using static System.Console;

Write("Enter Base: ");
double bas = double.Parse(ReadLine());
Write("Enter Length: ");
double height = double.Parse(ReadLine());

double hyp = Math.Sqrt(bas * bas + height * height);
double area = 0.5 * bas * height;

WriteLine("\nHypotenuse: " + Math.Round(hyp, 2));
WriteLine("Area: " + area);
WriteLine("Perimeter: " + Math.Round((bas + hyp + height), 2));
ReadLine();

