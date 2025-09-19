#version 330 core
        
layout(triangles) in;
layout(triangle_strip, max_vertices = 36) out;

in vec4 vfrontColor[];
out vec4 gfrontColor;

uniform float size = 0.07;

uniform float depth = -0.01;

out vec2 st;

void main( void )
{
	vec4 C = vec4 (0);
	for( int i = 0 ; i < 3 ; i++ )
	{
		gfrontColor = vfrontColor[i];
		st = vec2(-1, -1);
		gl_Position = gl_in[i].gl_Position;
		EmitVertex();
	}
    	EndPrimitive();
    	
    	C = gl_in[0].gl_Position + gl_in[1].gl_Position + gl_in[2].gl_Position; 
    	C = C / 3.0;
   
    	
    	vec4 vxt[4];
    	vxt[0] = vec4(C.x - size, C.y - size, C.z + depth, C.w) / C.w;
    	vxt[1] = vec4(C.x - size, C.y + size, C.z + depth, C.w) / C.w;
    	vxt[2] = vec4(C.x + size, C.y - size, C.z + depth, C.w) / C.w;
    	vxt[3] = vec4(C.x + size, C.y + size, C.z + depth, C.w) / C.w;
    	
    	vec2 sts[4];
    	sts[0] = vec2 (0, 0);
    	sts[1] = vec2 (0, 7);
    	sts[2] = vec2 (7, 0);
    	sts[3] = vec2 (7, 7);
    	
    	for (int i = 0; i < 3; i++) {
    		gfrontColor = vec4(1., 1., 0., 1.);
    		st = sts[i];
    		gl_Position = vxt[i];
    		EmitVertex();
    	}
    	EndPrimitive();
    	
    	for (int i = 0; i < 3; i++) {
    		gfrontColor = vec4(1., 1., 0., 1.);
    		st = sts[i+1];
    		gl_Position = vxt[i+1];
    		EmitVertex();
    	}
    	EndPrimitive();

	
    			
    
}
