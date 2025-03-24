#version 330 core

in vec4 frontColor;
out vec4 fragColor;

in vec2 vtexCoord;

uniform sampler2D colormap;

vec2 CANO = vec2(3.0/4.0, 1.0/4.0);
vec2 ESCUT = vec2(3./4., 0.);
vec2 ALIEN_1 = vec2(0., 3./4.); 
vec2 ALIEN_2 = vec2(1./4., 3./4.);
vec2 ALIEN_3 = vec2(2./4., 3./4.);
vec2 ALIEN_4 = vec2(3./4., 3./4.);
vec2 ALIEN_5 = vec2(0., 2./4.);
vec2 ALIEN_6 = vec2(1./4., 2./4.);

vec2 TEXS[8] = vec2[8](CANO, ESCUT, ALIEN_1, ALIEN_2, ALIEN_3, ALIEN_4, ALIEN_5, ALIEN_6); 

void main()
{

    fragColor = vec4(0); 
    
    vec2 coord = vtexCoord * 8.;
    int col = int(coord.x);     // 0,7
    int fila = int(coord.y);	// 0,7   
    
    vec2 aux = fract(coord);
    aux *= 1./4.0;
   
    if (fila == 0) {
    	if (col == 4){
    		fragColor = texture (colormap, aux + TEXS[0]);
    	} 
    }
    else if (fila == 1) {
    	if (col % 2 == 0) {
    		fragColor = texture (colormap, aux + TEXS[1]);
    	}
    }
    else {
    	fragColor = texture(colormap, aux + TEXS[fila]);
    }
    
    
    
    
}
