#version 330 core

in vec3 vertex;
in vec3 normal;

uniform mat4 modelViewProjectionMatrix;

void main() {
    gl_Position = modelViewProjectionMatrix * vec4(vertex, 1.0);
}