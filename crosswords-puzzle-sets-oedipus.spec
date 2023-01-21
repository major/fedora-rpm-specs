%global puzzleset oedipus
%global srcname puzzle-sets-%{puzzleset}

Name:           crosswords-%{srcname}
Version:        0.1.1
Release:        %autorelease
Summary:        Italian puzzle sets from Oedipus for GNOME Crosswords

License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/davide125/%{srcname}
Source:         %{url}/-/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson

BuildRequires:  glib2-devel
BuildRequires:  json-glib-devel

Requires:       crosswords
Supplements:    crosswords

# For the downloader script
Requires:       python3
Requires:       python3dist(puzpy)
Requires:       python3dist(requests)

%description
This repo contains Italian puzzle set downloaders for GNOME Crosswords. The
puzzles are pulled from Oedipus and converted to the ipuz format supported
by Crosswords.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install

install -Dpm0755 puzdownloader-%{puzzleset}.py \
  %{buildroot}%{_libexecdir}/puzdownloader-%{puzzleset}

%check
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/org.gnome.Crosswords.PuzzleSets.%{puzzleset}.metainfo.xml

%files
%license COPYING
%doc README.md
%{_datadir}/crosswords/puzzle-sets/%{puzzleset}
%{_libexecdir}/puzdownloader-%{puzzleset}
%{_metainfodir}/org.gnome.Crosswords.PuzzleSets.%{puzzleset}.metainfo.xml

%changelog
%autochangelog
