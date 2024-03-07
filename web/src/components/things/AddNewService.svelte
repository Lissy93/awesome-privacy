<script lang="ts">
  import yaml from 'js-yaml';
  import { writable } from 'svelte/store';
  import { makeAdditionRequest } from '../../utils/data-src-delete-n-edit';

  // Defining writable stores for each form field
  const listingCategory = writable('');
  const serviceName = writable('');
  const serviceUrl = writable('');
  const serviceIcon = writable('');
  const serviceDescription = writable('');
  const serviceGithub = writable('');
  const serviceTosdrId = writable('');
  const serviceOpenSource = writable(false);
  const serviceSecurityAudited = writable(false);
  const serviceCrypto = writable(false);
  const additionalInfo = writable('');
  
  $: yamlText = yaml.dump([{
        name: $serviceName,
        url: $serviceUrl,
        icon: $serviceIcon,
        description: $serviceDescription,
        github: $serviceGithub,
        tosdrId: $serviceTosdrId,
        openSource: $serviceOpenSource,
        securityAudited: $serviceSecurityAudited,
        acceptsCrypto: $serviceCrypto,
    }]);

  $: issueUrl = makeAdditionRequest({
      listingCategory: $listingCategory,
      serviceName: $serviceName,
      serviceUrl: $serviceUrl,
      serviceIcon: $serviceIcon,
      serviceDescription: $serviceDescription,
      serviceGithub: $serviceGithub,
      serviceTosdrId: $serviceTosdrId,
      serviceOpenSource: $serviceOpenSource,
      serviceSecurityAudited: $serviceSecurityAudited,
      serviceCrypto: $serviceCrypto,
      additionalInfo: $additionalInfo,
  }, yamlText);

  // Form submission handler
  function handleSubmit() {
      const formData = {
          listingCategory: $listingCategory,
          serviceName: $serviceName,
          serviceUrl: $serviceUrl,
          serviceIcon: $serviceIcon,
          serviceDescription: $serviceDescription,
          serviceGithub: $serviceGithub,
          serviceTosdrId: $serviceTosdrId,
          serviceOpenSource: $serviceOpenSource,
          serviceSecurityAudited: $serviceSecurityAudited,
          serviceCrypto: $serviceCrypto,
          additionalInfo: $additionalInfo,
      };
      const issueCreationUrl = makeAdditionRequest(formData, yamlText);
      window.open(issueCreationUrl, '_blank');
  }
</script>

<p>
  Before completing this form, you must ensure that the service you are adding aligns
  with the <a href="/about#creteria">Requirements</a> for Awesome Privacy.
  <br />
  You'll need a GitHub account in order to submit this form.
</p>

<form on:submit|preventDefault={handleSubmit}>
  <!-- Category Dropdown -->
  <div class="form-row">
    <label for="listing-category">Category</label>
    <select bind:value={$listingCategory} id="listing-category" required autocomplete="off">
      <option value="">--Please choose an option--</option>
      <option value="Essentials">Essentials</option>
      <option value="Communication">Communication</option>
      <option value="Security Tools">Security Tools</option>
      <option value="Networking">Networking</option>
      <option value="Productivity">Productivity</option>
      <option value="Utilities">Utilities</option>
      <option value="Operating Systems">Operating Systems</option>
      <option value="Development">Development</option>
      <option value="Home and IoT">Home and IoT</option>
      <option value="Finance">Finance</option>
      <option value="Social">Social</option>
      <option value="Media">Media</option>
      <option value="Creativity">Creativity</option>
    </select>
    <p>
      Choose the top-level category, which should align with
      the <a href="/browse">one of these</a>.
    </p>
  </div>

  <!-- Listing Name -->
  <div class="form-row">
    <label for="service-name">Listing Name</label>
    <input type="text" bind:value={$serviceName} id="service-name" required autocomplete="off">
    <p>Enter the name of the app, software or service</p>
  </div>

  <!-- Listing URL -->
  <div class="form-row">
    <label for="service-url">Listing URL</label>
    <input type="url" bind:value={$serviceUrl} id="service-url" required autocomplete="off">
    <p>Enter the fully-qualified domain name of the homepage for this listing</p>
  </div>
  
  <!-- Listing Icon -->
  <div class="form-row">
    <label for="service-icon">Listing Icon</label>
    <input type="url" bind:value={$serviceIcon} id="service-icon" required autocomplete="off">
    <p>Paste a URL to a square logo for the service. Dimensions must be no less than 64x64, and no more than 512x512 pixels</p>
  </div>

  <!-- Listing Description -->
  <div class="form-row">
    <label for="service-description">Listing Description</label>
    <textarea bind:value={$serviceDescription} id="service-description" required autocomplete="off"></textarea>
    <p>Please provide a description for this listing. Keep it factual and objective. Markdown is supported.</p>
  </div>

  <!-- GitHub Repository -->
  <div class="form-row">
    <label for="service-github">GitHub Repository</label>
    <input type="text" bind:value={$serviceGithub} id="service-github" required autocomplete="off">
    <p>Share a link to where the project's source is located</p>
  </div>

  <!-- ToS;DR ID -->
  <div class="form-row">
    <label for="service-tosdr-id">ToS;DR ID</label>
    <input type="number" bind:value={$serviceTosdrId} id="service-tosdr-id" autocomplete="off">
    <p>
      Has the Privacy policy been documented by <a href="https://tosdr.org/">tosdr.org</a>?
      If so, please include the report reference below (this is a 3 or 4-digit numerical ID).
      Skip section if not applicable.
    </p>
  </div>

    <!-- Open Source Checkbox -->
  <div class="form-row">
    <label for="service-open-source">Is Open Source?</label>
    <input type="checkbox" bind:checked={$serviceOpenSource} id="service-open-source">
    <p>Is this service fully open source? Aka, can it be compiled from source by the user, or self-hosted?</p>
  </div>

  <!-- Security Audited Checkbox -->
  <div class="form-row">
    <label for="service-security-audited">Security Audited?</label>
    <input type="checkbox" bind:checked={$serviceSecurityAudited} id="service-security-audited">
    <p>Has this service been independently security audited by an accredited auditor?</p>
  </div>

  <!-- Accepts Crypto Checkbox -->
  <div class="form-row">
    <label for="service-crypto">Accepts Anon Payment?</label>
    <input type="checkbox" bind:checked={$serviceCrypto} id="service-crypto">
    <p>If this is a hosted and paid for service, does it accept anonymous payment methods, including crypto (e.g., Monero)?</p>
  </div>

  <div class="final-info">
    <p>
      Finally, please provide any supporting material, including:
    </p>
    <ul>
      <li>
        A justification of why this app/service should be included in the list
      </li>
      <li>
        Links to any published security audit, if they exist
      </li>
      <li>
        Links to the services privacy policy, terms of service and other relevant
        documents where applicable
      </li>
      <li>
        Your affiliation with the service.
        For transparency, you must disclose if you are associated
        with them or any similar items in any way
      </li>
      <li>Links to relevant discussions, past issues/PRs related to this service</li>
    </ul>
    <textarea bind:value={$additionalInfo} id="additional-info" rows="5"></textarea>
  </div>

  <button type="submit">Submit</button>
  <a href={issueUrl} target="_blank" class="open-in-gh">Open in GitHub Issues</a>
</form>

<div class="output-yaml">
  <p>Below is the YAML content, which will be appended to the appropriate section
    within <a href="github.com/lissy93/awesome-privacy/blob/main/awesome-privacy.yml">awesome-privacy.yml</a>
    upon approval.
  </p>
  <pre>{@html yamlText}</pre>
  <p>Your submission will need to be reviewed by a maintainer and the community before it can be merged.</p>
</div>

<style lang="scss">
  .form-row {
    display: grid;
    grid-template-columns: 1fr 3fr 2fr;
    gap: 1rem;
    padding: 0.5rem 0;
    &:not(:last-child) {
      border-bottom: 1px solid var(--transparent-accent);
    }
    p {
      margin: 0;
      font-size: 0.8rem;
      opacity: 0.6;
    }
  }

  .final-info {
    display: flex;
    flex-direction: column;
    padding: 1rem 0;
    gap: 1rem;
    p {
      margin: 0.5rem 0;
    }
    ul {
      padding-left: 0.25rem;
      margin: 0 0 0.5rem 0;
      font-size: 0.8rem;
      opacity: 0.6;
      list-style: circle;
    }
  }

  input, textarea {
    width: 100%;
    border: 1px solid var(--accent-3);
    border-radius: var(--curve-md);
    font-size: 1.2rem;
    padding: 0.5rem 0;
    &:focus {
      outline: none;
      border: 2px solid var(--accent);
    }
  }
  input {
    height: fit-content;
    &[type="number"]::-webkit-outer-spin-button,
    &[type="number"]::-webkit-inner-spin-button {
        -webkit-appearance: none;
        margin: 0;
    }
    &[type="number"] {
        -moz-appearance: textfield;
    }
    &[type="checkbox"] {
      width: 2rem;
      height: 2rem;
    }
  }
  textarea {
    resize: vertical;
  }
  .open-in-gh {
    margin: 0 auto;
    font-size: 0.8rem;
    opacity: 0.6;
    display: block;
    text-align: center;
  }

  button {
    cursor: pointer;
    background: var(--accent-3);
    color: var(--accent-fg);
    padding: 0.5rem 2rem;
    border: 1px solid var(--foreground);
    box-shadow: 3px 3px 0 var(--foreground);
    border-radius: var(--curve-lg);
    font-size: 1.8rem;
    font-family: "Lekton", sans-serif;
    margin: 1rem auto;
    display: flex;
    transition: all 0.2s ease-in-out;
    &:hover {
      background: var(--accent);
    }
  }

  .output-yaml {
    pre {
      font-family: 'Courier New', Courier, monospace;
      background: #cecbf780;
      padding: 0.2rem 0.4rem;
      border-radius: var(--curve-sm);
      font-size: 0.9rem;
    }
  }
</style>
