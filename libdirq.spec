%define github_owner cern-mig
%define github_name  c-dirq

Summary:	C implementation of the simple directory queue algorithm
Name:		libdirq
Version:	0.5
Release:	13%{?dist}
License:	ASL 2.0
URL:		https://github.com/%{github_owner}/%{github_name}/
Source0:	https://github.com/%{github_owner}/%{github_name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:	make, gcc

%description
The goal of this library is to offer a "simple" queue system using the
underlying filesystem for storage, security and to prevent race conditions
via atomic operations. It focuses on simplicity, robustness and scalability.

Multiple concurrent readers and writers can interact with the same queue. 

Other implementations of the same algorithm exist so readers and writers can
be written in different programming languages.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files, libraries and documentation
for developing programs using the %{name} library.

%package static
Summary:	Static libraries for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description static
The %{name}-static package contains static libraries for developing programs
using the %{name} library.

%prep
%setup -q -n %{github_name}-%{version}
CFLAGS="${RPM_OPT_FLAGS}" ./configure --includedir=%{_includedir} --libdir=%{_libdir} --mandir=%{_mandir}

%build
make %{?_smp_mflags}

%check
make test

%install
make install INSTALLROOT=%{buildroot}

%clean
make clean
rm -rf %{buildroot}

%ldconfig_scriptlets

%files
%{_libdir}/*.so.*

%files devel
%doc CHANGES DESIGN LICENSE README.md doc/dirq.html src/dqt.c
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/*/*

%files static
%{_libdir}/*.a

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Lionel Cons <lionel.cons@cern.ch> - 0.5-4
- Added explicit compilation requirements (#1604568).

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 04 2017 Lionel Cons <lionel.cons@cern.ch> - 0.5-1
- Upgraded to upstream version 0.5.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Lionel Cons <lionel.cons@cern.ch> - 0.4-2
- Added support for $RPM_OPT_FLAGS (#1393899).

* Mon Nov 14 2016 Lionel Cons <lionel.cons@cern.ch> - 0.4-1
- Initial Fedora/EPEL packaging.
