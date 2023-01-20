%global forgeurl https://github.com/oleg-derevenetz/bwping
%global tag      RELEASE_2.5

Name:           bwping
Version:        2.5
Release:        2%{?dist}

Summary:        Measure bandwidth and response times using ICMP
License:        BSD
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
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Aug 12 2022 Alessio <alciregi@fedoraproject.org> 2.5-1
- Initial build
