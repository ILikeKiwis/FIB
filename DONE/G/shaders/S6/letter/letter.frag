#version 330 core

in vec4 frontColor;
out vec4 fragColor;

in vec2 vtexCoord;

vec4 W = vec4(1);
vec4 RED = vec4(1,0,0,1);
vec4 BLUE = vec4(0,0,1,1);
vec4 GREEN = vec4(0,1,0,1);

float s = vtexCoord.x * 9;
float t = vtexCoord.y * 9;

vec4 BLACK = vec4(0);
vec4 GREY = vec4(0.8);


void main()
{
    int col = int (s);
    int fila = int(t);
    
    fragColor = W;
    
    
    
    //if (col == fila) fragColor = GREEN; Diagonal parriba
    //if (col == 8 - fila) fragColor = BLUE; Diagonal pabajo 
    
    if (col == 2 && fila > 0 && fila < 8) fragColor = BLACK; // Palo
    if (col > 2 && (col == fila- 1  || col == 8 - (fila + 1)) && fila < 8 && fila > 0) fragColor = BLACK;
    // Ultima 
    if (fract(s) < 0.05 || fract(t) < 0.05) fragColor = W;
}
