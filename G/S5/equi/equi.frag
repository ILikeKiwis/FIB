#version 330 core

in vec4 frontColor;
out vec4 fragColor;

uniform sampler2D panorama;

in vec4 P;

const float PI = 3.141592;

void main()
{
    float x, y, z;
    x = P.x;
    y = P.y;
    z = P.z;
    
    float psi = asin(y) ;
    float zeta = atan(z,x) ;
    
    float s, t;
    
    s = zeta / (2.0*PI);
    t = psi/PI + 0.5;
    
    vec2 exCoord = vec2(s,t);
	
    fragColor = texture(panorama, exCoord);
}
