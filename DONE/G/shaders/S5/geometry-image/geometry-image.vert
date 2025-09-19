#version 330 core

layout (location = 0) in vec3 vertex;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec3 color;
layout (location = 3) in vec2 texCoord;

out vec4 frontColor;
out vec2 vtexCoord;



uniform sampler2D positionMap;
uniform sampler2D normalMap1;

uniform int mode = 1;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;
uniform mat4 modelViewMatrix;
uniform mat4 modelViewProjectionMatrix;

uniform mat4 modelMatrixInverse;
uniform mat4 viewMatrixInverse;
uniform mat4 projectionMatrixInverse;
uniform mat4 modelViewMatrixInverse;
uniform mat4 modelViewProjectionMatrixInverse;

uniform mat3 normalMatrix;

uniform vec4 lightAmbient;  // similar a gl_LightSource[0].ambient
uniform vec4 lightDiffuse;  // similar a gl_LightSource[0].diffuse
uniform vec4 lightSpecular; // similar a gl_LightSource[0].specular
uniform vec4 lightPosition; // similar a gl_LightSource[0].position; en eye space
uniform vec4 matAmbient;    // similar a gl_FrontMaterial.ambient 
uniform vec4 matDiffuse;    // similar a gl_FrontMaterial.diffuse 
uniform vec4 matSpecular;   // similar a gl_FrontMaterial.specular
uniform float matShininess; // similar a gl_FrontMaterial.shininess

uniform vec3 boundingBoxMin; // cantonada minima de la capsa englobant 
uniform vec3 boundingBoxMax; // cantonada maxima de la capsa englobant

uniform vec2 mousePosition;  // coordenades del cursor (window space; origen a la cantonada inferior esquerra)
uniform vec2 viewport;       // dimensions del viewport

int objectID;                // index of object in scene's array


vec4 Ambient() {
	return matAmbient * lightAmbient;
}

vec4 Difus(vec3 L, vec3 N, vec3 P, bool b){
	L = normalize(L);
	N = normalize(N);
	float d = max(0.0, dot(N,L));
	if (b) return vec4(P,0.0) * lightDiffuse * d;
	else return matDiffuse * lightDiffuse * d;
}

vec4 Difus_1(vec3 L, vec3 N){
	L = normalize(L);
	N = normalize(N);
	float d = max(0.0, dot(N,L));
	return matDiffuse * lightDiffuse * d;
}

vec4 Specular(vec3 R, vec3 V, vec3 N, vec3 L) {
	R = normalize(R);
	V = normalize(V);
	N = normalize(N);
	L = normalize(L);
	float s = 0;
	if (dot(N,L) > 0) s = pow(max(0.0,dot(R,V)), matShininess);
	return matSpecular * lightSpecular * s;
	 
}


void main()
{
    vtexCoord.s = (vertex.x + 1.0) / 2.0;
    vtexCoord.t = (vertex.y +1.0) / 2.0;
    vtexCoord *= 0.992;
    vtexCoord += 0.004;
    
    vec3 P = (texture(positionMap, vtexCoord)).xyz;
    
    
    vec3 normal_b = (texture(normalMap1, vtexCoord)).xyz;
    normal_b = normal_b * 2.0;
    normal_b = normal_b -1.0;
    
    vec3 N = normalize(normalMatrix*normal_b);
    frontColor = vec4(P,1.0);
    
    vec3 P_light = (modelViewMatrix * vec4(P, 1.0)).xyz;
    vec3 L = lightPosition.xyz - P_light;
    L = normalize(L);
    vec3 V = -P_light;
    
    vec3 R = normalize( 2.0*max(0.0,dot(N,L))*N-L );
    
    
    if (mode == 1) frontColor = vec4(P,1.0) * N.z;
    
    if (mode == 2) frontColor = Ambient() + Difus_1(L, N) + Specular(R, V, N, L);
    
    if (mode == 3) frontColor = Ambient() + Difus(L, N, P, true) + Specular(R, V, N, L);
    
    gl_Position = modelViewProjectionMatrix * vec4(P,1.0);
   
    
}
