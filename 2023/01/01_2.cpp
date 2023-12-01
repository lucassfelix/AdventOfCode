#include <iostream>
#include <fstream>
#include <map>
using namespace std;

#define DEBUG 1

int main()
{
    string line, sub;
    char firstDigit, lastDigit;
    int lineSize, sum = 0;

    map<string, char> digits{
        {"one", '1'},
        {"two", '2'},
        {"three", '3'},
        {"four", '4'},
        {"five", '5'},
        {"six", '6'},
        {"seven", '7'},
        {"eight", '8'},
        {"nine", '9'}};

    while (!cin.eof())
    {
        cin >> line;

        firstDigit = 'a';
        lastDigit = 'a';
        lineSize = line.size();
#if DEBUG == 1
        cout << "Line Size:" << lineSize << endl;
#endif
        for (int i = 0; i < lineSize; i++)
        {
            if (firstDigit != 'a' && lastDigit != 'a')
            {
                break;
            }

            if (firstDigit == 'a')
            {
#if DEBUG == 1
                cout << "First digit check" << endl;
#endif
                if (isdigit(line[i]))
                {
                    firstDigit = line[i];
                }
                else if (i+3 < lineSize && digits.count(sub = line.substr(i, 3)))
                {
                    firstDigit = digits[sub];
#if DEBUG == 1
                    cout << sub << endl;
#endif
                }
                else if (i+4 < lineSize &&digits.count(sub = line.substr(i, 4)))
                {
                    firstDigit = digits[sub];
#if DEBUG == 1
                    cout << sub << endl;
#endif
                }
                else if (i+5 < lineSize &&digits.count(sub = line.substr(i, 5)))
                {
                    firstDigit = digits[sub];
#if DEBUG == 1
                    cout << sub << endl;
#endif
                }
            }

            if (lastDigit == 'a')
            {
#if DEBUG == 1
                cout << "Last digit check" << endl;
#endif
                if (isdigit(line[lineSize - i - 1]))
                {
                    lastDigit = line[lineSize - i - 1];
                }
                else if (lineSize-i-3 >= 0 && digits.count(sub = line.substr(lineSize - i - 3, 3)))
                {
                    lastDigit = digits[sub];
#if DEBUG == 1
                    cout << sub << endl;
#endif
                }
                else if (lineSize-i-4 >= 0 && digits.count(sub = line.substr(lineSize - i - 4, 4)))
                {
                    lastDigit = digits[sub];
#if DEBUG == 1
                    cout << sub << endl;
#endif
                }
                else if (lineSize-i-5 >= 0 &&digits.count(sub = line.substr(lineSize - i - 5, 5)))
                {
                    lastDigit = digits[sub];
#if DEBUG == 1
                    cout << sub << endl;
#endif
                }
            }
        }
#if DEBUG == 1
        std::cout << firstDigit << lastDigit << endl;
#endif
        sum += (firstDigit - '0') * 10;
        sum += lastDigit - '0';
    }

    std::cout << sum;
}