Name:		qclib
Version:	2.5.0
Release:	3%{?dist}
Summary:	Library for extraction of system information for Linux on z Systems
License:	BSD-3-Clause
URL:		https://github.com/ibm-s390-linux/qclib
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz
ExclusiveArch:	s390 s390x
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	glibc-static
BuildRequires:	doxygen
BuildRequires:	which
# for EBCDIC to ASCII conversion
Requires:	glibc-gconv-extra

%description
%{summary}.

%package devel
Summary:	Development library and headers for qclib
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
qclib provides a C API for extraction of system information for Linux on z
Systems.
For instance, it will provide the number of CPUs
 * on the machine (CEC, Central Electronic Complex) layer
 * on the PR/SM (Processor Resource/Systems Manager) layer, i.e. visible to
   LPARs, including LPAR groups in z/VM hosts, guests and CPU pools
 * in KVM hosts and guests

This allows calculating the upper limit of CPU resources a highest level guest
can use. For example: If an LPAR on a z13 provides 4 CPUs to a z/VM hyper-visor,
and the hyper-visor provides 8 virtual CPUs to a guest, qclib can be used to
retrieve all of these numbers, and it can be concluded that not more capacity
than 4 CPUs can be used by the software running in the guest.

This package provides the development libraries and headers for qclib.

%package static
Summary:	Static library for qclib
Requires:	%{name}-devel = %{version}-%{release}
Provides:	%{name}-static = %{version}-%{release}

%description static
%{summary}. This package provides static libraries for qclib.


%prep
%autosetup


%build
make V=1 CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}" %{?_smp_mflags} all doc


%install
%make_install V=1 DOCDIR=%{_docdir}
make DESTDIR=%{buildroot} DOCDIR=%{_docdir} installdoc


%check
make test-sh test


%files
%dir %{_docdir}/%{name}
%license %{_docdir}/%{name}/LICENSE
%doc %{_docdir}/%{name}/README.md
%{_bindir}/zhypinfo
%{_bindir}/zname
%{_libdir}/libqc.so.*
%{_mandir}/man8/zhypinfo.8*
%{_mandir}/man8/zname.8*

%files devel
%doc %{_docdir}/%{name}/html/
%{_libdir}/libqc*.so
%{_includedir}/query_capacity.h

%files static
%{_libdir}/libqc*.a


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon May 13 2024 Dan Horák <dan[at]danny.cz> - 2.5.0-1
- updated to 2.5.0

* Tue Feb 13 2024 Dan Horák <dan[at]danny.cz> - 2.4.1-1
- updated to 2.4.1

* Tue Feb 06 2024 Dan Horák <dan[at]danny.cz> - 2.4.0-6
- add missing Requires

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Oct 30 2023 Dan Horák <dan[at]danny.cz> - 2.4.0-3
- work around a test failure (https://github.com/ibm-s390-linux/qclib/issues/2)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 13 2023 Dan Horák <dan[at]danny.cz> - 2.4.0-1
- updated to 2.4.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 20 2022 Dan Horák <dan[at]danny.cz> - 2.3.2-1
- updated to 2.3.2

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Apr 27 2022 Dan Horák <dan[at]danny.cz> - 2.3.1-1
- updated to 2.3.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 03 2021 Dan Horák <dan[at]danny.cz> - 2.3.0-1
- updated to 2.3.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 16 2020 Dan Horák <dan[at]danny.cz> - 2.2.1-1
- updated to 2.2.1

* Thu Sep 24 2020 Dan Horák <dan[at]danny.cz> - 2.2.0-2
- fix linking

* Wed Sep 23 2020 Dan Horák <dan[at]danny.cz> - 2.2.0-1
- updated to 2.2.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 22 2020 Dan Horák <dan[at]danny.cz> - 2.1.0-1
- updated to 2.1.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Dan Horák <dan[at]danny.cz> - 2.0.1-1
- updated to 2.0.1

* Tue Nov 19 2019 Dan Horák <dan[at]danny.cz> - 2.0.0-1
- updated to 2.0.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Dan Horák <dan[at]danny.cz> - 1.4.1-1
- updated to 1.4.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 19 2018 Dan Horák <dan[at]danny.cz> - 1.4.0-1
- updated to 1.4.0

* Mon Mar 12 2018 Dan Horák <dan[at]danny.cz> - 1.3.1-3
- fix LDFLAGS injection (#1552658)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Dan Horák <dan[at]danny.cz> - 1.3.1-1
- updated to 1.3.1

* Mon Dec 04 2017 Dan Horák <dan[at]danny.cz> - 1.3.0-1
- updated to 1.3.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 31 2016 Rafael dos Santos <rdossant@redhat.com> 1.2.0-1
- Initial packaging
