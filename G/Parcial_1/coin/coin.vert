#version 330 core

layout (location = 0) in vec3 vertex;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec3 color;
layout (location = 3) in vec2 texCoord;

out vec4 frontColor;
out vec2 vtexCoord;

uniform mat4 modelViewProjectionMatrix;
uniform mat3 normalMatrix;
uniform mat4 modelViewMatrix;
out vec3 P, N, L;

uniform int mode = 1;
uniform float time;

const float PI = 3.141592;

void main()
{
    float time_3 = mod(time, 3.0);
    vec3 aux = vertex;
    
    N = normalize(normalMatrix * normal);
    frontColor = vec4(color,1.0) * N.z;
    if (mode == 1) {
    		float t = smoothstep(0., 1., time_3);
    		aux.y = aux.y + (0.5*cos(t));
    		float a = 2.0*(2.0*PI*t);
    		mat3 rotate_Y = mat3(	vec3(cos(a), 0, -sin(a)),
    					vec3(0,1,0),
    					vec3(sin(a), 0, cos(a)));
    		aux = rotate_Y * aux;	 
    }
    
    vtexCoord = texCoord;
    P = (modelViewMatrix * vec4(aux, 1.0)).xyz;
    vec3 P_L = (modelViewMatrix * vec4(aux + aux/abs(aux), 1.0)).xyz;
    L = normalize(P_L - P);
    gl_Position = modelViewProjectionMatrix * vec4(aux, 1.0);
}
