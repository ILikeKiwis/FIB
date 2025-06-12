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

void MyGLWidget::initializeGL(){
  ExamGLWidget::initializeGL();
  posPat = 0;
  pintarCub = true;
  a_cub1 = 0.0f;
  a_cub2 = float((2*M_PI)/3);
  a_cub3 = float((2*(2*M_PI))/3);
}

void MyGLWidget::paintGL ()   // Mètode que has de modificar
{
  //ExamGLWidget::paintGL();
  glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

  // Pintem el terra
  glBindVertexArray (VAO_Terra);
  modelTransformTerra ();
  glDrawArrays(GL_TRIANGLE_STRIP, 0, 4);

  if (pintarCub) {
    // Pintem el cub-1
    glBindVertexArray(VAO_Cub);
    modelTransformCub (2.0, a_cub1);
    glDrawArrays(GL_TRIANGLES, 0, 36);
    
    // Pintem el cub-2
    glBindVertexArray(VAO_Cub);
    modelTransformCub (2.5, a_cub2);
    glDrawArrays(GL_TRIANGLES, 0, 36);

    // Pintem el cub-3
    glBindVertexArray(VAO_Cub);
    modelTransformCub (3.0, a_cub3);
    glDrawArrays(GL_TRIANGLES, 0, 36);
  }
  else {
    //Pintem Patricio
    glBindVertexArray (VAO_Patr);
    modelTransformPatricio ();
    glDrawArrays(GL_TRIANGLES, 0, patr.faces().size()*3);
  }
}

void MyGLWidget::modelTransformCub (float escala, float angle) 
{
  //ExamGLWidget::modelTransformCub (2.0, 0.0);
  TG = glm::mat4(1.0f);
  
  
  TG = glm::rotate(TG, angle, glm::vec3(0.0f, 1.0f, 0.0f));
  TG = glm::translate(TG, glm::vec3(5.0f, 0.0f, 0.0f));
  TG = glm::scale(TG, glm::vec3(escala/0.5f));
  

  glUniformMatrix4fv (transLoc, 1, GL_FALSE, &TG[0][0]);
  // En aquest mètode has de substituir aquest codi per construir la 
  // transformació geomètrica (TG) del cub usant els paràmetres adientment
}

void MyGLWidget::modelTransformPatricio ()    // Mètode que has de modificar
{
  //ExamGLWidget::modelTransformPatricio ();
  float a = 0;
  switch (posPat)
  {
  case 0:{
    a = a_cub1;
    break;
  }
  case 1:{
    a = a_cub2;
    break;
  }
  case 2:{
    a = a_cub3;
    break;
  }
  default:
    break;
  }


  TG = glm::mat4(1.0f);
  TG = glm::rotate(TG, a, glm::vec3(0.0f, 1.0f, 0.0f));
  TG = glm::translate(TG, glm::vec3(5.0f, 0.0f, 0.0f));
  TG = glm::rotate(TG, float(-90*(M_PI/180)), glm::vec3(0.0f, 1.0f, 0.0f));
  TG = glm::scale(TG, glm::vec3 (escala));
  TG = glm::scale(TG, glm::vec3(2.0f));
  TG = glm::translate(TG, -centreBasePat);
  
  
  
  
  glUniformMatrix4fv (transLoc, 1, GL_FALSE, &TG[0][0]);
}

void MyGLWidget::viewTransform ()    // Mètode que has de modificar
{
  if (!camPlanta)
    ExamGLWidget::viewTransform();
  else
  {
    // Codi per a la viewMatrix de la Càmera-2
  }
}

void MyGLWidget::projectTransform ()
{
  if (!camPlanta)
    ExamGLWidget::projectTransform();
  else
  {
    // Codi per a la projectMatrix de la Càmera-2
  }
}

void MyGLWidget::keyPressEvent(QKeyEvent* event) {
  makeCurrent();
  switch (event->key()) {
  case Qt::Key_V: {
      pintarCub = !pintarCub;
    break;
	}
  case Qt::Key_1: {
      // Patricio cub-1
      posPat = 0;
    break;
	}
  case Qt::Key_2: {
      // Patricio cub-2
      posPat = 1;
    break;
	}
  case Qt::Key_3: {
      // Patricio cub-3
      posPat = 2;
    break;
	}
  case Qt::Key_F: {
      colFoc = glm::vec3(1, 1, 0);
      enviaColFocus();
    break;
	}
  case Qt::Key_C: {
      // ...
    break;
	}
  case Qt::Key_Right: {
      a_cub1 += float((2*M_PI)/3);
      a_cub2 += float((2*M_PI)/3);
      a_cub3 += float((2*M_PI)/3);
    break;
	}
  case Qt::Key_Left: {
      a_cub1 += float(-(2*M_PI)/3);
      a_cub2 += float(-(2*M_PI)/3);
      a_cub3 += float(-(2*M_PI)/3);
    break;
	}
  case Qt::Key_R: {
      // ...
    break;
	}
  default: ExamGLWidget::keyPressEvent(event); break;
  }
  update();
}

