# This thing cannot build fast.
%global _smp_mflags -j1
%global optflags %{optflags} -Wno-error=unused-result -Wno-error=unused-but-set-variable -Wno-error=restrict -Wno-error=unused-variable -Wno-error=maybe-uninitialized -Wno-error=uninitialized

Name:		snobol4
Version:	2.3.1
Release:	6%{?dist}
# Majority: BSD-2-Clause
# BSD-3-Clause: modules/random/random.c
# BSD-4-Clause: lib/bsd/popen.c
# ISC: modules/base64/base64.c
License:	BSD-2-Clause AND BSD-3-Clause AND BSD-4-Clause AND ISC
URL:		https://www.regressive.org/snobol4/csnobol4/curr/
Source0:	https://ftp.regressive.org/snobol4/%{name}-%{version}.tar.gz
# Do not hardcode -O3.
Patch1:		snobol4-2.3.1-configure-no-opt.patch
Summary:	A port of Macro SNOBOL4
BuildRequires:	gcc, gcc-c++, m4, make
BuildRequires:	bzip2-devel
BuildRequires:	gdbm-devel
BuildRequires:	libedit-devel
BuildRequires:	openssl-devel
BuildRequires:	readline-devel
BuildRequires:	sqlite-devel
BuildRequires:	tcl-devel
BuildRequires:	xz-devel
BuildRequires:	zlib-devel

%description
This is a free port of the original SIL (SNOBOL4 Implementation
Language) "macro" version of SNOBOL4 (developed at Bell Labs) with the
`C' language as a target.

SNOBOL4, while known primarily as a string language excels at any task
involving symbolic manipulations.  It provides dynamic typing, garbage
collection, user data types, on the fly compilation.

%package devel
Summary:	Development files for snobol4
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for snobol4.

%prep
%setup -q
%patch -P1 -p1 -b .configure-no-opt

%build
# This isn't a real configure script, hence, no macro.
./configure --add-cflags="%{build_cflags}" --add-cppflags="%{build_cxxflags}" --prefix=%{_prefix} --mandir=%{_mandir} --snolibdir=%{_libdir}/snobol4 --with-tcl=%{_libdir}/tclConfig.sh
%make_build

%install
%make_install

# all in libdir? What is this, 1985? Oh wait, this is SNOBOL, so maybe 1969.
mkdir -p %{buildroot}%{_includedir}/snobol4
mv %{buildroot}%{_libdir}/%{name}/%{version}/include/* %{buildroot}%{_includedir}/snobol4
pushd %{buildroot}%{_libdir}/%{name}/%{version}/
rm -rf include
ln -s ../../../include/snobol4 include
popd

rm -rf %{buildroot}%{_libdir}/%{name}/%{version}/CHANGES %{buildroot}%{_libdir}/%{name}/%{version}/README

%files
%doc CHANGES README
%license COPYRIGHT
%{_bindir}/sdb*
%{_bindir}/snobol4*
%{_bindir}/snopea*
%{_libdir}/snobol4
%exclude %{_libdir}/snobol4/%{version}/include
%{_defaultdocdir}/%{name}-%{version}/
%{_mandir}/man1/sdb.1*
%{_mandir}/man1/snobol4*.1*
%{_mandir}/man1/snopea.1*
%{_mandir}/man3/snolib.3*
%{_mandir}/man3/snobol4*.3*
%{_mandir}/man7/snopea.7*

%files devel
%{_includedir}/%{name}
%{_libdir}/snobol4/%{version}/include

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Mar 30 2023 Tom Callaway <spot@fedoraproject.org> 2.3.1-2
- fix URL to be https
- use build_cflags and build_cxxflags
- correct License tag

* Sun Mar 26 2023 Tom Callaway <spot@fedoraproject.org> 2.3.1-1
- initial package
