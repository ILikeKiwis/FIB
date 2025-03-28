#version 330 core

in vec4 frontColor;
out vec4 fragColor;

in vec2 vtexCoord;

float slice = 1.0/30.0;

uniform float time;
uniform sampler2D explosion;

void main()
{ 
    fragColor = vec4(1);
    int frame = int(floor(time/slice));
    frame = frame % 48; // 0-47
    int i = 5 - frame/8; // offset de 7 a 0
    int j = frame%8; 	
    float t = i/6.0;
    float s = j/8.0;
    vec2 aux = vec2( vtexCoord.x * 1.0/8.0 + s, vtexCoord.y * 1.0/6.0 + t); 
    vec4 color = texture (explosion, aux);
    fragColor = color.a * color;
}
