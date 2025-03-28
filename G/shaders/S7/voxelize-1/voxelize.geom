#version 330 core
        
layout(triangles) in;
layout(points, max_vertices = 36) out;

in vec4 vfrontColor[];
out vec4 gfrontColor;

uniform mat4 modelViewProjectionMatrix;

uniform float step = 2;

void pintacub (vec3 c) {
	gl_Position = modelViewProjectionMatrix * vec4(c, 1.0);
}

void main( void )
{
	float x_bari = (gl_in[0].gl_Position.x + gl_in[1].gl_Position.x + gl_in[2].gl_Position.x)/3;
	float y_bari = (gl_in[0].gl_Position.y + gl_in[1].gl_Position.y + gl_in[2].gl_Position.y)/3;
	float z_bari = (gl_in[0].gl_Position.z + gl_in[1].gl_Position.z + gl_in[2].gl_Position.z)/3;
	int x = int(x_bari);
	int y = int(y_bari);
	int z = int(z_bari);
	
	vec3 bari = vec3(x_bari, y_bari, z_bari);
	if (mod(step, x) == 0 && mod(y, step) == 0 && mod(z, step) == 0){
		gfrontColor = vfrontColor[0];
		gl_Position = modelViewProjectionMatrix*vec4(bari, 1.0);
		EmitVertex();
		EndPrimitive();
	}
	if (mod(x_bari, step) == 0 && mod(y_bari, step) == 0 && mod(z_bari, step) == 0) {
		pintacub(bari);
	}
	
	for( int i = 0 ; i < 3 ; i++ )
	{
		gfrontColor = vfrontColor[i];
		gl_Position = gl_in[i].gl_Position;
		//EmitVertex();
	}
    EndPrimitive();
}
