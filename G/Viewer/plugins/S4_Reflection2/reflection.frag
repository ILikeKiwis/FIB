#version 330 core

out vec4 fragColor;

in vec3 frontColor;

uniform sampler2D colorMap;
uniform sampler2D colorMap1;
uniform sampler2D colorMap2;

uniform int mirror;

uniform vec2 size;

void main() {
    if (mirror == 1) {
		vec2 st = (gl_FragCoord.xy - vec2(0.5)) / size;
		fragColor = vec4(0.5 * vec3(0.5), 1) + 0.5 * texture(colorMap, st);
	} else if (mirror == 2) {
		vec2 st = (gl_FragCoord.xy - vec2(0.5)) / size;
		fragColor = vec4(0.5 * vec3(0.5), 1) + 0.5 * texture(colorMap1, st);
		//fragColor = vec4(1, 1, 0, 1);
	} else if (mirror == 3) {
		vec2 st = (gl_FragCoord.xy - vec2(0.5)) / size;
		fragColor = vec4(0.5 * vec3(0.5), 1) + 0.5 * texture(colorMap2, st);
		//fragColor = vec4(1, 0, 0, 1);
	} else {
		fragColor = vec4(frontColor, 1);
	}

	/*switch (mirror) {
		case 0:
			fragColor = vec4(frontColor, 1);
			break;
		case 1:
			vec2 st = (gl_FragCoord.xy - vec2(0.5)) / size;
			fragColor = vec4(0.5 * vec3(0.5), 1) + 0.5 * texture(colorMap, st);
			break;
		case 2: 
			vec2 st = (gl_FragCoord.xy - vec2(0.5)) / size;
			fragColor = vec4(0.5 * vec3(0.5), 1) + 0.5 * texture(colorMap1, st);
			break;
		case 3:
			vec2 st = (gl_FragCoord.xy - vec2(0.5)) / size;
			fragColor = vec4(0.5 * vec3(0.5), 1) + 0.5 * texture(colorMap2, st);
			break;
		default:
			fragColor = vec4(1, 0, 0, 1);
	}*/
}

