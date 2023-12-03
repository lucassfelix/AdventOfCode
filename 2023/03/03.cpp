#include <iostream>
#include <fstream>
#include <map>
#include <set>
#include <vector>
using namespace std;

#define DEBUG 0

struct Number
{
    pair<int,int> start;
    pair<int,int> end;
    int number;


};

pair<int,int> findNumStart(pair<int,int> digitIndex, vector<string> matrix)
{
    int row = digitIndex.first, col = digitIndex.second;
    while (isdigit(matrix[row][--col]))
    {
        
    }

    #if DEBUG == 1
    cout << "Number start is : " << row <<  " " << col + 1 << endl;
    #endif

    return {row,col + 1};   
}

int getGearRatio(pair<int,int> gearIndex, vector<string> matrix, map<pair<int,int>,int> numbers)
{
    #if DEBUG == 1
            cout << "checking adjacent for: " << gearIndex.first <<  " " << gearIndex.second << endl;

            cout << "Map size" << numbers.size() << endl;
#endif

    set<pair<int,int>> adjacent;
    for (int row = gearIndex.first -1 ; row <= gearIndex.first + 1; row++)
    {
        for (int col = gearIndex.second -1 ; col <= gearIndex.second + 1; col++)
        {
            if(row < 0 || row >= matrix.size() || col < 0 || col >= matrix[row].size())
            {
                continue;
            }

            if(isdigit(matrix[row][col]))
            {
                #if DEBUG == 1
                cout << "found digit at: " << row <<  " " << col << endl;
                #endif
                auto pair = findNumStart({row,col},matrix);
                cout << "Pair found is " << pair.first << " " << pair.second <<  endl;
                adjacent.insert(pair);
            }
        }
    }

    if(adjacent.size() == 2)
    {
        #if DEBUG == 1
        cout << "Two numbers found" << endl ;
        #endif
        int mult = 1;
        for (auto it = adjacent.begin(); it != adjacent.end(); it++)
        {
            int first = (*it).first;
            int second = (*it).second;

            
            cout << "Num is: " << numbers[{first,second}] << endl;
            mult = mult * numbers[*it];
        }
        cout << "Mult is: " << mult << endl<< endl;
        return mult;
    }

    cout << adjacent.size() << " numbers found" << endl << endl;
    
    return 0;

}

bool HasAdjacentSymbol(Number num, vector<string> matrix)
{

#if DEBUG == 1
            cout << "checking adjacent for: " << num.number << " " << num.start.second <<  " " << num.end.second << endl;
#endif

    for (int row = num.start.first - 1 ; row <= num.end.first + 1; row++)
    {
        for (int col = num.start.second - 1; col <= num.end.second + 1 ; col++)
        {
            if(row < 0 || row >= matrix.size() || col < 0 || col >= matrix[row].size())
            {
                continue;
            }
#if DEBUG == 1
            cout << matrix[row][col];
#endif

            if(!isdigit(matrix[row][col]) && matrix[row][col] != '.')
            {
                #if DEBUG == 1
                cout << endl;
#endif

                return true;
            }

        }

        #if DEBUG == 1
            cout << endl;
#endif
        
    }
    
    return false;
}


int main()
{

    map<pair<int,int>,int> numbers;

    vector<string> matrix;
    string line, newNumber;
    char charac;
    int sum = 0, secondStarSum = 0;

    while (!cin.eof())
    {
        cin >> line;
        matrix.push_back(line);
    }

    for (auto it = matrix.begin(); it != matrix.end(); it++)
    {
        #if DEBUG == 1
        cout << *it << endl;
#endif
    }

    for (int row = 0; row < matrix.size(); row++)
    {
        for (int col = 0; col < matrix[row].size(); col++)
        {

            charac = matrix[row][col];

            if(isdigit(charac))
            {
                newNumber = charac;
                pair<int,int> start(row,col);
                for (col++; col < matrix[row].size() && isdigit(matrix[row][col]); col++)
                {
                    newNumber.push_back(matrix[row][col]);
                }
                pair<int,int> end(row,col-1);
                
                int num = stoi(newNumber);

                Number newNum;
                newNum.start = start;
                newNum.end = end;
                newNum.number = num;

                numbers.insert({{start.first,start.second},num});


               
               
                if(HasAdjacentSymbol(newNum, matrix))
                {
                    sum += newNum.number;
                }
                
            }

        }
    }

    cout << endl << endl;

    for (int row = 0; row < matrix.size(); row++)
    {
        for (int col = 0; col < matrix[row].size(); col++)
        {
            if(matrix[row][col] == '*')
            {
                secondStarSum += getGearRatio({row,col},matrix, numbers);
            }
        }
    }
    
    
    cout << sum << endl << secondStarSum;

}