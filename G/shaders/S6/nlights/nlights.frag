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

in vec3 N, P;
vec3 V = normalize(-P);
vec3 pos = vec4(10, 0, 0, 1).xyz;

uniform int n = 2;
const float pi = 3.141592;

mat4 rotate (float a) {
	return mat4(	vec4(cos(a), sin(a), 0., 0.), 
			vec4(-sin(a), cos(a), 0., 0.),
			vec4(0., 0., 1.0, 0.),
			vec4(0., 0., 0., 1.));
}


void main()
{
    vec4 res = vec4(0);
    for (int i = 0; i < n; i++) {
    	float ang = (2.0*pi)/(n);
    	ang *= i;
    	vec3 aux = (rotate(ang) * vec4(pos, 1.0)).xyz;
    	
    	vec3 L = normalize(aux - P);
    	float NdotL = max(0.0, dot(N,L));
    	
    	vec3 R = normalize(2.0*NdotL*N-L);
    	
    	float shine = 0;
    	if (NdotL > 0) shine = pow(max(0.0, dot(R,V)), matShininess);
    	
    	res += ((matDiffuse * lightDiffuse * NdotL)/sqrt(n)) + (matSpecular * lightSpecular * shine);
    }
    fragColor = res;
}
