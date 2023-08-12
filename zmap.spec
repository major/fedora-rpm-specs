%global __cmake_in_source_build 1
%bcond_with     pfring
%bcond_without  debug

Name:           zmap
Version:        3.0.0
Release:        %autorelease
Summary:        Network scanner for Internet-wide network studies
License:        ASL 2.0
URL:            https://zmap.io
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  byacc
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  gengetopt
BuildRequires:  gmp-devel
BuildRequires:  libunistring-devel
BuildRequires:  json-c-devel
BuildRequires:  libpcap-devel

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
%autosetup

%build
%cmake -DWITH_JSON=ON     \
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
%{_sbindir}/zmap
%{_sbindir}/zblocklist
%{_sbindir}/ziterate
%{_sbindir}/ztee
%{_mandir}/man1/zmap.1*
%{_mandir}/man1/zblocklist.1*
%{_mandir}/man1/ziterate.1*
%{_mandir}/man1/ztee.1*

%changelog
%autochangelog
