document.addEventListener('DOMContentLoaded', function() {
    const artistDropdown = document.getElementById('artist-dropdown');
    const artistSearch = document.getElementById('artist-search');

    artistSearch.addEventListener('input', function() {
        const query = artistSearch.value;
        if (query.length >= 3) { // Fetch artists if search query is 3 or more characters
            fetchArtists(query);
        }
    });

    async function fetchArtists(query) {
        const response = await fetch(`https://musicbrainz.org/ws/2/artist?query=${query}&fmt=json`);
        const data = await response.json();
        populateDropdown(data.artists);
    }

    function populateDropdown(artists) {
        artistDropdown.innerHTML = '<option value="">--Select an artist--</option>';
        artists.forEach(artist => {
            const option = document.createElement('option');
            option.value = artist.id;
            option.textContent = artist.name;
            artistDropdown.appendChild(option);
        });
    }
});
