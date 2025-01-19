%{?mingw_package_header}

%global mingw_pkg_name antlr

Summary:		MinGW Windows ANTLR C++ run-time library
Name:			mingw-%{mingw_pkg_name}
Version:		2.7.7
Release:		36%{?dist}
License:		ANTLR-PD
URL:			http://www.antlr.org/
Source0:		http://www.antlr2.org/download/%{mingw_pkg_name}-%{version}.tar.gz
Patch1:			%{mingw_pkg_name}-%{version}-newgcc.patch
Patch2:			mingw-%{mingw_pkg_name}.patch

BuildArch:		noarch

BuildRequires: make
BuildRequires:		mingw32-filesystem >= 52
BuildRequires:		mingw64-filesystem >= 52
BuildRequires:		mingw32-gcc
BuildRequires:		mingw64-gcc
BuildRequires:		mingw32-gcc-c++
BuildRequires:		mingw64-gcc-c++
BuildRequires:		mingw32-binutils
BuildRequires:		mingw64-binutils
BuildRequires:		libtool
BuildRequires:		autoconf
BuildRequires:		automake

Requires:		pkgconfig


%description
ANTLR is a parser generator. This package contains the MinGW Windows
run-time library for ANTLR C++ parsers.

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:		%{summary}

%description -n mingw32-%{mingw_pkg_name}
ANTLR is a parser generator. This package contains the MinGW Windows
run-time library for ANTLR C++ parsers.

%package -n mingw32-%{mingw_pkg_name}-static
Summary:		Static Version of the MinGW Windows ANTLR C++ run-time library
Requires:		mingw32-%{mingw_pkg_name} = %{version}-%{release}

%description -n mingw32-%{mingw_pkg_name}-static
Static version of the MinGW Windows ANTLR run-time library.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:		%{summary}

%description -n mingw64-%{mingw_pkg_name}
ANTLR is a parser generator. This package contains the MinGW Windows
run-time library for ANTLR C++ parsers.

%package -n mingw64-%{mingw_pkg_name}-static
Summary:		Static Version of the MinGW Windows ANTLR C++ run-time library
Requires:		mingw32-%{mingw_pkg_name} = %{version}-%{release}

%description -n mingw64-%{mingw_pkg_name}-static
Static version of the MinGW Windows ANTLR run-time library.

%{?mingw_debug_package}

%prep
%setup -q -n %{mingw_pkg_name}-%{version}
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;
%patch -P1
%patch -P2 -p1 -b .mingw
# CRLF->LF
sed -i 's/\r//' LICENSE.txt

%build
%{mingw_configure} --without-examples
pushd lib/cpp
touch NEWS
rm -f {,antlr,src}/Makefile{.in,}
libtoolize -f -c
aclocal -I m4
autoconf
autoheader
automake -a -c
%{mingw_configure} --enable-static
%{mingw_make} %{?_smp_mflags}
popd

%install
pushd lib/cpp
%{mingw_make} install DESTDIR=$RPM_BUILD_ROOT
popd

rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/libantlr2.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/libantlr2.la

mkdir $RPM_BUILD_ROOT%{_bindir}
install -p -m 755 build_win32/scripts/antlr-config $RPM_BUILD_ROOT%{mingw32_bindir}/antlr-config
install -p -m 755 build_win64/scripts/antlr-config $RPM_BUILD_ROOT%{mingw64_bindir}/antlr-config
ln -s %{mingw32_bindir}/antlr-config $RPM_BUILD_ROOT%{_bindir}/%{mingw32_target}-antlr-config
ln -s %{mingw64_bindir}/antlr-config $RPM_BUILD_ROOT%{_bindir}/%{mingw64_target}-antlr-config

%files -n mingw32-%{mingw_pkg_name}
%doc LICENSE.txt
%{mingw32_includedir}/%{mingw_pkg_name}
%{mingw32_bindir}/antlr-config
%{mingw32_bindir}/libantlr2-0.dll
%{mingw32_libdir}/libantlr2.dll.a
%{mingw32_libdir}/pkgconfig/antlr2.pc
%{_bindir}/%{mingw32_target}-antlr-config

%files -n mingw32-%{mingw_pkg_name}-static
%{mingw32_libdir}/libantlr2.a

%files -n mingw64-%{mingw_pkg_name}
%doc LICENSE.txt
%{mingw64_includedir}/%{mingw_pkg_name}
%{mingw64_bindir}/antlr-config
%{mingw64_bindir}/libantlr2-0.dll
%{mingw64_libdir}/libantlr2.dll.a
%{mingw64_libdir}/pkgconfig/antlr2.pc
%{_bindir}/%{mingw64_target}-antlr-config

%files -n mingw64-%{mingw_pkg_name}-static
%{mingw64_libdir}/libantlr2.a


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.7-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.7-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.7-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.7-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.7-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.7-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.7-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 2.7.7-29
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.7-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.7-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.7-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 04 2020 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.7.7-25
- rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.7-25
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.7-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 2.7.7-22
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jan 27 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.7.7-11
- Rebuild against mingw-gcc 4.8 (win64 uses SEH exceptions now)

* Fri Aug  3 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.7.7-10
- enable 64bit build

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.7.7-8
- Rebuild against the mingw-w64 toolchain

* Tue Jan 31 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.7.7-7
- Moved the antlr-config script from %%{_exec_prefix}/%%{_mingw32_target}/bin
  to %%{_mingw32_bindir}
- Dropped the dependency extraction magic as it's done automatically by RPM 4.9
- Dropped the %%clean section and %%defattr tags

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon May 23 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.7.7-5
- transition to new package naming scheme

* Sun May  1 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.7.7-4
- remove unnecessary cruft reported by Kalev Lember

* Mon Feb 21 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.7.7-3
- build dynamic as well as static library

* Mon Feb 21 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.7.7-2
- fix antlr-config --cxxflags
- workaround for the libtool "cannot link static library to DLL" problem

* Sat Feb 19 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.7.7-1
- Initial Package (based on the native package)
