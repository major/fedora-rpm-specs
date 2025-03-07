%bcond openssl %[!(0%{?rhel} >= 10)]

%global __remake_config 1

Name:		mstflint
Summary:	Mellanox firmware burning tool
Version:	4.25.0
Release:	%autorelease
# COPYING says the license is your choice of OpenIB.org BSD or GPLv2.
# kernel/Makefile has the 3-clause BSD.
# ext_libs/{iniParser,json,muparser}/ have MIT.
# ext_libs/sqlite/ has the SQLite blessing.
License:	(GPL-2.0-only OR Linux-OpenIB) AND BSD-3-Clause AND MIT AND blessing
Url:		https://github.com/Mellanox/%{name}
Source0: 	https://github.com/Mellanox/%{name}/releases/download/v%{version}-1/%{name}-%{version}-1.tar.gz
Group:		Applications/System

Patch1:		0001-mflash-Fix-build-failure.patch
Patch4: 	add-default-link-flags-for-shared-libraries.patch
Patch6: 	replace-mlxfwreset-with-mstfwreset-in-mstflint-message.patch
# https://github.com/Mellanox/mstflint/pull/1163
Patch7:         fix-build-with-gcc15.patch

BuildRequires:	make
BuildRequires:	libstdc++-devel, zlib-devel, libibmad-devel, gcc-c++, gcc
BuildRequires:  libcurl-devel, boost-devel, libxml2-devel
%if %{with openssl}
BuildRequires:  openssl-devel
%if 0%{?fedora} >= 41
BuildRequires:  openssl-devel-engine
%endif
%endif
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
%setup -q -n %{name}-%{version}

%patch -P1 -p1
%patch -P4 -p1
%patch -P6 -p1
%patch -P7 -p1

find . -type f -iname '*.[ch]' -exec chmod a-x '{}' ';'
find . -type f -iname '*.cpp' -exec chmod a-x '{}' ';'

%build
%if %{__remake_config}
./autogen.sh
%endif
%configure \
%if %{with openssl}
    --enable-fw-mgr --enable-openssl \
%else
    --disable-openssl \
%endif
    --enable-adb-generic-tools
%make_build

%install
%make_install
# Remove the devel files that we don't ship
rm -fr %{buildroot}%{_includedir}
find %{buildroot} -type f -name '*.la' -delete
find %{buildroot} -type f -name '*.a' -delete

# Mark these shared libs executable for find-debuginfo.sh to find them.
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Debuginfo/
chmod +x %{buildroot}/%{_libdir}/mstflint/python_tools/*.so

%files
%doc README
%_bindir/*
%if %{with openssl}
%{_sysconfdir}/mstflint
%endif
%{_libdir}/mstflint

%{_datadir}/mstflint
%{_mandir}/man1/*

%changelog
%autochangelog
