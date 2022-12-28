#include <iostream>

using namespace std;
struct stek
{
    string value;
    stek *next;
};

bool isEmpty(stek *st) { return st == NULL; }

void push(stek* &NEXT, string VALUE)
{
    stek *MyStack = new stek;
    MyStack->value = VALUE;
    MyStack->next = NEXT;
    NEXT = MyStack;
}

string pop(stek* &NEXT)
{
    if(isEmpty(NEXT))
    {
    	return "";
	}
    string temp = NEXT->value;
    stek *MyStack = NEXT;

    NEXT = NEXT->next;
    delete MyStack;
    return temp;
}

void FndWord(stek* &NEXT)
{
    string longest_word = pop(NEXT);
    string item;

    while(!isEmpty(NEXT))
    {
    	item = pop(NEXT);
        if (item.size() > longest_word.size())
        {
           longest_word =item;
        }

    }

    cout<<"Result: "<<longest_word;

}



int main()
{
    stek *ob = NULL;
    int n;
    string word;


    cout<<"Input number of words"<<endl;
    cin>>n;

    cout<<"Input words"<<endl;

    for(int i = 0; i < n; i++)
    {
        cin>>word;
        push(ob,word);
    }

    FndWord(ob);


    return 0;
}
