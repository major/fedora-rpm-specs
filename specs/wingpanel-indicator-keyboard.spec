%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global srcname wingpanel-indicator-keyboard
%global appname io.elementary.wingpanel.keyboard

Name:           wingpanel-indicator-keyboard
Summary:        Keyboard Indicator for wingpanel
Version:        2.4.2
Release:        %autorelease
License:        LGPL-2.1-or-later AND GPL-2.0-or-later

URL:            https://github.com/elementary/%{name}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(ibus-1.0) >= 1.5.19
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(wingpanel) >= 3.0.0
BuildRequires:  pkgconfig(xkeyboard-config)

Requires:       wingpanel%{?_isa}
Supplements:    wingpanel%{?_isa}


%description
A keyboard indicator for wingpanel.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang keyboard-indicator


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%files -f keyboard-indicator.lang
%license COPYING
%doc README.md

%{_libdir}/wingpanel/libkeyboard.so

%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.metainfo.xml


%changelog
%autochangelog
