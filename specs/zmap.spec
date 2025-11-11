%global __cmake_in_source_build 1
%bcond_with     pfring
%bcond_without  debug

Name:           zmap
Version:        4.3.4
Release:        %autorelease
Summary:        Network scanner for Internet-wide network studies
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://zmap.io
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         zmap-bin-sbin-merge.patch
BuildRequires:  byacc
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gengetopt
BuildRequires:  gmp-devel
BuildRequires:  json-c-devel
BuildRequires:  Judy-devel
BuildRequires:  libpcap-devel
BuildRequires:  libunistring-devel

%description
ZMap is an open-source network scanner that enables researchers to easily 
perform Internet-wide network studies. With a single machine and a well 
provisioned network uplink, ZMap is capable of performing a complete scan of 
the IPv4 address space in under 45 minutes, approaching the theoretical limit
of gigabit Ethernet.

ZMap can be used to study protocol adoption over time, monitor service 
availability, and help us better understand large systems distributed across 
the Internet.

========== WARNING ==========
While ZMap is a powerful tool for researchers, please keep in mind that by 
running ZMap, you are potentially scanning the ENTIRE IPv4 address space and 
some users may not appreciate your scanning. We encourage ZMap users to 
respect requests to stop scanning and to exclude these networks from ongoing 
scanning.

%prep
%autosetup -p 0

%build
%cmake -DENABLE_DEVELOPMENT=OFF           \
       -DENABLE_LOG_TRACE=OFF             \
       -DWITH_JSON=ON                     \
       -DWITH_PFRING=OFF

%cmake_build

chmod 644 -v examples/udp-probes/*
find ./examples/ -type f -exec sed -i 's/\r$//' {} \+

%install
%cmake_install

%files
%doc AUTHORS CHANGELOG.md README.md examples/
%license LICENSE
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_bindir}/zmap
%{_bindir}/zblocklist
%{_bindir}/ziterate
%{_bindir}/ztee
%{_mandir}/man1/zmap.1*
%{_mandir}/man1/zblocklist.1*
%{_mandir}/man1/ziterate.1*
%{_mandir}/man1/ztee.1*

%changelog
%autochangelog
