#include <iostream>
#include <fstream>
#include <sstream>
#include <map>
#include <set>
#include <vector>
#include <math.h>
#include <algorithm>

using namespace std;

#define DEBUG 1
#define ull unsigned long long
#define ll long long

struct Point
{
    int x = 0;
    int y = 0;
    Point(int newX, int newY)
    {
        x = newX;
        y = newY;
    }
    Point()
    {
        x = 0;
        y = 0;
    }
    void set(int newX, int newY)
    {
        x = newX;
        y = newY;
    }

    bool operator<(const Point& p) const
    {
        return x < p.x || y < p.y;
    }

    bool operator=(const Point &p) const{
        return x == p.x && y == p.y;
    }

    bool operator==(const Point &p) const{
        return x == p.x && y == p.y;
    }

    friend ostream &operator<<(ostream &out, const Point& p)
    {
        out << "(" << p.x << ","<<p.y << ")";
        return out;
    }
};

struct Pipe
{
    vector<Point> neighbours;
    friend ostream &operator<<(ostream &out, const Pipe& p)
    {
        out << "{ ";
        for (int i = 0; i < p.neighbours.size(); i++)
        {
            out <<  p.neighbours[i] << " ";
        }
        out << "}";
        return out;
    }
};

map<Point,Pipe> pipes;

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

            Pipe newPipe;
            Point current(x,y),p1,p2;
            vector<Point> n;
            switch (c)
            {
            case 'S':
                startingX = x;
                startingY = y;
                break;
            
            case '|':
                p1.set(x,y-1);
                p2.set(x,y+1);
                n.push_back(p1);
                n.push_back(p2);
                break;
            case '-':
                p1.set(x+1,y);
                p2.set(x-1,y);
                n.push_back(p1);
                n.push_back(p2);
                break;
            case '7':
                p1.set(x,y-1);
                p2.set(x-1,y);
                n.push_back(p1);
                n.push_back(p2);
                break;
            case 'F':
                p1.set(x,y-1);
                p2.set(x+1,y);
                n.push_back(p1);
                n.push_back(p2);
                break;
            case 'J':
                p1.set(x,y+1);
                p2.set(x-1,y);
                n.push_back(p1);
                n.push_back(p2);
                break;
            case 'L':
                p1.set(x,y+1);
                p2.set(x+1,y);
                n.push_back(p1);
                n.push_back(p2);
                break;
            
            default:
                continue;
                break;
            }
            newPipe.neighbours = n;

            pipes.insert({current, newPipe});
        }
        y++;
    }


    

    cout << "S is " << startingX << " , " << startingY << endl;

    //Get S neighbours
    vector<Point> n;
    Point p(startingX,startingY-1); 
    cout << map[p.y][p.x] << endl;
    if(pipes.count(p) == 1 && (map[p.y][p.x] == '|'|| map[p.y][p.x] == 'F'|| map[p.y][p.x] == '7'))
    {
        cout << "Found!"<<endl;
        n.push_back(p);
        p = *(new Point);
    }

    p.set(startingX,startingY+1); 
    cout << map[p.y][p.x] << " " << pipes.count(p) << endl;

    if(pipes.count(p) == 1 && (map[p.y][p.x] == '|'|| map[p.y][p.x] == 'L'|| map[p.y][p.x] == 'J'))
    {
        cout << "Found!"<<endl;
        n.push_back(p);
        p = *(new Point);
    }

    p.set(startingX+1,startingY); 
    cout << map[p.y][p.x] << endl;

    if(pipes.count(p) == 1 && (map[p.y][p.x] == '-'|| map[p.y][p.x] == 'F'|| map[p.y][p.x] == 'L'))
    {
        cout << "Found!"<<endl;
        n.push_back(p);
        p = *(new Point);
    }

    p.set(startingX-1,startingY); 
    cout << map[p.y][p.x] << endl;

    if(pipes.count(p) == 1 && (map[p.y][p.x] == '-'|| map[p.y][p.x] == 'J'|| map[p.y][p.x] == '7'))
    {
        cout << "Found!"<<endl;
        n.push_back(p);
        p = *(new Point);
    }

    Point s(startingX,startingY);

    pipes[s].neighbours = n;

    for(auto it = pipes.begin(); it != pipes.end(); it++)
    {
        cout << (*it).first << (*it).second << endl;
    }

}