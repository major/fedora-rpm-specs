%global appid com.github.hugolabe.Wike

Name:           wike
Version:        1.8.1
Release:        3%{?dist}
Summary:        Wikipedia Reader for the GNOME Desktop

License:        GPLv3
URL:            https://github.com/hugolabe/wike
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Fix _fill_menu bug
# https://github.com/hugolabe/Wike/issues/89
Patch0:         %{url}/pull/90.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  meson
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       hicolor-icon-theme
Requires:       python3-gobject
Requires:       gtk3
Requires:       libhandy1
Requires:       webkit2gtk3
Requires:       python3dist(dbus-python)
Requires:       python3dist(requests)

%description
Wike is a Wikipedia reader for the GNOME Desktop. Provides access to all the 
content of this online encyclopedia in a native application, with a simpler and 
distraction-free view of articles.

%prep
%autosetup -n Wike-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{appid}.metainfo.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{appid}.desktop

%files -f %{name}.lang
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/actions/*
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_metainfodir}/%{appid}.metainfo.xml
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/services
%{_datadir}/dbus-1/services/%{appid}.SearchProvider.service
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/%{appid}.SearchProvider.ini

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Sep 24 2022 Gustavo Costa <xfgusta@gmail.com> - 1.8.1-2
- Fix _fill_menu bug (rhbz#2128121)

* Fri Sep 09 2022 Gustavo Costa <xfgusta@gmail.com> - 1.8.1-1
- Update to 1.8.1 (rhbz#2125166)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun May 29 2022 Gustavo Costa <xfgusta@fedoraproject.org> - 1.8.0-1
- Update to 1.8.0

* Mon Apr 04 2022 Gustavo Costa <xfgusta@fedoraproject.org> - 1.7.2-1
- Update to 1.7.2

* Tue Feb 08 2022 Gustavo Costa <xfgusta@fedoraproject.org> - 1.7.1-1
- Update to 1.7.1

* Fri Jan 21 2022 Gustavo Costa <xfgusta@fedoraproject.org> - 1.7.0-1
- Fix unowned directories
- Update to 1.7.0

* Fri Dec 17 2021 Gustavo Costa <xfgusta@fedoraproject.org> - 1.6.3-1
- Update to 1.6.3

* Sat Dec 04 2021 Gustavo Costa <xfgusta@fedoraproject.org> - 1.6.2-1
- Update to 1.6.2

* Wed Nov 17 2021 Gustavo Costa <xfgusta@fedoraproject.org> - 1.6.1-1
- Update to 1.6.1

* Sat Oct 16 2021 Gustavo Costa <xfgusta@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0

* Wed Sep 22 2021 Gustavo Costa <xfgusta@fedoraproject.org> - 1.5.7-1
- Update to 1.5.7

* Thu Sep 09 2021 Gustavo Costa <xfgusta@fedoraproject.org> - 1.5.6-1
- Update to 1.5.6
- Remove BR libhandy1-devel
- Add BR glib2-devel

* Thu Sep 02 2021 Gustavo Costa <xfgusta@fedoraproject.org> - 1.5.4-1
- Initial package
