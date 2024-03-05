import { slugify } from '@utils/fetch-data';

export const makeRemovalRequest = (categoryName: string, sectionName: string, serviceName: string, yaml?: string) => {
  const title = `[REMOVAL] ${serviceName}`;
  const under = `**${serviceName}** (source: [${categoryName} ➜ ${sectionName} ➜ ${serviceName}`
    + `](https://github.com/Lissy93/awesome-privacy/tree/main#${slugify(sectionName)}))`;
  const removalData = `&title=${encodeURIComponent(title)}&removal-data=`
    + `${encodeURIComponent(yaml || '')}&service-title=${encodeURIComponent(under)}`;
  const issueCreate = 'https://github.com/Lissy93/awesome-privacy/issues/new'
  const baseOptions = '?assignees=lissy93&labels=Suggested+Removal%2CAwaiting+'
    + 'Review&projects=&template=removal.yml'
  return `${issueCreate}${baseOptions}${removalData}`;
};

export const makeEditRequest = (categoryName: string, sectionName: string, serviceName: string, yaml?: string) => {
  const title = `[AMENDMENT] ${serviceName}`;
  const under = `**${serviceName}** (source: [${categoryName} ➜ ${sectionName} ➜ ${serviceName}`
    + `](https://github.com/Lissy93/awesome-privacy/tree/main#${slugify(sectionName)}))`;
  const removalData = `&title=${encodeURIComponent(title)}&amendment-data=`
    + `${encodeURIComponent(yaml || '')}&service-title=${encodeURIComponent(under)}`;
  const issueCreate = 'https://github.com/Lissy93/awesome-privacy/issues/new'
  const baseOptions = '?assignees=lissy93&labels=Suggested+Removal%2CAwaiting+'
    + 'Review&projects=&template=amendment.yml'
  return `${issueCreate}${baseOptions}${removalData}`;
};

export const fetchSrcData = async (categoryName: string, sectionName: string, serviceName: string) => {
  const lineNumberData = await fetch('/api/line-numbers.json')
    .then((res) => res.json());

  if ( lineNumberData
    && lineNumberData[categoryName]
    && lineNumberData[categoryName][sectionName]
    && lineNumberData[categoryName][sectionName][serviceName]
  ) {
    return {
      lineNumbers: lineNumberData[categoryName][sectionName][serviceName].lineNumbers,
      yamlContent: lineNumberData[categoryName][sectionName][serviceName].yaml,
    };
  } else {
    console.error('No line number data found for', categoryName, sectionName, serviceName);
    return { lineNumbers: [], yamlContent: '' };
  }
};
