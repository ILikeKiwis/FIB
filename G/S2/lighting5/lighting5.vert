#version 330 core

layout (location = 0) in vec3 vertex;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec3 color;
layout (location = 3) in vec2 texCoord;

uniform bool world;

out vec4 frontColor;
out vec2 vtexCoord;

out vec3 eN;
out vec3 eV;
out vec3 eL;

out vec3 wN;
out vec3 wV;
out vec3 wL;


uniform mat4 modelViewProjectionMatrix;
uniform mat3 normalMatrix;
uniform mat4 modelViewMatrix;
uniform mat4 modelViewMatrixInverse;

uniform vec4 lightAmbient;
uniform vec4 lightDiffuse;
uniform vec4 lightSpecular;
uniform vec4 lightPosition; 
uniform vec4 matAmbient;
uniform vec4 matDiffuse;
uniform vec4 matSpecular;
uniform float matShininess;

void main()
{
    eN = normalize(normalMatrix * normal);
    vec3 P = normalize(modelViewMatrix * vec4(vertex, 1)).xyz;
    eV = -P;
    eL = lightPosition.xyz - P;
    wN = normal;
    wV = (modelViewMatrixInverse*vec4(0,0,0,1)).xyz - vertex;
    wL = (modelViewMatrixInverse*lightPosition).xyz - vertex;
    
  
    gl_Position = modelViewProjectionMatrix * vec4(vertex, 1.0);
}
