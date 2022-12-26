%global puzzleset xword-dl
%global srcname puzzle-sets-%{puzzleset}

%global date 20220905
%global commit 5b233eba14166b5663e1c594b1183c2289433fa2
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           crosswords-%{srcname}
Version:        0.3.0~%{date}git%{shortcommit}
Release:        %autorelease
Summary:        Puzzle Sets from assorted newspapers for GNOME Crosswords

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

# For the downloader script
Requires:       python3-xword-dl

%description
Download crossword puzzles for GNOME Crosswords from assorted newspapers using
xword-dl.

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
%{_datadir}/crosswords/puzzle-sets/%{puzzleset}
%{_metainfodir}/org.gnome.Crosswords.PuzzleSets.%{puzzleset}.metainfo.xml

%changelog
%autochangelog
