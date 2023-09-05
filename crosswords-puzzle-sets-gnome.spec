%global puzzleset gnome
%global srcname puzzle-sets-%{puzzleset}

Name:           crosswords-%{srcname}
Version:        0.4.2
Release:        %autorelease
Summary:        Extra puzzles to go with GNOME Crosswords

# Code is under GPL-3.0-or-later, puzzles are under CC-BY-SA-4.0
License:        GPL-3.0-or-later and CC-BY-SA-4.0
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

%description
This package is for collecting the great puzzles put out by crossword
authors to go with GNOME Crosswords.

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
%license LICENSE COPYING.GPLv3
%doc README.md
%{_datadir}/crosswords/puzzle-sets/%{puzzleset}
%{_metainfodir}/org.gnome.Crosswords.PuzzleSets.%{puzzleset}.metainfo.xml

%changelog
%autochangelog
