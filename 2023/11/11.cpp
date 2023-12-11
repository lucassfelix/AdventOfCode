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
#define Point pair<int,int>

int manhhatan(Point a, Point b)
{
    return abs(a.first-b.first) + abs(a.second-b.second);
}

int main()
{

#if DEBUG == 0
#endif

    vector<string> universe;
    set<int> emptyColumns;
    set<int> emptyRows;
    string line;
    
    bool empty;
    int lineIndex = 0;
    
    while(!cin.eof())
    {

        getline(cin,line);
        if(count(line.begin(),line.end(),'#') == 0)
        {
            emptyRows.insert(lineIndex);
        }
        universe.push_back(line);
        lineIndex++;
    }


    for(int i = 0; i < universe[0].size();i++)
    {
        empty = true;
        for(int j = 0; j < universe.size();j++)
        {
            if(universe[j][i] == '#')
            {
                empty = false;
                break;
            }
        }
        if(empty)
        {
            emptyColumns.insert(i);
        }
    }

    vector<Point> galaxies;

    for(int i = 0; i < universe.size();i++)
    {
        for(int j = 0; j < universe[i].size();j++)
        {
            if(universe[i][j] == '#')
            {
                galaxies.push_back({j,i});
            }
        }
    }


#if DEBUG == 1
    cout << "Collumns: ";
    for(auto it = emptyColumns.begin(); it != emptyColumns.end();it++)
    {
        cout << *(it) << " ";
    }
    cout << endl;
    cout << "Rows: ";
    for(auto it = emptyRows.begin(); it != emptyRows.end();it++)
    {
        cout << *(it) << " ";
    }
    cout << endl;
#endif

    int sumStarOne = 0;
    ull sumStarTwo = 0;

    int expansionOne = 1;
    ull expansionTwo = 999999ull;

    for(int i = 0; i < galaxies.size();i++)
    {
        for(int j = i+1; j < galaxies.size();j++)
        {
            auto a = galaxies[i];
            auto b = galaxies[j];
            int auxSumOne = 0;
            ull auxSumTwo = 0ull;
            auxSumOne += manhhatan(a,b);
            auxSumTwo += manhhatan(a,b);
#if DEBUG == 1

            cout << endl<< "(" << a.first << "," << a.second << ") and (" << b.first << "," << b.second <<")"<<endl;
            cout << "Manhhatan = " << manhhatan(a,b) << endl;

            cout << "Columns" << endl;
#endif

            for(auto it = emptyColumns.begin(); it != emptyColumns.end();it++)
            {
                auto c = *it;
                auto biggest = a.first > b.first ? a : b;
                auto smallest = a.first > b.first ? b : a;
#if DEBUG == 1
                cout << c << " " <<smallest.first<< "," << biggest.first;
#endif
                if(smallest.first < c && biggest.first > c)
                {
#if DEBUG == 1
                    cout  << " OK!";
#endif
                    auxSumOne += expansionOne;
                    auxSumTwo += expansionTwo;
                }
#if DEBUG == 1
                cout  << endl;
#endif

            }
#if DEBUG == 1
            cout << "Rows" << endl;
#endif
            for(auto it = emptyRows.begin(); it != emptyRows.end();it++)
            {
                auto c = *it;
                auto biggest = a.second > b.second ? a : b;
                auto smallest = a.second > b.second ? b : a;
#if DEBUG == 1
                cout << c << " " <<smallest.second<< "," << biggest.second;
#endif
                if(smallest.second < c && biggest.second > c)
                {
#if DEBUG == 1
                    cout  << " OK!";
#endif
                    auxSumOne += expansionOne;
                    auxSumTwo += expansionTwo;
                }
#if DEBUG == 1
                cout  << endl << "Total Sum One = " << auxSumOne << endl << "Total Sum Two = " << auxSumTwo << endl;
#endif  
            }
            sumStarOne += auxSumOne;
            sumStarTwo += auxSumTwo;
        }
    }

#if DEBUG == 1
    for(int i = 0; i < universe.size();i++)
    {
        cout << universe[i] << endl;
    }
#endif

    cout << sumStarOne << endl << sumStarTwo;
}