#include "MyQLCDNumber.h"

MyQLCDNumber::MyQLCDNumber(QWidget *parent): QLCDNumber (parent){

}

void MyQLCDNumber::MyDisplay(int n) {
    if (n == 0) {
        setStyleSheet("color: green");
    }
    else if (n%2 == 0){
        setStyleSheet("color: red");
    }
    else {
        setStyleSheet("color: blue");
    }
    display(n);
}

void MyQLCDNumber::MyZero(){
    MyDisplay(0);
}