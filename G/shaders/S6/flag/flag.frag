#version 330 core

in vec4 frontColor;
out vec4 fragColor;

in vec2 vtexCoord;

vec4 RED = vec4(1,0,0,1);
vec4 WHITE = vec4(1);

float s = 3./4.;

vec2 C_gran = vec2(0.35, 0.5*s);

vec2 C_gran_tapa = vec2(0.5, 0.5*s);

vec2 C_pet = vec2(0.75, 0.5*s);

void main()
{
    fragColor = RED;
    if (distance(vtexCoord, C_gran_tapa) < 0.3) fragColor = RED;
    else if (distance(vtexCoord, C_gran) < 0.3) fragColor = WHITE;
    if (distance(vtexCoord, C_pet) < 0.15) fragColor = WHITE;
    
}
