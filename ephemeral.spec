%global uuid com.github.cassidyjames.%{name}

Name:           ephemeral
Version:        7.1.0
Release:        5%{?dist}
Summary:        Private-by-default, always-incognito browser

License:        GPLv3+
URL:            https://github.com/cassidyjames/ephemeral
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libdazzle-1.0)
BuildRequires:  pkgconfig(webkit2gtk-4.0)

Requires:       hicolor-icon-theme

%description
Browse the Internet in private without leaving a trace of history on your
computer. Ephemeral is a stripped down private browser that's perfect for
avoiding persistent cookies or web trackers. Close the window and all traces of
your browsing are removed from your device.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{uuid}

# No HiDPI version yet
rm -r %{buildroot}%{_datadir}/icons/hicolor/*@2

# SVG dupes
rm -r %{buildroot}%{_datadir}/icons/hicolor/{16x16,24x24,32x32,48x48,64x64}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{uuid}.lang
%license LICENSE
%doc README.md
%{_bindir}/%{uuid}
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_metainfodir}/*.xml


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Mar 26 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 7.1.0-1
- build(update): 7.1.0

* Fri Feb 19 2021 Fabio Valentini <decathorpe@gmail.com> - 7.0.5-3
- Rebuilt for granite 6 soname bump.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 7.0.5-1
- build(update): 7.0.5

* Wed Sep 30 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 7.0.0-1
- Update to 7.0.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 03 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 6.4.1-1
- Update to 6.4.1

* Wed Apr 29 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 6.4.0-1
- Update to 6.4.0

* Wed Apr 29 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 6.3.4-1
- Update to 6.3.4

* Wed Apr 01 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 6.3.3-1
- Update to 6.3.3

* Sat Mar 28 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 6.3.2-1
- Update to 6.3.2

* Mon Mar 23 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 6.3.1-1
- Update to 6.3.1
- Enable LTO
- Clean SVG icon dupes

* Tue Mar 03 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 6.3.0-1
- Update to 6.3.0

* Tue Feb 18 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 6.2.1-1
- Update to 6.2.1

* Fri Jan 31 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 6.2.0-1
- Update to 6.2.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 6.1.1-1
- Update to 6.1.1

* Mon Nov 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 6.1.0-1
- Update to 6.1.0

* Mon Oct 14 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 6.0.0-1
- Update to 6.0.0

* Tue Sep 17 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 5.3.0-1
- Update to 5.3.0

* Wed Jul 31 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 5.2.1-1
- Update to 5.2.1

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 5.1.0-1
- Update to 5.1.0
- Remove duplicate HiDPI icons

* Tue Apr 02 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 5.0.1-1
- Update to 5.0.1.

* Wed Mar 13 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 4.2.0-1
- 4.2.0
  - New option to close the window when opening a page in an external browser
  - The web view is now focused when navigating

* Sat Feb 23 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 4.1.2-1
- 4.1.2
  - Updated and corrected several autocomplete domains
  - No longer attempt to force HTTPS on protocol-less domains—fixes several popular sites
  - Strip whitespace from URL entry before navigating—fixes instances where trying to navigate to a domain would perform a search
- 4.1.1
  - Corrected joinmastodon.org TLD
  - Added descriptions for more sites
  - Removed dead sites
  - Updated translations
- 4.1.0
  - The URL entry will offer to complete over 400 popular sites*
  - New Search Engine choice in the Menu
  - Switched to Startpage.com by default

* Wed Feb 13 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 4.0.4-1
- Added German translations

* Sun Feb 10 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 4.0.3-9
- Updated spec file

* Tue Feb 05 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 4.0.3-1
- Added Russian translations

* Sun Feb 03 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 4.0.2-1
- Initial release
