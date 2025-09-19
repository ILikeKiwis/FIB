#ifndef _S1_SHOW_DEGREE_H
#define _S1_SHOW_DEGREE_H

#include "plugin.h" 
#include <QPainter>

class S1_show_degree: public QObject, public Plugin
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

	float degree;
	QPainter painter;
};

#endif
