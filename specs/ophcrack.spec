Name:           ophcrack
Version:        3.8.0
Release:        18%{?dist}
Summary:        Free Windows password cracker based on rainbow tables
# Automatically converted from old format: GPLv2+ with exceptions - review is highly recommended.
License:        LicenseRef-Callaway-GPLv2+-with-exceptions
URL:            https://ophcrack.sourceforge.io
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2

# Wrong FSF address in LICENSE FILE
# https://gitlab.com/objectifsecurite/ophcrack/issues/7
Patch0:         0001-correct-FSF-address.patch

# upstreamable
BuildRequires: make
BuildRequires:  automake libtool
BuildRequires:  openssl-devel
BuildRequires:  expat-devel
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(qwt5-qt4)
BuildRequires:  qt5-qtcharts-devel


%description
Ophcrack is a free Windows password cracker based on rainbow tables. 
It is a very efficient implementation of rainbow tables done by the 
inventors of the method. It comes with a Graphical User Interface and 
runs on multiple platforms. 

Features:

    * Runs on Windows, Linux/Unix, Mac OS X, ...
    * Cracks LM and NTLM hashes.
    * Free tables available for Windows XP and Vista.
    * Brute-force module for simple passwords.
    * Audit mode and CSV export.
    * Real-time graphs to analyze the passwords.
    * LiveCD available to simplify the cracking.
    * Loads hashes from encrypted SAM recovered from a Windows partition,
      Vista included.
    * Free and open source software (GPL).


%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

install -Dp -m0644 src/gui/pixmaps/os.png %{buildroot}%{_datadir}/pixmaps/ophcrack.png
install -dm0755 %{buildroot}%{_datadir}/applications

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Type=Application
Exec=%{name}
Name=Ophcrack
Comment=Windows password cracker
GenericName=Windows password cracker
Icon=ophcrack
Terminal=false
Categories=System;Security;
StartupNotify=true
EOF

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop


%files
%doc AUTHORS ChangeLog COPYING LICENSE LICENSE.OpenSSL NEWS README.md
%{_bindir}/%{name}
%{_datadir}/pixmaps/ophcrack.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 3.8.0-17
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 3.8.0-9
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Jeff Law <law@redhat.com> - 3.8.0-5
- Drop build requirement for qt5-devel

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Alessio <alciregi@fedoraproject.org> - 3.8.0-3
- Patch to FSF address in LICENSE file

* Sat Dec 14 2019 Alessio <alciregi@fedoraproject.org> - 3.8.0-2
- Invalid URL in spec file

* Fri Dec 13 2019 Alessio <alciregi@fedoraproject.org> - 3.8.0-1
- Update to latest upstream (BZ#1437500)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 05 2016 Filipe Rosset <rosset.filipe@gmail.com> - 3.6.1-1
- Rebuilt for new upstream release 3.6.1, fixes rhbz #1365143

* Mon Dec 05 2016 Filipe Rosset <rosset.filipe@gmail.com> - 3.6.0-8
- Spec clean up

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.6.0-5
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 07 2013 Adam Miller <maxamillion@fedoraproject.org> - 3.6.0-1
- Update to latest upstream (BZ#971711)

* Wed May 29 2013 Adam Miller <maxamillion@fedoraproject.org> - 3.5.0-1
- Update to latest upstream (BZ#919553)

* Mon Mar 04 2013 Adam Miller <maxamillion@fedoraproject.org> - 3.4.0-1
- Update to latest upstream (BZ#915223)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 19 2012 Rex Dieter <rdieter@fedoraproject.org> - 3.3.1-3
- s/qt-devel/qt4-devel/
- rebuild (qwt)
- undo LFLAGS hack (the default flags are legit)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Feb 11 2012 Adam Miller <maxamillion@fedoraproject.org> - 3.3.1-1
- Update to latest upstream release.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 3.3.0-5
- rebuilt with new openssl

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 02 2009 Adam Miller <maxamillion [AT] gmail.com> - 3.3.0-3
- Added comment for LFLAGS justification, fixed rpmlint warnings

* Tue Jun 02 2009 Adam Miller <maxamillion [AT] gmail.com> - 3.3.0-2
- Fixed licensing field, LFLAGS issue, desktop file guidelines, and doc listing

* Fri May 29 2009 Adam Miller <maxamillion [AT] gmail.com> - 3.3.0-1
- New upstream release fixes some packaging issues with the old makefile

* Thu May 28 2009 Adam Miller <maxamillion [AT] gmail.com> - 3.2.1-3
- Fixed the URL macro problem, also removed unneeded requires.

* Thu May 28 2009 Adam Miller <maxamillion [AT] gmail.com> - 3.2.1-2
- Fixed URL/Source0 mishap, fixed desktop file icon listing, fixed files list
- Got rid of unneeded >> from description listing

* Wed May 27 2009 Adam Miller <maxamillion [AT] gmail.com> - 3.2.1-1
- First build of ophcrack for Fedora
