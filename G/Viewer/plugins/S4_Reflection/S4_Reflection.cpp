#include "S4_Reflection.h"
#include "glwidget.h"

const int IMAGE_WIDTH = 512;
const int IMAGE_HEIGHT = IMAGE_WIDTH;

const QMatrix4x4 ref_mat = QMatrix4x4(
	1, 0, 0, 0,
	0, -1, 0, 0, 
	0, 0, 1, 0,
	0, 0, 0, 1
);


void S4_Reflection::onPluginLoad()
{
	GLWidget & g = *glwidget();
	g.makeCurrent();

	vs = new QOpenGLShader(QOpenGLShader::Vertex);
	fs = new QOpenGLShader(QOpenGLShader::Fragment);

	vs->compileSourceFile(g.getPluginPath() + "/../S4_Reflection/reflection.vert");
	fs->compileSourceFile(g.getPluginPath() + "/../S4_Reflection/reflection.frag");

	program = new QOpenGLShaderProgram();

	program->addShader(vs);
	program->addShader(fs);
	program->link();

	g.glActiveTexture(GL_TEXTURE0);
	g.glGenTextures( 1, &textureID);
	g.glBindTexture(GL_TEXTURE_2D, textureID);
	g.glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
	g.glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
	g.glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR);
	g.glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
	g.glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, IMAGE_WIDTH, IMAGE_HEIGHT, 0, GL_RGB, GL_FLOAT, NULL);
	g.glBindTexture(GL_TEXTURE_2D, 0);
	g.resize(IMAGE_WIDTH,IMAGE_HEIGHT);


	createMirror(g);
}

void S4_Reflection::preFrame()
{
	
}

void S4_Reflection::postFrame()
{
	
}

void S4_Reflection::onObjectAdd()
{
	GLWidget & widget = *glwidget();
	widget.makeCurrent();
	createMirror(widget);
}

bool S4_Reflection::drawScene()
{
	return false; // return true only if implemented
}

bool S4_Reflection::drawObject(int)
{
	return false; // return true only if implemented
}

bool S4_Reflection::paintGL()
{
	GLWidget & g = *glwidget();
	g.makeCurrent();

	program->bind();
	program->setUniformValue("modelViewProjectionMatrix", g.camera()->projectionMatrix() * g.camera()->viewMatrix());
	program->setUniformValue("mirror", false);

	g.glClearColor(1, 1, 1, 0);
	g.glClear(GL_DEPTH_BUFFER_BIT | GL_COLOR_BUFFER_BIT);

	program->setUniformValue("refMat", reflectionMatrix(0, -1, 0, g.scene()->boundingBox().min().y()));

	if (drawPlugin()) drawPlugin()->drawScene();
	
	g.glBindTexture(GL_TEXTURE_2D, textureID);
	g.glCopyTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, 0, 0, IMAGE_WIDTH, IMAGE_HEIGHT);
	g.glGenerateMipmap(GL_TEXTURE_2D);


	g.glClear(GL_DEPTH_BUFFER_BIT | GL_COLOR_BUFFER_BIT);


	program->setUniformValue("refMat", QMatrix4x4());

	if (drawPlugin()) drawPlugin()->drawScene();

	program->setUniformValue("colorMap", 0);
	program->setUniformValue("size", QVector2D(float(IMAGE_WIDTH), float(IMAGE_HEIGHT)));
	program->setUniformValue("mirror", true);
	drawMirror(g);
	
	g.glBindTexture(GL_TEXTURE_2D, 0);
	g.defaultProgram()->bind();
	

	return true; // return true only if implemented
}

void S4_Reflection::keyPressEvent(QKeyEvent *)
{
	
}

void S4_Reflection::mouseMoveEvent(QMouseEvent *)
{
	
}

void S4_Reflection::createMirror(GLWidget & g){
	GLuint VBO;
	const Point & min = g.scene()->boundingBox().min();
	const Point & max = g.scene()->boundingBox().max();
	float coords[] = {
		min.x(), min.y(), min.z(), 
		max.x(), min.y(), min.z(),
		min.x(), min.y(), max.z(),
		max.x(), min.y(), max.z()
	};
	g.glGenVertexArrays(1, &mirrorVAO);
	g.glBindVertexArray(mirrorVAO);
	g.glGenBuffers(1, &VBO);
	g.glBindBuffer(GL_ARRAY_BUFFER, VBO);
	g.glBufferData(GL_ARRAY_BUFFER, sizeof(coords), coords, GL_STATIC_DRAW);
	g.glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, 0);
	g.glEnableVertexAttribArray(0);
	g.glBindVertexArray(0);

}

void S4_Reflection::drawMirror(GLWidget &g){
	g.glBindVertexArray(mirrorVAO);
	g.glDrawArrays(GL_TRIANGLE_STRIP, 0, 4);
	g.glBindVertexArray(0);
}

QMatrix4x4 S4_Reflection::reflectionMatrix(float a, float b, float c, float d) {
	return QMatrix4x4(
	1 - 2 * a * a,   - 2 * a * b,   - 2 * a * c, - 2 * a * d,
 	  - 2 * a * b, 1 - 2 * b * b,   - 2 * b * c, - 2 * b * d,
	   -2 * a * c,   - 2 * b * c, 1 - 2 * c * c, - 2 * c * d,
	            0,             0,             0,           1
	);
}
