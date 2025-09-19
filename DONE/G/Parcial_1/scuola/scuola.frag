#version 330 core

in vec4 frontColor;
out vec4 fragColor;
in vec2 vtexCoord;
in vec3 P;

uniform int mode = 0;
uniform float R = 2;
uniform float time;
uniform sampler2D colorMap, depthMap1, normalMap2;

const float PI = 3.141592;
const vec3 golden = vec3(1.0, 0.84, 0.0);
const float shininess = 5.0;
uniform float AO = 1.5;

uniform mat4 modelViewMatrix;



void main()
{
    float a = time*2.0*PI;			// ANGLE (una rotació son 2pi graus per tant temps*2pi)
    mat3 rotate_Z = mat3(	vec3(cos(a), sin(a), 0),	//MATRIU ROTACIO Z
    				vec3(-sin(a), cos(a), 0),
    				vec3(0, 0, 1));
    vec4 og = texture(colorMap, vtexCoord);		// COLOR BASE
    vec4 d = texture(depthMap1, vtexCoord);		// DEPTH
    vec4 f1 = min((1.-d)*AO, 1.);			// F1
    vec4 n = texture(normalMap2, vtexCoord);		// NORMAL
    n *= 2;
    n += -1;
    vec3 L_pos = vec3(R,0.,1.);			// POS INI LIGHT
    L_pos = rotate_Z * L_pos;
    vec3 L = normalize(L_pos - P);			// VECTOR L
    float NdotL = max(0.0, dot(n.xyz, L));		// F2
    
    if (mode == 0) fragColor = og;
    else if (mode == 1) {
    	fragColor = og * f1;
    }
    else if (mode == 2) {
    	
    	fragColor = og * NdotL;
    }
    else {
    	fragColor = og * f1 *NdotL ;
    }
}
