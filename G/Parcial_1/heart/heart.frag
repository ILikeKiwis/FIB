#version 330 core

in vec4 frontColor;
out vec4 fragColor;
in vec2 vtexCoord;

vec2 C1 = vec2(0.35, 0.6);
vec2 C2 = vec2(0.65,0.6);
vec2 C3 = vec2(0.5, 0.13);

uniform int mode = 0;

vec4 WHITE = vec4(1);
vec4 RED = vec4(1,0,0,1);


void main()
{
    fragColor = WHITE;
    if(distance(vtexCoord, C1) < 0.255 || distance(vtexCoord, C2) < 0.255) fragColor = RED;
    else if(distance(vtexCoord, C3) < 0.45) {
    	fragColor = RED;
    }
}
