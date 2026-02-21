#version 330 core

layout (location = 0) in vec3 vertex;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec3 color;
layout (location = 3) in vec2 texCoord;

out vec4 frontColor;
out vec2 vtexCoord;

uniform mat4 modelViewProjectionMatrix;
uniform mat3 normalMatrix;

uniform float time;


void main()
{
    vec3 N = normalize(normalMatrix * normal);
    
    float A = (vertex.y-0.5)*sin(time);
    if(vertex.y < 0.5)A = 0;
    frontColor = vec4(color,1.0);
    vtexCoord = texCoord;
    mat3 rotate_X = mat3(	vec3(1, 0, 0),
    				vec3(0, cos(A), sin(A)), 
    				vec3(0, -sin(A), cos(A)));
    vec3 aux = vertex;
    aux = aux - vec3(0, 1, 0);
    aux = rotate_X*aux;
    aux = aux + vec3(0, 1, 0);
    gl_Position = modelViewProjectionMatrix * vec4(aux, 1.0);
}
