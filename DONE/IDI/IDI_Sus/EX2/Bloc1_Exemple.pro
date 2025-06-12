TEMPLATE    = app
QT         += opengl 

INCLUDEPATH +=  /usr/include/glm

FORMS += MyForm.ui

HEADERS += MyForm.h MyGLWidget.h MyQLineEdit.h MyQLabel.h MyQLCDNumber.h

SOURCES += main.cpp \
        MyForm.cpp MyGLWidget.cpp MyQLineEdit.cpp MyQLabel.cpp MyQLCDNumber.cpp
