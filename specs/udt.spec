Name:		udt
Version:	4.11
Release:	28%{?dist}
Summary:	UDP based Data Transfer Protocol

#		BSD except for src/md5.cpp and src/md5.h that are Zlib
License:	BSD-3-Clause AND Zlib
URL:		http://udt.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/udt/udt/%{version}/udt.sdk.%{version}.tar.gz

BuildRequires:	make
BuildRequires:	gcc-c++

%package devel
Summary:	UDP based Data Transfer Protocol - development files
Requires:	%{name} = %{version}-%{release}

%description
UDT is a reliable UDP based application level data transport protocol
for distributed data intensive applications over wide area high-speed
networks. UDT uses UDP to transfer bulk data with its own reliability
control and congestion control mechanisms. The new protocol can
transfer data at a much higher speed than TCP does. UDT is also a
highly configurable framework that can accommodate various congestion
control algorithms.

%description devel
UDT development files.

# Work around %%_builddir being defined too late (#2043864)
%global _package_note_file %{_builddir}/udt4/.package_note-%{name}-%{version}-%{release}.%{_arch}.ld

%prep
%setup -q -n udt4

sed 's!-O3!%{optflags}!' -i src/Makefile app/Makefile
sed 's!-shared!& %{?__global_ldflags} -lpthread -Wl,-soname,libudt.so.0!' \
    -i src/Makefile
sed 's!LDFLAGS =!& %{?__global_ldflags}!' -i app/Makefile
sed 's/\r//' -i doc/doc/udtdoc.css

%build
ARCH=
%ifarch %{ix86}
ARCH=IA32
%endif
%ifarch x86_64
ARCH=AMD64
%endif
%ifarch ia64
ARCH=IA64
%endif

# Parallel build fails - no _smp_mflags
make arch=$ARCH

%install
mkdir -p %{buildroot}%{_libdir}
install src/libudt.so %{buildroot}%{_libdir}/libudt.so.0
ln -s libudt.so.0 %{buildroot}%{_libdir}/libudt.so
mkdir -p %{buildroot}%{_includedir}/udt
install -p -m 644 src/*.h %{buildroot}%{_includedir}/udt

%ldconfig_scriptlets

%files
%{_libdir}/libudt.so.0
%doc RELEASE_NOTES.txt
%license LICENSE.txt

%files devel
%{_libdir}/libudt.so
%{_includedir}/udt
%doc doc

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.11-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 29 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 4.11-27
- Update License tag

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 4.11-26
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.11-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.11-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.11-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.11-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.11-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.11-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.11-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.11-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.11-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.11-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 16 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 4.11-13
- Add BuildRequires on gcc-c++
- Remove Group tags
- Don't clear the buildroot in the install section
- Switch to %%ldconfig_scriptlets

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.11-6
- Include more headers in devel package
- Adapt to new license packaging guidelines

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.11-5
- Rebuilt for GCC 5 C++11 ABI change

* Sat Mar 07 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.11-4
- Fix sed substitutions in case of slashes in rpm macros

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 14 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.11-2
- Add missing things for EPEL 5

* Mon Jun 09 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.11-1
- initial packaging for Fedora
