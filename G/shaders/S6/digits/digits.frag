#version 330 core

in vec4 frontColor;
out vec4 fragColor;

in vec2 vtexCoord;

uniform float time;
uniform sampler2D colorMap;

float off = 1./10.;

void main()
{
	fragColor = vec4(1, 0, 0, 1);
	int cen = int(time) / 100;
	int des = (int(time) % 100) / 10;
	int uni = int(time) % 10;
	vec4 C;
	if (vtexCoord.s < 1) {
		vec2 aux = fract(vtexCoord);
		aux.s *= off;
		aux.s += cen * off;
		C = texture(colorMap, aux);
	}
	else if (vtexCoord.s < 2) {
		vec2 aux = fract(vtexCoord);
		aux.s *= off;
		aux.s += des * off;
		C = texture(colorMap, aux);
	}
	else {
		vec2 aux = fract(vtexCoord);
		aux.s *= off;
		aux.s += uni * off;
		C = texture(colorMap, aux);
	}
	if (C.a < 0.5) discard;
}
