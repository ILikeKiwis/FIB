#version 330 core
        
layout(triangles) in;
layout(triangle_strip, max_vertices = 36) out;

in vec4 vfrontColor[];
out vec4 gfrontColor;

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



void main( void )
{
	float y = boundingBoxMin.y;
	for( int i = 0 ; i < 3 ; i++ )
	{
		gfrontColor = vfrontColor[i];
		gl_Position = modelViewProjectionMatrix * gl_in[i].gl_Position;
		EmitVertex();
	}
    EndPrimitive();
    
    	for( int i = 0 ; i < 3 ; i++ )
	{
		gfrontColor = vec4(0);
		vec4 aux = vec4(gl_in[i].gl_Position.x, y, gl_in[i].gl_Position.z, gl_in[i].gl_Position.w);
		gl_Position = modelViewProjectionMatrix * aux;
		EmitVertex();
	}
    EndPrimitive();
    	if (gl_PrimitiveIDIn == 0) {
    		float r = distance(boundingBoxMin, boundingBoxMax);
    		r = r/2;
    		vec3 C = (boundingBoxMax + boundingBoxMin)/2;
    		float y_pla = boundingBoxMin.y - 0.01;
    		gfrontColor = vec4(0, 1, 1, 1);
    		gl_Position = modelViewProjectionMatrix * vec4(C.x - r, y_pla, C.z - r, 1);
    		EmitVertex();
    		gfrontColor = vec4(0, 1, 1, 1);
    		gl_Position = modelViewProjectionMatrix * vec4(C.x + r, y_pla, C.z - r, 1);
    		EmitVertex();
    		gfrontColor = vec4(0, 1, 1, 1);
    		gl_Position = modelViewProjectionMatrix * vec4(C.x - r, y_pla, C.z + r, 1);
    		EmitVertex();
    		gfrontColor = vec4(0, 1, 1, 1);
    		gl_Position = modelViewProjectionMatrix * vec4(C.x + r, y_pla, C.z + r, 1);
    		EmitVertex();
    	}
    	EndPrimitive();
}
