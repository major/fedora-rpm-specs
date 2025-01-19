Name:           libgringotts
Version:        1.2.1
Release:        42%{?dist}
Summary:        A backend for managing encrypted data files on the disk
Summary(pl):    Zaplecze do zarządzania zaszyfrowanymi plikami danych na dysku

# SPDX confirmed
License:        GPL-2.0-or-later
URL:            http://gringotts.shlomifish.org/
Source0:        http://download.berlios.de/gringotts/%{name}-%{version}.tar.bz2
# Patch for bzip2 algo size fix for big endian
Patch0:         libgringotts-1.2.1-bzip2-algo-bigendian-sizefix.patch

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make

BuildRequires:  bzip2-devel
BuildRequires:  libmcrypt-devel
BuildRequires:  mhash-devel
BuildRequires:  zlib-devel


%description
libGringotts is a small, easy-to-use, thread-safe C library
 originally developed for Gringotts; its purpose is to 
encapsulate data (generic: ASCII, but also binary data) 
in an encrypted and compressed structure, to be written 
in a file or used elseway. It makes use of strong 
encryption algorithms, to ensure the data are as safe 
as possible, and allow the user to have the complete 
control over all the algorithms used in the process.

%description        -l pl
libGringotts to niewielka, łatwa w użyciu biblioteka 
napisana w C, początkowo tworzona dla Gringotts. 
Jej zadaniem jest przechowywanie danych 
(głównie: ASCII, ale równiez binarnych) w zaszyfrowanej 
i skompresowanej strukturze, zapisywanej np. w pliku.
Używa ona silnych algorytmów szyfrujących 
dla maskymalnego bezpieczeństwa danych 
oraz by zapewnić użytkownikowi pełną kontrolę nad nimi.


%package        devel
Summary:        Development files for libgringotts
Summary(pl):    Pliki deweloperskie dla libgringotts
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The libgringotts-devel package contains libraries and header files for
developing applications that use libgringotts.

%description    devel -l pl
Pakiet libgringotts-devel zawiera biblioteki i pliki nagłówków 
niezbędne do tworzenia aplikacji, które używają libgringotts.


%prep
%setup -q
%patch -P0 -p1 -b .bigendian

# For check
sed -i src/Makefile.am \
	-e 's|\(^[ \t][ \t]*\)@|\1|' \
	-e 's|test.c .libs/libgringotts.a|test.c -L.libs -lgringotts|' \
	-e 's|./libgrgtest|env LD_LIBRARY_PATH=.libs ./libgrgtest|' \
	%{nil}

autoreconf -fi

%build
%configure --disable-static
%make_build

%install
%make_install

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
# Clean up documentation directory
rm -rf $RPM_BUILD_ROOT%{_docdir}

%check
# Some tests e.g. 8) Password quality test (strings) reads /dev/random
# so tests may fail randomly.
# Repeat tests several times to rescue such failure.
test_status=1
for times in $(seq 1 3) ; do
	make check || continue
	test_status=0
	break
done
if test $test_status != 0 ; then exit 1 ; fi

%ldconfig_scriptlets

%files
%license	COPYING
%doc	AUTHORS
%doc	ChangeLog
%doc	NEWS
%doc	README
%doc	TODO

%{_libdir}/%{name}.so.2{,.*}

%files devel
%doc	docs/manual.htm
%{_includedir}/libgringotts.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri May 31 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.1-40
- Rebuild for %%patch macro usage update

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb  1 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.1-36
- Repeat tests to rescue test failure due to internal randomness

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 25 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.1-34
- Fix for big endian for bzip2 compression

* Fri Nov 25 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.1-33
- Call autoconf to remove huge patch for config.guess
- Execute check (rescue for big endian for now)
- Use SPDX license tag
- Avoid glob for %%files entry where preferable

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 13 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.1-26
- Fix FTBFS (bug 1734822)
 - Fix BR

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.1-23
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 27 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.2.1-15
- Reflect package is installing into %%{_pkgdocdir} directly.

* Thu Jun 19 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 1.2.1-14
- Fix for F20UnversionedDocdirs (#992085, #1106018)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 19 2013  Christoph Wickert <cwickert@fedoraproject.org> - 1.2.1-11
- Add aarch64 support (#925751)
- Spec file clean-up

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 06 2008 Jakub 'Livio' Rusinek <jakub.rusinek@gmail.com> - 1.2.1-4
- Shortened lines of text in description... Fixed

* Mon Feb 04 2008 Jakub 'Livio' Rusinek <jakub.rusinek@gmail.com> - 1.2.1-3
- Summary... Fixed
- Description... Fixed
- Requires for -devel... Fixed

* Mon Jan 28 2008 Jakub 'Livio' Rusinek <jakub.rusinek@gmail.com> - 1.2.1-2
- Summary and description... Fixed

* Sat Jan 26 2008 Jakub 'Livio' Rusinek <jakub.rusinek@gmail.com> - 1.2.1-1
- Initial package
