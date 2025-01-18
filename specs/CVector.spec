#global release_date 5Aug09
%{!?release_func:%global release_func() %1%%{?release_date:.%%release_date}%%{?dist}}
%define version_number 1.0.3

Name:           CVector
Version:        %{version_number}.1
Release:        %release_func 33
Summary:        ANSI C API for Dynamic Arrays

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://cvector.sourceforge.net/
%if 0%{?release_date:1}
Source0:        http://downloads.sourceforge.net/project/cvector/cvector/CVector-%{version}/CVector-%{version}-%{release_date}.tar.gz
%else
Source0:        http://downloads.sourceforge.net/project/cvector/cvector/CVector-1.0.3/CVector-%{version}.tar.gz
%endif
# to fix /-dynamic/-rdynamic/ issue, reported to upstream
Patch0:         CVector-1.0.3.1-dynamic.patch
# to fix libdir for lib64 architecture
Patch1:         CVector-1.0.3-lib64.patch

BuildRequires:  libtool
BuildRequires: make

%description
CVector is an ANSI C implementation of dynamic arrays to provide a
crude approximation to the C++ vector class.

%package devel
Summary:        Development tools for compiling programs using CVector
Requires:       %{name} = %{version}-%{release}

%description devel
The CVector-devel package includes the header and library files for
developing applications that use CVector.

%prep
%setup -q
%patch -P0 -p1 -b .dynamic
%if "%{_lib}" == "lib64"
%patch -P1 -p1 -b .lib64
%endif

%build
make CFLAGS="%{optflags}" %{?_smp_mflags}

%install
rm -rf %{buildroot}

make install CFLAGS="%{optflags}" INSTALL_PREFIX="%{buildroot}%{_prefix}"

# remove .la and .a files
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'

%check
make tests

%ldconfig_scriptlets

%files
%doc README_CVector.html README_CVector.txt lgpl.txt
%{_libdir}/libCVector-%{version_number}.so.*

%files devel
%{_includedir}/CVector.h
%{_libdir}/libCVector.so

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.3.1-32
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 02 2020 Björn Esser <besser82@fedoraproject.org> - 1.0.3.1-20
- Fix string quoting for rpm >= 4.16

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Apr  9 2011 Takanori MATSUURA <t.matsuu@gmail.com> - 1.0.3.1-3
- use %%{_lib} detection to fix

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 26 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 1.0.3.1-1
- update to 1.0.3.1
- use "make all" instead of "make"
- add %%check

* Tue Sep  1 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 1.0.3-1.5Aug09
- initial release

* Tue Sep  1 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 1.0.3-0.7.5Aug09
- use "-rdynamic" instead of "-shared"

* Tue Sep  1 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 1.0.3-0.6.5Aug09
- initial import for Fedora (#545046)

* Mon Aug 30 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 1.0.3-0.5.5Aug09
- change release versioning scheme
- provide 64 bit libdir fix as a patch
- remove useless s/dynamic/rsynamic/g

* Wed Dec  9 2009 Takanori MATSUURA <t.matsuu@gmail.com> - 1.0.3-4.20090805
- remove static library

* Wed Dec  9 2009 Takanori MATSUURA <t.matsuu@gmail.com> - 1.0.3-3.20090805
- apply changes mentioned in rhbz #545046 comment #4

* Tue Dec  8 2009 Takanori MATSUURA <t.matsuu@gmail.com> - 1.0.3-2.20090805
- fit to Fedora Packaging Guidelines

* Tue Aug 25 2009 Takanori MATSUURA <t.matsuu@gmail.com> - 1.0.3-1.20090805
- update to 1.0.3-5Aug09

* Wed Jul 29 2009 Takanori MATSUURA <t.matsuu@gmail.com> - 1.0.3-1
- initial build
