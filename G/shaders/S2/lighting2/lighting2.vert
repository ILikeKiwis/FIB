#version 330 core

layout (location = 0) in vec3 vertex;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec3 color;
layout (location = 3) in vec2 texCoord;

out vec4 frontColor;
out vec2 vtexCoord;

uniform mat4 modelViewProjectionMatrix;
uniform mat3 normalMatrix;
uniform mat4 modelViewMatrix;

uniform vec4 lightAmbient;
uniform vec4 lightDiffuse;
uniform vec4 lightSpecular;
uniform vec4 lightPosition; 
uniform vec4 matAmbient;
uniform vec4 matDiffuse;
uniform vec4 matSpecular;
uniform float matShininess;

vec4 Ambient(){
	return matAmbient * lightAmbient;
}

vec4 Difus(vec3 N, vec3 L){
	return matDiffuse * lightDiffuse * max(0.0, dot(N,L));
}
vec4 Especular(vec3 R, vec3 V, vec3 N, vec3 L) {
	float aux = 0;
	if (max(0.0, dot(N,L)) > 0) aux = pow(max(0.0, dot(R,V)), matShininess);
	return matSpecular * lightSpecular * aux;
}

vec4 Phong(vec3 N, vec3 L, vec3 R, vec3 V) {
	return Ambient() + Difus(N, L) + Especular(R, V, N, L);
}

void main()
{

    vec3 N = normalize(normalMatrix * normal);
    vec3 P = (modelViewMatrix * vec4(vertex, 1)).xyz;
    vec3 L = normalize(lightPosition.xyz - P);
    vec3 V = normalize(-P);
    vec3 R = normalize( 2.0*dot(N,L)* N-L);
    
    frontColor = Phong(N, L, R, V);
    vtexCoord = texCoord;
    gl_Position = modelViewProjectionMatrix * vec4(vertex, 1.0);
}
