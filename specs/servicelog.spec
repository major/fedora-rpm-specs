Name:           servicelog
Version:        1.1.16
Release:        8%{?dist}
Summary:        Servicelog Tools

License:        GPL-2.0-only
URL:            https://github.com/power-ras/servicelog
Source0:        https://github.com/power-ras/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  libservicelog-devel >= 1.1.9-2
BuildRequires:  autoconf libtool librtas-devel help2man

# because of librtas-devel in libservicelog
ExclusiveArch: ppc %{power64}

%description
Command-line interfaces for viewing and manipulating the contents of
the servicelog database. Contains entries that are useful
for performing system service operations, and for providing a history
of service operations that have been performed on the system.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
help2man -s 8 -N $RPM_BUILD_ROOT/%{_sbindir}/slog_common_event > $RPM_BUILD_ROOT/%{_mandir}/man8/slog_common_event.8

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%{_bindir}/servicelog
%{_bindir}/v1_servicelog
%{_bindir}/v29_servicelog
%{_bindir}/servicelog_notify
%{_bindir}/log_repair_action
%{_sbindir}/slog_common_event
%{_bindir}/servicelog_manage
%{_mandir}/man[18]/*.[18]*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Feb 16 2023 Than Ngo <than@redhat.com> - 1.1.16-4
- migrated to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 09 2022 Than Ngo <than@redhat.com> - 1.1.16-1
- Rebase to 1.1.16

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 28 2020 Stephen Gallagher <sgallagh@redhat.com> - 1.1.15-5
- Fix build failure on PowerNV builders

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 02 2019 Than Ngo <than@redhat.com> - 1.1.15-1
- rebase to 1.1.15
- update url

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jul 11 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.14-2
- Spec file cleanups
- Use %%license

* Mon Mar 21 2016 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 1.1.14-1
- Update to latest upstream 1.1.14

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Sep 22 2014 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 1.1.13
- Update to latest upstream 1.1.13

* Fri Aug 01 2014 Brent Baude <bbaude@redhat.com> - 1.1.12-5
- NVR bump for Fedora 21 build on merged koji

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jun 03 2014 Jakub Čajka <jcajka@redhat.com> - 1.1.12-3
- Spec file clean up

* Mon Apr 14 2014 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 1.1.12-2
- Grant permission to link with librtas library

* Fri Mar 07 2014 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 1.1.12
- Update to latest upstream 1.1.12

* Thu Oct 10 2013 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 1.1.11-3
- Add ppc64le architecture

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 21 2013 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 1.1.11
- Update to latest upstream 1.1.11

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 08 2012 Karsten Hopp <karsten@redhat.com> 1.1.10-1
- update to servicelog-1.1.10

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 09 2011 Jiri Skala <jskala@redhat.com> - 1.1.9-1
- update to latest upstream 1.1.9

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jun 16 2010 Roman Rakus <rrakus@redhat.com> - 1.1.7-2
- Generate missing man page from help (help2man)

* Tue May 18 2010 Roman Rakus <rrakus@redhat.com> - 1.1.7-1
- Initial packaging

