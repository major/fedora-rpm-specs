%global appname com.github.avojak.warble

Name:		warble
Version:	1.5.0
Release:	3%{?dist}
Summary:	The word-guessing game

License:	GPLv3+
URL:		https://github.com/avojak/warble
Source:		%{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	cmake
BuildRequires:	meson
BuildRequires:	pkgconfig(gee-0.8)
BuildRequires:	pkgconfig(granite)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libhandy-1)
BuildRequires:	vala
BuildRequires:	/usr/bin/appstream-util
BuildRequires:	/usr/bin/desktop-file-validate

%description
Native Linux word-guessing game built in Vala and Gtk.
Warble is inspired by the recently popular online game Wordle.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{appname}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{appname}.desktop

%files
%license COPYING LICENSE
%doc CONTRIBUTING.md README.md
%{_bindir}/%{appname}
%{_datadir}/%{appname}
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/metainfo/%{appname}.appdata.xml

%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jul 26 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 1.5.0-1
- Update to 1.5.0 (RHBZ #2107457)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0 and Hi-DPI directories fix

* Fri Apr 1 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 1.3.1-1
- new upstream release 1.3.1

* Tue Feb 15 2022 Ali Erdinc Koroglu <ali.erdinc.koroglu@intel.com> - 1.2.0-2
- Hi-DPI directories removed (rhbz#1537318)

* Thu Feb 10 2022 Ali Erdinc Koroglu <ali.erdinc.koroglu@intel.com> - 1.2.0-1
- Initial build.
