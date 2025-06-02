#include "Wire.h"
#include "glwidget.h"

void Wire::onPluginLoad()
{
	QString vert = 
	"#version 330 core\n"
	"uniform mat4 modelViewProjectionMatrix;"
	"in vec3 vertex;"
	"in vec3 normal;"
	"uniform mat3 normalMatrix;"
	"out vec4 frontColor;"
	"void main() {"
	"	vec3 N = normalize(normalMatrix * normal);"
	"	frontColor = vec4(vec3(N.z), 1.0);"
	"	gl_Position = modelViewProjectionMatrix * vec4(vertex, 1.0);"
	"}";	

	QString frag = 
	"#version 330 core \n"
	"in vec4 frontColor;"
	"out vec4 fragColor;"
	"uniform bool poly;"
	"void main() {"
	"	fragColor = frontColor;"
	"	if (poly) fragColor = vec4(0,0,0,1);"
	"}";

	vs = new QOpenGLShader(QOpenGLShader::Vertex);
	fs = new QOpenGLShader(QOpenGLShader::Fragment);

	vs->compileSourceCode(vert);
	fs->compileSourceCode(frag);

	program = new QOpenGLShaderProgram();

	program->addShader(vs);
	program->addShader(fs);
	program->link();
}

void Wire::preFrame()
{
	
}

void Wire::postFrame()
{
	
}

void Wire::onObjectAdd()
{
	
}

bool Wire::drawScene()
{
	return false; // return true only if implemented
}

bool Wire::drawObject(int)
{
	return false; // return true only if implemented
}

bool Wire::paintGL()
{
	GLWidget &g = *glwidget();
	g.makeCurrent();

	program->bind();
	program->setUniformValue("modelViewProjectionMatrix", camera()->projectionMatrix() * camera()->viewMatrix());
	program->setUniformValue("normalMatrix", camera()->viewMatrix().normalMatrix());
	program->setUniformValue("poly", false);

	g.glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);
	g.glPolygonOffset(0, 0);
	drawPlugin()->drawScene();

	program->setUniformValue("poly", true);

	g.glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
	g.glEnable(GL_POLYGON_OFFSET_LINE);
	g.glPolygonOffset(-1.0, -1.0);
	if (drawPlugin()) drawPlugin()->drawScene();
	return true; // return true only if implemented
}

void Wire::keyPressEvent(QKeyEvent *)
{
	
}

void Wire::mouseMoveEvent(QMouseEvent *)
{
	
}

