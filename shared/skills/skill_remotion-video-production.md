# SKILL — REMOTION VIDEO PRODUCTION
**Load when: producing programmatic video content, animating data visualizations, building scripted video assets for D.C.E or D.S.E.**
**Loadable by: D.C.E (primary), D.S.E — content production and brand transmission.**

---

## WHAT THIS SKILL IS

Remotion converts React components into rendered video. Write JSX, use CSS/Canvas/SVG/WebGL, pass props — the output is an MP4. Every variable, function, API call, and algorithm available in JavaScript is available as a production tool. This is the sovereign video production layer: code is the script, React is the camera, and the render is the final cut.

**Source repo:** `~/Desktop/pandorareposkills/remotion/`
**License:** Special — company license required for commercial production. Verify before deployment.

---

## CORE ARCHITECTURE

```
COMPOSITION
  The root container. Defines: width, height, fps, durationInFrames.
  One composition = one video output.

SEQUENCE
  A time slice inside a composition.
  Defines when a component appears and for how long.
  Sequences can be nested.

COMPONENT
  A React component that receives a `frame` prop.
  `frame` is the current frame number — use it to animate.
  Every rendered frame is a function of `frame`.

TIMELINE
  frame 0 → frame N = the video duration
  All animation is derived from frame position, not time-based state
```

**The core principle:** A Remotion video is a pure function. `f(frame) → visual`. Same frame = same output, every time. This makes it deterministic, testable, and version-controllable.

---

## PROJECT SETUP

```bash
# Create a new Remotion project
npx create-video@latest

# Navigate into the project
cd my-video

# Install dependencies
npm install

# Start the Remotion Studio (visual editor + preview)
npx remotion studio

# Render to MP4
npx remotion render src/index.ts MyComposition out/video.mp4
```

---

## COMPONENT ANATOMY

```tsx
import { AbsoluteFill, useCurrentFrame, interpolate } from "remotion";

export const MyScene: React.FC = () => {
  const frame = useCurrentFrame();

  // interpolate maps frame range to value range
  const opacity = interpolate(frame, [0, 30], [0, 1], {
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill style={{ backgroundColor: "#000" }}>
      <div style={{ opacity, color: "#fff", fontSize: 48 }}>
        Frame {frame}
      </div>
    </AbsoluteFill>
  );
};
```

**Key hooks:**
- `useCurrentFrame()` — returns current frame number
- `useVideoConfig()` — returns fps, width, height, durationInFrames
- `interpolate(frame, inputRange, outputRange, options)` — map frame to any value
- `spring({ frame, fps, config })` — physics-based spring animation

---

## SEQUENCE AND TIMING

```tsx
import { Sequence, AbsoluteFill } from "remotion";

export const MyComposition: React.FC = () => (
  <AbsoluteFill>
    {/* Scene 1: appears at frame 0, runs for 60 frames */}
    <Sequence from={0} durationInFrames={60}>
      <SceneOne />
    </Sequence>

    {/* Scene 2: appears at frame 60, runs to end */}
    <Sequence from={60}>
      <SceneTwo />
    </Sequence>

    {/* Overlay: appears at frame 30, runs for 120 frames */}
    <Sequence from={30} durationInFrames={120}>
      <OverlayComponent />
    </Sequence>
  </AbsoluteFill>
);
```

---

## COMPOSITION REGISTRATION

```tsx
// src/Root.tsx
import { Composition } from "remotion";
import { MyComposition } from "./MyComposition";

export const RemotionRoot: React.FC = () => (
  <>
    <Composition
      id="MyVideo"
      component={MyComposition}
      durationInFrames={300}    // 10 seconds at 30fps
      fps={30}
      width={1920}
      height={1080}
    />
  </>
);
```

---

## RENDER PIPELINE

```bash
# Render a specific composition
npx remotion render src/index.ts MyVideo output/video.mp4

# Render with specific frame range (for testing)
npx remotion render src/index.ts MyVideo output/test.mp4 --frames=0-60

# Render as image sequence (for post-processing)
npx remotion render src/index.ts MyVideo output/frames/ --sequence

# Render in parallel (faster on multi-core)
npx remotion render src/index.ts MyVideo output/video.mp4 --concurrency=4
```

---

## D.C.E PANDORA APPLICATIONS

| D.C.E Use Case | Remotion Approach |
|----------------|-------------------|
| Kinetic text scripts | Component per line, Sequence timing, spring animation |
| Data visualization | SVG paths driven by interpolate() over frame |
| YouTube intro/outro | Short composition, brand colors, motion logo |
| Social media clips | 1080x1080 or 9:16 composition, punchy timing |
| Slide deck export | One Sequence per slide, static frames as keyframes |

**Sovereign content production principle:** The script is the code. Variables are the content slots. Build once, render infinitely with different props. Data-driven content at scale.

---

## PROPS-DRIVEN CONTENT (SCALE PATTERN)

```tsx
type Props = {
  title: string;
  subtitle: string;
  accentColor: string;
};

export const ContentCard: React.FC<Props> = ({ title, subtitle, accentColor }) => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [0, 20], [0, 1]);

  return (
    <AbsoluteFill style={{ backgroundColor: accentColor, opacity }}>
      <h1>{title}</h1>
      <p>{subtitle}</p>
    </AbsoluteFill>
  );
};

// Register with default props
<Composition
  id="ContentCard"
  component={ContentCard}
  defaultProps={{ title: "Default", subtitle: "Default", accentColor: "#000" }}
  durationInFrames={90}
  fps={30}
  width={1080}
  height={1080}
/>
```

Pass props at render time via `--props='{"title":"Sovereign OS"}'` — one composition template, unlimited unique outputs.

---

*SKILL_REMOTION_VIDEO_PRODUCTION | Pandora OS | D.C.E primary, D.S.E*
*"The script is the code. The render is the transmission."*
