Console.WriteLine("Enter the mass of an object: ");
int mass = int.Parse(Console.ReadLine());
double weight = 0.0;
string msg = "";
if (mass > 10 && mass < 1000) {
    weight = mass * 9.8;
    msg = "The weight is " + weight;
}
else if (mass > 1000) {
    msg = "Too heavy!";
}
else if (mass < 10) {
    msg = "Too light!";
}
Console.WriteLine(msg);
Console.ReadLine();