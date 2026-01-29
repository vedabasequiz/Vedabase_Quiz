"use client";
import { useState, useEffect } from "react";
import Link from "next/link";
import { useParams, useRouter, useSearchParams } from "next/navigation";
import { getSbAvailability, listSbCantos, listSbChaptersInCanto } from "../../../lib/quizLoader";
import { getQuizResult, formatTimeAgo } from "../../../lib/quizProgress";

// Expand as you publish (ASCII-only)
const SB_CHAPTER_TITLES = {
  1: {
    1: "Questions by the Sages",
    2: "Divinity and Divine Service",
    3: "Krsna Is the Source of All Incarnations",
    4: "The Appearance of Sri Narada",
    5: "Narada's Instructions on Srimad-Bhagavatam for Vyasadeva",
    6: "Conversation Between Narada and Vyasadeva",
    7: "The Son of Drona Punished",
    8: "Prayers by Queen Kunti and Pariksit Saved",
    9: "The Passing Away of Bhismadeva in the Presence of Lord Krsna",
    10: "Departure of Lord Krsna for Dvaraka",
    11: "Lord Krsna's Entrance into Dvaraka",
    12: "Birth of Emperor Pariksit",
    13: "Dhritarastra Quits Home",
    14: "The Disappearance of Lord Krsna",
    15: "The Pandavas Retire Timely",
    16: "How Pariksit Received the Age of Kali",
    17: "Punishment and Reward of Kali",
    18: "Maharaja Pariksit Cursed by a Brahmana Boy",
    19: "The Appearance of Sukadeva Gosvami",
  },
  2: {
    1: "The First Step in God Realization",
    2: "The Lord in the Heart",
    3: "Pure Devotional Service: The Change in Heart",
    4: "The Process of Creation",
    5: "The Cause of All Causes",
    6: "Purusa-sukta Confirmed",
    7: "Scheduled Incarnations with Specific Functions",
    8: "Questions by Vidura",
    9: "Answers by Citing the Lord's Version",
    10: "Bhagavatam Is the Answer to All Questions",
  },
  3: {
    1: "Questions by Vidura",
    2: "Remembrance of Lord Krsna",
    3: "The Lord's Pastimes Out of Vrndavana",
    4: "Vidura Approaches Maitreya",
    5: "Vidura's Talks with Maitreya",
    6: "Creation of the Universal Form",
    7: "Further Inquiries by Vidura",
    8: "Manifestation of Brahma from Garbhodakasayi Visnu",
    9: "Brahma's Prayers for Creative Energy",
    10: "Divisions of the Creation",
    11: "Calculation of Time, from the Atom",
    12: "Creation of the Kumaras and Others",
    13: "The Appearance of Lord Varaha",
    14: "Pregnancy of Diti in the Evening",
    15: "Description of the Kingdom of God",
    16: "The Two Doorkeepers of Vaikuntha, Jaya and Vijaya, Cursed by the Sages",
    17: "Victory of Hiranyaksa Over All the Directions of the Universe",
    18: "The Battle Between Lord Boar and the Demon Hiranyaksa",
    19: "The Killing of the Demon Hiranyaksa",
    20: "Conversation Between Maitreya and Vidura",
    21: "Conversation Between Manu and Kardama",
    22: "The Marriage of Kardama Muni and Devahuti",
    23: "Devahuti's Lamentation",
    24: "The Renunciation of Kardama Muni",
    25: "The Glories of Devotional Service",
    26: "Fundamental Principles of Material Nature",
    27: "Understanding Material Nature",
    28: "Kapila's Instructions on the Execution of Devotional Service",
    29: "Explanation of Devotional Service by Lord Kapila",
    30: "Description by Lord Kapila of Adverse Fruitive Activities",
    31: "Lord Kapila's Instructions on the Movements of the Living Entities",
    32: "Entanglement in Fruitive Activities",
    33: "Activities of Kapila",
  },
  4: {
    1: "Genealogy of the Daughters of Manu",
    2: "Daksa Curses Lord Siva",
    3: "Talks Between Lord Siva and Sati",
    4: "Sati Quits Her Body",
    5: "Frustration of the Sacrifice of Daksa",
    6: "Brahma Satisfies Lord Siva",
    7: "The Sacrifice Performed by Daksa",
    8: "Dhruva Maharaja Leaves Home for the Forest",
    9: "Dhruva Maharaja Returns Home",
    10: "The Battle Between Lord Visnu and the Demons",
    11: "Svayambhuva Manu Advises Dhruva Maharaja to Stop Fighting",
    12: "Dhruva Maharaja Goes Back to Godhead",
    13: "Description of the Descendants of Dhruva Maharaja",
    14: "The Story of King Vena",
    15: "King Prthu's Appearance and Coronation",
    16: "Praise of King Prthu by the Professional Reciters",
    17: "Punishment and Reward of Kali",
    18: "Prthu Maharaja Milks the Earth Planet",
    19: "King Prthu's One Hundred Horse Sacrifices",
    20: "Lord Visnu's Appearance in the Sacrificial Arena of Maharaja Prthu",
    21: "Instructions by Maharaja Prthu",
    22: "Prthu Maharaja's Meeting with the Four Kumaras",
    23: "Lord Prthu's Going Back Home",
    24: "Chanting the Song Sung by Lord Siva",
    25: "The Characteristics of King Puranjana",
    26: "King Puranjana Goes to the Forest to Hunt, and His Queen Becomes Angry",
    27: "Attack by Candavega on the City of King Puranjana; the Character of Kalakanya",
    28: "Puranjana Becomes a Woman in the Next Life",
    29: "Talks Between Narada and King Pracinabarhi",
    30: "The Activities of the Pracetas",
    31: "Narada Instructs the Pracetas",
  },
  5: {
    1: "The Activities of Maharaja Priyavrata",
    2: "The Activities of Maharaja Agnidhra",
    3: "Rsabhadeva's Appearance in the Womb of Merudevi, the Wife of King Nabhi",
    4: "The Characteristics of Rsabhadeva, the Supreme Personality of Godhead",
    5: "Lord Rsabhadeva's Teachings to His Sons",
    6: "The Activities of Lord Rsabhadeva",
    7: "The Activities of King Bharata",
    8: "A Description of the Character of Bharata Maharaja",
    9: "The Supreme Character of Jada Bharata",
    10: "The Discussion Between Jada Bharata and Maharaja Rahugana",
    11: "Jada Bharata Instructs King Rahugana",
    12: "Conversation Between Maharaja Rahugana and Jada Bharata",
    13: "Further Talks Between King Rahugana and Jada Bharata",
    14: "The Material World as the Great Forest of Enjoyment",
    15: "The Glories of the Descendants of King Priyavrata",
    16: "A Description of Jambudvipa",
    17: "The Descent of the River Ganges",
    18: "The Prayers Offered to the Lord by the Residents of Jambudvipa",
    19: "A Description of the Island of Jambudvipa",
    20: "Studying the Structure of the Universe",
    21: "The Movements of the Sun",
    22: "The Orbits of the Planets",
    23: "The Sisumara Planetary Systems",
    24: "The Subterranean Heavenly Planets",
    25: "The Glories of Lord Ananta",
    26: "A Description of the Hellish Planets",
  },
  6: {
    1: "The History of the Life of Ajamila",
    2: "Ajamila Delivered by the Visnudutas",
    3: "Yamaraja Instructs His Messengers",
    4: "The Hamsa-guhya Prayers",
    5: "Narada Muni Cursed by Prajapati Daksa",
    6: "The Progeny of the Daughters of Daksa",
    7: "Indra Offends His Spiritual Master, Brhaspati",
    8: "The Narayana-kavaca Shield",
    9: "Appearance of the Demon Vrtrasura",
    10: "The Battle Between the Demigods and Vrtrasura",
    11: "The Transcendental Qualities of Vrtrasura",
    12: "Vrtrasura's Glorious Death",
    13: "King Citraketu Meets the Supreme Lord",
    14: "King Citraketu's Lamentation",
    15: "The Saints Narada and Angira Instruct King Citraketu",
    16: "King Citraketu Meets the Supreme Lord",
    17: "Mother Parvati Curses Citraketu",
    18: "Diti Vows to Kill King Indra",
    19: "Performing the Pumsavana Ritualistic Ceremony",
  },
  7: {
    1: "The Supreme Lord Is Equal to Everyone",
    2: "Hiranyakasipu, King of the Demons",
    3: "Hiranyakasipu's Plan to Become Immortal",
    4: "Hiranyakasipu Terrorizes the Universe",
    5: "Prahlada Maharaja, the Saintly Son of Hiranyakasipu",
    6: "Prahlada Instructs His Demoniac Schoolmates",
    7: "What Prahlada Learned in the Womb",
    8: "Lord Nrsimhadeva Slays the King of the Demons",
    9: "Prahlada Pacifies Lord Nrsimhadeva with Prayers",
    10: "Prahlada, the Best Among Exalted Devotees",
    11: "The Perfect Society: Four Social Classes",
    12: "The Perfect Society: Four Spiritual Classes",
    13: "The Behavior of a Perfect Person",
    14: "Ideal Family Life",
    15: "Instructions for Civilized Human Beings",
  },
  8: {
    1: "The Manus, Administrators of the Universe",
    2: "The Elephant Gajendra's Crisis",
    3: "Gajendra's Prayers of Surrender",
    4: "Gajendra Returns to the Spiritual World",
    5: "The Demigods Appeal to the Lord for Protection",
    6: "The Demigods and Demons Declare a Truce",
    7: "Lord Siva Saves the Universe by Drinking Poison",
    8: "The Churning of the Milk Ocean",
    9: "The Lord Incarnates as Mohini-murti",
    10: "The Battle Between the Demigods and the Demons",
    11: "King Indra Annihilates the Demons",
    12: "The Mohini-murti Incarnation Bewilders Lord Siva",
    13: "Description of Future Manus",
    14: "The System of Universal Management",
    15: "Bali Maharaja Conquers the Heavenly Planets",
    16: "Executing the Payo-vrata Process of Worship",
    17: "The Supreme Lord Agrees to Become Aditi's Son",
    18: "Lord Vamanadeva, the Dwarf Incarnation",
    19: "Lord Vamanadeva Begs Charity from Bali Maharaja",
    20: "Bali Maharaja Surrenders the Universe",
    21: "Bali Maharaja Arrested by the Lord",
    22: "Bali Maharaja Surrenders His Life",
    23: "The Demigods Regain the Heavenly Planets",
    24: "Matsya, the Lord's Fish Incarnation",
  },
  9: {
    1: "King Sudyumna Becomes a Woman",
    2: "The Dynasties of the Sons of Manu",
    3: "The Marriage of Sukanya and Cyavana Muni",
    4: "Ambarisa Maharaja Offended by Durvasa Muni",
    5: "Durvasa Muni's Life Spared",
    6: "The Downfall of Saubhari Muni",
    7: "The Descendants of King Mandhata",
    8: "The Sons of Sagara Meet Lord Kapiladeva",
    9: "The Dynasty of Amsuman",
    10: "The Pastimes of the Supreme Lord, Ramacandra",
    11: "Lord Ramacandra Rules the World",
    12: "The Dynasty of Kusa, the Son of Lord Ramacandra",
    13: "The Dynasty of Maharaja Nimi",
    14: "King Pururava Enchanted by Urvasi",
    15: "Parashurama, the Lord's Warrior Incarnation",
    16: "Lord Parashurama Destroys the World's Ruling Class",
    17: "The Dynasties of the Sons of Pururava",
    18: "King Yayati Regains His Youth",
    19: "King Yayati Achieves Liberation",
    20: "The Dynasty of Puru",
    21: "The Dynasty of Bharata",
    22: "The Descendants of Ajamidha",
    23: "The Dynasties of the Sons of Yayati",
    24: "Krsna, the Supreme Personality of Godhead",
  },
  10: {
    1: "The Advent of Lord Krsna: Introduction",
    2: "Prayers by the Demigods for Lord Krsna in the Womb",
    3: "The Birth of Lord Krsna",
    4: "The Atrocities of King Kamsa",
    5: "The Meeting of Nanda Maharaja and Vasudeva",
    6: "The Killing of the Demon Putana",
    7: "The Killing of the Demon Trnavarta",
    8: "Lord Krsna Shows the Universal Form Within His Mouth",
    9: "Mother Yasoda Binds Lord Krsna",
    10: "Deliverance of the Yamala-arjuna Trees",
    11: "The Childhood Pastimes of Krsna",
    12: "The Killing of the Demon Aghasura",
    13: "The Stealing of the Boys and Calves by Brahma",
    14: "Brahma's Prayers to Lord Krsna",
    15: "The Killing of Dhenuka, the Ass Demon",
    16: "Krsna Chastises the Serpent Kaliya",
    17: "The History of Kaliya",
    18: "Lord Balarama Slays the Demon Pralamba",
    19: "Swallowing the Forest Fire",
    20: "The Rainy Season and Autumn in Vrndavana",
    21: "The Gopis Glorify the Song of Krsna's Flute",
    22: "Krsna Steals the Garments of the Unmarried Gopis",
    23: "Delivering the Wives of the Brahmanas Who Performed Sacrifices",
    24: "Worshiping Govardhana Hill",
    25: "Lord Krsna Lifts Govardhana Hill",
    26: "Wonderful Krsna",
    27: "Lord Indra and Mother Surabhi Offer Prayers",
    28: "Krsna Rescues Nanda Maharaja from the Abode of Varuna",
    29: "Krsna and the Gopis Dance the Rasa Dance",
    30: "The Gopis Search for Krsna",
    31: "The Gopis' Songs of Separation",
    32: "The Reunion",
    33: "Description of the Rasa Dance",
    34: "The Gopas and Gopis Glorify Krsna",
    35: "The Gopis Sing of Krsna as He Wanders in the Forest",
    36: "The Slaying of Arista, the Bull Demon",
    37: "The Killing of the Demons Kesí and Vyoma",
    38: "Akrura's Arrival in Vrndavana",
    39: "Akrura's Vision",
    40: "The Prayers of Akrura",
    41: "Krsna and Balarama in Mathura",
    42: "The Breaking of the Bow in the Sacrificial Arena",
    43: "The Killing of the Elephant Kuvalayapida",
    44: "The Killing of Kamsa",
    45: "Krsna Rescues His Teacher's Son",
    46: "Uddhava Visits Vrndavana",
    47: "The Song of the Bee",
    48: "Krsna Pleases His Devotees",
    49: "Akrura's Mission in Hastinapura",
    50: "Krsna Establishes Friendship with Arjuna",
    51: "The Deliverance of Mucukunda",
    52: "Rukmini's Message to Lord Krsna",
    53: "Krsna Kidnaps Rukmini",
    54: "The Marriage of Krsna and Rukmini",
    55: "The History of Pradyumna",
    56: "The Syamantaka Jewel",
    57: "Satrájit Murdered, the Jewel Returned",
    58: "Krsna Marries Five Princesses",
    59: "The Killing of the Demon Naraka",
    60: "Lord Krsna Teases Queen Rukmini",
    61: "Lord Balarama Slays Rukmí",
    62: "The Meeting of Usa and Aniruddha",
    63: "Lord Krsna Fights with Bánásura",
    64: "The Deliverance of King Nrga",
    65: "Lord Balarama Visits Vrndavana",
    66: "Paundraka, the False Vasudeva",
    67: "Lord Balarama Slays Dantavakra",
    68: "The Marriage of Samba",
    69: "Narada Muni Visits Lord Krsna's Palaces in Dvaraka",
    70: "Lord Krsna's Daily Activities",
    71: "The Lord Travels to Indraprastha",
    72: "The Slaying of the Demon Jarasandha",
    73: "Lord Krsna Blesses the Liberated Kings",
    74: "The Deliverance of Sisupala at the Rajasuya Sacrifice",
    75: "Duryodhana Humiliated",
    76: "The Battle Between Salva and the Vrsnis",
    77: "Lord Krsna Slays the Demon Salva",
    78: "The Killing of Dantavakra, Viduratha and Romaharsana",
    79: "Lord Balarama Goes on Pilgrimage",
    80: "The Brahmana Sudama Visits Lord Krsna in Dvaraka",
    81: "The Lord Blesses Sudama Brahmana",
    82: "Krsna and Balarama Meet the Inhabitants of Vrndavana",
    83: "Draupadi Meets the Queens of Krsna",
    84: "The Sages' Teachings at Kuruksetra",
    85: "Lord Krsna Instructs Vasudeva and Retrieves Devaki's Sons",
    86: "Arjuna Kidnaps Subhadra, and Krsna Blesses His Devotees",
    87: "The Prayers of the Personified Vedas",
    88: "Lord Siva Saved from Vrkasura",
    89: "Krsna and Arjuna Retrieve a Brahmana's Sons",
    90: "Summary of Lord Krsna's Glories",
  },
  11: {
    1: "The Curse Upon the Yadu Dynasty",
    2: "Krsna and Uddhava",
    3: "Liberation from the Duality of Love and Hate",
    4: "Drumila Explains the Incarnations of Godhead to King Nimi",
    5: "Narada Concludes His Teachings to Vasudeva",
    6: "The Yadu Dynasty Retires to Prabhasa",
    7: "Lord Krsna Instructs Uddhava",
    8: "The Story of Pingala",
    9: "Detachment from All That Is Material",
    10: "The Nature of Fruitive Activity",
    11: "The Symptoms of Conditioned and Liberated Living Entities",
    12: "Beyond Renunciation and Knowledge",
    13: "The Hamsa-avatara Answers the Questions of the Sons of Brahma",
    14: "Lord Krsna Explains the Yoga System to Sri Uddhava",
    15: "Lord Krsna's Description of Mystic Yoga Perfections",
    16: "The Lord's Opulence",
    17: "Lord Krsna's Description of the Varnasrama System",
    18: "Description of Varnasrama-dharma",
    19: "The Perfection of Spiritual Knowledge",
    20: "Pure Devotional Service Surpasses Knowledge and Detachment",
    21: "The Behavior of a Perfect Person",
    22: "Enumeration of the Elements of Material Creation",
    23: "The Song of the Avanti Brahmana",
    24: "The Philosophy of Sankhya",
    25: "The Three Modes of Nature and Beyond",
    26: "The Aila-gita",
    27: "Lord Krsna's Instructions on the Process of Deity Worship",
    28: "Jnana-yoga",
    29: "Bhakti-yoga",
    30: "The Stages of Devotional Service",
    31: "The Disappearance of the Yadu Dynasty",
  },
  12: {
    1: "The Degraded Dynasties of Kali-yuga",
    2: "The Symptoms of Kali-yuga",
    3: "The Bhumi-gita",
    4: "The Four Categories of Universal Annihilation",
    5: "Sukadeva Gosvami's Final Instructions to Maharaja Pariksit",
    6: "Maharaja Pariksit Passes Away",
    7: "The Puranic Literatures",
    8: "Markandeya's Prayers to Nara-Narayana Rsi",
    9: "Markandeya Rsi Sees the Illusory Potency of the Lord",
    10: "Lord Siva and Uma Glorify Markandeya Rsi",
    11: "Summary Description of the Mahapurusa",
    12: "The Topics of Srimad-Bhagavatam Summarized",
    13: "The Glories of Srimad-Bhagavatam",
  },
};

function getAudienceFromSearchParams(searchParams) {
  const a = searchParams?.audience;
  const v = Array.isArray(a) ? a[0] : a;
  if (v === "kids" || v === "teens" || v === "adult") return v;
  return "adult";
}

export default function SbCantoPage() {
  const params = useParams();
  const router = useRouter();
  const searchParams = useSearchParams();
  const audience = getAudienceFromSearchParams(Object.fromEntries(searchParams));
  const [quizResults, setQuizResults] = useState({});

  useEffect(() => {
    if (!searchParams.get("audience")) {
      router.replace(`/sb/${params.canto}/?audience=adult`);
    }
  }, [searchParams, router, params.canto]);

  useEffect(() => {
    try {
      const stored = localStorage.getItem("vedabaseQuizResults");
      if (stored) setQuizResults(JSON.parse(stored));
    } catch (e) {
      // Ignore localStorage errors
    }
  }, []);

  const cantoNum = Number(params.canto);
  const audience = getAudienceFromSearchParams(searchParams);
  const audienceLabel = audience.charAt(0).toUpperCase() + audience.slice(1);

  const availability = getSbAvailability();

  // Define chapter counts per canto
  const CHAPTERS_PER_CANTO = {
    1: 19,
    2: 10,
    3: 33,
    4: 31,
    5: 26,
    6: 19,
    7: 15,
    8: 24,
    9: 24,
    10: 90,
    11: 31,
    12: 13,
  };

  const totalChapters = CHAPTERS_PER_CANTO[cantoNum] || 5;
  const chapters = Array.from({ length: totalChapters }, (_, i) => i + 1);

  function linkFor(chapter, aud) {
    const key = `${cantoNum}/${chapter}-${aud}`;
    const meta = availability.get(key);
    return meta ? `/quiz/${meta.slug}/` : null;
  }

  function titleFor(canto, chapter) {
    return SB_CHAPTER_TITLES[canto]?.[chapter] || "";
  }

  return (
    <main style={{ maxWidth: 900, margin: "0 auto", padding: "24px 16px" }}>
      {/* Breadcrumb (consistent with BG) */}
      <div style={{ fontSize: 14, opacity: 0.8, marginBottom: 10 }}>
        <Link href="/">Home</Link>
        <span style={{ opacity: 0.6 }}> / </span>
        <Link href={`/sb/?audience=${audience}`}>Srimad Bhagavatam</Link>
        <span style={{ opacity: 0.6 }}> / </span>
        <span>Canto {cantoNum}</span>
        <span style={{ opacity: 0.6 }}> / </span>
        <span>{audienceLabel}</span>
      </div>

      <h1 style={{ fontSize: 28, margin: "0 0 10px" }}>Srimad Bhagavatam</h1>
      <div style={{ opacity: 0.8, marginBottom: 8 }}>Canto {cantoNum}</div>

      {/* Tabs (match BG) */}
      <div className="filterBar" style={{ marginTop: 10, marginBottom: 18 }}>
        <Link href={`/sb/${cantoNum}/?audience=adult`}>
          <button className={`filterBtn ${audience === "adult" ? "filterBtnActive" : ""}`}>Adult</button>
        </Link>
        <Link href={`/sb/${cantoNum}/?audience=teens`}>
          <button className={`filterBtn ${audience === "teens" ? "filterBtnActive" : ""}`}>Teens</button>
        </Link>
        <Link href={`/sb/${cantoNum}/?audience=kids`}>
          <button className={`filterBtn ${audience === "kids" ? "filterBtnActive" : ""}`}>Kids</button>
        </Link>
      </div>

      {/* Cards (same as BG) */}
      <div className="chapterGrid">
        {chapters.map((ch) => {
          const selectedUrl = linkFor(ch, audience);
          const isAvailable = !!selectedUrl;
          const title = titleFor(cantoNum, ch);
          
          // Get quiz result for this chapter
          const slug = selectedUrl ? selectedUrl.replace(/^\/quiz\//, "").replace(/\/$/, "") : null;
          const result = slug ? quizResults[slug] : null;

          const cardInner = (
            <div className={`chapterCard ${isAvailable ? "" : "chapterCardDisabled"} ${result ? "chapterCardCompleted" : ""}`}>
              <div>
                <div style={{ fontWeight: 800, marginBottom: 8 }}>Chapter {ch}</div>
                {title ? <div className="chapterTitle">{title}</div> : null}
                
                {/* Progress badge */}
                {result && (
                  <div style={{ marginTop: 8, fontSize: 13 }}>
                    <div className="completionBadge">
                      ✓ {result.score}/{result.total} ({result.percentage}%)
                    </div>
                    <div className="lastPlayed">{formatTimeAgo(result.date)}</div>
                  </div>
                )}
              </div>

              {!isAvailable ? (
                <div className="comingSoonBadge">{audienceLabel}: coming soon</div>
              ) : (
                <div />
              )}
            </div>
          );

          return isAvailable ? (
            <Link key={ch} href={selectedUrl} className="cardLink">
              {cardInner}
            </Link>
          ) : (
            <div key={ch} className="cardLink cardLinkDisabled">
              {cardInner}
            </div>
          );
        })}
      </div>

      <div style={{ marginTop: 18 }}>
        <Link href={`/sb/?audience=${audience}`}>Back to cantos</Link>
      </div>
    </main>
  );
}
