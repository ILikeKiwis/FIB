#include "s3_depthnormal.h"
#include "glwidget.h"

void S3_depthnormal::onPluginLoad()
{
	program = new QOpenGLShaderProgram();
	program1 = new QOpenGLShaderProgram();
	fs_d = new QOpenGLShader(QOpenGLShader::Fragment);
	fs_n = new QOpenGLShader(QOpenGLShader::Fragment);
	vs_d = new QOpenGLShader(QOpenGLShader::Vertex);
	vs_n = new QOpenGLShader(QOpenGLShader::Vertex);

	fs_d->compileSourceFile("depth.frag");
	fs_n->compileSourceFile("normal.frag");
	vs_d->compileSourceFile("depth.vert");
	vs_n->compileSourceFile("normal.vert");

	
}

void S3_depthnormal::preFrame()
{
	
}

void S3_depthnormal::postFrame()
{
	
}

void S3_depthnormal::onObjectAdd()
{
	
}

bool S3_depthnormal::drawScene()
{
	return false; // return true only if implemented
}

bool S3_depthnormal::drawObject(int)
{
	return false; // return true only if implemented
}

bool S3_depthnormal::paintGL()
{
	GLWidget& g = *glwidget();
	g.makeCurrent();
	float ar = float(glwidget()->width()) / float(glwidget()->height());
	camera()->setAspectRatio(ar);

	// Pas 1

	program->addShader(fs_d);
	program->addShader(vs_d);
	program->link();
	program->bind();

	QMatrix4x4 MVP = camera()->projectionMatrix() * camera()->viewMatrix();


	program->setUniformValue("modelViewProjectionMatrix", MVP);


	float w = g.width();
	float h = g.height();

	g.glViewport(0, h/4, w/2, h/2);

	drawPlugin()->drawScene();

	program->release();
	//program->removeAllShaders();		//PREGUNTAR COMO SE HARIA CON SOLO UN PROGRAMA

	program1->addShader(fs_n);
	program1->addShader(vs_n);
	program1->link();
	program1->bind();

	g.glViewport(w/2, h/4, w/2, h/2);

	MVP = camera()->projectionMatrix() * camera()->viewMatrix();
	QMatrix3x3 N = camera()->viewMatrix().normalMatrix();

	program1->setUniformValue("normalMatrix", N);
	program1->setUniformValue("modelViewProjectionMatrix", MVP);

	drawPlugin()->drawScene();

	program1->release();
	
	return true; // return true only if implemented
}

void S3_depthnormal::keyPressEvent(QKeyEvent *)
{
	
}

void S3_depthnormal::mouseMoveEvent(QMouseEvent *)
{
	
}

