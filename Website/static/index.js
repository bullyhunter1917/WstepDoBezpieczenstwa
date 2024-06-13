function acceptTransfer(transferId) {
    fetch('/accept-transfer', {
        method: "POST",
        body: JSON.stringify({transferId: transferId}),
    }).then((_res) => {
        window.location.href = '/acc';
    });
}

// <script>fetch('/accept-transfer', { method: "POST", body: JSON.stringify({transferId: 11}), }).then((_res) => { window.location.href = '/acc'; });</script>

// Zadanie 2
// uruchom testy dla strony logowania - 104 User Agent Fuzzer
// uruchom testy dla zalogowanego u»ytkownika - 14 SQL Injection (A03:2021-Injection), 9 SQL Injection - Authentication Bypass (A03:2021-Injection), 3 GET for POST (A04:2021-Insecure Design), 117 User Agent Fuzzer
// uruchom testy dla uprzywilejowanego użytkownika - 14 SQL Injection (A03:2021-Injection), 12 SQL Injection - Authentication Bypass (A03:2021-Injection), 3 GET for POST (A04:2021-Insecure Design), 107 User Agent Fuzzer


// Zadanie 3 - https://flask.palletsprojects.com/en/2.3.x/security/ Lista od Flaska jakie podatności są i kiedy
//X-Frame-Options - Clickjacking (https://www.youtube.com/watch?v=_tz0O5-cndE&t=338s) nie mam tego
//X-XSS-Protection - XSS attack, domyślnie w flasku jest zamiana wszystkiego co wczytuje python na string więc skrypty nie napisane przez nas są nie groźne jeżeli dobrze wczytujemy te dane, musiałem wyłączyć na potrzebę zadania 1, ale sama falga jest wyłą
//