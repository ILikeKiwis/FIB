#version 330 core

in vec4 frontColor;
out vec4 fragColor;

in vec2 vtexCoord;

vec4 RED = vec4 (1, 0, 0, 1);

vec4 WHITE = vec4 (1);


vec2 C = vec2 (0.5, 0.5);

void main()
{
    if (distance(C, vtexCoord) > 0.2) fragColor = WHITE; 
    else fragColor = RED;
}
