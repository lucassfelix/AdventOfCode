#include <iostream>
#include <fstream>
#include <sstream>
#include <map>
#include <set>
#include <vector>
#include <math.h>
#include <algorithm>
using namespace std;

#define DEBUG 0

int main()
{


    vector<long long> seeds;
    vector<bool> hasTransformed;

    string line, dummy;

    getline(cin,line);

    stringstream ss(line);

    long long seed, sourceStart, destStart,range;

    ss >> dummy;

    while (ss >> seed)
    {
#if DEBUG == 1
        //cout << seed << endl;
#endif
        seeds.push_back(seed);
        hasTransformed.push_back(false);
    }

    getline(cin,line);

    while (!cin.eof())
    {
        getline(cin,line);

        for (int i = 0; i < hasTransformed.size(); i++)
        {
            hasTransformed[i] = false;
        }
        

        while (line != "")
        {
            getline(cin,line);
#if DEBUG == 1
            cout << line << endl;
#endif
            stringstream ss(line);

            ss >> destStart >> sourceStart >> range;

#if DEBUG == 1
            cout << "Souce Start: " << sourceStart << endl;
            cout << "Dest Start: " << destStart << endl;
            cout << "Range: " << range << endl;

#endif

            for (int i = 0; i < hasTransformed.size(); i++)
            {
                if(hasTransformed[i])
                {
                    continue;
                }

                if(seeds[i] >= sourceStart && seeds[i] < sourceStart + range)
                {
#if DEBUG == 1
                    cout << "Seed " << seeds[i] << " transformed into ";
#endif

                    seeds[i] = seeds[i] - (sourceStart - destStart);
                    hasTransformed[i] = true;
#if DEBUG == 1
                    cout << seeds[i] << endl;
#endif
                }
            }
            
            if(cin.eof())
            {
                break;
            }
        }
    }

    int min = INT_MAX;
#if DEBUG == 1
    cout << endl << "Seeds at end:" << endl;
#endif
    for(int i = 0; i < seeds.size(); i++)
    {
#if DEBUG == 1
        cout << seeds[i] << endl;
#endif
        if (seeds[i] < min)
        {
            min = seeds[i];
        }
    };

    cout << min;


}