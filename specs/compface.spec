Name:           compface
Version:        1.5.2
Release:        42%{?dist}
Summary:        Library and tools for handling X-Face data

License:        LicenseRef-compface
URL:            http://ftp.xemacs.org/pub/xemacs/aux/
Source0:        http://ftp.xemacs.org/pub/xemacs/aux/%{name}-%{version}.tar.gz
Source1:        compface-test.xbm
Source2:        compface-README.copyright
# originally from http://ftp.debian.org/debian/pool/main/libc/libcompface/libcompface_1.5.2-4.diff.gz
# libcompface_1.5.2-5.diff.gz adds a different fix for the stack-smashing
Patch0:         libcompface_1.5.2-4.diff.gz
# originally sent upstream
Patch1:         compface-1.5.2-stack-smashing.patch
#
Patch2:         compface-1.5.2-build.patch
Patch3: compface-configure-c99.patch
Patch4: compface-c99.patch
BuildRequires:  diffutils
BuildRequires:  gcc
BuildRequires: make

%description
This is the Compface image compression and decompression library and its
user tools. Compface converts 48x48 .xbm format (X bitmap) images to a
compressed format that can be placed in the X-Face: mail header. Some mail
programs are able to display such images when opening messages.

%package        devel
Summary:        Library and development files for handling X-Face data 
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
These files are needed when building software that uses the Compface
library.


%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1 -b .stack-smashing
%patch -P2 -p0
%patch -P3 -p1
%patch -P4 -p1


%build
CFLAGS="$RPM_OPT_FLAGS -fPIC" %configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT STRIP=/bin/true
mkdir -p _extdoc && install -p -m 0644 %{SOURCE2} _extdoc/README.copyright


%check
export LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}:$LD_LIBRARY_PATH
./compface %{SOURCE1} | ./uncompface -X > __test.xbm
cmp %{SOURCE1} __test.xbm


%files
%doc ChangeLog README xbm2xface.pl
%license _extdoc/README.copyright
%{_bindir}/compface
%{_bindir}/uncompface
%{_libdir}/libcompface.so.*
%{_mandir}/man1/compface.1*
%{_mandir}/man1/uncompface.1*

%files devel
%{_includedir}/compface.h
%{_libdir}/libcompface.so
%{_mandir}/man3/compface.3*
%{_mandir}/man3/uncompface.3*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug  7 2024 Michael Schwendt <mschwendt@fedoraproject.org> - 1.5.2-41
- migrated to SPDX license based on license review ticket #555
- include README.copyright file as license

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 06 2023 Florian Weimer <fweimer@redhat.com> - 1.5.2-36
- Fix C99 compatibility issues (#2167369)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 1.5.2-19
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan  6 2012 Michael Schwendt <mschwendt@fedoraproject.org> - 1.5.2-13
- rebuild for GCC 4.7 as requested
- drop obsolete items from spec file, plus use %%?dist and %%?_isa

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 15 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 1.5.2-10
- Minor spec updates.
- Sync with Debian's most recent 1.5.2-4 patchset, although it doesn't
  add anything for us compared with 1.5.2-3.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat May 31 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 1.5.2-8
- Drop "|| :" from check section. It failed to build for mdomsch
  in Rawhide today.

* Fri Feb 08 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 1.5.2-7
- rebuilt for GCC 4.3 as requested by Fedora Release Engineering

* Tue Aug 21 2007 Michael Schwendt <mschwendt@fedoraproject.org> - 1.5.2-6
- rebuilt

* Thu Jan  4 2007 Michael Schwendt <mschwendt@fedoraproject.org> - 1.5.2-5
- rebuilt
- Update summaries and url.

* Mon Aug 28 2006 Michael Schwendt <mschwendt@fedoraproject.org> - 1.5.2-4
- rebuilt

* Sat Aug  5 2006 Michael Schwendt <mschwendt@fedoraproject.org> - 1.5.2-3
- Add licence terms clarification from Debian's patch.

* Fri Aug  4 2006 Michael Schwendt <mschwendt@fedoraproject.org> - 1.5.2-2
- Add patch to prevent sscanf stack smashing through Debian's patch.
- Fix two GCC warnings in the same patch.
- Add one test to the %%check section and BR diffutils.

* Wed Aug  2 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.5.2-1
- Update to 1.5.2, apply Debian's 1.5.2-3 patchset.
- Crudely patch to build a shared lib (inspired by Debian), drop static one.
- Split -devel subpackage.

* Mon Jul 31 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4-7
- Ensure proper doc file permissions.

* Mon Feb 13 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4-6
- Rebuild.

* Fri Apr  7 2005 Michael Schwendt <mschwendt@fedoraproject.org> - 1.4-5
- rebuilt

* Fri Dec 17 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.4-4
- Let rpmbuild take care of stripping binaries.

* Fri May 30 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.4-0.fdr.3
- Add URL, other minor specfile tweaks (#63).

* Sat May  3 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.4-0.fdr.2
- Fix build on RH9 (#63).
- Save .spec in UTF-8.
- Provide -devel to ease possible future 'shared lib'ification.

* Sat Mar 22 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.4-0.fdr.1
- Update to current Fedora guidelines.

* Fri Feb  7 2003 Ville Skyttä <ville.skytta at iki.fi> - 1.4-1.fedora.1
- First Fedora release.
