#version 330 core

in vec4 frontColor;
out vec4 fragColor;

uniform float time;

in float x;

void main()
{
    float aux = x;
    if(aux > time) discard;
    fragColor = vec4(0,0,1,1);
}
