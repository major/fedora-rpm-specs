# For test builds, should be set to 0 for release builds.
%global alpha 0

Name:           fldigi
Version:        4.2.06
Release:        3%{?dist}
Summary:        Digital modem program for Linux

License:        GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-3.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND GPL-2.0-only AND BSL-1.0 AND MIT-0 AND LGPL-3.0-only AND GPL-1.0-only AND Apache-2.0

URL:            http://www.w1hkj.com/Fldigi.html
%if %{alpha}
Source0:        http://www.w1hkj.com/alpha/%{name}/%{name}-%{version}.tar.gz
%else
Source0:        http://www.w1hkj.com/files/%{name}/%{name}-%{version}.tar.gz
%endif
Source100:      fldigi.appdata.xml

Patch0:         fldigi-hamlib.patch

ExcludeArch:    i686

#BuildRequires:  automake autoconf libtool

BuildRequires:  asciidoc
BuildRequires:  desktop-file-utils
BuildRequires:  fltk-devel >= 1.3
BuildRequires:  gettext
BuildRequires:  gcc gcc-c++
BuildRequires:  hamlib-devel
%{?fedora:BuildRequires:  flxmlrpc-devel}
%if 0%{?rhel} < 8
BuildRequires:  fltk-static libXcursor-devel
%endif
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libudev-devel
BuildRequires:  make
BuildRequires:  portaudio-devel >= 19-4
BuildRequires:  pulseaudio-libs-devel
%if 0%{?fedora}
# For appstream-util
BuildRequires:  libappstream-glib
%endif

%{?fedora:Recommends:     trustedqsl}

Provides:       flarq = %{version}-%{release}

Obsoletes:      fldigi-doc < 4.1.14-1

%description
Fldigi is a modem program which supports most of the digital modes used by 
ham radio operators today. You can also use the program for calibrating your 
sound card to WWV or doing a frequency measurement test. The program also comes 
with a CW decoder. fldigi is written with the help of the Fast Light Toolkit X 
GUI. Fldigi is a fast moving project many added features with each update.

Flarq (Fast Light Automatic Repeat Request) is a file transfer application
that is based on the ARQ specification developed by Paul Schmidt, K9PS.
It is capable of transmitting and receiving frames of ARQ data via fldigi.


%prep
%autosetup -p1 -n %{name}-%{version}


%build
%if 0%{?rhel} && 0%{?rhel} < 8
%configure --enable-static
%else
%configure
%endif
make %{?_smp_mflags} CFLAGS="%{optflags}" LIBS="-lm -lX11 -lpthread" V=1


%install
%make_install

# Add keywords to desktop file for gnome-shell and software center.
echo "Keywords=modem;psk;rtty;cw;fsq;fsk;" >> %{buildroot}%{_datadir}/applications/%{name}.desktop

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/flarq.desktop

# Add fldigi-psk.png as it's in PNG format and higher resolution than the XPM.
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/
install -pm 0644 data/fldigi-psk.png \
    %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

%find_lang %{name}

%if 0%{?fedora}
# Install and validate appdata file
mkdir -p %{buildroot}%{_datadir}/appdata
install %{SOURCE100} -pm 0644 %{buildroot}%{_datadir}/appdata/
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.appdata.xml
%endif


%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog README NEWS
%{_bindir}/*
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.xpm 
%{_datadir}/pixmaps/flarq.xpm 
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/man1/flarq.1.gz
%{?fedora:%{_datadir}/appdata/fldigi.appdata.xml}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/flarq.desktop
%{_datadir}/%{name}/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 31 2024 Richard Shaw <hobbes1069@gmail.com> - 4.2.06-2
- Rebuild for Hamlib 4.6.

* Fri Oct 11 2024 Richard Shaw <hobbes1069@gmail.com> - 4.2.06-1
- Update to 4.2.06.

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Richard Shaw <hobbes1069@gmail.com> - 4.2.04-1
- Update to 4.2.04.

* Mon Nov 06 2023 Richard Shaw <hobbes1069@gmail.com> - 4.2.03-1
- Update to 4.2.03.

* Thu Sep 28 2023 Richard Shaw <hobbes1069@gmail.com> - 4.2.00-1
- Update to 4.2.00.

* Thu Aug 03 2023 Richard Shaw <hobbes1069@gmail.com> - 4.1.27-1
- Update to 4.1.27.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu May 18 2023 Richard Shaw <hobbes1069@gmail.com> - 4.1.26-2
- Update licenses to SPDX identifiers.

* Thu May 18 2023 Richard Shaw <hobbes1069@gmail.com> - 4.1.26-1
- Update to 4.1.26.

* Wed Feb 15 2023 Richard Shaw <hobbes1069@gmail.com> - 4.1.25-1
- Update to 4.1.25.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 07 2022 Richard Shaw <hobbes1069@gmail.com> - 4.1.23-3
- Rebuild for hamlib 4.5.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Richard Shaw <hobbes1069@gmail.com> - 4.1.23-1
- Update to 4.1.23.

* Wed May 04 2022 Richard Shaw <hobbes1069@gmail.com> - 4.1.21-1
- Update to 4.1.21.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 23 2021 Richard Shaw <hobbes1069@gmail.com> - 4.1.20-5
- Rebuild for hamlib 4.4.

* Thu Dec 23 2021 Richard Shaw <hobbes1069@gmail.com> - 4.1.20-4
- f35-build-side-49088

* Thu Dec 23 2021 Richard Shaw <hobbes1069@gmail.com> - 4.1.20-3
- 36-build-side-49086

* Tue Oct 12 2021 Richard Shaw <hobbes1069@gmail.com> - 4.1.20-2
- Rebuild for hamlib 4.3.1.

* Thu Aug 05 2021 Richard Shaw <hobbes1069@gmail.com> - 4.1.20-1
- Update to 4.1.20.

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 26 2021 Richard Shaw <hobbes1069@gmail.com> - 4.1.19-1
- Update to 4.1.19.

* Sun May 30 2021 Richard Shaw <hobbes1069@gmail.com> - 4.1.18-3
- Rebuild for hamlib 4.2.

* Tue Feb 02 2021 Richard Shaw <hobbes1069@gmail.com> - 4.1.18-2
- Rebuild for hamlib 4.1.

* Fri Jan 29 2021 Richard Shaw <hobbes1069@gmail.com> - 4.1.18-1
- Update to 4.1.18.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 03 2020 Richard Shaw <hobbes1069@gmail.com> - 4.1.17-1
- Update to 4.1.17.

* Mon Oct 19 2020 Richard Shaw <hobbes1069@gmail.com> - 4.1.15-1
- Update to 4.1.15.

* Mon Oct 12 2020 Richard Shaw <hobbes1069@gmail.com> - 4.1.14-1
- Update to 4.1.14.
- Remove large PDF docs, they can be downloaded seprately.
- Remove forced C++14 as the fixes patch has been updated to support C++17.

* Tue Aug 18 2020 Jeff Law <law@redhat.com> - 4.1.13-4
- Force C++14 as this code is not C++17 ready

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Richard Shaw <hobbes1069@gmail.com> - 4.1.13-2
- Add patch to fix various memory leaks and other type issues.

* Tue May 26 2020 Richard Shaw <hobbes1069@gmail.com> - 4.1.13-1
- Update to 4.1.13.

* Thu Apr 23 2020 Richard Shaw <hobbes1069@gmail.com> - 4.1.12-1
- Update to 4.1.12.

* Sat Apr 04 2020 Richard Shaw <hobbes1069@gmail.com> - 4.1.11-2
- Rebuild for hamlib 4.0.

* Thu Apr 02 2020 Richard Shaw <hobbes1069@gmail.com> - 4.1.11-1
- Update to 4.1.11.

* Wed Apr 01 2020 Richard Shaw <hobbes1069@gmail.com> - 4.1.10-1
- Update to 4.1.10.

* Tue Mar 31 2020 Richard Shaw <hobbes1069@gmail.com> - 4.1.09-3
- Rebuild for hamlib 4.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Richard Shaw <hobbes1069@gmail.com> - 4.1.09-1
- Update to 4.1.09.

* Thu Aug 15 2019 Richard Shaw <hobbes1069@gmail.com> - 4.1.08-1
- Update to 4.1.08.

* Tue Aug 06 2019 Richard Shaw <hobbes1069@gmail.com> - 4.1.07-1
- Update to 4.1.07.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 24 2019 Richard Shaw <hobbes1069@gmail.com> - 4.1.06-1
- Update to 4.1.06.

* Thu Jul 04 2019 Richard Shaw <hobbes1069@gmail.com> - 4.1.05-1
- Update to 4.1.05.

* Sat Jun 29 2019 Richard Shaw <hobbes1069@gmail.com> - 4.1.04-1
- Update to 4.1.04.

* Tue Jun 11 2019 Richard Shaw <hobbes1069@gmail.com> - 4.1.03-2
- Add patch for xmlrpc, fixes RHBZ#1705189.

* Mon Apr 22 2019 Richard Shaw <hobbes1069@gmail.com> - 4.1.03-1
- Update to 4.1.03.

* Sun Apr 14 2019 Richard Shaw <hobbes1069@gmail.com> - 4.1.02-1
- Update to 4.1.02.

* Tue Feb 19 2019 Richard Shaw <hobbes1069@gmail.com> - 4.1.01-1
- Update to 4.1.01.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Richard Shaw <hobbes1069@gmail.com> - 4.1.00-1
- Update to 4.1.00.

* Thu Aug 30 2018 Richard Shaw <hobbes1069@gmail.com> - 4.0.18-2
- Rebuild for hamlib 3.3.

* Thu Aug 30 2018 Richard Shaw <hobbes1069@gmail.com> - 4.0.18-1
- Update to 4.0.18.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 07 2018 Richard Shaw <hobbes1069@gmail.com> - 4.0.17-1
- Update to 4.0.17.

* Fri Feb 09 2018 Richard Shaw <hobbes1069@gmail.com> - 4.0.16-1
- Update to 4.0.16.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Richard Shaw <hobbes1069@gmail.com> - 4.0.14-1
- Update to latest upstream release.

* Sun Dec 31 2017 Richard Shaw <hobbes1069@gmail.com> - 4.0.13-1
- Update to latest upstream release.

* Sat Oct 28 2017 Richard Shaw <hobbes1069@gmail.com> - 4.0.12-1
- Update to latest upstream release.

* Sun Oct 22 2017 Richard Shaw <hobbes1069@gmail.com> - 4.0.11-1
- Update to latest upstream release.

* Tue Sep 26 2017 Richard Shaw <hobbes1069@gmail.com> - 4.0.10-1
- Update to latest upstream release.

* Mon Sep 04 2017 Richard Shaw <hobbes1069@gmail.com> - 4.0.9-1
- Update to latest upstream release.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Florian Weimer <fweimer@redhat.com> - 4.0.8-3
- Rebuild with binutils fix for ppc64le (#1475636)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Richard Shaw <hobbes1069@gmail.com> - 4.0.8-1
- Update to latest upstream release.

* Sun Jul 09 2017 Richard Shaw <hobbes1069@gmail.com> - 4.0.7-1
- Update to latest upstream release.

* Sat Jul 01 2017 Richard Shaw <hobbes1069@gmail.com> - 4.0.6-1
- Update to latest upstream release.

* Tue Jun 20 2017 Richard Shaw <hobbes1069@gmail.com> - 4.0.5-1
- Update to latest upstream release.

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Wed May 10 2017 Richard Shaw <hobbes1069@gmail.com> - 4.0.4-1
- Update to latest upstream release.

* Sun Apr 30 2017 Richard Shaw <hobbes1069@gmail.com> - 4.0.3-1
- Update to latest upstream release.

* Fri Apr 14 2017 Richard Shaw <hobbes1069@gmail.com> - 4.0.2-1
- Update to latest upstream release.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.23.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan  6 2017 Richard Shaw <hobbes1069@gmail.com> - 3.23.20-1
- Update to latest upstream release.

* Fri Dec 23 2016 Richard Shaw <hobbes1069@gmail.com> - 3.23.19-1
- Update to latest upstream release.

* Mon Dec 12 2016 Richard Shaw <hobbes1069@gmail.com> - 3.23.18-1
- Update to latest upstream release.

* Tue Dec 06 2016 Richard Shaw <hobbes1069@gmail.com> - 3.23.17-1
- Update to latest upstream release.

* Fri Nov 11 2016 Richard Shaw <hobbes1069@gmail.com> - 3.23.16-1
- Update to latest upstream release.
- Fldigi can now automatically upload contacts to LoTW through trustedqsl.

* Sun Oct 16 2016 Richard Shaw <hobbes1069@gmail.com> - 3.23.15-1
- Update to latest upstream release.

* Sun Sep 18 2016 Richard Shaw <hobbes1069@gmail.com> - 3.23.14-1
- Update to latest upstream release.

* Sat Aug  6 2016 Richard Shaw <hobbes1069@gmail.com> - 3.23.13-1
- Update to latest upstream release.

* Mon Jun 29 2016 Richard Shaw <hobbes1069@gmail.com> - 3.23.12-1
- Update to latest upstream release.

* Sun Jun 12 2016 Richard Shaw <hobbes1069@gmail.com> - 3.23.11-1
- Update to latest upstream release.

* Sun Apr  3 2016 Richard Shaw <hobbes1069@gmail.com> - 3.23.09-1
- Update to latest upstream release.

* Wed Feb 24 2016 Richard Shaw <hobbes1069@gmail.com> - 3.23.08-1
- Update to latest upstream release.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.23.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Jonathan Wakely <jwakely@redhat.com> - 3.23.07-2
- Patched for C++11 compatibility.

* Fri Jan 22 2016 Richard Shaw <hobbes1069@gmail.com> - 3.23.07-1
- Update to latest upstream release.

* Wed Dec  2 2015 Richard Shaw <hobbes1069@gmail.com> - 3.23.06-1
- Update to latest upstream release.

* Thu Nov 19 2015 Richard Shaw <hobbes1069@gmail.com> - 3.23.05-1
- Update to latest upstream release.

* Fri Oct 16 2015 Richard Shaw <hobbes1069@gmail.com> - 3.23.04-1
- Update to latest upstream release.

* Wed Sep 30 2015 Richard Shaw <hobbes1069@gmail.com> - 3.23.03-1
- Update to latest upstream release.

* Fri Sep 18 2015 Richard Hughes <rhughes@redhat.com> - 3.22.13-2
- Remove now-unused AppData file

* Tue Jul 21 2015 Richard Shaw <hobbes1069@gmail.com> - 3.22.13-1
- Update to latest upstream release.

* Sat Jul 18 2015 Richard Shaw <hobbes1069@gmail.com> - 3.22.12-1
- Update to latest upstream release.

* Wed Jul 15 2015 Richard Shaw <hobbes1069@gmail.com> - 3.22.11-1
- Update to latest upstream release.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.22.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun  1 2015 Richard Shaw <hobbes1069@gmail.com> - 3.22.10-1
- Update to latest upstream release.

* Tue May  5 2015 Richard Shaw <hobbes1069@gmail.com> - 3.22.08-1
- Update to latest upstream release.
- Update build requirements to use separate xmlrpc library.

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.22.07-2
- Rebuilt for GCC 5 C++11 ABI change

* Thu Apr  2 2015 Richard Shaw <hobbes1069@gmail.com> - 3.22.07-1
- Update to latest upstream release.

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 3.22.06-2
- Add an AppData file for the software center

* Sun Mar 22 2015 Richard Shaw <hobbes1069@gmail.com> - 3.22.06-1
- Update to latest upstream release.

* Tue Jan 13 2015 Richard Shaw <hobbes1069@gmail.com> - 3.22.05-1
- Update to latest upstream release.

* Fri Dec 26 2014 Richard Shaw <hobbes1069@gmail.com> - 3.22.04-1
- Update to latest upstream release.

* Thu Dec 25 2014 Richard Shaw <hobbes1069@gmail.com> - 3.22.03-1
- Update to latest upstream release.

* Mon Dec  1 2014 Richard Shaw <hobbes1069@gmail.com> - 3.22.02-1
- Update to latest upstream release.

* Mon Oct 20 2014 Richard Shaw <hobbes1069@gmail.com> - 3.22.01-1
- Update to latest upstream release.

* Thu Oct 16 2014 Richard Shaw <hobbes1069@gmail.com> - 3.22.00-1
- Update to latest upstream release.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 17 2014 Rex Dieter <rdieter@fedoraproject.org> - 3.21.83-2
- rebuild (for pulseaudio, bug #1117683)

* Sun Jun 29 2014 Richard Shaw <hobbes1069@gmail.com> - 3.21.83-1
- Update to latest upstream release.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.21.82-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 30 2014 Richard Shaw <hobbes1069@gmail.com> - 3.21.82-1
- Update to latest upstream release.

* Sun Mar 30 2014 Richard Shaw <hobbes1069@gmail.com> - 3.21.81-1
- Update to latest upstream release.

* Tue Mar 11 2014 Richard Shaw <hobbes1069@gmail.com> - 3.21-79-1
- Update to latest upstream release.

* Tue Mar  4 2014 Richard Shaw <hobbes1069@gmail.com> - 3.21.78-1
- Update to latest upstream release.

* Wed Oct 30 2013 Richard Shaw <hobbes1069@gmail.com> - 3.21.77-1
- Update to latest bugfix release.

* Thu Sep 12 2013 Richard Shaw <hobbes1069@gmail.com> - 3.21.76-1
- Update to latest bugfix release.

* Mon Sep  2 2013 Richard Shaw <hobbes1069@gmail.com> - 3.21.75-1
- Update to latest bugfix release.

* Tue Aug 27 2013 Richard Shaw <hobbes1069@gmail.com> - 3.21.74-1
- Update to latest bugfix release.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.21.68-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 3.21.68-2
- Perl 5.18 rebuild

* Sat Mar 16 2013 Richard Shaw <hobbes1069@gmail.com> - 3.21.68-1
- Update to latest bugfix release.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.21.49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 3 2012 Randall J. Berry, N3LRX <dp67@fedoraproject.org> - 3.21.49-1
- Upstream upddate to 3.21.49

* Mon May 14 2012 Randall J. Berry, N3LRX <dp67@fedoraproject.org> - 3.21.41-1
- Upstream upddate to 3.21.41
- Fix deps for F18/Rawhide

* Sat Jan 28 2012 Randall J. Berry, N3LRX <dp67@fedoraproject.org> - 3.21.37-2
- Upstream upddate to 3.21.37
- Remove patches fixed upstream
- Correct source URL

* Sat Jan 28 2012 Randall J. Berry, N3LRX <dp67@fedoraproject.org> - 3.21.37-1
- Upstream upddate to 3.21.37

* Sun Jan 15 2012 Randall J. Berry, N3LRX <dp67@fedoraproject.org> - 3.21.35-2
- Add patches for testing error correction
- Update rawhide builds

* Sun Jan 15 2012 Randall J. Berry, N3LRX <dp67@fedoraproject.org> - 3.21.35-1
- Upstream upddate to 3.21.35
- Rebuild against gcc 4.7

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.21.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jan 2 2012 Randall J. Berry, N3LRX <dp67@fedoraproject.org> - 3.21.34-2
- Test Build Against FLTK 1.3
