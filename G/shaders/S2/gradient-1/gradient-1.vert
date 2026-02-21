#version 330 core

layout (location = 0) in vec3 vertex;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec3 color;
layout (location = 3) in vec2 texCoord;

out vec4 frontColor;
out vec2 vtexCoord;

uniform mat4 modelViewProjectionMatrix;
uniform mat3 normalMatrix;

uniform vec3 boundingBoxMin;
uniform vec3 boundingBoxMax;

float y_MAX = boundingBoxMax.y - boundingBoxMin.y;

vec3 RED = vec3(1,0,0);
vec3 YELLOW = vec3(1,1,0);
vec3 GREEN = vec3(0,1,0);
vec3 CIAN = vec3(0,1,1);
vec3 BLUE = vec3(0,0,1);


void main()
{
    
    vec3 N = normalize(normalMatrix * normal);
    float y = vertex.y - boundingBoxMin.y;
    float t = y / y_MAX;
    t = t*4;
    vec3 c;
    c = BLUE;
    if (t<1) c = mix(RED, YELLOW, t);
    else if (t<2) c = mix(YELLOW, GREEN, t-1);
    else if (t<3) c = mix(GREEN, CIAN, t-2);
    else if (t<=4) c = mix(CIAN, BLUE, t-3);
    frontColor = vec4(c, 1);
    vtexCoord = texCoord;
    gl_Position = modelViewProjectionMatrix * vec4(vertex, 1.0);
}
