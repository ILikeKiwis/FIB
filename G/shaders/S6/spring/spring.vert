#version 330 core

layout (location = 0) in vec3 vertex;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec3 color;
layout (location = 3) in vec2 texCoord;

out vec4 frontColor;
out vec2 vtexCoord;

uniform mat4 modelViewProjectionMatrix;
uniform mat3 normalMatrix;

uniform float time;

void main()
{
    vec3 N = normalize(normalMatrix * normal);
    frontColor = vec4( N.z);
    vtexCoord = texCoord;
    
    float t = mod(time, 3.5);
    vec3 v;
    float aux = pow(t/0.5, 3);
    if (t < 0.5) {
    	v = mix(vec3(0), vertex, aux);
    }
    if (t > 0.5) { 
    	float t_aux = t-0.5;
    	t_aux = t_aux / 3.;
    	v = mix(vertex, vec3(0), t_aux); 
    }
    
    
    gl_Position = modelViewProjectionMatrix * vec4(v, 1.0);
}
