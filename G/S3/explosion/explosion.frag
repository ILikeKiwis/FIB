#version 330 core

in vec4 frontColor;
out vec4 fragColor;

in vec2 vtexCoord;

float slice = 1.0/30.0;

uniform float time;
uniform sampler2D explosion;

void main()
{ 
    float frame = floor(time/slice);
    int f = int(frame);
    frame = f % 48;
    float i = frame/8.0;
    float j = frame - 8.0*i;
    vec2 aux = vec2(vtexCoord.x*1.0/8.0, vtexCoord.y*1.0/6.0);
    aux.x += j/8.0;
    aux.y += i/6.0;
    vec4 color = texture (explosion, aux);
    fragColor = color.a * color;
}
