#include "MyQLabel.h"

MyQLabel::MyQLabel(QWidget *parent): QLabel(parent){

}

void MyQLabel::tractaSlider(int n)
{
    QString s = text();
    s.truncate(n);
    setText(s);
}