Name:           beets
Version:        2.3.1
Release:        %autorelease
Summary:        Music library manager and MusicBrainz tagger
License:        MIT and ISC
URL:            http://pypi.org/project/beets/
Source0:        %{pypi_source beets}

BuildRequires:  poetry
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  python3-pydata-sphinx-theme
BuildRequires:  python3-PyYAML
BuildRequires:  python3-mediafile
BuildRequires:  python3-musicbrainzngs >= 0.4
BuildRequires:  python3-munkres
BuildRequires:  python3-mutagen >= 1.23
BuildRequires:  python3-unidecode
BuildRequires:  python3-rarfile
BuildRequires:  python3-pip


# Tests
BuildRequires:  python-jellyfish
BuildRequires:  gstreamer1-plugins-good
BuildRequires:  python-responses
BuildRequires:  python-mock
BuildRequires:  pytest
BuildRequires:  python-pytest-timeout

BuildRequires:  make
BuildArch:      noarch

Requires:       python3 >= 3.8
Requires:       python3-confuse
Requires:       python3-jellyfish
Requires:       python3-mediafile >= 0.12.0
Requires:       python3-munkres >= 1.0.0
Requires:       python3-musicbrainzngs >= 0.4
Requires:       python3-mutagen >= 1.23
Requires:       python3-unidecode
Requires:       python3-rarfile
Requires:       python3-PyYAML
Requires:       python3-gstreamer1
Requires:       python3-acoustid
Requires:       python3-requests
Requires:       python3-pylast
Requires:       python3-musicbrainzngs >= 0.4
Requires:       python3-mpd2
Requires:       python3-gobject >= 3.0
Requires:       gstreamer1
Requires:       js-jquery
Requires:       js-backbone
Requires:       js-underscore
Requires:       python3-flask
Requires:       python3-lap

Obsoletes:      beets-plugins < %{version}

BuildSystem: pyproject
BuildOption(install): -l beets

%description
The purpose of beets is to get your music collection right once and for all. It
catalogs your collection, automatically improving its meta-data as it goes using
the MusicBrainz database. Then it provides a bouquet of tools for manipulating
and accessing your music.
Because beets is designed as a library, it can do almost anything you can
imagine for your music collection. Via plugins, beets becomes a panacea:
- Fetch or calculate all the meta-data you could possibly need: album art,
  lyrics, genres, tempos, ReplayGain levels, or acoustic fingerprints.
- Get meta-data from MusicBrainz, Discogs, or Beatport. Or guess meta-data using
  songs' file names or their acoustic fingerprints.
- Transcode audio to any format you like.
- Check your library for duplicate tracks and albums or for albums that are
  missing tracks.
- Browse your music library graphically through a Web browser and play it in
  any browser that supports HTML5 Audio.

%package doc
Summary:        Documentation for beets

%description doc
The beets-doc package provides useful information on the
beets Music Library Manager. Documentation is shipped in
both text and html formats.

%prep
# Tarball has wrong basedir https://github.com/beetbox/beets/issues/5284
%autosetup -p1 -n beets-%{version}

%build
%pyproject_wheel
pushd docs
# Not using {smp_flags} as sphinx fails with it from time to time
make SPHINXBUILD=sphinx-build-3 man html text
popd

%check
%pytest

%install
%pyproject_install
%pyproject_save_files -l beets -L

%files -n beets -f %{pyproject_files}
%{_bindir}/beet
%{python3_sitelib}/beetsplug/
%license LICENSE
%doc README.rst

%changelog
%autochangelog
