#version 330 core

in vec4 frontColor;
out vec4 fragColor;

vec2 C = vec2(0.5, 0.5);

in vec2 vtexCoord;

float aastep(float threshold, float x)
{
 	float width = 0.7*length(vec2(dFdx(x), dFdy(x)));
	return smoothstep(threshold-width, threshold+width, x);
} 

void main()
{
    float d = distance(C, vtexCoord);
    fragColor = vec4(1 - aastep(0.25, d));
}
