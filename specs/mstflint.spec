%global __remake_config 1

Name:		mstflint
Summary:	Mellanox firmware burning tool
Version:	4.36.0
Release:	%autorelease
# COPYING says the license is your choice of OpenIB.org BSD or GPLv2.
# kernel/Makefile has the 3-clause BSD.
# ext_libs/{iniParser,json,muparser}/ have MIT.
# ext_libs/sqlite/ has the SQLite blessing.
License:	(GPL-2.0-only OR Linux-OpenIB) AND BSD-3-Clause AND MIT AND blessing
Url:		https://github.com/Mellanox/%{name}
Source0: 	https://github.com/Mellanox/%{name}/releases/download/v%{version}-1/%{name}-%{version}-1.tar.gz

# jsoncpp and muParser are not in the RHEL/ELN content set, so we must
# bundle them there. On Fedora, use the system libraries.
%if !0%{?rhel}
%bcond_with bundled_jsoncpp
%bcond_with bundled_muparser
%else
%bcond_without bundled_jsoncpp
%bcond_without bundled_muparser
%endif

BuildRequires:	make
BuildRequires:	libstdc++-devel, zlib-devel, libibmad-devel, gcc-c++, gcc
BuildRequires:	libcurl-devel, boost-devel, libxml2-devel
BuildRequires:	openssl-devel
BuildRequires:	expat-devel
BuildRequires:	iniparser-devel
BuildRequires:	sqlite-devel
%if %{without bundled_jsoncpp}
BuildRequires:	jsoncpp-devel
%else
Provides:	bundled(jsoncpp)
%endif
%if %{without bundled_muparser}
BuildRequires:	muParser-devel
%else
Provides:	bundled(muParser)
%endif
%if %{__remake_config}
BuildRequires:	libtool, autoconf, automake
%endif
Obsoletes:	openib-mstflint <= 1.4 openib-tvflash <= 0.9.2 tvflash <= 0.9.0
ExcludeArch:	s390 %{arm} %{ix86}
Requires:	python3

%patchlist
# https://github.com/Mellanox/mstflint/pull/1831
0001-mtcr-fix-segfault-in-pciconf-open-when-VSEC-is-not-f.patch
# fix build with system libraries, https://github.com/Mellanox/mstflint/pull/1848
0010-mlxconfig-don-t-include-sqlite3.h-via-hardcoded-ext_.patch
0011-configure.ac-use-pkg-config-to-detect-libraries.patch

%description
This package contains firmware update tool, vpd dump and register dump tools
for network adapters based on Mellanox Technologies chips.

%prep
%autosetup -p1 -n %{name}-%{version}

# Make sure system libraries are used where possible. Delete the bundled
# sources. Exception: Keep */Makefile.am files because Makefiles are listed
# as AC_CONFIG_FILES in configure.ac unconditionally.
%global _unbundle_libs iniParser,sqlite%{!?with_bundled_jsoncpp:,json}%{!?with_bundled_muparser:,muparser}
find ext_libs/{%{_unbundle_libs}} -depth -mindepth 1 -name Makefile.am -prune -o -delete

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
