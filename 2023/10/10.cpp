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

map<pair<int,int>,vector<pair<int,int>>> pipes;

int main()
{

#if DEBUG == 1
#endif

    vector<string> map;
    string line;
    int startingX = 0, startingY = 0, y = 0;
    while(!cin.eof())
    {
        getline(cin,line);
        map.push_back(line);
        
        for (int x = 0; x < line.size(); x++)
        {
            auto c = line[x];
            if(c == '.')
            {
                continue;
            }

            pair<int,int> current(x,y),p1,p2;
            vector<pair<int,int>> n;
            switch (c)
            {
            case 'S':
                startingX = x;
                startingY = y;
                break;
            
            case '|':
                p1 = {x,y-1};
                p2 = {x,y+1};
                n.push_back(p1);
                n.push_back(p2);
                break;
            case '-':
                p1 = {x+1,y};
                p2 = {x-1,y};
                n.push_back(p1);
                n.push_back(p2);
                break;
            case '7':
                p1 = {x,y+1};
                p2 = {x-1,y};
                n.push_back(p1);
                n.push_back(p2);
                break;
            case 'F':
                p1 = {x,y+1};
                p2 = {x+1,y};
                n.push_back(p1);
                n.push_back(p2);
                break;
            case 'J':
                p1 = {x,y-1};
                p2 = {x-1,y};
                n.push_back(p1);
                n.push_back(p2);
                break;
            case 'L':
                p1 = {x,y-1};
                p2 = {x+1,y};
                n.push_back(p1);
                n.push_back(p2);
                break;
            
            default:
                continue;
                break;
            }

            pipes.insert({current, n});
        }
        y++;
    }

    //Get S neighbours
    vector<pair<int,int>> n;
    pair<int,int> p(startingX,startingY-1); 
    if(pipes.count(p) == 1 && (map[p.second][p.first] == '|'|| map[p.second][p.first] == 'F'|| map[p.second][p.first] == '7'))
    {
        n.push_back(p);
        p = *(new pair<int,int>);
    }

    p = {startingX,startingY+1}; 

    if(pipes.count(p) == 1 && (map[p.second][p.first] == '|'|| map[p.second][p.first] == 'L'|| map[p.second][p.first] == 'J'))
    {
        n.push_back(p);
        p = *(new pair<int,int>);
    }

    p = {startingX-1,startingY}; 

    if(pipes.count(p) == 1 && (map[p.second][p.first] == '-'|| map[p.second][p.first] == 'F'|| map[p.second][p.first] == 'L'))
    {
        n.push_back(p);
        p = *(new pair<int,int>);
    }

    p = {startingX+1,startingY}; 

    if(pipes.count(p) == 1 && (map[p.second][p.first] == '-'|| map[p.second][p.first] == 'J'|| map[p.second][p.first] == '7'))
    {
        n.push_back(p);
        p = *(new pair<int,int>);
    }

    pair<int,int> s(startingX,startingY);

    pipes[s] = n;


#if DEBUG == 1
    for(auto it = pipes.begin(); it != pipes.end(); it++)
    {
        auto p = (*it).first;
        auto n  = (*it).second;
        cout << "(" << p.first << "," << p.second <<") { ";
        for (int i = 0; i < n.size(); i++)
        {
            cout << "(" << n[i].first << "," << n[i].second <<") ";
        }
        cout <<"}"<<endl;
        
    }
#endif


    int steps = 1;

    Point lastC =s;
    Point c = pipes[s][0];

    while (c != s)
    {
#if DEBUG == 1
        cout << "ON " << c.first << "," << c.second << endl;
#endif
        for (int i = 0; i < pipes[c].size(); i++)
        {
            if (pipes[c][i] == lastC)
            {
#if DEBUG == 1

                cout << "\t" << "N is last " << pipes[c][i].first << "," << pipes[c][i].second << endl;
#endif
                continue;
            }
#if DEBUG == 1

            cout << "\t" << "N is next " << pipes[c][i].first << "," << pipes[c][i].second << endl;
#endif            
            lastC = c;
            c = pipes[c][i];
            steps++;
            break;
        }
    }

    cout << "Steps: " << steps << endl;;
    cout << "Star one: " << steps/2;
    
}
