%bcond_with largefile

Summary: A GNU set of database routines which use extensible hashing
Name: compat-gdbm
Version: 1.14.1
Release: 24%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
URL: http://www.gnu.org/software/gdbm/

Source: http://ftp.gnu.org/gnu/gdbm/gdbm-%{version}.tar.gz
# See https://bugzilla.redhat.com/show_bug.cgi?id=4457
# Upstream bug http://puszcza.gnu.org.ua/bugs/?func=detailitem&item_id=151
# Fixed in http://cvs.gnu.org.ua/viewvc/gdbm/gdbm/src/gdbmopen.c?r1=1.12&r2=1.13
# - version 1.10
#Patch0: gdbm-1.10-zeroheaders.patch

Patch1: gdbm-1.10-fedora.patch
Patch2: gdbm_gcc_10.patch

BuildRequires: gcc
BuildRequires: libtool
BuildRequires: gettext
BuildRequires: readline-devel
BuildRequires: make
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
This is package is used only for rebase of gdbm in Fedora.
Don't use it!

Gdbm is a GNU database indexing library, including routines which use
extensible hashing.  Gdbm works in a similar way to standard UNIX dbm
routines.  Gdbm is useful for developers who write C applications and
need access to a simple and efficient database or who are building C
applications which will use such a database.

If you're a C developer and your programs need access to simple
database routines, you should install gdbm.  You'll also need to
install gdbm-devel.

%package libs
Summary: Libraries files for gdbm

%description libs
Libraries for the Gdbm GNU database indexing library

%package devel
Summary: Development libraries and header files for the gdbm library
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires(post): info
Requires(preun): info

%description devel
Gdbm-devel contains the development libraries and header files for
gdbm, the GNU database system.  These libraries and header files are
necessary if you plan to do development using the gdbm database.

Install gdbm-devel if you are developing C programs which will use the
gdbm database library.  You'll also need to install the gdbm package.

%prep
%setup -q -n gdbm-%{version}
%patch -P1 -p1 -b .fedora
%patch -P2 -p1

%build
%configure \
    --disable-static \
%{!?with_largefile: --disable-largefile} \
    --disable-rpath

# get rid of rpath (as per https://fedoraproject.org/wiki/Packaging:Guidelines#Beware_of_Rpath)
# currently --disable-rpath doesn't work for gdbm_dump|load, gdbmtool and libgdbm_compat.so.4
# https://puszcza.gnu.org.ua/bugs/index.php?359
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

# create symlinks for compatibility
mkdir -p $RPM_BUILD_ROOT/%{_includedir}/gdbm 
ln -sf ../gdbm.h $RPM_BUILD_ROOT/%{_includedir}/gdbm/gdbm.h
ln -sf ../ndbm.h $RPM_BUILD_ROOT/%{_includedir}/gdbm/ndbm.h
ln -sf ../dbm.h $RPM_BUILD_ROOT/%{_includedir}/gdbm/dbm.h

# Remove libtool archives
find %{buildroot} -type f -name "*.la" -delete

rm -f $RPM_BUILD_ROOT/%{_infodir}/dir

rm -rf %{buildroot}%{_datadir}/locale

# Remove binaries from compat library
rm %{buildroot}%{_bindir}/gdbm*
rm %{buildroot}%{_mandir}/man1/gdbm*

%check
export LD_LIBRARY_PATH=`pwd`/src/.libs/:`pwd`/compat/.libs/
make check

%ldconfig_scriptlets libs

%files
%doc NEWS README THANKS AUTHORS NOTE-WARNING

%files libs
%license COPYING
%{_libdir}/libgdbm.so.5*

%files devel
%{_libdir}/libgdbm.so
%{_includedir}/*
%{_infodir}/*.info*
%{_mandir}/man3/*

%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.14.1-22
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 10 2020 Filip Januš <fjanus@redhat.com> - 1.14.1-11
- Resolves: #1799246
- After upgrade GCC to version gcc version 10.0.1 build fails
- Patch gdbm_gcc_10.patch was added

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 mskalick@redhat.com - 1.14.1-6
- Remove binaries from compat-gdbm rpm - they conflicted with binaries from gdbm

* Wed Jul 04 2018 mskalick@redhat.com - 1.14.1-5
- Rebase to 1.14.1 from Rawhide to allow soname bump in Rawhide (gdbm is in
  minimal buildroot)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Marek Skalický <mskalick@redhat.com> - 1.14-4
- Rebase to 1.14 from Rawhide to allow soname bump in Rawhide (gdbm is in
  minimal buildroot)
- Remove files which might conflict with gdbm package

* Tue Jan 16 2018 Marek Skalický <mskalick@redhat.com> - 1:1.14-3
- Fix -devel require to include also epoch

* Tue Jan 16 2018 Marek Skalický <mskalick@redhat.com> - 1:1.14-2
- Introduce epoch to not to break upgrade path from F27

* Wed Jan 03 2018 Petr Kubat <pkubat@redhat.com> - 1.14-1
- Upgrade to gdbm 1.14
- Resolves #1467431

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 23 2017 Marek Skalický <mskalick@redhat.com> - 1.13-1
- Upgrade to gdbm 1.13

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Mar 17 2016 Marek Skalicky <mskalick@redhat.com> - 1.12-1
- Upgrade to gdbm-1.12 (#1336604)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 1.11-5
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jul 12 2014 Tom Callaway <spot@fedoraproject.org> - 1.11-3
- fix license handling

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 05 2014 Honza Horak <hhorak@redhat.com> - 1.11-1
- Upgrade to gdbm-1.11
  Resolves: #1046643

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 25 2013 Honza Horak <hhorak@redhat.com> - 1.10-6
- Fixed some issues found by Coverity
- Add support of aarch64

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug 27 2012 Honza Horak <hhorak@redhat.com> - 1.10-4
- Spec file cleanup
- Use make DESTDIR=... install instead of %%make_install

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 14 2011 Honza Horak <hhorak@redhat.com> - 1.10-1
- Updated to new upstream release 1.10
- Dropped -shortread patch, which has been already applied by upstream
- Disable large file support, that is enabled by default since 1.9, 
  but not compatible with db files created using gdbm-1.8.3 and lower
- License change to GPLv3+
- Add doc files THANKS AUTHORS NOTE-WARNING
- Changed text in NOTE-WARNING to correspond with build settings

* Tue Sep 20 2011 Honza Horak <hhorak@redhat.com> - 1.9.1-1
- Updated to new upstream release 1.9.1
- Dropped -filestruct, -ndbmlock and -fhs patches, they are not 
  needed anymore and GDBM_NOLOCK is used always
- Run testsuite

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 13 2011 Jan Horak <hhorak@redhat.com> - 1.8.3-8
- Added filestruct patch (#668178)

* Mon Jan 03 2011 Karel Klic <kklic@redhat.com> - 1.8.3-7
- Removed BuildRoot tag
- Removed %%clean section
- Added ndbmlock patch (#663932)

* Mon Apr 12 2010 Karel Klic <kklic@redhat.com> - 1.8.3-6
- Use fcntl instead of flock for locking to make nfs safe (#477300)

* Thu Mar 11 2010 Karel Klic <kklic@redhat.com> - 1.8.3-5
- Removed fake Provides: libgdbm.so.2 and corresponding symlinks
- Moved autoconf, libtoolize from %%build to %%prep section
- Remove static builds from the devel package (#556050)

* Thu Mar 11 2010 Karel Klic <kklic@redhat.com> - 1.8.3-4
- Provides: libgdbm.so.2()(64bit) for x86_64 architecture

* Thu Mar 11 2010 Karel Klic <kklic@redhat.com> - 1.8.3-3
- Added temporary symlinks to retain compatibility with gdbm 1.8.0

* Wed Mar 10 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.8.3-2
- %%files: track shlib sonames, so abi breaks are less of a surprise

* Tue Mar 09 2010 Karel Klic <kklic@redhat.com> - 1.8.3-1
- Newer upstream release
- Removed gdbm-1.8.0-64offset.patch, because it was merged by the upstream
- `jbj' patch extended and renamed to `zeroheaders'
- Added shortread patch from Debian

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Apr 17 2009 Stepan Kasal <skasal@redhat.com> - 1.8.0-32
- Clean up the spec, for merge review.

* Fri Feb 27 2009 Stepan Kasal <skasal@redhat.com> - 1.8.0-31
- drop *-cflags.patch, move all makefile fixes to *-fhs.patch
- propagate libdir to Makefile; no need to set it on cmdline

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jul 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.8.0-29
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.8.0-28
- Autorebuild for GCC 4.3

* Tue Apr 3 2007 Ondrej Dvoracek <odvorace@redhat.com> - 1.8.0-27
- made install-info use in scriptlets safe (#223688)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.8.0-26.2.1
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.8.0-26.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.8.0-26.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 24 2006 Warren Togami <wtogami@redhat.com> 1.8.0-26
- remove .la (#171535)

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Sat Apr 09 2005 Florian La Roche <laroche@redhat.com>
- rebuild

* Sun Aug  8 2004 Alan Cox <alan@redhat.com> 1.8.0-24
- Close bug #125319

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Oct  4 2002 Nalin Dahyabhai <nalin@redhat.com> 1.8.0-19
- rebuild

* Fri Sep 13 2002 Nalin Dahyabhai <nalin@redhat.com> 1.8.0-18.1
- run make with libdir overridden so that it has the value passed to configure
  instead of $(prefix)/lib

* Wed Jul 24 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.8.0-18
- Remove cflags for large database support - not compatible 
  with databases without it

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Apr 25 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.8.0-15
- Use 64bit offset
- Patch to make the above not break from downsj@downsj.com (#63980) 

* Tue Feb 26 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.8.0-14
- Rebuild

* Fri Jan 25 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.8.0-13
- Update location
- auto* changes to make it build

* Wed Oct 17 2001 Trond Eivind Glomsrød <teg@redhat.com> 1.8.0-11
- Add URL (# 54607)

* Mon Jun 25 2001 Nalin Dahyabhai <nalin@redhat.com>
- s/Copyright:/License:/g
- include text docs in binary package

* Tue Jun 12 2001 Than Ngo <than@redhat.com>
- fix to build against new libtool

* Mon Mar 19 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Make it respect RPM_OPT_FLAGS/CFLAGS - #32242. 
  Patch from dan@D00M.cmc.msu.ru

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jun  5 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging.

* Mon Feb  7 2000 Bill Nottingham <notting@redhat.com>
- handle compressed manpages

* Tue Aug 10 1999 Jeff Johnson <jbj@redhat.com>
- make sure created database header is initialized (#4457).

* Tue Jun  1 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.8.0.
- repackage to include /usr/include/gdbm/*dbm.h compatibility includes.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 19)

* Thu Dec 17 1998 Cristian Gafton <gafton@redhat.com>
- build against glibc 2.1

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- gdbm-devel moved to Development/Libraries

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- buildroot and built for Manhattan

* Tue Oct 14 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Thu Jun 12 1997 Erik Troan <ewt@redhat.com>
- built against glibc
