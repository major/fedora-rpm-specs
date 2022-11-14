%global puzzleset puzzlepull
%global srcname puzzle-sets-%{puzzleset}

Name:           crosswords-%{srcname}
Version:        0.3.0
Release:        %autorelease
Summary:        The Guardian daily cryptic for GNOME Crosswords

License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/jrb/%{srcname}
Source:         %{url}/-/archive/%{version}/%{srcname}-%{version}.tar.gz
# Add Locale to the puzzleset
Patch:          %{url}/-/commit/aaee6594b3c1e4f7f8e806b2ceaafa4d922731c2.patch
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
Requires:       python3dist(flask)
Requires:       python3dist(ipuz)
Requires:       python3dist(requests)

%description
Download cryptic puzzles from The Guardian to go with GNOME Crosswords.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install

install -Dpm0755 puzzlepull.py %{buildroot}%{_libexecdir}/guardian-downloader

%check
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/org.gnome.Crosswords.PuzzleSets.%{puzzleset}.metainfo.xml

%files
%{_datadir}/crosswords/puzzle-sets/%{puzzleset}
%{_libexecdir}/guardian-downloader
%{_metainfodir}/org.gnome.Crosswords.PuzzleSets.%{puzzleset}.metainfo.xml

%changelog
%autochangelog
