module.exports = (req, res) => {
  const apiKey = process.env.GEOAPIFY_API_KEY || "";
  const payload = `window.__APP_CONFIG__ = { GEOAPIFY_API_KEY: ${JSON.stringify(apiKey)} };\n`;
  res.setHeader("Content-Type", "application/javascript; charset=utf-8");
  res.status(200).send(payload);
};
