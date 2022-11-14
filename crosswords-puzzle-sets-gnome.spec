%global puzzleset gnome
%global srcname puzzle-sets-%{puzzleset}
%global date 20221107
%global commit 0bef3d252c097610cd34b65f8704abe87d823d97
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           crosswords-%{srcname}
Version:        0.3.0~%{date}git%{shortcommit}
Release:        %autorelease
Summary:        Extra puzzles to go with GNOME Crosswords

License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/jrb/%{srcname}
Source:         %{url}/-/archive/%{commit}/%{srcname}-%{commit}.tar.gz
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
%autosetup -n %{srcname}-%{commit} -p1

%build
%meson
%meson_build

%install
%meson_install

%check
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/org.gnome.Crosswords.PuzzleSets.%{puzzleset}.metainfo.xml

%files
%doc README.md
%{_datadir}/crosswords/puzzle-sets/%{puzzleset}
%{_metainfodir}/org.gnome.Crosswords.PuzzleSets.%{puzzleset}.metainfo.xml

%changelog
%autochangelog
