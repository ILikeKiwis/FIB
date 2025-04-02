#version 330 core

in vec4 frontColor;
out vec4 fragColor;

in vec2 vtexCoord;

uniform float time;
uniform sampler2D fbm;
const float pi = 3.14159;

vec4 RED = vec4 (1., 0., 0., 1.);
vec4 YELLOW = vec4 (1., 1., 0., 1.);
vec4 GREEN = vec4 (0., 1., 0., 1.);
vec4 CIAN = vec4 (0., 1., 1., 1.);
vec4 BLUE = vec4 (0., 0., 1., 1.);
vec4 MAGENTA = vec4 (1., 0., 1., 1.);

vec4 colors [7] = vec4 [7] (RED, YELLOW, GREEN, CIAN, BLUE, MAGENTA, RED);	// Creo que se puede quitar el ultimo red y que sean solo 6 elementos
 
void main()
{
    float r = (texture(fbm, vtexCoord)).r;
    float A = 1.0;
    float f = 0.1;
    float psi = 2.0*pi*r;
    float v = A * sin(2.0*pi*f*time + psi);
    v += 1;
    v *= 3.; 	// Passem v de [-1, 1] a [0, 6];
    fragColor = mix(colors[int(v)%6], colors[int(v+1)%6], fract(v)); 
    
}
