import { marked } from 'marked';

export const parseMarkdown = (text: string | undefined): string => {
  if (!text) return '';

  // Custom renderer
  const renderer = new marked.Renderer();

  // Override function to handle headings
  renderer.heading = (text, level) => {
    const escapedText = text.toLowerCase().replace(/[^\w]+/g, '-');
    return `<h${level} id="${escapedText}">${text}</h${level}>`;
  };

  // Override function to handle links
  renderer.link = (href, title, text) => {
    if (href.startsWith('/')) {
      href = `https://github.com/Lissy93/personal-security-checklist/blob/old-version/${href}`;
    }
    title = title ? `title="${title}"` : '';
    return `<a href="${href}" ${title} target="_blank" rel="noopener noreferrer">${text}</a>`;
  };

  // Sanitize the input to remove <script> tags
  const sanitizeHtml = (html: string): string => {
    return html.replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, '');
  };

  // Configure marked with the custom renderer
  marked.use({ renderer });

  // Parse the markdown, then sanitize the HTML to remove <script> tags
  const rawHtml = marked.parse(text, { async: false}) as string;
  const sanitizedHtml = sanitizeHtml(rawHtml);

  return sanitizedHtml;
};

export const formatLink = (link: string) => {
  return (link || '').replace(/^(https?:\/\/)?(www\.)?/, '').replace(/\/+$/, '');
};
