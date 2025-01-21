%global subversion 417.1

Name:           xar
Version:        1.8.0.%{subversion}
Release:        15%{?dist}
Summary:        The eXtensible ARchiver
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://opensource.apple.com/source/xar
Source:         https://opensource.apple.com/tarballs/xar/xar-%{subversion}.tar.gz
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  libxml2-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
BuildRequires:  bzip2-devel
BuildRequires:  gawk
BuildRequires:  autoconf


#First 4 patches taken from Gentoo Xar package. To make Xar more suitable for Linux systems
#Copyright Gentoo authors 2019 GPLv2
Patch0:         xar-1.6.1-ext2.patch
Patch1:         xar-1.8-safe_dirname.patch
Patch2:         xar-1.8-arm-ppc.patch
Patch3:         xar-1.8-openssl-1.1.patch

Patch4:         xar-1.8-Add-OpenSSL-To-Configuration.patch
Patch5:         xar-1.8-gnuconfig.patch


%description
The XAR project aims to provide an easily extensible archive format. Important
design decisions include an easily extensible XML table of contents for random
access to archived files, storing the toc at the beginning of the archive to
allow for efficient handling of streamed archives, the ability to handle files
of arbitrarily large sizes, the ability to choose independent encodings for
individual files in the archive, the ability to store checksums for individual
files in both compressed and uncompressed form, and the ability to query the
table of content's rich meta-data.


%package devel
Summary: Development files for the eXtensible ARchiver
Requires: %{name} = %{version}-%{release}

%description devel
Development files for the eXtensible ARchiver.


%prep
%setup -n xar-%{subversion}
pushd xar
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
sed 's:-Wl,-rpath,::g' -i configure.ac #No rpath
sed 's:filetree.h:../lib/filetree.h:g' -i src/xar.c #Fix path
sed 's:util.h:../lib/util.h:g' -i src/xar.c #Fix path
popd

%build
pushd xar
env NOCONFIGURE=1 ./autogen.sh
%configure --disable-static
make %{?_smp_mflags}
popd


%install
pushd xar
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/libxar.la #Not needed
popd

%ldconfig_scriptlets


%files
%doc README xar/ChangeLog xar/TODO
%license xar/LICENSE
%{_bindir}/xar
%{_libdir}/libxar.so.*
%{_mandir}/man1/xar.1*

%files devel
%{_includedir}/xar/
%{_libdir}/libxar.so


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0.417.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.8.0.417.1-14
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0.417.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0.417.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0.417.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0.417.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 1.8.0.417.1-9
- Enable build on aarch64, ppc64le

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0.417.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0.417.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.8.0.417.1-6
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0.417.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0.417.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0.417.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0.417.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 2020 Mosaab Alzoubi <moceap[AT]hotmail[DOT]com> - 1.8.0.417.1-1
- Use Apple upstream instead of non-fresh Github one
- New upstream in 1.8 dev branch with 417.1 subversion
- Close CVE-2018-17093
- Close CVE-2018-17094
- Close CVE-2017-11124
- Close CVE-2017-11125
- Close CVE-2010-3798
- Use license macro
- Add OpenSSL To Configuration

* Wed Jan 1 2020 Mosaab Alzoubi <moceap[AT]hotmail[DOT]com> - 1.6.1-1
- Update to 1.6.1
- Change upstream
- Exclude CVE-2010-0055 patch, includes in upstream
- Exclude norpath patch, using sed
- Pass FTBFS state #1676224
- General clean of the spec
- Use Fedora guide lines in Source URL 

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Apr 28 2010 Matthias Saou <http://freshrpms.net/> 1.5.2-6
- Include patch to fix CVE-2010-0055 (#570678).

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.5.2-5
- rebuilt with new openssl

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Tomas Mraz <tmraz@redhat.com> 1.5.2-2
- rebuild with new openssl

* Tue Dec 23 2008 Matthias Saou <http://freshrpms.net/> 1.5.2-1
- Update to 1.5.2.
- Remove no longer needed install and memset patches.
- Disable newly built-by-default static lib and remove useless .la file.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> 
- Autorebuild for GCC 4.3

* Fri Dec 07 2007 Release Engineering <rel-eng at fedoraproject dot org> 
- Rebuild for deps

* Thu Aug 23 2007 Matthias Saou <http://freshrpms.net/> 1.5.1-4
- Rebuild for new BuildID feature.
- Add /usr/bin/awk build requirement, needed for the libxml configure check.

* Wed Aug  8 2007 Matthias Saou <http://freshrpms.net/> 1.5.1-2
- Patch memset call with swapped arguments (Dave Jones).

* Wed Jul 11 2007 Matthias Saou <http://freshrpms.net/> 1.5.1-1
- Update to 1.5.1.

* Wed May 30 2007 Matthias Saou <http://freshrpms.net/> 1.5-1
- Update to 1.5.
- Include patch to remove rpath.
- Include patch to fix file modes, and get the lib properly stripped.

* Sun Feb 25 2007 Matthias Saou <http://freshrpms.net/> 1.4-1
- Initial RPM release.
