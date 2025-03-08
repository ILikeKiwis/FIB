#version 330 core

in vec4 frontColor;
out vec4 fragColor;

in vec2 vtexCoord;

vec4 BLACK = vec4 (0,0,0,1);

vec4 ORANGE = vec4 (0.75,0.5,0,1);

vec4 GREY = vec4(0.2,0.2,0.2,1);

vec2 C = vec2(0.5, 0.5);

vec2 peduncle = vec2 (0.5, 0.75);

vec2 ull1 = vec2(0.4, 0.6);
vec2 ull2 = vec2(0.6, 0.6);

vec2 b_grey = vec2 (0.5, 0.55);
vec2 b_org = vec2 (0.5, 0.5);

void main()
{
    float d = distance(C, vtexCoord);	
    float ss = smoothstep(0.25,0.5,d);
    ss = 1 - ss;
    fragColor = ORANGE * ss;
    
    float d_car = distance (C, vtexCoord);
    if (d_car < 0.3) fragColor = GREY;
    
    if (abs(vtexCoord.x - peduncle.x) < 0.025 && abs(vtexCoord.y - peduncle.y) < 0.15) fragColor = GREY;
    
    
    float d_b_grey = distance(b_grey, vtexCoord);
    float d_b_org = distance(b_org, vtexCoord);
    
    if (d_b_org < 0.2) fragColor = ORANGE;
    if (d_b_grey < 0.2) fragColor = GREY;
    
    
    float d_ull1 = distance(ull1, vtexCoord);
    float d_ull2 = distance(ull2, vtexCoord);
    
    if (d_ull1 < 0.075 || d_ull2 < 0.075) fragColor = ORANGE; 
}
