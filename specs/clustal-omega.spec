Name:		clustal-omega
Version:	1.2.4
Release:	22%{?dist}
Summary:	Clustal Omega is a command-line multiple sequence alignment tool

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://www.clustal.org/omega/clustal-omega-1.2.0.tar.gz
Source0:	http://www.clustal.org/omega/%{name}-%{version}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	argtable-devel
BuildRequires: make

# bundled library exception provided by FPC
# https://fedorahosted.org/fpc/ticket/399
Provides:	bundled(squid) = 1.9

%description
Clustal Omega is a command-line multiple sequence alignment tool.
The tool is widely used in molecular biology for multiple alignment of
both nucleic acid and protein sequences. Clustal Omega is the latest version
in the clustal tools for the sequence alignment.

%package devel
Summary:	Development files for Clustal Omega
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development package for Clustal Omega

%prep
%setup -q
sed -i 's/\r$//' README
sed -i 's/mktemp/mkstemp/g' src/clustal-omega.c
# disable -O3 compiler flags
sed -i 's/\${AM_CFLAGS} -O3/${AM_CFLAGS}/g' configure
sed -i 's/\${AM_CXXFLAGS} -O3/${AM_CXXFLAGS}/g' configure

# fix for GCC-6 FTBFS
sed -i '/inline float log/d' src/hhalign/util-C.h

%build
export CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" LDFLAGS="%{optflags}"
%configure --disable-static
make V=1 %{?_smp_mflags}

%install
%make_install
# removing libtool generated static libs
rm -f %{buildroot}%{_libdir}/libclustalo.la %{buildroot}%{_libdir}/libclustalo.a

%files
%doc COPYING README
%{_bindir}/clustalo

%files devel
%{_libdir}/pkgconfig/clustalo.pc
%{_includedir}/clustalo/

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.4-21
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 16 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2.4-7
- Add gcc-c++ as BR

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 28 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2.4-1
- Update to 1.2.4

* Thu Nov 17 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2.3-1
- Update to 1.2.3

* Tue Feb 16 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2.1-9
- Added fix for GCC-6 FTBFS - Thanks Yaakov Selkowitz

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.2.1-6
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jul 12 2014 Mukundan Ragavan <nonamedotc@gmail.com> - 1.2.1-4
- Initial build for F22

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 17 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2.1-2
- Fixed errors pointed out in package review
- removed dir ownership of /usr/lib64/pkgconfig
- used correct compiler flags

* Thu Mar 6 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2.1-1
- Updated to latest upstream version
- Fixed spec file errors

* Fri Jan 24 2014 nonamedotc <nonamedotc@fedoraproject.org> - 1.2.0-1
- Changed package description, fixed links to sources

* Thu Jan 16 2014 nonamedotc <nonamedotc@fedoraproject.org> - 1.2.0-1
- First build of clustal omega
