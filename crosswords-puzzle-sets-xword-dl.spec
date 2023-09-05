%global puzzleset xword-dl
%global srcname puzzle-sets-%{puzzleset}

Name:           crosswords-%{srcname}
Version:        0.4.4
Release:        %autorelease
Summary:        Puzzle Sets from assorted newspapers for GNOME Crosswords

License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/jrb/%{srcname}
Source:         %{url}/-/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  gcc
BuildRequires:  libappstream-glib
BuildRequires:  meson

BuildRequires:  glib2-devel
BuildRequires:  json-glib-devel

Requires:       crosswords
Supplements:    crosswords

# For the downloader script
Requires:       python3-xword-dl

# Replace puzzlepull which has been merged into xword-dl
Provides:       crosswords-puzzle-sets-puzzlepull = %{version}-%{release}
Obsoletes:      crosswords-puzzle-sets-puzzlepull < 0.3.0-2

%description
Download crossword puzzles for GNOME Crosswords from assorted newspapers using
xword-dl.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install

%check
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/org.gnome.Crosswords.PuzzleSets.%{puzzleset}.metainfo.xml

%files
%license COPYING
%doc README.md
%{_datadir}/crosswords/puzzle-sets/%{puzzleset}
%{_metainfodir}/org.gnome.Crosswords.PuzzleSets.%{puzzleset}.metainfo.xml

%changelog
%autochangelog
