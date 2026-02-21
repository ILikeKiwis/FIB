#include "S5_boundry.h"
#include "glwidget.h"
#include <set>

void S5_boundry::onPluginLoad()
{
	boundry();
}

void S5_boundry::preFrame()
{
	
}

void S5_boundry::postFrame()
{
	
}

void S5_boundry::onObjectAdd()
{
	boundry();
}

bool S5_boundry::drawScene()
{
	return false; // return true only if implemented
}

bool S5_boundry::drawObject(int)
{
	return false; // return true only if implemented
}

bool S5_boundry::paintGL()
{
	return false; // return true only if implemented
}

void S5_boundry::keyPressEvent(QKeyEvent *)
{
	
}

void S5_boundry::mouseMoveEvent(QMouseEvent *)
{
	
}

void S5_boundry::boundry(){
	int n_obj = scene()->objects().size();

	for (int i = 0; i < n_obj; i++) {
		set<pair<int ,int>> edges;
		set<pair<int, int>> rep;
		Object aux = scene()->objects()[i];
		for (int j = 0; j < aux.faces().size(); j++) {
			Face f = aux.faces()[j]; 
			for (int k = 0; k < f.numVertices(); k++) {
				int v1 = f.vertexIndex(k);
				int v2 = f.vertexIndex((k+1)%f.numVertices());

				pair<int, int> p (v1, v2);

				if (v1 > v2) {
					p = pair<int, int > (v2, v1);
				}

				if (!rep.insert(p).second) rep.erase(p);

				edges.insert(p);
			}
		}
		cout << "E=" << edges.size() << endl;
		cout << "Border=" << rep.size() << endl;
		cout << endl;
 	}
}

