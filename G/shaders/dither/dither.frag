#version 330 core

in float frontColor;
out vec4 fragColor;

uniform int mode = 2;

const vec4 BLACK = vec4(0, 0, 0, 1);
const vec4 WHITE = vec4(1);

bool parell(int x) {
	return x % 2 == 0;
}

void main()
{
	vec4 pos = gl_FragCoord;
	float col = frontColor;
	
	int x = int(pos.x);
	int y = int(pos.y);
	
	if (mode == 2) {
		if (parell(x) && parell(y)) col -= 0.5;
		else if (parell(x) && !parell(y)) col += 0.25;
		else if (!parell(x) && !parell(y)) col -= 0.25;
	}
	
	if (col < 0.5) fragColor = BLACK;
	else fragColor = WHITE;
}


