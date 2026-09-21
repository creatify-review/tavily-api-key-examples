// Run one Tavily Search call with the JavaScript SDK.
//
//   npm i @tavily/core
//   export TAVILY_API_KEY=tvly-...
//   node examples/quickstart.js "Who is Leo Messi?"
//
// Client construction and the search call match the quickstart's JavaScript tab.

const { tavily } = require("@tavily/core");

async function main() {
  const apiKey = process.env.TAVILY_API_KEY;
  if (!apiKey) {
    console.error("TAVILY_API_KEY is not set. Copy a key from app.tavily.com first.");
    process.exit(1);
  }
  if (!apiKey.startsWith("tvly-")) {
    console.error("Warning: Tavily keys start with 'tvly-'; check the value you exported.");
  }

  const query = process.argv[2] || "Who is Leo Messi?";
  const tvly = tavily({ apiKey });
  const response = await tvly.search(query);

  // Print the full response once and read the keys before writing parsing code.
  console.log(JSON.stringify(response, null, 2));
}

main().catch((err) => {
  console.error("Search failed:", err && err.message ? err.message : err);
  process.exit(1);
});
