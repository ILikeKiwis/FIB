#ifndef _ANIMATE_VERT_H
#define _ANIMATE_VERT_H

#include "plugin.h" 
#include <QElapsedTimer>

class Animate_vert: public QObject, public Plugin
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
	QElapsedTimer elapsedTimer;
	QOpenGLShaderProgram *program;
	QOpenGLShader *fs, *vs;
};

#endif
