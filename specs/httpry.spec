%global     srcname     httpry

Summary:    A specialized packet sniffer designed for displaying and logging HTTP traffic
Name:       %{srcname}
Version:    0.1.8
Release:    25%{?dist}
License:    GPL-2.0-only and BSD-3-Clause
URL:        http://dumpsterventures.com/jason/%{srcname}/
Source:     http://dumpsterventures.com/jason/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires: libpcap-devel
BuildRequires: make

%description
httpry is a specialized packet sniffer designed for displaying and logging
HTTP traffic. It is not intended to perform analysis itself, but to capture,
parse, and log the traffic for later analysis. It can be run in real-time
displaying the traffic as it is parsed, or as a daemon process that logs to
an output file. It is written to be as lightweight and flexible as possible,
so that it can be easily adaptable to different applications.

%prep
%setup -q

%build
sed -i 's/^CCFLAGS.*$/CCFLAGS = \$(RPM_OPT_FLAGS) \$(RPM_LD_FLAGS) -I\/usr\/include\/pcap -I\/usr\/local\/include\/pcap/' Makefile
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
install -Dp -m 0755 %{srcname} ${RPM_BUILD_ROOT}%{_sbindir}/%{srcname}
install -Dp -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc doc/ChangeLog doc/COPYING doc/format-string doc/method-string doc/perl-tools doc/README
%{_sbindir}/%{srcname}
%{_mandir}/man1/%{srcname}.1*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 08 2023 Major Hayden <major@redhat.com> - 0.1.8-20
- Migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

%autochangelog
