#ifndef _S5_LABELER_H
#define _S5_LABELER_H

#include "plugin.h" 

class S5_Labeler: public QObject, public Plugin
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
	// add private methods and attributes here

	QOpenGLShader *vs, *fs, *gs;
	QOpenGLShaderProgram *program;
};

#endif
