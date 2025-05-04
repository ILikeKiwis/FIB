#ifndef _S3_DEPTHNORMAL_H
#define _S3_DEPTHNORMAL_H

#include "plugin.h" 

class S3_depthnormal: public QObject, public Plugin
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

	QOpenGLShaderProgram* program, *program1;
	QOpenGLShader *fs_d, *vs_d;
	QOpenGLShader *fs_n, *vs_n;

};

#endif
