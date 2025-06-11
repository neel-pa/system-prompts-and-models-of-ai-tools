// Basic scroll animation for features
window.addEventListener('scroll', () => {
    const features = document.querySelectorAll('.feature');
    features.forEach(feature => {
        const rect = feature.getBoundingClientRect();
        if (rect.top < window.innerHeight - 100) {
            feature.classList.add('visible');
        }
    });
});
