%global reponame crash-trace

Summary: Trace extension module for the crash utility
Name: crash-trace-command
Version: 3.0
Release: 5%{?dist}
License: GPLv2
Source: https://github.com/fujitsu/crash-trace/archive/v%{version}/%{name}-%{version}.tar.gz
URL: https://github.com/fujitsu/crash-trace
ExclusiveOS: Linux
ExclusiveArch: aarch64 ppc64le s390x x86_64
BuildRequires: crash-devel >= 7.2.0-2
BuildRequires: gcc
Requires: trace-cmd
Requires: crash >= 7.2.0-2

Patch0001: 0001-Makefile-set-DT_SONAME-to-trace.so.patch
Patch0002: 0002-Makefile-fix-build-failure-on-aarch64-and-ppc64le.patch

%description
Command for reading ftrace data from a dump file.

%prep
%autosetup -n %{reponame}-%{version}

%build
%make_build

%install
install -m 0755 -d %{buildroot}%{_libdir}/crash/extensions
install -m 0755 -t %{buildroot}%{_libdir}/crash/extensions %{_builddir}/%{reponame}-%{version}/trace.so

%files
%dir %{_libdir}/crash
%dir %{_libdir}/crash/extensions
%{_libdir}/crash/extensions/trace.so
%license COPYING

%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb 19 2021 HATAYAMA Daisuke <d.hatayama@fujitsu.com> - 3.0-2
- Makefile: set DT_SONAME to trace.so
- Makefile: fix build failure on aarch64 and ppc64le
* Fri Jan 22 2021 HATAYAMA Daisuke <d.hatayama@fujitsu.com> - 3.0-1
- Initial crash-trace-command package
