import Link from "next/link";
import { redirect } from "next/navigation";
import { listSbCantos } from "../../lib/quizLoader";

function getAudienceFromSearchParams(searchParams) {
  const a = searchParams?.audience;
  const v = Array.isArray(a) ? a[0] : a;
  return v === "kids" ? "kids" : "adult"; // default adult
}

export default function SbIndex({ searchParams }) {
  // UX: make default explicit in URL
  if (!searchParams?.audience) {
    redirect("/sb/?audience=adult");
  }

  const cantos = listSbCantos();
  const audience = getAudienceFromSearchParams(searchParams);

  return (
    <main style={{ maxWidth: 900, margin: "0 auto", padding: "24px 16px" }}>
      <h1 style={{ fontSize: 28, marginBottom: 10 }}>Srimad Bhagavatam</h1>

      {/* Tabs: Adult / Kids only */}
      <div className="filterBar" style={{ marginBottom: 18 }}>
        <Link href="/sb/?audience=adult">
          <button className={`filterBtn ${audience === "adult" ? "filterBtnActive" : ""}`}>Adult</button>
        </Link>
        <Link href="/sb/?audience=kids">
          <button className={`filterBtn ${audience === "kids" ? "filterBtnActive" : ""}`}>Kids</button>
        </Link>
      </div>

      {cantos.length === 0 ? (
        <div style={{ opacity: 0.8 }}>No SB quizzes added yet.</div>
      ) : (
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))", gap: 12 }}>
          {cantos.map((c) => (
            <a
              key={c}
              href={`/sb/${c}/?audience=${audience}`}
              style={{
                padding: 14,
                border: "1px solid #ddd",
                borderRadius: 10,
                textDecoration: "none",
                color: "inherit",
              }}
            >
              <div style={{ fontWeight: 800 }}>Canto {c}</div>
              <div style={{ opacity: 0.8 }}>Browse chapters</div>
            </a>
          ))}
        </div>
      )}

      <div style={{ marginTop: 18 }}>
        <Link href="/">Back to home</Link>
      </div>
    </main>
  );
}
