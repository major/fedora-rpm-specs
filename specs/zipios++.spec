# define these if using CVS version
%global cvs_date 2007.04.28
%global cvs_ver +cvs.%cvs_date

Name:           zipios++
Version:        0.1.5.9
Release:        35%{dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
Summary:        C++ library for reading and writing Zip files
Summary(pl.UTF-8): Biblioteka C++ do odczytu i zapisu plików Zip
URL:            http://zipios.sourceforge.net/
# Upstream is dead. Using updated Debian source as they are fixing FTBFS issues.
Source0:        ftp://ftp.debian.org/debian/pool/main/z/%{name}/%{name}_%{version}%{cvs_ver}.orig.tar.gz

# Patches extracted from debian diff
# ftp://ftp.debian.org/debian/pool/main/z/zipios++
Patch0:         zipios++-cstdlib.patch
Patch1:         zipios++-amd64_fix.patch
Patch2:         zipios++-fc16-ptrdiff_t.patch
Patch3:         zipios++-zipinputstreambuff.patch
Patch4:         0001-cppunit-config-no-longer-exists-use-pkg-config.patch
Patch10:        zipios++-zipheadio-size0.patch


BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libstdc++-devel
BuildRequires:  libtool
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  graphviz
BuildRequires:  ImageMagick
BuildRequires:  doxygen


%description
Zipios++ is a java.util.zip-like C++ library for reading and writing
Zip files. Access to individual entries is provided through standard
C++ iostreams. A simple read-only virtual file system that mounts
regular directories and zip files is also provided.

%description -l pl.UTF-8
Zipios++ jest jak java.util.zip biblioteką C++ do odczytywania oraz
zapisywania plików Zip. Dostęp do pojedyńczych wpisów jest możliwy
poprzez standardowe strumienie we/wy C++. Prosty wirtualny system
plików (tylko do odczytu) montujący regularne katalogi oraz pliki zip
również jest dostarczany.


%package devel
Summary:        Header files for zipios++
Summary(pl.UTF-8): Pliki nagłówkowe zipios++
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libstdc++-devel
Requires:       zlib-devel

%description devel
The header files are only needed for development of programs using the
zipios++.

%description devel -l pl.UTF-8
W pakiecie tym znajdują się pliki nagłówkowe, przeznaczone dla
programistów używających bibliotek zipios++.


%prep
%autosetup -p1 -n %{name}-%{version}%{cvs_ver}

chmod 0644 COPYING


%build
autoreconf -if
%configure
%make_build
make V=1 doc


%install
%make_install

# Remove static libs
rm -f %{buildroot}%{_libdir}/*.{a,la}


%{ldconfig_scriptlets}


%files
%doc AUTHORS NEWS README
%license COPYING
%{_libdir}/*.so.*

%files devel
%doc doc/html
%{_libdir}/*.so
%{_includedir}/zipios++


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5.9-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1.5.9-34
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5.9-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5.9-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5.9-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5.9-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5.9-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5.9-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5.9-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5.9-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5.9-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5.9-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5.9-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5.9-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5.9-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 13 2018 Richard Shaw <hobbes1069@gmail.com> - 0.1.5.9-20
- Add patch for zero size vector.
- Bring spec file up to current standards.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May  1 2015 Richard Shaw <hobbes1069@gmail.com> - 0.1.5.9-13
- Rebuild for C++ abi breakage.
- Only build documentation for non-rawhide builds due to bug in convert from
  the ImageMagick package (BZ#1217741).

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 27 2012 Richard Shaw <hobbes1069@gmail.com> - 0.1.5.9-7
- Add patch for bug in opening zip streams (BZ#834975).

* Tue Apr 10 2012 Richard Shaw <hobbes1069@gmail.com> - 0.1.5.9-5
- Cleanup spec file for submission to Fedora.
- Reference Debian source since upstream is dead.

* Thu Mar 29 2012  <jman@greaser.zultron.com> - 0.1.5.9-4
- Rebuild in koji

* Tue Mar 13 2012  <jman@greaser.zultron.com> - 0.1.5.9-3
- Add forgotten 'BuildRequires' entries

* Tue Jan 24 2012 John Morris <jman@caps.zultron.com> - 0.1.5.9-2
- Building for F16
- Adding "using std::ptrdiff_t" hack to get compilation to work; someone who knows C++ should examine this

* Sat Jul 16 2011  <jman@caps.zultron.com> - 0.1.5.9-1
- update RPM to version used in Ubuntu (known to work with FreeCAD)
- configure script exists; remove autoconf steps

* Thu Jul 14 2011  <jman@zultron.com> - 0.1.5-6
- patch "void zipios::ZipOutputStream::putNextEntry (const std::string & entryName)" back into headers:  putNextEntry-header.patch

* Tue Jul 12 2011  <jman@zultron.com> - 0.1.5-5
- C++ header dependency cleanups in patch4; see http://gcc.gnu.org/gcc-4.3/porting_to.html
- Changes for Fedora 13
