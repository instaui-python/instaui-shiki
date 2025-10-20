export function trimNewlines(s: string) {
  return s.replace(/^[\r\n\u2028\u2029]+|[\r\n\u2028\u2029]+$/g, "");
}
