#include <iostream>
#include <fstream>
#include <sstream>
#include <map>
#include <set>
#include <vector>
#include <math.h>
#include <algorithm>
#include <bits/stdc++.h>

using namespace std;

#define DEBUG 0
#define ull unsigned long long
#define ll long long

map<char, int> cardStrenght = {{'A',0},{'K',1},{'Q',2},{'J',3},{'T',4},{'9',5},{'8',6},{'7',7},{'6',8},{'5',9},{'4',10},{'3',11},{'2',12}};
struct Hand
{
    string cards = "";
    ull value = 0;
};
map<string,bool> FiveOfKind,FourOfKind, ThreeOfKind, FullHouse, TwoPairs, OnePair;

bool compareCards(const string &a, const string &b)
{
    for (int i = 0; i < a.size(); i++)
    {
        if (cardStrenght[a[i]] < cardStrenght[b[i]])
        {
            return true;
        }
        else if(cardStrenght[a[i]] > cardStrenght[b[i]])
        {
            return false;
        }
    }
    return true;
}




bool isFiveOfAKind(const Hand &h)
{
#if DEBUG == 1
    cout << "Is " << h.cards << " five of a kind? ";
#endif
    if(FiveOfKind.count(h.cards) == 1)
    {
        auto k = FiveOfKind[h.cards];
        #if DEBUG == 1
            auto s = k?"Yes!":"...";
            cout << s << " (Already calculated!)" << endl;
        #endif
        return k;
    }

    auto k = h.cards[0];

    if(count(h.cards.begin(),h.cards.end(),k) == 5)
    {
        #if DEBUG == 1
            cout << "Yes!" << endl;
        #endif
        FiveOfKind.insert({h.cards,true});
        return true;
    }
#if DEBUG == 1
            cout << "..." << endl;
        #endif
    FiveOfKind.insert({h.cards,false});
    return false;
}

bool isFourOfAKind(const Hand &h)
{
    #if DEBUG == 1
    cout << "Is " << h.cards << " four of a kind? ";
#endif
    if(FourOfKind.count(h.cards) == 1)
    {
        auto k = FourOfKind[h.cards];
        #if DEBUG == 1
            auto s = k?"Yes!":"...";
            cout << s << " (Already calculated!)" << endl;
        #endif
        return k;
    }

    auto k = h.cards[0];

    if(count(h.cards.begin(),h.cards.end(),k) == 4)
    {
         #if DEBUG == 1
            cout << "Yes!" << endl;
        #endif
        FourOfKind.insert({h.cards,true});
        return true;
    }

    k = h.cards[1];

    if(count(h.cards.begin(),h.cards.end(),k) == 4)
    {
         #if DEBUG == 1
            cout << "Yes!" << endl;
        #endif
        FourOfKind.insert({h.cards,true});
        return true;
    }
 #if DEBUG == 1
            cout << "..." << endl;
        #endif
    FourOfKind.insert({h.cards,false});
    return false;
}

bool isFullHouse(const Hand &h)
{
#if DEBUG == 1
    cout << "Is " << h.cards << " a full house? ";
#endif

    if(FullHouse.count(h.cards) == 1)
    {
        auto k = FullHouse[h.cards];
        #if DEBUG == 1
            auto s = k?"Yes!":"...";
            cout << s << " (Already calculated!)" << endl;
        #endif
        return k;
    }

    char str[5]; 
    h.cards.copy(str,5,0);
    string cards(str);
    sort(begin(cards),end(cards));
    auto last = unique(begin(cards),end(cards));
    cards.erase(last,end(cards));

    #if DEBUG == 1
    cout << endl << "Size: " << cards.size() << endl;
    for_each(cards.begin(),cards.end(),[](const char &c)
    {
        cout << c << endl;
    });
#endif

    if (cards.size() != 2)
    { 
#if DEBUG == 1
        cout << "..." << endl;
#endif
        FullHouse.insert({h.cards,false});
        return false;
    }
#if DEBUG == 1
    cout << "Yes!" << endl;
#endif
    FullHouse.insert({h.cards,true});
    return true;

}

bool isThreeOfAKind(const Hand &h)
{
#if DEBUG == 1
    cout << "Is " << h.cards << " three of a kind? ";
#endif

    if(ThreeOfKind.count(h.cards) == 1)
    {
        auto k = ThreeOfKind[h.cards];
        #if DEBUG == 1
            auto s = k?"Yes!":"...";
            cout << s << " (Already calculated!)" << endl;
        #endif
        return k;
    }
    auto k = h.cards[0];

    if(count(h.cards.begin(),h.cards.end(),k) == 3)
    {
         #if DEBUG == 1
            cout << "Yes!" << endl;
        #endif
        ThreeOfKind.insert({h.cards,true});
        return true;
    }

    k = h.cards[1];

    if(count(h.cards.begin(),h.cards.end(),k) == 3)
    {
         #if DEBUG == 1
            cout << "Yes!" << endl;
        #endif
        ThreeOfKind.insert({h.cards,true});


        return true;
    }

    k = h.cards[2];

    if(count(h.cards.begin(),h.cards.end(),k) == 3)
    {
         #if DEBUG == 1
            cout << "Yes!" << endl;
        #endif
        ThreeOfKind.insert({h.cards,true});


        return true;
    }

 #if DEBUG == 1
            cout << "..." << endl;
        #endif
    ThreeOfKind.insert({h.cards,false});

    return false;
}

bool isTwoPair(const Hand &h)
{
    #if DEBUG == 1
    cout << "Is " << h.cards << " two pairs? ";
#endif
    if(TwoPairs.count(h.cards) == 1)
    {
        auto k = TwoPairs[h.cards];
        #if DEBUG == 1
            auto s = k?"Yes!":"...";
            cout << s << " (Already calculated!)" << endl;
        #endif
        return k;
    }
    char str[5];  
    h.cards.copy(str,5,0);
    string cards(str);
    sort(begin(cards),end(cards));
    auto last = unique(begin(cards),end(cards));
    cards.erase(last,end(cards));

#if DEBUG == 1
    cout << endl << "Size: " << cards.size() << endl;
    for_each(cards.begin(),cards.end(),[](const char &c)
    {
        cout << c << endl;
    });
#endif

    if (cards.size() == 3)
    {
         #if DEBUG == 1
            cout << "Yes!" << endl;
        #endif
        TwoPairs.insert({h.cards,true});
        return true;
    }
     #if DEBUG == 1
            cout << "..." << endl;
        #endif
    TwoPairs.insert({h.cards,false});
    return false;
}

bool isOnePair(const Hand &h)
{
#if DEBUG == 1
    cout << "Is " << h.cards << " one pair? ";
#endif

    if(OnePair.count(h.cards) == 1)
    {
        auto k = OnePair[h.cards];
        #if DEBUG == 1
            auto s = k?"Yes!":"...";
            cout << s << " (Already calculated!)" << endl;
        #endif
        return k;
    }
  
    char str[5]; 
    h.cards.copy(str,5,0);
    string cards(str);
    sort(begin(cards),end(cards));
    auto last = unique(begin(cards),end(cards));
    cards.erase(last,end(cards));

    if (cards.size() == 4)
    {
#if DEBUG == 1
    cout << "Yes!" << endl;
#endif
        OnePair.insert({h.cards,true});
        return true;
    }


#if DEBUG == 1
            cout << "..." << endl;
#endif
    OnePair.insert({h.cards,false});    
    return false;
}

bool compareHands(const Hand &a, const Hand &b)
{
    bool typeA,typeB;
    typeA = isFiveOfAKind(a);
    typeB = isFiveOfAKind(b);
    if(typeA && !typeB)
    {
        return true;
    }
    if(!typeA && typeB)
    {
        return false;
    }
    if(typeA && typeB)
    {
        return compareCards(a.cards,b.cards);
    }
    typeA = isFourOfAKind(a);
    typeB = isFourOfAKind(b);
    if(typeA && !typeB)
    {
        return true;
    }
    if(!typeA && typeB)
    {
        return false;
    }
    if(typeA && typeB)
    {
        return compareCards(a.cards,b.cards);
    }
    typeA = isFullHouse(a);
    typeB = isFullHouse(b);
    if(typeA && !typeB)
    {
        return true;
    }
    if(!typeA && typeB)
    {
        return false;
    }
    if(typeA && typeB)
    {
        return compareCards(a.cards,b.cards);
    }
    typeA = isThreeOfAKind(a);
    typeB = isThreeOfAKind(b);
    if(typeA && !typeB)
    {
        return true;
    }
    if(!typeA && typeB)
    {
        return false;
    }
    if(typeA && typeB)
    {
        return compareCards(a.cards,b.cards);
    }
    typeA = isTwoPair(a);
    typeB = isTwoPair(b);
    if(typeA && !typeB)
    {
        return true;
    }
    if(!typeA && typeB)
    {
        return false;
    }
    if(typeA && typeB)
    {
        return compareCards(a.cards,b.cards);
    }
    typeA = isOnePair(a);
    typeB = isOnePair(b);
    if(typeA && !typeB)
    {
        return true;
    }
    if(!typeA && typeB)
    {
        return false;
    }
    if(typeA && typeB)
    {
        return compareCards(a.cards,b.cards);
    }
    return compareCards(a.cards,b.cards);
}

int main()
{

#if DEBUG == 1
#endif

    vector<Hand> hands;

    string cards;
    ull bid;

    while(!cin.eof())
    {
        cin >> cards >> bid;
        Hand h;
        h.cards = cards;
        h.value = bid;
        hands.push_back(h);
    }

#if DEBUG == 1
    for_each(hands.begin(),hands.end(),[](const Hand &h)
    {
        cout << h.cards << " " << h.value << endl;
    });
#endif

#if DEBUG == 1

    cout << endl << "AFTER SORT" << endl;
#endif

    sort(hands.begin(),hands.end(),compareHands);

    ull winnigs = 0;




#if DEBUG == 1
    int index = hands.size();
    for_each(hands.begin(),hands.end(),[&index](const Hand &h)
    {
        cout << h.cards << " =  " << h.value << " * " << index-- <<endl;
    });
#endif

    for (int i = 0; i < hands.size(); i++)
    {
        winnigs += (hands.size() - i) * hands[i].value;
#if DEBUG == 1     
        cout << (hands.size() - i) <<" * " << hands[i].value << endl;
#endif

    }

    cout << winnigs;
    

}