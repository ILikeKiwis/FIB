#include "modelInfo1.h"
#include "glwidget.h"

void ModelInfo1::onPluginLoad()
{
	
}

void ModelInfo1::preFrame()
{
	
}

void ModelInfo1::postFrame()
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
	cout << "o " <<objects << std::endl;
	cout << "p " <<poligons << std::endl;
	cout << "v " <<vertex << std::endl;
	cout << "% " <<t << std::endl;
	cout << "tr " <<triangles << endl;
}

void ModelInfo1::onObjectAdd()
{
	
}

bool ModelInfo1::drawScene()
{
	return false; // return true only if implemented
}

bool ModelInfo1::drawObject(int)
{
	return false; // return true only if implemented
}

bool ModelInfo1::paintGL()
{
	return false; // return true only if implemented
}

void ModelInfo1::keyPressEvent(QKeyEvent *)
{
	
}

void ModelInfo1::mouseMoveEvent(QMouseEvent *)
{
	
}

