#version 330 core

in vec4 frontColor;
out vec4 fragColor;

uniform float time;

void main()
{
    float aux = gl_FragCoord.x+1;
    if(aux > time) discard;
    fragColor = vec4(0,0,1,1);
}
