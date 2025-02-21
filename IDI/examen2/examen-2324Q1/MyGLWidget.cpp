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
  glm::vec3 pMax = glm::vec3(10, 10, 10);
  glm::vec3 pMin = glm::vec3(-10,-1,-10);

  centreEsc = (pMax+pMin)/glm::vec3(2);
  radiEsc = sqrt(10*10 + 10*10 + 4.5*4.5);
}

void MyGLWidget::iniCamera ()
{
  // Inicialitzem els paràmetres de càmera amb valors arbitraris
  angleY = glm::radians(15.);
  angleX = glm::radians(15.);
  ra = float(width())/height();
  fovog = 2.f*glm::asin(1.f/2.f);
  fov = fovog;
  zn = radiEsc;
  zf = 3*radiEsc;

  projectTransform ();
  viewTransform ();
}

void MyGLWidget::paintGL ()
{
  glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

  
  // Pintem el terra = GROUND_BRICKS

  glUniform3fv(colorLoc,1,&red[0]);
  glBindVertexArray (VAO_models[GROUND_BRICKS]);
  modelTransformGround();
  glDrawArrays(GL_TRIANGLES, 0, models[GROUND_BRICKS].faces().size()*3);
   
  // Pintem el bloc de Lego actual (currentBrick) del color actual
  glUniform3fv(colorLoc,1,&currentColor[0]);
  glBindVertexArray (VAO_models[currentBrickModelIndex]);
  modelTransformCurrentBrick();
  glDrawArrays(GL_TRIANGLES, 0, models[currentBrickModelIndex].faces().size()*3); 
  glUniform3fv(colorLoc,1,&black[0]);
  glDrawArrays(GL_LINES, 0, models[currentBrickModelIndex].faces().size()*3); 

  for(int i = 0; i < NUM_BRICKS; i++) {
    if (pintarBricks[i] == true) {
      glUniform3fv(colorLoc,1,&brickColors[i][0]);
      glBindVertexArray (VAO_models[brickModelIndex[i]]);
      modelTransformBrick(i);
      glDrawArrays(GL_TRIANGLES, 0, models[brickModelIndex[i]].faces().size()*3); 
    }
  }
  
  glBindVertexArray(0);
}

void MyGLWidget::modelTransformCurrentBrick()
{
  glm::mat4 TG(1.f);
  TG = glm::translate(TG, glm::vec3(posX, posY, posZ));
  if (currentBrickModelIndex == 1) {
    if (int(numrot) %2 == 0) TG = glm::translate(TG, glm::vec3(0.5,0,0)); 
    else  TG = glm::translate(TG, glm::vec3(0,0,0.5));
  }
  TG = glm::scale(TG, glm::vec3 (escalaModels[currentBrickModelIndex], escalaModels[currentBrickModelIndex], escalaModels[currentBrickModelIndex]));
  TG = glm::rotate(TG, rot*numrot, glm::vec3(0,1,0));
  TG = glm::rotate(TG, float(glm::radians(90.)), glm::vec3(1,0,0));
  TG = glm::translate(TG, -centreCapsaModels[currentBrickModelIndex]);  
  glUniformMatrix4fv (transLoc, 1, GL_FALSE, &TG[0][0]);
  TGCurrent = TG;
}

void MyGLWidget::viewTransform ()
{
  View = glm::translate(glm::mat4(1.f), glm::vec3(0, 0, -2*radiEsc));
  View = glm::rotate(View, angleX, glm::vec3(1,0,0));
  View = glm::rotate(View, -angleY, glm::vec3(0, 1, 0));
  View = glm::translate(View, -centreEsc);

  glUniformMatrix4fv (viewLoc, 1, GL_FALSE, &View[0][0]);
}


void MyGLWidget::projectTransform ()
{
  glm::mat4 Proj;  // Matriu de projecció

  Proj = glm::perspective(fov, ra, zn, zf);

  glUniformMatrix4fv (projLoc, 1, GL_FALSE, &Proj[0][0]);
}

void MyGLWidget::keyPressEvent(QKeyEvent* event) 
{
  makeCurrent();
  switch (event->key()) {
  case Qt::Key_A: {
    posX --;
    break;
	}
  case Qt::Key_D: {
    posX ++;
    break;
    }
  case Qt::Key_W: {
    posZ++;
    break;
	}
  case Qt::Key_S: {
    posZ--;
    break;  
	}
  case Qt::Key_Up: {
    posY++;
    break;
	}
  case Qt::Key_Down: {
    posY--;
    break;  
	}		
  case Qt::Key_Q: {
    numrot++;
    break;
	}
  case Qt::Key_C: {
    if (orto) {
      orto = !orto;
      projectTransform();
    }
    else {
      orto = !orto;
      glm::mat4 Proj;  // Matriu de projecció

      Proj = glm::ortho(-radiEsc, radiEsc, -radiEsc, radiEsc, radiEsc, 3*radiEsc);
      glUniformMatrix4fv (projLoc, 1, GL_FALSE, &Proj[0][0]);
    }
    break;
	}
  case Qt::Key_Space: {
    pintarBricks[currentBrickObjectIndex] = true;
    brickModelIndex[currentBrickObjectIndex] = currentBrickModelIndex;
    brickTGs[currentBrickObjectIndex] = TGCurrent;
    brickColors[currentBrickObjectIndex] = currentColor;
    currentBrickObjectIndex++;
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
    angleX -= (e->y() - yClick) * M_PI / alt;
    viewTransform ();
  }

  xClick = e->x();
  yClick = e->y();

  update ();
}

void MyGLWidget::resizeGL(int w, int h)
{
#ifdef __APPLE__
  // Aquest codi és necessari únicament per a MACs amb pantalla retina.
  GLint vp[4];
  glGetIntegerv (GL_VIEWPORT, vp);
  ample = vp[2];
  alt = vp[3];
#else
  ample = w;
  alt = h;
#endif

  ra = float(ample)/float(alt);
  if (ra < 1) fov = 2* atan(tan(fovog/2.f)/ra);
  projectTransform();
}

