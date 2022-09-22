Name:           libgringotts
Version:        1.2.1
Release:        32%{?dist}
Summary:        A backend for managing encrypted data files on the disk
Summary(pl):    Zaplecze do zarządzania zaszyfrowanymi plikami danych na dysku

License:        GPLv2+
URL:            http://gringotts.shlomifish.org/
Source0:        http://download.berlios.de/gringotts/%{name}-%{version}.tar.bz2
Patch0:         libgringotts-1.2.1-aarch64.patch

BuildRequires:  gcc
BuildRequires:  bzip2-devel
BuildRequires:  libmcrypt-devel
BuildRequires:  mhash-devel
BuildRequires:  zlib-devel
BuildRequires: make


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
Requires:       libgringotts = %{version}-%{release} pkgconfig

%description    devel
The libgringotts-devel package contains libraries and header files for
developing applications that use libgringotts.

%description    devel -l pl
Pakiet libgringotts-devel zawiera biblioteki i pliki nagłówków 
niezbędne do tworzenia aplikacji, które używają libgringotts.


%prep
%setup -q
%patch0 -p1 -b .aarch64

%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT libgringottsdocdir=%{_pkgdocdir}
#pcdir="%{RPM_BUILD_ROOT}%{_libdir}/pkgconfig/"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%ldconfig_scriptlets


%files
%{_pkgdocdir}
%exclude %{_pkgdocdir}/manual.htm
%{_libdir}/*.so.*

%files devel
%{_pkgdocdir}/manual.htm
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*


%changelog
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
