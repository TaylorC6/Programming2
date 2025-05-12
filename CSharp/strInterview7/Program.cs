Console.Write("Enter a string: ");
string word = Console.ReadLine().ToLower();

int vowel = 0;
int cons = 0;

for (int i = 0; i < word.Length; i++) {
    char let = word[i];
    if (let == 'a' || let == 'e' || let == 'i' || let == 'o' || let == 'u')
        vowel++;
    else if (let >= 'a' && let <= 'z') cons++;
}

Console.WriteLine("{0} contains {1} vowels and {2} consonats",
                    word, vowel, cons);
Console.ReadLine();