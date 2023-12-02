#include <iostream>
#include <fstream>
#include <map>
using namespace std;

#define DEBUG 0

#define MAX_RED 12
#define MAX_GREEN 13
#define MAX_BLUE 14

int main()
{
    string color, dummy;
    char endToken;
    int id, num, sum = 0, secondStarSum = 0;

    bool possible;

    map<string,int> colorMax {{"green",MAX_GREEN}, {"blue",MAX_BLUE}, {"red", MAX_RED}};
    map<string,int> maxColor;

    while (!cin.eof())
    {
        endToken = 'a';
        possible = true;

        cin >> dummy >> id >> dummy;

        #if DEBUG == 1
            cout << "ID:" << id << endl;
        #endif

        maxColor = {{"green",0}, {"blue",0}, {"red", 0}};

        while (endToken != 'x')
        {
            cin >> num >> color;

            endToken = color[color.size()-1];
            if(endToken == ';' || endToken == ',')
            {
                color.erase(color.size()-1);
            }
            else
            {
                endToken = 'x';
            }

            #if DEBUG == 1
                cout << num <<  color << endToken << endl;
            #endif

            if(num > maxColor[color])
            {
                maxColor[color] = num;
            }

            if(num > colorMax[color])
            {
                possible = false;
            }    
        }

        if (possible)
        {
            sum += id;
        }

        #if DEBUG == 1
                cout <<  maxColor["green"] << " " << maxColor["blue"] << " " << maxColor["red"] << endl;
        #endif

        secondStarSum += maxColor["green"] * maxColor["blue"] * maxColor["red"];
        
    }
    

    cout << sum << endl;
    cout << secondStarSum;
}