<script lang="ts">
  import FontAwesome from '@components/form/FontAwesome.svelte';
  import SaveListing from '@components/things/SaveListing.svelte';
  import { slugify } from '@utils/fetch-data';
  import { formatLink } from '@utils/parse-markdown';
  import type { Service } from 'src/types/Service';

  export let service: Service;
  export let categoryName: string;
  export let sectionName: string;

  // Computed values based on props
  let serviceRef = slugify(service.name);
  let categorySlug = slugify(categoryName);
  let sectionSlug = slugify(sectionName);
</script>

<div class="service" id={serviceRef}>
  <div class="service-head">
    <a
      class="service-title"
      href={`/${categorySlug}/${sectionSlug}/${serviceRef}`}
    >
      <h4>{service.name}</h4>
    </a>
    {#if service.followWith}
      <p class="follow-with">({service.followWith})</p>
    {/if}
  </div>

  <div class="save-listing">
    <SaveListing {categoryName} {sectionName} serviceName={service.name} />
  </div>

  <div class="service-body">
    <img
      width="40"
      height="40"
      loading="lazy"
      decoding="async"
      class="service-icon"
      alt={`${service.name} Icon`}
      data-service-url={formatLink(service.url)}
      src={service.icon || `https://icon.horse/icon/${formatLink(service.url)}`}
    />
    <div class="service-body">
      <p>{@html service.description}</p>
    </div>
  </div>

  <div class="service-links">
    <a class="link" href={service.url}>
      <FontAwesome iconName="website" /> <span>{formatLink(service.url)}</span>
    </a>
    {#if service.github}
      <a class="link" href={`https://github.com/${service.github}`}>
        <FontAwesome iconName="sourceCode" /> GitHub
      </a>
    {/if}
    <a href={`/${categorySlug}/${sectionSlug}/${serviceRef}`}>
      <FontAwesome iconName="viewReport" /> View Report ➔
    </a>
  </div>
</div>

<style lang="scss">
  @import './service-card.scss';
</style>
