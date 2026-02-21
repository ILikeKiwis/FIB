#version 330 core

in vec4 frontColor;
out vec4 fragColor;

in vec2 P;

uniform int mode = 1;

uniform vec2 p1 = vec2 (-3, -8);
uniform vec2 p2 = vec2 ( 3, -8);
uniform vec2 p3 = vec2 (-2, 2);
uniform vec2 p4 = vec2 (2, 2);

uniform sampler2D courtMap;
uniform sampler2D player1;

in vec2 vtexCoord;

vec4 WHITE = vec4(1);
vec4 BLACK = vec4(0,0,0,1);

void main()
{
    vec4 color = texture(courtMap, vtexCoord);
    vec2 ps [4] = vec2[] (
    	p1,
    	p2,
    	p3,
    	p4
    );
    if (mode > 0){
    	if (fract(P.x) < 0.05 || fract(P.y) < 0.05) color = vec4(color.rgb * 1.2, color.a);
    	if (mode == 2){
    		float d_p[4];
    		d_p[0] = distance(P, p1);
    		d_p[1] = distance(P, p2);
    		d_p[2] = distance(P, p3);
    		d_p[3] = distance(P, p4);
    		for (int i = 0; i < 4; i++) {
    			if (d_p [i] < 0.4) color = WHITE;
    			if (d_p [i] > 0.4 && d_p [i] < 0.5) color = BLACK;
    		}
    	}
    	if (mode == 3) {
    		for(int i = 0; i<4; i++) {
    			if (abs(P.x - ps[i].x) < 1 && abs(P.y - ps[i].y) < 1) {
    				float s = P.x - ps[i].x-1;
    				float t = P.y - ps[i].y-1;
    				if (P.y > 0) t = -t;
    				vec4 aux_color = texture(player1, vec2(s/2,t/2));
    				if (aux_color.r > 0.5 || aux_color.b < 0.5) color = aux_color;
    			}
    		}
    	}
    }	
    fragColor = color;
} 
