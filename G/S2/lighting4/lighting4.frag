#version 330 core

in vec4 frontColor;
out vec4 fragColor;
in vec3 N;
in vec3 P;
in vec3 V;

uniform vec4 lightAmbient;
uniform vec4 lightDiffuse;
uniform vec4 lightSpecular;
uniform vec4 lightPosition; 
uniform vec4 matAmbient;
uniform vec4 matDiffuse;
uniform vec4 matSpecular;
uniform float matShininess;


vec4 Ambient() {
	return matAmbient * lightAmbient;
}

vec4 Difus(float NdotL) {
	
	return matDiffuse * lightDiffuse * NdotL;
}

vec4 Especular(float RdotV, float NdotL) {
	float shin = 0;
	if (NdotL > 0) shin = pow(RdotV, matShininess);
	return matSpecular * lightSpecular * shin;
}
vec4 Phong(vec3 N, vec3 L, vec3 V) {
	float NdotL = max(0.0, dot(N,L));
	vec3 R = normalize(2.0*NdotL*N-L);
	float RdotV = max(0.0, dot(R,V));
	return Ambient() + Difus(NdotL) + Especular (RdotV, NdotL);
}

void main()
{	
	vec3 L = lightPosition.xyz - P;
	L = normalize(L);
	vec3 Nn = normalize(N);
	vec3 Vn = normalize(V);
    fragColor = Phong(Nn, L, Vn);
}
