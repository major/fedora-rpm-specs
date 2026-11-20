%global __remake_config 1

%global mainver	4.38.0
%global subver	1

# jsoncpp, muParser and spdlog are not in the RHEL/ELN content set, so we
# must bundle them there. On Fedora, use the system libraries.
# iniparser-devel on RHEL <= 10 lacks a .pc file, so pkg-config detection
# fails; bundle it there too.
%if !0%{?rhel}
%bcond_with bundled_iniparser
%bcond_with bundled_jsoncpp
%bcond_with bundled_muparser
%bcond_with bundled_spdlog
%else
%bcond_without bundled_jsoncpp
%bcond_without bundled_muparser
%bcond_without bundled_spdlog
%if 0%{?rhel} <= 10
%bcond_without bundled_iniparser
%else
%bcond_with bundled_iniparser
%endif
%endif

# COPYING says the license is your choice of OpenIB.org BSD or GPLv2.
# No 3-clause BSD code ends up in the binary: ext_libs/crow is removed in
# %%prep (--enable-remote is off), and of kernel/ only mst.h is used at all
# (dual GPL-2.0/OpenIB, included by mtcr_ul/mtcr_ul_com.c); the 3-clause text
# appears only in kernel/Makefile, which nothing builds.
# ext_libs/fkYAML/ is always bundled and has MIT, so MIT is always in the tag;
# the other MIT libraries (iniParser, json, spdlog) cannot change it.
# ext_libs/muparser/ adds BSD-2-Clause only when it is actually bundled.
# sqlite is never bundled, so its blessing does not apply to the binary.
%global license_exp (GPL-2.0-only OR Linux-OpenIB) AND MIT
%if %{with bundled_muparser}
%global license_exp %{license_exp} AND BSD-2-Clause
%endif

Name:		mstflint
Summary:	Mellanox firmware burning tool
Version:	%{mainver}_%{subver}
Release:	%autorelease
License:	%{license_exp}
Url:		https://github.com/Mellanox/%{name}
# The upstream tarball at %%realSource0 ships prebuilt, non-free libdpa_elf
# blobs (mlxdpa/dpa_elf/*/libdpa_elf). Removing them in %%prep is not enough,
# since they would still be present in the source RPM. Instead, Source0 is a
# repacked version with the blobs stripped out by generate-tarball.sh,
# distinguished from the pristine upstream tarball by a ".free" suffix.
%global realSource0 https://github.com/Mellanox/%{name}/releases/download/v%{mainver}-%{subver}/%{name}-%{mainver}-%{subver}.tar.gz
Source0:	%{name}-%{mainver}-%{subver}.free.tar.gz
Source1:	generate-tarball.sh

BuildRequires:	make
BuildRequires:	libstdc++-devel, zlib-devel, libibmad-devel, gcc-c++, gcc
BuildRequires:	libcurl-devel, boost-devel, libxml2-devel
BuildRequires:	openssl-devel
BuildRequires:	expat-devel
BuildRequires:	sqlite-devel
%if %{without bundled_iniparser}
BuildRequires:	iniparser-devel
%else
Provides:	bundled(iniparser)
%endif
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
%if %{without bundled_spdlog}
BuildRequires:	spdlog-devel
%else
Provides:	bundled(spdlog)
%endif
%if %{__remake_config}
BuildRequires:	libtool, autoconf, automake
%endif
%if 0%{?rhel}
BuildRequires:	hardlink
%endif
Obsoletes:	openib-mstflint <= 1.4 openib-tvflash <= 0.9.2 tvflash <= 0.9.0
ExcludeArch:	s390 %{arm} %{ix86}
Requires:	python3

%patchlist
# fix build with system libraries
# https://github.com/Mellanox/mstflint/pull/1848
0001-mlxconfig-don-t-include-sqlite3.h-via-hardcoded-ext_.patch
0002-configure.ac-use-pkg-config-to-detect-libraries.patch
0003-build-link-jsoncpp-into-the-hand-written-.so-recipes.patch
# use the system CA trust store instead of a private stale bundle
# https://github.com/Mellanox/mstflint/pull/2090
0020-mlxfwupdate-use-the-system-trust-store-instead-of-a-.patch
0021-mlxfwupdate-rename-_ceritifcate-to-_caBundlePath.patch
# device_info: drop the vestigial shebang from the properties modules
# https://github.com/Mellanox/mstflint/pull/2131
0030-device_info-drop-the-vestigial-shebang-from-the-prop.patch
# build: use the system spdlog when pkg-config can find one
# https://github.com/Mellanox/mstflint/pull/2132
0031-build-prefer-a-system-spdlog-when-pkg-config-can-fi.patch
# build: only build the DPA-only ext_libs with --enable-dpa
# https://github.com/Mellanox/mstflint/pull/2133
0032-build-only-build-the-DPA-only-ext_libs-with-enable-dpa.patch

%description
This package contains firmware update tool, vpd dump and register dump tools
for network adapters based on Mellanox Technologies chips.

%prep
%autosetup -p1 -n %{name}-%{mainver}

# Make sure system libraries are used where possible. Delete the bundled
# sources. Exception: Keep */Makefile.am files because Makefiles are listed
# as AC_CONFIG_FILES in configure.ac unconditionally.
# asio/crow (mst_server) and mini-yaml/sole (mlxdpa) are only used with
# --enable-remote / --enable-dpa, which we never enable. Remove their sources
# too, so that turning either feature on would fail loudly instead of silently
# bundling them.
%global _unbundle_dirs ext_libs/sqlite ext_libs/mini-yaml ext_libs/sole
%{!?with_bundled_iniparser:%global _unbundle_dirs %{_unbundle_dirs} ext_libs/iniParser}
%{!?with_bundled_jsoncpp:%global _unbundle_dirs %{_unbundle_dirs} ext_libs/json}
%{!?with_bundled_muparser:%global _unbundle_dirs %{_unbundle_dirs} ext_libs/muparser}
%{!?with_bundled_spdlog:%global _unbundle_dirs %{_unbundle_dirs} ext_libs/spdlog}
# asio and crow have no Makefile in AC_CONFIG_FILES, but asio ships one under
# include/ that the find below would preserve, leaving a directory it cannot
# delete, so remove them wholesale.
rm -rf ext_libs/asio ext_libs/crow
find %{_unbundle_dirs} -mindepth 1 -name Makefile.am -o -print -delete

# kernel/ is a separate out-of-tree module tree; this package never builds or
# installs it. Keep only kernel/mst.h, which mtcr_ul/mtcr_ul_com.c includes,
# and drop the rest so that building the module from here is impossible.
find kernel -mindepth 1 ! -name mst.h -delete

find . -type f -perm /a+x \( -name '*.[ch]' -o -name '*.cpp' \) -exec chmod a-x '{}' '+'

%build
%if %{__remake_config}
autoreconf -fiv
%endif
%configure --enable-fw-mgr --enable-openssl --enable-adb-generic-tools --enable-cables
%make_build

%install
%make_install
# Remove the devel files that we don't ship
rm -fr %{buildroot}%{_includedir}
find %{buildroot} -type f,l \( -name '*.a' -o -name '*.la' \) -delete

# Mark these shared libs executable for find-debuginfo.sh to find them.
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Debuginfo/
chmod +x %{buildroot}/%{_libdir}/mstflint/{python_tools,sdk}/*.so

%if 0%{?rhel}
# rpmlint reports files-duplicated-waste for identical files that are not
# hardlinked. Fedora deduplicates the whole buildroot as part of
# %%__os_install_post (linkdupes from add-determinism), RHEL buildroots
# do not, so hardlink the duplicates here.
hardlink -c %{buildroot}
%endif

%files
%doc README
%_bindir/*
%{_libdir}/mstflint

%{_datadir}/mstflint
%{_mandir}/man1/*

%changelog
%autochangelog
