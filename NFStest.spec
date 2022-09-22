Name: NFStest		
Version: 2.1.5
Release: 14%{?dist}
Summary: NFS Testing Tool

License: GPLv2+ 
URL: http://wiki.linux-nfs.org/wiki/index.php/NFStest
Source0: http://www.linux-nfs.org/~mora/nfstest/releases/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python2-devel
Requires: nfs-utils sudo tcpdump 
Requires: coreutils iproute iptables 
Requires: openssh-clients psmisc util-linux

%description
Provides a set of tools for testing either the NFS client or the NFS server, 
most of the functionality is focused mainly on testing the client. 
%prep
%setup -q

%build
%py2_build

%install
%py2_install

%files
%{_bindir}/nfstest_alloc
%{_bindir}/nfstest_cache
%{_bindir}/nfstest_delegation
%{_bindir}/nfstest_dio
%{_bindir}/nfstest_file
%{_bindir}/nfstest_interop
%{_bindir}/nfstest_io
%{_bindir}/nfstest_lock
%{_bindir}/nfstest_pkt
%{_bindir}/nfstest_pnfs
%{_bindir}/nfstest_posix
%{_bindir}/nfstest_sparse
%{_bindir}/nfstest_xid
%{_bindir}/nfstest_ssc
%{_mandir}/*/*
#For noarch packages: sitelib
%{python2_sitelib}/*

%doc COPYING README

%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Miro Hrončok <mhroncok@redhat.com> - 2.1.5-11
- Remove unused BuildRequires on python2-setuptools

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 11 2017 Iryna Shcherbina <ishcherb@redhat.com> - 2.1.5-3
- Fix ambiguous Python 2 dependency declarations
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr 21 2017 Steve Dickson <steved@redhat.com> 2.1.5-1
- Added needed Requires (bz 1444184)

* Thu Feb 16 2017 Steve Dickson <steved@redhat.com> 2.1.5-0
- Update to latest upstream version: 2.1.5 (bz 1422947)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 23 2015 Steve Dickson <steved@redhat.com> 2.1.1
- Update to latest upstream version: 2.1.1 (bz 1244918)

* Thu Jul 23 2015 Steve Dickson <steved@redhat.com> 1.0.11-0
- Updated to latest upstream release: 1.0.11 (bz 1244918)

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar  2 2015 Steve Dickson <steved@redhat.com> 1.0.9-0
- Updated to latest upstream release: 1.0.9

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 29 2014 Steve Dickson <steved@redhat.com> 1.0.8-0
- Updated to latest upstream release: 1.0.8

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 24 2013 Steve Dickson <steved@redhat.com> 1.0.2-0
- Updated to latest upstream release: 1.0.2

* Mon Mar 18 2013 Steve Dickson <steved@redhat.com> 1.0.1-1
- Added required BuildRequires

* Thu Feb 21 2013 Steve Dickson <steved@redhat.com> 1.0.1-0 
- Inital commit.


