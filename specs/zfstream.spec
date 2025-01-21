%global vday 02
%global vmonth 12
%global vyear 2004

Name:           zfstream
Version:        %{vyear}%{vmonth}%{vday}
Release:        42%{?dist}
Summary:        Library for reading and writing compressed and non-compressed files

License:        LGPL-2.1-or-later
URL:            http://www.wanderinghorse.net/computing/%{name}/
Source0:        http://www.wanderinghorse.net/computing/%{name}/libs11n_%{name}-%{vyear}.%{vmonth}.%{vday}.tar.gz
# I tried half a day to get the rather peculiar original build system working,
# but I failed, so I decided to simply replace it by autotools.
# This has the further advantage that it knows how to cross-compile,
# as evidenced by the mingw32-zfstream package also under review.
Source1:        %{name}-autotools.tar.gz
# The patch has been sent via private mail to the author. The author responded
# that the patch had been integrated into his personal tree, but apparently
# he has not gotten around to release a new version.
Patch1:         %{name}-zip.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  bzip2-devel
BuildRequires:  libtool
BuildRequires:  minizip-ng-compat-devel

%description
zfstream is a small C++ library which provides an abstraction API for reading
and writing compressed and non-compressed files using the same API. It supports
libz and libbz2 compression schemes. The library is trivial to use and provides
client applications with a unified interface for reading and writing files
without having to know whether they are compressed or not.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
Requires:       bzip2-devel
Requires:       zlib-devel 

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n libs11n_%{name}-%{vyear}.%{vmonth}.%{vday} -a 1
%patch -P1 -p0 -b .zip
aclocal
autoconf
autoheader
libtoolize -f
touch NEWS README AUTHORS
automake -a -c

%build
%configure --disable-static
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'



%ldconfig_scriptlets


%files
%{_libdir}/*.so.*

%files devel
%doc ChangeLog
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 04 2023 Lukas Javorsky <ljavorsk@redhat.com> - 20041202-39
- Rebuilt for minizip-ng transition Fedora change
- Fedora Change: https://fedoraproject.org/wiki/Changes/MinizipNGTransition

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 15 2022 Sandro Mani <manisandro@gmail.com> - 20041202-36
- Rebuild (minizip-ng)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Feb 09 2021 Miro Hrončok <mhroncok@redhat.com> - 20041202-32
- Rebuilt for minizip 3.0.0

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20041202-27
- add missing library to pkgconf file
- use pkgconf for zlib and bzip2

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 24 2018 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20041202-25
- use minizip instead of minizip-compat

* Tue Aug 28 2018 Patrik Novotný <panovotn@redhat.com - 20041202-24
- change requires to minizip-compat(-devel), rhbz#1609830, rhbz#1615381

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 20041202-23
- Rebuild with fixed binutils

* Sun Jul 29 2018 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20041202-22
- explicitly add gcc and g++ to the build root

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20041202-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 20041202-15
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20041202-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20041202-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20041202-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20041202-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20041202-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20041202-9
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20041202-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20041202-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20041202-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May  1 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20041202-5
- rebuild

* Fri May  1 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20041202-4
- reformat description

* Thu Apr 30 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20041202-3
- use %%{name} macro (more)
- remove minizip from Source1
- shortened summary
- fix BR/R

* Tue Nov  4 2008 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20041202-2
- changed description
- added unused-direct-shlib-dependency trick
- add library dependences

* Thu Dec 27 2007 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20041202-1
- initial packaging

