#include "S2_drawBB.h"
#include "glwidget.h"


void S2_drawBB::onPluginLoad()
{
	GLWidget &g = *glwidget();
	float coords [] = {
		1, 0, 0,	//C
		0, 0, 0,	//D
		1, 1, 0,	//B
		0, 1, 0,	//A
		0, 1, 1,	//G
		0, 0, 0,	//D
		0, 0, 1,	//H
		1, 0, 0, 	//C
		1, 0, 1, 	//E
		1, 1, 0, 	//B
		1, 1, 1, 	//F
		0, 1, 1, 	//G
		1, 0, 1, 	//E
		0, 0, 1		//H
	};

	
	g.makeCurrent();
	g.glGenVertexArrays(1, &VAObox);
	g.glGenBuffers(1, &VBOcoord);
	g.glBindVertexArray(VAObox);
	g.glBindBuffer(GL_ARRAY_BUFFER, VBOcoord);
	g.glBufferData(GL_ARRAY_BUFFER, sizeof(coords), coords, GL_STATIC_DRAW);
	g.glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, 0);
	g.glEnableVertexAttribArray(0);
	g.glBindVertexArray(0);

	vs = new QOpenGLShader(QOpenGLShader::Vertex);
	fs = new QOpenGLShader(QOpenGLShader::Fragment);
	vs->compileSourceFile("drawBB.vert");
	fs->compileSourceFile("drawBB.frag");
	program = new QOpenGLShaderProgram();
	program->addShader(vs);
	program->addShader(fs);		//Preguntar lo de addshaderfrom source file

	program->link();
	
	for (Object & obj : g.scene()->objects()){
		obj.computeBoundingBox();
	}
	g.glBindVertexArray(VAObox);
	g.glDrawArrays(GL_TRIANGLES, 0, 14);

}

void S2_drawBB::preFrame()
{
	
}

void S2_drawBB::postFrame()
{
	GLWidget &g = *glwidget();
	program->bind();
	g.makeCurrent();
	GLint polygonMode;
	g.glGetIntegerv(GL_POLYGON_MODE, &polygonMode);
	
	g.glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
	for (Object & obj : g.scene()->objects()){
		Point  trans = obj.boundingBox().min();
		Point scale = obj.boundingBox().max() - obj.boundingBox().min();
		
		program->setUniformValue("translate", trans);
		program->setUniformValue("scale", scale);
		QMatrix4x4 mvp = g.camera()->projectionMatrix() * g.camera()->viewMatrix();
		program->setUniformValue("modelViewProjectionMatrix", mvp);
		g.glBindVertexArray(VAObox);
		g.glDrawArrays(GL_TRIANGLE_STRIP, 0, 14);

	}
	g.glPolygonMode(GL_FRONT_AND_BACK, polygonMode);
	program->release();
}

void S2_drawBB::onObjectAdd()
{
	GLWidget & widget = * glwidget();
	widget.makeCurrent();
	for (Object & object : widget.scene()->objects())
		object.computeBoundingBox();

}

bool S2_drawBB::drawScene()
{
	return false; // return true only if implemented
}

bool S2_drawBB::drawObject(int)
{
	return false; // return true only if implemented
}

bool S2_drawBB::paintGL()
{
	return false; // return true only if implemented
}

void S2_drawBB::keyPressEvent(QKeyEvent *)
{
	
}

void S2_drawBB::mouseMoveEvent(QMouseEvent *)
{
	
}

