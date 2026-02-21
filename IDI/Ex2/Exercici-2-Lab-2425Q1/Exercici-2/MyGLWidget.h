#include "LL2GLWidget.h"

#include <vector>

#include <QTimer>

class MyGLWidget : public LL2GLWidget {
  Q_OBJECT

  public:
    MyGLWidget(QWidget *parent);
    ~MyGLWidget();

  public slots:
    void anim();

  protected:
  
    virtual void initializeGL ();
    virtual void paintGL();
    virtual void keyPressEvent (QKeyEvent *event);

    virtual void modelTransformTerra();   
    void modelTransformLEGO(glm::vec3 pos);
    void modelTransformParet(glm::vec3 pos, glm::vec3 escala);
    virtual void modelTransformPatricio (glm::vec3 pos);
    virtual void modelTransformPilota ();
    
    virtual void viewTransform ();
    virtual void projectTransform ();

    virtual void iniEscena ();
    
    virtual void mouseMoveEvent (QMouseEvent *event);
    float angY, angX;
    float zPorter, zPat;
    bool gol;
    bool pers;
    bool indiv;
    


    void rebotaParet();
    void rebotaParetPat();
    bool rebotaPat();
    void canviaDireccioPat();
    glm::vec3 posIniPilota;
    glm::vec3 posPat;

  private:
  
    int printOglError(const char file[], int line, const char func[]);
   
};
