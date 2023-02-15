%global app_id  com.bitstower.Markets

Name:           bitstower-markets
Version:        0.5.4
Release:        %autorelease
Summary:        A stock and currency tracker
License:        GPL-3.0-or-later
URL:            https://github.com/tomasz-oponowicz/markets
Source0:        %{url}/archive/%{version}/markets-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires:       hicolor-icon-theme

%description
The Markets application delivers financial data to your fingertips.
Track stocks prices, currency exchange rates, and cryptocurrencies.


%prep
%autosetup -n markets-%{version}


%build
%meson
%meson_build


%install
%meson_install

desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{app_id}.appdata.xml

%find_lang %{app_id}


%files -f %{app_id}.lang
%license COPYING
%doc README.md
%{_bindir}/bitstower-markets
%{_datadir}/appdata/%{app_id}.appdata.xml
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/glib-2.0/schemas/%{app_id}.gschema.xml
%{_datadir}/icons/hicolor/*/*/%{app_id}*


%changelog
%autochangelog
