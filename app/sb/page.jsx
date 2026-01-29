import Link from "next/link";
import { redirect } from "next/navigation";
import SbCantoListClient from "../../components/SbCantoListClient";

function getAudienceFromSearchParams(searchParams) {
  const a = searchParams?.audience;
  const v = Array.isArray(a) ? a[0] : a;
  if (v === "kids" || v === "teens" || v === "adult") return v;
  return "adult";
}

export default function SbIndex({ searchParams }) {
  if (!searchParams?.audience) {
    redirect("/sb/?audience=adult");
  }

  const audience = getAudienceFromSearchParams(searchParams);
  const audienceLabel = audience.charAt(0).toUpperCase() + audience.slice(1);

  return (
    <main style={{ maxWidth: 900, margin: "0 auto", padding: "24px 16px" }}>
      {/* Breadcrumb (match BG style) */}
      <div style={{ fontSize: 14, opacity: 0.8, marginBottom: 10 }}>
        <Link href="/">Home</Link>
        <span style={{ opacity: 0.6 }}> / </span>
        <span>Srimad Bhagavatam</span>
        <span style={{ opacity: 0.6 }}> / </span>
        <span>{audienceLabel}</span>
      </div>

      <h1 style={{ fontSize: 28, margin: "0 0 10px" }}>Srimad Bhagavatam</h1>

      {/* Tabs */}
      <div className="filterBar" style={{ marginTop: 10, marginBottom: 18 }}>
        <Link href="/sb/?audience=adult">
          <button className={`filterBtn ${audience === "adult" ? "filterBtnActive" : ""}`}>Adult</button>
        </Link>
        <Link href="/sb/?audience=teens">
          <button className={`filterBtn ${audience === "teens" ? "filterBtnActive" : ""}`}>Teens</button>
        </Link>
        <Link href="/sb/?audience=kids">
          <button className={`filterBtn ${audience === "kids" ? "filterBtnActive" : ""}`}>Kids</button>
        </Link>
      </div>

      {/* Canto List with Progress */}
      <SbCantoListClient audience={audience} />

      <div style={{ marginTop: 18 }}>
        <Link href="/">Back to home</Link>
      </div>
    </main>
  );
}
