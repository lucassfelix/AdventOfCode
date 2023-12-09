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
#define ull unsigned long long
#define ll long long

bool zeroes(vector<ll> v)
{
    for(auto it = v.begin(); it != v.end(); it++)
    {
        if(*it != 0)
        {
            return false;
        }
    }
    return true;
}

int main()
{

#if DEBUG == 1
#endif

    string line;
    ll num, sum = 0, sumTwo = 0;

    while (!cin.eof())
    {

        getline(cin,line);
        stringstream stream(line);

        vector<vector<ll>> differences;
        vector<ll> diff;

        while (stream >> num)
        {
            diff.push_back(num);
        }
        differences.push_back(diff);
    
#if DEBUG == 1

        for(int i = 0; i < diff.size() -1 ; i++)
        {
            cout << diff[i] << " ";
        }

        cout << endl;

#endif

        while (diff.size() == 0 || !zeroes(diff))
        {
            diff = {};
            auto last = *(--differences.end());
            for(int i = 0; i < last.size() -1 ; i++)
            {
                diff.push_back(last[i+1] - last[i]);
            }
            differences.push_back(diff);
        }

        
#if DEBUG == 1
        cout << endl << "After diffs"<<endl;
        for (int i = 0; i < differences.size(); i++)
        {
            for (int j = 0; j < differences[i].size(); j++)
            {
                cout << differences[i][j] << " ";
            }
            cout << endl;
        }
#endif

        ll last;

        for (int i = differences.size()-2; i > 0; i--)
        {
            auto size = differences[i].size();
            auto lastElement = differences[i][size-1];
            auto otherSize = differences[i-1].size();
            auto otherLastElement = differences[i-1][otherSize-1];
#if DEBUG == 1

            cout << lastElement << " + " << otherLastElement << endl;
#endif

            last = otherLastElement + lastElement;
            differences[i-1].push_back(last);
        }
        
        sum += last;


        for (int i = differences.size()-2; i > 0; i--)
        {
            auto firstElement = differences[i][0];
            auto otherFirstElement = differences[i-1][0];
#if DEBUG == 1

            cout << otherFirstElement << " - " << firstElement << endl;
#endif

            last = otherFirstElement - firstElement;
            differences[i-1].insert(differences[i-1].begin(),last);
        }

        sumTwo += last;
#if DEBUG == 1

        cout << endl;

#endif



    }
    
    cout << sum << endl << sumTwo;

}