#version 330 core

in vec4 frontColor;
out vec4 fragColor;

uniform int n = 2;

void main()
{
    int aux = int(gl_FragCoord.y);
    if (aux % n != 0) discard;
    fragColor = frontColor;
}
