Name:    scottfree
Version: 1.14
Release: 33%{?dist}
Summary: Interpreter for Scott Adams format text adventure games

License: GPL-2.0-or-later
URL:     http://ifarchive.org/if-archive/scott-adams/interpreters/scottfree/
Source0: http://ifarchive.org/if-archive/scott-adams/interpreters/scottfree/ScottFree.tar.gz
# Man page taken from Debian
Source1: %{name}.6
# Fix Makefile
Patch0:  %{name}-1.14-Makefile.patch
# Add missing headers
# https://salsa.debian.org/games-team/scottfree/blob/master/debian/patches/02_scottcurses_includes.diff
Patch1:  %{name}-1.14-includes.patch
# Fix format strings
# https://salsa.debian.org/games-team/scottfree/blob/master/debian/patches/format-strings.patch
Patch2: %{name}-1.14-format_strings.patch
# Include time.h, fix two warnings in fscanf calls
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=968375
# https://salsa.debian.org/games-team/scottfree/blob/master/debian/patches/04_968375.patch
Patch3: %{name}-1.14-fscanf.patch
Patch4: scottfree-c99.patch
# Fix building with gcc 15
Patch5: %{name}-1.14-gcc15.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: ncurses-devel


%description
ScottFree is an interpreter for Scott-Adams-format text adventure games
(remember those?). It reads and executes TRS-80 format data files.

Most Adventure International Games are distributed as shareware and are 
available from http://ifarchive.org/if-archive/scott-adams/


%prep
%autosetup -c -p1

# Fix file permissions
chmod 644 *


%build
%set_build_flags
%make_build


%install
%make_install

# Install man page
install -d %{buildroot}%{_mandir}/man6
install -p -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man6/


%files
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*
%doc README Definition


%changelog
* Thu Feb 13 2025 Andrea Musuruane <musuruan@gmail.com> - 1.14-33
- Fix FTBFS (BZ #2341333)

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.14-31
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 09 2024 Florian Weimer <fweimer@redhat.com> - 1.14-28
- Fix return-mismatch C compatibility issue (#2257413)

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 17 2022 Andrea Musuruane <musuruan@gmail.com> - 1.14-25
- Added a patch from Debian to fix FTBFS (fix #2113724)
- Added a patch from Debian to fix a crash when restoring a save file

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 30 2019 Andrea Musuruane <musuruan@gmail.com> - 1.14-18
- Imported in Fedora

* Fri Dec 20 2019 Andrea Musuruane <musuruan@gmail.com> - 1.14-17
- Spec file clean up

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.14-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.14-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.14-15
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.14-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.14-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 02 2017 Andrea Musuruane <musuruan@gmail.com> - 1.14-12
- Fixed missing debuginfo
- Added URL tag
- Updated Source0 tags
- Updated description
- Added man page from Debian
- Dropped Group tag

* Fri Sep 01 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.14-11
- Disable debuginfo

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.14-7
- Mass rebuilt for Fedora 19 Features

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.14-5
- rebuild for new F11 features

* Mon Aug 11 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 1.14-4
- rebuild to fix early trouble on RPM Fusions x86 builders

* Fri Nov 02 2007 Andrea Musuruane <musuruan@gmail.com> 1.14-3
- changed license due to new guidelines
- removed %%{?dist} tag from changelog

* Mon Oct 09 2006 Andrea Musuruane <musuruan@gmail.com> 1.14-2
- changed patch name to lowercase to match RPM name
- changed group to "Amusements/Games"
- added %%{?_smp_mflags} to make invocation to speed up SMP builds

* Sat Oct 07 2006 Andrea Musuruane <musuruan@gmail.com> 1.14-1
- initial package based on the old RH 5.2 package and a patch from Debian

