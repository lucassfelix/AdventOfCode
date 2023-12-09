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


struct Node
{
    string name;

    Node *right;
    Node *left;
};


map<string,Node> nodes;

#if DEBUG == 1
#endif

bool reachedEnd(vector<ull> v)
{
    for (auto it = v.begin(); it != v.end(); it++)
    {
        if((*it) == 0)
        {
            return false;
        }
    }

    return true;
}

ull getNextPrime(ull current)
{
    for (ull i = current; i < ULONG_LONG_MAX; i++)
    {
        
    }
    return 0ull;
    
}

ull mmc(vector<ull> v)
{
    for(int i = 0; i < v.size(); i++)
    {
        cout << v[i] << endl;
    }
    return 0ull;
}

int main()
{
    string command, dummy, nodeName,right,left;

    vector<Node> ghosts;
    vector<ull> pathToZ;

    cin >> command;
    while(!cin.eof())
    {
        cin >> nodeName >> dummy >> left >> right;

        left = left.substr(1,3);
        right = right.substr(0,3);
        Node newNode;
        Node* ptrNode = &newNode;
        ptrNode->name = nodeName;
        
        if(nodes.count(nodeName) == 1)
        {
#if DEBUG == 1
            cout << nodeName << " already exists" << endl;
#endif
            ptrNode = &nodes[nodeName];
        }
        
        if(nodes.count(right)==0)
        {
            Node auxNewNode;
            auxNewNode.name = right; 
            nodes.insert({right,auxNewNode});
        }

        if(nodes.count(left)==0)
        {
            Node auxNewNode;
            auxNewNode.name = left; 
            nodes.insert({left,auxNewNode});
        }

        ptrNode->right = &nodes[right];
        ptrNode->left = &nodes[left];

        if(nodes.count(nodeName) == 0)
        {
            nodes.insert({nodeName,*ptrNode});
        }

        if (ptrNode->name[2] == 'A')
        {
            ghosts.push_back(*ptrNode);
            pathToZ.push_back(0);
        }
        

    }

    Node currentNode = nodes["AAA"];

    int steps = 0;
/*
    while (currentNode.name != "ZZZ")
    {

#if DEBUG == 1
        cout << currentNode.left<< endl;
        cout << "On: " << currentNode.name << " = " << (*currentNode.left).name << " , " << (*currentNode.right).name << " Going: " << command[steps%command.size()] << endl;

#endif
        if(command[steps%command.size()] == 'R')
        {
            currentNode = *currentNode.right;
        }
        else
        {
            currentNode = *currentNode.left;
        }
        steps++;
    }

    */

    cout << "Estrela 1: " << steps << endl;

    ull stepsTwo = 0;
#if DEBUG == 1

    for (auto it = ghosts.begin(); it != ghosts.end(); it++)
    {
        cout << (*it).name << " , ";
    }
    cout << endl;
#endif
    
    while (!reachedEnd(pathToZ))
    {
#if DEBUG == 1
        cout << "Step " << stepsTwo <<" Going: " << command[steps%command.size()] << endl;
#endif
        for (int i = 0; i < ghosts.size(); i++)
        {
            auto n = ghosts[i];
            if (n.name[2]== 'Z')
            {
                pathToZ[i] = stepsTwo;
            }
            
#if DEBUG == 1
            cout << "\t" << "On: " << n.name << " = " << (*n.left).name << " , " << (*n.right).name << endl;
#endif

            if(command[stepsTwo%command.size()] == 'R')
            {
                ghosts[i] = *n.right;
            }
            else
            {
                ghosts[i] = *n.left;
            }
        }

        stepsTwo++;
    }


    ull resposta = mmc(pathToZ);

    
   // cout << stepsTwo;
}