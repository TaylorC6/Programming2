//List<type> var = new List<type>() { x, y, z };
// List<string> text = [];
// List<string> lines = new List<string>();

// List<int> nums = [1, 2, 3];

List<int> nums = new List<int>() { 1, 2, 3 };

nums.Add(4);
nums.Add(5);
nums.Add(6);
nums.Add(7);
nums.RemoveAt(5); // Removes 6
nums.Remove(7); // Removes 7
Console.WriteLine("Length: " + nums.Count);
Console.WriteLine(string.Join(", ", nums)); // "1, 2, 3, 4, 5

Console.WriteLine("foreach:");
foreach (int n in nums)
    Console.WriteLine(n);

Console.ReadLine();

// Look at C# Documentation on MSDN for all List methods