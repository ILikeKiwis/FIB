#version 330 core

layout (location = 0) in vec3 vertex;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec3 color;
layout (location = 3) in vec2 texCoord;

out vec4 frontColor;
out vec2 vtexCoord;

uniform mat4 modelViewProjectionMatrix;
uniform mat3 normalMatrix;

vec4 RED = vec4(1, 0, 0, 1);
vec4 YELLOW = vec4(1, 1, 0, 1);
vec4 GREEN = vec4(0, 1, 0, 1);
vec4 CIAN = vec4(0, 1, 1, 1);
vec4 BLUE = vec4(0, 0, 1, 1);


void main()
{	
    vec3 N = normalize(normalMatrix * normal);
    vec4 pos = modelViewProjectionMatrix * vec4(vertex, 1.0);
    float y = pos.y/pos.w;
    y = (y+1)*2;
    if (y<1) frontColor = mix(RED, YELLOW, y);
    else if (y<2) frontColor = mix(YELLOW, GREEN, y-1);
    else if (y<3) frontColor = mix(GREEN, CIAN, y-2);
    else  if (y<=4) frontColor = mix (CIAN, BLUE, y-3);
    vtexCoord = texCoord;
    gl_Position = modelViewProjectionMatrix * vec4(vertex, 1.0);
}
