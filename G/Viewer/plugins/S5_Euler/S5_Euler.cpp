#include "S5_Euler.h"
#include "glwidget.h"
#include <set>

void S5_Euler::onPluginLoad()
{
	Euler();
}

void S5_Euler::preFrame()
{
	
}

void S5_Euler::postFrame()
{
	
}

void S5_Euler::onObjectAdd()
{
	Euler();
}

bool S5_Euler::drawScene()
{
	return false; // return true only if implemented
}

bool S5_Euler::drawObject(int)
{
	return false; // return true only if implemented
}

bool S5_Euler::paintGL()
{
	return false; // return true only if implemented
}

void S5_Euler::keyPressEvent(QKeyEvent *)
{
	
}

void S5_Euler::mouseMoveEvent(QMouseEvent *)
{
	
}

void S5_Euler::Euler() {
	int n_obj = scene()->objects().size();

	for (int i = 0; i < n_obj; i++) {
		set<pair<int ,int>> edges;
		Object aux = scene()->objects()[i];
		cout << "F=" << aux.faces().size() << endl;
		cout << "V=" << aux.vertices().size() << endl;
		for (int j = 0; j < aux.faces().size(); j++) {
			Face f = aux.faces()[j]; 
			for (int k = 0; k < f.numVertices(); k++) {
				int v1 = f.vertexIndex(k);
				int v2 = f.vertexIndex((k+1)%f.numVertices());

				pair<int, int> p (v1, v2);

				if (v1 > v2) {
					p = pair<int, int > (v2, v1);
				}

				edges.insert(p);
			}
		}
		cout << "E=" << edges.size() << endl;
		cout << "X=" << aux.faces().size() + aux.vertices().size() - edges.size() << endl;
		cout << endl;
 	}
}