%global __remake_config 1

Name:		mstflint
Summary:	Mellanox firmware burning tool
Version:	4.34.0
Release:	%autorelease
# COPYING says the license is your choice of OpenIB.org BSD or GPLv2.
# kernel/Makefile has the 3-clause BSD.
# ext_libs/{iniParser,json,muparser}/ have MIT.
# ext_libs/sqlite/ has the SQLite blessing.
License:	(GPL-2.0-only OR Linux-OpenIB) AND BSD-3-Clause AND MIT AND blessing
Url:		https://github.com/Mellanox/%{name}
Source0: 	https://github.com/Mellanox/%{name}/releases/download/v%{version}-2/%{name}-%{version}-2.tar.gz

BuildRequires:	make
BuildRequires:	libstdc++-devel, zlib-devel, libibmad-devel, gcc-c++, gcc
BuildRequires:  libcurl-devel, boost-devel, libxml2-devel
BuildRequires:  openssl-devel
BuildRequires:  expat-devel
%if %{__remake_config}
BuildRequires:  libtool, autoconf, automake
%endif
Obsoletes:	openib-mstflint <= 1.4 openib-tvflash <= 0.9.2 tvflash <= 0.9.0
ExcludeArch:	s390 s390x %{arm}
Requires:	python3

%description
This package contains firmware update tool, vpd dump and register dump tools
for network adapters based on Mellanox Technologies chips.

%prep
%autosetup -p1 -n %{name}-%{version}

find . -type f -perm /a+x \( -name '*.[ch]' -o -name '*.cpp' \) -exec chmod a-x '{}' '+'

%build
%if %{__remake_config}
./autogen.sh
%endif
%configure --enable-fw-mgr --enable-openssl --enable-adb-generic-tools
%make_build

%install
%make_install
# Remove the devel files that we don't ship
rm -fr %{buildroot}%{_includedir}
find %{buildroot} -type f,l \( -name '*.a' -o -name '*.la' \) -delete

# Mark these shared libs executable for find-debuginfo.sh to find them.
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Debuginfo/
chmod +x %{buildroot}/%{_libdir}/mstflint/{python_tools,sdk}/*.so

%files
%doc README
%_bindir/*
%{_sysconfdir}/mstflint
%{_libdir}/mstflint

%{_datadir}/mstflint
%{_mandir}/man1/*

%changelog
%autochangelog
