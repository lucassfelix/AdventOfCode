#include <iostream>
#include <fstream>
#include <sstream>
#include <map>
#include <set>
#include <vector>
#include <math.h>
using namespace std;

#define DEBUG 0

#define ull unsigned long long

struct Race{
    ull time;
    ull dist;
};

ull getWinningWays(Race r)
{
    ull sum = 0;
    for (ull i = 0; i <= r.time/2; i++)
    {
        #if DEBUG == 1
        cout << i << " * " << r.time-i << " > " << r.dist;
        #endif
        if(i * (r.time - i) > r.dist)
        {
            #if DEBUG == 1
            cout << " YES "  << endl;
            #endif
            sum++;
        }
            #if DEBUG == 1
        else
        {
            cout << " NO"  << endl;
        }
            #endif
    }
    if(r.time % 2 == 0 )
    {
        return (sum*2) - 1;
    }
    else
    {
        return sum*2;
    }
}

int main()
{

#if DEBUG == 1
#endif

    string line, dummy;

    ull time, dist, index;
    vector<Race> races;




    getline(cin,line);
    stringstream ss(line);

    ss >> dummy;

    while (ss >> time)
    {
        Race r;
        r.time = time;
        races.push_back(r);
    }

#if DEBUG == 1
    cout << "Read Times" << endl;
#endif

    getline(cin,line);
    stringstream so(line);
    so >> dummy;


    index = 0;
    while (so >> dist)
    {
        races[index].dist = dist;
        index++;
    }

    #if DEBUG == 1
    cout << "Read Distance" << endl;
#endif

    #if DEBUG == 1
    cout << "Races size: " << races.size() << endl;
#endif
    



    ull mult = 1;
    for (auto it = races.begin();it != races.end(); it++)
    {
        auto aux = getWinningWays(*it);
        mult *= aux ;
 #if DEBUG == 1
       cout << "Result: " << aux << endl;
#endif
    }
    
    cout << mult;

}