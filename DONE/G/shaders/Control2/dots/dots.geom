#version 330 core
        
layout(triangles) in;
layout(triangle_strip, max_vertices = 36) out;

in vec4 vfrontColor[];
in vec3 vN[];
out vec4 gfrontColor;
out vec4 P;
out vec4 C;

uniform bool culling = true;

uniform mat4 modelViewProjectionMatrix;

void main( void )
{
	vec4 c = (gl_in[0].gl_Position + gl_in[1].gl_Position + gl_in[2].gl_Position) / 3.0;
	bool back = (vN[0].z < 0) && (vN[1].z < 0) && (vN[2].z < 0);
	if (culling && back) {
	
	}
	else {
		for( int i = 0 ; i < 3 ; i++ )
		{
			gfrontColor = vfrontColor[i];
			gl_Position = modelViewProjectionMatrix * gl_in[i].gl_Position;
			P = gl_in[i].gl_Position;
			C = vec4(c.xyz, 1.0);
			EmitVertex();
		}
	    EndPrimitive();
	}
}
