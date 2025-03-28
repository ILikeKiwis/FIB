#version 330 core
        
layout(triangles) in;
layout(triangle_strip, max_vertices = 36) out;

in vec4 vfrontColor[];
out vec4 gfrontColor;

uniform float step = 0.5;

void pintacub (vec3 c) {
	
}

void main( void )
{
	float x_bari = (gl_in[0].gl_Position.x + gl_in[1].gl_Position.x + gl_in[2].gl_Position.x)/3;
	float y_bari = (gl_in[0].gl_Position.y + gl_in[1].gl_Position.y + gl_in[2].gl_Position.y)/3;
	float z_bari = (gl_in[0].gl_Position.z + gl_in[1].gl_Position.z + gl_in[2].gl_Position.z)/3;
	
	vec3 bari = vec3(x_bari, y_bari, z_bari);
	
	if (mod(x_bari, step) == 0 && mod(y_bari, step) == 0 && mod(z_bari, step) == 0) {
		pintacub(bari);
	}
	
	for( int i = 0 ; i < 3 ; i++ )
	{
		gfrontColor = vfrontColor[i];
		gl_Position = gl_in[i].gl_Position;
		EmitVertex();
	}
    EndPrimitive();
}
