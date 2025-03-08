#version 330 core

in vec4 frontColor;
out vec4 fragColor;

in vec2 vtexCoord;

uniform float time;

uniform sampler2D fons;
uniform sampler2D noise1;

vec2 a = vec2(.003, -.005);

void main()
{
    vec4 n = texture(noise1, vec2(vtexCoord.s + 0.08*time, vtexCoord.t + 0.07*time));
    vec2 b = vec2(n.r, n.g);
    
    float d = dot(b, a);
    
    fragColor = texture(fons, vec2(vtexCoord.s + d, vtexCoord.t + d));
}
