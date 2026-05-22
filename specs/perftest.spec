Name:           perftest
Summary:        IB Performance Tests
Version:        26.01.5
Release:        %autorelease
License:        GPL-2.0-only OR BSD-2-Clause
Source:		https://github.com/linux-rdma/perftest/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
Url:            https://github.com/linux-rdma/perftest

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libibverbs-devel >= 1.2.0
BuildRequires:  librdmacm-devel >= 1.0.21
BuildRequires:  libibumad-devel >= 1.3.10.2
BuildRequires:  pciutils-devel
Obsoletes:      openib-perftest < 1.3
ExcludeArch:    s390 %{arm}

%description
Perftest is a collection of simple test programs designed to utilize 
RDMA communications and provide performance numbers over those RDMA
connections.  It does not work on normal TCP/IP networks, only on
RDMA networks.

%prep
%setup -q
find src -type f -iname '*.[ch]' -exec chmod a-x '{}' ';'

%build
%configure
%make_build

%install
for file in ib_{atomic,read,send,write}_{lat,bw} raw_ethernet_{lat,bw}; do
	install -D -m 0755 $file %{buildroot}%{_bindir}/$file
done

%files
%doc README
%license COPYING
%_bindir/*

%changelog
%autochangelog
