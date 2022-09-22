%global uuid com.github.maoschanz.%{name}

Name: drawing
Version: 1.0.1
Release: 2%{?dist}
Summary: Drawing application for the GNOME desktop
BuildArch: noarch

License: GPLv3+
URL: https://github.com/maoschanz/drawing
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: itstool
BuildRequires: libappstream-glib
BuildRequires: meson >= 0.50.0
BuildRequires: python3-cairo
BuildRequires: python3-devel
BuildRequires: python3-gobject

BuildRequires: pkgconfig(gtk+-3.0)

Requires: gtk3
Requires: hicolor-icon-theme
Requires: python3-cairo
Requires: python3-gobject

%description
This application is a basic image editor, similar to Microsoft Paint, but
aiming at the GNOME desktop.

PNG, JPEG and BMP files are supported.

Besides GNOME, some more traditional design layouts are available too, as well
as an elementaryOS layout. It should also be compatible with the Pinephone and
Librem 5 smartphones.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name} --with-gnome


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.{png,svg}
%{_metainfodir}/*.xml


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Apr 11 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.1-1
- chore(update): 1.0.1

* Sat Mar 26 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.0-1
- chore(update): 1.0.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 06 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.8.5-1
- chore(update): 0.8.5

* Sun Nov 07 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.8.4-1
- chore(update): 0.8.4

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.8.3-1
- build(update): 0.8.3

* Tue Jun 29 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.8.2-1
- build(update): 0.8.2

* Sun Jun 13 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.8.1-1
- build(update): 0.8.1

* Sun Apr 25 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.8.0-1
- build(update): 0.8.0

* Sat Jan 30 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.5-1
- build(update): 0.6.5

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov  1 08:33:58 EET 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.3-1
- build(update): 0.6.3

* Sat Oct 17 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.2-1
- build(update): 0.6.2

* Fri Oct  2 2020 Artem - 0.6.1-1
- Update to 0.6.1

* Sun Sep 20 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.0-1
- Update to 0.6.0

* Sat Sep 12 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.14-1
- Update to 0.4.14

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 08 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.13-1
- Update to 0.4.13

* Fri Feb 28 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.12-1
- Update to 0.4.12

* Sun Feb 16 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.11-1
- Update to 0.4.11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.10-1
- Update to 0.4.10

* Sat Dec 14 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.9-1
- Update to 0.4.9

* Fri Nov 08 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.8-1
- Update to 0.4.8

* Thu Oct 10 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.7-1
- Update to 0.4.7

* Wed Oct 09 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.6-1
- Update to 0.4.6

* Fri Oct 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.5-1
- Update to 0.4.5

* Tue Sep 10 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.4-1
- Update to 0.4.4

* Wed Sep 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.3-1
- Update to 0.4.3

* Tue Jul 30 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.2-1
- Update to 0.4.2

* Sun Jul 28 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.1-1
- Update to 0.4.1

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 10 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2-1
- Initial package.
