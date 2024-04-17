    function showCountryInfo(countryName, button) {
        const countryInfoDiv = button.parentElement.querySelector('.country-info');
        fetch(`http://worldinformationapienv.eba-zcmupdkn.us-east-1.elasticbeanstalk.com/country-info?country=${countryName}`)
            .then(response => response.json())
            .then(data => {
                const countryInfoHTML = `
                    <p><strong>Capital:</strong> ${data.capital}</p>
                    <p><strong>Area:</strong> ${data.area} sq. km</p>
                    <p><strong>Region:</strong> ${data.region}</p>
                    <p><strong>Subregion:</strong> ${data.subregion}</p>
                    <p><strong>Languages:</strong> ${data.languages ? data.languages.join(", ") : 'N/A'}</p>
                `;
                countryInfoDiv.innerHTML = countryInfoHTML;
                countryInfoDiv.style.display = 'block';
            })
            .catch(error => {
                console.error("Error fetching country details:", error);
            });
        }
