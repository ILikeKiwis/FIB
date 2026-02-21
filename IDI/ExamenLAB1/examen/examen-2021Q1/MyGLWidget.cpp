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

MyGLWidget::~MyGLWidget() {
}



void MyGLWidget::paintGL ()   // Mètode que has de modificar
{
  glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

  // Pintem el terra
  glBindVertexArray (VAO_Terra);
  modelTransformTerra ();
  glDrawArrays(GL_TRIANGLE_STRIP, 0, 4);

  //Pintem Cubs 
  
  if (!pintaPat) {

    //Cub-1
    glBindVertexArray(VAO_Cub);
    modelTransformCub (2, posCub1);
    glDrawArrays(GL_TRIANGLES, 0, 36);

    //Cub-2 
    glBindVertexArray(VAO_Cub);
    modelTransformCub (2.5, posCub2);
    glDrawArrays(GL_TRIANGLES, 0, 36);

    //Cub-3 
    glBindVertexArray(VAO_Cub);
    modelTransformCub (3, posCub3);
    glDrawArrays(GL_TRIANGLES, 0, 36);
  }
  
  else {
 // Pintem el Patricio
  
    glBindVertexArray (VAO_Patr);
    modelTransformPatricio ();
    glDrawArrays(GL_TRIANGLES, 0, patr.faces().size()*3);
  }

  glBindVertexArray(0);
  
}

void MyGLWidget::modelTransformCub (float escala, float angle) 
{

  escala = float(escala/0.5);

  TG = glm::mat4(1.f);
  TG = glm::rotate(TG, angle, glm::vec3(0, 1, 0));
  TG = glm::translate(TG, glm::vec3(5,0,0));
  TG = glm::scale(TG, glm::vec3(escala));
  
  //Ja apareix al centre.
  glUniformMatrix4fv (transLoc, 1, GL_FALSE, &TG[0][0]);
  // En aquest mètode has de substituir aquest codi per construir la 
  // transformació geomètrica (TG) del cub usant els paràmetres adientment
}

void MyGLWidget::modelTransformPatricio ()    // Mètode que has de modificar
{
  TG = glm::mat4(1.f);
  TG = glm::rotate(TG, angPat, glm::vec3(0,1,0));
  TG = glm::translate(TG, glm::vec3(5,0,0));
  TG = glm::scale(TG, glm::vec3 (escala*2, escala*2, escala*2));
  TG = glm::rotate(TG, float(-M_PI/2.f), glm::vec3(0,1,0));
  TG = glm::translate(TG, -centreBasePat);
  
  glUniformMatrix4fv (transLoc, 1, GL_FALSE, &TG[0][0]);
}

void MyGLWidget::viewTransform ()    // Mètode que has de modificar
{
  if (!camPlanta)
    ExamGLWidget::viewTransform();
  else
  {
    View = glm::lookAt(glm::vec3(0,1.5+2.*radiEsc, 0), glm::vec3(0,1.5,0), glm::vec3(1,0,0));
    //View = glm::translate(glm::mat4(1.f), glm::vec3(0,0, -(1.5+2.*radiEsc)));
    //View = glm::rotate(View, float(glm::radians(90.)), glm::vec3(1,0,0));
    //View = glm::rotate(View, float(glm::radians(90.)), glm::vec3(0,1,0));
    //View = glm::translate(View, -centreEsc);
    glUniformMatrix4fv (viewLoc, 1, GL_FALSE, &View[0][0]);
  }
}

void MyGLWidget::projectTransform ()
{
  if (!camPlanta)
    ExamGLWidget::projectTransform();
  else
  {
    glm::mat4 Proj;
    Proj = glm::ortho(-radiEsc, radiEsc, -radiEsc, radiEsc, radiEsc, 3*radiEsc);
    glUniformMatrix4fv (projLoc, 1, GL_FALSE, &Proj[0][0]);
  }
}

void MyGLWidget::keyPressEvent(QKeyEvent* event) {
  makeCurrent();
  switch (event->key()) {
  case Qt::Key_V: {
      pintaPat = !pintaPat;
    break;
	}
  case Qt::Key_1: {
      // Patricio Cub-1
      angPat = posCub1;
      modelTransformPatricio();
    break;
	}
  case Qt::Key_2: {
      // Patricio Cub-2
      angPat = posCub2;
      modelTransformPatricio();
    break;
	}
  case Qt::Key_3: {
      // Patricio Cub-3
      angPat = posCub3;
      modelTransformPatricio();
    break;
	}
  case Qt::Key_F: {
      if (groc) colFoc = glm::vec3(1,1,1);
      else colFoc = glm::vec3(1,1,0);
      groc = !groc;
      enviaColFocus();
    break;
	}
  case Qt::Key_C: {
      camPlanta = !camPlanta;
      viewTransform();
      projectTransform();
    break;
	}
  case Qt::Key_Right: {
      angPat += rot;
      posCub1 += rot;
      posCub2 += rot;
      posCub3 += rot;
    break;
	}
  case Qt::Key_Left: {
      angPat -= rot;
      posCub1 -= rot;
      posCub2 -= rot;
      posCub3 -= rot;
    break;
	}
  case Qt::Key_R: {
      angleY = 0.65;
      angleX = -1.2;
      posCub1 = 0;
      posCub2 = rot;
      posCub3 = 2.*rot;
      angPat = posCub1;
      camPlanta = false;
      pintaPat = false; 
      groc = false;
      enviaColFocus();
      viewTransform();
      projectTransform();
    break;
	}
  default: ExamGLWidget::keyPressEvent(event); break;
  }
  update();
}

