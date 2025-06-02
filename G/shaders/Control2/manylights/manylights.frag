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

uniform int NUM = 5;

uniform vec3 boundingBoxMin; // cantonada minima de la capsa englobant 
uniform vec3 boundingBoxMax; // cantonada maxima de la capsa englobant

uniform mat4 modelViewMatrix;

uniform float decay = 6.0;


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
	
	vec3 Nn = normalize(N);
	vec3 Vn = normalize(V);
	vec4 res = vec4(0);
	int n_lights = (NUM+1);
	float x_min = boundingBoxMin.x;
	float y_min = boundingBoxMin.y;
	float z_min = boundingBoxMin.z;
	float x_delta = (boundingBoxMax.x - x_min) / NUM;
	float y_delta = (boundingBoxMax.y - y_min) / NUM;
	float z_delta = (boundingBoxMax.z - z_min) / NUM;
	for (int i = 0; i < n_lights; i++) {
		for(int j = 0; j < n_lights; j++) {
			for(int k = 0; k < n_lights; k++) {
				vec4 pos = modelViewMatrix * vec4(x_min + i*x_delta, y_min + j*y_delta, z_min + k*z_delta, 1.0);
				vec3 L = normalize(pos.xyz - P);
				float factor = exp(-decay*distance(pos.xyz, P));
				
				res += Phong(Nn, L, Vn)*factor;
			}
		}
	}
    fragColor = res;
}
