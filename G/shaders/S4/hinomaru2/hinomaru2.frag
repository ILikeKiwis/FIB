#version 330 core

in vec4 frontColor;
out vec4 fragColor;

in vec2 vtexCoord;

vec4 RED = vec4 (1, 0, 0, 1);

vec4 WHITE = vec4 (1);

const float PI = 3.141592;

vec2 C = vec2 (0.5, 0.5);

const float psi = PI / 16.0;

uniform bool classic = true;



void main()
{
    float d = distance(C, vtexCoord);	
    vec2 u = vtexCoord - C;
    float a = atan(u.s, u.t);
    if (d<0.2) fragColor = RED; 
    else if (!classic && (mod(a/psi + 0.5, 2) < 1)) fragColor = RED;
    else fragColor = WHITE;
}
