import SbCantoListClient from "../../../components/SbCantoListClient";

export default function SbCantosPage({ searchParams }) {
  const audience = searchParams?.audience || "adult";
  const audienceLabel = audience.charAt(0).toUpperCase() + audience.slice(1);
  return (
    <main style={{ maxWidth: 900, margin: "0 auto", padding: "24px 16px" }}>
      {/* Breadcrumb */}
      <div style={{ fontSize: 14, opacity: 0.8, marginBottom: 10 }}>
        <a href="/">Home</a>
        <span style={{ opacity: 0.6 }}> / </span>
        <a href={`/sb?audience=${audience}`}>Shrimad Bhagavatam</a>
        <span style={{ opacity: 0.6 }}> / </span>
        <span>{audienceLabel}</span>
      </div>
      <h1 style={{ fontSize: 28, margin: "0 0 10px" }}>Shrimad Bhagavatam Cantos</h1>
      {/* Audience filter bar */}
      <div className="filterBar" style={{ marginTop: 10, marginBottom: 18 }}>
        <a href="/sb/cantos?audience=adult">
          <button className={`filterBtn ${audience === "adult" ? "filterBtnActive" : ""}`}>Adult</button>
        </a>
        <a href="/sb/cantos?audience=teens">
          <button className={`filterBtn ${audience === "teens" ? "filterBtnActive" : ""}`}>Teens</button>
        </a>
        <a href="/sb/cantos?audience=kids">
          <button className={`filterBtn ${audience === "kids" ? "filterBtnActive" : ""}`}>Kids</button>
        </a>
      </div>
      <SbCantoListClient audience={audience} />
      <div style={{ marginTop: 18 }}>
        <a href={`/sb?audience=${audience}`} className="backLink">&larr; Back</a>
      </div>
    </main>
  );
}
