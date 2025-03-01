#version 330 core

in vec4 frontColor;
out vec4 fragColor;

in vec2 vtexCoord;

uniform sampler2D colorMap;

in vec3 N;
in vec3 L;
in vec3 R;
in vec3 V;

uniform float time = 7.1;

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
	
	int frame = int(floor(time/2.0));
	float t = (2.0-frame%3) / 3.0;
	float s = (frame/3.0) / 4.0;
	
	vec2 texCoord = vec2(vtexCoord.x * 1.0/4.0 + s, vtexCoord.y * 1.0/3.0 + t);
	
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
    
    fragColor = Difus(N, L) + Especular(N, L, R, V);
}
