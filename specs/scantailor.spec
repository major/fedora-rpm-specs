%global __cmake_in_source_build 1
Name:           scantailor
Version:        0.9.11.1
Release:        39%{?dist}
Summary:        An interactive post-processing tool for scanned pages

License:        GPL-3.0-or-later OR LGPL-2.1-only
URL:            http://scantailor.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
# Don't override CFLAGS and CXXFLAGS: https://github.com/scantailor/scantailor/pull/160
Patch0:         0001-respect-CFLAGS-and-CXXFLAGS.patch
Patch1:         boost1.6.patch
Patch2:         gcc6-build-patch.patch
Patch3:         f30-buildfailures.patch
Patch4:         boost-1.83.0-compat.patch

BuildRequires: make
BuildRequires:  cmake
BuildRequires:  boost-devel
BuildRequires:  libXext-devel
BuildRequires:  qt-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  libjpeg-devel
BuildRequires:  zlib-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libXrender-devel
BuildRequires:  desktop-file-utils
BuildRequires:  glibc-static

%description
Scan Tailor is an interactive post-processing tool for scanned pages.
It performs operations such as page splitting, deskewing, adding/removing
borders, and others. You give it raw scans, and you get pages ready to be
printed or assembled into a PDF or DJVU file. Scanning, optical character
recognition, and assembling multi-page documents are out of scope of this
project.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1 -z .boost
%patch -P2 -p1 -b .gcc6-build
%patch -P3 -p1 -b .f30-buildfaulures
%patch -P4 -p1

%build
%cmake . -DEXTRA_LIBS=Xrender -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo -DCMAKE_INSTALL_PREFIX="/usr" 
make %{?_smp_mflags}
mv resources/icons/COPYING resources/icons/COPYING-icons

%install
make install DESTDIR=$RPM_BUILD_ROOT
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/scalable/apps
cp -p resources/appicon.svg \
        ${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/scalable/apps/scantailor.svg

%check
make tests
./tests/tests

%files
%doc COPYING resources/icons/COPYING-icons
%{_bindir}/scantailor
%{_bindir}/scantailor-cli
%{_datadir}/scantailor/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/scantailor.svg

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11.1-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 06 2023 Patrick Palka <ppalka@redhat.com> - 0.9.11.1-36
- Fix build with boost-1.83.0

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 26 2020 Jeff Law <law@redhat.com> - 0.9.11.1-29
- Do not force C++11 mode
- Adjust for F33 cmake macro changes

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11.1-28
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 29 2019 Jan Horak <jhorak@redhat.com> - 0.9.11.1-24
- Fixing building issues

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.11.1-20
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.11.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Tue Mar 14 2017 Jan Horak <jhorak@redhat.com> - 0.9.11.1-16
- Fixed rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 29 2015 Adam Williamson <awilliam@redhat.com>  - 0.9.11.1-13
- respect CFLAGS and CXXFLAGS (and hence fix build)

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.9.11.1-12
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.11.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.9.11.1-10
- Rebuild for boost 1.57.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.11.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.11.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 0.9.11.1-7
- Rebuild for boost 1.55.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 0.9.11.1-5
- Rebuild for boost 1.54.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 0.9.11.1-3
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 0.9.11.1-2
- rebuild against new libjpeg

* Tue Feb 28 2012 Jan Horak <jhorak@redhat.com> - 0.9.11.1-1
- Update to 0.9.11.1

* Wed Feb  1 2012 Jan Horak <jhorak@redhat.com> - 0.9.11-1
- Update to 0.9.11

* Sun Aug 14 2011 Jan Horak <jhorak@redhat.com> - 0.9.10-1
- Update to 0.9.10

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 15 2010 Jan Horak <jhorak@redhat.com> - 0.9.9.2-1
- Update to 0.9.9.2

* Tue Aug 10 2010 Jan Horak <jhorak@redhat.com> - 0.9.9.1-1
- Update to 0.9.9.1

* Mon Jun 14 2010 Jan Horak <jhorak@redhat.com> - 0.9.9-1
- Update to 0.9.9

* Wed Apr 28 2010 Jan Horak <jhorak@redhat.com> - 0.9.8.1-1
- Update to 0.9.8.1

* Wed Apr  7 2010 Jan Horak <jhorak@redhat.com> - 0.9.8-1
- Update to 0.9.8

* Tue Feb 16 2010 Jan Horak <jhorak@redhat.com> - 0.9.7.2-2
- Renaming of COPYING-icons moved to prep section

* Mon Feb 15 2010 Jan Horak <jhorak@redhat.com> - 0.9.7.2-1
- Initial release

