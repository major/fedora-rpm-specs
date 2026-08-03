Name:           beets
Version:        2.13.1
Release:        %autorelease
Summary:        Music library manager and MusicBrainz tagger
License:        MIT and ISC
URL:            http://pypi.org/project/beets/
Source0:        %{pypi_source beets}

Patch:          allow-python3.15-build.patch

BuildRequires:  python-requests-ratelimiter

# Tests
BuildRequires:  python3-jellyfish
BuildRequires:  gstreamer1-plugins-good
BuildRequires:  python3-responses
BuildRequires:  pytest
BuildRequires:  python3-pytest-timeout

BuildArch:      noarch

Requires:       python-packaging
Provides:       beets-plugins = %{version}-%{release}
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

%pyproject_extras_subpkg -a -n %{name} aura beatport embedart fetchart lastgenre lastimport lyrics metasync mpdstats reflink scrub tidal thumbnails web

%prep
# Tarball has wrong basedir https://github.com/beetbox/beets/issues/5284
%autosetup -p1 -n beets-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%check
PYTHONPATH=. python3 - <<'PY'
import beets
assert beets.__version__ == "%{version}", f"got {beets.__version__}"
PY

%pytest \
  --deselect test/test_importer.py::ImportDuplicateAlbumTest::test_merge_duplicate_album \
  --deselect test/test_importer.py::ImportTest::test_empty_directory_singleton_warning \
  --deselect test/test_importer.py::ImportTest::test_empty_directory_warning \
  --deselect test/test_importer.py::ImportTest::test_skip_non_album_dirs \
  --ignore test/plugins

%install
%pyproject_install
%pyproject_save_files -l beets beetsplug -L

# Manpages are pre-generated and included in the upstream sdist since 2.13.1.
install -Dm0644 man/beet.1 \
  %{buildroot}%{_mandir}/man1/beet.1
install -Dm0644 man/beetsconfig.5 \
  %{buildroot}%{_mandir}/man5/beetsconfig.5

%files -n beets -f %{pyproject_files}
%{_bindir}/beet
%{_mandir}/man1/beet.1*
%{_mandir}/man5/beetsconfig.5*
%license LICENSE
%doc README.rst

%autochangelog
