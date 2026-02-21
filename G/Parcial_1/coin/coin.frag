#version 330 core

in vec4 frontColor;
out vec4 fragColor;
in vec2 vtexCoord;
in vec3 N, P, L;

const vec3 golden = vec3(1.0, 0.84, 0.0);
const float shininess = 5.0;

vec4 matAmbient = vec4(golden, 1.0);
vec4 matDiffuse = matAmbient;
vec4 matSpecular = vec4(1);
vec4 lightAmbient = vec4(0.2,0.2,0.2,1.0);
vec4 lightDiffuse = vec4(0.7,0.7,0.7, 1.0);
vec4 lightSpecular = vec4(1);

vec4 Ambient(){
	return matAmbient * lightAmbient;
}

vec4 Difus(vec3 L, vec3 N) {
	L = normalize(L);
	N = normalize(N);
	
	float NdotL = max(0.0, dot(N,L));
	
	return matDiffuse * lightDiffuse * NdotL;
}

vec4 Especular(vec3 L, vec3 N, vec3 V, vec3 R, float s) {
	L = normalize(L);
	N = normalize(N);
	V = normalize(V);
	R = normalize(R);

	float NdotL = max(0.0, dot(N,L));
	float shine = 0;
	
	if (NdotL > 0) shine = pow(max(0.0, dot(R,V)), s);
	
	return matSpecular * lightSpecular * shine;
} 

vec4 Phong(vec3 N, vec3 L, vec3 R, vec3 V, float s) {
	return Ambient() + Difus(L, N) + Especular(L, N, V, R, s); 
}


void main()
{
    vec3 V = -P;
    vec3 R = 2.0*dot(N,L)*N-L;
    float s = shininess;
    if (vtexCoord.s >= 0.5) s = s*0.5;
    vec4 light = Phong(N, L, R, V, s);
    fragColor = light;
}
