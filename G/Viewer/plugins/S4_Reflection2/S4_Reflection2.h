#ifndef _S4_REFLECTION2_H
#define _S4_REFLECTION2_H

#include "plugin.h" 

class S4_Reflection2: public QObject, public Plugin
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
	GLuint textureID_Z, textureID_XY, textureID_ZY, mirrorZVAO, mirrorXYVAO, mirrorZYVAO;

	void createMirror(GLWidget& g);
	void drawMirror(GLWidget &g);

	QMatrix4x4 reflectionMatrix(float a, float b, float c, float d);

};

#endif
