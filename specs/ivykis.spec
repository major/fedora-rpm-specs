%if 0%{?rhel} > 6 || 0%{?fedora} > 16
%global librarydir %{_libdir}
%else
%global librarydir /%{_lib}
%endif

Summary:        Library for asynchronous I/O readiness notification
Name:           ivykis
Version:        0.43.2
Release:        3%{?dist}

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://libivykis.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/libivykis/%{version}/%{name}-%{version}.tar.gz


BuildRequires:  gcc
BuildRequires: make
%description
ivykis is a library for asynchronous I/O readiness notification.
It is a thin, portable wrapper around OS-provided mechanisms such
as epoll_create(2), kqueue(2), poll(2), poll(7d) (/dev/poll) and
port_create(3C).

ivykis was mainly designed for building high-performance network
applications, but can be used in any event-driven application that
uses poll(2)able file descriptors as its event sources.

%package devel
Summary:        Development files for the ivykis package
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description devel
ivykis is a library for asynchronous I/O readiness notification.
This package contains files needed to develop applications using
ivykis.


%prep
%setup -q

%build
%configure --libdir=%{librarydir}
%{__make} %{_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

rm -f %{buildroot}%{librarydir}/libivykis.{a,la}

%if "%{librarydir}" != "%{_libdir}"
  mkdir -p %{buildroot}%{_libdir}
  mv %{buildroot}%{librarydir}/pkgconfig %{buildroot}%{_libdir}/
%endif

%check
make check


%ldconfig_scriptlets


%files
%doc AUTHORS COPYING
%{librarydir}/libivykis.so.*

%files devel
%{librarydir}/libivykis.so
%{_includedir}/iv*
%{_libdir}/pkgconfig/*
%{_mandir}/man3/*.3*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.43.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.43.2-2
- convert license to SPDX

* Thu Jul 25 2024 Peter Czanik <peter@czanik.hu> - 0.43.2-1
- update to 0.43.2
- re-enable "make check"

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 30 2024 Peter Czanik <peter@czanik.hu> - 0.43-1
- update to 0.43
- disable "make check" temporarily

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.42.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.42.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.42.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.42.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.42.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.42.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.42.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.42.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.42.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.42.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.42.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 19 2019 My Karlsson <mk@acc.umu.se> - 0.42.4-1
- Update to 0.42.4

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.42.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 19 2018 My Karlsson <mk@acc.umu.se> - 0.42.3-3
- Rebuilt

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.42.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 05 2018 My Karlsson <mk@acc.umu.se> - 0.42.3-1
- Update to 0.42.3

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.42.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Nov 12 2017 My Karlsson <mk@acc.umu.se> - 0.42.2-1
- Update to 0.42.2

* Sat Aug 19 2017 My Karlsson <mk@acc.umu.se> - 0.42.1-1
- Update to 0.42.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat May 6 2017 My Karlsson <mk@acc.umu.se> - 0.42-1
- Update to 0.42.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 0.41-1
- Update to 0.41.

* Fri Nov 11 2016 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 0.40-3
- Patch file: ivykis-0.40-aarch64-and-ppc64.patch

* Wed Nov  2 2016 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 0.40-2
- Run the test suite

* Wed Nov  2 2016 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 0.40-1
- Update to 0.40.

* Sun Oct 30 2016 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 0.36.3-1
- Update to 0.36.3.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.36.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 17 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.36.2-1
- Update to 0.36.2.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 17 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.36.1-1
- Update to 0.36.1.

* Mon Dec 10 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.30.5-1
- Update to 0.30.5.

* Sun Oct  7 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.30.4-2
- Handle review issues (863719#c1)

* Sat Oct  6 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.30.4-1
- Initial specfile for Fedora and EPEL.

# vim:set ai ts=4 sw=4 sts=4 et:
