import { slugify } from '@utils/fetch-data';

export const makeRemovalRequest = (
  categoryName: string,
  sectionName: string,
  serviceName: string,
  yaml?: string,
) => {
  const title = `[REMOVAL] ${serviceName}`;
  const under =
    `**${serviceName}** (source: [${categoryName} ➜ ${sectionName} ➜ ${serviceName}` +
    `](https://github.com/Lissy93/awesome-privacy/tree/main#${slugify(sectionName)}))`;
  const removalData =
    `&title=${encodeURIComponent(title)}&removal-data=` +
    `${encodeURIComponent(yaml || '')}&service-title=${encodeURIComponent(under)}`;
  const issueCreate = 'https://github.com/Lissy93/awesome-privacy/issues/new';
  const baseOptions =
    '?assignees=lissy93&labels=Suggested+Removal%2CAwaiting+' +
    'Review&projects=&template=removal.yml';
  return `${issueCreate}${baseOptions}${removalData}`;
};

export const makeEditRequest = (
  categoryName: string,
  sectionName: string,
  serviceName: string,
  yaml?: string,
) => {
  const title = `[AMENDMENT] ${serviceName}`;
  const under =
    `**${serviceName}** (source: [${categoryName} ➜ ${sectionName} ➜ ${serviceName}` +
    `](https://github.com/Lissy93/awesome-privacy/tree/main#${slugify(sectionName)}))`;
  const removalData =
    `&title=${encodeURIComponent(title)}&amendment-data=` +
    `${encodeURIComponent(yaml || '')}&service-title=${encodeURIComponent(under)}`;
  const issueCreate = 'https://github.com/Lissy93/awesome-privacy/issues/new';
  const baseOptions =
    '?assignees=lissy93&labels=Suggested+Removal%2CAwaiting+' +
    'Review&projects=&template=amendment.yml';
  return `${issueCreate}${baseOptions}${removalData}`;
};

export const makeAdditionRequest = (
  formData: {
    listingCategory: string;
    serviceName: string;
    serviceUrl: string;
    serviceIcon: string;
    serviceDescription: string;
    serviceGithub: string;
    serviceTosdrId: string;
    serviceIosApp: string;
    serviceAndroidApp: string;
    serviceDiscordInvite: string;
    serviceSubreddit: string;
    serviceOpenSource: boolean;
    serviceSecurityAudited: boolean;
    serviceCrypto: boolean;
    additionalInfo: string;
  },
  yamlText?: string,
) => {
  const userInfo = formData.additionalInfo
    .split('\n')
    .map((line) => `> ${line}`)
    .join('\n');
  const additionalInfoText: string =
    `\n${userInfo}` +
    `\n\n**YAML Content for Addition**\n\n\`\`\`yaml\n${yamlText || '# nothing yet'}\n\`\`\`\n` +
    `\n\n<sup>This ticket was submitted via ` +
    `<a href="https://awesome-privacy.xyz/submit">awesome-privacy.xyz/submit</a></sup>`;

  const issueTitle = `[ADDITION] ${formData.serviceName} (Complete)`;
  const queryParams = new URLSearchParams({
    assignees: 'lissy93,liss-bot',
    labels: '',
    projects: '',
    template: 'complete-addition.yml',
    title: issueTitle,
    'listing-category': formData.listingCategory,
    'service-name': formData.serviceName,
    'service-url': formData.serviceUrl,
    'service-icon': formData.serviceIcon,
    'service-description': formData.serviceDescription,
    'service-github': formData.serviceGithub,
    'service-tosdr-id': formData.serviceTosdrId,
    'service-opensource': formData.serviceOpenSource ? 'true' : 'false',
    'service-security-audited': formData.serviceSecurityAudited
      ? 'true'
      : 'false',
    'service-crypto': formData.serviceCrypto ? 'true' : 'false',
    'additional-info': additionalInfoText,
  });
  const issueCreateUrl =
    'https://github.com/Lissy93/awesome-privacy/issues/new';
  return `${issueCreateUrl}?${queryParams.toString()}`;
};

export const makeSourceYamlLink = async (
  categoryName: string,
  sectionName: string,
  serviceName: string,
) => {
  const sourceData = await fetchSrcData(categoryName, sectionName, serviceName);
  const lineNumbers = sourceData.lineNumbers || null;
  const numberRange = lineNumbers
    ? `L${lineNumbers.start}-L${lineNumbers.end}`
    : '';
  const yamlLink =
    'https://github.com/lissy93/awesome-privacy/blob/main/awesome-privacy.yml';
  return `${yamlLink}${numberRange}`;
};

export const fetchSrcData = async (
  categoryName: string,
  sectionName: string,
  serviceName: string,
) => {
  const lineNumberData = await fetch('/api/line-numbers.json').then((res) =>
    res.json(),
  );

  if (
    lineNumberData &&
    lineNumberData[categoryName] &&
    lineNumberData[categoryName][sectionName] &&
    lineNumberData[categoryName][sectionName][serviceName]
  ) {
    return {
      lineNumbers:
        lineNumberData[categoryName][sectionName][serviceName].lineNumbers,
      yamlContent: lineNumberData[categoryName][sectionName][serviceName].yaml,
    };
  } else {
    console.error(
      'No line number data found for',
      categoryName,
      sectionName,
      serviceName,
    );
    return { lineNumbers: [], yamlContent: '' };
  }
};
