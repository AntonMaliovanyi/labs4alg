#include <iostream>

using namespace std;

struct TQueueItem
{
    int value;
    TQueueItem *next;
};

struct TQueue
{
    TQueueItem *head;
    TQueueItem *tail;
};


TQueue initQueue()
{
    TQueue q;
    q.head = NULL;
    q.tail = NULL;
    return q;
}

int IsEmpty(const TQueue&q)
{
    return q.head == NULL;
}



void enQueue(TQueue &q, int value)
{
    if(IsEmpty(q))
    {
        q.head = new TQueueItem();
        q.head->value = value;
        q.head->next = NULL;
        q.tail = q.head;
    }
    else
    {
        q.tail->next = new TQueueItem;
        q.tail->next->value = value;
        q.tail->next->next = NULL;
        q.tail = q.tail->next;
    }
}


int deQueue(TQueue &q)
{
    if(IsEmpty(q))
    {
        return 0;
    }
    else
    {
        int result = q.head->value;
        TQueueItem *item = q.head;
        q.head = q.head->next;

        delete item;

        if(q.head == NULL) q.tail = q.head;

        return result;
    }
}

void destroyQueue(TQueueItem *&q)
{
    if(q != NULL)
    {
        destroyQueue(q->next);
        delete q;
        q = NULL;
    }
}

bool Check(int elem, TQueue &q1)
{
    TQueue temp;
    temp = initQueue();
    while(!IsEmpty(q1))
        enQueue(temp, deQueue(q1));

    int elem1;
    bool found = false;
    while(!IsEmpty(temp))
    {
        elem1 = deQueue(temp);
        enQueue(q1, elem1);
        if(elem == elem1)
        {
            found = true;
        }
    }
    
    return found;
    
}







int main()
{
    TQueue q;
    q = initQueue();

    int n, el;

    cout<<"Input n"<<endl;
    cin>>n;

    cout<<"Input elements(q)"<<endl;
    for(int i = 0; i < n; i++)
    {
        cin>>el;
        enQueue(q, el);
    }

    TQueue q1;
    q1 = initQueue();

    cout<<"Input elements(q1)"<<endl;
    for(int i = 0; i < n; i++)
    {
        cin>>el;
        enQueue(q1, el);
    }

    TQueue q2;
    q2 = initQueue();

    int elem;
    
    while(!IsEmpty(q))
    {
        elem = deQueue(q);
        if(Check(elem, q1))
        {
            enQueue(q2, elem);
        }
    }


    cout<<"Result: ";
    while(!IsEmpty(q2))
    {
        cout<<deQueue(q2)<<" ";
    }


    return 0;
}
