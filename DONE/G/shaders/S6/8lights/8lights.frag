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

vec3 L1 = boundingBoxMin;
vec3 L2 = boundingBoxMax;
vec3 L3 = vec3(boundingBoxMin.x, boundingBoxMin.y, boundingBoxMax.z);
vec3 L4 = vec3(boundingBoxMin.x, boundingBoxMax.y, boundingBoxMin.z);
vec3 L5 = vec3(boundingBoxMin.x, boundingBoxMax.y, boundingBoxMax.z);
vec3 L6 = vec3(boundingBoxMax.x, boundingBoxMin.y, boundingBoxMin.z);
vec3 L7 = vec3(boundingBoxMax.x, boundingBoxMin.y, boundingBoxMax.z);
vec3 L8 = vec3(boundingBoxMax.x, boundingBoxMax.y, boundingBoxMin.z);

vec3 Ls[8] = vec3[8](L1, L2, L3, L4, L5, L6, L7, L8);


void main()
{
    fragColor = vec4(0);
    // Passar eye space 
    for (int i = 0; i < 8; i++) {
    	Ls[i] = (modelViewMatrix * vec4(Ls[i], 1.0)).xyz;
    }
    
    vec3 V = normalize(-P);
    for (int i = 0; i < 8; i++) {
    	vec3 L = normalize(Ls[i] - P);
    	float NdotL = max(0.0, dot(N,L));
    	
    	vec3 R = normalize(2.0*NdotL*N-L);
    	
    	float shine = 0;
    	if (NdotL > 0) shine = pow(max(0.0, dot(R,V)), matShininess);
    	fragColor += (matDiffuse * lightDiffuse * NdotL)/2.0 + (matSpecular * lightSpecular * shine);
    }
}
