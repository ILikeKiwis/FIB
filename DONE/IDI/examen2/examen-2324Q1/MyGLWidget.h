#include "ExamGLWidget.h"

class MyGLWidget:public ExamGLWidget
{
  Q_OBJECT

  public:
    MyGLWidget(QWidget *parent=0);
    ~MyGLWidget();

  protected:
    virtual void paintGL ();
    virtual void keyPressEvent(QKeyEvent* event);
    virtual void mouseMoveEvent (QMouseEvent *event);

    virtual void iniEscena ();
    virtual void iniCamera ();
    virtual void projectTransform ();
    virtual void viewTransform ();
    
    virtual void modelTransformCurrentBrick();

    virtual void resizeGL(int w, int h);

    glm::vec3 red = glm::vec3(0.7,0,0);
    glm::vec3 black = glm::vec3(0);

    float rav;
    float fovog;
    float posX = 0, posY = 0, posZ = 0;
    float rot = glm::radians(90.);
    float numrot = 0;

    glm::mat4 TGCurrent;

    bool orto = false;

  public slots:
    
  signals:


  private:
    int printOglError(const char file[], int line, const char func[]);
    
};
