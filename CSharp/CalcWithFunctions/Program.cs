// <access level> <static or not> <return type> name(<args>) {}
// In console apps, we'll make all functions "static"
// Not static in Forms appsL always "public" though

static int add(int x, int y) { return x + y; }
static int sub(int x, int y) { return x - y; }
static int mul(int x, int y) { return x * y; }
static int div(int x, int y) { return x / y; }

static void wait() { // void means "returns nothing"
    Console.ReadLine();
    // return;
}

Random rand = new Random();
int n1 = rand.Next(1,101);
int n2 = rand.Next(150, 201);
Console.Write("Choose an option: add, sub, mul, or div: ");
string op = Console.ReadLine().ToLower();
int result = 0;
if (op == "add") result = add(n1, n2);
else if (op == "sub") result = sub(n1, n2);
else if (op == "mul") result = mul(n1, n2);
else if (op == "div") result = div(n1, n2);
else Console.WriteLine("ERROR");
Console.WriteLine("num1=" + n1 + "\t num2=" + n2);
Console.WriteLine("Result: " + result);
wait();