# disable offensive fortunes by default
%bcond_with offensive
# there are no actual tests
%bcond_with tests

%global CookieDir %{_datadir}/games/fortune

# needed to support out-of-source builds on EPEL8
%undefine __cmake_in_source_build

Name:		fortune-mod
Version:	3.24.0
Release:	2%{?dist}
Summary:	A program which will display a fortune

# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		https://github.com/shlomif/fortune-mod
Source0:	https://www.shlomifish.org/open-source/projects/fortune-mod/arcs/fortune-mod-%{version}.tar.xz
Source1:	kernelnewbies-fortunes.tar.gz
Source2:	bofh-excuses.tar.bz2
# originally at http://www.aboleo.net/software/misc/fortune-tao.tar.gz
Source3:	fortune-tao.tar.gz
Source4:	http://www.splitbrain.org/Fortunes/hitchhiker/fortune-hitchhiker.tgz
# originally at http://www.dibona.com/opensources/osfortune.tar.gz
Source5:	osfortune.tar.gz
Source6:	http://humorix.org/downloads/humorixfortunes-1.4.tar.gz

BuildRequires:	perl(Cwd)
BuildRequires:	perl(File::Find::Object)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Path::Tiny)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::RunValgrind)
BuildRequires:	perl(Test::Trap)
BuildRequires:	perl(autodie)
BuildRequires:	perl(lib)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:	perl-Test-Harness
BuildRequires:	perl-interpreter
BuildRequires:	perl-libs
BuildRequires:	pkgconfig(librinutils)
BuildRequires:	recode-devel
BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	valgrind
BuildRequires:	valgrind-devel
BuildRequires:	chrpath


%description
Fortune-mod contains the ever-popular fortune program, which will
display quotes or witticisms. Fun-loving system administrators can add
fortune to users' .login files, so that the users get their dose of
wisdom each time they log in.


%prep
%setup -q -n %{name}-%{version}

%build
%cmake -DCOOKIEDIR=%{CookieDir} -DLOCALDIR=%{CookieDir} -DNO_OFFENSIVE=TRUE
%cmake_build

%install
%cmake_install

tar zxvf %{SOURCE1} -C $RPM_BUILD_ROOT%{CookieDir}
%if %{without offensive}
rm -f $RPM_BUILD_ROOT%{CookieDir}/men-women*
%endif

mv $RPM_BUILD_ROOT/usr/games/fortune $RPM_BUILD_ROOT%{_bindir}
rm -f $RPM_BUILD_ROOT%{_bindir}/rot
# this isn't debian
rm -f $RPM_BUILD_ROOT%{CookieDir}/debian*
rm -f $RPM_BUILD_ROOT%{CookieDir}/off/debian*

# Using bzcat for portability because tar keeps changing the switch
bzcat %{SOURCE2} | tar xvf - -C $RPM_BUILD_ROOT%{CookieDir}

# Non-standard source files, need to move things around
tar zxvf %{SOURCE3} -C $RPM_BUILD_ROOT%{CookieDir}/ fortune-tao/tao*
mv $RPM_BUILD_ROOT%{CookieDir}/fortune-tao/* $RPM_BUILD_ROOT%{CookieDir}/
rmdir $RPM_BUILD_ROOT%{CookieDir}/fortune-tao

tar zxvf %{SOURCE4} -C $RPM_BUILD_ROOT%{CookieDir}/ fortune-hitchhiker/hitch*
mv $RPM_BUILD_ROOT%{CookieDir}/fortune-hitchhiker/* $RPM_BUILD_ROOT%{CookieDir}/
rmdir $RPM_BUILD_ROOT%{CookieDir}/fortune-hitchhiker

tar zxvf %{SOURCE5} -C $RPM_BUILD_ROOT%{CookieDir}/
chmod 644 $RPM_BUILD_ROOT%{CookieDir}/osfortune*

tar zxvf %{SOURCE6} -C $RPM_BUILD_ROOT%{CookieDir}/ humorixfortunes-1.4/*
mv $RPM_BUILD_ROOT%{CookieDir}/humorixfortunes-1.4/* $RPM_BUILD_ROOT%{CookieDir}/
rmdir $RPM_BUILD_ROOT%{CookieDir}/humorixfortunes-1.4

# Recreate random access files for the added fortune files.
strfile="`find . -type f -name strfile -executable -print | head -1`"
for i in \
    kernelnewbies bofh-excuses tao hitchhiker \
    osfortune humorix-misc humorix-stories \
; do "$strfile" $RPM_BUILD_ROOT%{CookieDir}/$i ; done

# Fix for https://fedoraproject.org/wiki/Changes/Broken_RPATH_will_fail_rpmbuild
#ERROR   0001: file '/usr/bin/strfile' contains a standard runpath '/usr/lib64' in [/usr/lib64]
#ERROR   0001: file '/usr/bin/unstr' contains a standard runpath '/usr/lib64' in [/usr/lib64]
#ERROR   0001: file '/usr/bin/fortune' contains a standard runpath '/usr/lib64' in [/usr/lib64]
chrpath -d %{buildroot}%{_bindir}/strfile
chrpath -d %{buildroot}%{_bindir}/unstr
chrpath -d %{buildroot}%{_bindir}/fortune

%check
%__rm -f tests/t/trailing-space*.t
%__rm -f tests/t/valgrind*.t
# The fortune-mod tests suite does not use CTest - only "[build-cmd] check"
# ctest
%cmake_build --target check

%files
%license COPYING.txt
%doc README ChangeLog TODO
%{_bindir}/fortune
%{_bindir}/strfile
%{_bindir}/unstr
%{CookieDir}
%{_mandir}/man*/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 18 2024 Shlomi Fish <shlomif@shlomifish.org> 3.24.0-1
- New upstream version

* Wed Oct 09 2024 Shlomi Fish <shlomif@shlomifish.org> 3.22.0-4
- Restore running the tests-suite. Update the build-deps ( valgrind, IO::All)

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 3.22.0-3
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 02 2024 Shlomi Fish <shlomif@shlomifish.org> 3.22.0-1
- New upstream version

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 12 2023 Shlomi Fish <shlomif@shlomifish.org> 3.20.0-1
- New upstream version

* Tue Mar 07 2023 Shlomi Fish <shlomif@shlomifish.org> 3.18.0-1
- New upstream version

* Wed Feb 22 2023 Shlomi Fish <shlomif@shlomifish.org> 3.16.0-1
- New upstream version

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 10 2022 Shlomi Fish <shlomif@shlomifish.org> 3.14.1-1
- New upstream version

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu May 05 2022 Shlomi Fish <shlomif@shlomifish.org> 3.14.0-1
- New upstream version

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 29 2021 Shlomi Fish <shlomif@shlomifish.org> 3.12.0-1
- New upstream version

* Wed Dec 15 2021 Shlomi Fish <shlomif@shlomifish.org> 3.10.0-1
- New upstream version

* Tue Dec 14 2021 Shlomi Fish <shlomif@shlomifish.org> 3.8.0-1
- New upstream version

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 13 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 3.6.1-2
- cleanup spec
- support building on EPEL8
- use --with offensive to skip removing offensive cookies

* Tue Jun 15 2021 Sérgio Basto <sergio@serjux.com> - 3.6.1-1
- Update to 3.6.1
- Fix broken RPATH

* Tue Apr 20 2021 Shlomi Fish <shlomif@shlomifish.org> 3.6.0-1
- New upstream version ; use recode again.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 11 2020 Shlomi Fish <shlomif@shlomifish.org> 3.4.1-1
- New upstream version ; use recode again.

* Fri Sep 25 2020 Shlomi Fish <shlomif@shlomifish.org> 3.2.0-1
- New upstream version

* Tue Jul 28 2020 Shlomi Fish <shlomif@shlomifish.org> 2.28.0-1
- New upstream version; cmake macros; F33 mass rebuild.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 02 2020 Shlomi Fish <shlomif@shlomifish.org> 2.26.0-1
- New upstream version, which includes fixes for integer overflows.

* Tue Apr 28 2020 Shlomi Fish <shlomif@shlomifish.org> 2.24.0-1
- New upstream version, which includes fixes for buffer overflows.

* Thu Apr 02 2020 Shlomi Fish <shlomif@cpan.org> - 2.18.0-1
- New upstream version

- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 20 2019 Petr Pisar <ppisar@redhat.com> - 2.10.0-2
- Rebuild against recode-3.7.2 (bug #1379055)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 18 2017 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.99.5-1
- Update to new upstream's latest release

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.99.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.99.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.99.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.99.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.99.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.99.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.99.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.99.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.99.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.99.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.99.1-11
- Autorebuild for GCC 4.3

* Fri Jan 11 2008 Jeff Sheltren <jeff@osuosl.org> 1.99.1-10
- Rebuild for F9

* Tue Jun  5 2007 Jeff Sheltren <sheltren@cs.ucsb.edu> 1.99.1-9
- Rebuild

* Mon Apr  9 2007 Jeff Sheltren <sheltren@cs.ucsb.edu> 1.99.1-8
- Rebuild for Fedora 7

* Sat Sep  9 2006 Jeff Sheltren <sheltren@cs.ucsb.edu> 1.99.1-7
- bump release for buildsystem

* Sat Sep  9 2006 Jeff Sheltren <sheltren@cs.ucsb.edu> 1.99.1-6
- Rebuild for FE6

* Mon Feb 20 2006 Jeff Sheltren <sheltren@cs.ucsb.edu> 1.99.1-5
- Rebuild for Fedora Extras 5

* Tue Oct  4 2005 Jeff Sheltren <sheltren@cs.ucsb.edu> 1.99.1-4
- Move fortunes into _datadir/games/fortune

* Mon Mar 21 2005 Jeff Sheltren <sheltren@cs.ucsb.edu> 1.99.1-3
- Bump version to 3 for fc4 package

* Mon Mar 14 2005 Jeff Sheltren <sheltren@cs.ucsb.edu> 1.99.1-2
- Add patch for moving fortunes into offensive directory

* Sun Mar 13 2005 Jeff Sheltren <sheltren@cs.ucsb.edu> 1.99.1-1
- Update to newer source (see URL)
- Update patches as necessary, separate cflags patch as it was only applied if applying offensive patches
- New source has recode-devel buildreq
- Remove debian fortunes which are included in new source

* Sat Nov 13 2004 Michael Schwendt <mschwendt[AT]users.sf.net> 1.0-25
- Recreate .dat files at build-time to fix x86_64 fedora.us bug #2279.
- Use %%CookieDir everywhere.
- Bump release to 25, drop Epoch.

* Sun Jun 08 2003 Michel Alexandre Salim <salimma[AT]users.sourceforge.net> 1.0-24.fdr.4
- Added Humorix fortunes
- Used $RPM_BUILD_ROOT

* Sun May 04 2003 Michel Alexandre Salim <salimma[AT]users.sourceforge.net> 1.0-24.fdr.3
- Added Tao Te Ching (fortune-tao), O'Reilly (osfortune) and H2G2 (fortune-hitchhiker) cookies
- Fixed BuildRoot
- Added Epoch
- Reverted to .tar.gz for main source, .tar.bz2 not available upstream

* Fri May 02 2003 Michel Alexandre Salim <salimma[AT]users.sourceforge.net> 1.0-24.fdr.2
- Modified installation paths to conform with Red Hat-packaged games, i.e. binaries in /usr and data files under /usr/games

* Fri May 02 2003 Michel Alexandre Salim <salimma[AT]users.sourceforge.net> 1.0-24.fdr.1
- Converted from fortune-mod-1.0-24 from RH8.0
- Updated package naming, added URL

* Thu Aug 22 2002 Mike A. Harris <mharris@redhat.com> 1.0-24
- Removed -o option from fortune, the manpage and --help message, as
  we do not provide or support the offensive fortunes for obvious
  reasons.  (#54713)
