#version 330 core

in vec4 frontColor;
out vec4 fragColor;

in vec2 vtexCoord;

uniform sampler2D colormap;

const float c = 16.;

const int GHOST = 0;
const int PACMAN = 1;
const int EMPTY = 2;
const int WALL = 3;
const int CORNER = 4;
const int POINT = 5;

float calc_offset (int f, int s){
	return (f-s)/6.0;
}

vec2 calc_texCoord(float s, float t, float offset) {
	return vec2 ((s*1.0/6.0)+offset, t);
}


void main()
{
    
    float s = vtexCoord.s * c;	// Dividmos el plano en c*c casillas
    float t = vtexCoord.t * c; 
   
    int s_int = int(s);		// Parte entera para ciertas decisiones
    int t_int = int(t);
    
    float offset;
    
    vec2 texCoord;
    if (s_int == 0) {
    	if (t_int == 0) {//Esquina 0.0
    		offset = calc_offset(CORNER, s_int);
    		texCoord = calc_texCoord(1-s, 1-t, offset);
    		fragColor = texture(colormap, texCoord); 
    	}
    	else if (t_int < 15) {//Paredes izquierda
    		offset = calc_offset(WALL, t_int);
    		fragColor = texture(colormap, vec2(t*1.0/6.0 +  offset, s));
    	}
    	else {
    		offset = calc_offset(CORNER, s_int);
    		texCoord = calc_texCoord(1-s, t, offset);
    		fragColor = texture(colormap, texCoord); 
    	}
    }
    else if (s_int == 15) {
    	if (t_int == 0) {
    		offset = calc_offset(CORNER, s_int);
    		texCoord = calc_texCoord(s, 1-t, offset);
    		fragColor = texture(colormap, texCoord);
    	}
    	else if (t_int < 15) {
    		offset = calc_offset(WALL, t_int);
    		fragColor = texture(colormap, vec2(t*1.0/6.0 +  offset, s));
    	}
    	else {
    		offset = calc_offset(CORNER, s_int);
    		texCoord = calc_texCoord(s, t, offset);
    		fragColor = texture(colormap, texCoord); 
    	}
    }
    else if (t_int == 0 || t_int == 15) {
    	offset = calc_offset(WALL, s_int);
    	texCoord = calc_texCoord(s, t, offset);
    	fragColor = texture(colormap, texCoord);
    }
    
    else if (t_int % 3 == 0 && s_int % 3 == 0) {
    	offset = calc_offset(WALL, s_int);
    	texCoord = calc_texCoord(s, t, offset);
    	fragColor = texture(colormap, texCoord);
    }
    
    else if (s_int == 2 && t_int == 2) {
    	offset = calc_offset(PACMAN, s_int);
    	texCoord = calc_texCoord(s, t, offset);
    	fragColor = texture(colormap, texCoord);
    }
    else if (s_int == 3 && t_int == 2) {
    	offset = calc_offset(GHOST, s_int);
    	texCoord = calc_texCoord(s, t, offset);
    	fragColor = texture(colormap, texCoord);
    }
    else if (s_int == 7 && t_int == 4) {
    	offset = calc_offset(GHOST, s_int);
    	texCoord = calc_texCoord(s, t, offset);
    	fragColor = texture(colormap, texCoord);
    }
    else {
    	offset = calc_offset(POINT, s_int);
    	texCoord = calc_texCoord(s, t, offset);
    	fragColor = texture(colormap, texCoord);
    }
   
}
