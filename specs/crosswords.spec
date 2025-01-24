%bcond docs 1
%bcond tests 1

# The libipuz shared library version
%global ipuz_soversion 0.5

Name:           crosswords
Version:        0.3.14
Release:        %autorelease
Summary:        Solve crossword puzzles

# * crosswords itself is GPL-3.0-or-later
# * the puzzle sets it bundles are CC-BY-SA-4.0
# * the broda word list is LicenseRef-Fedora-UltraPermissive per
#   https://gitlab.com/fedora/legal/fedora-license-data/-/issues/627
# * the wordnik word list is MIT per word-lists/LICENSE.wordnik
License:        GPL-3.0-or-later AND CC-BY-SA-4.0 AND LicenseRef-Fedora-UltraPermissive AND MIT
URL:            https://gitlab.gnome.org/jrb/crosswords
Source:         %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz

# Big endian systems are not supported
# https://jrb.pages.gitlab.gnome.org/crosswords/devel-docs/PACKAGING.html
ExcludeArch:    s390x

BuildRequires:  desktop-file-utils
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  sed
%if %{with docs}
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(myst-parser)
%endif
%if %{with tests}
# gen-word-list requires en_US.UTF8
# https://gitlab.gnome.org/jrb/crosswords/-/issues/109
BuildRequires:  glibc-langpack-en
%endif

BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libipuz-%{ipuz_soversion})
BuildRequires:  pkgconfig(libpanel-1)
BuildRequires:  pkgconfig(librsvg-2.0)

Requires:       dbus-common
Requires:       %{name}-puzzle-sets-cats-and-dogs = %{version}-%{release}
Requires:       %{name}-puzzle-sets-uri = %{version}-%{release}
Recommends:     %{name}-thumbnailer = %{version}-%{release}
Suggests:       crossword-editor = %{version}-%{release}
%if %{with docs}
Suggests:       %{name}-doc = %{version}-%{release}
%endif

%description
A simple and fun game of crosswords. Load your crossword files, or play one of
the included games. Features include:

- Support for shaped and colored crosswords
- Loading .ipuz and .puz files
- Hint support, such as showing mistakes and suggesting words
- Dark mode support
- Locally installed crosswords as well as support for 3rd party downloaders

%package        puzzle-sets-cats-and-dogs
Summary:        Puzzles about cats and dogs for GNOME Crosswords
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    puzzle-sets-cats-and-dogs
This package contains a puzzle set about cats and dogs for GNOME Crosswords.

%package        puzzle-sets-internal
Summary:        Load additional puzzles for GNOME Crosswords
Requires:       %{name} = %{version}-%{release}
Provides:       crosswords-puzzle-sets-uri = %{version}-%{release}
Obsoletes:      crosswords-puzzle-sets-uri < 0.3.6-3
BuildArch:      noarch

# Used to load .puz files from disk
Recommends:     ipuz-convertor = %{version}-%{release}

%description    puzzle-sets-internal
This package contains puzzle sets used internally by GNOME Crosswords to load
additional puzzles from disk.

%package        thumbnailer
Summary:        GNOME Crosswords Thumbnailer

%description    thumbnailer
This package provides a thumbnailer for crosswords puzzles in formats supported
by GNOME Crosswords.

%if %{with docs}
%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
This package contains additional documentation for GNOME Crosswords.
%endif

%package -n     crossword-editor
Summary:        Crossword puzzle editor

Requires:       %{name}%{?_isa} = %{version}-%{release}
Recommends:     %{name}-thumbnailer = %{version}-%{release}
# Used to load .puz files from disk
Recommends:     ipuz-convertor = %{version}-%{release}

%description -n crossword-editor
Standalone-tool to create crossword puzzles based on GNOME Crosswords. It can
be used to create simple puzzles with grids and clues. It has a pattern solver
and grid autofill dialog for filling in hard-to-finish corners, and will make
suggestions of words when creating the grid.

%package -n     ipuz-convertor
Summary:        Converts puz files to ipuz files
BuildArch:      noarch

Requires:       crosswords
Requires:       python3
Requires:       python3dist(beautifulsoup4)
Requires:       python3dist(dateparser)
Requires:       python3dist(lxml)
Requires:       python3dist(puzpy)
Requires:       python3dist(regex)
Requires:       python3dist(requests)
Requires:       python3dist(xdfile)

%description -n ipuz-convertor
ipuz-convertor is a script to convert puzzle files from puz to ipuz.

%prep
%autosetup -p1

# Update image references in README
mkdir images
cp -p data/images/{a-dogs-day,hero}.png images/
sed -i 's:data/images/:images/:g' README.md

# Relax lxml version pin on older releases
%if 0%{?fedora} < 42
sed -i 's:^lxml>=.*:lxml:' requirements.txt
%endif

# Generate Python dependencies for the converter
%generate_buildrequires
%pyproject_buildrequires -N requirements.txt

%build
%meson -Ddevelopment=false
%meson_build

%if %{with docs}
sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%meson_install
%find_lang %{name}

%if %{with tests}
%check
%meson_test

appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/org.gnome.Crosswords.metainfo.xml

desktop-file-validate \
  %{buildroot}/%{_datadir}/applications/org.gnome.Crosswords.desktop \
  %{buildroot}/%{_datadir}/applications/org.gnome.Crosswords.Editor.desktop
%endif

%files -f %{name}.lang
%license COPYING
%doc CONTRIBUTING.md NEWS.md README.md TODO.md images
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/puzzle-sets
%dir %{_datadir}/%{name}/word-lists/
%{_datadir}/%{name}/word-lists/player.gresource
%{_datadir}/applications/org.gnome.Crosswords.desktop
%{_datadir}/dbus-1/services/org.gnome.Crosswords.service
%{_datadir}/glib-2.0/schemas/org.gnome.Crosswords.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Crosswords.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Crosswords-symbolic.svg
%{_datadir}/mime/packages/org.gnome.Crosswords.xml
%{_metainfodir}/org.gnome.Crosswords.metainfo.xml

%if %{with docs}
%files doc
%license COPYING
%doc html
%endif

%files puzzle-sets-cats-and-dogs
%license COPYING
%{_datadir}/%{name}/puzzle-sets/cats-and-dogs

%files puzzle-sets-internal
%license COPYING
%{_datadir}/%{name}/puzzle-sets/*
%exclude %{_datadir}/%{name}/puzzle-sets/cats-and-dogs

%files thumbnailer
%license COPYING
%{_bindir}/%{name}-thumbnailer
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/%{name}.thumbnailer

%files -n crossword-editor
%license word-lists/LICENSE.wordnik
%{_bindir}/crossword-editor
%{_datadir}/%{name}/word-lists/broda.gresource
%{_datadir}/%{name}/word-lists/wordnik.gresource
%{_datadir}/applications/org.gnome.Crosswords.Editor.desktop
%{_datadir}/dbus-1/services/org.gnome.Crosswords.Editor.service
%{_datadir}/glib-2.0/schemas/org.gnome.Crosswords.Editor.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Crosswords.Editor.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Crosswords.Editor-symbolic.svg
%{_metainfodir}/org.gnome.Crosswords.Editor.metainfo.xml

%files -n ipuz-convertor
%license COPYING
%{_datadir}/%{name}/ipuz-convertor
%{_libexecdir}/ipuz-convertor

%changelog
%autochangelog
