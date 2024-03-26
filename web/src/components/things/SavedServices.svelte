<script lang="ts">
import { onMount } from 'svelte';
import { writable } from 'svelte/store';

import type { Category, Service } from '../../types/Service';
import { slugify } from "@utils/fetch-data";
import ServiceCard from './ServiceCard.svelte';

export let allData: Category[];
export let serviceList: string[] | null = null;

interface SavedServices {
  category: string;
  section: string;
  service: Service;
}

const savedServices = writable<SavedServices[]>([]);

onMount(async () => {
  const results: SavedServices[] = [];
  const saved = serviceList || JSON.parse(localStorage.getItem('savedServices') || '[]');
  saved.forEach((serviceId: string) => {
    const parts = serviceId.split('/');
    const categoryName = parts[0];
    const sectionName = parts[1];
    const serviceName = parts[2];

    const category = allData.find((category) => slugify(category.name) === categoryName);
    if (!category) return;
    const section = category.sections.find((section) => slugify(section.name) === sectionName);
    if (!section) return;
    const service = section.services.find((service) => slugify(service.name) === serviceName);
    if (!service) return;
    results.push({ category: category.name, section: section.name, service});
  });
  savedServices.set(results || []);
});

</script>

<div>
  {#if $savedServices.length > 0}
    <div class="saved-services">
      {#each $savedServices as thingy}
        <ServiceCard
          categoryName={thingy.category}
          sectionName={thingy.section}
          service={thingy.service}
        />
      {/each}
    </div>
  {:else if !serviceList}
    <div class="nothing-yet">
      <p>Here you'll find a list of all the software and services you've bookmarked.</p>
      <small>
        All data is stored on-device, in your browser's local storage,
        and not sent anywhere unless you choose to share it
      </small>
      <p class="nope">Nothing saved yet!</p>
    </div>
  {/if}
</div>

<style lang="scss">
  .saved-services {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 1rem;
    margin-top: 1rem;
  }

  .nothing-yet {
    text-align: center;
    p {
      margin: 0;
    }
    small {
      font-size: 0.8rem;
      opacity: 0.6;
    }
    .nope {
      font-weight: bold;
      margin: 2rem 0;
      opacity: 0.2;
      font-size: 1.6rem;
    }
  }
</style>
