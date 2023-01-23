Summary: Chdir for DOS and Unix
Name: wcd
Version: 6.0.4
Release: 4%{?dist}
License: GPLv2
Source: http://waterlan.home.xs4all.nl/wcd/%{name}-%{version}.tar.gz
URL: http://waterlan.home.xs4all.nl/
BuildRequires: make
BuildRequires: gcc
BuildRequires: gettext
BuildRequires: ncurses-devel
BuildRequires: libunistring-devel

%description
Wcd.   Directory changer for DOS and Unix.  Another Norton
Change Directory (NCD) clone.

Wcd is a command-line program to change directory fast. It
saves time typing at the keyboard.  One needs to type only
a part of a directory  name and wcd  will jump to it.  Wcd
has a fast selection  method  in  case of multiple matches
and allows aliasing and  banning of directories.  Wcd also
includes a full-screen interactive  directory tree browser
with speed search.

%prep
%setup -q

%build
make -C src %{?_smp_mflags} prefix=%{_prefix} UCS=1 UNINORM=1

%install
make -C src install DESTDIR=${RPM_BUILD_ROOT} prefix=%{_prefix} mandir=%{_mandir}
make -C src install-profile DESTDIR=${RPM_BUILD_ROOT} prefix=%{_prefix} sysconfdir=%{_sysconfdir}

%find_lang %{name} --with-man

%files -f %{name}.lang
%{_bindir}/wcd.exe
# Overwrite the old config files. Old config files may break a new
# installation when the name of the binary changes.
%config %{_sysconfdir}/profile.d/wcd.*
# https://fedoraproject.org/wiki/Packaging_tricks#As_part_of_the_staged_install
%{_defaultdocdir}/%{name}-%{version}/
%{_mandir}/man1/wcd.*
# The name of the manual page is 'wcd', equal to the name of the package and
# defined alias (csh) and function (sh) in the config files, and not equal to
# the name of the binary. The name of the binary may vary and is in fact not
# important.


%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 2 2021 Erwin Waterlander <waterlan@xs4all.nl> - 6.0.4-1
- New upstream version 6.0.4.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 14 2019 Erwin Waterlander <waterlan@xs4all.nl> - 6.0.3-1
- New upstream version 6.0.3.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Erwin Waterlander <waterlan@xs4all.nl> - 6.0.2-3
- Build requires gcc (bug #1606664).

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 11 2018 Erwin Waterlander <waterlan@xs4all.nl> - 6.0.2-1
- New upstream version 6.0.2.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 16 2017 Erwin Waterlander <waterlan@xs4all.nl> - 6.0.1-1
- New upstream version 6.0.1.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 22 2017 Erwin Waterlander <waterlan@xs4all.nl> - 6.0.0-1
- New upstream version 6.0.0.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 4 2017 Erwin Waterlander <waterlan@xs4all.nl> - 5.3.4-1
- New upstream version 5.3.4.

* Thu Nov 3 2016 Erwin Waterlander <waterlan@xs4all.nl> - 5.3.3-1
- New upstream version 5.3.3.

* Fri Feb 19 2016 Erwin Waterlander <waterlan@xs4all.nl> - 5.3.2-1
- New upstream version 5.3.2.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 3 2015 Erwin Waterlander <waterlan@xs4all.nl> - 5.3.1-1
- New upstream version 5.3.1.

* Thu Sep 24 2015 Erwin Waterlander <waterlan@xs4all.nl> - 5.3.0-1
- New upstream version 5.3.0.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 19 2015 Erwin Waterlander <waterlan@xs4all.nl> - 5.2.7-1
- New upstream version 5.2.7.

* Fri Jan 30 2015 Erwin Waterlander <waterlan@xs4all.nl> - 5.2.6-2
- Fixed Source.

* Mon Jan 19 2015 Erwin Waterlander <waterlan@xs4all.nl> - 5.2.6-1
- New upstream version 5.2.6.

* Tue Sep 02 2014 Pádraig Brady <pbrady@redhat.com> - 5.2.5-4
- rebuild for libunistring soname bump

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 11 2014 Erwin Waterlander <waterlan@xs4all.nl> - 5.2.5-2
- Fixed packaging new manual translations.

* Wed Jun 11 2014 Erwin Waterlander <waterlan@xs4all.nl> - 5.2.5-1
- New upstream version 5.2.5.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 29 2013 Erwin Waterlander <waterlan@xs4all.nl> - 5.2.4-1
- New upstream version 5.2.4.

* Mon Aug  5 2013 Tim Waugh <twaugh@redhat.com> - 5.2.3-4
- Fixed doc-related build problem (bug #992868).

* Fri Feb 22 2013 Erwin Waterlander <waterlan@xs4all.nl> - 5.2.3-3
- Build requires perl-Pod-Checker.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 29 2012 Erwin Waterlander <waterlan@xs4all.nl> - 5.2.3-1
- New upstream version 5.2.3.
- Set _sysconfdir while installing profile (the makefile supports
  it now).

* Tue Oct 09 2012 Erwin Waterlander <waterlan@xs4all.nl> - 5.2.2-6
- Use _sysconfdir for config files.

* Thu Sep 27 2012 Erwin Waterlander <waterlan@xs4all.nl> - 5.2.2-5
- Added comment to explain why configs are overwritten and the name
  of the manual is not equal to the name of the binary.

* Mon Sep 24 2012 Erwin Waterlander <waterlan@xs4all.nl> - 5.2.2-4
- Summary starts with capital letter C.
- Config files marked with config.
- Removed clean section (needed only if supporting EPEL5).
- Moved man-pages under doc.

* Sun Sep 23 2012 Erwin Waterlander <waterlan@xs4all.nl> - 5.2.2-3
- Increment release version.

* Sun Sep 23 2012 Erwin Waterlander <waterlan@xs4all.nl> - 5.2.2-2
- Removed tag Packager.
- Removed Buildrequires sed.
- Changed License tag from GPL to GPLv2

* Sun Sep 23 2012 Erwin Waterlander <waterlan@xs4all.nl> - 5.2.2-1
- Initial version for Fedora.

