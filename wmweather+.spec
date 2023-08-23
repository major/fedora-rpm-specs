%define _legacy_common_support 1
%global commit be2f4b3010e78f7d6c68922db36641ab743f9db9

Name:           wmweather+
Version:        2.18^20211125gitbe2f4b30
Release:        %autorelease
Summary:        Weather status dockapp

License:        GPL-2.0-or-later
URL:            http://sourceforge.net/projects/wmweatherplus/
#Source0:        https://downloads.sourceforge.net/project/wmweatherplus/%%{name}/%%{name}-%%{version}.tar.gz
Source0:	https://sourceforge.net/code-snapshots/git/w/wm/wmweatherplus/git.git/wmweatherplus-git-%{commit}.zip
Patch0: wmweather+-configure-c99.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequireS:  libXpm-devel
BuildRequires:  WINGs-devel
BuildRequires:  pcre2-devel
BuildRequires:  openssl-devel
BuildRequires:  libcurl-devel
BuildRequires:  autoconf automake

%description
wmweather+ will download the National Weather Serivce METAR bulletins; AVN,
ETA, and MRF forecasts; and any weather map for display in a WindowMaker
dockapp. Think wmweather with a smaller font, forecasts, a weather map, and a
sky condition display.

%prep
%autosetup -p1 -n wmweatherplus-git-%{commit}

autoreconf -fvi

%build
%configure
%make_build

%install
%make_install

%files
%doc COPYING README
%{_bindir}/wmweather+
%{_mandir}/man1/*

%changelog
%autochangelog
