Name:           beets
Version:        2.5.1
Release:        %autorelease
Summary:        Music library manager and MusicBrainz tagger
License:        MIT and ISC
URL:            http://pypi.org/project/beets/
Source0:        %{pypi_source beets}

BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3-pydata-sphinx-theme
BuildRequires:  python3dist(poetry-core) >= 1
# Sphinx extras used by upstream docs
BuildRequires:  python3dist(sphinxcontrib-htmlhelp)
BuildRequires:  python3dist(sphinxcontrib-serializinghtml)
BuildRequires:  python-sphinx-design
BuildRequires:  python-sphinx-copybutton

# Tests
BuildRequires:  python3-jellyfish
BuildRequires:  gstreamer1-plugins-good
BuildRequires:  python3-responses
BuildRequires:  python3-mock
BuildRequires:  pytest
BuildRequires:  python3-pytest-timeout

BuildRequires:  make
BuildArch:      noarch

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

%package doc
Summary:        Documentation for beets

%description doc
The beets-doc package provides useful information on the
beets Music Library Manager. Documentation is shipped in
both text and html formats.

%prep
# Tarball has wrong basedir https://github.com/beetbox/beets/issues/5284
%autosetup -p1 -n beets-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

pushd docs
env PYTHONPATH=.. sphinx-build-3 -b man  -d _build/doctrees . _build/man
env PYTHONPATH=.. sphinx-build-3 -b html -d _build/doctrees . _build/html
env PYTHONPATH=.. sphinx-build-3 -b text -d _build/doctrees . _build/text
popd

%check
# Minimal sanity: upstream sets __version__ in 2.5.1
PYTHONPATH=. python3 - <<'PY'
import beets
assert beets.__version__ == "%{version}", f"got {beets.__version__}"
PY

%pytest \
  --deselect test/test_importer.py::ImportDuplicateAlbumTest::test_merge_duplicate_album

%install
%pyproject_install
%pyproject_save_files -l beets beetsplug -L
install -Dm0644 docs/_build/man/beet.1 \
  %{buildroot}%{_mandir}/man1/beet.1
install -Dm0644 docs/_build/man/beetsconfig.5 \
  %{buildroot}%{_mandir}/man5/beetsconfig.5
# Copy only HTML docs
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -a docs/_build/html %{buildroot}%{_docdir}/%{name}/html
rm -f %{buildroot}%{_docdir}/%{name}/html/.buildinfo

%files -n beets -f %{pyproject_files}
%{_bindir}/beet
%{_mandir}/man1/beet.1*
%{_mandir}/man5/beetsconfig.5*
%license LICENSE
%doc README.rst

%files doc
%doc %{_docdir}/%{name}/html
%license LICENSE

%autochangelog
