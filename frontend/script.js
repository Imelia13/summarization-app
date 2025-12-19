function updateCounter() {
  const text = document.getElementById("text").value.trim();

  const wordCount = text
    ? text.split(/\s+/).filter(w => w.length > 0).length
    : 0;

  const charCount = text.length;

  document.getElementById("wordCount").innerText = `${wordCount} kata`;
  document.getElementById("charCount").innerText = `${charCount} karakter`;
}

async function summarize() {
  const textArea = document.getElementById("text");
  const result = document.getElementById("result");

  const text = textArea.value.trim();

  const wordCount = text
    ? text.split(/\s+/).filter(w => w.length > 0).length
    : 0;

  if (wordCount < 10) {
    alert("Teks terlalu pendek (minimal 10 kata).");
    return;
  }

  result.innerHTML = "⏳ Sedang meringkas...";

  try {
    const response = await fetch("http://127.0.0.1:8000/summarize", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ text })
    });

    if (!response.ok) {
      const err = await response.text();
      throw new Error(err);
    }

    const data = await response.json();

    result.innerText = data.summary || "⚠️ Ringkasan tidak tersedia.";

  } catch (error) {
    console.error(error);
    result.innerText = "❌ Gagal terhubung ke server backend.";
  }
}
