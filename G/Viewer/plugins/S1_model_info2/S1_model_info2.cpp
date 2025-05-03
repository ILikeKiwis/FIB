#include "S1_model_info2.h"
#include "glwidget.h"

void S1_model_info2::onPluginLoad()
{
	
}

void S1_model_info2::preFrame()
{
	
}

void S1_model_info2::postFrame()
{
	int objects = scene()->objects().size();
	int poligons = 0;
	int vertex = 0;
	//int vertex = 0;
	int triangles = 0;
	for (int i = 0; i < objects; i++) {
		Object aux = scene()->objects()[i];
		poligons += aux.faces().size();
		vertex += aux.vertices().size();
		for (int j = 0; j < aux.faces().size(); j ++) {
			if (aux.faces()[j].numVertices() == 3) triangles++;
		}
	}
	float t = triangles / float(poligons);
	QFont font;
	font.setPixelSize(20);
	int x = 15;
	int y_ini = 35;
	painter.begin(glwidget());
	painter.setFont(font);
	painter.drawText(x, y_ini, QString::number(objects));
	painter.drawText(x, y_ini+25, QString::number(poligons));
	painter.drawText(x, y_ini+50, QString::number(vertex));
	painter.drawText(x, y_ini+75, QString::number(t));
	painter.end();

}

void S1_model_info2::onObjectAdd()
{
	
}

bool S1_model_info2::drawScene()
{
	return false; // return true only if implemented
}

bool S1_model_info2::drawObject(int)
{
	return false; // return true only if implemented
}

bool S1_model_info2::paintGL()
{
	return false; // return true only if implemented
}

void S1_model_info2::keyPressEvent(QKeyEvent *)
{
	
}

void S1_model_info2::mouseMoveEvent(QMouseEvent *)
{
	
}

