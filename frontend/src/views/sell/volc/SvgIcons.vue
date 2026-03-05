<script>
export default {
  name: 'VolcIcon',
  props: {
    name: { type: String, required: true },
    size: { type: [Number, String], default: 20 },
    color: { type: String, default: 'currentColor' }
  },
  computed: {
    iconSize() {
      return typeof this.size === 'number' ? this.size + 'px' : this.size
    }
  }
}
</script>

<template>
  <svg
    xmlns="http://www.w3.org/2000/svg"
    :width="iconSize"
    :height="iconSize"
    viewBox="0 0 24 24"
    fill="none"
    :stroke="color || '#000'"
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    style="flex-shrink: 0"
  >
    <!-- Arrow Right -->
    <template v-if="name === 'arrow-right'">
      <line x1="5" y1="12" x2="19" y2="12" />
      <polyline points="12 5 19 12 12 19" />
    </template>

    <!-- Sparkles -->
    <template v-if="name === 'sparkles'">
      <path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z" />
      <path d="M5 3v4" /><path d="M19 17v4" />
      <path d="M3 5h4" /><path d="M17 19h4" />
    </template>

    <!-- Zap -->
    <template v-if="name === 'zap'">
      <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2" />
    </template>

    <!-- Globe -->
    <template v-if="name === 'globe'">
      <circle cx="12" cy="12" r="10" />
      <line x1="2" y1="12" x2="22" y2="12" />
      <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" />
    </template>

    <!-- Shield -->
    <template v-if="name === 'shield'">
      <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
    </template>

    <!-- Brain -->
    <template v-if="name === 'brain'">
      <path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96.44 2.5 2.5 0 0 1-2.96-3.08 3 3 0 0 1-.34-5.58 2.5 2.5 0 0 1 1.32-4.24 2.5 2.5 0 0 1 1.98-3A2.5 2.5 0 0 1 9.5 2Z" />
      <path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96.44 2.5 2.5 0 0 0 2.96-3.08 3 3 0 0 0 .34-5.58 2.5 2.5 0 0 0-1.32-4.24 2.5 2.5 0 0 0-1.98-3A2.5 2.5 0 0 0 14.5 2Z" />
    </template>

    <!-- Video -->
    <template v-if="name === 'video'">
      <path d="m22 8-6 4 6 4V8Z" /><rect width="14" height="12" x="2" y="6" rx="2" ry="2" />
    </template>

    <!-- Eye -->
    <template v-if="name === 'eye'">
      <path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z" /><circle cx="12" cy="12" r="3" />
    </template>

    <!-- Mic -->
    <template v-if="name === 'mic'">
      <path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z" />
      <path d="M19 10v2a7 7 0 0 1-14 0v-2" /><line x1="12" y1="19" x2="12" y2="22" />
    </template>

    <!-- Image -->
    <template v-if="name === 'image'">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2" /><circle cx="9" cy="9" r="2" />
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21" />
    </template>

    <!-- AudioLines -->
    <template v-if="name === 'audio-lines'">
      <path d="M2 10v3" /><path d="M6 6v11" /><path d="M10 3v18" /><path d="M14 8v7" /><path d="M18 5v13" /><path d="M22 10v3" />
    </template>

    <!-- Server -->
    <template v-if="name === 'server'">
      <rect width="20" height="8" x="2" y="2" rx="2" ry="2" /><rect width="20" height="8" x="2" y="14" rx="2" ry="2" />
      <line x1="6" y1="6" x2="6.01" y2="6" /><line x1="6" y1="18" x2="6.01" y2="18" />
    </template>

    <!-- Container -->
    <template v-if="name === 'container'">
      <path d="M22 7.7c0-.6-.4-1.2-.8-1.5l-6.3-3.8a3.2 3.2 0 0 0-2.8-.1L2.8 6.2c-.5.3-.8.9-.8 1.5s.3 1.2.8 1.5l8.3 4.8c.9.5 2 .5 2.8 0l7.3-4.3c.4-.3.8-.9.8-1.5Z" />
      <path d="M2 17.5 9.5 22c.9.5 2 .5 2.8 0l8.7-5" />
      <path d="M2 12.5l7.5 4.5c.9.5 2 .5 2.8 0l8.7-5" />
    </template>

    <!-- Search -->
    <template v-if="name === 'search'">
      <circle cx="11" cy="11" r="8" /><line x1="21" y1="21" x2="16.65" y2="16.65" />
    </template>

    <!-- HardDrive -->
    <template v-if="name === 'hard-drive'">
      <line x1="22" y1="12" x2="2" y2="12" />
      <path d="M5.45 5.11 2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11z" />
      <line x1="6" y1="16" x2="6.01" y2="16" /><line x1="10" y1="16" x2="10.01" y2="16" />
    </template>

    <!-- Database -->
    <template v-if="name === 'database'">
      <ellipse cx="12" cy="5" rx="9" ry="3" /><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3" />
      <path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5" />
    </template>

    <!-- MemoryStick -->
    <template v-if="name === 'memory-stick'">
      <path d="M6 19v-3" /><path d="M10 19v-3" /><path d="M14 19v-3" /><path d="M18 19v-3" />
      <path d="M8 11V9" /><path d="M16 11V9" /><path d="M12 11V9" />
      <path d="M2 15h20" /><path d="M2 7a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V7Z" />
    </template>

    <!-- Bot -->
    <template v-if="name === 'bot'">
      <path d="M12 8V4H8" /><rect width="16" height="12" x="4" y="8" rx="2" />
      <path d="M2 14h2" /><path d="M20 14h2" /><path d="M15 13v2" /><path d="M9 13v2" />
    </template>

    <!-- Layers -->
    <template v-if="name === 'layers'">
      <polygon points="12 2 2 7 12 12 22 7 12 2" />
      <polyline points="2 17 12 22 22 17" /><polyline points="2 12 12 17 22 12" />
    </template>

    <!-- BookOpen -->
    <template v-if="name === 'book-open'">
      <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z" />
      <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z" />
    </template>

    <!-- Languages -->
    <template v-if="name === 'languages'">
      <path d="m5 8 6 6" /><path d="m4 14 6-6 2-3" /><path d="M2 5h12" /><path d="M7 2h1" />
      <path d="m22 22-5-10-5 10" /><path d="M14 18h6" />
    </template>

    <!-- MessageCircle -->
    <template v-if="name === 'message-circle'">
      <path d="m3 21 1.9-5.7a8.5 8.5 0 1 1 3.8 3.8z" />
    </template>

    <!-- Gamepad -->
    <template v-if="name === 'gamepad'">
      <line x1="6" y1="12" x2="10" y2="12" /><line x1="8" y1="10" x2="8" y2="14" />
      <line x1="15" y1="13" x2="15.01" y2="13" /><line x1="18" y1="11" x2="18.01" y2="11" />
      <rect width="20" height="12" x="2" y="6" rx="2" />
    </template>

    <!-- GraduationCap -->
    <template v-if="name === 'graduation-cap'">
      <path d="M22 10v6M2 10l10-5 10 5-10 5z" /><path d="M6 12v5c3 3 6 3 6 3s3 0 6-3v-5" />
    </template>

    <!-- Headphones -->
    <template v-if="name === 'headphones'">
      <path d="M3 18v-6a9 9 0 0 1 18 0v6" />
      <path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3zM3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z" />
    </template>

    <!-- TrendingUp -->
    <template v-if="name === 'trending-up'">
      <polyline points="22 7 13.5 15.5 8.5 10.5 2 17" /><polyline points="16 7 22 7 22 13" />
    </template>

    <!-- Car -->
    <template v-if="name === 'car'">
      <path d="M19 17h2c.6 0 1-.4 1-1v-3c0-.9-.7-1.7-1.5-1.9C18.7 10.6 16 10 16 10s-1.3-1.4-2.2-2.3c-.5-.4-1.1-.7-1.8-.7H5c-.6 0-1.1.4-1.4.9l-1.4 2.9A3.7 3.7 0 0 0 2 12v4c0 .6.4 1 1 1h2" />
      <circle cx="7" cy="17" r="2" /><path d="M9 17h6" /><circle cx="17" cy="17" r="2" />
    </template>

    <!-- Landmark -->
    <template v-if="name === 'landmark'">
      <line x1="3" y1="22" x2="21" y2="22" /><line x1="6" y1="18" x2="6" y2="11" />
      <line x1="10" y1="18" x2="10" y2="11" /><line x1="14" y1="18" x2="14" y2="11" />
      <line x1="18" y1="18" x2="18" y2="11" /><polygon points="12 2 20 7 4 7" />
    </template>

    <!-- Smartphone -->
    <template v-if="name === 'smartphone'">
      <rect width="14" height="20" x="5" y="2" rx="2" ry="2" /><line x1="12" y1="18" x2="12.01" y2="18" />
    </template>

    <!-- Flask -->
    <template v-if="name === 'flask'">
      <path d="M10 2v7.527a2 2 0 0 1-.211.896L4.72 20.55a1 1 0 0 0 .9 1.45h12.76a1 1 0 0 0 .9-1.45l-5.069-10.127A2 2 0 0 1 14 9.527V2" />
      <path d="M8.5 2h7" /><path d="M7 16.5h10" />
    </template>

    <!-- Pill -->
    <template v-if="name === 'pill'">
      <path d="m10.5 20.5 10-10a4.95 4.95 0 1 0-7-7l-10 10a4.95 4.95 0 1 0 7 7Z" />
      <path d="m8.5 8.5 7 7" />
    </template>

    <!-- Cpu -->
    <template v-if="name === 'cpu'">
      <rect width="16" height="16" x="4" y="4" rx="2" />
      <rect width="6" height="6" x="9" y="9" rx="1" />
      <path d="M15 2v2" /><path d="M15 20v2" /><path d="M2 15h2" /><path d="M2 9h2" />
      <path d="M20 15h2" /><path d="M20 9h2" /><path d="M9 2v2" /><path d="M9 20v2" />
    </template>

    <!-- Code -->
    <template v-if="name === 'code'">
      <polyline points="16 18 22 12 16 6" /><polyline points="8 6 2 12 8 18" />
    </template>

    <!-- Users -->
    <template v-if="name === 'users'">
      <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2" /><circle cx="9" cy="7" r="4" />
      <path d="M22 21v-2a4 4 0 0 0-3-3.87" /><path d="M16 3.13a4 4 0 0 1 0 7.75" />
    </template>

    <!-- ShieldCheck -->
    <template v-if="name === 'shield-check'">
      <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
      <path d="m9 12 2 2 4-4" />
    </template>

    <!-- FileCheck -->
    <template v-if="name === 'file-check'">
      <path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z" />
      <polyline points="14 2 14 8 20 8" /><path d="m9 15 2 2 4-4" />
    </template>

    <!-- Award -->
    <template v-if="name === 'award'">
      <circle cx="12" cy="8" r="6" fill="currentColor" />
      <path d="M15.477 12.89 17 22l-5-3-5 3 1.523-9.11" fill="currentColor" />
    </template>

    <!-- Menu -->
    <template v-if="name === 'menu'">
      <line x1="4" y1="12" x2="20" y2="12" /><line x1="4" y1="6" x2="20" y2="6" /><line x1="4" y1="18" x2="20" y2="18" />
    </template>

    <!-- X -->
    <template v-if="name === 'x'">
      <line x1="18" y1="6" x2="6" y2="18" /><line x1="6" y1="6" x2="18" y2="18" />
    </template>

    <!-- Lock -->
    <template v-if="name === 'lock'">
      <rect width="18" height="11" x="3" y="11" rx="2" ry="2" /><path d="M7 11V7a5 5 0 0 1 10 0v4" />
    </template>

    <!-- ChevronDown -->
    <template v-if="name === 'chevron-down'">
      <polyline points="6 9 12 15 18 9" />
    </template>

    <!-- ChevronRight -->
    <template v-if="name === 'chevron-right'">
      <polyline points="9 18 15 12 9 6" />
    </template>

    <!-- Cloud -->
    <template v-if="name === 'cloud'">
      <path d="M17.5 19H9a7 7 0 1 1 6.71-9h1.79a4.5 4.5 0 1 1 0 9Z" />
    </template>

    <!-- Network -->
    <template v-if="name === 'network'">
      <rect x="16" y="16" width="6" height="6" rx="1" />
      <rect x="2" y="16" width="6" height="6" rx="1" />
      <rect x="9" y="2" width="6" height="6" rx="1" />
      <path d="M5 16v-3a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v3" />
      <path d="M12 12V8" />
    </template>

    <!-- BarChart -->
    <template v-if="name === 'bar-chart'">
      <line x1="12" y1="20" x2="12" y2="10" />
      <line x1="18" y1="20" x2="18" y2="4" />
      <line x1="6" y1="20" x2="6" y2="16" />
    </template>

    <!-- Settings -->
    <template v-if="name === 'settings'">
      <circle cx="12" cy="12" r="3" />
      <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z" />
    </template>

    <!-- Monitor -->
    <template v-if="name === 'monitor'">
      <rect x="2" y="3" width="20" height="14" rx="2" ry="2" />
      <line x1="8" y1="21" x2="16" y2="21" />
      <line x1="12" y1="17" x2="12" y2="21" />
    </template>

    <!-- Workflow -->
    <template v-if="name === 'workflow'">
      <rect width="8" height="8" x="3" y="3" rx="2" />
      <path d="M7 11v4a2 2 0 0 0 2 2h4" />
      <rect width="8" height="8" x="13" y="13" rx="2" />
    </template>

    <!-- Wand -->
    <template v-if="name === 'wand'">
      <path d="M15 4V2" /><path d="M15 16v-2" /><path d="M8 9h2" /><path d="M20 9h2" />
      <path d="M17.8 11.8 20 14" /><path d="M15 9h0" />
      <path d="M17.8 6.2 20 4" /><path d="m3 21 9-9" />
      <path d="M12.2 6.2 10 4" />
    </template>

    <!-- FileText -->
    <template v-if="name === 'file-text'">
      <path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z" />
      <polyline points="14 2 14 8 20 8" />
      <line x1="16" y1="13" x2="16" y2="13" /><line x1="16" y1="17" x2="16" y2="17" />
      <line x1="10" y1="9" x2="8" y2="9" />
    </template>

    <!-- Palette -->
    <template v-if="name === 'palette'">
      <circle cx="13.5" cy="6.5" r="0.5" fill="currentColor" />
      <circle cx="17.5" cy="10.5" r="0.5" fill="currentColor" />
      <circle cx="8.5" cy="7.5" r="0.5" fill="currentColor" />
      <circle cx="6.5" cy="12.5" r="0.5" fill="currentColor" />
      <path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10c.926 0 1.648-.746 1.648-1.688 0-.437-.18-.835-.437-1.125-.29-.289-.438-.652-.438-1.125a1.64 1.64 0 0 1 1.668-1.668h1.996c3.051 0 5.555-2.503 5.555-5.554C21.965 6.012 17.461 2 12 2z" />
    </template>

    <!-- AI Analysis -->
    <template v-if="name === 'ai-analysis'">
      <path d="M3 6h18M3 12h18M3 18h18" />
      <path d="M8 12l2-2l2 2l2-2"  stroke-linejoin="round"/>
      <circle cx="18" cy="12" r="2" fill="currentColor"/>
    </template>

    <!-- AI Video -->
    <template v-if="name === 'ai-video'">
      <rect x="3" y="5" width="18" height="14" rx="2" />
      <path d="M10 8l4 2.5L10 13V8z" fill="currentColor"/>
      <circle cx="17" cy="8" r="1" fill="currentColor"/>
    </template>

    <!-- AI Assistant -->
    <template v-if="name === 'ai-assistant'">
      <rect x="7" y="4" width="10" height="16" rx="2" />
      <circle cx="12" cy="8" r="2" fill="currentColor"/>
      <path d="M9 12h6" />
      <path d="M10 15h4" />
    </template>

    <!-- AI Design -->
    <template v-if="name === 'ai-design'">
      <path d="M3 17h18" />
      <path d="M8 17l-2-5l6-3l6 3l-2 5"  stroke-linejoin="round"/>
      <path d="M12 4v13" />
    </template>

    <!-- AI Extract -->
    <template v-if="name === 'ai-extract'">
      <rect x="5" y="5" width="14" height="14" rx="2" />
      <circle cx="12" cy="12" r="4" />
      <path d="M8 8l8 8" />
      <path d="M16 8l-8 8" />
    </template>

    <!-- Stream -->
    <template v-if="name === 'stream'">
      <path d="M3 18l4-4l4 4l4-4l4 4"  stroke-linejoin="round"/>
      <path d="M3 12l4-4l4 4l4-4l4 4"  stroke-linejoin="round"/>
      <path d="M3 6h18" />
    </template>

    <!-- SMS -->
    <template v-if="name === 'sms'">
      <rect x="5" y="3" width="14" height="18" rx="2" />
      <path d="M9 7h6" />
      <path d="M9 11h6" />
      <path d="M9 15h4" />
      <path d="M18 15l3-3l-3-3"  stroke-linejoin="round"/>
    </template>

    <!-- ECS -->
    <template v-if="name === 'ecs'">
      <rect x="4" y="4" width="16" height="16" rx="2" />
      <rect x="6" y="6" width="12" height="4" rx="1" />
      <rect x="6" y="14" width="12" height="4" rx="1" />
      <circle cx="8" cy="10" r="1" fill="currentColor"/>
      <circle cx="12" cy="10" r="1" fill="currentColor"/>
      <circle cx="16" cy="10" r="1" fill="currentColor"/>
    </template>

    <!-- GPU -->
    <template v-if="name === 'gpu'">
      <rect x="4" y="4" width="16" height="16" rx="2" />
      <path d="M8 8h8" />
      <path d="M8 12h8" />
      <path d="M8 16h8" />
      <path d="M12 8V16" />
    </template>

    <!-- Bare Metal -->
    <template v-if="name === 'bare-metal'">
      <rect x="5" y="5" width="14" height="14" rx="1" />
      <rect x="7" y="7" width="10" height="3" rx="0.5" fill="currentColor"/>
      <rect x="7" y="11" width="10" height="3" rx="0.5" fill="currentColor"/>
      <rect x="7" y="15" width="10" height="3" rx="0.5" fill="currentColor"/>
    </template>

    <!-- Cloud PC -->
    <template v-if="name === 'cloud-pc'">
      <rect x="3" y="5" width="18" height="12" rx="2" />
      <circle cx="8" cy="8" r="1" fill="currentColor"/>
      <circle cx="12" cy="8" r="1" fill="currentColor"/>
      <circle cx="16" cy="8" r="1" fill="currentColor"/>
      <path d="M6 19l6-3l6 3"  stroke-linejoin="round"/>
    </template>

    <!-- Benefit Trial -->
    <template v-if="name === 'benefit-trial'">
      <rect x="5" y="7" width="14" height="10" rx="1" />
      <path d="M12 3v4" />
      <path d="M9 10h6" />
      <circle cx="12" cy="13" r="2" fill="currentColor"/>
    </template>

    <!-- Benefit Price -->
    <template v-if="name === 'benefit-price'">
      <circle cx="12" cy="12" r="10" />
      <path d="M8 12h8" />
      <path d="M12 8V16" />
      <path d="M9 9l3 3l3-3"  stroke-linejoin="round"/>
    </template>

    <!-- Benefit Combo -->
    <template v-if="name === 'benefit-combo'">
      <rect x="4" y="4" width="16" height="16" rx="2" />
      <path d="M8 10h8" />
      <path d="M8 14h8" />
      <circle cx="12" cy="12" r="2" fill="currentColor"/>
    </template>

    <!-- Benefit AI -->
    <template v-if="name === 'benefit-ai'">
      <circle cx="12" cy="12" r="8" />
      <circle cx="12" cy="12" r="3" fill="currentColor"/>
      <path d="M12 7l3 3l-3 3l-3-3l3-3z"  stroke-linejoin="round"/>
    </template>

    <!-- Feature Advanced -->
    <template v-if="name === 'feature-advanced'">
      <path d="M12 2v6l3 3"  stroke-linejoin="round"/>
      <path d="M12 22v-6l-3-3"  stroke-linejoin="round"/>
      <path d="M2 12h6l3-3"  stroke-linejoin="round"/>
      <path d="M22 12h-6l-3 3"  stroke-linejoin="round"/>
    </template>

    <!-- Feature Stable -->
    <template v-if="name === 'feature-stable'">
      <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
      <path d="M9 12l2 2l4-4"  stroke-linejoin="round"/>
    </template>

    <!-- Feature Secure -->
    <template v-if="name === 'feature-secure'">
      <rect x="5" y="11" width="14" height="10" rx="2" />
      <rect x="5" y="5" width="14" height="10" rx="2" />
      <path d="M12 11V5" />
      <path d="M8 15l4 4l4-4"  stroke-linejoin="round"/>
    </template>

    <!-- Feature Service -->
    <template v-if="name === 'feature-service'">
      <path d="M12 2v20" />
      <path d="M6 10h12" />
      <path d="M6 14h12" />
      <circle cx="12" cy="6" r="2" fill="currentColor"/>
      <circle cx="12" cy="18" r="2" fill="currentColor"/>
    </template>

    <!-- Setting -->
    <template v-if="name === 'setting'">
      <circle cx="12" cy="12" r="10" />
      <circle cx="12" cy="12" r="3" fill="currentColor"/>
      <path d="M12 6v2" />
      <path d="M12 16v2" />
      <path d="M6 12h2" />
      <path d="M16 12h2" />
      <path d="M19.07 19.07l1.41 1.41" />
      <path d="M3.51 3.51l1.41 1.41" />
      <path d="M19.07 4.93l1.41-1.41" />
      <path d="M3.51 20.49l1.41-1.41" />
    </template>

    <!-- 7Day -->
    <template v-if="name === '7day'">
      <rect x="5" y="5" width="14" height="14" rx="2" />
      <circle cx="12" cy="9" r="1" fill="currentColor"/>
      <circle cx="9" cy="12" r="1" fill="currentColor"/>
      <circle cx="12" cy="12" r="1" fill="currentColor"/>
      <circle cx="15" cy="12" r="1" fill="currentColor"/>
      <circle cx="9" cy="15" r="1" fill="currentColor"/>
      <circle cx="12" cy="15" r="1" fill="currentColor"/>
      <circle cx="15" cy="15" r="1" fill="currentColor"/>
    </template>

    <!-- 15Day -->
    <template v-if="name === '15day'">
      <circle cx="12" cy="12" r="10" />
      <circle cx="12" cy="12" r="3" fill="currentColor"/>
      <path d="M12 2v2" />
      <path d="M12 20v2" />
      <path d="M2 12h2" />
      <path d="M20 12h2" />
      <path d="M16.5 7.5l1.41 1.41" />
      <path d="M6.5 17.5l1.41 1.41" />
      <path d="M16.5 16.5l1.41-1.41" />
      <path d="M6.5 6.5l1.41-1.41" />
    </template>

    <!-- Post -->
    <template v-if="name === 'post'">
      <rect x="5" y="5" width="14" height="14" rx="2" />
      <path d="M7 9h10" />
      <path d="M7 12h10" />
      <path d="M7 15h10" />
      <path d="M12 5v2" />
    </template>
  </svg>
</template>

