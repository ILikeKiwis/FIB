#version 330 core

in vec4 frontColor;
out vec4 fragColor;

in vec2 vtexCoord;
in vec3 N;

uniform sampler2D colormap;

vec2 C1 = vec2(0.34, 0.65);
vec2 C2 = vec2(0.66, 0.65);

void main()
{
    fragColor = texture(colormap, vtexCoord);
    C1 += -0.1*N.xy;
    C2 += -0.1*N.xy;
    if (distance(vtexCoord, C1) < 0.05 || distance(vtexCoord, C2) < 0.05) fragColor = vec4(0);
    
}
