%global puzzleset technopol
%global srcname puzzle-sets-%{puzzleset}

Name:           crosswords-%{srcname}
Version:        0.1.0
Release:        %autorelease
Summary:        Polish crosswords downloader from TECHNOPOL for GNOME Crosswords

License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/miku/%{srcname}
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
Requires:       python3dist(beautifulsoup4)
Requires:       python3dist(requests)

%description
This repo contains Polish puzzle set downloaders for GNOME Crosswords. The
puzzles are pulled from TECHNOPOL and converted to ipuz format supported
by Crosswords.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install

install -Dpm0755 technopol.py %{buildroot}%{_bindir}/technopol-downloader

%check
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/org.gnome.Crosswords.PuzzleSets.%{puzzleset}.metainfo.xml

%files
%license COPYING
%doc README.md
%{_bindir}/technopol-downloader
%{_datadir}/crosswords/puzzle-sets/%{puzzleset}/
%{_metainfodir}/org.gnome.Crosswords.PuzzleSets.%{puzzleset}.metainfo.xml

%changelog
%autochangelog
