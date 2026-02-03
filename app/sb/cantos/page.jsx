import SbCantoListClient from "../../../components/SbCantoListClient";

export default function SbCantosPage({ searchParams }) {
  const audience = searchParams?.audience || "adult";
  return (
    <main style={{ maxWidth: 900, margin: "0 auto", padding: "24px 16px" }}>
      <SbCantoListClient audience={audience} />
    </main>
  );
}
