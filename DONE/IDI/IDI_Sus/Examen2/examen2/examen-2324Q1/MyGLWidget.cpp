// MyGLWidget.cpp
#include "MyGLWidget.h"
#include <iostream>
#include <stdio.h>

#define printOpenGLError() printOglError(__FILE__, __LINE__)
#define CHECK() printOglError(__FILE__, __LINE__,__FUNCTION__)
#define DEBUG() std::cout << __FILE__ << " " << __LINE__ << " " << __FUNCTION__ << std::endl;

int MyGLWidget::printOglError(const char file[], int line, const char func[]) 
{
    GLenum glErr;
    int    retCode = 0;

    glErr = glGetError();
    const char * error = 0;
    switch (glErr)
    {
        case 0x0500:
            error = "GL_INVALID_ENUM";
            break;
        case 0x501:
            error = "GL_INVALID_VALUE";
            break;
        case 0x502: 
            error = "GL_INVALID_OPERATION";
            break;
        case 0x503:
            error = "GL_STACK_OVERFLOW";
            break;
        case 0x504:
            error = "GL_STACK_UNDERFLOW";
            break;
        case 0x505:
            error = "GL_OUT_OF_MEMORY";
            break;
        default:
            error = "unknown error!";
    }
    if (glErr != GL_NO_ERROR)
    {
        printf("glError in file %s @ line %d: %s function: %s\n",
                             file, line, error, func);
        retCode = 1;
    }
    return retCode;
}

MyGLWidget::MyGLWidget(QWidget *parent) : ExamGLWidget(parent) {

		
}

MyGLWidget::~MyGLWidget() {
}

void MyGLWidget::iniEscena ()
{
  ExamGLWidget::iniEscena();

}

void MyGLWidget::iniCamera ()
{
  angleY = float(15*(M_PI/180));
  angleX = float(15*(M_PI/180));
  ra = float(width())/height();
  fov = float(M_PI/3.0);
  zn = 15;
  zf = 65;

  glUniform3fv(posCLoc,1,&centreEsc[0]);

  projectTransform ();
  viewTransform ();
}

void MyGLWidget::paintGL ()
{
  glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

  
  // Pintem el terra = GROUND_BRICKS
  glm::vec3 colTerra = glm::vec3(0.7, 0, 0);
  glUniform3fv(colorLoc,1,&colTerra[0]);
  glBindVertexArray (VAO_models[GROUND_BRICKS]);
  modelTransformGround();
  glDrawArrays(GL_TRIANGLES, 0, models[GROUND_BRICKS].faces().size()*3);
   
  // Pintem el bloc de Lego actual (currentBrick) del color actual
  glUniform3fv(colorLoc,1,&currentColor[0]);
  glBindVertexArray (VAO_models[currentBrickModelIndex]);
  modelTransformCurrentBrick();
  glDrawArrays(GL_TRIANGLES, 0, models[currentBrickModelIndex].faces().size()*3); 
  glDrawArrays(GL_LINES, 0, models[currentBrickModelIndex].faces().size()*3); 
  glBindVertexArray(0);
}

void MyGLWidget::modelTransformCurrentBrick()
{
  ExamGLWidget::modelTransformCurrentBrick();
}

void MyGLWidget::viewTransform ()
{
  View = glm::translate(glm::mat4(1.f), glm::vec3(0, 0, -2*radiEsc));
  View = glm::rotate(View, angleX, glm::vec3(1, 0, 0));
  View = glm::rotate(View, -angleY, glm::vec3(0, 1, 0));
  View = glm::translate(View, -centreEsc);
  glUniformMatrix4fv (viewLoc, 1, GL_FALSE, &View[0][0]);
}

void MyGLWidget::projectTransform ()
{
  ExamGLWidget::projectTransform();
}

void MyGLWidget::keyPressEvent(QKeyEvent* event) 
{
  makeCurrent();
  switch (event->key()) {
  case Qt::Key_A: {
    break;
	}
  case Qt::Key_D: {
    break;
    }
  case Qt::Key_W: {
    break;
	}
  case Qt::Key_S: {
    break;  
	}
  case Qt::Key_Up: {
    break;
	}
  case Qt::Key_Down: {
    break;  
	}		
  case Qt::Key_Q: {
    break;
	}
  case Qt::Key_C: {
    break;
	}
  case Qt::Key_Space: {
    break;
    }
  case Qt::Key_R: {
    break;
	}
  default: ExamGLWidget::keyPressEvent(event); break;
  }
  
  update();
}


void MyGLWidget::mouseMoveEvent(QMouseEvent *e)
{
  makeCurrent();
  if (DoingInteractive == ROTATE)
  {
    // Fem la rotació (només en Y)
    angleY += (e->x() - xClick) * M_PI / ample;
    angleX += (yClick - e->y()) * M_PI / alt;
    viewTransform ();
  }

  xClick = e->x();
  yClick = e->y();

  update ();
}

void MyGLWidget::carregaShaders(){
  ExamGLWidget::carregaShaders();
  posCLoc = glGetUniformLocation (program->programId(), "posFocus");
}


