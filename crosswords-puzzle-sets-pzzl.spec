%global puzzleset pzzl
%global srcname puzzle-sets-%{puzzleset}

Name:           crosswords-%{srcname}
Version:        4.1
Release:        %autorelease
Summary:        Dutch puzzle sets from pzzl.net for GNOME Crosswords

License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/philip.goto/%{srcname}
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
Requires:       python3
Requires:       python3dist(python-dateutil)
Requires:       python3dist(requests)

%description
This package contains Dutch puzzle set downloaders for GNOME Crosswords. The
puzzles are pulled from pzzl.net and converted to ipuz format supported by
Crosswords. Right now this puzzle set contains both mini and large puzzles
published on De Telegraaf.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install

install -Dpm0755 ipzzl.py %{buildroot}%{_libexecdir}/ipzzl

%check
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/org.gnome.Crosswords.PuzzleSets.%{puzzleset}.metainfo.xml

%files
%license COPYING
%doc README.md
%{_datadir}/crosswords/puzzle-sets/%{puzzleset}
%{_libexecdir}/ipzzl
%{_metainfodir}/org.gnome.Crosswords.PuzzleSets.%{puzzleset}.metainfo.xml

%changelog
%autochangelog
