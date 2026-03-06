<template>
  <div id="volcengine-app">
    <NavBar />
    <main>
      <HeroSection />
      <ModelsSection />
      <AgentSection />
      <CloudProductsSection />
      <ScenariosSection />
      <SolutionsSection />
      <EcosystemSection />
    </main>
    <FooterSection />
  </div>
</template>

<script>
import NavBar from '../volc/NavBar.vue';
import HeroSection from '../volc/HeroSection.vue';
import ModelsSection from '../volc/ModelsSection.vue';
import AgentSection from '../volc/AgentSection.vue';
import CloudProductsSection from '../volc/CloudProductsSection.vue';
import ScenariosSection from '../volc/ScenariosSection.vue';
import SolutionsSection from '../volc/SolutionsSection.vue';
import EcosystemSection from '../volc/EcosystemSection.vue';
import FooterSection from '../volc/FooterSection.vue';

export default {
  name: 'HomeIndex',
  components: {
    NavBar,
    HeroSection,
    ModelsSection,
    AgentSection,
    CloudProductsSection,
    ScenariosSection,
    SolutionsSection,
    EcosystemSection,
    FooterSection,
  },
};
</script>

<style src="../volc/volc-main.css"></style>
<style scoped>
#volcengine-app {
  background-color: var(--bg-primary);
  color: var(--text-primary);
  min-height: 100vh;
}

#volcengine-app main {
  background: transparent;
}
</style>
