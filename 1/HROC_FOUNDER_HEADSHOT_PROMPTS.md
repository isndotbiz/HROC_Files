# HROC FOUNDER HEADSHOT PROMPTS — GPT Image 1.5 Edit

**Purpose:** Generate uniform, photorealistic founder headshots for HROC website
**#1 Rule:** THE FACE MUST MATCH EXACTLY. Everything else is secondary.
**Method:** GPT Image 1.5 **edit** mode — each prompt uses the corresponding source image as input
**Output Size:** 1024x1024 (1:1 square)
**Quality:** `quality="low"` for cost control

---

## FACE IDENTITY LOCK (prepend to ALL prompts)

```
CRITICAL — FACE IDENTITY LOCK: The face in the output image MUST be pixel-level
identical to the face in the input image. Preserve every facial feature exactly:
eye shape, eye color, iris pattern, eyebrow shape, nose shape, nostril width, lip
shape, lip thickness, jawline, chin shape, cheekbone structure, forehead shape,
ear shape, skin tone, freckles, moles, blemishes, wrinkles, facial hair pattern,
smile lines, and overall facial geometry. The face must be recognizable as the
exact same person — not a similar-looking person, THE SAME person. If in doubt,
change NOTHING about the face. Treat the face region as a locked mask that cannot
be modified.
```

---

## UNIFORM STUDIO SETUP (same for ALL four founders)

```
Background: Seamless warm-neutral studio paper (#E8E0D8 to #D5CCC3 gradient),
softly lit by a large softbox at camera-left (45 degrees), white fill card at
camera-right. Background falls to smooth creamy bokeh, no hard edges or horizon line.

Lighting: Soft directional key light from camera-left, gentle modeling shadows
under cheekbone and jaw. Subtle specular highlights on nose bridge and cheekbones.
Fill ratio approximately 2:1. Natural 5200K white balance. Rectangular softbox
catchlights visible in both eyes.

Camera: Canon EOS R5, 85mm f/1.4L, ISO 200, shallow depth of field.
Shoulder-up framing, centered composition.
```

---

## REALISM & PROPORTIONS (same for ALL four founders)

```
Realism: Visible skin pore texture, natural under-eye shadows, micro fly-away hairs
along hairline, subtle skin color variation (no uniform color cast). No airbrushing,
no frequency separation, no beauty-filter smoothing, no plastic skin. Natural lip
color. The output must be indistinguishable from an unretouched DSLR photograph of
a real human being.

Body proportions: Anatomically correct human proportions — normal shoulder width
relative to head size, natural neck length, realistic collar bone and shoulder
positioning. No elongation, no compression, no uncanny distortion.

Hard constraints: No text, no logos, no watermarks. Do not alter the subject's
expression or pose. Do not change clothing or accessories.
```

---

## 1) ALICIA (input: `a1.png`)

```
[FACE IDENTITY LOCK]

[UNIFORM STUDIO SETUP]

Subject: This exact woman with straight dark-brown hair parted at center, wearing
a white sleeveless top. Her face, expression, head angle, and pose must remain
absolutely unchanged. Only the background and lighting quality may change.

[REALISM & PROPORTIONS]
```

---

## 2) BRI (input: `b1.png`)

```
[FACE IDENTITY LOCK]

[UNIFORM STUDIO SETUP]

Subject: This exact woman with wavy brown hair, wearing a white crew-neck t-shirt
and gold pendant necklace. Her face, expression, head angle, and pose must remain
absolutely unchanged. Only the background and lighting quality may change. Keep the
gold pendant necklace exactly as-is.

[REALISM & PROPORTIONS]
```

---

## 3) JONATHAN (input: `j1.png`)

```
[FACE IDENTITY LOCK]

[UNIFORM STUDIO SETUP]

Subject: This exact man with short reddish-brown hair, short beard stubble, blue
eyes, wearing a navy henley shirt and gold chain necklace. His face, facial hair,
expression, head angle, and pose must remain absolutely unchanged. Only the
background and lighting quality may change. Preserve the exact beard stubble
pattern and density.

[REALISM & PROPORTIONS]
```

---

## 4) LILLY (input: `l1.png`)

```
[FACE IDENTITY LOCK]

[UNIFORM STUDIO SETUP]

Subject: This exact woman with wavy dark-brown shoulder-length hair, green eyes,
wearing a black tank top, with a small dark mole below the collarbone. Her face,
expression, head angle, and pose must remain absolutely unchanged. Only the
background and lighting quality may change. Preserve the green eye color and iris
detail exactly.

[REALISM & PROPORTIONS]
```

---

## HOW TO RUN

```bash
cd D:\workspace\HROC_Files\1
pip install openai
export OPENAI_API_KEY="your-key-here"
python generate_headshots.py
```

Output will be saved to `D:\workspace\HROC_Files\1\output/`

---

## IF FACES DRIFT — TROUBLESHOOTING

### Face changed slightly
Append to prompt:
```
ABSOLUTE PRIORITY: Do not regenerate the face. The face pixels from the input image
must be transferred exactly. Only modify the area surrounding the face — background,
lighting on non-facial surfaces, and color grading. The face itself is untouchable.
```

### Skin looks too smooth / plastic
Append to prompt:
```
Increase visible skin micro-texture — pores on the nose and cheeks, fine peach fuzz
along the jawline lit by the softbox edge, and subtle redness variation around the
nose and inner cheeks. This must look like a real photograph, not a render.
```

### Body proportions are wrong
Append to prompt:
```
Anatomically correct proportions: Head-to-shoulder ratio approximately 1:2.5,
neck length proportional to head height, natural trapezius slope, realistic
clavicle positioning. No elongated neck, no oversized head, no narrow shoulders.
```

### Backgrounds don't match between founders
Use exact override for all four:
```
Background override: Exact hex #DDD5CC seamless paper, lit by a single large
Profoto B10 softbox at 45 degrees camera-left, 6 feet from subject. Background
is 8 feet behind subject, receiving approximately 2 stops less light, creating
natural falloff to #C4BBB0 at the edges.
```
