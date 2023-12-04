#include <iostream>
#include <fstream>
#include <sstream>
#include <map>
#include <set>
#include <vector>
#include <math.h>
using namespace std;

#define DEBUG 0

int main()
{

#if DEBUG == 1
#endif

    string dummy, strNum, line;
    int num, wins, sum = 0, currentScratch = 0, secondSum = 0;

    set<int> winningNumbers;
    vector<int> copies(198,0);

    while (!cin.eof())
    {
        getline(cin,line);
        istringstream sstream(line);

        wins = -1;
        winningNumbers.clear();

        sstream >> dummy >> dummy;
    
        copies[currentScratch] += 1;

        sstream >> strNum;
        while (strNum != "|")
        {
            num = stoi(strNum);
            winningNumbers.insert(num);
            sstream >> strNum;
        }
        while (sstream >> num)
        {
            if(winningNumbers.count(num) == 1)
            {
#if DEBUG == 1
                cout << "Found winning: " << num << endl;
#endif

                wins++;
            }
        }
#if DEBUG == 1
        cout << endl;
#endif

        for (int i = 0 ; i < copies.size() && i < (wins+1); i++)
        {
            copies[currentScratch + i + 1] += copies[currentScratch];
        }

        if (wins != -1)
        {
            sum += pow(2,wins);
        }
        currentScratch++;
    }

    cout << "First Star:" << sum << endl;
    for (int i = 0; i < copies.size(); i++)
    {
#if DEBUG == 1
        cout << i << ": " << copies[i] << endl;
#endif
        secondSum += copies[i];
    }
    
    cout << "Second Star:" << secondSum << endl;

    

}