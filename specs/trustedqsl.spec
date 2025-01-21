%undefine __cmake_in_source_build

%global srcname tqsl
%global libtqslver 2.5

Name:           trustedqsl
Version:        2.7.5
Release:        2%{?dist}
Summary:        Tool for digitally signing Amateur Radio QSO records
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://sourceforge.net/projects/trustedqsl/

Source0:        https://www.arrl.org/%{srcname}/%{srcname}-%{version}.tar.gz

Patch0:         tqsl-tqsllib.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake%{?rhel:3}
#BuildRequires:  lmdb-devel
BuildRequires:  sqlite-devel
BuildRequires:  openssl-devel
BuildRequires:  curl-devel
BuildRequires:  expat-devel
BuildRequires:  wxGTK-devel
BuildRequires:  zlib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       curl

%description
The TrustedQSL applications are used for generating digitally signed
QSO records (records of Amateur Radio contacts). This package
contains the GUI applications tqslcert and tqsl.

%package -n tqsllib
Epoch:          1
Summary:        TrustedQSL library

%description -n tqsllib
The TrustedQSL library is used for generating digitally signed
QSO records (records of Amateur Radio contacts). This package
contains the library and configuration files needed to run
TrustedQSL applications.

%package -n tqsllib-devel
Epoch:          1
Summary:        Development files the for TrustedQSL library
Requires:       tqsllib%{?_isa} = %{epoch}:%{version}-%{release}

%description -n tqsllib-devel
The TrustedQSL library is used for generating digitally signed
QSO records (records of Amateur Radio contacts). This package
contains the to develop with tqsllib.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
# Use cmake 3 on rhel/epel
%if 0%{?rhel}
%global cmake %cmake3
%endif
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo

%cmake_build


%install
%cmake_install

# Remove bundled language file that shouldn't be there.
find %{buildroot}%{_datadir}/locale/ -type f -name wxstd.mo -exec rm -f {} \;

%find_lang tqslapp

desktop-file-validate %{buildroot}/%{_datadir}/applications/org.arrl.trustedqsl.desktop

%if 0%{?fedora}
# Install metainfo file
mkdir -p %{buildroot}%{_metainfodir}
install -pm 0644 apps/org.arrl.trustedqsl.metainfo.xml %{buildroot}%{_metainfodir}/

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%endif

%ldconfig_scriptlets tqsllib


%files -f tqslapp.lang
%license LICENSE.txt
%doc AUTHORS.txt README
%{_bindir}/tqsl
%{_datadir}/applications/org.arrl.trustedqsl.desktop
%{?fedora:%{_metainfodir}/org.arrl.trustedqsl.metainfo.xml}
%{_datadir}/icons/hicolor/*/apps/org.arrl.trustedqsl.png
%{_datadir}/pixmaps/TrustedQSL.png
%{_datadir}/TrustedQSL
%{_mandir}/man5/*.5*

%files -n tqsllib
%doc src/LICENSE src/ChangeLog.txt
%{_libdir}/libtqsllib.so.%{libtqslver}

%files -n tqsllib-devel
%{_includedir}/*
%{_libdir}/libtqsllib.so


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 18 2024 Richard Shaw <hobbes1069@gmail.com> - 2.7.5-1
- Update to 2.7.5.

* Tue Nov 05 2024 Richard Shaw <hobbes1069@gmail.com> - 2.7.4-1
- Update to 2.7.4.

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1:2.7.2-3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Mar 11 2024 Daniel Rusek <mail@asciiwolf.com> - 2.7.2-1
- Update to 2.7.2.

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 10 2023 Richard Shaw <hobbes1069@gmail.com> - 2.7.1-1
- Update to 2.7.1.

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 22 2022 Richard Shaw <hobbes1069@gmail.com> - 2.6.5-2
- Rebuild for updated wxGTK.

* Tue Oct 11 2022 Richard Shaw <hobbes1069@gmail.com> - 2.6.5-1
- Update to 2.6.5.

* Fri Sep 09 2022 Richard Shaw <hobbes1069@gmail.com> - 2.6.4-1
- Update to 2.6.4.

* Thu Aug 04 2022 Scott Talbert <swt@techie.net> - 2.6.2-3
- Rebuild with wxWidgets 3.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri May 20 2022 Richard Shaw <hobbes1069@gmail.com> - 2.6.2-1
- Update to 2.6.2.

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.9-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Dec 05 2021 Richard Shaw <hobbes1069@gmail.com> - 2.5.9-1.1
- Rebuild with fixed OpenSSL 3 patch.

* Sun Dec 05 2021 Richard Shaw <hobbes1069@gmail.com> - 2.5.9-1
- Update to 2.5.9.

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.5.8-3
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 09 2021 Richard Shaw <hobbes1069@gmail.com> - 2.5.8-1
- Update to 2.5.8.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 18 2020 Richard Shaw <hobbes1069@gmail.com> - 2.5.7-1
- Update to 2.5.7.

* Thu Oct 22 2020 Richard Shaw <hobbes1069@gmail.com> - 2.5.5-1
- Update to 2.5.5.

* Wed Jul 29 2020 Richard Shaw <hobbes1069@gmail.com> - 2.5.4-1
- Update to 2.5.4.

* Thu Apr 23 2020 Richard Shaw <hobbes1069@gmail.com> - 2.5.3-1
- Update to 2.5.3.

* Wed Apr 08 2020 Richard Shaw <hobbes1069@gmail.com> - 2.5.2-1
- Update to 2.5.2.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 2020 Richard Shaw <hobbes1069@gmail.com> - 2.5.1-1
- Update to 2.5.1.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 04 2019 Richard Shaw <hobbes1069@gmail.com> - 2.4.7-1
- Update to 2.4.7.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Richard Shaw <hobbes1069@gmail.com> - 2.4.3-1
- Update to 2.4.3.

* Wed Oct 31 2018 Richard Shaw <hobbes1069@gmail.com> - 2.4.1-1
- Update to 2.4.1.

* Mon Oct 29 2018 Scott Talbert <swt@techie.net> - 2.4-3
- Rebuild with wxWidgets 3.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 02 2018 Richard Shaw <hobbes1069@gmail.com> - 2.4-1
- Update to 2.4.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 11 2017 Richard Shaw <hobbes1069@gmail.com> - 2.3.1-4
- Fix requires for devel package.

* Thu Sep 07 2017 Richard Shaw <hobbes1069@gmail.com> - 2.3.1-3
- Get rid of seprate library version as it is more trouble than it's worth.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul  3 2017 Richard Shaw <hobbes1069@gmail.com> - 2.3.1-1
- Update to latest upstream release.

* Sat Mar  4 2017 Richard Shaw <hobbes1069@gmail.com> - 2.3-4
- Rebuild for broken dependencies with tqsllib.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov  6 2016 Richard Shaw <hobbes1069@gmail.com> - 2.3-1
- Update to latest upstream release.

* Thu Oct  6 2016 Richard Shaw <hobbes1069@gmail.com> - 2.2.2-1
- Update to latest upstream release.

* Thu Mar 24 2016 Richard Shaw <hobbes1069@gmail.com> - 2.2.1-1
- Update to latest upstream release.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-11.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 15 2015 Richard Shaw <hobbes1069@gmail.com> - 2.0.3-11
- Rebuild to fix broken dependency.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-9.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May  4 2015 Richard Shaw <hobbes1069@gmail.com> - 2.0.3-9
- Rebuild for bad version requirement from devel package on the main package.

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.0.3-8
- Rebuilt for GCC 5 C++11 ABI change

* Wed Mar 18 2015 Richard Shaw <hobbes1069@gmail.com> - 2.0.3-7
- Add patch to work around SSL MD5 certification verification being disabled in
  F21+, see https://bugzilla.redhat.com/show_bug.cgi?id=1202157

* Mon Sep  8 2014 Richard Shaw <hobbes1069@gmail.com> - 2.0.3-6
- Update to latest upstream release.
- Add dist tag to libtqsl release and clean up the mess I made.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul  7 2014 Richard Shaw <hobbes1069@gmail.com> - 2.0.2-1
- Update to latest upstream release.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Dec 19 2013 Richard Shaw <hobbes1069@gmail.com> - 2.0.1-1
- Update to version 2.0.1.
- Add conditionals for EPEL-6.

* Wed Sep 25 2013 Richard Shaw <hobbes1069@gmail.com> - 1.14.3-1
- Update to latest upstream release.
- This package now provides tqsllib.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-3
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 20 2011 cooly@gnome.eu.org - 1.13-1
- drop icon and gcc patch - fixed upstream
- new upstream release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 1.11-7
- rebuilt against wxGTK-2.8.11-2

* Sun Oct 25 2009 Lucian Langa <cooly@gnome.eu.org> - 1.11-6
- fix desktop file (#530839)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 01 2008 Lucian Langa <cooly@gnome.eu.org> - 1.11-3
- fix unowned directories

* Fri Oct 10 2008 Lucian Langa <cooly@gnome.eu.org> - 1.11-2
- misc cleanups
- update buildrequires
- package missing docs

* Sun Jul 13 2008 Lucian Langa <lucilanga@gnome.org> - 1.11-1
- initial spec file for fedora

