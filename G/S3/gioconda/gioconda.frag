#version 330 core

in vec4 frontColor;
out vec4 fragColor;

in vec2 vtexCoord;

uniform sampler2D sampler;

uniform float time;

bool obert = true;

float s_ull = 0.393;
float t_ull = 0.652;

vec2 c_ull = vec2(s_ull, t_ull);

float r = 0.025;



void main()
{
    vec2 texCoord = vtexCoord;
    obert = fract(time)<= 0.5;
    if (!obert) {
    	if ( distance(vtexCoord, c_ull) <= r) {
    		texCoord.x += 0.057;
    		texCoord.y -= 0.172;
    	}
    }
    fragColor = texture(sampler, texCoord);
}
