#version 330 core

in vec4 frontColor;
out vec4 fragColor;

uniform int N = 2;

in vec2 vtexCoord;

const vec2 C = vec2(0.5, 0.5);

const float R = 0.2;

uniform sampler2D colorMap;

void main()
{
	vec2 st = vtexCoord;
	vec2 delta = st-C;
	float d = length(delta);
	if (d < R && N > 0) {
		//float r = R / N ;
		//st = delta / r;
		//st += (1.0 * N);
		//st /= 2*N;
		for (int i = 1; i <= N; i++) {
			if (d < R/i) {
				float r = R/i;
				st = delta / r;
				st += 1.0;
				st /= 2.0;
			}
		}
	}
	fragColor = texture(colorMap, st);
}
