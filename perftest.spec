Name:           perftest
Summary:        IB Performance Tests
# Upstream uses a dash in the version. Not valid in the Version field, so we use a dot instead.
%global upstream_ver 4.5-0.20
# The directory in the tarball has only the part before the dash.
%global tarball_ver 4.5
Version:        4.5.0.20
Release:        %autorelease
License:        GPLv2 or BSD
Source:         https://github.com/linux-rdma/perftest/releases/download/v4.5-0.20/perftest-4.5-0.20.gac7cca5.tar.gz
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
%setup -q -n %{name}-%{tarball_ver}
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
