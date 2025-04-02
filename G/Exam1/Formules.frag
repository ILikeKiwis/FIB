#version 330 core

in vec4 frontColor;
out vec4 fragColor;

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

//Phong

in vec3 L, N, R, V;

vec4 Ambient(){
	return matAmbient * lightAmbient;
}

vec4 Difus(vec3 L, vec3 N) {
	L = normalize(L);
	N = normalize(N);
	
	float NdotL = max(0.0, dot(N,L));
	
	return matDiffuse * lightDiffuse * NdotL;
}

vec4 Especular(vec3 L, vec3 N, vec3 V, vec3 R) {
	L = normalize(L);
	N = normalize(N);
	V = normalize(V);
	R = normalize(R);

	float NdotL = max(0.0, dot(N,L));
	float shine = 0;
	
	if (NdotL > 0) shine = pow(max(0.0, dot(R,V)), matShininess);
	
	return matSpecular * lightSpecular * shine;
} 

vec4 Phong(vec3 N, vec3 L, vec3 R, vec3 V) {
	return Ambient() + Difus(L, N) + Especular(L, N, V, R); 
}

void main()
{
    fragColor = Phong(N, L, R, V);
}
