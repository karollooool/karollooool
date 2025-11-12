<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Profile (icons row)</title>

  <style>
    /* Page layout */
    :root{
      --bg:#0e1518;
      --panel:#0b0f12;
      --muted:#9aa3ab;
      --line:#262b2f;
      --accent:#e6e9ee;
    }

    html,body{height:100%;}
    body{
      margin:0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial;
      background:linear-gradient(180deg,var(--bg), #071018);
      color:var(--accent);
      -webkit-font-smoothing:antialiased;
      -moz-osx-font-smoothing:grayscale;
      display:flex;
      align-items:flex-start;
      justify-content:center;
      padding:36px 16px;
    }

    /* Container similar to screenshot */
    .card{
      width:920px;
      max-width:100%;
      background:transparent;
      border-left:1px solid rgba(255,255,255,0.02);
      border-right:1px solid rgba(255,255,255,0.02);
      padding:22px 34px;
      box-sizing:border-box;
    }

    header h1{
      margin:0 0 14px;
      text-align:center;
      font-size:28px;
      font-weight:700;
    }

    hr.section-sep{
      border:0;
      height:1px;
      background:var(--line);
      margin:10px 0 18px;
      opacity:0.9;
    }

    /* About section */
    .about{
      padding:8px 0 14px;
      border-top:1px solid var(--line);
      border-bottom:1px solid transparent;
    }
    .about h2{
      display:flex;
      gap:8px;
      align-items:center;
      font-size:18px;
      margin:14px 0;
    }

    .about ul{
      margin:10px 0 0 0;
      padding:0 0 14px 0;
      list-style:none;
      color:var(--muted);
      font-size:14px;
      line-height:1.6;
    }
    .about li{margin:6px 0; white-space:pre-line;}

    /* I code with area */
    .code-with{
      margin-top:8px;
      padding-top:16px;
      border-top:1px solid var(--line);
    }

    .code-with h3{
      display:flex;
      align-items:center;
      gap:10px;
      font-size:18px;
      margin:6px 0 12px;
    }

    /* Icon row */
    .icons{
      display:flex;
      align-items:center;
      gap:14px;              /* spacing between icons */
      padding:10px 0 22px;
    }

    /* Each icon box controls size */
    .icon{
      width:44px;            /* change these values to scale icons */
      height:44px;
      display:inline-flex;
      align-items:center;
      justify-content:center;
      background:transparent;
      border-radius:8px;
      transition:transform .12s ease, opacity .12s ease;
      opacity:0.98;
    }

    /* Allow using <img> or inline <svg> inside .icon */
    .icon svg, .icon img{
      width:100%;
      height:100%;
      display:block;
    }

    .icon:hover{ transform:translateY(-4px); opacity:1; }

    /* small helper for caption/legend */
    .muted { color:var(--muted); font-size:13px; margin-top:4px; }
  </style>
</head>
<body>
  <main class="card" role="main" aria-label="Profile">
    <header>
      <h1>Welcome to my profile !</h1>
    </header>

    <div class="about" aria-labelledby="about-heading">
      <h2 id="about-heading">🔗 💬 About me</h2>
      <ul>
        <li>🎓 20 years old</li>
        <li>📚 Bachelor in Computer Science at Laval University</li>
        <li>🛠️ Actual Project : Monbot, an AI Rocket League Bot</li>
        <li>🎯 Goal : Mastering C++</li>
      </ul>
    </div>

    <section class="code-with" aria-labelledby="code-heading">
      <h3 id="code-heading">👨‍💻 I code with</h3>

      <div class="icons" role="list" aria-label="programming-icons">
        <!-- Icon 1: first SVG from user's message -->
        <div class="icon" title="Icon 1">
          <svg viewBox="0 0 128 128" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">
            <path fill="#00599c" d="M118.766 95.82c.89-1.543 1.441-3.28 1.441-4.843V36.78c0-1.558-.55-3.297-1.441-4.84l-55.32 31.94Zm0 0"/>
            <path fill="#004482" d="m68.36 126.586 46.933-27.094c1.352-.781 2.582-2.129 3.473-3.672l-55.32-31.94L8.12 95.82c.89 1.543 2.121 2.89 3.473 3.672l46.933 27.094c2.703 1.562 7.13 1.562 9.832 0Zm0 0"/>
            <path fill="#659ad2" d="M118.766 31.941c-.891-1.546-2.121-2.894-3.473-3.671L68.359 1.172c-2.703-1.563-7.129-1.563-9.832 0L11.594 28.27C8.89 29.828 6.68 33.66 6.68 36.78v54.196c0 1.562.55 3.3 1.441 4.843L63.445 63.88Zm0 0"/>
            <path fill="#fff" d="M63.445 26.035c-20.867 0-37.843 16.977-37.843 37.844s16.976 37.844 37.843 37.844c13.465 0 26.024-7.247 32.77-18.91L79.84 73.335c-3.38 5.84-9.66 9.465-16.395 9.465-10.433 0-18.922-8.488-18.922-18.922 0-10.434 8.49-18.922 18.922-18.922 6.73 0 13.017 3.629 16.39 9.465l16.38-9.477c-6.75-11.664-19.305-18.91-32.77-18.91zM92.88 57.57v4.207h-4.207v4.203h4.207v4.207h4.203V65.98h4.203v-4.203h-4.203V57.57H92.88zm15.766 0v4.207h-4.204v4.203h4.204v4.207h4.207V65.98h4.203v-4.203h-4.203V57.57h-4.207z"/>
          </svg>
        </div>

        <!-- Icon 2: simple circular avatar-like SVG (from user's message) -->
        <div class="icon" title="Icon 2">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" aria-hidden="true" focusable="false">
            <path fill="#a9bacd" d="M125 50c-4-32-24-50-62-50C29 0 3 24 3 64c0 39 24 64 64 64 32 0 55-19 58-50H87c-2 11-8 20-20 20-21 0-24-16-24-33 0-23 8-35 22-35 13 0 20 7 22 20z" />
          </svg>
        </div>

        <!-- Icon 3: colorful multi-path SVG (from user's message) -->
        <div class="icon" title="Icon 3">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" aria-hidden="true" focusable="false">
            <path fill="#0074BD" d="M47.617 98.12s-4.767 2.774 3.397 3.71c9.892 1.13 14.947.968 25.845-1.092 0 0 2.871 1.795 6.873 3.351-24.439 10.47-55.308-.607-36.115-5.969zm-2.988-13.665s-5.348 3.959 2.823 4.805c10.567 1.091 18.91 1.18 33.354-1.6 0 0 1.993 2.025 5.132 3.131-29.542 8.64-62.446.68-41.309-6.336z"/>
            <path fill="#EA2D2E" d="M69.802 61.271c6.025 6.935-1.58 13.17-1.58 13.17s15.289-7.891 8.269-17.777c-6.559-9.215-11.587-13.792 15.635-29.58 0 .001-42.731 10.67-22.324 34.187z"/>
            <path fill="#0074BD" d="M102.123 108.229s3.529 2.91-3.888 5.159c-14.102 4.272-58.706 5.56-71.094.171-4.451-1.938 3.899-4.625 6.526-5.192 2.739-.593 4.303-.485 4.303-.485-4.953-3.487-32.013 6.85-13.743 9.815 49.821 8.076 90.817-3.637 77.896-9.468zM49.912 70.294s-22.686 5.389-8.033 7.348c6.188.828 18.518.638 30.011-.326 9.39-.789 18.813-2.474 18.813-2.474s-3.308 1.419-5.704 3.053c-23.042 6.061-67.544 3.238-54.731-2.958 10.832-5.239 19.644-4.643 19.644-4.643zm40.697 22.747c23.421-12.167 12.591-23.86 5.032-22.285-1.848.385-2.677.72-2.677.72s.688-1.079 2-1.543c14.953-5.255 26.451 15.503-4.823 23.725 0-.002.359-.327.468-.617z"/>
            <path fill="#EA2D2E" d="M76.491 1.587S89.459 14.563 64.188 34.51c-20.266 16.006-4.621 25.13-.007 35.559-11.831-10.673-20.509-20.07-14.688-28.815C58.041 28.42 81.722 22.195 76.491 1.587z"/>
            <path fill="#0074BD" d="M52.214 126.021c22.476 1.437 57-.8 57.817-11.436 0 0-1.571 4.032-18.577 7.231-19.186 3.612-42.854 3.191-56.887.874 0 .001 2.875 2.381 17.647 3.331z"/>
          </svg>
        </div>

        <!-- Icon 4: you can duplicate or add other icons here; using Icon 1 again as an example -->
        <div class="icon" title="Icon 4">
          <svg viewBox="0 0 128 128" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">
            <path fill="#00599c" d="M118.766 95.82c.89-1.543 1.441-3.28 1.441-4.843V36.78c0-1.558-.55-3.297-1.441-4.84l-55.32 31.94Zm0 0"/>
            <path fill="#004482" d="m68.36 126.586 46.933-27.094c1.352-.781 2.582-2.129 3.473-3.672l-55.32-31.94L8.12 95.82c.89 1.543 2.121 2.89 3.473 3.672l46.933 27.094c2.703 1.562 7.13 1.562 9.832 0Zm0 0"/>
            <path fill="#659ad2" d="M118.766 31.941c-.891-1.546-2.121-2.894-3.473-3.671L68.359 1.172c-2.703-1.563-7.129-1.563-9.832 0L11.594 28.27C8.89 29.828 6.68 33.66 6.68 36.78v54.196c0 1.562.55 3.3 1.441 4.843L63.445 63.88Zm0 0"/>
            <path fill="#fff" d="M63.445 26.035c-20.867 0-37.843 16.977-37.843 37.844s16.976 37.844 37.843 37.844c13.465 0 26.024-7.247 32.77-18.91L79.84 73.335c-3.38 5.84-9.66 9.465-16.395 9.465-10.433 0-18.922-8.488-18.922-18.922 0-10.434 8.49-18.922 18.922-18.922 6.73 0 13.017 3.629 16.39 9.465l16.38-9.477c-6.75-11.664-19.305-18.91-32.77-18.91zM92.88 57.57v4.207h-4.207v4.203h4.207v4.207h4.203V65.98h4.203v-4.203h-4.203V57.57H92.88zm15.766 0v4.207h-4.204v4.203h4.204v4.207h4.207V65.98h4.203v-4.203h-4.203V57.57h-4.207z"/>
          </svg>
        </div>
      </div>

      <div class="muted">Tip: change the .icon width/height to scale all icons at once (e.g. 32px or 48px).</div>
    </section>
  </main>
</body>
</html>
