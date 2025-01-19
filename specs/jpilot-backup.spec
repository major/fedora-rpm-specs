Summary: Enhanced backup plugin for J-Pilot
Name: jpilot-backup
Version: 0.60
Release: 41%{dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Source: http://www.jlogday.com/code/jpilot-backup/%{name}-%{version}.tar.gz
Patch0: jpilot-backup-libdir.patch
Patch1: jpilot-backup-configure-c99.patch
URL: http://www.jlogday.com/code/jpilot-backup/
Requires: jpilot >= 0.99.2
BuildRequires:  gcc
BuildRequires: pilot-link-devel
BuildRequires: gtk2-devel
BuildRequires: gdbm-devel
BuildRequires: make

# pilot-link excludes s390 and s390s, as such I must also exclude those arches
ExcludeArch: s390 s390x

%description
Features include multiple archives, automatic backups at user-specified times,
and the ability to specify which databases to backup.

%prep
%setup -n %{name}-%{version} -q
%patch -P0 -p1 -b .libdir
%patch -P1 -p1 -b .c99

%build
%configure --libdir=/%{_lib}/jpilot/plugins --with-pilot-prefix=%{_prefix}

make %{?_smp_mflags}

%install
make prefix=$RPM_BUILD_ROOT%{_prefix} install

# manually remove the libtool archive
find %{buildroot} -type f -name "*.la" -delete


%files
%doc README README.NFS ChangeLog CREDITS TODO
%license COPYING
%{_libdir}/jpilot/plugins/libbackup.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.60-40
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 12 2022 Florian Weimer <fweimer@redhat.com> - 0.60-34%{dist}
- Port configure script to C99

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri May 20 2016 Till Maas <opensource@till.name> - 0.60-20
- Remove uneeded %%if condition

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb 02 2015 Patrick C. F. Ernzer <jpilot-backup.spec@pcfe.net> 0.60-17
- COPYING now listed as a license
- adjusted isa_bits test for latest build system changes

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 25 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.60-15
- Remove aarch64 patch (handled in %%configure macro)
- Generalise 64 bit arch detection
- Cleanup spec

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 25 2013 Patrick C. F. Ernzer <jpilot-backup.spec@pcfe.net> 0.60-12
- update config.guess and config.sub to recognize aarch64 (RHBZ #925611)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 30 2011 Patrick C. F. Ernzer <jpilot-backup.spec@pcfe.net> 0.60-8
- Rebuilt against new gdbm-1.9.1-1 as per email request Fri, 30 Sep 2011 15:28:31 +0200

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Mar 14 2010 Patrick C. F. Ernzer <jpilot-backup.spec@pcfe.net> 0.60-6
- Rebuilt for gdbm soname change

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 26 2009 Patrick C. F. Ernzer <jpilot-backup.spec@pcfe.net> 0.60-4
- added a comment as to why I exclude s390 and s390s

* Tue May 26 2009 Patrick C. F. Ernzer <jpilot-backup.spec@pcfe.net> 0.60-3
- pilot-link excludes s390 and s390s, so this package needs to do the same

* Wed Feb 25 2009 Patrick C. F. Ernzer <jpilot-backup.spec@pcfe.net> 0.60-2
- fixed patch with help of Phil K. Thanks

* Sat Feb 21 2009 Patrick C. F. Ernzer <jpilot-backup.spec@pcfe.net> 0.60-1
- bump to 0.60
- new site for jpilot-backup

* Tue Dec 16 2008 Patrick C. F. Ernzer <jpilot-backup.spec@pcfe.net> 0.53-5
- incorporate feedback from Bug 474768 Comments #5

* Wed Dec 10 2008 Patrick C. F. Ernzer <jpilot-backup.spec@pcfe.net> 0.53-4
- incorporate feedback from Bug 474768 Comments #1, #2 and #3

* Fri Dec 05 2008 Patrick C. F. Ernzer <jpilot-backup.spec@pcfe.net> 0.53-3
- minor cleanups to remove rpmlint warnings
- BuildRequires gtk2-devel and gdbm-devel added
- Requires gdbm added

* Thu Nov 27 2008 Patrick C. F. Ernzer <jpilot-backup.spec@pcfe.net> 0.53-2
- add libdir patch so this compiles on x86_64

* Thu Jun 14 2007 Patrick C. F. Ernzer <jpilot-backup.spec@pcfe.net> 0.53
- bump to 0.53
- changed obsolete Copyright tag to current License tag

* Wed Jan 29 2003 Jason Day <jasonday@worldnet.att.net> 0.50
- Added README.NFS to docs

* Mon Oct 14 2002 Jason Day <jasonday@worldnet.att.net> 0.43
- Bump version

* Tue May 14 2002 Jason Day <jasonday@worldnet.att.net> 0.42
- Minor misc cleanup
- Added TODO to dist files

* Sun Apr  7 2002 Jason Day <jasonday@worldnet.att.net> 0.41.2-1
- incorporated Sylvain's changes into main trunk, making patch
  unnecessary

* Sat Feb  9 2002 Sylvain Holtzer <sylvain.holtzer@free.fr> 0.41.2-0.sho1
- minor fixes : "version" upgraded ; requires jpilot-0.99.2 ;
- added sho1.patch, so we don't need superuser privileges (Makefile.in,
  and this .spec - see (v01) pattern) ;
- used rpm macros, and "make install" ;
- installs libbackup.la ;

