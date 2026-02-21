#version 330 core

in vec4 frontColor;
out vec4 fragColor;

in vec2 vtexCoord;
in vec4 P_clip;

uniform sampler2D jungla;

uniform vec2 mousePosition;
uniform vec2 viewport;

uniform float magnific = 3.0;



vec4 blurImage( in vec2 coords )
{
    float Pi = 6.28318530718; // Pi*2
    float Directions = 16.0; // BLUR DIRECTIONS (Default 16.0 - More is better but slower)
    float Quality = 8.0; // BLUR QUALITY (Default 4.0 - More is better but slower)
    float Size = 10.0; // BLUR SIZE (Radius)
   
    vec2 Radius = Size/viewport;

    vec4 Color = texture(jungla, coords);
    for( float d=0.0; d<Pi; d+=Pi/Directions)
    {
        float cd = cos(d);
        float sd = sin(d);
		for(float i=1.0/Quality; i<=1.0; i+=1.0/Quality)
        {
			Color += texture(jungla, coords+vec2(cd,sd)*Radius*i);		
        }
    }
    
    // Output to screen
    Color /= Quality * Directions - 15.0;
    return  Color;
}


void main()
{
    vec2 Pos_pixel= vtexCoord * viewport;
    
    vec2 C_d = vec2(mousePosition.x - 80, mousePosition.y);
    vec2 C_e = vec2(mousePosition.x + 80, mousePosition.y);
    
    float dist_d = distance(Pos_pixel, C_d);
    float dist_e = distance(Pos_pixel, C_e);
    float dist_r = distance(Pos_pixel, mousePosition);
    
    vec2 P = mousePosition + (Pos_pixel-mousePosition)/magnific;
    P = P/viewport;
    
    
    fragColor = blurImage(vtexCoord);
    if ((dist_d < 105 && dist_d > 100) ||  (dist_e < 105 && dist_e > 100)) fragColor = vec4(0.0);
    if (dist_d < 100 || dist_e < 100 ) fragColor = texture(jungla, P);
    
    
    
}
