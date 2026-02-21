#version 330 core

in vec4 frontColor;
out vec4 fragColor;

in vec2 vtexCoord;

uniform sampler2D colorMap;

in vec3 N;
uniform vec4 lightPosition;
in vec3 P;

uniform float time;

uniform vec4 lightSpecular;
uniform vec4 matSpecular;
uniform float matShininess;

vec4 Difus(vec3 N, vec3 L) {

	vec3 WHITE = vec3(0.0);
	vec3 GREY = vec3(0.8);
	
	float dot = max(0.0, dot(N,L));
	vec4 lightDiffuse;
	if (int(time) % 2 == 0) lightDiffuse = vec4(mix(0.0, 0.8, fract(time)));
	else lightDiffuse = vec4(mix(0.8, 0.0, fract(time)));
	
	float frame = floor(time/2.0);
	int f = int(frame);
	float t = (2-f%3) / 3.0; 
	float s = (f/3) / 4.0;
	
	vec2 texCoord = vec2(fract(vtexCoord.s)/4.0 + s, fract(vtexCoord.t)/3.0 + t);
	
	vec4 matDiff = texture(colorMap,  texCoord);
	
	return matDiff * lightDiffuse * dot;
}

vec4 Especular(vec3 N, vec3 L, vec3 R, vec3 V) {
	float aux = 0;
	if (dot(N,L) > 0) aux = pow(max(0.0, dot(R,V)), matShininess);
	return matSpecular * lightSpecular * aux;
}

void main()
{
    vec3 L = normalize(lightPosition.xyz - P);
    vec3 R = normalize(2.0* dot(N,L) * N - L);
    vec3 V = normalize(-P);
    fragColor = Difus(N, L) + Especular(N, L, R, V);
}
