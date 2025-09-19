#version 330 core 

in vec3 vertex;
in vec3 normal;
out vec3 N;

uniform mat3 normalMatrix;
uniform mat4 modelViewProjectionMatrix;

void main() {
    N = normalize(normalMatrix * normal);
    gl_Position = modelViewProjectionMatrix * vec4(vertex, 1.0);
}