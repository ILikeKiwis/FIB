#include "MyGLWidget.h"
#include <iostream>
#include <stdio.h>

#define printOpenGLError() printOglError(__FILE__, __LINE__)
#define CHECK() printOglError(__FILE__, __LINE__,__FUNCTION__)
#define DEBUG() std::cout << __FILE__ << " " << __LINE__ << " " << __FUNCTION__ << std::endl;

MyGLWidget::MyGLWidget(QWidget *parent=0) : LL2GLWidget(parent) 
{
}

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

MyGLWidget::~MyGLWidget()
{
}

void MyGLWidget::initializeGL ( ){
  LL2GLWidget::initializeGL();
  connect(&timer, SIGNAL(timeout()), this, SLOT(anim()));
}

void MyGLWidget::anim() {
  makeCurrent();
  if (indiv){
    if (rebotaPorter()){
      canviaDireccio();
    }
    else {
      rebotaParet();
    }
  }
  else {
    if (rebotaPorter()){
      canviaDireccio();
    }
    else if (rebotaPat()) {
      canviaDireccioPat();
    }
    else {
      rebotaParetPat();
    }
  }
  if (posPilota.x > 12 or posPilota.x < -12 or posPilota.z > 8 or posPilota.z < -8) {
    gol = true;
  }
  posPilota += dirPilota;
  modelTransformPilota();
  update();
}

bool MyGLWidget::rebotaPat(){
  bool rebota = false;

  if ((posPilota[0] > -10.5) && (posPilota[0] < -9.5) && 
      (posPilota[2] >= posPat[2]-1.5) && (posPat[2] <= posPorter[2]+1.5))
    rebota = true;

  return rebota;
}

void MyGLWidget::canviaDireccioPat(){
  dirPilota = posPilota-posPat;
}

void MyGLWidget::paintGL(){
  
  glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

  // LEGO
  glBindVertexArray (VAO_models[LEGO]);
  modelTransformLEGO (posPorter);
  glDrawArrays(GL_TRIANGLES, 0, models[LEGO].faces().size()*3);

  // Pilota
  if (!gol){
    glBindVertexArray (VAO_models[PILOTA]);
    modelTransformPilota ();
    glDrawArrays(GL_TRIANGLES, 0, models[PILOTA].faces().size()*3);
  }
  
  // Paret1
  glBindVertexArray (VAO_Cub);
  modelTransformParet(glm::vec3(0, 0, -7.9), glm::vec3(24,2,0.2));
  glDrawArrays(GL_TRIANGLES, 0, 36);

  // Paret2
  glBindVertexArray (VAO_Cub);
  modelTransformParet(glm::vec3(0, 0, 7.9), glm::vec3(24,2,0.2));
  glDrawArrays(GL_TRIANGLES, 0, 36);

  // Paret3
  if (indiv) {
    glBindVertexArray (VAO_Cub);
    modelTransformParet(glm::vec3(-11.9, 0, 0), glm::vec3(0.2,2,16));
    glDrawArrays(GL_TRIANGLES, 0, 36);
  }
  else {
    glBindVertexArray (VAO_models[PATRICIO]);
    modelTransformPatricio (posPat);
    glDrawArrays(GL_TRIANGLES, 0, models[PATRICIO].faces().size()*3);
  }
// Terra
  glBindVertexArray (VAO_Terra);
  modelTransformTerra ();
  glDrawArrays(GL_TRIANGLE_STRIP, 0, 4);

  glBindVertexArray (0);
}

//MODEL_TRANSFORMS

void MyGLWidget::modelTransformTerra(){
  glm::mat4 TG(1.0f);
  TG = glm::scale(TG, glm::vec3(24/8, 0, 16/8));
  glUniformMatrix4fv (transLoc, 1, GL_FALSE, &TG[0][0]);
}

void MyGLWidget::modelTransformLEGO(glm::vec3 pos){
  glm::mat4 TG(1.0f);
  TG = glm::translate(TG, pos);
  TG = glm::scale(TG, glm::vec3(escalaModels[LEGO]));
  TG = glm::rotate(TG, float(-90*(M_PI/180)), glm::vec3(0, 1, 0));
  TG = glm::translate(TG, -centreBaseModels[LEGO]);
  glUniformMatrix4fv (transLoc, 1, GL_FALSE, &TG[0][0]);
}

void MyGLWidget::modelTransformParet(glm::vec3 pos, glm::vec3 escala){
  glm::mat4 TG(1.0f);
  TG = glm::translate(TG, pos);
  TG = glm::scale(TG, glm::vec3(escala));
  glUniformMatrix4fv (transLoc, 1, GL_FALSE, &TG[0][0]);
}

void MyGLWidget::modelTransformPilota(){
  glm::mat4 TG(1.0f);
  
  TG = glm::translate(TG, posPilota);
  TG = glm::scale(TG, glm::vec3(escalaModels[PILOTA]));
  TG = glm::translate(TG, -centreBaseModels[PILOTA]);
  glUniformMatrix4fv (transLoc, 1, GL_FALSE, &TG[0][0]);
}

void MyGLWidget::modelTransformPatricio (glm::vec3 pos){
  glm::mat4 TG(1.0f);
  TG = glm::translate(TG, pos);
  TG = glm::scale(TG, glm::vec3(escalaModels[PATRICIO]));
  TG = glm::rotate(TG, float(90*(M_PI/180)), glm::vec3(0, 1, 0));
  TG = glm::translate(TG, -centreBaseModels[PATRICIO]);
  glUniformMatrix4fv(transLoc, 1, GL_FALSE, &TG[0][0]);
}



void MyGLWidget::keyPressEvent(QKeyEvent* event) 
{
  makeCurrent();
  switch (event->key()) {
    case Qt::Key_Up: { 
        timer.start(100);
      break;
    }
    case Qt::Key_I: {
      timer.stop();
      gol = false;
      posPilota = posIniPilota;
      dirInicialPilota();
      break;
        }           
    case Qt::Key_Left: { 
      if (zPorter < 6){
        zPorter += 0.5;
        posPorter.z += 0.5;
      }
      break;
    }  
    case Qt::Key_Right: { 
      if (zPorter > -6){
        zPorter -= 0.5;
        posPorter.z += -0.5;
      }
      break;
    }
    case Qt::Key_C: { 
      pers = !pers;
      viewTransform();
      projectTransform();
      break;
    }           
    case Qt::Key_R: { 
      MyGLWidget::iniEscena();
      viewTransform();
      projectTransform();
      break;
    }  
    case Qt::Key_2: {
      indiv = false;
      viewTransform();
      break;
    }
    case Qt::Key_1: {
      indiv = true;
      viewTransform();
      break;
    }
    case Qt::Key_D: { 
      if (zPat < 6){
        zPat += 0.5;
        posPat.z += 0.5;
      }
      break;
    }  
    case Qt::Key_A: { 
      if (zPat > -6){
        zPat -= 0.5;
        posPat.z += -0.5;
      }
      break;
    }
    default: event->ignore(); break;
  }
  update();
}

void MyGLWidget::mouseMoveEvent (QMouseEvent *event){
  makeCurrent();
  if (DoingInteractive == ROTATE)
  {
    angX += (event->x() - xClick) * factorAngleY;
    angY += (event->y() - yClick) * factorAngleX;
    viewTransform ();
  }

  xClick = event->x();
  yClick = event->y();

  update ();
}


//CAMARA
void MyGLWidget::iniEscena(){ 
  zPorter = zPat = 0;
  radiEscena = sqrt(12*12+2*2+8*8);
  angX = 0;
  angY = 45*M_PI/180;
  posPorter = glm::vec3(11.0, 0.0, 0.0);  // posició inicial del porter
  posPilota = glm::vec3(9.0, 0.0, 0.0);  // posició inicial de la pilota
  posPat = glm::vec3(-11,0,0);
  posIniPilota = posPilota;
  dirInicialPilota();    // direcció inicial de la pilota
  pers = true;
  gol = false;
  indiv = true;
}

void MyGLWidget::viewTransform(){
  glm::vec3 up_in (-1, 0, 0);
  glm::vec3 up_dos (0, 0, -1);
  glm::vec3 up;
  if(indiv) up = up_in;
  else up = up_dos;
  glm::mat4 View(1.0f);
  View = glm::translate(View, glm::vec3(0,0,-2*radiEscena));
  View = glm::rotate(View, float(angY), glm::vec3(1, 0, 0));
  View = glm::rotate(View, float(angX), glm::vec3(0, 1, 0));
  View = glm::translate(View, glm::vec3(0,-2,0));
  if (!pers) View = glm::lookAt(glm::vec3(0,18,0), glm::vec3(0,2,0), up);
  glUniformMatrix4fv (viewLoc, 1, GL_FALSE, &View[0][0]);
}



void MyGLWidget::projectTransform (){
  glm::mat4 Proj(1.0f);
  if (pers) Proj = glm::perspective (float(M_PI/3.0), 1.0f, radiEscena, radiEscena*3);
  else Proj = glm::ortho(-radiEscena, radiEscena, -radiEscena, radiEscena, radiEscena, 3*radiEscena);
  glUniformMatrix4fv (projLoc, 1, GL_FALSE, &Proj[0][0]);
}


void MyGLWidget::rebotaParet(){
  
  if (posPilota.x > -20 and posPilota.x < -10.7) {
    dirPilota = glm::vec3(-dirPilota.x, dirPilota.y, dirPilota.z);
  }
  if (posPilota.z > -20 and posPilota.z < -6.7) {
    dirPilota = glm::vec3(dirPilota.x, dirPilota.y, -dirPilota.z);
  }
  if (posPilota.z < 20 and posPilota.z > 6.7) {
    dirPilota = glm::vec3(dirPilota.x, dirPilota.y, -dirPilota.z);
  }
}
void MyGLWidget::rebotaParetPat(){
  if (posPilota.z > -20 and posPilota.z < -6.7) {
    dirPilota = glm::vec3(dirPilota.x, dirPilota.y, -dirPilota.z);
  }
  if (posPilota.z < 20 and posPilota.z > 6.7) {
    dirPilota = glm::vec3(dirPilota.x, dirPilota.y, -dirPilota.z);
  }
}
