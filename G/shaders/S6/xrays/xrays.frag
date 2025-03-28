#version 330 core

in vec2 vtexCoord;
out vec4 fragColor;
in vec4 frontColor;	


uniform sampler2D foot0;
uniform sampler2D foot1;
uniform sampler2D foot2;
uniform sampler2D foot3;

in vec3 P;


const float R = 80.0;

uniform int layer = 1;

uniform vec2 mousePosition;
uniform bool virtualMouse = false;
uniform float mouseX, mouseY; 
uniform vec2 viewport; 

vec2 mouse()
{
	if (virtualMouse) return vec2(mouseX, mouseY);
	else return mousePosition;
}

void main()
{
	
	// a completar. Recorda usar mouse() per obtenir les coords del mouse, en window space
	vec4 TEXS[4] = vec4[4](texture(foot0, vtexCoord), texture(foot1, vtexCoord), texture(foot2, vtexCoord), texture(foot3, vtexCoord));
	vec2 Pos_frag = gl_FragCoord.xy;
	float d = distance(Pos_frag, mouse());
	
	if (d >= R) fragColor = TEXS[0];
	else fragColor = mix(TEXS[layer], TEXS[0], d/R);
	
}
