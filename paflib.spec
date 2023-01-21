Name:    paflib
Version: 0.3.0
Release: 15%{?dist}
Summary: Library for accessing Power Architecture Facilities
License: MIT
URL:     https://github.com/paflib/paflib
Source0: https://github.com/paflib/paflib/archive/%{version}.tar.gz

ExclusiveArch: ppc %{power64}
BuildRequires: make
BuildRequires: libtool

%package devel
Summary: Header files for paflib
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Contains header files for building with paflib.

%description
PAFLib is a IBM written library which exposes Power Architecture Facilities to
user space via an API. This includes the Data Stream Control Register Facility
(DSCR) and the Event-Based Branching facility (EBB). Linux kernel 3.9 has
exposed problem-state DSCR usage for ISA 2.06 (POWER7 emulated) and ISA
2.07 (POWER8 in hardware). Linux 3.10 has exposed the EBB facility.

%prep
%setup -q -n %{name}-%{version}

%build
# enable ebb, as it is automaticly disabled if mcpu!=power8
%configure --disable-static --enable-ebb
make %{?_smp_mflags}

%check
# Hardening breaks tests compilation
export CFLAGS=`echo "%{optflags}" | sed 's/-specs=\/usr\/lib\/rpm\/redhat\/redhat-hardened-cc1//'`
export CXXFLAGS=`echo "%{optflags}" | sed 's/-specs=\/usr\/lib\/rpm\/redhat\/redhat-hardened-cc1//'`
export LDFLAGS=`echo "%{optflags}" | sed 's/-specs=\/usr\/lib\/rpm\/redhat\/redhat-hardened-cc1//'`

%configure --disable-static --enable-ebb
# do not fail on test failures as builder might not support all required features
make check || :

%install
make install DESTDIR=$RPM_BUILD_ROOT

# we are installing it using doc
rm -rf %{buildroot}/usr/share/doc/libpaf/ChangeLog.md
find %{buildroot} -type f -name "*.la" -delete

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc README.md ChangeLog.md
%{_libdir}/libpaf-ebb.so.*
%{_libdir}/libpaf-dsc.so.*

%files devel
%{_libdir}/libpaf-dsc.so
%{_libdir}/libpaf-ebb.so
%dir %{_includedir}/paf
%{_includedir}/paf/dsc.h
%{_includedir}/paf/ebb.h
%{_includedir}/paf/ppr.h
%{_includedir}/paf/tb.h
%{_mandir}/man3/libpaf-tb.3*
%{_mandir}/man3/libpaf-dsc.3*
%{_mandir}/man3/libpaf-ebb.3*
%{_mandir}/man3/libpaf-ppr.3*

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 02 2016 Jakub Čajka <jcajka@redhat.com> - 0.3.0-1
- rebase to 0.3.0

* Mon Jul 11 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.2.0-3
- spec cleanups
- Use %%license

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 06 2015 Jakub Čajka <jcajka@redhat.com> - 0.2.0-1
- Rebase to 0.2.0
- Enabled tests run
- Resolves: BZ#1251120

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Sep 25 2014 Rajalakshmi S <raji@linux.vnet.ibm.com> 0.1.4-1
- Update release

* Thu Sep 25 2014 Rajalakshmi S <raji@linux.vnet.ibm.com> 0.1.4-5
- Update next release

* Mon Sep 15 2014 Rajalakshmi S <raji@linux.vnet.ibm.com> 0.1.3-4
- Move manual pages to devel package and remove Group tag

* Wed Sep 10 2014 Rajalakshmi S <raji@linux.vnet.ibm.com> 0.1-3
- Various spec file fixes

* Tue Sep 09 2014 Rajalakshmi S <raji@linux.vnet.ibm.com> 0.1-2
- Remove passing libdir and prefix to configure in spec file
- Remove RPM_BUILD_ROOT cleanup in install in spec file

* Tue Sep 09 2014 Rajalakshmi S <raji@linux.vnet.ibm.com> 0.1-1
- Fix builddir in spec-file

* Mon Sep 01 2014 Rajalakshmi S <raji@linux.vnet.ibm.com> 0.1-1
- Initial RPM release
