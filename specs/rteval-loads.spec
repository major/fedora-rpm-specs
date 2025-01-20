Name:		rteval-loads
Version:	1.6
Release:	9%{?dist}
Summary:	Source files for rteval loads
Group:		Development/Tools
License:	GPL-2.0-only
URL:		https://git.kernel.org/pub/scm/utils/rteval/rteval.git
Source0:	https://www.kernel.org/pub/linux/kernel/v6.x/linux-6.6.1.tar.xz

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

%description
This package provides source code for system loads used by the rteval package

%prep

%build

%install
mkdir -p %{buildroot}%{_datadir}/rteval/loadsource
install -m 644 %{SOURCE0} %{buildroot}%{_datadir}/rteval/loadsource

%files
%defattr(-,root,root,-)
%dir %{_datadir}/rteval/loadsource
%{_datadir}/rteval/loadsource/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 01 2023 John Kacur <jkacur@redhat.com> - 1.6-5
- Upgrade the kernel to linux-6.6.1

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Feb 17 2023 John Kacur <jkacur@redhat.com> - 1.6-3
- Upgrade the kernel to linux-6.1.8

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 18 2022 John Kacur <jkacur@redhat.com> - 1.6-1
-Upgrade the kernel to linux-5.18.1.tar.xz
- Update the version number to sync more closely with rhel and CENTOS

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 John Kacur <jkacur@redhat.com> - 1.4-12
- Since this package only delivers kernel, moving the spec requires
  for building it to the rteval packages

* Sun Jan 10 2021 John Kacur <jkacur@redhat.com> - 1.4-11
- Remove stress-ng since it is already packaged with Fedora

* Thu Jul 23 2020 John Kacur <jkacur@redhat.com> - 1.4-10
- Rebuild bumping up both packages release number to avoid
- brew clashes
Resolves: rhbz#1859763

* Thu Jul 23 2020 John Kacur <jkacur@redhat.com> - 1.4-9
- Rebuild excluding aarch64 since stress-ng already exists there
Resolves: rhbz#1859763

* Thu Jul 23 2020 John Kacur <jkacur@redhat.com> - 1.4-8
- Upgrade to kernel linux-5.7
- Removing old "Obsoletes" from spec file
Resolves: rhbz#1859763

* Fri May 22 2020 John Kacur <jkacur@redhat.com> - 1.4-7
- Add stress-ng as a subpackage
Resolves: rhbz#1816357

* Thu Nov 21 2019 John Kacur <jkacur@redhat.com> - 1.4-6
- Update the gating test run_tests.sh for the kernel linux-5.1
Resolves: rhbz#1775202

* Fri Nov 08 2019 John Kacur <jkacur@redhat.com> - 1.4-5
- Upgrade to using kernel linux-5.1
Resolves: rhbz#1724827

* Mon Apr 01 2019 Clark Williams <williams@redhat.com> - 1.4-4
- OSCI gating framework
Resolves: rhbz#1682425

* Tue Jun 12 2018 John Kacur <jkacur@redhat.com> - 1.4-3
- Trigger a rebuild for rhel-8.0

* Thu Oct 19 2017 John Kacur <jkacur@redhat.com> - 1.4-2
- updated the url of the linux kernel in this spec file
Resolves: rhbz1504141

* Tue Jan 10 2017 Clark Williams <williams@redhat.com> - 1.4-1
- updated kernel tarball to 4.9 [1432625]

* Fri Jun  5 2015 Clark Williams <williams@redhat.com> - 1.3-3
- add requires for kernel-header package [1228740]

* Mon Nov 10 2014 Luis Claudio R. Goncalves <lgoncalv@redhat.com> - 1.3-2
-  rebuild for RHEL-7.1 (1151569)

* Fri May 20 2011 Clark Williams <williams@redhat.com> - 1.3-1
- updated kernel tarball to 2.6.39

* Mon Feb  7 2011 Clark Williams <williams@redhat.com> - 1.2-3
- initial build for MRG 2.0 (RHEL6)

* Thu Jul 15 2010 Clark Williams <williams@redhat.com> - 1.2-2
- removed rteval require from specfile (caused circular dependency)

* Thu Jul  8 2010 Clark Williams <williams@redhat.com> - 1.2-1
- removed hackbench tarball (now using rt-tests hackbench)

* Fri Feb 19 2010 Clark Williams <williams@redhat.com> - 1.1-1
- updated hackbench source with fixes from David Sommerseth
  <davids@redhat.com> to cleanup child processes

* Thu Nov  5 2009 Clark Williams <williams@redhat.com> - 1.0-1
- initial packaging effort
