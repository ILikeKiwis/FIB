#include "S4_Reflection2.h"
#include "glwidget.h"

const int IMAGE_WIDTH = 512;
const int IMAGE_HEIGHT = IMAGE_WIDTH;

const QMatrix4x4 ref_mat = QMatrix4x4(
	1, 0, 0, 0,
	0, -1, 0, 0, 
	0, 0, 1, 0,
	0, 0, 0, 1
);


void S4_Reflection2::onPluginLoad()
{
	GLWidget & g = *glwidget();
	g.makeCurrent();

	vs = new QOpenGLShader(QOpenGLShader::Vertex);
	fs = new QOpenGLShader(QOpenGLShader::Fragment);

	vs->compileSourceFile("reflection.vert");
	fs->compileSourceFile("reflection.frag");

	program = new QOpenGLShaderProgram();

	program->addShader(vs);
	program->addShader(fs);
	program->link();

	g.glActiveTexture(GL_TEXTURE0);
	g.glGenTextures( 1, &textureID_Z);
	g.glBindTexture(GL_TEXTURE_2D, textureID_Z);
	g.glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
	g.glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
	g.glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR);
	g.glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
	g.glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, IMAGE_WIDTH, IMAGE_HEIGHT, 0, GL_RGB, GL_FLOAT, NULL);
	g.glBindTexture(GL_TEXTURE_2D, 0);
	g.resize(IMAGE_WIDTH,IMAGE_HEIGHT);

	g.glActiveTexture(GL_TEXTURE1);
	g.glGenTextures( 1, &textureID_ZY);
	g.glBindTexture(GL_TEXTURE_2D, textureID_ZY);
	g.glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
	g.glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
	g.glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR);
	g.glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
	g.glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, IMAGE_WIDTH, IMAGE_HEIGHT, 0, GL_RGB, GL_FLOAT, NULL);
	g.glBindTexture(GL_TEXTURE_2D, 1);
	g.resize(IMAGE_WIDTH,IMAGE_HEIGHT);

	g.glActiveTexture(GL_TEXTURE2);
	g.glGenTextures( 1, &textureID_XY);
	g.glBindTexture(GL_TEXTURE_2D, textureID_XY);
	g.glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
	g.glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
	g.glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR);
	g.glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
	g.glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, IMAGE_WIDTH, IMAGE_HEIGHT, 0, GL_RGB, GL_FLOAT, NULL);
	g.glBindTexture(GL_TEXTURE_2D, 2);
	g.resize(IMAGE_WIDTH,IMAGE_HEIGHT);

	createMirror(g);
}

void S4_Reflection2::preFrame()
{
	
}

void S4_Reflection2::postFrame()
{
	
}

void S4_Reflection2::onObjectAdd()
{
	GLWidget & widget = *glwidget();
	widget.makeCurrent();
	createMirror(widget);
}

bool S4_Reflection2::drawScene()
{
	return false; // return true only if implemented
}

bool S4_Reflection2::drawObject(int)
{
	return false; // return true only if implemented
}

bool S4_Reflection2::paintGL()
{
	GLWidget & g = *glwidget();
	g.makeCurrent();

	program->bind();
	program->setUniformValue("modelViewProjectionMatrix", g.camera()->projectionMatrix() * g.camera()->viewMatrix());
	program->setUniformValue("mirror", 0);

	g.glClearColor(1, 1, 1, 0);
	g.glClear(GL_DEPTH_BUFFER_BIT | GL_COLOR_BUFFER_BIT);

	program->setUniformValue("refMat", reflectionMatrix(0, -1, 0, g.scene()->boundingBox().min().y()));

	if (drawPlugin()) drawPlugin()->drawScene();
	
	g.glActiveTexture(GL_TEXTURE0);
	g.glBindTexture(GL_TEXTURE_2D, textureID_Z);
	g.glCopyTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, 0, 0, IMAGE_WIDTH, IMAGE_HEIGHT);
	g.glGenerateMipmap(GL_TEXTURE_2D);

	g.glClear(GL_DEPTH_BUFFER_BIT | GL_COLOR_BUFFER_BIT);

	program->setUniformValue("refMat", reflectionMatrix(0, 0, -1, g.scene()->boundingBox().min().z()));

	if (drawPlugin()) drawPlugin()->drawScene();
	
	g.glActiveTexture(GL_TEXTURE1);
	g.glBindTexture(GL_TEXTURE_2D, textureID_ZY);
	g.glCopyTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, 0, 0, IMAGE_WIDTH, IMAGE_HEIGHT);
	g.glGenerateMipmap(GL_TEXTURE_2D);

	

	g.glClear(GL_DEPTH_BUFFER_BIT | GL_COLOR_BUFFER_BIT);

	program->setUniformValue("refMat", reflectionMatrix(-1, 0, 0, g.scene()->boundingBox().min().x()));

	if (drawPlugin()) drawPlugin()->drawScene();
	
	g.glActiveTexture(GL_TEXTURE2);
	g.glBindTexture(GL_TEXTURE_2D, textureID_XY);
	g.glCopyTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, 0, 0, IMAGE_WIDTH, IMAGE_HEIGHT);
	g.glGenerateMipmap(GL_TEXTURE_2D);

	
	g.glClear(GL_DEPTH_BUFFER_BIT | GL_COLOR_BUFFER_BIT);
	// Ultima pintada 
	program->setUniformValue("refMat", QMatrix4x4());
	//program->setUniformValue("mirror", 0);

	if (drawPlugin()) drawPlugin()->drawScene();

	g.glActiveTexture(GL_TEXTURE0);
	g.glBindTexture(GL_TEXTURE_2D, textureID_Z);

	g.glActiveTexture(GL_TEXTURE1);
	g.glBindTexture(GL_TEXTURE_2D, textureID_ZY);

	g.glActiveTexture(GL_TEXTURE2);
	g.glBindTexture(GL_TEXTURE_2D, textureID_XY);
	program->setUniformValue("colorMap", 0);
	program->setUniformValue("colorMap1", 2);
	program->setUniformValue("colorMap2", 1);
	program->setUniformValue("size", QVector2D(float(IMAGE_WIDTH), float(IMAGE_HEIGHT)));


	drawMirror(g);
	
	g.glActiveTexture(GL_TEXTURE0);
	g.glBindTexture(GL_TEXTURE_2D, 0);

	g.glActiveTexture(GL_TEXTURE1);
	g.glBindTexture(GL_TEXTURE_2D, 0);

	g.glActiveTexture(GL_TEXTURE2);
	g.glBindTexture(GL_TEXTURE_2D, 0);

	//g.defaultProgram()->bind();
	

	return true; // return true only if implemented
}

void S4_Reflection2::keyPressEvent(QKeyEvent *)
{
	
}

void S4_Reflection2::mouseMoveEvent(QMouseEvent *)
{
	
}

void S4_Reflection2::createMirror(GLWidget & g){
	GLuint VBO_Z;
	const Point & min = g.scene()->boundingBox().min();
	const Point & max = g.scene()->boundingBox().max();
	float coords[] = {
		min.x(), min.y(), min.z(), 
		max.x(), min.y(), min.z(),
		min.x(), min.y(), max.z(),
		max.x(), min.y(), max.z()
	};
	g.glGenVertexArrays(1, &mirrorZVAO);
	g.glBindVertexArray(mirrorZVAO);
	g.glGenBuffers(1, &VBO_Z);
	g.glBindBuffer(GL_ARRAY_BUFFER, VBO_Z);
	g.glBufferData(GL_ARRAY_BUFFER, sizeof(coords), coords, GL_STATIC_DRAW);
	g.glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, 0);
	g.glEnableVertexAttribArray(0);
	g.glBindVertexArray(0);

	float coordsXY[] = {
		min.x(), min.y(), min.z(), 
		min.x(), max.y(), min.z(),
		max.x(), min.y(), min.z(),
		max.x(), max.y(), min.z()
	};

	GLuint VBO_XY;
	g.glGenVertexArrays(1, &mirrorXYVAO);
	g.glBindVertexArray(mirrorXYVAO);
	g.glGenBuffers(1, &VBO_XY);
	g.glBindBuffer(GL_ARRAY_BUFFER, VBO_XY);
	g.glBufferData(GL_ARRAY_BUFFER, sizeof(coordsXY), coordsXY, GL_STATIC_DRAW);
	g.glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, 0);
	g.glEnableVertexAttribArray(0);
	g.glBindVertexArray(0);


	float coordsZY[] = {
		min.x(), min.y(), min.z(), 
		min.x(), max.y(), min.z(),
		min.x(), min.y(), max.z(),
		min.x(), max.y(), max.z()
	};

	GLuint VBO_ZY;
	g.glGenVertexArrays(1, &mirrorZYVAO);
	g.glBindVertexArray(mirrorZYVAO);
	g.glGenBuffers(1, &VBO_ZY);
	g.glBindBuffer(GL_ARRAY_BUFFER, VBO_ZY);
	g.glBufferData(GL_ARRAY_BUFFER, sizeof(coordsZY), coordsZY, GL_STATIC_DRAW);
	g.glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, 0);
	g.glEnableVertexAttribArray(0);
	g.glBindVertexArray(0);


}

void S4_Reflection2::drawMirror(GLWidget &g){
	program->setUniformValue("mirror", 1);
	g.glBindVertexArray(mirrorZVAO);
	g.glDrawArrays(GL_TRIANGLE_STRIP, 0, 4);
	g.glBindVertexArray(0);

	program->setUniformValue("mirror", 2);
	g.glBindVertexArray(mirrorZYVAO);
	g.glDrawArrays(GL_TRIANGLE_STRIP, 0, 4);
	g.glBindVertexArray(0);

	program->setUniformValue("mirror", 3);
	g.glBindVertexArray(mirrorXYVAO);
	g.glDrawArrays(GL_TRIANGLE_STRIP, 0, 4);
	g.glBindVertexArray(0);
}

QMatrix4x4 S4_Reflection2::reflectionMatrix(float a, float b, float c, float d) {
	return QMatrix4x4(
	1 - 2 * a * a,   - 2 * a * b,   - 2 * a * c, - 2 * a * d,
 	  - 2 * a * b, 1 - 2 * b * b,   - 2 * b * c, - 2 * b * d,
	   -2 * a * c,   - 2 * b * c, 1 - 2 * c * c, - 2 * c * d,
	            0,             0,             0,           1
	);
}
