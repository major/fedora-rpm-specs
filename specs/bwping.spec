%global forgeurl https://github.com/oleg-derevenetz/bwping
%global tag      RELEASE_2.5

Name:           bwping
Version:        2.5
Release:        7%{?dist}

Summary:        Measure bandwidth and response times using ICMP
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://bwping.sourceforge.net/

%forgemeta
Source0:        %{forgesource}

# bwping needs to be run with sudo, then these tests will fail
Patch0:         0001-remove-failing-tests.patch

BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  autoconf

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%description
BWPing is a tool to measure bandwidth and response
times between two hosts using Internet Control Message
Protocol (ICMP) echo request/echo reply mechanism.
It does not require any special software on the remote host.
The only requirement is the ability to respond on ICMP echo
request messages.

%prep
%forgeautosetup

%build
autoreconf -i
%configure
%make_build

%install
%make_install

%check
make check

%files
%doc AUTHORS README
%license COPYING 
%{_sbindir}/bwping*
%{_mandir}/man8/bwping*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 2.5-6
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Aug 12 2022 Alessio <alciregi@fedoraproject.org> 2.5-1
- Initial build
