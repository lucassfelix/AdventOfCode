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

struct Seed
{
    ull source;
    ull end;
};

struct Range
{
    ull sourceStart;
    ull destStart;
    ull range;
};

ull getLowestReverseConvertion(ull num,const vector<Range> map)
{
    if (num < map[0].destStart)
    {
        return num;
    }
    

    for (int i = 0; i < map.size(); i++)
    {
        if (num >= map[i].destStart && num < (map[i].destStart + map[i].range))
        {
            #if DEBUG == 1
            cout << "Transformation: " << num << " Dest: " << map[i].destStart << " Source: " << map[i].sourceStart << endl;
            #endif
            
            auto aux = map[i].destStart - map[i].sourceStart;
            return num - aux;
            
        }
    }

    return num;
}

bool isSeed(ull value, vector<Seed> seeds)
{
    for (int i = 0; i < seeds.size(); i++)
    {
        if(value >= seeds[i].source && value < seeds[i].end)
        {
            return true;
        }
    }

    return false;
    
}

int main()
{
    vector<Seed> seeds;

    vector<vector<Range>> maps;

    string line, dummy;

    getline(cin,line);

    stringstream ss(line);

    ull seed, sourceStart, destStart,range;

    ss >> dummy;

    while (ss >> seed)
    {
        ss >> range;
        Seed newS;
        newS.source = seed;
        newS.end = seed + range;
        seeds.push_back(newS);
    }


    getline(cin,line);

    while (!cin.eof())
    {
        getline(cin,line);

        vector<Range> map;

        while (line != "")
        {
            getline(cin,line);

            if(line == "")
            {
                break;
            }
#if DEBUG == 1
            cout << "Line:" << line << endl;
#endif
            stringstream ss(line);

            ss >> destStart >> sourceStart >> range;

            Range r;
            r.destStart = destStart;
            r.sourceStart = sourceStart;
            r.range = range;

            map.push_back(r);
    
            if(cin.eof())
            {
                break;
            }
        }

        sort(map.begin(),map.end(), [](const Range &a, const Range &b)
        {
            return a.destStart < b.destStart;
        });

        maps.push_back(map);
    }


    auto lastMap =  maps[maps.size()-1];
    auto lastRange = lastMap[lastMap.size()-1];

#if DEBUG == 1
    for_each(seeds.begin(), seeds.end(), [](const Seed &s)
    {
        cout << "Source: " << s.source << " Range:" << s.end << endl;
    });
#endif

#if DEBUG == 1
    for_each(maps.begin(), maps.end(), [](const vector<Range> &v)
    {
    cout << v.size() << endl;
        for_each(v.begin(), v.end(), [](const Range &r)
        {
            cout << r.destStart << " "<< r.sourceStart << " " << r.range<< endl;
        });
        cout << endl;
    });
#endif

    for (ull i = 0; i < lastRange.destStart + lastRange.range; i++)
    {
        ull value = i;
#if DEBUG == 1
        cout << "Starting as: " << value << endl;
#endif
        if(i % 10000000 == 0)
        {
            cout << "Loading...  "  << i << endl;
        }

        for (int map = maps.size()-1; map >= 0; map--)
        {
            value = getLowestReverseConvertion(value, maps[map]);
#if DEBUG == 1
            cout << map << ":" << value << endl;
#endif

        }

        if(isSeed(value,seeds))
        {
            cout << "Seed found: " << value << endl;
            cout << "Lowest location: " << i << endl;
            return 1;
        }

    }
    


    
}