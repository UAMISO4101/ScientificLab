function showSponsors(response) {
    var sponsorsList  =$("#selectPatrocinador");
    var sponsor;
    for (var i=0; i <response.length; i++){
        sponsor = response[i];
        sponsorsList.append(new Option(sponsor.fields.nombre, sponsor.pk));
    }
}
