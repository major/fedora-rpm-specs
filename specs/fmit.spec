Summary:       Free Music Instrument Tuner
Name:          fmit
Version:       1.2.14
Release:       12%{?dist}
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:           http://gillesdegottex.github.io/fmit/
Source0:       https://github.com/gillesdegottex/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: qt5-linguist
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5OpenGL)
BuildRequires: pkgconfig(Qt5Multimedia)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: gettext
BuildRequires: itstool
BuildRequires: freeglut-devel
BuildRequires: libXi-devel
BuildRequires: libXmu-devel
BuildRequires: fftw3-devel
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: portaudio-devel
BuildRequires: desktop-file-utils
BuildRequires: make


%description
%{name} is a graphical utility for tuning musical instruments, with
error and volume history and advanced features like waveform shape,
harmonics ratio (formants), and micro-tonal tuning.


%prep
%setup -q

# disable acs_qt capture system on linux
sed -i 's/^\(CONFIG += acs_qt\)/# \1/g' fmit.pro


%build
%{qmake_qt5} PREFIX=%{_prefix} CONFIG+="acs_alsa acs_jack acs_portaudio"
lrelease-qt5 %{name}.pro
%make_build


%install
%make_install INSTALL_ROOT=%{buildroot}

# we use svg icon
rm -rf %{buildroot}%{_datadir}/icons/hicolor/128x128

appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

mkdir -p %{buildroot}%{_datadir}/%{name}/tr/
cp -a tr/*.qm %{buildroot}%{_datadir}/%{name}/tr/
rm -f %{buildroot}%{_datadir}/%{name}/tr/*.ts
%find_lang %{name} --with-qt --without-mo


%files -f %{name}.lang
%license COPYING_GPL.txt COPYING_LGPL.txt
%doc INSTALL.txt README.txt
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/tr
%dir %{_datadir}/%{name}/scales
%{_datadir}/%{name}/scales/*.scl
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{name}-symbolic.svg


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.14-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.14-11
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 03 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.2.14-1
- Fix BuildRequires for qt5 (rhbz#1863573)
- Update to the latest available version

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.13-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.2.13-1
- Update to the latest available version.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 03 2019 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.2.6-2
- Update to the latest available version.
- Switch to compile with qt5.
- Modernize .spec file.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 12 2018 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.1.13-1
- Update to the latest available version.

* Sat Feb 24 2018 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.1.12-5
- Add missing BR (gcc-c++)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.1.12-1
- Update to the latest available version.

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Aug 18 2016 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.1.8-5
- Update to the latest available version.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 30 2016 Rex Dieter <rdieter@fedoraproject.org> 1.0.12-3
- use %%{qmake_qt4} macro to ensure proper build flags (#1303288)

* Mon Jan 25 2016 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.0.12-2
- Enable also ALSA, JACK and PortAudio backends.

* Wed Nov 11 2015 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.0.12-1
- Update to the latest available version, rhbz#1239505.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 Richard Hughes <richard@hughsie.com> - 0.99.5-1
- Rebuilt for new upstream version 0.99.5

* Fri May 30 2014 Richard Hughes <richard@hughsie.com> - 0.99.4-1
- Rebuilt for new upstream version 0.99.4

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.2-3
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jan 27 2011 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.99.2-1
- update to the 0.99.2 version,
- drop patches now upstream,
- translation's files installation enabled.

* Mon Jan 17 2011 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.98.1-4
- preserve the timestamp of the icon file.

* Wed Dec 30 2010 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.98.1-3
- build process does not depend on the BUILD_SHARED_LIBS variable.

* Mon Dec 28 2010 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.98.1-2
- build corrected.
- translation's files installation disabled until fixed upstream.

* Mon Dec 28 2010 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.98.1-1
- initial RPM release.
