#version 330 core

in vec4 frontColor;
out vec4 fragColor;

in vec2 vtexCoord;

vec4 BLACK = vec4(0);
vec4 GREY = vec4(0.8);

uniform float n = 8;

int s = int(fract(vtexCoord.s) * n);

int t = int(fract(vtexCoord.t) * n);


void main()
{
    if ( (s+t) % 2 == 0) fragColor = GREY;
    else fragColor = BLACK;
}
