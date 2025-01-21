Name:           xvkbd
Version:        4.1
Release:        12%{?dist}
Summary:        Virtual Keyboard for X Window System
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://t-sato.in.coocan.jp/xvkbd
Source0:        %{url}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
# The following icon is licensed under CC BY-SA 3.0.
Source2:        http://download.sourceforge.jp/xvkbd-fedora/45742/%{name}.png
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  imake
BuildRequires:  libX11-devel
BuildRequires:  libXaw-devel
BuildRequires:  libXtst-devel
BuildRequires:  Xaw3d-devel

%description
xvkbd is a virtual (graphical) keyboard program for X Window System
which provides facility to enter characters onto other clients
(software) by clicking on a keyboard displayed on the screen. This
may be used for systems without a hardware keyboard such as kiosk
terminals or hand-held devices. This program also has facility to send
characters specified as the command line option to another client.

%prep
%autosetup -p1
sed -i 's|<X11/Xaw|<X11/Xaw3d|g' xvkbd.c

%build
xmkmf -a
# Installed "normal" files should have 0644 permission, not 0444 permission.
# So I modify Makefile directly.
sed -i.mode -e 's|-m 0444|-m 0644|' Makefile
%make_build CCOPTIONS="%{optflags}" EXTRA_LDOPTIONS="%{?__global_ldflags}"

%install
# By default this installs some file under /usr/lib/X11/app-defaults,
# even on 64 bit architecture. So I had to add "LIBDIR=%{_libdir}/X11".
make LIBDIR=%{_libdir}/X11 DESTDIR=%{buildroot} INSTALLFLAGS="-c -p" \
          install install.man
rm -frv %{buildroot}%{_libdir}/X11/app-defaults
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{S:1}
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -pDm644 %{S:2} %{buildroot}%{_datadir}/pixmaps

%files
%doc README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/X11/app-defaults/XVkbd*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/X11/words.english

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul  26 2024 Miroslav Suchý <msuchy@redhat.com> - 4.1-11
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Raphael Groner <raphgro@fedoraproject.org> - 4.1-1
- bump to v4.1 

* Fri Feb  7 2020 Jerry James <loganjerry@gmail.com> - 3.9-6
- Add patch to fix build with -fno-common

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 3.9-3
- Rebuild with fixed binutils

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 02 2018 Raphael Groner <projects.rg@smart.ms> - 3.9-1
- new version
- new homepage

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 3.7-7
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Sep 13 2015 Christopher Meng <rpm@cicku.me> - 3.7-1
- Update to 3.7

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Feb 15 2015 Christopher Meng <rpm@cicku.me> - 3.6-1
- Update to 3.6

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Christopher Meng <rpm@cicku.me> - 3.5-1
- Update to 3.5

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Feb 26 2012 Orion Poplawski <orion@cora.nwra.com> - 3.2-5
- Rebuild with Xaw3d 1.6.1

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Aug 28 2010 Akio Idehara <zbe64533 at gmail.com> 3.2-2
- Rebuild for F14

* Tue May 18 2010 Akio Idehara <zbe64533 at gmail.com> 3.2-1
- Update to 3.2

* Sun Feb 28 2010 Akio Idehara <zbe64533 at gmail.com> 3.1-5
- Rebuild for F13

* Sat Feb 6 2010 Akio Idehara <zbe64533 at gmail.com> 3.1-4
- Fix build without optflags (#562381)

* Sat Feb 6 2010 Akio Idehara <zbe64533 at gmail.com> 3.1-3
- Separate patch related to 64-bit arch which depends on C99

* Fri Feb 5 2010 Akio Idehara <zbe64533 at gmail.com> 3.1-2
- Fix default define
- Fix warning on 64-bit arch

* Wed Feb 3 2010 Akio Idehara <zbe64533 at gmail.com> 3.1-1
- Update to 3.1

* Mon Feb 1 2010 Akio Idehara <zbe64533 at gmail.com> 3.0-6
- Change Icon size

* Sun Jan 24 2010 Akio Idehara <zbe64533 at gmail.com> 3.0-5
- Fix Icon permission

* Sun Jan 10 2010 Akio Idehara <zbe64533 at gmail.com> 3.0-4
- Clarify Source2 license (CC BY-SA 3.0) and URL

* Fri Jan 8 2010 Akio Idehara <zbe64533 at gmail.com> 3.0-3
- Add the lack of BuildRequires statements
- Fix build failure on x86_64
- Fix some trivial mistake

* Sat Dec 5 2009 Akio Idehara <zbe64533 at gmail.com> 3.0-2
- Add Desktop files

* Sat Dec 5 2009 Akio Idehara <zbe64533 at gmail.com> 3.0-1
- Initial RPM release
