#version 330 core

layout (location = 0) in vec3 coords;

uniform mat4 modelViewProjectionMatrix;
uniform vec3 translate, scale;
void main () {
    gl_Position = modelViewProjectionMatrix * vec4((coords * scale) + translate, 1.0);
}