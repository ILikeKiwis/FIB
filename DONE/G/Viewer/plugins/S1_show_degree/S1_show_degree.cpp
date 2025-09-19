#include "S1_show_degree.h"
#include "glwidget.h"

void S1_show_degree::onPluginLoad()
{
	Object obj = scene()->objects().at(0);
	int aristes = 0;
	for (Face f : obj.faces()) {
		aristes += f.numVertices();
	}

	degree = float(aristes) / float(obj.vertices().size());
}

void S1_show_degree::preFrame()
{
	
}

void S1_show_degree::postFrame()
{
	QFont font;
	font.setPixelSize(32);
	painter.begin(glwidget());
	painter.setFont(font);
	int x = 15;
	int y = 40;
	painter.drawText(x, y, QString::number(degree));
	painter.end();
}

void S1_show_degree::onObjectAdd()
{
	onPluginLoad();
}

bool S1_show_degree::drawScene()
{
	return false; // return true only if implemented
}

bool S1_show_degree::drawObject(int)
{
	return false; // return true only if implemented
}

bool S1_show_degree::paintGL()
{
	return false; // return true only if implemented
}

void S1_show_degree::keyPressEvent(QKeyEvent *)
{
	
}

void S1_show_degree::mouseMoveEvent(QMouseEvent *)
{
	
}

