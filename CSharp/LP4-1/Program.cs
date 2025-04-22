Console.Write("Enter # of Copies to Print: ");
int copies = int.Parse(Console.ReadLine());
double price = 0;
double cost = 0;
// && AND      || OR      ! NOT
if (copies > 0 && copies <= 99) price = 0.30;
else if (copies > 99 && copies <= 499) price = 0.28;
else if (copies > 499 && copies <= 749) price = 0.27;
else if (copies > 749 && copies <= 1000) price = 0.26;
else if (copies > 1000) price = 0.25;
else Console.WriteLine("Invalid # of Copies!");

Console.WriteLine("Your Price Per Copy is: " + price);
Console.WriteLine("Your Total Price is: $" + price * copies);
Console.ReadLine();
