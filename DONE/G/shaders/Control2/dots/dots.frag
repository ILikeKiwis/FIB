#version 330 core

in vec4 gfrontColor;
out vec4 fragColor;

in vec4 P;
in vec4 C;

uniform float size = 0.02;

uniform bool opaque = true;
void main()
{
    float d = distance(P, C);
    if (d > size) {
    	if (opaque) fragColor = vec4(1);
    	else discard;
    } 
    else {
    	fragColor = gfrontColor;
    }
}
