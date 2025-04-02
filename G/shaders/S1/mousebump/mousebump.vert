#version 330 core

layout (location = 0) in vec3 vertex;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec3 color;
layout (location = 3) in vec2 texCoord;

out vec4 frontColor;
out vec2 vtexCoord;

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

uniform int test = 0;
uniform float radius = 300;

vec2 getMousePositionWindowSpace() {
    if(test == 0) return mousePosition;
    if(test == 1) return vec2(400,520);
    if(test == 2) return vec2(600,225);
    if(test == 3) return vec2(200,375);
    return vec2(400,300);
}



void main()
{
    vec3 N = normalize(normalMatrix * normal);
    
    vtexCoord = texCoord;
    vec3 P = (modelViewMatrix * vec4(vertex, 1.0)).xyz;
    
    float diagonal = distance(boundingBoxMin, boundingBoxMax);
    
    vec3 P2 = P + N*0.03*diagonal;
    
    vec4 window_P4 = modelViewProjectionMatrix * vec4(vertex, 1.0);
    
    
    vec2 Pos_pixel = vec2(window_P4.x/window_P4.w, window_P4.y/window_P4.w);		//Al hacer division de perspectiva queda entre [-1,1] y para multipilacr por el wiport necesitamos [0, 1]
    Pos_pixel += 1;
    Pos_pixel /= 2;
    
    float d = distance(Pos_pixel * viewport, getMousePositionWindowSpace());
    
    float t = smoothstep(0.8*radius, 0.05*radius, d);
    //t = 1-t;
    
    vec3 aux = mix(P, P2, t);
    frontColor = mix(vec4(1), vec4(1, 0, 0, 1), t) * N.z;
    gl_Position =  projectionMatrix * vec4(aux, 1.0);
}
