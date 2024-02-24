<script lang="ts">
  import { onMount } from "svelte";
  import { writable } from "svelte/store"; // Import writable to create a reactive variable
  import type { Category, Service } from "../../types/Service";
  import { parseMarkdown, formatLink } from '@utils/parse-markdown';
  import { slugify } from '@utils/fetch-data';

  interface ServiceResult extends Service {
    path: string;
  }

  export let categories: Category[];
  export let searchTerm: string;

  let results = writable<ServiceResult[]>([]);

  onMount(async () => {

    const apiEndpoint = `https://awesome-privacy.as93.workers.dev/${searchTerm}`;
    const fetchedServices = await fetch(apiEndpoint)
      .then((response) => response.json())
      .then((data) => {
        console.log("SmartSuggestions data", data);
        return JSON.parse(data);
      });

    const tmpResults: ServiceResult[] = [];
    categories.forEach((category) => {
      (category.sections || []).forEach((section) => {
        (section.services || []).forEach((service) => {
          if (fetchedServices.includes(service.name)) {
            const path = `/${slugify(category.name)}/${slugify(section.name)}#${slugify(service.name)}`
            tmpResults.push({ ...service, path });
            return;
          }
        });
      });
    });
    results.set(tmpResults);
  });
</script>

{#if $results.length === 1}
  <h3>Top Result</h3>
{/if}
{#if $results.length > 1}
  <h3>Top Results</h3>
{/if}
  <section>
    {#each $results as service (service)}
      <a class="service-result" href={service.path}>
        <div class="service-head">
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
          <div>
            <h4>
              {service.name}
              {#if service.followWith}
              <p class="follow-with">({service.followWith})</p>
              {/if}
            </h4>
            <a class="service-link" href={service.url}>{formatLink(service.url)}</a>
          </div>
        </div>
      </a>
    {/each}
  </section>



<style lang="scss">
  h3 {
    width: 80vw;
    max-width: 900px;
    margin: 1rem auto;
    color: var(--accent-3);
    font-size: 1.6rem;
  }
  section {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 1rem;
    width: 80vw;
    max-width: 900px;
    margin: 0 auto;
    .service-result {
      background: var(--accent-fg);
      padding: 1rem;
      border-radius: var(--curve-sm);
      border: 1px solid var(--foreground);
      box-shadow: 3px 3px 0 var(--foreground);
      color: var(--foreground);
      text-decoration: none;

      .service-head {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        h4 {
          margin: 0;
          font-size: 1.6rem;
          display: flex;
          align-items: center;
          gap: 0.5rem;
          .follow-with {
            opacity: 0.7;
            font-style: italic;
            margin: 0;
            font-size: 0.85rem;
            font-weight: 400;
          }
        }
        .service-icon {
          width: 2.5rem;
          height: 2.5rem;
          border-radius: var(--curve-sm);

          font-size: 10px;
          overflow: hidden;
          color: var(--accent);
        }

        .service-link {
          max-width: 300px;
          text-overflow: ellipsis;
          overflow: hidden;
          white-space: nowrap;
        }
      }
    }
  }
</style>
