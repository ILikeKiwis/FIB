#ifndef _S2_DRAWBB_H
#define _S2_DRAWBB_H

#include "plugin.h" 

class S2_drawBB: public QObject, public Plugin
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

	GLuint VAObox;
	GLuint VBOcoord;

	QOpenGLShaderProgram *program;
	QOpenGLShader *fs, *vs;
	string vs_name = "drawBB.vert";
	string fs_name = "drawBB.frag";

};

#endif
