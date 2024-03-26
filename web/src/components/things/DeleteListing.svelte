
<script lang="ts">
  import FontAwesome from '@components/form/FontAwesome.svelte';
  import { fetchSrcData, makeRemovalRequest } from '@utils/data-src-delete-n-edit';
  import { onMount } from 'svelte';


  export let categoryName: string;
  export let sectionName: string;
  export let serviceName: string;

  const apYaml = 'https://github.com/lissy93/awesome-privacy/blob/main/awesome-privacy.yml';

  let yamlContent = '';
  let editLink = apYaml;

  onMount(async () => {
    const results = await fetchSrcData(categoryName, sectionName, serviceName);
    yamlContent = results.yamlContent;

    const lineNumbers = results.lineNumbers || null;
    const numberRange = lineNumbers ? `#L${lineNumbers.start}-L${lineNumbers.end}` : '';
    const yamlLink = 'https://github.com/lissy93/awesome-privacy/blob/main/awesome-privacy.yml';
    editLink = `${yamlLink}${numberRange}`;
  });

</script>

<div class="actions">
  <a title="Edit" target="_blank"
    href={editLink}>
    <FontAwesome iconName="edit" />
  </a>
  <a title="Delete" target="_blank"
    href={makeRemovalRequest(categoryName, sectionName, serviceName, yamlContent)}>
    <FontAwesome iconName="delete" />
  </a>
</div>

<style lang="scss">
.actions {
  position: absolute;
  right: 3.5rem;
  top: 1rem;
  width: 2.8rem;
  gap: 1rem;
  opacity: 0;
  display: flex;
  transition: all 0.2s ease-in-out;
  a {
    color: var(--foreground);
    width: 1rem;
    transition: all 0.2s ease-in-out;
    &:hover {
      color: var(--accent-3);
      opacity: 1;
    }
  }
  
}
</style>
