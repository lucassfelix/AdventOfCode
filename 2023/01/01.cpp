#include <iostream>
#include <fstream>
using namespace std;


int main()
{
    string line;    
    char firstDigit, lastDigit;
    int lineSize, sum = 0;

    while (!cin.eof())
    {
        cin >> line;

        firstDigit = 'a';
        lastDigit = 'a';
        lineSize = line.size();

        for (int i = 0; i < lineSize; i++)
        {
            if(firstDigit != 'a' && lastDigit != 'a')
            {
                break;
            }

            if (firstDigit == 'a')
            {
                if (isdigit(line[i]))
                {
                    firstDigit = line[i];
                }
            }

            if (lastDigit == 'a')
            {
                if (isdigit(line[lineSize-i-1]))
                {
                    lastDigit = line[lineSize-i-1];
                }
            }
        }
        
        cout << firstDigit << lastDigit << endl;

        sum += (firstDigit - '0') * 10;
        sum += lastDigit - '0';
    }
    
    cout << sum;
    
}