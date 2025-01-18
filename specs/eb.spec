Name:           eb
Version:        4.4.3
Release:        27%{?dist}
Summary:        Library for accessing Japanese CD-ROM electronic books
Summary(ja):    CD-ROM 書籍にアクセスするためのライブラリ

License:        BSD-3-Clause
URL:            http://www.sra.co.jp/people/m-kasahr/eb/
Source0:        ftp://ftp.sra.co.jp/pub/misc/eb/%{name}-%{version}.tar.bz2
Patch1:         eb-aclocal-conf-libdir.patch
Patch2:         eb-gcc14.patch

BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  zlib-devel
%ifarch aarch64
BuildRequires:	autoconf
%endif

%description
EB Library is a C library for accessing CD-ROM books.
EB Library supports to access CD-ROM books of
EB, EBG, EBXA, EBXA-C, S-EBXA and EPWING formats.

%description -l ja
EB ライブラリは CD-ROM 書籍にアクセスするための C のライブラリです。
EB, EBG, EBXA, EBXA-C, S-EBXA および EPWING 形式の
CD-ROM 書籍に対応しています。


%package devel
Summary:        Development files for eb
Requires:       eb = %{version}
Requires:       zlib-devel

%description devel
This package contains development files needs to use eb in programs.


%prep
%setup -q
%patch -P1 -p1 -b .1-etc~
%patch -P2 -p1


%build
%ifarch aarch64
autoconf
%endif
%configure --disable-static --sysconfdir=%{_libdir}
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build


%install
%make_install

rm $RPM_BUILD_ROOT%{_libdir}/libeb.la

rm -rf tmp
mkdir -p tmp
mv $RPM_BUILD_ROOT%{_datadir}/eb/doc tmp/html

%find_lang %{name}
%find_lang %{name}utils
cat %{name}utils.lang >> %{name}.lang


%ldconfig_scriptlets


%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/*
%{_libdir}/libeb.so.*
%{_datadir}/eb


%files devel
%doc tmp/html
%{_includedir}/eb
%{_libdir}/eb.conf
%{_libdir}/libeb.so
%{_datadir}/aclocal/*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 08 2024 Parag Nemade <pnemade@fedoraproject.org> - 4.4.3-25
- Resolves: rhbz#2261072 - Fix FTBFS

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 11 2021 Jens Petersen <petersen@redhat.com> - 4.4.3-18
- remove RPATH to fix FTBFS (#1987434)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 12 2020 Tom Stellard <tstellar@redhat.com>
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 27 2020 Jitka Plesnikova <jplesnik@redhat.com> - 4.4.3-15
- Specify all perl dependencies for build

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Jens Petersen <petersen@redhat.com> - 4.4.3-10
- BR gcc

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep  2 2013 Jens Petersen <petersen@redhat.com> - 4.4.3-1
- update to 4.4.3

* Mon Sep  2 2013 Jens Petersen <petersen@redhat.com> - 4.4.1-9
- run autoconf for aarch64 (#926499)
- cleanup buildroot and defattr lines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 4.4.1-7
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.1-3
- Rebuilt for glibc bug#747377

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 31 2009 Jens Petersen <petersen@redhat.com> - 4.4.1-1
- update to 4.4.1 (Mamoru Tasaka, #518072)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 14 2008 Jens Petersen <petersen@redhat.com> - 4.3.2-1
- update to 4.3.2

* Wed Feb 14 2007 Jens Petersen <petersen@redhat.com> - 4.3-2
- eb-devel requires zlib-devel (#228243)
- move eb.conf build config file to eb-devel and libdir
- add eb-aclocal-conf-libdir.patch to update eb.conf location

* Mon Feb 12 2007 Jens Petersen <petersen@redhat.com> - 4.3-1
- initial packaging for Fedora (#228241)
