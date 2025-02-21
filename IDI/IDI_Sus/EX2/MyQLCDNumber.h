#include <QLCDNumber>

class MyQLCDNumber: public QLCDNumber{
    Q_OBJECT
    public:
        MyQLCDNumber (QWidget *parent);
    public slots: 
        void MyDisplay (int);
        void MyZero();
};