type Level = 'warn' | 'error';

interface LogEntry {
  level: Level;
  source: string;
  message: string;
}

const entries: LogEntry[] = [];

export const warn = (source: string, message: string) => {
  console.warn(`[${source}] ${message}`);
  entries.push({ level: 'warn', source, message });
};

export const error = (source: string, message: string) => {
  console.error(`[${source}] ${message}`);
  entries.push({ level: 'error', source, message });
};

export const printSummary = () => {
  if (entries.length === 0) return;

  const grouped: Record<string, { errors: number; warnings: number; messages: string[] }> = {};
  for (const entry of entries) {
    if (!grouped[entry.source]) {
      grouped[entry.source] = { errors: 0, warnings: 0, messages: [] };
    }
    const group = grouped[entry.source];
    if (entry.level === 'error') group.errors++;
    else group.warnings++;
    group.messages.push(`  ${entry.level.toUpperCase()}: ${entry.message}`);
  }

  console.log('\n───────────── Build fetch summary ──────────────');
  for (const [source, { errors, warnings, messages }] of Object.entries(grouped)) {
    const parts = [];
    if (errors) parts.push(`${errors} error${errors > 1 ? 's' : ''}`);
    if (warnings) parts.push(`${warnings} warning${warnings > 1 ? 's' : ''}`);
    console.log(`[${source}] ${parts.join(', ')}`);
    for (const msg of messages) {
      console.log(msg);
    }
  }
  console.log('────────────────────────────────────────────────\n');

  entries.length = 0;
};
