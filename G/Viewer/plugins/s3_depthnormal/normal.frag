#version 330 core

in vec3 N;
out vec4 fragColor;

void main() {
    vec3 color = N + 1;
    color = color / 2.;
    fragColor = vec4(color, 1.0);
}