#version 330 core
        
layout(triangles) in;
layout(triangle_strip, max_vertices = 36) out;

in vec4 vfrontColor[];
out vec4 gfrontColor;

in vec3 vN[];

uniform float time; 
const float speed = 0.5;

uniform mat4 modelViewProjectionMatrix;

void main( void )
{
	vec3 N = (vN[0] + vN[1]+ vN[2])/3;
	for( int i = 0 ; i < 3 ; i++ )
	{
		gfrontColor = vfrontColor[i];
		vec3 trans = speed * time * N;
		gl_Position = modelViewProjectionMatrix * vec4(gl_in[i].gl_Position.xyz + trans, gl_in[i].gl_Position.w);
		EmitVertex();
	}
    EndPrimitive();
}
