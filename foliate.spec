%global appname com.github.johnfactotum.Foliate

Name:           foliate
Version:        2.6.4
Release:        3%{?dist}
Summary:        Simple and modern GTK eBook reader

License:        GPLv3+
URL:            https://johnfactotum.github.io/foliate/
Source0:        https://github.com/johnfactotum/foliate/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.40

BuildRequires:  pkgconfig(gjs-1.0) >= 1.52
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(iso-codes) >= 3.67
BuildRequires:  pkgconfig(webkit2gtk-4.0)

Requires:       gjs
Requires:       hicolor-icon-theme
Requires:       webkit2gtk3

# For text-to-speech (TTS) support
Recommends:     espeak-ng

# Support for viewing .mobi, .azw, and .azw3 files
Recommends:     python3 >= 3.4

# Alternative text-to-speech (TTS) engines
Suggests:       espeak
Suggests:       festival

%description
A simple and modern GTK eBook viewer, built with GJS and Epub.js.

%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

# Ambiguous python shebang
find %{buildroot}%{_datadir}/%{appname}/assets/KindleUnpack/ -type f -name "*.py" -exec sed -e 's@/usr/bin/env python@/usr/bin/python3@g' -i "{}" \;
find %{buildroot}%{_datadir}/%{appname}/assets/KindleUnpack/ -type f -name "mobiml2xhtml.py" -exec sed -e 's@/usr/bin/python@/usr/bin/python3@g' -i "{}" \;

%find_lang %{appname}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{appname}.lang
%license COPYING
%doc README.md
%{_bindir}/%{appname}
%{_datadir}/%{appname}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_metainfodir}/*.xml


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 13 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 2.6.4-1
- chore(update): 2.6.4
- build(add BR): iso-codes

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 01 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2.6.3-1
- build(update): 2.6.3

* Fri Mar 26 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2.6.2-1
- build(update): 2.6.2

* Wed Mar 24 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2.6.1-1
- build(update): 2.6.1

* Wed Mar 24 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2.6.0-1
- build(update): 2.6.0

* Mon Feb 01 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2.5.0-3
- build: Add 'webkit2gtk3' dep | rh#1923207

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 15 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.5.0-1
- build(update): 2.5.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 06 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.4.2-1
- Update to 2.4.2

* Mon Jul 06 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.4.1-1
- Update to 2.4.1

* Thu Jul 02 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.4.0-1
- Update to 2.4.0

* Thu Jun 18 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.3.0-1
- Update to 2.3.0

* Mon Jun 08 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.2.1-1
- Update to 2.2.1

* Fri May 29 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.2.0-1
- Update to 2.2.0

* Thu Apr 09 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.1.1-1
- Update to 2.1.1

* Wed Apr 08 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.1.0-1
- Update to 2.1.0

* Sun Apr 05 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0.0-1
- Update to 2.0.0

* Mon Mar 30 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.5.3-3
- Add dep: gjs | RHBZ#1818634

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.5.3-1
- Update to 1.5.3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.5.2-1
- Update to 1.5.2

* Sun Jul 14 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.5.0-2
- Update to 1.5.0

* Sat Jul 13 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.4.0-3
- Patch: Use book language for Wikipedia

* Thu Jul 11 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.4.0-2
- Update to 1.4.0

* Sat Jun 29 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.3.1-1
- Update to 1.3.1

* Tue Jun 18 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.3.0-1
- Update to 1.3.0

* Thu Jun 06 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.2.0-1
- Update to 1.2.0

* Sun Jun 02 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.1.0-1
- Update to 1.1.0

* Sat Jun 01 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.1-1
- Initial package
