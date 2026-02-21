#include "ExamGLWidget.h"

class MyGLWidget:public ExamGLWidget
{
  Q_OBJECT

  public:
    MyGLWidget(QWidget *parent=0) : ExamGLWidget(parent) {}
    ~MyGLWidget();

  protected:
    virtual void paintGL ();
    virtual void keyPressEvent(QKeyEvent* event);
    virtual void modelTransformCub (float escala, float angle);
    virtual void modelTransformPatricio ();
    virtual void projectTransform ();
    virtual void viewTransform ();

  private:
    int printOglError(const char file[], int line, const char func[]);
    
    
    float angPat = 0;
    float rot = 2.*M_PI/3;
    bool pintaPat = false;
    bool groc = false;
    //Posicions dels cubs (es a dir angles)
    float posCub1 = 0;
    float posCub2 = rot;
    float posCub3 = 2.*rot;
};
