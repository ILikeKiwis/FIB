#include "animate_vert.h"
#include "glwidget.h"

void Animate_vert::onPluginLoad()
{
	elapsedTimer.start();
	QString vs_src = 
	"#version 330 core\n"
	"layout (location = 0) in vec3 vertex;"
	"layout (location = 1) in vec3 normal;"
	"layout (location = 2) in vec3 color;"
	"layout (location = 3) in vec2 texCoord;"

	"out vec4 frontColor;"
	"out vec2 vtexCoord;"

	"uniform mat4 modelViewProjectionMatrix;"
	"uniform mat3 normalMatrix;"

	"uniform float time;"

	"float amplitude = 0.1;"
	"float freq = 1;"

	"float PI = 3.1415;"

	"void main()"
	"{"
	 "	vec3 N = normalize(normalMatrix * normal);"
	 "	frontColor = vec4(vec3(1),1.0) * N.z;"
	 "	vtexCoord = texCoord;"
	 "	vec3 aux = vertex;"
	 "	float d = amplitude * sin(2*PI*freq*time);"
	 "	aux += normal*d;"
	 "	gl_Position = modelViewProjectionMatrix * vec4(aux, 1.0);"
	"}";
	
	vs = new QOpenGLShader(QOpenGLShader::Vertex, this);
	vs->compileSourceCode(vs_src);
	cout << "VS log:" << vs->log().toStdString() << endl;
	
	QString fs_src = 
	"#version 330 core\n"
	"in vec4 frontColor;"
	"out vec4 fragColor;"
	"void main() {"
	"	fragColor = frontColor;"
	"}";
	
	fs = new QOpenGLShader(QOpenGLShader::Fragment, this);
	fs->compileSourceCode(fs_src);
	cout << "FS log:" << fs->log().toStdString() << endl;
	
	program = new QOpenGLShaderProgram(this);
	program->addShader(vs);
	program->addShader(fs);
	program->link();
	cout << "Link log:" << program->log().toStdString() << endl;
}

void Animate_vert::preFrame()
{
	program->bind();
	
	program->setUniformValue("time", float(elapsedTimer.elapsed() / 1000.0));
	QMatrix4x4 MVP = camera()->projectionMatrix() * camera()->viewMatrix();
	program->setUniformValue("modelViewProjectionMatrix", MVP);
	QMatrix3x3 N = camera()->viewMatrix().normalMatrix();
	program->setUniformValue("normalMatrix", N);
}

void Animate_vert::postFrame()
{
	program->release();
}

void Animate_vert::onObjectAdd()
{
	
}

bool Animate_vert::drawScene()
{
	return false; // return true only if implemented
}

bool Animate_vert::drawObject(int)
{
	return false; // return true only if implemented
}

bool Animate_vert::paintGL()
{
	return false; // return true only if implemented
}

void Animate_vert::keyPressEvent(QKeyEvent *)
{
	
}

void Animate_vert::mouseMoveEvent(QMouseEvent *)
{
	
}

