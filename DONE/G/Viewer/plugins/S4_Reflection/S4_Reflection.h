#ifndef _S4_REFLECTION_H
#define _S4_REFLECTION_H

#include "plugin.h" 

class S4_Reflection: public QObject, public Plugin
{
	Q_OBJECT
	Q_PLUGIN_METADATA(IID "Plugin") 
	Q_INTERFACES(Plugin)

  public:
	 void onPluginLoad();
	 void preFrame();
	 void postFrame();

	 void onObjectAdd();
	 bool drawScene();
	 bool drawObject(int);

	 bool paintGL();

	 void keyPressEvent(QKeyEvent *);
	 void mouseMoveEvent(QMouseEvent *);
  private:
	QOpenGLShaderProgram *program;
	QOpenGLShader *vs, *fs;
	GLuint textureID, mirrorVAO;

	void createMirror(GLWidget& g);
	void drawMirror(GLWidget &g);

	QMatrix4x4 reflectionMatrix(float a, float b, float c, float d);

};

#endif
