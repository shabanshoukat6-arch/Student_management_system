
document.addEventListener("DOMContentLoaded", function () {
    const themeSelect = document.getElementById("themeSelect");
    const root = document.documentElement;

    const availableThemes = [
        "midnight-purple",
        "ocean-blue",
        "emerald-green",
        "rose-pink",
        "black-gold"
    ];

    function applyTheme(theme) {
        if (!availableThemes.includes(theme)) {
            theme = "midnight-purple";
        }

        root.setAttribute("data-theme", theme);
        themeSelect.value = theme;

        try {
            localStorage.setItem("studentSystemTheme", theme);
        } catch (error) {
            // Theme still works for the current page.
        }
    }

    let savedTheme = "midnight-purple";

    try {
        savedTheme =
            localStorage.getItem("studentSystemTheme") ||
            "midnight-purple";
    } catch (error) {
        savedTheme = "midnight-purple";
    }

    applyTheme(savedTheme);

    themeSelect.addEventListener("change", function () {
        applyTheme(this.value);
    });
});
