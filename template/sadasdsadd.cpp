#include<iostream>
using namespace std;

class Dad{
    public:
    void CharectorsOfDad(){
        cout<<"EYES, NOSE, EARS"
    }
}

class Mom{
    public:
    void CharectorsOfMom(){
        cout<<"SMILE, MAD, BEAUTI"    
    }
}

class Sreenidhi:public Dad, public Mom{
    public:
    
}


void Main(){
    Sreenidhi obj;
    obj.CharectorsOfMom()
    obj.CharectorsOfDad()
}