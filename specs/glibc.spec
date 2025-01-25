%global glibcsrcdir glibc-2.40.9000-808-g76c3f7f81b
%global glibcversion 2.40.9000
# Pre-release tarballs are pulled in from git using a command that is
# effectively:
#
# git archive HEAD --format=tar --prefix=$(git describe --match 'glibc-*')/ \
#	> $(git describe --match 'glibc-*').tar
# gzip -9 $(git describe --match 'glibc-*').tar
#
# glibc_release_url is only defined when we have a release tarball.
# Conversly, glibc_autorequires is set for development snapshots, where
# dependencies based on symbol versions are inaccurate.
%{lua: if string.match(rpm.expand("%glibcsrcdir"), "^glibc%-[0-9.]+$") then
    rpm.define("glibc_release_url https://ftp.gnu.org/gnu/glibc/")
  end
  local major, minor = string.match(rpm.expand("%glibcversion"),
                                    "^([0-9]+)%.([0-9]+)%.9000$")
  if major and minor then
    rpm.define("glibc_autorequires 1")
    -- The minor version in a .9000 development version lags the actual
    -- symbol version by one.
    local symver = "GLIBC_" .. major .. "." .. (minor + 1)
    rpm.define("glibc_autorequires_symver " .. symver)
  else
    rpm.define("glibc_autorequires 0")
  end}
##############################################################################
# We support the following options:
# --with/--without,
# * testsuite - Running the testsuite.
# * benchtests - Running and building benchmark subpackage.
# * bootstrap - Bootstrapping the package.
# * werror - Build with -Werror
# * docs - Build with documentation and the required dependencies.
# * valgrind - Run smoke tests with valgrind to verify dynamic loader.
#
# You must always run the testsuite for production builds.
# Default: Always run the testsuite.
%bcond_without testsuite
# Default: Always build the benchtests.
%bcond_without benchtests
# Default: Not bootstrapping.
%bcond_with bootstrap
# Default: Enable using -Werror
%bcond_without werror
# Default: Always build documentation.
%bcond_without docs

# Default: Always run valgrind tests if there is architecture support.
%ifarch %{valgrind_arches}
%bcond_without valgrind
%else
%bcond_with valgrind
%endif
# Restrict %%{valgrind_arches} further in case there are problems with
# the smoke test.
%if %{with valgrind}
%ifarch ppc64 ppc64p7
# The valgrind smoke test does not work on ppc64, ppc64p7 (bug 1273103).
%undefine with_valgrind
%endif
%endif

# Build the POWER10 multilib.
%ifarch ppc64le
%define buildpower10 1
%else
%define buildpower10 0
%endif

%if %{with bootstrap}
# Disable benchtests, -Werror, docs, and valgrind if we're bootstrapping
%undefine with_benchtests
%undefine with_werror
%undefine with_docs
%undefine with_valgrind
%endif

# We do our own build flags management.  In particular, see
# glibc_shell_* below.
%undefine _auto_set_build_flags

##############################################################################
# Utility functions for pre/post scripts.  Stick them at the beginning of
# any lua %pre, %post, %postun, etc. sections to have them expand into
# those scripts.  It only works in lua sections and not anywhere else.
%global glibc_post_funcs %{expand:
-- We use lua because there may be no shell that we can run during
-- glibc upgrade. We used to implement much of %%post as a C program,
-- but from an overall maintenance perspective the lua in the spec
-- file was simpler and safer given the operations required.
-- All lua code will be ignored by rpm-ostree; see:
-- https://github.com/projectatomic/rpm-ostree/pull/1869
-- If we add new lua actions to the %%post code we should coordinate
-- with rpm-ostree and ensure that their glibc install is functional.
-- We must not use rpm.execute because this is a RPM 4.15 features and
-- we must still support downstream bootstrap with RPM 4.14 and missing
-- containerized boostrap.

-- Open-code rpm.execute with error message handling.
function post_exec (msg, program, ...)
  if rpm.spawn ~= nil then
    local status = rpm.spawn ({program, ...})
    if status == nil then
      io.stdout:write (msg)
      assert (nil)
    end
  else
    local pid = posix.fork ()
    if pid == 0 then
      posix.exec (program, ...)
      io.stdout:write (msg)
      assert (nil)
    elseif pid > 0 then
      posix.wait (pid)
    end
  end
end

function call_ldconfig ()
  post_exec("Error: call to ldconfig failed.\n",
	    "ldconfig")
end

function update_gconv_modules_cache ()
  local iconv_dir = "%{_libdir}/gconv"
  local iconv_cache = iconv_dir .. "/gconv-modules.cache"
  local iconv_modules = iconv_dir .. "/gconv-modules"
  if posix.utime(iconv_modules) == 0 then
    if posix.utime (iconv_cache) == 0 then
      post_exec ("Error: call to %{_prefix}/sbin/iconvconfig failed.\n",
		 "%{_prefix}/sbin/iconvconfig",
		 "-o", iconv_cache,
		 "--nostdlib",
		 iconv_dir)
    else
      io.stdout:write ("Error: Missing " .. iconv_cache .. " file.\n")
    end
  end
end}

##############################################################################
# %%package glibc - The GNU C Library (glibc) core package.
##############################################################################
Summary: The GNU libc libraries
Name: glibc
Version: %{glibcversion}

# We'll use baserelease here for two reasons:
# - It is known to rpmdev-bumpspec, so it will be properly handled for mass-
#   rebuilds
# - It allows using the Release number without the %%dist tag in the dependency
#   generator to make the generated requires interchangeable between Rawhide
#   and ELN (.elnYY < .fcXX).
%global baserelease 33
Release: %{baserelease}%{?dist}

# Licenses:
#
# High level license status of the glibc source tree:
#
# * In general, GPLv2+ is used by programs, LGPLv2+ is used for
#   libraries.
#
# * LGPLv2+ with exceptions is used for things that are linked directly
#   into dynamically linked programs and shared libraries (e.g. crt
#   files, lib*_nonshared.a).  Historically, this exception also applies
#   to parts of libio.
#
# * GPLv2+ with exceptions is used for parts of the Arm unwinder.
#
# * GFDL is used for the documentation.
#
# * UNICODE v3 is used for the Unicode data files.
#
# * Some other licenses are used in various places (BSD, Inner-Net,
#   ISC, Public Domain, etc.).
#
# Licenses that make an appearance in the source tree but are not used:
#
# * HSRL and FSFAP are only used in test cases, which currently do not
#   ship in binary RPMs, so they are not listed here.
#
# * GPLv3+ is used by manual/texinfo.tex, which we do not use and a test and
#   some scripts that we do not ship, and so it is not listed here.
#
# * LGPLv3+ is used by some Hurd code, which we do not build.
#
# * A copyleft license is used in posix/runtests.c, but it is only a test
#   case and so the license is not listed here.
#
# * A "PCRE License" is used by PCRE.tests, but it is only a test case and
#   so the license is not listed here.
#
# * BSL-1.0 is only used by a test from boost and so the license is not
#   listed here.
#
# * Unlicense is used in an OpenRISC 1000 file which we don't support.
#
# SPDX references:
# https://spdx.org/licenses
# https://docs.fedoraproject.org/en-US/legal/allowed-licenses
# https://gitlab.com/fedora/legal/fedora-license-data
#
# SPDX license string based on evaluation of glibc-2.39 sources by
# ScanCode toolkit (https://github.com/nexB/scancode-toolkit),
# and accounting for exceptions listed above:
License: LGPL-2.1-or-later AND SunPro AND LGPL-2.1-or-later WITH GCC-exception-2.0 AND BSD-3-Clause AND GPL-2.0-or-later AND LGPL-2.1-or-later WITH GNU-compiler-exception AND GPL-2.0-only AND ISC AND LicenseRef-Fedora-Public-Domain AND HPND AND CMU-Mach AND LGPL-2.0-or-later AND Unicode-3.0 AND GFDL-1.1-or-later AND GPL-1.0-or-later AND FSFUL AND MIT AND Inner-Net-2.0 AND X11 AND GPL-2.0-or-later WITH GCC-exception-2.0 AND GFDL-1.3-only AND GFDL-1.1-only

URL: http://www.gnu.org/software/glibc/
Source0: %{?glibc_release_url}%{glibcsrcdir}.tar.xz
Source1: bench.mk
Source2: glibc-bench-compare
Source3: glibc.req.in
Source4: glibc.attr
Source10: wrap-find-debuginfo.sh
Source11: parse-SUPPORTED.py
# Include in the source RPM for reference.
Source12: ChangeLog.old

# glibc_ldso: ABI-specific program interpreter name.  Used for debuginfo
# extraction (wrap-find-debuginfo.sh) and smoke testing ($run_ldso below).
#
# glibc_has_libnldbl: -lnldbl is supported for long double as double.
#
# glibc_has_libmvec: libmvec is available.
#
# glibc_rtld_early_cflags: The ABI baseline for architectures with
# potentially a later baseline.  The --with-rtld-early-cflags=
# configure option is passed to the main glibc build if this macro is
# defined.
%ifarch %{ix86}
%global glibc_ldso /lib/ld-linux.so.2
%global glibc_has_libnldbl 0
%global glibc_has_libmvec 0
%endif
%ifarch aarch64
%global glibc_ldso /lib/ld-linux-aarch64.so.1
%global glibc_has_libnldbl 0
%global glibc_has_libmvec 1
%endif
%ifarch ppc
%global glibc_ldso /lib/ld.so.1
%global glibc_has_libnldbl 1
%global glibc_has_libmvec 0
%endif
%ifarch ppc64
%global glibc_ldso /lib64/ld64.so.1
%global glibc_has_libnldbl 1
%global glibc_has_libmvec 0
%endif
%ifarch ppc64le
%global glibc_ldso /lib64/ld64.so.2
%global glibc_has_libnldbl 1
%global glibc_has_libmvec 0
%define glibc_rtld_early_cflags -mcpu=power8
%endif
%ifarch riscv64
%global glibc_ldso /lib/ld-linux-riscv64-lp64d.so.1
%global glibc_has_libnldbl 0
%global glibc_has_libmvec 0
%endif
%ifarch s390
%global glibc_ldso /lib/ld.so.1
%global glibc_has_libnldbl 1
%global glibc_has_libmvec 0
%define glibc_rtld_early_cflags -march=z13
%endif
%ifarch s390x
%global glibc_ldso /lib/ld64.so.1
%global glibc_has_libnldbl 1
%global glibc_has_libmvec 0
%define glibc_rtld_early_cflags -march=z13
%endif
%ifarch x86_64 x86_64_v2 x86_64_v3 x86_64_v4
%global glibc_ldso /lib64/ld-linux-x86-64.so.2
%global glibc_has_libnldbl 0
%global glibc_has_libmvec 1
%define glibc_rtld_early_cflags -march=x86-64
%endif

# This is necessary to enable source RPM building under noarch, as
# used by some build environments.
%ifarch noarch
%global glibc_ldso /lib/ld.so
%global glibc_has_libnldbl 0
%global glibc_has_libmvec 0
%endif

######################################################################
# Activate the wrapper script for debuginfo generation, by rewriting
# the definition of __debug_install_post.
%{lua:
local wrapper = rpm.expand("%{SOURCE10}")
local sysroot = rpm.expand("%{glibc_sysroot}")
local original = rpm.expand("%{macrobody:__debug_install_post}")
-- Strip leading newline.  It confuses the macro redefinition.
-- Avoid embedded newlines that confuse the macro definition.
original = original:match("^%s*(.-)%s*$"):gsub("\\\n", "")
rpm.define("__debug_install_post bash " .. wrapper
  .. " " .. sysroot .. " %{_prefix}%{glibc_ldso} " .. original)
}

# sysroot package support.  These contain arch-specific packages, so
# turn off the rpmbuild check.
%global _binaries_in_noarch_packages_terminate_build 0
# Variant of %%dist that contains just the distribution release, no affixes.
%{?fedora:%global sysroot_dist fc%{fedora}}
%{?rhel:%global sysroot_dist el%{rhel}}
%{?!sysroot_dist:%global sysroot_dist root}
# The name of the sysroot package.
%global sysroot_package_arch sysroot-%{_arch}-%{sysroot_dist}-%{name}
# Installed path for the sysroot tree.  Must contain /sys-root/, which
# triggers filtering.
%global sysroot_prefix /usr/%{_arch}-redhat-linux/sys-root/%{sysroot_dist}

# The wrapper script relies on the fact that debugedit does not change
# build IDs.
%global _no_recompute_build_ids 1
%undefine _unique_build_ids

%ifarch %{ix86}
# The memory tracing tools (like mtrace, memusage) in glibc-utils only work
# when the corresponding memory tracing libraries are preloaded.  So we ship
# memory allocation tracing/checking libraries in glibc-utils, except on
# i686 where we need to ship them in glibc.i686.  This is because
# glibc-utils.x86_64 will contain only the 64-bit version of these
# libraries.
%global glibc_ship_tracelibs_in_utils 0
%else
%global glibc_ship_tracelibs_in_utils 1
%endif

##############################################################################
# Patches:
# - See each individual patch file for origin and upstream status.
# - For new patches follow template.patch format.
##############################################################################
Patch4: glibc-fedora-linux-tcsetattr.patch
Patch8: glibc-fedora-manual-dircategory.patch
Patch13: glibc-fedora-localedata-rh61908.patch
Patch17: glibc-cs-path.patch
Patch23: glibc-python3.patch
Patch24: glibc-environ-malloc.patch

##############################################################################
# Continued list of core "glibc" package information:
##############################################################################
Obsoletes: glibc-profile < 2.4
Obsoletes: nscd < 2.35
Provides: ldconfig
%if "%{_sbindir}" == "%{_bindir}"
# We rely on filesystem to create the compat symlinks for us
Requires: filesystem(unmerged-sbin-symlinks)
%endif
Provides: /sbin/ldconfig
Provides: /usr/sbin/ldconfig
# Historic file paths provided for backwards compatibility.
Provides: %{glibc_ldso}

# The dynamic linker supports DT_GNU_HASH
Provides: rtld(GNU_HASH)

# We need libgcc for cancellation support in POSIX threads.
Requires: libgcc%{_isa}

Requires: glibc-common = %{version}-%{release}

# Various components (regex, glob) have been imported from gnulib.
Provides: bundled(gnulib)

Requires(pre): basesystem
Requires: basesystem

%ifarch %{ix86}
# Automatically install the 32-bit variant if the 64-bit variant has
# been installed.  This covers the case when glibc.i686 is installed
# after nss_*.x86_64.  (See below for the other ordering.)
Recommends: (nss_db(x86-32) if nss_db(x86-64))
Recommends: (nss_hesiod(x86-32) if nss_hesiod(x86-64))
# Deinstall the glibc32 package if present.  This helps tests that do
# not run against the compose.
Conflicts: glibc32 <= %{version}-%{release}
Obsoletes: glibc32 <= %{version}-%{release}
%endif

# This is for building auxiliary programs like memusage
# For initial glibc bootstraps it can be commented out
%if %{without bootstrap}
BuildRequires: gd-devel libpng-devel zlib-devel
%endif
%if %{with docs}
%endif
%if %{without bootstrap}
BuildRequires: libselinux-devel >= 1.33.4-3
%endif
BuildRequires: audit-libs-devel >= 1.1.3, sed >= 3.95, libcap-devel, gettext
# We need procps-ng (/bin/ps), util-linux (/bin/kill), and gawk (/bin/awk),
# but it is more flexible to require the actual programs and let rpm infer
# the packages. However, until bug 1259054 is widely fixed we avoid the
# following:
# BuildRequires: /bin/ps, /bin/kill, /bin/awk
# And use instead (which should be reverted some time in the future):
BuildRequires: procps-ng, util-linux, gawk
BuildRequires: systemtap-sdt-devel

%if %{with valgrind}
# Require valgrind for smoke testing the dynamic loader to make sure we
# have not broken valgrind.
BuildRequires: valgrind
%endif

# We use python for the microbenchmarks and locale data regeneration
# from unicode sources (carried out manually). We choose python3
# explicitly because it supports both use cases.  On some
# distributions, python3 does not actually install /usr/bin/python3,
# so we also depend on python3-devel.
BuildRequires: python3 python3-devel

# This GCC version is needed for -fstack-clash-protection support.
BuildRequires: gcc >= 7.2.1-6
%global enablekernel 3.2
Conflicts: kernel < %{enablekernel}
%define target %{_target_cpu}-redhat-linux
%ifarch ppc64le
%global target ppc64le-redhat-linux
%endif

# GNU make 4.0 introduced the -O option.
BuildRequires: make >= 4.0

# The intl subsystem generates a parser using bison.
BuildRequires: bison >= 2.7

# binutils 2.30-17 is needed for --generate-missing-build-notes.
BuildRequires: binutils >= 2.30-17

# Earlier releases have broken support for IRELATIVE relocations
Conflicts: prelink < 0.4.2

%if %{without bootstrap}
%if %{with testsuite}
BuildRequires: diffutils
# The testsuite builds static C++ binaries that require a C++ compiler,
# static C++ runtime from libstdc++-static, and lastly static glibc.
BuildRequires: gcc-c++
BuildRequires: libstdc++-static
# A configure check tests for the ability to create static C++ binaries
# before glibc is built and therefore we need a glibc-static for that
# check to pass even if we aren't going to use any of those objects to
# build the tests.
BuildRequires: glibc-static

# libidn2 (but not libidn2-devel) is needed for testing AI_IDN/NI_IDN.
BuildRequires: libidn2

# The testsuite runs mtrace, which is a perl script
BuildRequires: perl-interpreter
%endif
%endif

# The compressed character maps and info files both require gzip for
# building.
#
# We support using gzip (gzip) or bzip (bzip2) at runtime to decompress
# the character maps, but we don't require them with Requires: to be
# able to use the 'locale' program with the installed compressed maps
# since this is a rare activity for most deployments.
BuildRequires: gzip

# Filter out all GLIBC_PRIVATE symbols since they are internal to
# the package and should not be examined by any other tool.
%global __filter_GLIBC_PRIVATE 1
%global __provides_exclude ^libc_malloc_debug\\.so.*$

# For language packs we have glibc require a virtual dependency
# "glibc-langpack" wich gives us at least one installed langpack.
# If no langpack providing 'glibc-langpack' was installed you'd
# get language-neutral support e.g. C, POSIX, and C.UTF-8 locales.
# In the past we used to install the glibc-all-langpacks by default
# but we no longer do this to minimize container and VM sizes.
# Today you must actively use the language packs infrastructure to
# install language support.
Requires: glibc-langpack = %{version}-%{release}
Suggests: glibc-minimal-langpack = %{version}-%{release}

# Suggest extra gconv modules so that they are installed by default but can be
# removed if needed to build a minimal OS image.
Recommends: glibc-gconv-extra%{_isa} = %{version}-%{release}
# Use redhat-rpm-config as a marker for a buildroot configuration, and
# unconditionally pull in glibc-gconv-extra in that case.
Requires: (glibc-gconv-extra%{_isa} = %{version}-%{release} if redhat-rpm-config)

%description
The glibc package contains standard libraries which are used by
multiple programs on the system. In order to save disk space and
memory, as well as to make upgrading easier, common system code is
kept in one place and shared between programs. This particular package
contains the most important sets of shared libraries: the standard C
library and the standard math library. Without these two libraries, a
Linux system will not function.

######################################################################
# libnsl subpackage
######################################################################

%package -n libnsl
Summary: Legacy support library for NIS
Requires: %{name}%{_isa} = %{version}-%{release}

%description -n libnsl
This package provides the legacy version of libnsl library, for
accessing NIS services.

This library is provided for backwards compatibility only;
applications should use libnsl2 instead to gain IPv6 support.

##############################################################################
# glibc "devel" sub-package
##############################################################################
%package devel
Summary: Object files for development using standard C libraries.
Requires: %{name} = %{version}-%{release}
Requires: libxcrypt-devel%{_isa} >= 4.0.0
Requires: kernel-headers >= 3.2
BuildRequires: kernel-headers >= 3.2
# For backwards compatibility, when the glibc-headers package existed.
Provides: glibc-headers = %{version}-%{release}
Provides: glibc-headers(%{_target_cpu})
Obsoletes: glibc-headers < %{version}-%{release}
# For backwards compatibility with alternative Fedora approach to
# work around multilib issue in composes.
%if 0%{?fedora}
%ifarch x86_64
Provides: glibc-headers-x86 = %{version}-%{release}
Obsoletes: glibc-headers-x86 < %{version}-%{release}
%endif
%ifarch s390x
Provides: glibc-headers-s390 = %{version}-%{release}
Obsoletes: glibc-headers-s390 < %{version}-%{release}
%endif
%endif

%description devel
The glibc-devel package contains the object files necessary
for developing programs which use the standard C libraries (which are
used by nearly all programs).  If you are developing programs which
will use the standard C libraries, your system needs to have these
standard object files available in order to create the
executables.

Install glibc-devel if you are going to develop programs which will
use the standard C libraries.

##############################################################################
# glibc "doc" sub-package
##############################################################################
%if %{with docs}
%package doc
Summary: Documentation for GNU libc
BuildArch: noarch
Requires: %{name} = %{version}-%{release}

# Removing texinfo will cause check-safety.sh test to fail because it seems to
# trigger documentation generation based on dependencies.  We need to fix this
# upstream in some way that doesn't depend on generating docs to validate the
# texinfo.  I expect it's simply the wrong dependency for that target.
BuildRequires: texinfo >= 5.0

%description doc
The glibc-doc package contains The GNU C Library Reference Manual in info
format.  Additional package documentation is also provided.
%endif

##############################################################################
# glibc "static" sub-package
##############################################################################
%package static
Summary: C library static libraries for -static linking.
Requires: %{name}-devel = %{version}-%{release}
Requires: libxcrypt-static%{?_isa} >= 4.0.0

%description static
The glibc-static package contains the C library static libraries
for -static linking.  You don't need these, unless you link statically,
which is highly discouraged.

##############################################################################
# glibc "common" sub-package
##############################################################################
%package common
Summary: Common binaries and locale data for glibc
Requires: %{name} = %{version}-%{release}
Recommends: tzdata >= 2003a

%if "%{_sbindir}" == "%{_bindir}"
# We rely on filesystem to create the compat symlinks for us
Requires: filesystem(unmerged-sbin-symlinks)
%endif

%description common
The glibc-common package includes common binaries for the GNU libc
libraries, as well as national language (locale) support.

######################################################################
# File triggers to do ldconfig calls automatically (see rhbz#1380878)
######################################################################

# File triggers for when libraries are added or removed in standard
# paths.
%transfiletriggerin common -P 2000000 -p <lua> -- /lib /usr/lib /lib64 /usr/lib64
%glibc_post_funcs
call_ldconfig()
%end

%transfiletriggerpostun common -P 2000000 -p <lua> -- /lib /usr/lib /lib64 /usr/lib64
%glibc_post_funcs
call_ldconfig()
%end

# We need to run ldconfig manually because __brp_ldconfig assumes that
# glibc itself is always installed in $RPM_BUILD_ROOT, but with sysroots
# we may be installed into a subdirectory of that path.  Therefore we
# unset __brp_ldconfig and run ldconfig by hand with the sysroots path
# passed to -r.
%undefine __brp_ldconfig

######################################################################

%package locale-source
Summary: The sources for the locales
Requires: %{name} = %{version}-%{release}
Requires: %{name}-common = %{version}-%{release}

%description locale-source
The sources for all locales provided in the language packs.
If you are building custom locales you will most likely use
these sources as the basis for your new locale.

# We define a global regular expression to capture all of the locale
# sources. We use it later when constructing the various packages.
%global locale_rx eo syr tok *_*

%{lua:
-- To make lua-mode happy: '

-- List of supported locales.  This is used to generate the langpack
-- subpackages below.  This table needs adjustments if the set of
-- glibc locales changes.  "code" is the glibc code for the language
-- (before the "_".  "name" is the English translation of the language
-- name (for use in subpackage descriptions).  "regions" is a table of
-- variant specifiers (after the "_", excluding "@" and "."
-- variants/charset specifiers).  The table must be sorted by the code
-- field, and the regions table must be sorted as well.
--
-- English translations of language names can be obtained using (for
-- the "aa" language in this example):
--
-- python3 -c 'import langtable; print(langtable.language_name("aa", languageIdQuery="en"))'

local locales =  {
  { code="aa", name="Afar", regions={ "DJ", "ER", "ET" } },
  { code="af", name="Afrikaans", regions={ "ZA" } },
  { code="agr", name="Aguaruna", regions={ "PE" } },
  { code="ak", name="Akan", regions={ "GH" } },
  { code="am", name="Amharic", regions={ "ET" } },
  { code="an", name="Aragonese", regions={ "ES" } },
  { code="anp", name="Angika", regions={ "IN" } },
  {
    code="ar",
    name="Arabic",
    regions={
      "AE",
      "BH",
      "DZ",
      "EG",
      "IN",
      "IQ",
      "JO",
      "KW",
      "LB",
      "LY",
      "MA",
      "OM",
      "QA",
      "SA",
      "SD",
      "SS",
      "SY",
      "TN",
      "YE" 
    } 
  },
  { code="as", name="Assamese", regions={ "IN" } },
  { code="ast", name="Asturian", regions={ "ES" } },
  { code="ayc", name="Southern Aymara", regions={ "PE" } },
  { code="az", name="Azerbaijani", regions={ "AZ", "IR" } },
  { code="be", name="Belarusian", regions={ "BY" } },
  { code="bem", name="Bemba", regions={ "ZM" } },
  { code="ber", name="Berber", regions={ "DZ", "MA" } },
  { code="bg", name="Bulgarian", regions={ "BG" } },
  { code="bhb", name="Bhili", regions={ "IN" } },
  { code="bho", name="Bhojpuri", regions={ "IN", "NP" } },
  { code="bi", name="Bislama", regions={ "VU" } },
  { code="bn", name="Bangla", regions={ "BD", "IN" } },
  { code="bo", name="Tibetan", regions={ "CN", "IN" } },
  { code="br", name="Breton", regions={ "FR" } },
  { code="brx", name="Bodo", regions={ "IN" } },
  { code="bs", name="Bosnian", regions={ "BA" } },
  { code="byn", name="Blin", regions={ "ER" } },
  { code="ca", name="Catalan", regions={ "AD", "ES", "FR", "IT" } },
  { code="ce", name="Chechen", regions={ "RU" } },
  { code="chr", name="Cherokee", regions={ "US" } },
  { code="ckb", name="Central Kurdish", regions={ "IQ" } },
  { code="cmn", name="Mandarin Chinese", regions={ "TW" } },
  { code="crh", name="Crimean Turkish", regions={ "RU", "UA" } },
  { code="cs", name="Czech", regions={ "CZ" } },
  { code="csb", name="Kashubian", regions={ "PL" } },
  { code="cv", name="Chuvash", regions={ "RU" } },
  { code="cy", name="Welsh", regions={ "GB" } },
  { code="da", name="Danish", regions={ "DK" } },
  {
    code="de",
    name="German",
    regions={ "AT", "BE", "CH", "DE", "IT", "LI", "LU" } 
  },
  { code="doi", name="Dogri", regions={ "IN" } },
  { code="dsb", name="Lower Sorbian", regions={ "DE" } },
  { code="dv", name="Divehi", regions={ "MV" } },
  { code="dz", name="Dzongkha", regions={ "BT" } },
  { code="el", name="Greek", regions={ "CY", "GR" } },
  {
    code="en",
    name="English",
    regions={
      "AG",
      "AU",
      "BW",
      "CA",
      "DK",
      "GB",
      "HK",
      "IE",
      "IL",
      "IN",
      "NG",
      "NZ",
      "PH",
      "SC",
      "SG",
      "US",
      "ZA",
      "ZM",
      "ZW" 
    } 
  },
  { code="eo", name="Esperanto", regions={} },
  {
    code="es",
    name="Spanish",
    regions={
      "AR",
      "BO",
      "CL",
      "CO",
      "CR",
      "CU",
      "DO",
      "EC",
      "ES",
      "GT",
      "HN",
      "MX",
      "NI",
      "PA",
      "PE",
      "PR",
      "PY",
      "SV",
      "US",
      "UY",
      "VE" 
    } 
  },
  { code="et", name="Estonian", regions={ "EE" } },
  { code="eu", name="Basque", regions={ "ES" } },
  { code="fa", name="Persian", regions={ "IR" } },
  { code="ff", name="Fulah", regions={ "SN" } },
  { code="fi", name="Finnish", regions={ "FI" } },
  { code="fil", name="Filipino", regions={ "PH" } },
  { code="fo", name="Faroese", regions={ "FO" } },
  { code="fr", name="French", regions={ "BE", "CA", "CH", "FR", "LU" } },
  { code="fur", name="Friulian", regions={ "IT" } },
  { code="fy", name="Western Frisian", regions={ "DE", "NL" } },
  { code="ga", name="Irish", regions={ "IE" } },
  { code="gbm", name="Garhwali", regions={ "IN" } },
  { code="gd", name="Scottish Gaelic", regions={ "GB" } },
  { code="gez", name="Geez", regions={ "ER", "ET" } },
  { code="gl", name="Galician", regions={ "ES" } },
  { code="gu", name="Gujarati", regions={ "IN" } },
  { code="gv", name="Manx", regions={ "GB" } },
  { code="ha", name="Hausa", regions={ "NG" } },
  { code="hak", name="Hakka Chinese", regions={ "TW" } },
  { code="he", name="Hebrew", regions={ "IL" } },
  { code="hi", name="Hindi", regions={ "IN" } },
  { code="hif", name="Fiji Hindi", regions={ "FJ" } },
  { code="hne", name="Chhattisgarhi", regions={ "IN" } },
  { code="hr", name="Croatian", regions={ "HR" } },
  { code="hsb", name="Upper Sorbian", regions={ "DE" } },
  { code="ht", name="Haitian Creole", regions={ "HT" } },
  { code="hu", name="Hungarian", regions={ "HU" } },
  { code="hy", name="Armenian", regions={ "AM" } },
  { code="ia", name="Interlingua", regions={ "FR" } },
  { code="id", name="Indonesian", regions={ "ID" } },
  { code="ig", name="Igbo", regions={ "NG" } },
  { code="ik", name="Inupiaq", regions={ "CA" } },
  { code="is", name="Icelandic", regions={ "IS" } },
  { code="it", name="Italian", regions={ "CH", "IT" } },
  { code="iu", name="Inuktitut", regions={ "CA" } },
  { code="ja", name="Japanese", regions={ "JP" } },
  { code="ka", name="Georgian", regions={ "GE" } },
  { code="kab", name="Kabyle", regions={ "DZ" } },
  { code="kk", name="Kazakh", regions={ "KZ" } },
  { code="kl", name="Kalaallisut", regions={ "GL" } },
  { code="km", name="Khmer", regions={ "KH" } },
  { code="kn", name="Kannada", regions={ "IN" } },
  { code="ko", name="Korean", regions={ "KR" } },
  { code="kok", name="Konkani", regions={ "IN" } },
  { code="ks", name="Kashmiri", regions={ "IN" } },
  { code="ku", name="Kurdish", regions={ "TR" } },
  { code="kv", name="Komi", regions={ "RU" } },
  { code="kw", name="Cornish", regions={ "GB" } },
  { code="ky", name="Kyrgyz", regions={ "KG" } },
  { code="lb", name="Luxembourgish", regions={ "LU" } },
  { code="lg", name="Ganda", regions={ "UG" } },
  { code="li", name="Limburgish", regions={ "BE", "NL" } },
  { code="lij", name="Ligurian", regions={ "IT" } },
  { code="ln", name="Lingala", regions={ "CD" } },
  { code="lo", name="Lao", regions={ "LA" } },
  { code="lt", name="Lithuanian", regions={ "LT" } },
  { code="ltg", name="Latgalian", regions={ "LV" } },
  { code="lv", name="Latvian", regions={ "LV" } },
  { code="lzh", name="Literary Chinese", regions={ "TW" } },
  { code="mag", name="Magahi", regions={ "IN" } },
  { code="mai", name="Maithili", regions={ "IN", "NP" } },
  { code="mdf", name="Moksha", regions={ "RU" } },
  { code="mfe", name="Morisyen", regions={ "MU" } },
  { code="mg", name="Malagasy", regions={ "MG" } },
  { code="mhr", name="Meadow Mari", regions={ "RU" } },
  { code="mi", name="Maori", regions={ "NZ" } },
  { code="miq", name="Miskito", regions={ "NI" } },
  { code="mjw", name="Karbi", regions={ "IN" } },
  { code="mk", name="Macedonian", regions={ "MK" } },
  { code="ml", name="Malayalam", regions={ "IN" } },
  { code="mn", name="Mongolian", regions={ "MN" } },
  { code="mni", name="Manipuri", regions={ "IN" } },
  { code="mnw", name="Mon", regions={ "MM" } },
  { code="mr", name="Marathi", regions={ "IN" } },
  { code="ms", name="Malay", regions={ "MY" } },
  { code="mt", name="Maltese", regions={ "MT" } },
  { code="my", name="Burmese", regions={ "MM" } },
  { code="nan", name="Min Nan Chinese", regions={ "TW" } },
  { code="nb", name="Norwegian Bokmål", regions={ "NO" } },
  { code="nds", name="Low German", regions={ "DE", "NL" } },
  { code="ne", name="Nepali", regions={ "NP" } },
  { code="nhn", name="Tlaxcala-Puebla Nahuatl", regions={ "MX" } },
  { code="niu", name="Niuean", regions={ "NU", "NZ" } },
  { code="nl", name="Dutch", regions={ "AW", "BE", "NL" } },
  { code="nn", name="Norwegian Nynorsk", regions={ "NO" } },
  { code="nr", name="South Ndebele", regions={ "ZA" } },
  { code="nso", name="Northern Sotho", regions={ "ZA" } },
  { code="oc", name="Occitan", regions={ "FR" } },
  { code="om", name="Oromo", regions={ "ET", "KE" } },
  { code="or", name="Odia", regions={ "IN" } },
  { code="os", name="Ossetic", regions={ "RU" } },
  { code="pa", name="Punjabi", regions={ "IN", "PK" } },
  { code="pap", name="Papiamento", regions={ "AW", "CW" } },
  { code="pl", name="Polish", regions={ "PL" } },
  { code="ps", name="Pashto", regions={ "AF" } },
  { code="pt", name="Portuguese", regions={ "BR", "PT" } },
  { code="quz", name="Cusco Quechua", regions={ "PE" } },
  { code="raj", name="Rajasthani", regions={ "IN" } },
  { code="rif", name="Tarifit", regions={ "MA" } },
  { code="ro", name="Romanian", regions={ "RO" } },
  { code="ru", name="Russian", regions={ "RU", "UA" } },
  { code="rw", name="Kinyarwanda", regions={ "RW" } },
  { code="sa", name="Sanskrit", regions={ "IN" } },
  { code="sah", name="Sakha", regions={ "RU" } },
  { code="sat", name="Santali", regions={ "IN" } },
  { code="sc", name="Sardinian", regions={ "IT" } },
  { code="scn", name="Sicilian", regions={ "IT" } },
  { code="sd", name="Sindhi", regions={ "IN" } },
  { code="se", name="Northern Sami", regions={ "NO" } },
  { code="sgs", name="Samogitian", regions={ "LT" } },
  { code="shn", name="Shan", regions={ "MM" } },
  { code="shs", name="Shuswap", regions={ "CA" } },
  { code="si", name="Sinhala", regions={ "LK" } },
  { code="sid", name="Sidamo", regions={ "ET" } },
  { code="sk", name="Slovak", regions={ "SK" } },
  { code="sl", name="Slovenian", regions={ "SI" } },
  { code="sm", name="Samoan", regions={ "WS" } },
  { code="so", name="Somali", regions={ "DJ", "ET", "KE", "SO" } },
  { code="sq", name="Albanian", regions={ "AL", "MK" } },
  { code="sr", name="Serbian", regions={ "ME", "RS" } },
  { code="ss", name="Swati", regions={ "ZA" } },
  { code="ssy", name="Saho", regions={ "ER" } },
  { code="st", name="Southern Sotho", regions={ "ZA" } },
  { code="su", name="Sudanese", regions={ "ID" } },
  { code="sv", name="Swedish", regions={ "FI", "SE" } },
  { code="sw", name="Swahili", regions={ "KE", "TZ" } },
  { code="syr", name="Syriac", regions={} },
  { code="szl", name="Silesian", regions={ "PL" } },
  { code="ta", name="Tamil", regions={ "IN", "LK" } },
  { code="tcy", name="Tulu", regions={ "IN" } },
  { code="te", name="Telugu", regions={ "IN" } },
  { code="tg", name="Tajik", regions={ "TJ" } },
  { code="th", name="Thai", regions={ "TH" } },
  { code="the", name="Chitwania Tharu", regions={ "NP" } },
  { code="ti", name="Tigrinya", regions={ "ER", "ET" } },
  { code="tig", name="Tigre", regions={ "ER" } },
  { code="tk", name="Turkmen", regions={ "TM" } },
  { code="tl", name="Tagalog", regions={ "PH" } },
  { code="tn", name="Tswana", regions={ "ZA" } },
  { code="to", name="Tongan", regions={ "TO" } },
  { code="tok", name="Toki Pona", regions={} },
  { code="tpi", name="Tok Pisin", regions={ "PG" } },
  { code="tr", name="Turkish", regions={ "CY", "TR" } },
  { code="ts", name="Tsonga", regions={ "ZA" } },
  { code="tt", name="Tatar", regions={ "RU" } },
  { code="ug", name="Uyghur", regions={ "CN" } },
  { code="uk", name="Ukrainian", regions={ "UA" } },
  { code="unm", name="Unami language", regions={ "US" } },
  { code="ur", name="Urdu", regions={ "IN", "PK" } },
  { code="uz", name="Uzbek", regions={ "UZ" } },
  { code="ve", name="Venda", regions={ "ZA" } },
  { code="vi", name="Vietnamese", regions={ "VN" } },
  { code="wa", name="Walloon", regions={ "BE" } },
  { code="wae", name="Walser", regions={ "CH" } },
  { code="wal", name="Wolaytta", regions={ "ET" } },
  { code="wo", name="Wolof", regions={ "SN" } },
  { code="xh", name="Xhosa", regions={ "ZA" } },
  { code="yi", name="Yiddish", regions={ "US" } },
  { code="yo", name="Yoruba", regions={ "NG" } },
  { code="yue", name="Cantonese", regions={ "HK" } },
  { code="yuw", name="Yau", regions={ "PG" } },
  { code="zgh", name="Tamazight", regions={ "MA" } },
  { code="zh", name="Mandarin Chinese", regions={ "CN", "HK", "SG", "TW" } },
  { code="zu", name="Zulu", regions={ "ZA" } } 
}

-- Prints a list of LANGUAGE "_" REGION pairs.  The output is expected
-- to be identical to parse-SUPPORTED.py.  Called from the %%prep section.
function print_locale_pairs()
   for i = 1, #locales do
      local locale = locales[i]
      if #locale.regions == 0 then
	 print(locale.code .. "\n")
      else
	 for j = 1, #locale.regions do
	    print(locale.code .. "_" .. locale.regions[j] .. "\n")
	 end
      end
   end
end

local function compute_supplements(locale)
   local lang = locale.code
   local regions = locale.regions
   result = "langpacks-core-" .. lang
   for i = 1, #regions do
      result = result .. " or langpacks-core-" .. lang .. "_" .. regions[i]
   end
   return result
end

-- Emit the definition of a language pack package.
local function lang_package(locale)
   local lang = locale.code
   local langname = locale.name
   local suppl = compute_supplements(locale)
   print(rpm.expand([[

%package langpack-]]..lang..[[

Summary: Locale data for ]]..langname..[[

Provides: glibc-langpack = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
Requires: %{name}-common = %{version}-%{release}
Supplements: ((glibc and (]]..suppl..[[)) unless glibc-all-langpacks)
%description langpack-]]..lang..[[

The glibc-langpack-]]..lang..[[ package includes the basic information required
to support the ]]..langname..[[ language in your applications.
%files -f langpack-]]..lang..[[.filelist langpack-]]..lang..[[
]]))
end

for i = 1, #locales do
   lang_package(locales[i])
end
}

# The glibc-all-langpacks provides the virtual glibc-langpack,
# and thus satisfies glibc's requirement for installed locales.
# Users can add one more other langauge packs and then eventually
# uninstall all-langpacks to save space.
%package all-langpacks
Summary: All language packs for %{name}.
Requires: %{name} = %{version}-%{release}
Requires: %{name}-common = %{version}-%{release}
Provides: %{name}-langpack = %{version}-%{release}
%description all-langpacks

# No %files, this is an empty package. The C/POSIX and
# C.UTF-8 files are already installed by glibc. We create
# minimal-langpack because the virtual provide of
# glibc-langpack needs at least one package installed
# to satisfy it. Given that no-locales installed is a valid
# use case we support it here with this package.
%package minimal-langpack
Summary: Minimal language packs for %{name}.
Provides: glibc-langpack = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
Requires: %{name}-common = %{version}-%{release}
%description minimal-langpack
This is a Meta package that is used to install minimal language packs.
This package ensures you can use C, POSIX, or C.UTF-8 locales, but
nothing else. It is designed for assembling a minimal system.
%files minimal-langpack

# Infrequently used iconv converter modules.
%package gconv-extra
Summary: All iconv converter modules for %{name}.
Requires: %{name}%{_isa} = %{version}-%{release}
Requires: %{name}-common = %{version}-%{release}

%description gconv-extra
This package contains all iconv converter modules built in %{name}.

##############################################################################
# Subpackages for NSS modules except nss_files, nss_compat, nss_dns
##############################################################################

# This should remain it's own subpackage or "Provides: nss_db" to allow easy
# migration from old systems that previously had the old nss_db package
# installed. Note that this doesn't make the migration that smooth, the
# databases still need rebuilding because the formats were different.
# The nss_db package was deprecated in F16 and onwards:
# https://lists.fedoraproject.org/pipermail/devel/2011-July/153665.html
# The different database format does cause some issues for users:
# https://lists.fedoraproject.org/pipermail/devel/2011-December/160497.html
%package -n nss_db
Summary: Name Service Switch (NSS) module using hash-indexed files
Requires: %{name}%{_isa} = %{version}-%{release}
%ifarch x86_64
# Automatically install the 32-bit variant if the 64-bit variant has
# been installed.  This covers the case when glibc.i686 is installed
# before nss_db.x86_64.  (See above for the other ordering.)
Recommends: (nss_db(x86-32) if glibc(x86-32))
%endif

%description -n nss_db
The nss_db Name Service Switch module uses hash-indexed files in /var/db
to speed up user, group, service, host name, and other NSS-based lookups.

%package -n nss_hesiod
Summary: Name Service Switch (NSS) module using Hesiod
Requires: %{name}%{_isa} = %{version}-%{release}
%ifarch x86_64
# Automatically install the 32-bit variant if the 64-bit variant has
# been installed.  This covers the case when glibc.i686 is installed
# before nss_hesiod.x86_64.  (See above for the other ordering.)
Recommends: (nss_hesiod(x86-32) if glibc(x86-32))
%endif

%description -n nss_hesiod
The nss_hesiod Name Service Switch module uses the Domain Name System
(DNS) as a source for user, group, and service information, following
the Hesiod convention of Project Athena.

%package nss-devel
Summary: Development files for directly linking NSS service modules
Requires: %{name}%{_isa} = %{version}-%{release}
Requires: nss_db%{_isa} = %{version}-%{release}
Requires: nss_hesiod%{_isa} = %{version}-%{release}

%description nss-devel
The glibc-nss-devel package contains the object files necessary to
compile applications and libraries which directly link against NSS
modules supplied by glibc.

This is a rare and special use case; regular development has to use
the glibc-devel package instead.

##############################################################################
# glibc "utils" sub-package
##############################################################################
%package utils
Summary: Development utilities from GNU C library
Requires: %{name} = %{version}-%{release}

%description utils
The glibc-utils package contains memusage, a memory usage profiler,
mtrace, a memory leak tracer and xtrace, a function call tracer
which can be helpful during program debugging.

If unsure if you need this, don't install this package.

%if %{with benchtests}
%package benchtests
Summary: Benchmarking binaries and scripts for %{name}
%description benchtests
This package provides built benchmark binaries and scripts to run
microbenchmark tests on the system.
%endif

##############################################################################
# compat-libpthread-nonshared
# See: https://sourceware.org/bugzilla/show_bug.cgi?id=23500
##############################################################################
%package -n compat-libpthread-nonshared
Summary: Compatibility support for linking against libpthread_nonshared.a.

%description -n compat-libpthread-nonshared
This package provides compatibility support for applications that expect
libpthread_nonshared.a to exist. The support provided is in the form of
an empty libpthread_nonshared.a that allows dynamic links to succeed.
Such applications should be adjusted to avoid linking against
libpthread_nonshared.a which is no longer used. The static library
libpthread_nonshared.a is an internal implementation detail of the C
runtime and should not be expected to exist.

%if %{without bootstrap}
%package -n %sysroot_package_arch
Summary: Sysroot package for glibc, %{_arch} architecture
BuildArch: noarch
Provides: sysroot-%{_arch}-%{name}
# The files are not usable for execution, so do not provide nor
# require anything.
AutoReqProv: no

%description -n %sysroot_package_arch
This package contains development files for the glibc package
that can be installed across architectures.
%dnl %%{without bootstrap}
%endif

##############################################################################
# glibc32 (only for use in building GCC, not shipped)
##############################################################################
%ifarch x86_64
%package -n glibc32
Summary: The GNU libc libraries (32-bit)
Conflicts: glibc(x86-32)
%dnl The gcc package does not use ELF dependencies to install glibc32:
%dnl BuildRequires: (glibc32 or glibc-devel(%{__isa_name}-32))
%dnl Not generating the ELF dependencies for glibc32 makes it less likely
%dnl that the package is selected by accident over glibc.i686.
AutoReqProv: no

%description -n glibc32
This package is only used for internal building of multilib aware
packages, like gcc, due to a technical limitation in the distribution
build environment. Any package which needs both 32-bit and 64-bit
runtimes at the same time must install glibc32 (marked as a 64-bit
package) to access the 32-bit development files during a 64-bit build.

This package is not supported or intended for use outside of the
distribution build enviroment. Regular users can install both 32-bit and
64-bit runtimes and development files without any problems.

%endif

##############################################################################
# Prepare for the build.
##############################################################################
%prep
%autosetup -n %{glibcsrcdir} -p1

##############################################################################
# %%prep - Additional prep required...
##############################################################################
# Make benchmark scripts executable
chmod +x benchtests/scripts/*.py scripts/pylint

# Remove all files generated from patching.
find . -type f -size 0 -o -name "*.orig" -exec rm -f {} \;

# Ensure timestamps on configure files are current to prevent
# regenerating them.
touch `find . -name configure`

# Ensure *-kw.h files are current to prevent regenerating them.
touch locale/programs/*-kw.h

# Verify that our locales table is compatible with the locales table
# in the spec file.
set +x
echo '%{lua: print_locale_pairs()}' > localedata/SUPPORTED.spec
set -x
python3 %{SOURCE11} localedata/SUPPORTED > localedata/SUPPORTED.glibc
diff -u \
  --label "spec file" localedata/SUPPORTED.spec \
  --label "glibc localedata/SUPPORTED" localedata/SUPPORTED.glibc
rm localedata/SUPPORTED.spec localedata/SUPPORTED.glibc

##############################################################################
# Build glibc...
##############################################################################
%build
# Log osystem information
uname -a
LD_SHOW_AUXV=1 /bin/true
ld.so --list-diagnostics || true
ld.so --list-tunables || true
cat /proc/cpuinfo
cat /proc/sysinfo 2>/dev/null || true
cat /proc/meminfo
df

# Propgate select compiler flags from redhat-rpm-config.  These flags
# are target-dependent, so we use only those which are specified in
# redhat-rpm-config.  We keep the -m32/-m32/-m64 flags to support
# multilib builds.

%{lua:
-- Split the string argument into keys of an associate array.
-- The values are set to true.
local function string_to_array(s)
    local result = {}
    for e in string.gmatch(s, "%S+") do
        result[e] = true
    end
    return result
end

local inherit_flags = {}

-- These flags are put into the CC and CXX arguments to configure.
-- Alternate builds do not use the flags listed here, only the main build does.
inherit_flags.cc_main = string_to_array [[
-march=armv8-a+lse
-march=armv8.1-a
-march=haswell
-march=i686
-march=x86-64
-march=x86-64-v2
-march=x86-64-v3
-march=x86-64-v4
-march=z13
-march=z14
-march=z15
-march=zEC12
-mcpu=power10
-mcpu=power8
-mcpu=power9
-mtune=generic
-mtune=power10
-mtune=power8
-mtune=power9
-mtune=z13
-mtune=z14
-mtune=z15
-mtune=zEC12
]]

-- Like inherit_flags_cc_main, but also used for alternate builds.
inherit_flags.cc = string_to_array [[
-m31
-m32
-m64
]]

-- These flags are passed through CFLAGS and CXXFLAGS.
inherit_flags.cflags = string_to_array [[
-O2
-O3
-Wall
-Wp,-D_GLIBCXX_ASSERTIONS
-fasynchronous-unwind-tables
-fno-omit-frame-pointer
-fstack-clash-protection
-funwind-tables
-g
-mbackchain
-mbranch-protection=standard
-mfpmath=sse
-mno-omit-leaf-frame-pointer
-msse2
-mstackrealign
-specs=/usr/lib/rpm/redhat/redhat-annobin-cc1
]]

-- Iterate over the build_cflags RPM variable and emit a shell
-- variable that contains the inherited flags of the indicated variant.
local function shell_build_flags(variant)
    local result = {}
    local inherit = assert(inherit_flags[variant])
    for f in string.gmatch(rpm.expand("%build_cflags"), "%S+") do
        if inherit[f] then
	    result[#result + 1] = f
	end
    end
    print("glibc_flags_" .. variant .. "=\"" .. table.concat(result, " ")
          .. "\"\n")
end

shell_build_flags('cc_main') -- Set $glibc_flags_cc_main.
shell_build_flags('cc') -- Set $glibc_flags_cc.
shell_build_flags('cflags') -- Set $glibc_flags_cflags.
}

%if 0%{?_annotated_build} > 0
# libc_nonshared.a cannot be built with the default hardening flags
# because the glibc build system is incompatible with
# -D_FORTIFY_SOURCE.  The object files need to be marked as to be
# skipped in annobin annotations.  (The -specs= variant of activating
# annobin does not work here because of flag ordering issues.)
# See <https://bugzilla.redhat.com/show_bug.cgi?id=1668822>.
BuildFlagsNonshared="-fplugin=annobin -fplugin-arg-annobin-disable -Wa,--generate-missing-build-notes=yes"
%endif

# Special flag to enable annobin annotations for statically linked
# assembler code.  Needs to be passed to make; not preserved by
# configure.
%global glibc_make_flags_as ASFLAGS="-g -Wa,--generate-missing-build-notes=yes"
%global glibc_make_flags %{glibc_make_flags_as}

##############################################################################
# %%build - Generic options.
##############################################################################
EnableKernel="--enable-kernel=%{enablekernel}"

##############################################################################
# build()
#	Build glibc in the directory $1, passing the rest of the arguments
#	as additional configure arguments.  Several
#	global values are used to determine build flags, kernel version,
#	system tap support, etc.
##############################################################################
build()
{
	local builddir=$1
	shift
	rm -rf $builddir
	mkdir $builddir
	pushd $builddir
	../configure "$@" \
		--prefix=%{_prefix} \
		--with-headers=%{_prefix}/include $EnableKernel \
		--with-nonshared-cflags="$BuildFlagsNonshared" \
		--enable-bind-now \
		--build=%{target} \
		--enable-stack-protector=strong \
		--enable-systemtap \
%ifarch %{ix86}
		--disable-multi-arch \
%endif
%if %{without werror}
		--disable-werror \
%endif
		--disable-profile \
%if %{with bootstrap}
		--without-selinux \
%endif
%ifarch aarch64
		--enable-memory-tagging \
%endif
		--disable-crypt \
	        --disable-build-nscd \
	        --disable-nscd \
		--enable-fortify-source ||
		{ cat config.log; false; }

	# We enable DT_GNU_HASH and DT_HASH for ld.so and DSOs to improve
	# compatibility with applications that expect DT_HASH e.g. Epic Games
	# Easy Anti-Cheat.  This is temporary as applications move to
	# supporting only DT_GNU_HASH.  This was initially enabled in Fedora
	# 37.  We must use 'env' because it is the only way to pass, via the
	# environment, two variables that set the initial Makefile values for
	# LDFLAGS used to build shared objects and the dynamic loader.
	env LDFLAGS.so="-Wl,--hash-style=both" \
		LDFLAGS-rtld="-Wl,--hash-style=both" \
		%make_build -r %{glibc_make_flags}
	popd
}

%ifarch x86_64
# Build for the glibc32 package.
build build-%{target}-32 \
  CC="gcc -m32" \
  CXX="g++ -m32" \
  CFLAGS="${glibc_flags_cflags/-m64/-m32}" \
  --host=i686-linux-gnu \
#
%endif

# Default set of compiler options.
build build-%{target} \
  CC="gcc $glibc_flags_cc $glibc_flags_cc_main" \
  CXX="g++ $glibc_flags_cc $glibc_flags_cc_main" \
  CFLAGS="$glibc_flags_cflags" \
  %{?glibc_rtld_early_cflags:--with-rtld-early-cflags=%glibc_rtld_early_cflags} \
%ifarch x86_64
  --enable-cet \
%endif
#

# POWER10 build variant.
%if %{buildpower10}
build build-%{target}-power10 \
  CC="gcc $glibc_flags_cc" \
  CXX="g++ $glibc_flags_cc" \
  CFLAGS="$glibc_flags_cflags" \
  --with-cpu=power10 \
#
%endif


##############################################################################
# Install glibc...
##############################################################################
%install

# The built glibc is installed into a subdirectory of $RPM_BUILD_ROOT.
# For a system glibc that subdirectory is "/" (the root of the filesystem).
# This is called a sysroot (system root) and can be changed if we have a
# distribution that supports multiple installed glibc versions.
%global glibc_sysroot $RPM_BUILD_ROOT

# Create symbolic links for Features/UsrMove (aka UsrMerge, MoveToUsr).
# See below: Remove UsrMove symbolic links.
usrmove_file_names="bin lib lib64 sbin"
for d in $usrmove_file_names ; do
    mkdir -p "%{glibc_sysroot}/usr/$d"
    ln -s "usr/$d" "%{glibc_sysroot}/$d"
done

%ifarch riscv64
# RISC-V ABI wants to install everything in /usr/lib64/lp64d.
# Make these be symlinks to /usr/lib64.  See:
# Make these be symlinks to /lib64 or /usr/lib64 respectively.  See:
# https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/DRHT5YTPK4WWVGL3GIN5BF2IKX2ODHZ3/
for d in %{glibc_sysroot}%{_libdir}; do
	mkdir -p $d
	(cd $d && ln -sf . lp64d)
done
%endif

%ifarch x86_64
# Install for the glibc32 package.
pushd build-%{target}-32
%make_build install_root=%{glibc_sysroot} install
popd
pushd %{glibc_sysroot}
rm -rf etc var usr/bin usr/lib/gconv usr/libexec usr/sbin usr/share
rm -f lib/libnss_db* lib/libnss_hesiod* lib/libnsl* usr/lib/libnsl* usr/lib/libnss*
rm usr/lib/libc_malloc_debug.so
strip -g usr/lib/*.o
popd
mkdir glibc32-headers
cp -a %{glibc_sysroot}%{_includedir} glibc32-headers
%endif

# Build and install:
pushd build-%{target}
%make_build install_root=%{glibc_sysroot} install
%make_build install_root=%{glibc_sysroot} \
	install-locale-files -C ../localedata objdir=`pwd`
popd
# Locale creation via install-locale-files does not group identical files
# via hardlinks, so we must group them ourselves.
hardlink -c %{glibc_sysroot}/usr/lib/locale

%ifarch x86_64
# Verify that there are no unexpected differences in the header files common
# between i386 and x86_64.
diff -ur %{glibc_sysroot}%{_includedir} glibc32-headers/include \
     > glibc-32-64.diff || true
if test -s  glibc-32-64.diff ; then
    if test $(grep -v '^Only in ' glibc-32-64.diff | wc -l) -ne 0; then
	: Unexpected header file differences
	exit 1
    fi
else
    : Missing additional stubs header files.
fi
rm glibc-32-64.diff
rm -rf glibc32-headers
%endif

%if %{glibc_autorequires}
mkdir -p %{glibc_sysroot}/%{_rpmconfigdir} %{glibc_sysroot}/%{_fileattrsdir}
sed < %{SOURCE3} \
    -e s/@VERSION@/%{version}/ \
    -e s/@RELEASE@/%{baserelease}/ \
    -e s/@SYMVER@/%{glibc_autorequires_symver}/ \
    > %{glibc_sysroot}/%{_rpmconfigdir}/glibc.req
cp %{SOURCE4} %{glibc_sysroot}/%{_fileattrsdir}/glibc.attr
%endif

# Implement Changes/Unify_bin_and_sbin.
%if "%{_sbindir}" == "%{_bindir}"
mv %{glibc_sysroot}/usr/sbin/{iconvconfig,zic} %{glibc_sysroot}/%{_bindir}/
%endif

# install_different:
#	Install all core libraries into DESTDIR/SUBDIR. Either the file is
#	installed as a copy or a symlink to the default install (if it is the
#	same). The path SUBDIR_UP is the prefix used to go from
#	DESTDIR/SUBDIR to the default installed libraries e.g.
#	ln -s SUBDIR_UP/foo.so DESTDIR/SUBDIR/foo.so.
#	When you call this function it is expected that you are in the root
#	of the build directory, and that the default build directory is:
#	"../build-%{target}" (relatively).
#	The primary use of this function is to install alternate runtimes
#	into the build directory and avoid duplicating this code for each
#	runtime.
install_different()
{
	local lib libbase libbaseso dlib
	local destdir="$1"
	local subdir="$2"
	local subdir_up="$3"
	local libdestdir="$destdir/$subdir"
	# All three arguments must be non-zero paths.
	if ! [ "$destdir" \
	       -a "$subdir" \
	       -a "$subdir_up" ]; then
		echo "One of the arguments to install_different was emtpy."
		exit 1
	fi
	# Create the destination directory and the multilib directory.
	mkdir -p "$destdir"
	mkdir -p "$libdestdir"
	# Walk all of the libraries we installed...
	for lib in libc math/libm
	do
		libbase=${lib#*/}
		# Take care that `libbaseso' has a * that needs expanding so
		# take care with quoting.
		libbaseso=$(basename %{glibc_sysroot}/%{_libdir}/${libbase}.so.*)
		# Only install if different from default build library.
		if cmp -s ${lib}.so ../build-%{target}/${lib}.so; then
			ln -sf "$subdir_up"/$libbaseso $libdestdir/$libbaseso
		else
			cp -a ${lib}.so $libdestdir/$libbaseso
		fi
	done
}

%if %{buildpower10}
pushd build-%{target}-power10
install_different "$RPM_BUILD_ROOT/%{_libdir}/glibc-hwcaps" power10 ..
popd
%endif


##############################################################################
# Remove the files we don't want to distribute
##############################################################################

# Remove the libNoVersion files.
# XXX: This looks like a bug in glibc that accidentally installed these
#      wrong files. We probably don't need this today.
rm -f %{glibc_sysroot}/%{_libdir}/libNoVersion*

# Remove the old nss modules.
rm -f %{glibc_sysroot}%{_libdir}/libnss1-*
rm -f %{glibc_sysroot}%{_libdir}/libnss-*.so.1

# This statically linked binary is no longer necessary in a world where
# the default Fedora install uses an initramfs, and further we have rpm-ostree
# which captures the whole userspace FS tree.
# Further, see https://github.com/projectatomic/rpm-ostree/pull/1173#issuecomment-355014583
rm -f %{glibc_sysroot}/{usr/,}sbin/sln

##############################################################################
# Remove separate sbin directory
##############################################################################

# 'make install' insists on creating a separate /usr/sbin directory,
# Instead of fighting with this, just move things to the right location.
%if "%{_sbindir}" == "%{_bindir}"
mv "%{glibc_sysroot}/usr/sbin/"* "%{glibc_sysroot}/usr/bin/"
rmdir "%{glibc_sysroot}/usr/sbin"
%endif

######################################################################
# Run ldconfig to create all the symbolic links we need
######################################################################

# Note: This has to happen before creating /etc/ld.so.conf.

mkdir -p %{glibc_sysroot}/var/cache/ldconfig
truncate -s 0 %{glibc_sysroot}/var/cache/ldconfig/aux-cache

# ldconfig is statically linked, so we can use the new version.
%{glibc_sysroot}/%{_sbindir}/ldconfig -N -r %{glibc_sysroot}

##############################################################################
# Install info files
##############################################################################

%if %{with docs}
# Move the info files if glibc installed them into the wrong location.
if [ -d %{glibc_sysroot}%{_prefix}/info -a "%{_infodir}" != "%{_prefix}/info" ]; then
  mkdir -p %{glibc_sysroot}%{_infodir}
  mv -f %{glibc_sysroot}%{_prefix}/info/* %{glibc_sysroot}%{_infodir}
  rm -rf %{glibc_sysroot}%{_prefix}/info
fi

# Compress all of the info files.
gzip -9nvf %{glibc_sysroot}%{_infodir}/libc*

# Copy the debugger interface documentation over to the right location
mkdir -p %{glibc_sysroot}%{_docdir}/glibc
cp elf/rtld-debugger-interface.txt %{glibc_sysroot}%{_docdir}/glibc
cp posix/gai.conf %{glibc_sysroot}%{_docdir}/glibc
%else
rm -f %{glibc_sysroot}%{_infodir}/dir
rm -f %{glibc_sysroot}%{_infodir}/libc.info*
%endif

##############################################################################
# Create locale sub-package file lists
##############################################################################

olddir=`pwd`
pushd %{glibc_sysroot}%{_prefix}/lib/locale
rm -f locale-archive
$olddir/build-%{target}/elf/ld.so \
        --library-path $olddir/build-%{target}/ \
        $olddir/build-%{target}/locale/localedef \
	--alias-file=$olddir/intl/locale.alias \
        --prefix %{glibc_sysroot} --add-to-archive \
        %locale_rx
# Historically, glibc-all-langpacks deleted the file on updates (sic),
# so we need to restore it in the posttrans scriptlet (like the old
# glibc-all-langpacks versions)
ln locale-archive locale-archive.real

# Almost half the LC_CTYPE files in langpacks are identical to the C.utf8
# variant which is installed by default.  When we keep them as hardlinks,
# each langpack ends up retaining a copy.  If we convert these to symbolic
# links instead, we save ~350K each when they get installed that way.
#
# LC_MEASUREMENT and LC_PAPER also have several duplicates but we don't
# bother with these because they are only ~30 bytes each.
pushd %{glibc_sysroot}/usr/lib/locale
for f in $(find %locale_rx -samefile C.utf8/LC_CTYPE); do
  rm $f && ln -s '../C.utf8/LC_CTYPE' $f
done
popd

# Create the file lists for the language specific sub-packages:
for i in %locale_rx 
do
    lang=${i%%_*}
    if [ ! -e langpack-${lang}.filelist ]; then
        echo "%dir %{_prefix}/lib/locale" >> langpack-${lang}.filelist
    fi
    echo "%dir  %{_prefix}/lib/locale/$i" >> langpack-${lang}.filelist
    echo "%{_prefix}/lib/locale/$i/*" >> langpack-${lang}.filelist
done
popd
pushd %{glibc_sysroot}%{_prefix}/share/locale
for i in */LC_MESSAGES/libc.mo
do
    locale=${i%%%%/*}
    lang=${locale%%%%_*}
    echo "%lang($lang) %{_prefix}/share/locale/${i}" \
         >> %{glibc_sysroot}%{_prefix}/lib/locale/langpack-${lang}.filelist
done
popd
mv  %{glibc_sysroot}%{_prefix}/lib/locale/*.filelist .

##############################################################################
# Install configuration files for services
##############################################################################

# Include ld.so.conf
echo 'include ld.so.conf.d/*.conf' > %{glibc_sysroot}/etc/ld.so.conf
truncate -s 0 %{glibc_sysroot}/etc/ld.so.cache
chmod 644 %{glibc_sysroot}/etc/ld.so.conf
mkdir -p %{glibc_sysroot}/etc/ld.so.conf.d
truncate -s 0 %{glibc_sysroot}/etc/gai.conf

# Include %{_libdir}/gconv/gconv-modules.cache
truncate -s 0 %{glibc_sysroot}%{_libdir}/gconv/gconv-modules.cache
chmod 644 %{glibc_sysroot}%{_libdir}/gconv/gconv-modules.cache

# Remove any zoneinfo files; they are maintained by tzdata.
rm -rf %{glibc_sysroot}%{_prefix}/share/zoneinfo

# Make sure %config files have the same timestamp across multilib packages.
#
# XXX: Ideally ld.so.conf should have the timestamp of the spec file, but there
# doesn't seem to be any macro to give us that.  So we do the next best thing,
# which is to at least keep the timestamp consistent. The choice of using
# SOURCE0 is arbitrary.
touch -r %{SOURCE0} %{glibc_sysroot}/etc/ld.so.conf
touch -r inet/etc.rpc %{glibc_sysroot}/etc/rpc

%if %{with benchtests}
# Build benchmark binaries.  Ignore the output of the benchmark runs.
pushd build-%{target}
make BENCH_DURATION=1 bench-build
popd

# Copy over benchmark binaries.
mkdir -p %{glibc_sysroot}%{_prefix}/libexec/glibc-benchtests
cp $(find build-%{target}/benchtests -type f -executable) %{glibc_sysroot}%{_prefix}/libexec/glibc-benchtests/
# ... and the makefile.
for b in %{SOURCE1} %{SOURCE2}; do
	cp $b %{glibc_sysroot}%{_prefix}/libexec/glibc-benchtests/
done
# .. and finally, the comparison scripts.
cp benchtests/scripts/benchout.schema.json %{glibc_sysroot}%{_prefix}/libexec/glibc-benchtests/
cp benchtests/scripts/compare_bench.py %{glibc_sysroot}%{_prefix}/libexec/glibc-benchtests/
cp benchtests/scripts/import_bench.py %{glibc_sysroot}%{_prefix}/libexec/glibc-benchtests/
cp benchtests/scripts/validate_benchout.py %{glibc_sysroot}%{_prefix}/libexec/glibc-benchtests/
%endif

# The #line directives gperf generates do not give the proper
# file name relative to the build directory.
pushd locale
ln -sf programs/*.gperf .
popd
pushd iconv
ln -sf ../locale/programs/charmap-kw.gperf .
popd

%if %{with docs}
# Remove the `dir' info-heirarchy file which will be maintained
# by the system as it adds info files to the install.
rm -f %{glibc_sysroot}%{_infodir}/dir
%endif

# Disallow linking against libc_malloc_debug.
rm %{glibc_sysroot}%{_libdir}/libc_malloc_debug.so

# Strip all of the installed object files.
strip -g %{glibc_sysroot}%{_libdir}/*.o

# The xtrace and memusage scripts have hard-coded paths that need to be
# translated to a correct set of paths using the $LIB token which is
# dynamically translated by ld.so as the default lib directory.
for i in %{glibc_sysroot}%{_prefix}/bin/{xtrace,memusage}; do
%if %{with bootstrap}
  test -w $i || continue
%endif
  sed -e 's~=/%{_lib}/libpcprofile.so~=%{_libdir}/libpcprofile.so~' \
      -e 's~=/%{_lib}/libmemusage.so~=%{_libdir}/libmemusage.so~' \
      -e 's~='\''/\\\$LIB/libpcprofile.so~='\''%{_prefix}/\\$LIB/libpcprofile.so~' \
      -e 's~='\''/\\\$LIB/libmemusage.so~='\''%{_prefix}/\\$LIB/libmemusage.so~' \
      -i $i
done

##############################################################################
# Build an empty libpthread_nonshared.a for compatiliby with applications
# that have old linker scripts that reference this file. We ship this only
# in compat-libpthread-nonshared sub-package.
##############################################################################
ar cr %{glibc_sysroot}%{_libdir}/libpthread_nonshared.a

# Remove UsrMove symbolic links.
# These should not end in the packaged contents.
# They are part of the filesystem package.
for d in $usrmove_file_names ; do
    rm "%{glibc_sysroot}/$d"
done

###############################################################################
# Sysroot package creation.
###############################################################################

%if %{without bootstrap}
mkdir -p %{glibc_sysroot}/%{sysroot_prefix}
pushd %{glibc_sysroot}/%{sysroot_prefix}
mkdir -p usr/lib usr/lib64

cp -a %{glibc_sysroot}/%{_prefix}/include usr/.
%ifarch x86_64
# 32-bit headers for glibc32 don't go in the sysroot.
rm usr/include/gnu/*-32.h
%endif
for lib in lib lib64;  do
%ifarch x86_64
    if [ "$lib" = "lib" ]; then
	# 32-bit libraries built for glibc32 don't go in the sysroot.
	continue
    fi
%endif
    for pfx in "" %{_prefix}/; do
	if test -d %{glibc_sysroot}/$pfx$lib ; then
	    # Implement UsrMove: everything goes into usr/$lib.  Only
	    # copy files directly in $lib.
	    find %{glibc_sysroot}/$pfx$lib -maxdepth 1 -type f \
		| xargs -I '{}' cp  '{}' usr/$lib/.
	    # Symbolic links need to be adjusted for UsrMove: They
	    # need to stay within the same directory.
	    for sl in `find %{glibc_sysroot}/$pfx$lib -maxdepth 1 -type l`; do
		set +x
		slbase=$(basename $sl)
		sltarget=$(basename $(readlink $sl))
		if test "$sltarget" = . ; then
		    # This is the lp64d symbolic link on riscv64, see above.
		    continue
		fi
		if ! test -r usr/$lib/$sltarget; then
		    echo "$sl: inferred $sltarget ($(readlink $sl)) missing"
		    exit 1
		fi
		set -x
		ln -sf $sltarget usr/$lib/$slbase
	    done
	fi
    done
done

# Workaround for the lack of a kernel sysroot package.  Copy the
# kernel headers into the sysroot.
rpm -ql kernel-headers | grep "^/usr/include" | while read f ; do
    if test -f "$f" ; then
        install -D "$f" "./$f"
    fi
done

# Remove the executable bit from files in the sysroot.  This prevents
# debuginfo extraction.
find -type f | xargs chmod a-x

# Use sysroot-relative paths in linker script.  Ignore symbolic links.
sed -e 's,\([^0-9a-zA-Z=*]/lib\),/usr/lib,g' \
    -e 's,\([^0-9a-zA-Z=*]\)/,\1/,g' \
    -i $(find -type f -name 'lib[cm].so')

popd
%dnl %%{without bootstrap}
%endif

##############################################################################
# Beyond this point in the install process we no longer modify the set of
# installed files.
##############################################################################

# Placement of files in subpackages is mostly controlled by the
# %%files section below.  There are some exceptions where a subset of
# files are put in one package and need to be elided from another
# package, and it's not possible to do this easily using explicit file
# lists or directory matching.  For these exceptions. .filelist file
# are created.

# Make the sorting below more consistent.
export LC_ALL=C

# `make_sysroot_filelist PATH FIND-ARGS LIST` writes %%files section
# lines for files and directories in the sysroot under PATH to the
# file LIST, with FIND-ARGS passed to the find command.  The output is
# passed through sort.
make_sysroot_filelist () {
  (
    find "%{glibc_sysroot}$1" \( -type f -o -type l \) $2 \
      -printf "$1/%%P\n" || true
    find "%{glibc_sysroot}$1" -type d $2 -printf "%%%%dir $1/%%P\n" || true
  ) | sort > "$3"
}

# `remove_from_filelist FILE1 FILE2` removes the lines from FILE1
# which are also in FILE2.  The lines must not contain tabs, and the
# file is sorted as a side effect.  The input files must be sorted
# according to the sort command.
remove_from_filelist () {
    comm -23 "$1" "$2" > "$1.tmp"
    mv "$1.tmp" "$1"
}

# `split_sysroot_file_list DIR FIND-ARGS REGEXP MAIN-LIST EXCEPTIONS-LIST`
# creates a list of files in the sysroot subdirectory # DIR.
# Files and directories are enumerated with the find command,
# passing FIND-ARGS as an extra argument.  Those output paths that
# match REGEXP (an POSIX extended regular expression; all whitespace
# in it is removed before matching) are put into EXCEPTIONS-LIST.  The
# remaining files are put into MAIN-LIST.
split_sysroot_file_list () {
  make_sysroot_filelist "$1" "$2" "$4"
  grep -E -e "$(printf %%s "$3" | tr -d '[:space:]')" < "$4" > "$5"
  remove_from_filelist "$4" "$5"
}

# The primary gconv converters are in the glibc package, the rest goes
# into glibc-gconv-extra.  The Z9 and Z900 subpatterns are for
# s390x-specific converters.  The -name clause skips over files
# that are not loadable gconv modules.
split_sysroot_file_list \
  %{_libdir}/gconv '-name *.so' \
  'gconv/
   (CP1252
   |ISO8859-15?
   |UNICODE
   |UTF-[0-9]+
   |ISO-8859-1_CP037_Z900
   |UTF(8|16)_UTF(16|32)_Z9
   )\.so$' \
  gconv-extra.filelist glibc.filelist

##############################################################################
# Run the glibc testsuite
##############################################################################
%check
%if %{with testsuite}

# Run the glibc tests. If any tests fail to build we exit %check with
# an error, otherwise we print the test failure list and the failed
# test output and continue.  Write to standard error to avoid
# synchronization issues with make and shell tracing output if
# standard output and standard error are different pipes.
run_tests () {
  # This hides a test suite build failure, which should be fatal.  We
  # check "Summary of test results:" below to verify that all tests
  # were built and run.
  %make_build check |& tee rpmbuild.check.log >&2
  test -n tests.sum
  if ! grep -Eq '^\s+=== Summary of results ===$' rpmbuild.check.log ; then
    echo "FAIL: test suite build of target: $(basename "$(pwd)")" >& 2
    exit 1
  fi
  set +x
  grep -v ^PASS: tests.sum > rpmbuild.tests.sum.not-passing || true
  if test -n rpmbuild.tests.sum.not-passing ; then
    echo ===================FAILED TESTS===================== >&2
    echo "Target: $(basename "$(pwd)")" >& 2
    cat rpmbuild.tests.sum.not-passing >&2
    while read failed_code failed_test ; do
      for suffix in out test-result ; do
        if test -e "$failed_test.$suffix"; then
	  echo >&2
          echo "=====$failed_code $failed_test.$suffix=====" >&2
          cat -- "$failed_test.$suffix" >&2
	  echo >&2
        fi
      done
    done <rpmbuild.tests.sum.not-passing
  fi

  # Unconditonally dump differences in the system call list.
  echo "* System call consistency checks:" >&2
  cat misc/tst-syscall-list.out >&2
  set -x
}

# Increase timeouts
export TIMEOUTFACTOR=16
parent=$$
echo ====================TESTING=========================

# Default libraries.
pushd build-%{target}
run_tests
popd

%if %{buildpower10}
# Run this test only if the server supports Power10 instructions.
if LD_SHOW_AUXV=1 /bin/true | grep -E "AT_HWCAP2:[^$]*arch_3_1" > /dev/null; then
  echo ====================TESTING -mcpu=power10=============
  pushd build-%{target}-power10
  run_tests
  popd
fi
%endif

echo ====================TESTING END=====================
PLTCMD='/^Relocation section .*\(\.rela\?\.plt\|\.rela\.IA_64\.pltoff\)/,/^$/p'
echo ====================PLT RELOCS LD.SO================
readelf -Wr %{glibc_sysroot}%{_libdir}/ld-*.so | sed -n -e "$PLTCMD"
echo ====================PLT RELOCS LIBC.SO==============
readelf -Wr %{glibc_sysroot}%{_libdir}/libc-*.so | sed -n -e "$PLTCMD"
echo ====================PLT RELOCS END==================

run_ldso="%{glibc_sysroot}/%{_prefix}%{glibc_ldso} --library-path %{glibc_sysroot}/%{_libdir}"

# Show the auxiliary vector as seen by the new library
# (even if we do not perform the valgrind test).
LD_SHOW_AUXV=1 $run_ldso /bin/true

%if 0%{?_enable_debug_packages}
# Finally, check if valgrind runs with the new glibc.
# We want to fail building if valgrind is not able to run with this glibc so
# that we can then coordinate with valgrind to get it fixed before we update
# glibc.
%if %{with valgrind}
$run_ldso /usr/bin/valgrind --error-exitcode=1 \
	$run_ldso /usr/bin/true
# true --help performs some memory allocations.
$run_ldso /usr/bin/valgrind --error-exitcode=1 \
	$run_ldso /usr/bin/true --help >/dev/null
%endif
%endif

%endif


%pre -p <lua>
-- Check that the running kernel is new enough
required = '%{enablekernel}'
rel = posix.uname("%r")
if rpm.vercmp(rel, required) < 0 then
  error("FATAL: kernel too old", 0)
end

-- (1) Remove multilib libraries from previous installs.
-- In order to support in-place upgrades, we must immediately remove
-- all platform directories before installing a new glibc
-- version.  RPM only deletes files removed by updates near the end
-- of the transaction.  If we did not remove all platform
-- directories here, they may be preferred by the dynamic linker
-- during the execution of subsequent RPM scriptlets, likely
-- resulting in process startup failures.

-- Full set of libraries glibc may install.
install_libs = { "anl", "BrokenLocale", "c", "dl", "m", "mvec",
		 "nss_compat", "nss_db", "nss_dns", "nss_files",
		 "nss_hesiod", "pthread", "resolv", "rt", "SegFault",
		 "thread_db", "util" }

-- We are going to remove these libraries. Generally speaking we remove
-- all core libraries in the multilib directory.
-- For the versioned install names, the version are [2.0,9.9*], so we
-- match "libc-2.0.so" and so on up to "libc-9.9*".
-- For the unversioned install names, we match the library plus ".so."
-- followed by digests.
remove_regexps = {}
for i = 1, #install_libs do
  -- Versioned install name.
  remove_regexps[#remove_regexps + 1] = ("lib" .. install_libs[i]
                                         .. "%%-[2-9]%%.[0-9]+%%.so$")
  -- Unversioned install name.
  remove_regexps[#remove_regexps + 1] = ("lib" .. install_libs[i]
                                         .. "%%.so%%.[0-9]+$")
end

-- Two exceptions:
remove_regexps[#install_libs + 1] = "libthread_db%%-1%%.0%%.so"
remove_regexps[#install_libs + 2] = "libSegFault%%.so"

-- We are going to search these directories.
local remove_dirs = { "%{_libdir}/i686",
		      "%{_libdir}/i686/nosegneg",
		      "%{_libdir}/power6",
		      "%{_libdir}/power7",
		      "%{_libdir}/power8",
		      "%{_libdir}/power9",
		    }

-- Add all the subdirectories of the glibc-hwcaps subdirectory.
repeat
  local iter = posix.files("%{_libdir}/glibc-hwcaps")
  if iter ~= nil then
    for entry in iter do
      if entry ~= "." and entry ~= ".." then
        local path = "%{_libdir}/glibc-hwcaps/" .. entry
        if posix.access(path .. "/.", "x") then
          remove_dirs[#remove_dirs + 1] = path
        end
      end
    end
  end
until true

-- Walk all the directories with files we need to remove...
for _, rdir in ipairs (remove_dirs) do
  if posix.access (rdir) then
    -- If the directory exists we look at all the files...
    local remove_files = posix.files (rdir)
    for rfile in remove_files do
      for _, rregexp in ipairs (remove_regexps) do
	-- Does it match the regexp?
	local dso = string.match (rfile, rregexp)
        if (dso ~= nil) then
	  -- Removing file...
	  os.remove (rdir .. '/' .. rfile)
	end
      end
    end
  end
end

%post -p <lua>
%glibc_post_funcs
-- (1) Update /etc/ld.so.conf
-- Next we update /etc/ld.so.conf to ensure that it starts with
-- a literal "include ld.so.conf.d/*.conf".

local ldsoconf = "/etc/ld.so.conf"
local ldsoconf_tmp = "/etc/glibc_post_upgrade.ld.so.conf"

if posix.access (ldsoconf) then

  -- We must have a "include ld.so.conf.d/*.conf" line.
  local have_include = false
  for line in io.lines (ldsoconf) do
    -- This must match, and we don't ignore whitespace.
    if string.match (line, "^include ld.so.conf.d/%%*%%.conf$") ~= nil then
      have_include = true
    end
  end

  if not have_include then
    -- Insert "include ld.so.conf.d/*.conf" line at the start of the
    -- file. We only support one of these post upgrades running at
    -- a time (temporary file name is fixed).
    local tmp_fd = io.open (ldsoconf_tmp, "w")
    if tmp_fd ~= nil then
      tmp_fd:write ("include ld.so.conf.d/*.conf\n")
      for line in io.lines (ldsoconf) do
        tmp_fd:write (line .. "\n")
      end
      tmp_fd:close ()
      local res = os.rename (ldsoconf_tmp, ldsoconf)
      if res == nil then
        io.stdout:write ("Error: Unable to update configuration file (rename).\n")
      end
    else
      io.stdout:write ("Error: Unable to update configuration file (open).\n")
    end
  end
end

-- (2) Rebuild ld.so.cache early.
-- If the format of the cache changes then we need to rebuild
-- the cache early to avoid any problems running binaries with
-- the new glibc.

call_ldconfig()

-- (3) Update gconv modules cache.
-- If the /usr/lib/gconv/gconv-modules.cache exists, then update it
-- with the latest set of modules that were just installed.
-- We assume that the cache is in _libdir/gconv and called
-- "gconv-modules.cache".

update_gconv_modules_cache()

-- (4) On upgrades, restart systemd if installed.  "systemctl -q" does
-- not suppress the error message (which is common in chroots), so
-- open-code rpm.execute with standard error suppressed.
if tonumber(arg[2]) >= 2
   and posix.access("%{_prefix}/bin/systemctl", "x")
then
  if rpm.spawn ~= nil then
    rpm.spawn ({"%{_prefix}/bin/systemctl", "daemon-reexec"},
               {stderr="/dev/null"})
  else
    local pid = posix.fork()
    if pid == 0 then
      posix.redirect2null(2)
      posix.exec("%{_prefix}/bin/systemctl", "daemon-reexec")
    elseif pid > 0 then
      posix.wait(pid)
    end
  end
end

%posttrans all-langpacks -e -p <lua>
-- The old glibc-all-langpacks postun scriptlet deleted the locale-archive
-- file, so we may have to resurrect it on upgrades.
local archive_path = "%{_prefix}/lib/locale/locale-archive"
local real_path = "%{_prefix}/lib/locale/locale-archive.real"
local stat_archive = posix.stat(archive_path)
local stat_real = posix.stat(real_path)
-- If the hard link was removed, restore it.
if stat_archive ~= nil and stat_real ~= nil
    and (stat_archive.ino ~= stat_real.ino
         or stat_archive.dev ~= stat_real.dev) then
  posix.unlink(archive_path)
  stat_archive = nil
end
-- If the file is gone, restore it.
if stat_archive == nil then
  posix.link(real_path, archive_path)
end
-- Remove .rpmsave file potentially created due to config file change.
local save_path = archive_path .. ".rpmsave"
if posix.access(save_path) then
  posix.unlink(save_path)
end

%post gconv-extra -p <lua>
%glibc_post_funcs
update_gconv_modules_cache ()

%postun gconv-extra -p <lua>
%glibc_post_funcs
update_gconv_modules_cache ()

%files -f glibc.filelist
%{_sbindir}/ldconfig
%{_sbindir}/iconvconfig
%{_libexecdir}/getconf
%{_prefix}%{glibc_ldso}
%{_libdir}/libBrokenLocale.so.1
%{_libdir}/libanl.so.1
%{_libdir}/libc.so.6
%{_libdir}/libdl.so.2
%{_libdir}/libm.so.6
%{_libdir}/libnss_compat.so.2
%{_libdir}/libnss_dns.so.2
%{_libdir}/libnss_files.so.2
%{_libdir}/libpthread.so.0
%{_libdir}/libresolv.so.2
%{_libdir}/librt.so.1
%{_libdir}/libthread_db.so.1
%{_libdir}/libutil.so.1
%{_libdir}/libpcprofile.so
%{_libdir}/audit
%if %{glibc_has_libmvec}
%{_libdir}/libmvec.so.1
%endif
%ifarch %{ix86}
# Needs to be in glibc.i686 so that glibc-utils.x86_64 can use it.
%{_libdir}/libmemusage.so
%{_libdir}/libc_malloc_debug.so.0
%endif
%if %{buildpower10}
%{_libdir}/glibc-hwcaps
%endif
%verify(not md5 size mtime) %config(noreplace) /etc/ld.so.conf
%verify(not md5 size mtime) %config(noreplace) /etc/rpc
%dir /etc/ld.so.conf.d
%dir %{_libdir}/gconv
%dir %{_libdir}/gconv/gconv-modules.d
%verify(not md5 size mtime) %config(noreplace) %{_libdir}/gconv/gconv-modules
%verify(not md5 size mtime) %{_libdir}/gconv/gconv-modules.cache
%ifarch s390x
%verify(not md5 size mtime) %config(noreplace) %{_libdir}/gconv/gconv-modules.d/gconv-modules-s390.conf
%endif
%dir %attr(0700,root,root) /var/cache/ldconfig
%attr(0600,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/cache/ldconfig/aux-cache
%attr(0644,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /etc/ld.so.cache
%attr(0644,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /etc/gai.conf
# If rpm doesn't support %license, then use %doc instead.
%{!?_licensedir:%global license %%doc}
%license COPYING COPYING.LIB LICENSES

%files common
%{_bindir}/gencat
%{_bindir}/getconf
%{_bindir}/getent
%{_bindir}/iconv
%{_bindir}/ld.so
%{_bindir}/ldd
%{_bindir}/locale
%{_bindir}/localedef
%{_bindir}/pldd
%{_bindir}/sotruss
%{_bindir}/sprof
%{_bindir}/tzselect
%{_bindir}/zdump
%{_sbindir}/zic
%dir %{_datarootdir}/i18n
%dir %{_datarootdir}/i18n/locales
%dir %{_datarootdir}/i18n/charmaps
%dir %{_prefix}/lib/locale
%{_datarootdir}/locale/locale.alias
%{_prefix}/lib/locale/C.utf8

%files all-langpacks
%{_prefix}/lib/locale/locale-archive
%{_prefix}/lib/locale/locale-archive.real
%{_prefix}/share/locale/*/LC_MESSAGES/libc.mo

%files locale-source
%{_datarootdir}/i18n/locales
%{_datarootdir}/i18n/charmaps

%files devel
%{_includedir}/*
%if %{glibc_autorequires}
%attr(0755,root,root) %{_rpmconfigdir}/glibc.req
%{_fileattrsdir}/glibc.attr
%endif
%{_libdir}/*.o
%{_libdir}/libBrokenLocale.so
%{_libdir}/libanl.a
%{_libdir}/libanl.so
%{_libdir}/libc.so
%{_libdir}/libc_nonshared.a
%{_libdir}/libdl.a
%{_libdir}/libg.a
%{_libdir}/libm.so
%{_libdir}/libmcheck.a
%{_libdir}/libpthread.a
%{_libdir}/libresolv.so
%{_libdir}/librt.a
%{_libdir}/libthread_db.so
%{_libdir}/libutil.a
%if %{glibc_has_libnldbl}
%{_libdir}/libnldbl_nonshared.a
%endif
%if %{glibc_has_libmvec}
%{_libdir}/libmvec.so
%endif
%ifarch x86_64
# This files are included in the buildroot for glibc32 below.
%exclude %{_includedir}/gnu/lib-names-32.h
%exclude %{_includedir}/gnu/stubs-32.h
%endif

%if %{with docs}
%files doc
%{_datarootdir}/doc
%{_infodir}/*.info*
%endif

%files static
%{_libdir}/libBrokenLocale.a
%{_libdir}/libc.a
%{_libdir}/libm.a
%{_libdir}/libresolv.a
%if %{glibc_has_libmvec}
%{_libdir}/libm-%{version}.a
%{_libdir}/libmvec.a
%endif

%files utils
%{_bindir}/memusage
%{_bindir}/memusagestat
%{_bindir}/mtrace
%{_bindir}/pcprofiledump
%{_bindir}/xtrace
%ifnarch %{ix86}
# Needs to be in glibc.i686 so that glibc-utils.x86_64 can use it.
%{_libdir}/libmemusage.so
%{_libdir}/libc_malloc_debug.so.0
%endif

%files -f gconv-extra.filelist gconv-extra
%verify(not md5 size mtime) %config(noreplace) %{_libdir}/gconv/gconv-modules.d/gconv-modules-extra.conf

%files -n nss_db
%{_bindir}/makedb
%{_libdir}/libnss_db.so.2
/var/db/Makefile
%files -n nss_hesiod
%{_libdir}/libnss_hesiod.so.2
%doc hesiod/README.hesiod
%files nss-devel
%{_libdir}/libnss_compat.so
%{_libdir}/libnss_db.so
%{_libdir}/libnss_hesiod.so

%files -n libnsl
%{_libdir}/libnsl.so.1

%if %{with benchtests}
%files benchtests
%{_libexecdir}/glibc-benchtests
%endif

%files -n compat-libpthread-nonshared
%{_libdir}/libpthread_nonshared.a

%if %{without bootstrap}
%files -n sysroot-%{_arch}-%{sysroot_dist}-glibc
%{sysroot_prefix}
%endif

%ifarch x86_64
%files -n glibc32
%{_includedir}/gnu/lib-names-32.h
%{_includedir}/gnu/stubs-32.h
%{_prefix}/lib/*.a
%{_prefix}/lib/*.o
%{_prefix}/lib/*.so*
%{_prefix}/lib/audit/*
%endif

%changelog
* Thu Jan 23 2025 Florian Weimer <fweimer@redhat.com> - 2.40.9000-33
- Apply patch to improve compatibility with environ/malloc misuse

* Thu Jan 23 2025 Florian Weimer <fweimer@redhat.com> - 2.40.9000-32
- Auto-sync with upstream branch master,
  commit 76c3f7f81b7b99fedbff6edc07cddff59e2ae6e2:
- po: Incorporate translations
- Fix underallocation of abort_msg_s struct (CVE-2025-0395)
- Fix typo: _POSIX_REATIME_SIGNALS -> _POSIX_REALTIME_SIGNALS [BZ# 32515]
- aarch64: Add HWCAP_GCS

* Mon Jan 20 2025 Florian Weimer <fweimer@redhat.com> - 2.40.9000-31
- Auto-sync with upstream branch master,
  commit 1ac28b781882e3f14b41dcb06f3f945d53938948:
- stdlib: Test for expected sequence of random numbers from rand
- stdlib: Fix unintended change to the random_r implementation
- NEWS: Add the extensible rseq ABI to new features
- Linux: Do not check unused bytes after sched_getattr in tst-sched_setattr
- aarch64: Fix tests not compatible with targets supporting GCS
- aarch64: Use __alloc_gcs in makecontext
- aarch64: Add GCS user-space allocation logic
- aarch64: Process gnu properties in static exe
- aarch64: Ignore GCS property of ld.so
- aarch64: Handle GCS marking
- aarch64: Use l_searchlist.r_list for bti
- aarch64: Mark objects with GCS property note
- aarch64: Enable GCS in dynamic linked exe
- aarch64: Enable GCS in static linked exe
- aarch64: Add glibc.cpu.aarch64_gcs tunable
- aarch64: Add GCS support for makecontext
- aarch64: Mark swapcontext with indirect_return
- aarch64: Add GCS support for setcontext
- aarch64: Add GCS support to vfork
- aarch64: Add GCS support to longjmp
- aarch64: Define jmp_buf offset for GCS
- elf.h: Define GNU_PROPERTY_AARCH64_FEATURE_1_GCS
- aarch64: Add asm helpers for GCS

* Mon Jan 20 2025 Florian Weimer <fweimer@redhat.com> - 2.40.9000-30
- CVE-2025-0577: getrandom, arc4random could return predictable data
  after fork (#2338960)
- Drop glibc-benchtests-extra-pi-inputs.patch, applied upstream.
- Auto-sync with upstream branch master,
  commit 91bb902f58264a2fd50fbce8f39a9a290dd23706:
- nptl: Use all of g1_start and g_signals
- nptl: rename __condvar_quiesce_and_switch_g1
- nptl: Fix indentation
- nptl: Use a single loop in pthread_cond_wait instaed of a nested loop
- nptl: Remove g_refs from condition variables
- nptl: Remove unnecessary quadruple check in pthread_cond_wait
- nptl: Remove unnecessary catch-all-wake in condvar group switch
- nptl: Update comments and indentation for new condvar implementation
- pthreads NPTL: lost wakeup fix 2
- Linux: Add tests that check that TLS and rseq area are separate
- Consolidate TLS block allocation for static binaries with ld.so
- elf: Iterate over loaded object list in _dl_determine_tlsoffset
- benchtests: Add dummy in put files cospi, cospif, sinpi, sinpif, tanpi, tanpif
- Linux: Fixes for getrandom fork handling
- affinity-inheritance: Overallocate CPU sets
- inet: Add common IPv6 packet header macros
- aarch64: Use 64-bit variable to access the special registers
- x86-64: Cast __rseq_offset to long long int [BZ #32543]
- Linux: Update internal copy of '<sys/rseq.h>'
- nptl: Remove the rseq area from 'struct pthread'
- nptl: Move the rseq area to the 'extra TLS' block
- nptl: Introduce <rseq-access.h> for RSEQ_* accessors
- nptl: add rtld_hidden_proto to __rseq_size and __rseq_offset
- Add Linux 'extra TLS'
- Add generic 'extra TLS'
- nptl: Add rseq auxvals
- Add missing include guards to <dl-tls.h>
- configure: Clear libc_cv_cc_wimplicit_fallthrough if not supported
- elf: Always define TLS_TP_OFFSET
- x86: Add missing #include <features.h> to <thread_pointer.h>
- Move <thread_pointer.h> to kernel-independent sysdeps directories
- math: Fix acosf when building with gcc <= 11

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.9000-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Jan 12 2025 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.40.9000-28
- Rebuilt for the bin-sbin merge (2nd attempt)

* Thu Jan 09 2025 Florian Weimer <fweimer@redhat.com> - 2.40.9000-27
- Drop glibc-nolink-libc.patch, applied upstream.
- Drop glibc-clone-reset-tid.patch, unnecessary due to upstream reverts.
- Add glibc-benchtests-extra-pi-inputs.patch to fix aarch64 build failure.
- Auto-sync with upstream branch master,
  commit 502a71c5785f21ef4e3bad59949fdf86df73d385:
- i686: Regenerate multiarch ulps
- Revert "configure: default to --prefix=/usr on GNU/Linux"
- elf: Minimize library dependencies of tst-nolink-libc.c
- elf: Second ld.so relocation only if libc.so has been loaded
- Revert "x86_64: Remove unused padding from tcbhead_t"
- Revert "nptl: More useful padding in struct pthread"
- LoongArch: Regenerate preconfigure. [bug 32521]
- loongarch: Drop __GI_XXX for strcpy/stpcpy IFUNC implementations
- AArch64: Improve codegen in SVE expm1f and users
- AArch64: Add vector tanpi routines
- AArch64: Add vector cospi routines
- AArch64: Add vector sinpi to libmvec
- math: Remove no-mathvec flag
- AArch64: Improve codegen for SVE log1pf users
- AArch64: Improve codegen for SVE logs
- AArch64: Improve codegen in SVE tans
- AArch64: Improve codegen in AdvSIMD asinh
- math: Add a reference to Clang's <tgmath.h> C23 issue
- Redirect mempcpy and stpcpy only in libc.a
- mlock, mlock2, munlock: Use __attr_access_none macro
- stdlib: random_r: fix unaligned access in initstate and initstate_r [BZ #30584]
- assert: Remove the use of %n from __assert_fail_base (#2318508)
- Translations: Regenerate libc.pot

* Fri Jan  3 2025 Florian Weimer <fweimer@redhat.com> - 2.40.9000-26
- x86_64: Reset TID during clone if !CLONE_VM (#2335406)

* Thu Jan 02 2025 Florian Weimer <fweimer@redhat.com> - 2.40.9000-25
- Update glibc-nolink-libc.patch following upstream development.
- Update glibc-python3.patch to resolve copyright year conflict.
- Auto-sync with upstream branch master,
  commit cc74583f23657515b1d09d0765032422af71de52:
- elf: Remove the remaining uses of GET_ADDR_OFFSET
- elf: Use TLS_DTV_OFFSET in __tls_get_addr
- s390: Define TLS_DTV_OFFSET instead of GET_ADDR_OFFSET
- elf: Introduce generic <dl-tls.h>
- Update copyright dates not handled by scripts/update-copyrights
- Update copyright in generated files by running "make"
- Update copyright dates with scripts/update-copyrights
- mlock, mlock2, munlock: Tell the compiler we don't dereference the pointer
- elf: Add glibc.rtld.execstack
- elf: Do not change stack permission on dlopen/dlmopen
- x86-64: Reorder dynamic linker list in ldd script (bug 32508)
- libio: asprintf should write NULL upon failure
- nptl: More useful padding in struct pthread
- elf: Remove the GET_ADDR_ARGS and related macros from the TLS code
- build-many-glibcs.py: Add --exclude option
- NEWS: Mention testing glibc build with a different set of compilers
- support: Add support_record_failure_barrier
- io: statx, fstatat: Drop nonnull attribute on the path argument
- configure: Improve configure output for C++ Compiler
- getaddrinfo.c: Avoid uninitialized pointer access [BZ #32465]
- include/sys/cdefs.h: Add __attribute_optimization_barrier__
- assert: Use __writev in assert.c [BZ #32492]
- elf: Check PDE load address with non-empty text section
- Add clang specific warning suppression macros
- Add include/libc-misc.h
- Don't redefine INFINITY nor NAN
- assert: ensure posix compliance, add tests for such
- posix: fix system when a child cannot be created [BZ #32450]
- Fix elf: Introduce is_rtld_link_map [BZ #32488]
- elf: Reorder audit events in dlcose to match _dl_fini (bug 32066)
- elf: Call la_objclose for proxy link maps in _dl_fini (bug 32065)
- elf: Signal la_objopen for the proxy link map in dlmopen (bug 31985)
- elf: Add the endswith function to <endswith.h>
- elf: Move _dl_rtld_map, _dl_rtld_audit_state out of GL
- elf: Introduce is_rtld_link_map
- Add F_CREATED_QUERY from Linux 6.12 to bits/fcntl-linux.h
- Add HWCAP_LOONGARCH_LSPW from Linux 6.12 to bits/hwcap.h
- Add MSG_SOCK_DEVMEM from Linux 6.12 to bits/socket.h
- Linux: Accept null arguments for utimensat pathname
- x86_64: Remove unused padding from tcbhead_t
- Add NT_X86_XSAVE_LAYOUT and NT_ARM_POE from Linux 6.12 to elf.h
- Add SCHED_EXT from Linux 6.12 to bits/sched.h
- math: Use tanhf from CORE-MATH
- math: Use sinhf from CORE-MATH
- math: Use coshf from CORE-MATH
- math: Use atanhf from CORE-MATH
- math: Use atan2f from CORE-MATH
- math: Use atanf from CORE-MATH
- math: Use asinhf from CORE-MATH
- math: Use asinf from CORE-MATH
- math: Use acoshf from CORE-MATH
- math: Use acosf from CORE-MATH
- math: Fix the expected carg (inf) results
- math: Fix the expected atan2f (inf) results
- math: Fix the expected atanf (inf) results
- math: Add inf support on gen-auto-libm-tests.c
- math: Fix spurious-divbyzero flag name
- benchtests: Add tanhf benchmark
- benchtests: Add sinhf benchmark
- benchtests: Add coshf benchmark
- benchtests: Add atanhf benchmark
- benchtests: Add atan2f benchmark
- benchtests: Add atanf benchmark
- benchtests: Add asinhf benchmark
- benchtests: Add asinf benchmark
- benchtests: Add acoshf benchmark
- benchtests: Add acosf benchmark
- Update syscall lists for Linux 6.12
- ungetc: Guarantee single char pushback
- sys/platform/x86.h: Do not depend on _Bool definition in C++ mode
- ldbl-96: Set -1 to "int sign_exponent:16"
- x86: Avoid integer truncation with large cache sizes (bug 32470)
- AArch64: Improve codegen of AdvSIMD expf family
- AArch64: Improve codegen of AdvSIMD atan(2)(f)
- AArch64: Improve codegen of AdvSIMD logf function family
- manual: Document more sigaction flags
- Remove duplicated BUILD_CC in Makeconfig
- iconv: do not report error exit with transliteration [BZ #32448]

* Mon Dec 16 2024 DJ Delorie <dj@redhat.com> - 2.40.9000-24
- Auto-sync with upstream branch master,
  commit dd413a4d2f320d5c3bc43e0788919724c89b3dab.
- Fix sysdeps/x86/fpu/Makefile: Split and sort tests
- sysdeps/x86/fpu/Makefile: Split and sort tests
- Use empty initializer to silence GCC 4.9 or older
- Linux: Check for 0 return value from vDSO getrandom probe
- hppa: Update libm-test-ulps
- Revert "Add braces in initializers for GCC 4.9 or older"
- tst-difftime.c: Use "main (void)"
- or1k: Update libm-test-ulps
- htl: move pthread_sigmask into libc.
- htl: move __pthread_sigstate into libc.
- htl: move __pthread_sigstate_destroy into libc.
- Return EXIT_UNSUPPORTED if __builtin_add_overflow unavailable
- ifuncmain9.c: Return EXIT_UNSUPPORTED for GCC 5.4 or older
- include/bits/sigstksz.h: Avoid #elif IS_IN (libsupport)
- regex.h: Avoid #elif __STDC_VERSION__
- tst-assert-c++.cc: Return EXIT_UNSUPPORTED for GCC 4.9 or older
- Add braces in initializers for GCC 4.9 or older
- Return EXIT_UNSUPPORTED if __builtin_mul_overflow unavailable
- tst-minsigstksz-1.c: Return EXIT_UNSUPPORTED for GCC 4.9 or older
- tester.c: Use -Wmemset-transposed-args for GCC 5 or newer
- Makefile.in: Add test to check xcheck rule
- Don't use TEST_CXX as CXX for build
- AArch64: Update libm-test-ulps

* Fri Dec 13 2024 Arjun Shankar <arjun@redhat.com> - 2.40.9000-23
- Auto-sync with upstream branch master,
  commit 97b74cbbb0724c26fbbd5037a6ab9f81ac0a10a1:
- s390: Simplify elf_machine_{load_address, dynamic} [BZ #31799]
- or1k: Update libm-test-ulps
- nptl: Add <thread_pointer.h> for or1k
- Implement C23 atan2pi
- Clear CXX and TEST_CXX if C++ link test fails
- math: Remove __XXX math functions from installed math.h [BZ #32418]
- Optimize bsearch() implementation for performance
- benchtests: Add benchmark test for bsearch
- Implement C23 atanpi
- powerpc64: Fix dl-trampoline.S big-endian / non-ROP build failure
- powerpc: Use correct procedure call standard for getrandom vDSO call (bug 32440)
- Add TEST_CC and TEST_CXX support
- ﻿powerpc64le: ROP changes for the dl-trampoline functions
- malloc: Add tcache path for calloc
- Implement C23 asinpi
- malloc: add indirection for malloc(-like) functions in tests [BZ #32366]
- Implement C23 acospi
- ﻿powerpc64le: ROP changes for the *context and setjmp functions
- nptl: Add <thread_pointer.h> for m68k
- nptl: Add <thread_pointer.h> for RISC-V
- nptl: add RSEQ_SIG for RISC-V
- AArch64: Improve codegen in users of ADVSIMD expm1 helper
- AArch64: Improve codegen in users of ADVSIMD log1p helper
- AArch64: Improve codegen in AdvSIMD logs
- AArch64: Improve codegen in AdvSIMD pow
- s390x: Regenerated ULPs.
- htl: move pthread_condattr_setpshared into libc.
- htl: move pthread_condattr_setclock into libc.
- htl: move pthread_condattr_init into libc.
- htl: move pthread_condattr_getpshared into libc.
- htl: move pthread_condattr_getclock into libc.
- htl: move __pthread_default_condattr into libc.
- htl: move pthread_condattr_destroy into libc.
- math: Add sinpi,cospi,tanpi sparc64 ulps
- math: Add tanpi aarch64 ulps
- math: Exclude internal math symbols for tests [BZ #32414]
- Remove AC_SUBST(libc_cv_mtls_descriptor)
- Implement C23 tanpi
- Fix typo in elf/Makefile:postclean-generated
- math: xfail some sinpi tests for ibm128-libgcc
- math: xfail some cospi tests for ibm128-libgcc
- powerpc: Update ulps
- AArch64: Update libm-test-ulps
- i686: Update libm-test-ulps
- x86-64: Update libm-test-ulps
- Use M_LIT in place of M_MLIT for literals
- Add further test of TLS
- hurd: Protect against servers returning bogus read/write lengths
- Fix and sort variables in Makefiles
- Implement C23 sinpi
- Implement C23 cospi
- malloc: Optimize small memory clearing for calloc
- Use Linux 6.12 in build-many-glibcs.py
- locale: More strictly implement ISO 8601 for Esperanto locale
- elf: Consolidate stackinfo.h
- manual: Describe struct link_map, support link maps with dlinfo
- Add threaded test of sem_trywait
- Add test of ELF hash collisions
- nptl: Add new test for pthread_spin_trylock

* Thu Dec 12 2024 Carlos O'Donell <carlos@redhat.com> - 2.40.9000-22
- Add BuildRequires for gzip to support compressing installed files.

* Fri Nov 29 2024 Florian Weimer <fweimer@redhat.com> - 2.40.9000-21
- Drop glibc-rh2327564-1.patch, glibc-rh2327564-2.patch.  Fixed upstream.
  (#2327564)
- Auto-sync with upstream branch master,
  commit e2436d6f5aa47ce8da80c2ba0f59dfb9ffde08f3:
- malloc: send freed small chunks to smallbin
- AArch64: Remove zva_128 from memset
- benchtests: Add calloc test
- libio: make _IO_least_marker static
- malloc: Avoid func call for tcache quick path in free()
- math: Add internal roundeven_finite
- RISC-V: Use builtin for fma and fmaf
- RISC-V: Use builtin for copysign and copysignf
- Silence most -Wzero-as-null-pointer-constant diagnostics
- sysdeps: linux: Fix output of LD_SHOW_AUXV=1 for AT_RSEQ_*
- nptl: initialize cpu_id_start prior to rseq registration
- math: Fix branch hint for 68d7128942
- ﻿powerpc64le: ROP Changes for strncpy/ppc-mount
- math: Fix non-portability in the computation of signgam in lgammaf
- malloc: Split _int_free() into 3 sub functions
- math: Use tanf from CORE-MATH
- math: Use lgammaf from CORE-MATH
- math: Use erfcf from CORE-MATH
- math: Use erff from CORE-MATH
- math: Split s_erfF in erff and erfc
- math: Use cbrtf from CORE-MATH
- benchtests: Add tanf benchmark
- benchtests: Add lgammaf benchmark
- benchtests: Add erfcf benchmark
- benchtests: Add erff benchmark
- benchtests: Add cbrtf benchmark
- elf: Handle static PIE with non-zero load address [BZ #31799]
- x86/string: Use `movsl` instead of `movsd` in strncat [BZ #32344]
- stdlib: Make getenv thread-safe in more cases
- aarch64: Remove non-temporal load/stores from oryon-1's memset
- aarch64: Remove non-temporal load/stores from oryon-1's memcpy
- ﻿powerpc64le: _init/_fini file changes for ROP
- misc: remove extra va_end in error_tail (bug 32233)
- intl: avoid alloca for arbitrary sizes (bug 32380)

* Thu Nov 21 2024 Florian Weimer <fweimer@redhat.com> - 2.40.9000-20
- Revert aarch64 memset changes (cec3aef3241cec3aef32412779e) (#2327564)

* Wed Nov 20 2024 Florian Weimer <fweimer@redhat.com> - 2.40.9000-19
- Auto-sync with upstream branch master,
  commit 47311cca31e685fa7bfe19bb8cef17d2d3d7fff9:
- manual: Add description of AArch64-specific pkey flags
- AArch64: Add support for memory protection keys
- AArch64: Remove thunderx{,2} memcpy
- powerpc64le: Optimized strcat for POWER10
- powerpc: Improve the inline asm for syscall wrappers
- elf: handle addition overflow in _dl_find_object_update_1 [BZ #32245]
- x86/string: Use `movsl` instead of `movsd` in strncpy/strncat [BZ #32344]
- manual: Fix overeager s/int/size_t/ in memory.texi
- linux: Add support for getrandom vDSO

* Wed Nov 13 2024 Florian Weimer <fweimer@redhat.com> - 2.40.9000-18
- Only relocate ld.so for the second time of libc.so has been loaded

* Mon Nov 11 2024 DJ Delorie <dj@redhat.com> - 2.40.9000-17
- Auto-sync with upstream branch master,
  commit 7b544224f82d20019f9b28522ebf8114a372d1a2.
- stat.h: Fix missing declaration of struct timespec
- mach: Fix __xpg_strerror_r on in-range but undefined errors [BZ #32350]
- x86/string: Use `movsl` instead of `movsd` [BZ #32344]
- Rename new tst-sem17 test to tst-sem18
- Avoid uninitialized result in sem_open when file does not exist
- nptl: initialize rseq area prior to registration
- s390x: Update ulps
- elf: avoid jumping over a needed declaration
- math: Fix log10f on some ABIs
- stdio-common: Add tests for formatted vsnprintf output specifiers
- stdio-common: Add tests for formatted vsprintf output specifiers
- stdio-common: Add tests for formatted vfprintf output specifiers
- stdio-common: Add tests for formatted vdprintf output specifiers
- stdio-common: Add tests for formatted vasprintf output specifiers
- stdio-common: Add tests for formatted vprintf output specifiers
- stdio-common: Add tests for formatted snprintf output specifiers
- stdio-common: Add tests for formatted sprintf output specifiers
- stdio-common: Add tests for formatted fprintf output specifiers
- stdio-common: Add tests for formatted dprintf output specifiers
- stdio-common: Add tests for formatted asprintf output specifiers
- stdio-common: Add tests for formatted printf output specifiers
- nptl: fix __builtin_thread_pointer detection on LoongArch
- math: Fix incorrect results of exp10m1f with some GCC versions
- misc: Align argument name for pkey_*() functions with the manual
- manual: Use more precise wording for memory protection keys
- elf: Switch to main malloc after final ld.so self-relocation
- elf: Introduce _dl_relocate_object_no_relro
- elf: Do not define consider_profiling, consider_symbind as macros
- elf: rtld_multiple_ref is always true
- Add Arm HWCAP2_* constants from Linux 3.15 and 6.2 to <bits/hwcap.h>
- Add feature test macro _ISOC2Y_SOURCE
- added license for sysdeps/ieee754/flt-32/e_gammaf_r.c
- AArch64: Remove SVE erf and erfc tables
- x86_64: Add exp2m1f with FMA
- x86_64: Add exp10m1f with FMA
- math: Use log10p1f from CORE-MATH
- math: Use log1pf from CORE-MATH
- math: Use log2p1f from CORE-MATH
- math: Use log10f from CORE-MATH
- math: Use expm1f from CORE-MATH
- math: Use exp2m1f from CORE-MATH
- math: Use exp10m1f from CORE-MATH
- benchtests: Add log10p1f benchmark
- benchtests: Add log1p benchmark
- benchtests: Add log2p1f benchmark
- benchtests: Add log10f benchmark
- benchtests: Add expm1f benchmark
- benchtests: Add exp2m1f benchmark
- benchtests: Add exp10m1f benchmark
- math: Add e_gammaf_r to glibc code and style
- LoongArch: Add RSEQ_SIG in rseq.h.
- nptl: Add <thread_pointer.h> for LoongArch
- Link tst-clock_gettime with $(librt)
- powerpc64: Obviate the need for ROP protection in clone/clone3
- Add tests of time, gettimeofday, clock_gettime
- Add more tests of pthread attributes initial values
- Document further requirement on mixing streams / file descriptors
- powerpc64le: Adhere to ABI stack alignment requirement
- AArch64: Small optimisation in AdvSIMD erf and erfc
- Revert "elf: Run constructors on cyclic recursive dlopen (bug 31986)"
- elf: Change ldconfig auxcache magic number (bug 32231)
- SHARED-FILES: Mention bundled Linux 6.10 headers.
- libio: Fix crash in fputws [BZ #20632]
- stdio-common: Fix scanf parsing for NaN types [BZ #30647]

* Mon Nov  4 2024 Florian Weimer <fweimer@redhat.com> - 2.40.9000-16
- Exclude 32-bit headers from the x86_64 package

* Mon Oct 28 2024 Florian Weimer <fweimer@redhat.com> - 2.40.9000-15
- Use rpm.spawn instead of posix.fork if availabe (#2291869)

* Mon Oct 28 2024 Florian Weimer <fweimer@redhat.com> - 2.40.9000-14
- Eliminate the glibc-headers package

* Sat Oct 26 2024 Florian Weimer <fweimer@redhat.com> - 2.40.9000-13
- Restore compatibility with libglvnd by reverting
  "elf: Run constructors on cyclic recursive dlopen (bug 31986)"

* Fri Oct 25 2024 Florian Weimer <fweimer@redhat.com> - 2.40.9000-12
- Complete Features/UsrMove (aka UsrMerge, MoveToUsr) transition (#1063607)

* Fri Oct 25 2024 Florian Weimer <fweimer@redhat.com> - 2.40.9000-11
- Rework filelist construction

* Fri Oct 25 2024 Florian Weimer <fweimer@redhat.com> - 2.40.9000-10
- Auto-sync with upstream branch master,
  commit ac73067cb7a328bf106ecd041c020fc61be7e087:
- elf: Fix map_complete Systemtap probe in dl_open_worker

* Fri Oct 25 2024 Florian Weimer <fweimer@redhat.com> - 2.40.9000-9
- Auto-sync with upstream branch master,
  commit 43db5e2c0672cae7edea7c9685b22317eae25471:
- elf: Signal RT_CONSISTENT after relocation processing in dlopen (bug 31986)
- elf: Signal LA_ACT_CONSISTENT to auditors after RT_CONSISTENT switch
- elf: Run constructors on cyclic recursive dlopen (bug 31986)
- Linux: Match kernel text for SCHED_ macros
- libio: Correctly link tst-popen-fork against libpthread

* Thu Oct 24 2024 Patsy Griffin <patsy@redhat.com> - 2.40.9000-8
- Auto-sync with upstream branch master,
  commit c5dd659f22058bf9b371ab1cba07631f1206c674.
- Add more tests of pthread_mutexattr_gettype and pthread_mutexattr_settype
- libio: Fix a deadlock after fork in popen
- configure: default to --prefix=/usr on GNU/Linux
- manual: Document stdio.h functions that may be macros
- Check time arguments to pthread_timedjoin_np and pthread_clockjoin_np
- Add .b4-config file
- linux: Fix tst-syscall-restart.c on old gcc (BZ 32283)
- sparc: Fix restartable syscalls (BZ 32173)
- support: Make support_process_state_wait return the found state
- Enable transliteration rules with two input characters in scn_IT [BZ #32280]

* Mon Oct 14 2024 DJ Delorie <dj@redhat.com> - 2.40.9000-7
- Auto-sync with upstream branch master,
  commit 9d4b4515a88c5d0bbfc7809374f322c507c2d779.
- locale: Fix some spelling typos
- LoongArch: Regenerate loongarch/arch-syscall.h by build-many-glibcs.py update-syscalls.
- manual: Fix and test @deftypef* function formatting
- replace tgammaf by the CORE-MATH implementation
- Add IPPROTO_SMC from Linux 6.11 to netinet/in.h
- misc: Add support for Linux uio.h RWF_ATOMIC flag
- linux: Update stat-generic.h with linux 6.11
- Update kernel version to 6.11 in header constant tests
- linux: Add MAP_DROPPABLE from Linux 6.11
- Update PIDFD_* constants for Linux 6.11
- Update syscall lists for Linux 6.11
- Use Linux 6.11 in build-many-glibcs.py
- Fix header guard in sysdeps/mach/hurd/x86_64/vm_param.h
- rt: more clock_nanosleep tests addendum
- rt: more clock_nanosleep tests
- stdlib: Make abort/_Exit AS-safe (BZ 26275)
- linux: Use GLRO(dl_vdso_time) on time
- linux: Use GLRO(dl_vdso_gettimeofday) on gettimeofday
- S390: Don't use r11 for cu-instructions as used as frame-pointer. [BZ# 32192]
- stdio-common/Makefile: Fix FAIL: lint-makefiles
- Fix whitespace related license issues.
- Add freopen special-case tests: thread cancellation
- hurd: Add missing va_end call in fcntl implementation. [BZ #32234]

* Wed Oct 02 2024 Carlos O'Donell <carlos@redhat.com> - 2.40.9000-6
- Auto-sync with upstream branch master,
  commit a36814e1455093fc9ebfcdf6ef39bb0cf3d447da.
- riscv: align .preinit_array (bug 32228)
- linux: sparc: Fix clone for LEON/sparcv8 (BZ 31394)
- linux: sparc: Fix syscall_cancel for LEON
- math: Improve layout of expf data
- Disable _TIME_BITS if the compiler defaults to it
- Disable _FILE_OFFSET_BITS if the compiler defaults to it
- Do not use -Wp to disable fortify (BZ 31928)
- libio: Set _vtable_offset before calling _IO_link_in [BZ #32148]
- Add a new fwrite test that exercises buffer overflow
- x86/string: Fixup alignment of main loop in str{n}cmp-evex [BZ #32212]
- stdio-common: Fix memory leak in tst-freopen4* tests on UNSUPPORTED
- Linux: Block signals around _Fork (bug 32215)
- Update to Unicode 16.0.0 [BZ #32168]
- manual: Document that feof and ferror are mutually exclusive
- stdio-common: Add new test for fdopen
- Fix missing randomness in __gen_tempname (bug 32214)
- arc: Cleanup arcbe
- arc: Remove HAVE_ARC_BE macro and disable big-endian port
- scripts: Remove arceb-linux-gnu from build-many-glibcs.py
- LoongArch: Undef __NR_fstat and __NR_newfstatat.
- Add tests of fread

* Tue Sep 24 2024 Arjun Shankar <arjun@redhat.com> - 2.40.9000-5
- Auto-sync with upstream branch master,
  commit da29dc24d419656a4a6d6d61598b767b86b1425d:
- nptl: Prefer setresuid32 in tst-setuid2
- elf: Move __rtld_malloc_init_stubs call into _dl_start_final
- elf: Eliminate alloca in open_verify
- elf: Remove version assert in check_match in elf/dl-lookup.c
- elf: In rtld_setup_main_map, assume ld.so has a DYNAMIC segment
- misc: Enable internal use of memory protection keys
- misc: Link tst-mkstemp-fuse-parallel with $(shared-thread-library)
- iconv: Use $(run-program-prefix) for running iconv (bug 32197)
- AArch64: Simplify rounding-multiply pattern in several AdvSIMD routines
- AArch64: Improve codegen in users of ADVSIMD expm1f helper
- AArch64: Improve codegen in users of AdvSIMD log1pf helper
- AArch64: Improve codegen in SVE F32 logs
- AArch64: Improve codegen in SVE expf & related routines
- Linux: readdir64_r should not skip d_ino == 0 entries (bug 32126)
- dirent: Add tst-rewinddir
- dirent: Add tst-readdir-long
- Linux: Use readdir64_r for compat __old_readdir64_r (bug 32128)
- dirent: Add tst-closedir-leaks
- support: Add valgrind instructions to <support/fuse.h>
- support: Fix memory leaks in FUSE tests
- misc: FUSE-based tests for mkstemp
- Add freopen special-case tests: chroot, EFBIG, stdin/stdout/stderr
- Make tst-strtod-underflow type-generic
- Add tests of more strtod special cases
- Add more tests of strtod end pointer
- Make tst-strtod2 and tst-strtod5 type-generic
- Implement run-built-tests=no for make xcheck, always build xtests
- Test that errno is set to 0 at program startup
- Add another test for fclose on an unopened file

* Fri Sep 20 2024 Florian Weimer <fweimer@redhat.com> - 2.40.9000-4
- Auto-sync with upstream branch master,
  commit fa1b0d5e9f6e0353e16339430770a7a8824c0468:
- iconv: Input buffering for the iconv program (bug 6050)
- iconv: Multiple - on command line should not fail (bug 32050)
- iconv: Support in-place conversions (bug 10460, bug 32033)
- iconv: Preserve iconv -c error exit on invalid inputs (bug 32046)
- manual: __is_last is no longer part of iconv internals
- iconv: Do not use mmap in iconv (the program) (bug 17703)
- iconv: Base tests for buffer management
- AArch64: Add vector logp1 alias for log1p
- Linux: Add missing scheduler constants to <sched.h>
- Linux: Add the sched_setattr and sched_getattr functions
- manual: Extract the @manpageurl{func,sec} macro
- AArch64: Remove memset-reg.h
- debug: Fix read error handling in pcprofiledump
- AArch64: Optimize memset
- aarch64: Avoid redundant MOVs in AdvSIMD F32 logs
- Document limitations on streams passed to freopen
- stdlib: Do not use GLIBC_PRIVATE ABI for errno in libc_nonshared.a
- manual: Safety annotations for clock_gettime, clock_getres
- timezone: sync to TZDB 2024b
- Fix freopen handling of ,ccs= (bug 23675)
- powerpc64le: Build new strtod tests with long double ABI flags (bug 32145)

* Thu Sep 19 2024 Florian Weimer <fweimer@redhat.com> - 2.40.9000-3
- Use make xcheck in such a way that xtests are actually built

* Thu Sep 19 2024 Florian Weimer <fweimer@redhat.com> - 2.40.9000-2
- Ensure that xtests can be built

* Thu Sep 05 2024 Florian Weimer <fweimer@redhat.com> - 2.40.9000-1
- Remove RHEL-18039-1.patch, RHEL-18039-2.patch.  Applied upstream.
- Auto-sync with upstream branch master,
  commit 9c0d6f7a1046aba111e25e34ec07242853e859dc:
- Fix memory leak on freopen error return (bug 32140)
- Clear flags2 flags set from mode in freopen (bug 32134)
- Linux: readdir_r needs to report getdents failures (bug 32124)
- libio: Attempt wide backup free only for non-legacy code
- Do not set errno for overflowing NaN payload in strtod/nan (bug 32045)
- powerpc64: Fix syscall_cancel build for powerpc64le-linux-gnu [BZ #32125]
- Fix strtod subnormal rounding (bug 30220)
- manual: Add Descriptor-Relative Access section
- x86: Enable non-temporal memset for Hygon processors
- x86: Add cache information support for Hygon processors
- x86: Add new architecture type for Hygon processors
- ﻿powerpc64: Optimize strcpy and stpcpy for Power9/10
- nptl: Fix Race conditions in pthread cancellation [BZ#12683]
- x86: Unifies 'strnlen-evex' and 'strnlen-evex512' implementations.
- string: strerror, strsignal cannot use buffer after dlmopen (bug 32026)
- ungetc: Fix backup buffer leak on program exit [BZ #27821]
- ungetc: Fix uninitialized read when putting into unused streams [BZ #27821]
- x86: Add `Avoid_STOSB` tunable to allow NT memset without ERMS
- x86: Use `Avoid_Non_Temporal_Memset` to control non-temporal path
- x86: Fix bug in strchrnul-evex512 [BZ #32078]
- manual: Document dprintf and vdprintf
- manual: Document generic printf error codes
- ARC: Regenerate ULPs
- support: Add options list terminator to the test driver
- Define __libc_initial for the static libc
- Turn on -Wimplicit-fallthrough by default if available
- elf: Remove struct dl_init_args from elf/dl-open.c
- nptl: Fix stray process left by tst-cancel7 blocking testing
- nptl: Reorder semaphore release in tst-cancel7
- sysdeps: Re-flow and sort multiline gnu/Makefile definitions
- login: Re-flow and sort multiline Makefile definitions
- benchtests: Add random memset benchmark
- AArch64: Improve generic strlen
- rtld: Fix handling of '--' option
- manual/stdio: Further clarify putc, putwc, getc, and getwc
- stdlib: Allow concurrent quick_exit (BZ 31997)
- elf: Avoid re-initializing already allocated TLS in dlopen (bug 31717)
- elf: Clarify and invert second argument of _dl_allocate_tls_init
- Fix name space violation in fortify wrappers (bug 32052)
- iconv: Fix matching of multi-character transliterations (bug 31859)
- x86: Tunables may incorrectly set Prefer_PMINUB_for_stringop (bug 32047)
- x86: Add missing switch/case fall-through markers to init_cpu_features
- stdlib: Link tst-concurrent-exit with $(shared-thread-library)
- hurd: Fix missing pthread_ compat symbol in libc
- resolv: Fix tst-resolv-short-response for older GCC (bug 32042)
- Add mremap tests
- mremap: Update manual entry
- linux: Update the mremap C implementation [BZ #31968]
- Enhanced test coverage for strncmp, wcsncmp
- Enhance test coverage for strnlen, wcsnlen
- stdlib: Mark `abort` as `cold`
- stdlib: Allow concurrent exit (BZ 31997)
- Add F_DUPFD_QUERY from Linux 6.10 to bits/fcntl-linux.h
- Add STATX_SUBVOL from Linux 6.10 to bits/statx-generic.h
- Update syscall lists for Linux 6.10
- assert: Mark `__assert_fail` as `cold`
- x86-64: Remove sysdeps/x86_64/x32/dl-machine.h

* Wed Jul 31 2024 Patsy Griffin <patsy@redhat.com> - 2.40-3
- Auto-sync with upstream branch release/2.40/master,
  commit 132a72f93cb4ad9f16b8469dc061de5f75f6a44e.
- manual: make setrlimit() description less ambiguous
- manual/stdio: Clarify putc and putwc
- malloc: add multi-threaded tests for aligned_alloc/calloc/malloc
- malloc: avoid global locks in tst-aligned_alloc-lib.c

* Fri Jul 26 2024 Florian Weimer <fweimer@redhat.com> - 2.40-2
- Support clearing options in /etc/resolv.conf, RES_OPTIONS with a - prefix
- Introduce the strict-error/RES_STRICTERR stub resolver option

* Fri Jul 26 2024 Florian Weimer <fweimer@redhat.com> - 2.40-1
- Switch to upstream 2.40 release branch
- Auto-sync with upstream branch release/2.40/master,
  commit 145b5886379c8de4f0a1bca3556a4c3d7b6c24b2:
- manual: Do not mention STATIC_TLS in dynamic linker hardening recommendations
- resolv: Do not wait for non-existing second DNS response after error (bug 30081)
- resolv: Allow short error responses to match any query (bug 31890)
- Increase version number to 2.40
- libc.pot: regenerate (only line number changes)
- x86: Disable non-temporal memset on Skylake Server

* Thu Jul 18 2024 Arjun Shankar <arjun@redhat.com> - 2.39.9000-35
- ppc64le: Build early startup code with -mcpu=power8

* Mon Jul 15 2024 DJ Delorie <dj@redhat.com> - 2.39.9000-34
- Auto-sync with upstream branch master,
  commit a11e15ea0ab1ee8a1947b6be52beca53693f0991.
- math: Update alpha ulps
- hurd: Fix restoring message to be retried
- nptl: Convert tst-sem11 and tst-sem12 tests to use the test driver
- nptl: Add copyright notice tst-sem11 and tst-sem12 tests
- tests: XFAIL audit tests failing on all mips configurations, bug 29404
- time/Makefile: Split and sort tests
- s390x: Fix segfault in wcsncmp [BZ #31934]

* Sat Jul 13 2024 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.39.9000-33
- Rebuilt for the bin-sbin merge (again)

* Wed Jul 10 2024 Florian Weimer <fweimer@redhat.com> - 2.39.9000-32
- Auto-sync with upstream branch master,
  commit 2e456ccf0c34a056e3ccafac4a0c7effef14d918:
- Linux: Make __rseq_size useful for feature detection (bug 31965)
- po: incorporate translations (bg)
- manual: add syscalls
- libio: handle opening a file when all files are closed (bug 31963)
- ldconfig: Ignore all GDB extension files
- ldconfig: Move endswithn into a new header file
- math: Update m68k ULPs
- stdlib: fix arc4random fallback to /dev/urandom (BZ 31612)
- elf: Make dl-rseq-symbols Linux only

* Tue Jul 09 2024 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.39.9000-31
- Rebuilt for the bin-sbin merge
- ldconfig is moved to /usr/bin and paths are adjusted for merged-sbin

* Thu Jul 04 2024 Arjun Shankar <arjun@redhat.com> - 2.39.9000-30
- Auto-sync with upstream branch master,
  commit 2b92982e2369d292560793bee8e730f695f48ff3:
- nptl: fix potential merge of __rseq_* relro symbols
- riscv: Update nofpu libm test ulps
- manual: Recommendations for dynamic linker hardening
- socket: Add new test for shutdown
- elf/rtld: Fix auxiliary vector for enable_secure
- ﻿hppa/vdso: Provide 64-bit clock_gettime() vDSO only
- debug: Fix clang open fortify wrapper (BZ 31927)
- Add --disable-static-c++-tests option [BZ #31797]
- Add --disable-static-c++-link-check option [BZ #31412]
- Update mmap() flags and errors lists
- MIPSr6/math: Use builtin fma and fmaf
- elf: Support recursive use of dynamic TLS in interposed malloc
- Fix conditionals on mtrace-based tests (bug 31892)
- signal/Makefile: Split and sort tests
- x86: Set default non_temporal_threshold for Zhaoxin processors
- x86_64: Optimize large size copy in memmove-ssse3
- x86: Set preferred CPU features on the KH-40000 and KX-7000 Zhaoxin processors
- Aarch64: Add new memset for Qualcomm's oryon-1 core
- Aarch64: Add memcpy for qualcomm's oryon-1 core
- debug: Fix clang open fortify wrapper (BZ 31927)
- debug: Fix clang mq_open fortify wrapper (BZ 31917)
- tests-mbwc: Silence gcc 14 -Werror=format-overflow=

* Thu Jun 27 2024 Patsy Griffin <patsy@redhat.com> - 2.39.9000-29
- Move ANSI_X3.110-1983 support from main package to glibc-gconv-extra.

* Thu Jun 27 2024 Patsy Griffin <patsy@redhat.com> - 2.39.9000-28
- Auto-sync with upstream branch master,
  commit 21738846a19eb4a36981efd37d9ee7cb6d687494.
- time: Avoid memcmp overread in tzset (bug 31931)
- Fix strnlen doc re array size
- arm: Avoid UB in elf_machine_rel()
- LoongArch: Fix tst-gnu2-tls2 test case
- posix: Fix pidfd_spawn/pidfd_spawnp leak if execve fails (BZ 31695)
- INSTALL: regenerate
- Revert "MIPSr6/math: Use builtin fma and fmaf"
- INSTALL: Fix typo ibmlondouble to ibmlongdouble
- RISC-V: Execute a PAUSE hint in spin loops
- MIPSr6/math: Use builtin fma and fmaf
- po: incorporate translations (cs, de, hr, ko, pl, ro, ru, sv, uk, zh_CN)
- mtrace: make shell commands robust against meta characters
- hppa/vdso: Add wrappers for vDSO functions
- Update hppa libm-test-ulps
- Benchtests: Remove broken walk benchmarks
- Update hppa libm-test-ulps
- RISC-V: Update ulps
- MIPS: Update ulps

* Thu Jun 20 2024 Florian Weimer <fweimer@redhat.com> - 2.39.9000-27
- Auto-sync with upstream branch master,
  commit dd144dce21c864781fade4561581d50fb4549956:
- malloc: Replace shell/Perl gate in mtrace
- s390x: Capture grep output in static PIE check
- i386: Update ulps
- malloc: Always install mtrace (bug 31892)
- Translations: Regenerate libc.pot
- s390x: Regenerate ULPs.
- LoongArch: Fix _dl_tlsdesc_dynamic in LSX case
- aarch64: Update ulps
- powerpc: Update ulps
- Linux: Include <dl-symbol-redir-ifunc.h> in dl-sysdep.c
- linux: add definitions for hugetlb page size encodings
- elf: Remove HWCAP_IMPORTANT
- elf: Remove LD_HWCAP_MASK / tunable glibc.cpu.hwcap_mask
- elf: Remove _DL_PLATFORMS_COUNT
- elf: Remove _DL_FIRST_PLATFORM
- elf: Remove _DL_HWCAP_PLATFORM
- elf: Remove platform strings in dl-procinfo.c
- elf: Remove _dl_string_platform
- elf: Remove loading legacy hwcaps/platform entries in dynamic loader
- x86: Remove HWCAP_START and HWCAP_COUNT
- math: Update mips32/mips64 ulps for log2p1
- Convert to autoconf 2.72 (vanilla release, no distribution patches)
- Implement C23 exp2m1, exp10m1
- Implement C23 log10p1
- Implement C23 logp1
- support: Include <limits.h> for NAME_MAX use in temp_file.c
- support: Include <stdlib.h> for atoi use in support_wait_for_thread_exit
- Extend tst-getconf.sh test with NPROCESSORS_CONF and NPROCESSORS_ONLN
- Define ISO 639-3 "ltg" (Latgalian) and add ltg_LV locale
- Minor code improvement to timespec_subtract example
- Modernize and fix doc’s “Date and Time” (BZ 31876)
- manual: minor language fix (bz 31340)
- x86: Fix value for `x86_memset_non_temporal_threshold` when it is undesirable
- elf: Change module-names to modules-names in comments
- resolv: Track single-request fallback via _res._flags (bug 31476)
- x86: Properly set x86 minimum ISA level [BZ #31883]
- tunables: sort tunables list (BZ 30027)
- linux: Remove __stack_prot

* Wed Jun 12 2024 DJ Delorie <dj@redhat.com> - 2.39.9000-26
- Auto-sync with upstream branch master,
  commit e7ac92e6ca9784b397189df0b2e1fb34f425bab8.
- <stdio.h>: Acknowledge that getdelim/getline are in POSIX
- localedata: Lowercase day and abday in cs_CZ
- x86: Properly set MINIMUM_X86_ISA_LEVEL for i386 [BZ #31867]
- x86: Enable non-temporal memset tunable for AMD
- hurd: Fix getxattr/listxattr returning ERANGE
- hurd: Fix setxattr return value on replacing
- hurd: Fix getxattr("gnu.translator") returning ENODATA
- hurd: Fix lsetxattr return value
- localedata: add new locales scn_IT
- support: Fix typo in xgetsockname error message
- getconf: Add NPROCESSORS_{CONF,ONLN} [BZ #31661]
- Linux: Add epoll ioctls
- Improve doc for time_t range (BZ 31808)
- difftime can throw exceptions
- malloc: New test to check malloc alternate path using memory obstruction
- math: Fix exp10 undefined left shift
- libio: Test for fdopen memory leak without SEEK_END support (bug 31840)
- Remove memory leak in fdopen (bug 31840)
- Add new AArch64 HWCAP2 definitions from Linux 6.9 to bits/hwcap.h
- Add more NT_ARM_* constants from Linux kernel to elf.h
- stdlib: Describe __cxa_finalize usage in function comment
- elf: Avoid some free (NULL) calls in _dl_update_slotinfo
- x86: Add seperate non-temporal tunable for memset
- x86: Improve large memset perf with non-temporal stores [RHEL-29312]
- elf: add note identifier for dlopen metadata
- elf: update NT_FDO_PACKAGING_METADATA spec URL

* Wed May 29 2024 Arjun Shankar <arjun@redhat.com> - 2.39.9000-25
- Auto-sync with upstream branch master,
  commit 0c1d2c277a59f08fd3232b33d18644ea890190ea:
- LoongArch: Use "$fcsr0" instead of "$r0" in _FPU_{GET,SET}CW
- x86_64: Reformat elf_machine_rela
- i386: Disable Intel Xeon Phi tests for GCC 15 and above (BZ 31782)
- difftime is pure, not const
- parse_fdinfo: Don't advance pointer twice [BZ #31798]
- elf/Makefile: Split and sort PIE tests
- Revert "Test fscanf of long double without <stdio.h>"
- sysdeps/ieee754/ldbl-opt/Makefile: Split and sort libnldbl-calls
- Test fscanf of long double without <stdio.h>
- sysdeps/ieee754/ldbl-opt/Makefile: Remove test-nldbl-redirect-static
- sysdeps/ieee754/ldbl-opt/Makefile: Split and sort tests
- s390x: Regenerate ULPs.
- powerpc: Remove duplicated versionsort from libm.a (BZ 31789)
- Update kernel version to 6.9 in header constant tests
- localedata: cv_RU: update translation

* Thu May 23 2024 Patsy Griffin <patsy@redhat.com> - 2.39.9000-24
- Auto-sync with upstream branch master,
  commit eaa8113bf0eb599025e3efdbe1bb214ee8dc645a.
- math: Provide missing math symbols on libc.a (BZ 31781)
- s390: Make utmp32, utmpx32, and login32 shared only (BZ 31790)
- microblaze: Remove cacheflush from libc.a (BZ 31788)
- powerpc: Remove duplicated llrintf and llrintf32 from libm.a (BZ 31787)
- powerpc: Remove duplicate strchrnul and strncasecmp_l libc.a (BZ 31786)
- loongarch: Remove duplicate strnlen in libc.a (BZ 31785)
- aarch64: Remove duplicate memchr/strlen in libc.a (BZ 31777)
- Update PIDFD_* constants for Linux 6.9
- Define write_profiling functions only in profile library [BZ #31756]
- Don't provide XXXf128_do_not_use aliases [BZ #31757]
- Don't provide scalb/significand _FloatN aliases [BZ #31760]
- math: Fix isnanf128 static build (BZ 31774)
- math: Add support for auto static math tests
- Change _IO_stderr_/_IO_stdin_/_IO_stdout to compat symbols [BZ #31766]
- Obsolete _dl_mcount_wrapper in glibc 2.40 [BZ #31765]
- math: Fix i386 and m68k exp10 on static build (BZ 31775)
- math: Fix i386 and m68k fmod/fmodf on static build (BZ 31488)
- Remove the clone3 symbol from libc.a [BZ #31770]
- aarch64/fpu: Add vector variants of pow
- Compile libmvec with -fno-math-errno
- manual: clarify defintions of floating point exponent bounds (bug 31518)
- LoongArch: Update ulps
- LoongArch: Fix tst-gnu2-tls2 compiler error
- resolv: Make _res_opcodes a compat symbol [BZ #31764]
- i386: Don't define stpncpy alias when used in IFUNC [BZ #31768]
- powerpc: Update ulps
- arm: Update ulps
- aarch64: Update ulps
- math: Add more details to the test driver output.
- Implement C23 log2p1
- Update syscall lists for Linux 6.9
- Rename procutils_read_file to __libc_procutils_read_file [BZ #31755]
- nearbyint: Don't define alias when used in IFUNC [BZ #31759]
- Pass -nostdlib -nostartfiles together with -r [BZ #31753]

* Wed May 22 2024 Florian Weimer <fweimer@redhat.com> - 2.39.9000-23
- Use release instead of baserelease for glibc32 conflict

* Sun May 19 2024 Florian Weimer <fweimer@redhat.com> - 2.39.9000-22
- Add Conflicts:/Obsoletes: for glibc32 to glibc.i686

* Sun May 19 2024 Florian Weimer <fweimer@redhat.com> - 2.39.9000-21
- Auto-sync with upstream branch master,
  commit 8d7b6b4cb27d4dec1dd5f7960298c1699275f962:
- socket: Use may_alias on sockaddr structs (bug 19622)
- Use a doubly-linked list for _IO_list_all (bug 27777)
- ﻿powerpc64: Fix by using the configure value $libc_cv_cc_submachine [BZ #31629]
- aarch64/fpu: Add vector variants of cbrt
- aarch64/fpu: Add vector variants of hypot
- Use Linux 6.9 in build-many-glibcs.py
- localedata: Fix several issues with the set of characters considered 0-width [BZ #31370]
- math: Add GLIBC_TEST_LIBM_VERBOSE environment variable support.
- malloc: Improve aligned_alloc and calloc test coverage.
- Unify output from backtrace_symbols_fd with backtrace_symbols (bug 31730)
- manual: add dup3
- Force DT_RPATH for --enable-hardcoded-path-in-tests
- powerpc: Fix __fesetround_inline_nocheck on POWER9+ (BZ 31682)
- localedata: add mdf_RU locale
- elf: Make glibc.rtld.enable_secure ignore alias environment variables
- elf: Remove glibc.rtld.enable_secure check from parse_tunables_string
- elf: Only process multiple tunable once (BZ 31686)

* Wed May 15 2024 Arjun Shankar <arjun@redhat.com> - 2.39.9000-20
- i686: Move libc_malloc_debug.so.0 back to glibc
- Other arches: Move libmemusage.so to glibc-utils

* Tue May 14 2024 Arjun Shankar <arjun@redhat.com> - 2.39.9000-19
- Move libc_malloc_debug.so.0 from glibc to glibc-utils

* Mon May 06 2024 DJ Delorie <dj@redhat.com> - 2.39.9000-18
- Auto-sync with upstream branch master,
  commit 5f245f3bfbe61b2182964dafb94907e38284b806.
- Add crt1-2.0.o for glibc 2.0 compatibility tests
- ﻿powerpc: Optimized strncmp for power10
- build-many-glibcs.py: Add openrisc hard float glibc variant
- or1k: Add hard float support
- or1k: Add hard float libm-test-ulps
- nscd: Use time_t for return type of addgetnetgrentX
- Add a test to check for duplicate definitions in the static library
- i686: Fix multiple definitions of __memmove_chk and __memset_chk
- i586: Fix multiple definitions of __memcpy_chk and __mempcpy_chk
- nscd: Typo inside comment in netgroup cache

* Wed May 01 2024 Carlos O'Donell <carlos@redhat.com> - 2.39.9000-17
- Update License tag to match upstream.
- Auto-sync with upstream branch master,
  commit 91695ee4598b39d181ab8df579b888a8863c4cab:
- time: Allow later version licensing.
- hurd: Stop mapping AT_NO_AUTOMOUNT to O_NOTRANS
- libio: Sort test variables in Makefile
- AArch64: Remove unused defines of CPU names
- Make sure INSTALL is ASCII plaintext again
- x86: In ld.so, diagnose missing APX support in APX-only builds
- elf: Also compile dl-misc.os with $(rtld-early-cflags)
- CVE-2024-33601, CVE-2024-33602: nscd: netgroup: Use two buffers in addgetnetgrentX (bug 31680)
- CVE-2024-33600: nscd: Avoid null pointer crashes after notfound response (bug 31678)
- CVE-2024-33600: nscd: Do not send missing not-found response in addgetnetgrentX (bug 31678)
- CVE-2024-33599: nscd: Stack-based buffer overflow in netgroup cache (bug 31677)
- i386: ulp update for SSE2 --disable-multi-arch configurations

* Thu Apr 25 2024 Florian Weimer <fweimer@redhat.com> - 2.39.9000-16
- Enable CPU compatibility diagnostics in ld.so (RHEL-31738)

* Thu Apr 25 2024 Florian Weimer <fweimer@redhat.com> - 2.39.9000-15
- Auto-sync with upstream branch master,
  commit 41903cb6f460d62ba6dd2f4883116e2a624ee6f8:
- GLIBC-SA-2024-0004: add commit for 2.31 branch
- benchtests: Add difficult strstr needle for bruteforce algorithms
- x86: Define MINIMUM_X86_ISA_LEVEL in config.h [BZ #31676]
- LoongArch: Add glibc.cpu.hwcap support.
- nptl: Fix tst-cancel30 on kernels without ppoll_time64 support

* Tue Apr 23 2024 Arjun Shankar <arjun@redhat.com> - 2.39.9000-14
- Drop glibc-rh827510.patch, fixed differently upstream.
- Auto-sync with upstream branch master,
  commit 16c8dfba14ff7596ad3aea941a240f8abcdc50e6:
- Revert "Allow glibc to be compiled without EXEC_PAGESIZE"
- locale: Handle loading a missing locale twice (Bug 14247)
- elf: Do not check for loader mmap on tst-decorate-maps (BZ 31553)
- Use --enable-obsolete in build-many-glibcs.py for nios2-linux-gnu
- login: Use unsigned 32-bit types for seconds-since-epoch
- login: structs utmp, utmpx, lastlog _TIME_BITS independence (bug 30701)
- login: Check default sizes of structs utmp, utmpx, lastlog
- benchtests: Add random() benchmark
- advisories: Add Reported-By
- Fix 'Reported-By' to use Camel Case for commit 6a98f4640ea453f
- Document CVE-2024-2961
- iconv: ISO-2022-CN-EXT: fix out-of-bound writes when writing escape sequence (CVE-2024-2961)
- elf/rtld: Count skipped environment variables for enable_secure

* Mon Apr 22 2024 Florian Weimer <fweimer@redhat.com> - 2.39.9000-13
- Build POWER10 multilib

* Sun Apr 14 2024 Florian Weimer <fweimer@redhat.com> - 2.39.9000-12
- Auto-sync with upstream branch master,
  commit 14e56bd4ce15ac2d1cc43f762eb2e6b83fec1afe:
- powerpc: Fix ld.so address determination for PCREL mode (bug 31640)
- Revert "x86_64: Suppress false positive valgrind error"
- wcsmbs: Ensure wcstr worst-case linear execution time (BZ 23865)
- wcsmbs: Add test-wcsstr
- posix: Sync tempname with gnulib
- socket: Add new test for connect
- libsupport: Add xgetpeername

* Tue Apr 09 2024 Patsy Griffin <patsy@redhat.com> - 2.39.9000-11
- Auto-sync with upstream branch master,
  commit 42e48e720c78ab75eb8def9e866da52b0ac278df.
- nptl: Add tst-pthread-key1-static for BZ #21777
- elf: Add ld.so test with non-existing program name
- elf: Check objname before calling fatal_error
- Use crtbeginT.o and crtend.o for non-PIE static executables
- aarch64: Enhanced CPU diagnostics for ld.so
- x86: Add generic CPUID data dumper to ld.so --list-diagnostics
- elf: Add CPU iteration support for future use in ld.so diagnostics
- timezone: sync to TZDB 2024a
- Fix bsearch, qsort doc to match POSIX better
- x86-64: Exclude FMA4 IFUNC functions for -mapxf
- Reinstate generic features-time64.h
- Cleanup __tls_get_addr on alpha/microblaze localplt.data
- arm: Remove ld.so __tls_get_addr plt usage
- aarch64: Remove ld.so __tls_get_addr plt usage
- math: x86 trunc traps when FE_INEXACT is enabled (BZ 31603)
- math: x86 floor traps when FE_INEXACT is enabled (BZ 31601)
- math: x86 ceill traps when FE_INEXACT is enabled (BZ 31600)
- aarch64/fpu: Add vector variants of erfc
- aarch64/fpu: Add vector variants of tanh
- aarch64/fpu: Add vector variants of sinh
- aarch64/fpu: Add vector variants of atanh
- aarch64/fpu: Add vector variants of asinh
- aarch64/fpu: Add vector variants of acosh
- aarch64/fpu: Add vector variants of cosh
- aarch64/fpu: Add vector variants of erf
- misc: Add support for Linux uio.h RWF_NOAPPEND flag
- manual: significand() uses FLT_RADIX, not 2
- manual: Clarify return value of cbrt(3)
- manual: floor(log2(fabs(x))) has rounding errors
- manual: logb(x) is floor(log2(fabs(x)))
- powerpc: Add missing arch flags on rounding ifunc variants
- math: Reformat Makefile.
- Always define __USE_TIME_BITS64 when 64 bit time_t is used
- benchtests: Improve benchtests for strstr
- x86_64: Remove avx512 strstr implementation
- signal: Avoid system signal disposition to interfere with tests

* Tue Mar 26 2024 DJ Delorie <dj@redhat.com> - 2.39.9000-10
- Auto-sync with upstream branch master,
  commit 96d1b9ac2321b565f340ba8f3674597141e3450d.
- RISC-V: Fix the static-PIE non-relocated object check
- htl: Implement some support for TLS_DTV_AT_TP
- htl: Respect GL(dl_stack_flags) when allocating stacks
- hurd: Use the RETURN_ADDRESS macro
- hurd: Disable Prefer_MAP_32BIT_EXEC on non-x86_64 for now
- Allow glibc to be compiled without EXEC_PAGESIZE
- hurd: Stop relying on VM_MAX_ADDRESS
- hurd: Move internal functions to internal header
- stdlib: Fix tst-makecontext2 log when swapcontext fails
- or1k: Add prctl wrapper to unwrap variadic args
- or1k: Only define fpu rouding and exceptions with hard-float
- or1k: Update libm test ulps
- AArch64: Check kernel version for SVE ifuncs

* Wed Mar 20 2024 Florian Weimer <fweimer@redhat.com> - 2.39.9000-9
- Drop glibc-rh2269799.patch, fixed differently upstream.
- Auto-sync with upstream branch master,
  commit 1ea051145612f199d8716ecdf78b084b00b5a727:
- ﻿powerpc: Placeholder and infrastructure/build support to add Power11 related changes.
- ﻿powerpc: Add HWCAP3/HWCAP4 data to TCB for Power Architecture.
- elf: Enable TLS descriptor tests on aarch64
- arm: Update _dl_tlsdesc_dynamic to preserve caller-saved registers (BZ 31372)
- Ignore undefined symbols for -mtls-dialect=gnu2
- Add tst-gnu2-tls2mod1 to test-internal-extras
- x86-64: Allocate state buffer space for RDI, RSI and RBX (#2269799)
- riscv: Update nofpu libm test ulps
- Add STATX_MNT_ID_UNIQUE from Linux 6.8 to bits/statx-generic.h
- linux: Use rseq area unconditionally in sched_getcpu (bug 31479)
- aarch64: fix check for SVE support in assembler
- Update kernel version to 6.8 in header constant tests
- Update syscall lists for Linux 6.8
- Use Linux 6.8 in build-many-glibcs.py
- powerpc: Remove power8 strcasestr optimization
- riscv: Fix alignment-ignorant memcpy implementation
- linux/sigsetops: fix type confusion (bug 31468)
- LoongArch: Correct {__ieee754, _}_scalb -> {__ieee754, _}_scalbf
- duplocale: protect use of global locale (bug 23970)

* Sat Mar 16 2024 Florian Weimer <fweimer@redhat.com> - 2.39.9000-8
- Global dynamic TLS access may clobber RBX (#2269799)

* Fri Mar 15 2024 Florian Weimer <fweimer@redhat.com> - 2.39.9000-7
- Do not generate ELF dependency information for glibc32

* Wed Mar 13 2024 Joseph Myers <josmyers@redhat.com> - 2.39.9000-6
- Build glibc32 binary package from glibc sources as part of x86_64 build,
  not from glibc32 SRPM that contains binaries from i686 RPM build.

* Mon Mar 04 2024 Patsy Griffin <patsy@redhat.com> - 2.39.9000-5
- Auto-sync with upstream branch master,
  commit b6e3898194bbae78910bbe9cd086937014961e45.
- x86-64: Simplify minimum ISA check ifdef conditional with if
- manual/tunables - Add entry for enable_secure tunable.
- NEWS: Move enable_secure_tunable from 2.39 to 2.40.
- riscv: Add and use alignment-ignorant memcpy
- riscv: Add ifunc helper method to hwprobe.h
- riscv: Enable multi-arg ifunc resolvers
- riscv: Add __riscv_hwprobe pointer to ifunc calls
- riscv: Add hwprobe vdso call support
- linux: Introduce INTERNAL_VSYSCALL
- riscv: Add Linux hwprobe syscall support
- rtld: Add glibc.rtld.enable_secure tunable.
- x86-64: Update _dl_tlsdesc_dynamic to preserve AMX registers
- x86_64: Suppress false positive valgrind error
- x86: Don't check XFD against /proc/cpuinfo
- x86-64: Don't use SSE resolvers for ISA level 3 or above
- x86: Update _dl_tlsdesc_dynamic to preserve caller-saved registers
- sysdeps/unix/sysv/linux/x86_64/Makefile: Add the end marker
- cdefs: Drop access attribute for _FORTIFY_SOURCE=3 (BZ #31383)
- s390: Improve static-pie configure tests
- x86: Change ENQCMD test to CHECK_FEATURE_PRESENT
- debug: Improve mqueue.h fortify warnings with clang
- debug: Improve fcntl.h fortify warnings with clang
- wcsmbs: Improve fortify with clang
- syslog: Improve fortify with clang
- socket: Improve fortify with clang
- unistd: Improve fortify with clang
- stdlib: Improve fortify with clang
- string: Improve fortify with clang
- libio: Improve fortify with clang
- cdefs.h: Add clang fortify directives
- Update SHARED-FILES and license for Unicode 15.1.0.
- aarch64/fpu: Sync libmvec routines from 2.39 and before with AOR
- S390: Do not clobber r7 in clone [BZ #31402]
- x86_64: Exclude SSE, AVX and FMA4 variants in libm multiarch
- hurd: Reformat Makefile.
- htl/tests: Reformat Makefile.
- htl: Reformat Makefile.
- hesiod: Reformat Makefile.
- gmon: Reformat Makefile.
- dlfcn: Reformat Makefile.
- dirent: Reformat Makefile.
- ctype: Reformat Makefile.
- csu: Reformat Makefile.
- conform: Reformat Makefile.
- Support compiling .S files with additional options
- x86-64: Save APX registers in ld.so trampoline
- benchtests: Add more benchtests for rounding functions.
- tests: gracefully handle AppArmor userns containment
- treewide: python-scripts: use `is None` for none-equality
- powerpc: Remove power7 strstr optimization
- arm: Use _dl_find_object on __gnu_Unwind_Find_exidx (BZ 31405)
- math: Update mips64 ulps

* Tue Feb 27 2024 Arjun Shankar <arjun@redhat.com> - 2.39.9000-4
- Analyse glibc-2.39 sources for license information
- Migrate License field to SPDX identifiers for
  https://docs.fedoraproject.org/en-US/legal/allowed-licenses/
  https://docs.fedoraproject.org/en-US/legal/update-existing-packages
  (#2222074)

* Thu Feb 22 2024 DJ Delorie <dj@redhat.com> - 2.39.9000-3
- Auto-sync with upstream branch master,
  commit b881f1efcd1b30c2afab3599b41ce9cd4864c823.
- elf: Add new LoongArch reloc types (110 to 126) into elf.h
- build-many-glibcs.py: Add s390 --disable-multi-arch / multi-arch configurations.
- sparc: Treat the version field in the FPU control word as reserved
- Implement setcontext/getcontext/makecontext/swapcontext for Hurd x86_64
- Use proc_getchildren_rusage when available in getrusage and times.
- Linux: Switch back to assembly syscall wrapper for prctl (bug 29770)
- i386: Use generic memrchr in libc (bug 31316)

* Thu Feb 15 2024 Carlos O'Donell <carlos@redhat.com> - 2.39.9000-1
- Auto-sync with upstream branch master,
  commit ef7f4b1fef67430a8f3cfc77fa6aada2add851d7:
- Apply the Makefile sorting fix
- sysdeps/x86_64/Makefile (tests): Add the end marker
- sort-makefile-lines.py: Allow '_' in name and "^# name"
- trivial doc fix: remove weird phrase "syscall takes zero to five arguments"
- mips: Use builtins for ffs and ffsll
- x86: Expand the comment on when REP STOSB is used on memset
- x86: Do not prefer ERMS for memset on Zen3+
- x86: Fix Zen3/Zen4 ERMS selection (BZ 30994)
- x86/cet: fix shadow stack test scripts
- test_printers_common.py: Remove invalid escape sequence
- elf: Remove attempt at env handling in elf/tst-rtld-list-diagnostics.py
- Add SOL_VSOCK from Linux 6.7 to bits/socket.h
- localedata: ssy_ER: Fix syntax error
- localedata: hr_HR: change currency to EUR/€
- Change lv_LV collation to agree with the recent change in CLDR
- Add new AArch64 HWCAP2 definitions from Linux 6.7 to bits/hwcap.h
- string: Add hidden builtin definition for __strcpy_chk.
- arm: Remove wrong ldr from _dl_start_user (BZ 31339)
- LoongArch: Use builtins for ffs and ffsll
- Remove sysdeps/ia64/math-use-builtins-ffs.h
- Fix stringop-overflow warning in tst-strlcat2.
- mips: FIx clone3 implementation (BZ 31325)
- stdlib: fix qsort example in manual
- soft-fp: Add brain format support
- Rename c2x / gnu2x tests to c23 / gnu23
- manual: Fix up stdbit.texi
- string: Use builtins for ffs and ffsll
- misc: tst-poll: Proper synchronize with child before sending the signal
- math: Remove bogus math implementations
- Refer to C23 in place of C2X in glibc
- elf: Remove _dl_sysdep_open_object hook function
- build-many-glibcs: relax version check to allow non-digit characters
- Use gcc __builtin_stdc_* builtins in stdbit.h if possible
- Open master branch for glibc 2.40 development

* Wed Feb  7 2024 Florian Weimer <fweimer@redhat.com> - 2.39-2
- Ignore symbolic links to . in sysroot construction

* Fri Feb 02 2024 Carlos O'Donell <carlos@redhat.com> - 2.39-1
- Switch to upstream 2.39 release,
  commit ef321e23c20eebc6d6fb4044425c00e6df27b05f
- Document CVE-2023-6246, CVE-2023-6779, and CVE-2023-6780
- Update advisory format and introduce some automation
- manual/io: Fix swapped reading and writing phrase.
- Fix typo
- S390: Fix building with --disable-mutli-arch [BZ #31196]
- NEWS: insert advisories and fixed bugs for 2.39
- contrib.texi: update
- INSTALL, install.texi: minor updates, regenerate
- libc.pot: regenerate
- version.h, include/features.h: Bump version to 2.39
- Create ChangeLog.old/ChangeLog.28

* Wed Jan 31 2024 Florian Weimer <fweimer@redhat.com> - 2.38.9000-39
- Add noarch sysroot subpackages

* Tue Jan 30 2024 Patsy Griffin <patsy@redhat.com> - 2.38.9000-38
- Auto-sync with upstream branch master,
  commit ddf542da94caf97ff43cc2875c88749880b7259b:
- syslog: Fix integer overflow in __vsyslog_internal (CVE-2023-6780)
- syslog: Fix heap buffer overflow in __vsyslog_internal (CVE-2023-6779)
- syslog: Fix heap buffer overflow in __vsyslog_internal (CVE-2023-6246)
- Use binutils 2.42 branch in build-many-glibcs.py
- elf: correct relocation statistics for !ELF_MACHINE_START_ADDRESS

* Mon Jan 29 2024 Arjun Shankar <arjun@redhat.com> - 2.38.9000-37
- Auto-sync with upstream branch master,
  commit ae49a7b29acc184b03c2a6bd6ac01b5e08efd54f:
- Relicense IBM portions of resolv/base64.c resolv/res_debug.c.
- localedata: Use consistent values for grouping and mon_grouping
- manual: fix order of arguments of memalign and aligned_alloc (Bug 27547)

* Thu Jan 25 2024 Jens Petersen <petersen@redhat.com> - 2.38.9000-36
- no longer supplement langpacks if all-langpacks installed

* Wed Jan 24 2024 Florian Weimer <fweimer@redhat.com> - 2.38.9000-35
- Add crh_RU, gbm_IN, ssy_ER locales.
- Auto-sync with upstream branch master,
  commit 486452affbac684db739b7fcca1e84e8a7ce33d1:
- manual, NEWS: Document malloc side effect of dynamic TLS changes
- NEWS: Update temporary files ignored by ldconfig
- po: Incorporate translations (sr)
- string: Disable stack protector for memset in early static initialization
- qsort: Fix a typo causing unnecessary malloc/free (BZ 31276)
- riscv: add support for static PIE
- localedata: renamed:    aa_ER@saaho -> ssy_ER
- Define ISO 639-3 "ssy" (Saho)
- localedata: add crh_RU, Crimean Tartar language in the Cyrillic script as used in Russia.
- localedata: tr_TR, ku_TR: Sync with CLDR: “Turkey” -> “Türkiye”
- localedata: miq_NI: Shorten month names in abmon
- Update kernel version to 6.7 in header constant tests
- localedata: add gbm_IN locale
- Define ISO 639-3 "gbm" (Garhwali)
- Update syscall lists for Linux 6.7
- stdlib: Remove unused is_aligned function from qsort.c

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.9000-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 DJ Delorie <dj@redhat.com> - 2.38.9000-33
- Auto-sync with upstream branch master,
  commit e2803cfd8bb00b54816d1a2c381d2cf82b136da6.
- NEWS: Mention PLT rewrite on x86-64
- stdlib: Verify heapsort for two-element cases
- stdlib: Fix heapsort for cases with exactly two elements
- localedata: anp_IN: Fix abbreviated month names

* Mon Jan 15 2024 DJ Delorie <dj@redhat.com> - 2.38.9000-32
- Auto-sync with upstream branch master,
  commit 709fbd3ec3595f2d1076b4fec09a739327459288.
- stdlib: Reinstate stable mergesort implementation on qsort
- x86-64: Check if mprotect works before rewriting PLT
- aarch64: Add NEWS entry about libmvec for 2.39

* Mon Jan 15 2024 Carlos O'Donell <carlos@redhat.com> - 2.38.9000-31
- Add new locales for kv_RU, su_ID, tok, and zgh_MA.
- Drop glibc-rh2255506.patch; fix applied upstream.
- Enable Intel CET only on x86_64.
- Auto-sync with upstream branch master,
  commit 064c708c78cc2a6b5802dce73108fc0c1c6bfc80:
- localedata/unicode-gen/utf8_gen.py: fix Hangul syllable name
- x86_64: Optimize ffsll function code size.
- localedata: Remove redundant comments
- RISC-V: Enable static-pie.
- linux: Fix fstat64 on alpha and sparc64
- math: remove exp10 wrappers
- Benchtests: Increase benchmark iterations
- debug/getwd_chk.c: warning should be emitted for the __getwd_chk symbol.
- Make __getrandom_nocancel set errno and add a _nostatus version
- x86-64/cet: Make CET feature check specific to Linux/x86
- Incorporate translations (zh_CN)
- Define ISO 639-3 "glk" (Gilaki)
- resolv: Fix endless loop in __res_context_query
- localedata: revert all the remaining locale sources to UTF-8
- localedata: am_ET ber_DZ en_GB en_PH en_US fil_PH kab_DZ om_ET om_KE ti_ET tl_PH: convert to UTF-8
- localedata: resolve cyclic dependencies
- localedata: kv_RU: convert to UTF-8
- localedata: add new locale kv_RU
- elf: Fix tst-nodeps2 test failure.
- localedata: Sort Makefile variables.
- locale: Sort Makefile variables.
- i386: Remove CET support bits
- x86-64/cet: Move check-cet.awk to x86_64
- x86-64/cet: Move dl-cet.[ch] to x86_64 directories
- x86: Move x86-64 shadow stack startup codes
- Fix deprecated utcnow() usage in build-many-glibcs.py
- Fix invalid escape sequence in build-many-glibcs.py
- math: Fix test-fenv.c feupdateenv tests
- Remove installed header rule on $(..)include/%.h
- i386: Fail if configured with --enable-cet
- i386: Remove CET support
- x86: Move CET infrastructure to x86_64
- localedata: su_ID: make lang_name agree with CLDR
- localedata: add new locale su_ID
- localedata: add new locale zgh_MA
- INSTALL: regenerate
- localedata: add tok/UTF-8 to SUPPORTED
- localedata: tok: add yY and nN to yesexpr and noexpr
- localedata: tok: convert to UTF-8
- localedata: add data for tok (Toki Pona)
- Remove ia64-linux-gnu
- localedata: dz_BT, bo_CN: convert to UTF-8
- localedata: dz_BT, bo_CN: Fix spelling of "phur bu" in both Tibetan and Dzongkha
- localedata: bo_CN: Fix spelling errors in Tibetan data
- localedata: bo_CN: Fix incomplete edit in Tibetan yesexpr
- localedata: dz_BT: Fix spelling errors in Dzongha data
- localedata: unicode-gen: Remove redundant \s* from regexp, fix comments
- localedata: convert the remaining *_RU locales to UTF-8
- Incorporate translations
- x32: Handle displacement overflow in PLT rewrite [BZ #31218]
- x86: Fixup some nits in longjmp asm implementation
- stdlib: Fix stdbit.h with -Wconversion for clang
- stdlib: Fix stdbit.h with -Wconversion for older gcc
- elf: Add ELF_DYNAMIC_AFTER_RELOC to rewrite PLT
- aarch64: Make cpu-features definitions not Linux-specific
- hurd: Initializy _dl_pagesize early in static builds
- hurd: Only init early static TLS if it's used to store stack or pointer guards
- hurd: Make init-first.c no longer x86-specific
- hurd: Drop x86-specific assembly from init-first.c
- hurd: Pass the data pointer to _hurd_stack_setup explicitly
- x86-64/cet: Check the restore token in longjmp
- localedata: ru_RU, ru_UA: convert to UTF-8
- localedata: es_??: convert to UTF-8
- localedata: miq_NI: convert to UTF-8
- i386: Ignore --enable-cet
- mach: Drop SNARF_ARGS macro
- mach: Drop some unnecessary vm_param.h includes
- hurd: Declare _hurd_intr_rpc_msg* with protected visibility
- hurd: Add some missing includes
- localedata: fy_DE: make this "Western Frisian" to agree with the language code "fy"
- localedata: fy_DE, fy_NL: convert to UTF-8
- localedata: ast_ES: convert to UTF-8
- localedata: ast_ES: Remove wrong copyright text
- localedata: de_{AT,BE,CH,IT,LU}: convert to UTF-8
- localedata: lv_LV, it_IT, it_CH: convert to UTF-8
- localedata: it_IT, lv_LV: currency symbol should follow the amount
- Implement C23 <stdbit.h>
- localedata: ms_MY should not use 12-hour format
- localedata: es_ES: convert to UTF-8
- localedata: es_ES: Add am_pm strings
- aarch64: Add longjmp test for SME
- aarch64: Add setcontext support for SME
- aarch64: Add longjmp support for SME
- aarch64: Add SME runtime support
- localedata: convert uz_UZ and uz_UZ@cyrillic to UTF-8
- localedata: uz_UZ and uz_UZ@cyrillic: Fix decimal point and thousands separator
- libio: Check remaining buffer size in _IO_wdo_write (bug 31183)
- getaddrinfo: translate ENOMEM to EAI_MEMORY (bug 31163)
- string: Add additional output in test-strchr failure
- Add a setjmp/longjmp test between user contexts
- x86/cet: Add -fcf-protection=none before -fcf-protection=branch
- Regenerate libc.pot
- Omit regex.c pragmas no longer needed
- Update copyright dates not handled by scripts/update-copyrights
- Update copyright in generated files by running "make"
- Update copyright dates with scripts/update-copyrights
- x86/cet: Run some CET tests with shadow stack
- x86/cet: Don't set CET active by default
- x86/cet: Check feature_1 in TCB for active IBT and SHSTK
- x86/cet: Enable shadow stack during startup
- elf: Always provide _dl_get_dl_main_map in libc.a
- x86/cet: Sync with Linux kernel 6.6 shadow stack interface
- RISC-V: Add support for dl_runtime_profile (BZ #31151)
- debug: Add fortify wprintf tests
- debug: Add fortify syslog tests
- debug: Add fortify dprintf tests
- debug: Increase tst-fortify checks for compiler without __va_arg_pack support
- debug: Adapt fortify tests to libsupport
- localedata: yo_NT: remove redundant comments
- localedata: convert en_AU, en_NZ, mi_NZ, niu_NZ to UTF-8
- localedata: First day of the week in AU is Monday, LC_TIME in en_NZ is identical to LC_TIME in en_AU then
- localedata: convert yo_NG to UTF-8, check that language name in Yoruba agrees with CLDR
- x86-64: Fix the tcb field load for x32 [BZ #31185]
- x86-64: Fix the dtv field load for x32 [BZ #31184]

* Wed Jan  3 2024 Florian Weimer <fweimer@redhat.com> - 2.38.9000-30
- Infinite loop in res_mkquery with malformed domain name (#2255506)

* Fri Dec 22 2023 Florian Weimer <fweimer@redhat.com> - 2.38.9000-29
- Auto-sync with upstream branch master,
  commit 61bac1a9d2ab80ebcbc51484722e6ea43414bec7:
- nss: Remove unused allocation from get_nscd_addresses in getaddrinfo
- x86/cet: Don't disable CET if not single threaded
- x86: Modularize sysdeps/x86/dl-cet.c
- x86/cet: Update tst-cet-vfork-1
- elf: Add TLS modid reuse test for bug 29039
- aarch64: Add SIMD attributes to math functions with vector versions
- aarch64: Add half-width versions of AdvSIMD f32 libmvec routines
- Fix elf/tst-env-setuid[-static] if test needs to be rerun.
- Fix elf: Do not duplicate the GLIBC_TUNABLES string
- tst-setcontext10.c: Undef _FORTIFY_SOURCE
- Fix elf: Do not duplicate the GLIBC_TUNABLES string
- riscv: Fix feenvupdate with FE_DFL_ENV (BZ 31022)
- manual: Clarify undefined behavior of feenableexcept (BZ 31019)
- x86: Do not raises floating-point exception traps on fesetexceptflag (BZ 30990)
- i686: Do not raise exception traps on fesetexcept (BZ 30989)
- powerpc: Do not raise exception traps for fesetexcept/fesetexceptflag (BZ 30988)
- elf: Do not set invalid tunables values
- elf: Do not duplicate the GLIBC_TUNABLES string
- x86/cet: Check CPU_FEATURE_ACTIVE in permissive mode
- x86/cet: Check legacy shadow stack code in .init_array section
- x86/cet: Add tests for GLIBC_TUNABLES=glibc.cpu.hwcaps=-SHSTK
- x86/cet: Check CPU_FEATURE_ACTIVE when CET is disabled
- x86/cet: Check legacy shadow stack applications
- localedata: id_ID: change first weekday to Sunday
- s390: Set psw addr field in getcontext and friends.
- x86: Unifies 'strlen-evex' and 'strlen-evex512' implementations.
- x86/cet: Don't assume that SHSTK implies IBT
- id_ID: Update Time Locales
- Update code to handle the new ABI for sending inlined port rights.
- x86/cet: Check user_shstk in /proc/cpuinfo
- Add a test for setjmp/longjmp within user context
- Add a test for longjmp from user context
- powerpc: Add space for HWCAP3/HWCAP4 in the TCB for future Power.
- powerpc: Fix performance issues of strcmp power10
- localedata: Convert el_GR and el_CY locales to UTF-8
- localedata: el_GR: Greece now uses the 24h format for time
- powerpc : Add optimized memchr for POWER10
- intl: Treat C.UTF-8 locale like C locale, part 2 (BZ# 16621)
- resolv: Fix a few unaligned accesses to fields in HEADER
- x86: Check PT_GNU_PROPERTY early

* Wed Dec 13 2023 Carlos O'Donell <carlos@redhat.com> - 2.38.9000-28
- Depend only on RPM 4.14 features (RHEL-19045)

* Fri Dec 08 2023 Carlos O'Donell <carlos@redhat.com> - 2.38.9000-27
- Drop glibc-rh2248502.patch; fix applied upstream, and
- Auto-sync with upstream branch master,
  commit b3bee76c5f59498b9c189608f0a3132e2013fa1a:
- elf: Initialize GLRO(dl_lazy) before relocating libc in dynamic startup
- Move CVE information into advisories directory
- powerpc: Optimized strcmp for power10
- elf: Fix wrong break removal from 8ee878592c
- localedata: Convert day names in nn_NO locale to UTF-8
- localedata: Remove trailing whitespace in weekday names in nn_NO locale
- elf: Refactor process_envvars
- elf: Ignore LD_BIND_NOW and LD_BIND_NOT for setuid binaries
- elf: Ignore loader debug env vars for setuid
- Adapt the security policy for the security page
- aarch64: correct CFI in rawmemchr (bug 31113)
- math: Add new exp10 implementation
- aarch64: fix tested ifunc variants
- stdlib: Fix array bounds protection in insertion sort phase of qsort
- Revert "Update code to handle the new ABI for sending inlined port rights."
- Revert "hurd: Fix build"
- hurd: Fix build
- Update code to handle the new ABI for sending inlined port rights.
- hurd: [!__USE_MISC] Do not #undef BSD macros in ioctls
- linux: Make fdopendir fail with O_PATH (BZ 30373)
- Avoid padding in _init and _fini. [BZ #31042]
- aarch64: Improve special-case handling in AdvSIMD double-precision libmvec routines
- malloc: Improve MAP_HUGETLB with glibc.malloc.hugetlb=2
- elf: Add a way to check if tunable is set (BZ 27069)

* Tue Nov 28 2023 Arjun Shankar <arjun@redhat.com> - 2.38.9000-26
- Drop glibc-benchtests-aarch64.patch; fix applied upstream, and
- Auto-sync with upstream branch master,
  commit 9469261cf1924d350feeec64d2c80cafbbdcdd4d:
- x86: Only align destination to 1x VEC_SIZE in memset 4x loop
- elf: Fix TLS modid reuse generation assignment (BZ 29039)
- Add TCP_MD5SIG_FLAG_IFINDEX from Linux 5.6 to netinet/tcp.h.
- elf: Relocate libc.so early during startup and dlmopen (bug 31083)
- elf: Introduce the _dl_open_relocate_one_object function
- elf: In _dl_relocate_object, skip processing if object is relocated
- Remove __access_noerrno
- malloc: Use __get_nprocs on arena_get2 (BZ 30945)
- aarch64: Fix libmvec benchmarks

* Mon Nov 27 2023 Florian Weimer <fweimer@redhat.com> - 2.38.9000-25
- Fix qsort workaround (#2248502)

* Thu Nov 23 2023 Florian Weimer <fweimer@redhat.com> - 2.38.9000-24
- Restore qsort workaround for 389-ds-base.  (#2248502)

* Wed Nov 22 2023 Florian Weimer <fweimer@redhat.com> - 2.38.9000-23
- Apply glibc-benchtests-aarch64.patch to fix an aarch64 build failure.
- Drop glibc-rh2244688.patch revert.  Fix applied upstream.
- Drop glibc-rh2244992.patch, glibc-rh2248915.patch, glibc-rh2248502-3.patch.
  All applied upstream.
- Auto-sync with upstream branch master,
  commit 5d7f1bce7d8eea31f4baeb68bcc3124b35acc751:
- posix: Revert the removal of the crypt prototype from <unistd.h>
- elf: Add comments on how LD_AUDIT and LD_PRELOAD handle __libc_enable_secure
- elf: Ignore LD_LIBRARY_PATH and debug env var for setuid for static
- elf: Remove any_debug from dl_main_state
- elf: Remove LD_PROFILE for static binaries
- elf: Ignore LD_PROFILE for setuid binaries
- s390: Use dl-symbol-redir-ifunc.h on cpu-tunables
- x86: Use dl-symbol-redir-ifunc.h on cpu-tunables
- elf: Emit warning if tunable is ill-formatted
- elf: Fix _dl_debug_vdprintf to work before self-relocation
- elf: Do not parse ill-formatted strings
- elf: Do not process invalid tunable format
- elf: Add all malloc tunable to unsecvars
- elf: Ignore GLIBC_TUNABLES for setuid/setgid binaries
- elf: Add GLIBC_TUNABLES to unsecvars
- elf: Remove /etc/suid-debug support
- stdlib: The qsort implementation needs to use heapsort in more cases
- stdlib: Handle various corner cases in the fallback heapsort for qsort
- stdlib: Avoid another self-comparison in qsort
- hurd: fix restarting reauth_dtable on signal
- hurd: Prevent the final file_exec_paths call from signals
- manual: Fix termios.c example. (Bug 31078)
- aarch64: Add vector implementations of expm1 routines
- linux: Use fchmodat2 on fchmod for flags different than 0 (BZ 26401)
- intl: Add test case for bug 16621
- resolv: free only initialized items from gai pool
- ldconfig: Fixes for skipping temporary files.
- nptl: Link tst-execstack-threads-mod.so with -z execstack
- nptl: Rename tst-execstack to tst-execstack-threads
- localedata: Convert oc_FR locale to UTF-8
- localedata: Add information for Occitan
- elf: Fix force_first handling in dlclose (bug 30981)
- elf: Handle non-directory name in search path (BZ 31035)
- New Zealand locales (en_NZ & mi_NZ) first day of week should be Monday
- x86: Fix unchecked AVX512-VBMI2 usage in strrchr-evex-base.S
- posix: Check pidfd_spawn with tst-spawn7-pid
- y2038: Fix support for 64-bit time on legacy ABIs
- AArch64: Remove Falkor memcpy
- AArch64: Add memset_zva64
- AArch64: Cleanup emag memset
- test: Run the tst-tls-allocation-failure-static-patched with test-wrapper.
- aarch64: Add vector implementations of log1p routines
- aarch64: Add vector implementations of atan2 routines
- aarch64: Add vector implementations of atan routines
- aarch64: Add vector implementations of acos routines
- aarch64: Add vector implementations of asin routines

* Wed Nov 15 2023 Florian Weimer <fweimer@redhat.com> - 2.38.9000-22
- Work around another self-comparison application issue in qsort (#2248502)

* Sat Nov 11 2023 Florian Weimer <fweimer@redhat.com> - 2.38.9000-21
- Fix missing entries in /etc/ld.so.cache (#2248915)

* Sat Nov 11 2023 Florian Weimer <fweimer@redhat.com> - 2.38.9000-20
- Drop glibc-rh2248502-*.patch, workaround applied upstream
- Auto-sync with upstream branch master,
  commit d1dcb565a1fb5829f9476a1438c30eccc4027d04:
- Fix type typo in “String/Array Conventions” doc
- stdlib: Avoid element self-comparisons in qsort (#2248502)
- elf: Add glibc.mem.decorate_maps tunable
- linux: Decorate __libc_fatal error buffer
- assert: Decorate error message buffer
- malloc: Decorate malloc maps
- nptl: Decorate thread stack on pthread_create
- support: Add support_set_vma_name
- linux: Add PR_SET_VMA_ANON_NAME support

* Wed Nov  8 2023 Florian Weimer <fweimer@redhat.com> - 2.38.9000-19
- Fix force-first handling in dlclose, take two (#2244992, #2246048)

* Tue Nov 07 2023 Florian Weimer <fweimer@redhat.com> - 2.38.9000-18
- Revert back to old qsort/qsort_r implementation (#2248502)
- Adjust test build completion check to match new DejaGnu-style message.
- Auto-sync with upstream branch master,
  commit 5dd3bda59c2d9da138f0d98808d087cdb95cdc17:
- sysdeps: sem_open: Clear O_CREAT when semaphore file is expected to exist [BZ #30789]
- Add SEGV_CPERR from Linux 6.6 to bits/siginfo-consts.h
- linux: Sync Linux 6.6 elf.h
- linux: Add HWCAP2_HBC from Linux 6.6 to AArch64 bits/hwcap.h
- linux: Add FSCONFIG_CMD_CREATE_EXCL from Linux 6.6 to sys/mount.h
- linux: Add MMAP_ABOVE4G from Linux 6.6 to sys/mman.h
- Update kernel version to 6.6 in header constant tests
- Update syscall lists for Linux 6.6
- Format test results closer to what DejaGnu does
- AArch64: Cleanup ifuncs
- Use correct subdir when building tst-rfc3484* for mach and arm
- stdlib: Add more qsort{_r} coverage
- stdlib: qsort: Move some macros to inline function
- stdlib: Move insertion sort out qsort
- stdlib: Optimization qsort{_r} swap implementation
- string: Add internal memswap implementation
- crypt: Remove manul entry for --enable-crypt
- Use Linux 6.6 in build-many-glibcs.py
- crypt: Remove libcrypt support
- sparc: Remove optimize md5, sha256, and sha512
- build-many-glibcs: Fix traililing whitespace
- AArch64: Add support for MOPS memcpy/memmove/memset
- Move getnameinfo from 'inet' to 'nss'
- Move getaddrinfo from 'posix' into 'nss'
- Move 'services' routines from 'inet' into 'nss'
- Move 'rpc' routines from 'inet' into 'nss'
- Move 'protocols' routines from 'inet' into 'nss'
- Move 'networks' routines from 'inet' into 'nss'
- Move 'netgroup' routines from 'inet' into 'nss'
- Move 'hosts' routines from 'inet' into 'nss'
- Move 'ethers' routines from 'inet' into 'nss'
- Move 'aliases' routines from 'inet' into 'nss'
- Remove 'shadow' and merge into 'nss'
- Remove 'pwd' and merge into 'nss'
- Remove 'gshadow' and merge into 'nss'
- Remove 'grp' and merge into 'nss' and 'posix'
- malloc: Fix tst-tcfree3 build csky-linux-gnuabiv2 with fortify source
- test-container: disable ld.so system cache on DSO detection
- aarch64: Add vector implementations of exp10 routines
- aarch64: Add vector implementations of log10 routines
- aarch64: Add vector implementations of log2 routines
- aarch64: Add vector implementations of exp2 routines
- aarch64: Add vector implementations of tan routines
- elf: ldconfig should skip temporary files created by package managers
- tst-spawn-cgroup.c: Fix argument order of UNSUPPORTED message.
- Add NT_PPC_DEXCR and NT_PPC_HASHKEYR from Linux 6.5 to elf.h
- s390: Fix undefined behaviour in feenableexcept, fedisableexcept [BZ #30960]
- elf: Do not print the cache entry if --inhibit-cache is used

* Thu Oct 26 2023 Carlos O'Donell <carlos@redhat.com> - 2.38.9000-17
- Revert "Fix force-first handling in dlclose" (#2246048)

* Tue Oct 24 2023 Arjun Shankar <arjun@redhat.com> - 2.38.9000-16
- Provide template gai.conf in glibc-doc

* Thu Oct 19 2023 Florian Weimer <fweimer@redhat.com> - 2.38.9000-15
- Fix force-first handling in dlclose (#2244992)

* Wed Oct 18 2023 Florian Weimer <fweimer@redhat.com> - 2.38.9000-14
- Revert "x86: Prepare `strrchr-evex` and `strrchr-evex512` for AVX10" (#2244688)
- Auto-sync with upstream branch master,
  commit dd32e1db386c77c61850a7cbd0c126b7b3c63ece:
- Revert "elf: Always call destructors in reverse constructor order (bug 30785)"
- Revert "elf: Fix compile error with -DNDEBUG [BZ #18755]"
- Add strlcat/wcslcat testcase.
- Add strlcpy/wcslcpy testcase
- Add LE DSCP code point from RFC-8622.
- Add HWCAP2_MOPS from Linux 6.5 to AArch64 bits/hwcap.h
- Add SCM_SECURITY, SCM_PIDFD to bits/socket.h
- Add AT_HANDLE_FID from Linux 6.5 to bits/fcntl-linux.h
- Avoid maybe-uninitialized warning in __kernel_rem_pio2
- Fix WAIT_FOR_DEBUGGER for container tests.

* Thu Oct 12 2023 Florian Weimer <fweimer@redhat.com> - 2.38.9000-13
- Drop glibc-disable-werror-tst-realloc.patch, GCC was fixed long ago.
- Auto-sync with upstream branch master,
  commit 69239bd7a216007692470aa9d5f3658024638742:
- stdlib: fix grouping verification with multi-byte thousands separator (bug 30964)
- build-many-glibcs: Check for required system tools
- x86: Prepare `strrchr-evex` and `strrchr-evex512` for AVX10
- aarch64: Optimise vecmath logs
- aarch64: Cosmetic change in SVE exp routines
- aarch64: Optimize SVE cos & cosf
- aarch64: Improve vecmath sin routines
- nss: Get rid of alloca usage in makedb's write_output.
- debug: Add regression tests for BZ 30932
- Fix FORTIFY_SOURCE false positive
- nss: Rearrange and sort Makefile variables
- inet: Rearrange and sort Makefile variables
- Fix off-by-one OOB write in iconv/tst-iconv-mt

* Tue Oct 03 2023 Arjun Shankar <arjun@redhat.com> - 2.38.9000-12
- Auto-sync with upstream branch master,
  1056e5b4c3f2d90ed2b4a55f96add28da2f4c8fa:
- tunables: Terminate if end of input is reached (CVE-2023-4911)
- Propagate GLIBC_TUNABLES in setxid binaries

* Tue Oct 03 2023 Arjun Shankar <arjun@redhat.com> - 2.38.9000-11
- Auto-sync with upstream branch master,
  9e4e896f0f5a19a16c1a77567463b013a0f4952d:
- Linux: add ST_NOSYMFOLLOW
- resolve: Remove __res_context_query alloca usage
- mips: dl-machine-reject-phdr: Get rid of alloca.
- x86: Add support for AVX10 preset and vec size in cpu-features
- resolv: Fix a comment typo in __resolv_conf_load
- Remove unused -DRESOLVER getaddrinfo build flag
- C2x scanf %wN, %wfN support
- test-container: Use nftw instead of rm -rf

* Thu Sep 28 2023 Patsy Griffin <patsy@redhat.com> - 2.38.9000-10
- Auto-sync with upstream branch master,
  commit 29d4591b07a4da53320e949557c6946c62c26bde.
- hurd: Drop REG_GSFS and REG_ESDS from x86_64's ucontext
- elf: Fix compile error with -DNDEBUG [BZ #18755]
- MIPS: Add relocation types
- MIPS: Add new section type SHT_MIPS_ABIFLAGS
- MIPS: Add ELF file header flags
- fegetenv_and_set_rn now uses the builtins provided by GCC.
- io: Do not implement fstat with fstatat
- libio: Add nonnull attribute for most FILE * arguments in stdio.h
- AArch64: Remove -0.0 check from vector sin
- Document CVE-2023-4806 and CVE-2023-5156 in NEWS
- elf: Add dummy declaration of _dl_audit_objclose for !SHARED
- Fix leak in getaddrinfo introduced by the fix for CVE-2023-4806 [BZ #30843]
- elf: dl-lookup: Remove unused alloca.h include
- Remove unused localedata/th_TH.in
- Adapt collation in th_TH locale to use the iso14651_t1_common file and sync the collation with CLDR
- Revert "LoongArch: Add glibc.cpu.hwcap support."
- Update kernel version to 6.5 in header constant tests
- LoongArch: Add glibc.cpu.hwcap support.
- math: Add a no-mathvec flag for sin (-0.0)

* Mon Sep 18 2023 Arjun Shankar <arjun@redhat.com> - 2.38.9000-9
- Auto-sync with upstream branch master,
  commit bb5bbc20702981c287aa3e44640e7d2f2b9a28cf:
- Update to Unicode 15.1.0 [BZ #30854]
- localedata/unicode-gen/utf8_gen.py: adapt regexp to get relevant lines from EastAsianWidth.txt
- Fix regexp syntax warnings in localedata/unicode-gen/ctype_compatibility.py
- getaddrinfo: Fix use after free in getcanonname (CVE-2023-4806)
- LoongArch: Change to put magic number to .rodata section
- LoongArch: Add ifunc support for strrchr{aligned, lsx, lasx}
- LoongArch: Add ifunc support for strcpy, stpcpy{aligned, unaligned, lsx, lasx}
- LoongArch: Replace deprecated $v0 with $a0 to eliminate 'as' Warnings.
- LoongArch: Add lasx/lsx support for _dl_runtime_profile.
- Add MOVE_MOUNT_BENEATH from Linux 6.5 to sys/mount.h
- CVE-2023-4527: Stack read overflow with large TCP responses in no-aaaa mode
- resolv: Fix some unaligned accesses in resolver [BZ #30750]
- Update syscall lists for Linux 6.5

* Mon Sep 11 2023 Patsy Griffin <patsy@redhat.com> - 2.38.9000-8
- Auto-sync with upstream branch master,
  commit 073edbdfabaad4786e974a451efe4b6b3f7a5a61.
- ia64: Work around miscompilation and fix build on ia64's gcc-10 and later
- stdio: Remove __libc_message alloca usage
- htl: avoid exposing the vm_region symbol
- libio: Fix oversized __io_vtables
- Use Linux 6.5 in build-many-glibcs.py
- elf: Remove unused l_text_end field from struct link_map

* Fri Sep 08 2023 Florian Weimer <fweimer@redhat.com> - 2.38.9000-7
- Auto-sync with upstream branch master,
  commit 6985865bc3ad5b23147ee73466583dd7fdf65892:
- elf: Always call destructors in reverse constructor order (bug 30785)
- io: Fix record locking contants for powerpc64 with __USE_FILE_OFFSET64
- manual: Fix ld.so diagnostics menu/section structure
- getaddrinfo: Get rid of alloca
- riscv: Add support for XTheadBb in string-fz[a,i].h
- getcanonname: Fix a typo
- linux: Add pidfd_getpid
- posix: Add pidfd_spawn and pidfd_spawnp (BZ 30349)
- linux: Add posix_spawnattr_{get, set}cgroup_np (BZ 26371)
- linux: Define __ASSUME_CLONE3 to 0 for alpha, ia64, nios2, sh, and sparc
- __call_tls_dtors: Use call_function_static_weak
- intl: Treat C.UTF-8 locale like C locale (BZ# 16621)
- htl: Fix stack information for main thread
- htl: thread_local destructors support
- elf: Fix slow tls access after dlopen [BZ #19924]
- x86: Check the lower byte of EAX of CPUID leaf 2 [BZ #30643]

* Tue Aug 29 2023 DJ Delorie <dj@redhat.com> - 2.38.9000-6
- Auto-sync with upstream branch master,
  commit e1d3312015e8f70344620375aedf91afe7e7e7a4.
- add GB18030-2022 charmap and test the entire GB18030 charmap [BZ #30243]
- Use GMP 6.3.0, MPFR 4.2.1 in build-many-glibcs.py
- localedata: Translit common emojis to smileys [BZ #30649]
- nscd: Skip unusable entries in first pass in prune_cache (bug 30800)
- LoongArch: Change loongarch to LoongArch in comments
- LoongArch: Add ifunc support for memcmp{aligned, lsx, lasx}
- LoongArch: Add ifunc support for memset{aligned, unaligned, lsx, lasx}
- LoongArch: Add ifunc support for memrchr{lsx, lasx}
- LoongArch: Add ifunc support for memchr{aligned, lsx, lasx}
- LoongArch: Add ifunc support for rawmemchr{aligned, lsx, lasx}
- LoongArch: Micro-optimize LD_PCREL
- LoongArch: Remove support code for old linker in start.S
- LoongArch: Simplify the autoconf check for static PIE
- Add F_SEAL_EXEC from Linux 6.3 to bits/fcntl-linux.h.
- argp-parse: Get rid of alloca
- gencat: Get rid of alloca.
- m68k: Use M68K_SCALE_AVAILABLE on __mpn_lshift and __mpn_rshift
- m68k: Fix build with -mcpu=68040 or higher (BZ 30740)
- elf: Check that --list-diagnostics output has the expected syntax
- manual: Document ld.so --list-diagnostics output
- manual/jobs.texi: Add missing @item EPERM for getpgid
- LoongArch: Add ifunc support for strncmp{aligned, lsx}
- LoongArch: Add ifunc support for strcmp{aligned, lsx}
- LoongArch: Add ifunc support for strnlen{aligned, lsx, lasx}
- htl: move pthread_attr_setdetachstate into libc
- htl: move pthread_attr_getdetachstate into libc
- htl: move pthread_attr_setschedpolicy into libc
- htl: move pthread_attr_getschedpolicy into libc
- htl: move pthread_attr_setinheritsched into libc
- htl: move pthread_attr_getinheritsched into libc
- htl: move pthread_attr_getschedparam into libc
- htl: move pthread_setschedparam into libc
- htl: move pthread_getschedparam into libc
- htl: move pthread_equal into libc
- Linux: Avoid conflicting types in ld.so --list-diagnostics

* Tue Aug 22 2023 Arjun Shankar <arjun@redhat.com> - 2.38.9000-5
- Auto-sync with upstream branch master,
  commit f6c8204fd7fabf0cf4162eaf10ccf23258e4d10e:
- elf: Do not run constructors for proxy objects
- x86_64: Add log1p with FMA
- Remove references to the defunct db2 subdir
- string: Fix tester build with fortify enable with gcc < 12
- s390x: Fix static PIE condition for toolchain bootstrapping.
- m68k: fix __mpn_lshift and __mpn_rshift for non-68020
- sysdeps: tst-bz21269: fix -Wreturn-type
- Loongarch: Add ifunc support for memcpy{aligned, unaligned, lsx, lasx} and memmove{aligned, unaligned, lsx, lasx}
- Loongarch: Add ifunc support for strchr{aligned, lsx, lasx} and strchrnul{aligned, lsx, lasx}
- sysdeps: tst-bz21269: handle ENOSYS & skip appropriately
- sysdeps: tst-bz21269: fix test parameter
- hurd: Fix strictness of <mach/thread_state.h>
- hurd: Add prototype for and thus fix _hurdsig_abort_rpcs call
- io/tst-statvfs: fix statfs().f_type comparison test on some arches
- fxprintf: Get rid of alloca

* Tue Aug 15 2023 Carlos O'Donell <carlos@redhat.com> - 2.38-4
- Collect dynamic loader diagnostics from the build system.

* Tue Aug 15 2023 Florian Weimer <fweimer@redhat.com> - 2.38-3
- Auto-sync with upstream branch master,
  commit d6fe19facc61caffb25383d9c25eff86a0e115c8:
- configure: Add -Wall again to the default CFLAGS
- malloc: Remove bin scanning from memalign (bug 30723)
- resolv/nss_dns/dns-host: Get rid of alloca.
- x86_64: Add expm1 with FMA
- elf: Add new LoongArch reloc types (101 to 108) into elf.h
- x86: Fix incorrect scope of setting `shared_per_thread` [BZ# 30745]
- x86_64: Add log2 with FMA
- malloc: Enable merging of remainders in memalign (bug 30723)
- nscd: Do not rebuild getaddrinfo (bug 30709)
- x86_64: Sort fpu/multiarch/Makefile
- i686: Fix build with --disable-multiarch
- x86_64: Fix build with --disable-multiarch (BZ 30721)
- Add PTRACE_SET_SYSCALL_USER_DISPATCH_CONFIG etc. from Linux 6.4 to sys/ptrace.h
- Add PACKET_VNET_HDR_SZ from Linux 6.4 to netpacket/packet.h
- linux: statvfs: allocate spare for f_type
- x86: Fix for cache computation on AMD legacy cpus.
- powerpc longjmp: Fix build after chk hidden builtin fix
- LoongArch: Fix static PIE condition for toolchain bootstrapping.
- chk: Add and fix hidden builtin definitions for *_chk
- tst-realpath-toolong: return "unsupported" when PATH_MAX is undefined
- tst-*glob*: Do not check d_name size
- iconv: restore verbosity with unrecognized encoding names (bug 30694)
- configure: Remove --enable-all-warnings option
- Add IP_PROTOCOL from Linux 6.4 to bits/in.h
- Update kernel version to 6.4 in header constant tests
- PowerPC: Influence cpu/arch hwcap features via GLIBC_TUNABLES
- vfprintf-internal: Get rid of alloca.
- stdlib: Improve tst-realpath compatibility with source fortification
- Open master branch for glibc 2.39 development

* Tue Aug  1 2023 Siddhesh Poyarekar <siddhesh@redhat.com> - 2.38-2
- Drop downstream glibc shadow stack userspace support patches.

* Tue Aug  1 2023 Florian Weimer <fweimer@redhat.com> - 2.38-1
- Switch to upstream 2.38 release
- <sys/platform/x86.h>: Add APX support
- translations: update cs, nl, vi
- string: Fix tester build with fortify enable with gcc 6
- linux: Fix i686 with gcc6
- i386: Remove memset_chk-nonshared.S
- i386: Fix build with --enable-fortify=3
- posix: Fix test-errno build with fortify enable
- powerpc: Fix powerpc64 strchrnul build with old gcc
- sunrpc: Fix netname build with older gcc
- malloc: Fix set-freeres.c with gcc 6
- nscd: cleanup obsolete _FORTIFY_SOURCE setting

* Mon Jul 31 2023 Patsy Griffin <patsy@redhat.com> - 2.37.9000-20
- Allow for the optional removal of tzdata.
- Rebuilt for https://fedoraproject.org/wiki/Changes/AllowRemovalOfTzdata 

* Tue Jul 25 2023 DJ Delorie <dj@redhat.com> - 2.37.9000-19
- Auto-sync with upstream branch master,
  commit 637aac2ae3980de31a6baab236a9255fe853cc76.
- Include sys/rseq.h in tst-rseq-disable.c
- string: Fix tester with fortify enabled
- string: Fix bug-strncat1 with fortify enabled
- nscd: Use errval, not errno to guide cache update (bug 30662)
- Restore lookup of IPv4 mapped addresses in files database (bug 25457)
- Revert "MIPS: Sync elf.h from binutils"
- riscv: Update rvd libm test ulps
- MIPS: Sync elf.h from binutils
- Merge translations (bg, hr, pl, sv)
- nptl: Unconditionally use a 32-byte rseq area
- hurd: Fix tst-openloc
- scripts: Fix fortify checks if compiler does not support _FORTIFY_SOURCE=3
- configure: Disable building libcrypt by default
- nptl: Make tst-tls3mod.so explicitly lazy
- make ‘struct pthread’ a complete type
- scripts: Add fortify checks on installed headers
- Update x86_64 libm-test-ulps (x32 ABI)
- Fix getting return address in elf/tst-audit28.c.
- [PATCH v1] x86: Use `3/4*sizeof(per-thread-L3)` as low bound for NT threshold.
- x86: Fix slight bug in `shared_per_thread` cache size calculation.
- Update i686 libm-test-ulps (again)
- Update i686 libm-test-ulps
- Merge translations (de, ro, uk, zh_TW)
- Regenerate libc.pot
- configure: Use autoconf 2.71
- Update sparc libm-test-ulps
- s390: Add the clone3 wrapper
- manual: Fix typos in struct dl_find_object
- sparc: Fix la_symbind for bind-now (BZ 23734)
- i386: make debug wrappers compatible with static PIE
- LoongArch: Fix soft-float bug about _dl_runtime_resolve{,lsx,lasx}

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.37.9000-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Arjun Shankar <arjun@redhat.com> - 2.37.9000-17
- Auto-sync with upstream branch master,
  commit 7f079fdc16e88ebb8020e17b2fd900e8924da29a:
- LoongArch: Add vector implementation for _dl_runtime_resolve.
- LoongArch: config: Added HAVE_LOONGARCH_VEC_ASM.
- sysdeps: Add missing hidden definitions for i386
- sysdeps/s390: Exclude fortified routines from being built with _FORTIFY_SOURCE
- Translations: Add new ro support and update others.
- elf: _dl_find_object may return 1 during early startup (bug 30515)
- LoongArch: config: Rewrite check on static PIE.
- Revert "hppa: Drop 16-byte pthread lock alignment"
- realloc: Limit chunk reuse to only growing requests [BZ #30579]
- vfscanf-internal: Remove potentially unbounded allocas

* Thu Jul 06 2023 Frédéric Bérat <fberat@redhat.com> - 2.37.9000-16
- Add "--enable-fortify-source" option to configure
- Auto-sync with upstream branch master,
  commit 5324d258427fd11ca0f4f595c94016e568b26d6b.
- fileops: Don't process ,ccs= as individual mode flags (BZ#18906)
- sysdeps/ieee754/ldbl-128ibm-compat: Fix warn unused result
- libio/bits/stdio2-decl.h: Avoid PLT entries with _FORTIFY_SOURCE
- libio/bits/stdio2.h: Clearly separate declaration from definitions
- misc/bits/syslog.h: Clearly separate declaration from definition
- misc/bits/select2.h: Clearly separate declaration from definitions
- unistd: Avoid PLT entries with _FORTIFY_SOURCE
- posix/bits/unistd.h: Clearly separate declaration from definitions
- wchar: Avoid PLT entries with _FORTIFY_SOURCE
- misc/sys/cdefs.h: Create FORTIFY redirects for internal calls
- stdio: Ensure *_chk routines have their hidden builtin definition available
- string: Ensure *_chk routines have their hidden builtin definition available
- sysdeps: Ensure ieee128*_chk routines to be properly named
- Exclude routines from fortification
- Allow glibc to be built with _FORTIFY_SOURCE
- manual: Update documentation of strerror and related functions
- manual: Enhance documentation of the <ctype.h> functions
- Always do locking when accessing streams (bug 15142, bug 14697)
- hurd: Implement MAP_EXCL
- hurd: Fix mapping at address 0 with MAP_FIXED
- hurd: Fix calling vm_deallocate (NULL)
- hurd: Map brk non-executable
- htl: Let Mach place thread stacks
- mach: strerror must not return NULL (bug 30555)
- hppa: xfail debug/tst-ssp-1 when have-ssp is yes (gcc-12 and later)
- support: Build with exceptions and asynchronous unwind tables [BZ #30587]
- hurd: Make getrandom return ENOSYS when /dev/random is not set up
- Stop applying a GCC-specific workaround on clang [BZ #30550]
- ld.so: Always use MAP_COPY to map the first segment [BZ #30452]
- setenv.c: Get rid of alloca.
- Add checks for wday, yday and new date formats
- aarch64: Add vector implementations of exp routines
- aarch64: Add vector implementations of log routines
- aarch64: Add vector implementations of sin routines
- aarch64: Add vector implementations of cos routines
- Switch to UTF-8 for INSTALL
- Make sure INSTALL is ASCII plaintext
- Update syscall lists for Linux 6.4

* Wed Jun 28 2023 Carlos O'Donell <carlos@redhat.com> - 2.37.9000-15
- Auto-sync with upstream branch master,
  commit d35fbd3e684e6bb5e5ec452ad8dac6ada8424bdd:
- linux: Return unsupported if procfs can not be mount on tst-ttyname-namespace
- linux: Split tst-ttyname
- Use Linux 6.4 in build-many-glibcs.py
- x86: Adjust Linux x32 dl-cache inclusion path
- elf: Update list of RISC-V relocations
- Fix tests-clean Makefile target (bug 30545)
- check_native: Get rid of alloca
- ifaddrs: Get rid of alloca
- x86: Make dl-cache.h and readelflib.c not Linux-specific
- elf: Port ldconfig away from stack-allocated paths
- Call "CST" a time zone abbreviation, not a name
- benchtests: fix warn unused result
- sysdeps/powerpc/fpu/tst-setcontext-fpscr.c: Fix warn unused result
- rt/tst-mqueue4.c: Fix wrong number of argument for mq_open
- debug/readlink{, at}_chk.c: Harmonize declaration and definition
- wcsmbs/bits/wchar2{, -decl}.h: Clearly separate declaration from definitions
- stdio-common: tests: Incorrect maxlen parameter for swprintf
- sysdeps/{i386, x86_64}/mempcpy_chk.S: fix linknamespace for __mempcpy_chk
- hurd: readv: Get rid of alloca
- hurd: writev: Add back cleanup handler
- Fix misspellings -- BZ 25337
- C2x scanf %b support
- C2x printf %wN, %wfN support (bug 24466)
- tests: replace system by xsystem
- tests: replace read by xread
- hurd: writev: Get rid of alloca
- grantpt: Get rid of alloca
- string: strerror must not return NULL (bug 30555)
- hurd: Add strlcpy, strlcat, wcslcpy, wcslcat to libc.abilist
- manual: Manual update for strlcat, strlcpy, wcslcat, wclscpy
- Add the wcslcpy, wcslcat functions
- Implement strlcpy and strlcat [BZ #178]
- tests: replace fgets by xfgets
- tests: replace fread by xfread
- posix: Add test case for gai_strerror()
- posix: Handle success in gai_strerror()
- LoongArch: Add support for dl_runtime_profile
- malloc: Decrease resource usage for malloc tests
- stdlib: Tune down fork arc4random tests
- tst-getdate: Improve testcase flexibility and add test.
- x86: Make the divisor in setting `non_temporal_threshold` cpu specific
- x86: Refactor Intel `init_cpu_features`
- x86: Increase `non_temporal_threshold` to roughly `sizeof_L3 / 4`
- Remove unused DATEMSK file for tst-getdate
- resolv_conf: release lock on allocation failure (bug 30527)

* Thu Jun 08 2023 Siddhesh Poyarekar <siddhesh@redhat.com> - 2.37.9000-14
- Shadow stack userspace support, downstream only and disabled by default.

* Wed Jun 07 2023 Arjun Shankar <arjun@redhat.com> - 2.37.9000-13
- Auto-sync with upstream branch master,
  commit 85e6d8b4175fcb195011a0a1bad37d6f3b2355db:
- time: Fix use-after-free in getdate
- Move {read,write}_all functions to a dedicated header
- tests: Replace various function calls with their x variant
- tests: fix warn unused result on asprintf calls
- pthreads: Use _exit to terminate the tst-stdio1 test
- support: Add delayed__exit (with two underscores)

* Mon Jun 05 2023 Arjun Shankar <arjun@redhat.com> - 2.37.9000-12
- Auto-sync with upstream branch master,
  commit e3622a8f391deea3b75a577dce70d023dfa3f1c7.
- time: Also check for EPERM while trying to clock_settime
- linux: Fail as unsupported if personality call is filtered
- Remove MAP_VARIABLE from hppa bits/mman.h
- hurd: Fix x86_64 sigreturn restoring bogus reply_port
- Add lint-makefiles Makefile linting test.
- elf: Sort Makefile variables.
- Fix a few more typos I missed in previous round -- BZ 25337
- Fix all the remaining misspellings -- BZ 25337
- Use __nonnull for the epoll_wait(2) family of syscalls
- Fix invalid use of NULL in epoll_pwait2(2) test
- getipv4sourcefilter: Get rid of alloca
- getsourcefilter: Get rid of alloca.
- tests: fix warn unused results
- nptl_db/thread_dbP.h: fix warn unused result
- malloc/{memusage.c, memusagestat.c}: fix warn unused result
- catgets/gencat.c: fix warn unused result
- tests: replace ftruncate by xftruncate
- tests: replace write by xwrite
- x86-64: Use YMM registers in memcmpeq-evex.S

* Thu Jun 01 2023 Patsy Griffin <patsy@redhat.com> - 2.37.9000-11
- Auto-sync with upstream branch master,
  commit 6286cca2cb8389dcffec39238a8bf15ffea96396.
- support: Don't fail on fchown when spawning sgid processes
- io: Fix F_GETLK, F_SETLK, and F_SETLKW for powerpc64
- elf: Remove spurios SHARED conditional from elf/rtld.c
- Fix misspellings in sysdeps/ -- BZ 25337
- io: Fix record locking contants on 32 bit arch with 64 bit default time_t (BZ#30477)
- io: Re-flow and sort multiline Makefile definitions
- elf: Make more functions available for binding during dlclose (bug 30425)
- LoongArch: Fix inconsistency in SHMLBA macro values between glibc and kernel
- Fix misspellings in elf/ -- BZ 25337
- riscv: Add the clone3 wrapper
- posix: Add error message for EAI_OVERFLOW
- setsourcefilter: Replace alloca with a scratch_buffer.
- time: strftime_l: Avoid an unbounded alloca.
- x86: Use 64MB as nt-store threshold if no cacheinfo [BZ #30429]
- hurd: Fix setting up signal thread stack alignment
- mach: Fix startup with stack protector
- Fix misspellings in manual/ -- BZ 25337
- Fix misspellings in iconv/ and iconvdata/ -- BZ 25337
- Add MFD_NOEXEC_SEAL, MFD_EXEC from Linux 6.3 to bits/mman-shared.h
- Add IP_LOCAL_PORT_RANGE from Linux 6.3 to bits/in.h
- Add AT_RSEQ_* from Linux 6.3 to elf.h
- setipv4sourcefilter: Avoid using alloca.
- wchar: Define va_list for POSIX (BZ #30035)
- elf: add test for dl-printf
- elf: fix handling of negative numbers in dl-printf
- elf: Update comment in open_path
- elf: Add test for locating libraries in root dir (bug 30435)
- io: Re-flow and sort multiline Makefile definitions
- Fix special case for C2x strtol binary constant handling (BZ# 30371)
- rtld: properly handle root directory in load path (bug 30435)
- sysdeps/pthread/eintr.c: fix warn unused result
- sunrpc/netname.c: fix warn unused result
- locale/programs/locarchive.c: fix warn unused result
- support: Reformat Makefile.
- Regenerate configure fragment -- BZ 25337.
- Fix misspellings in sysdeps/powerpc -- BZ 25337
- Fix misspellings in sysdeps/unix -- BZ 25337
- Fix misspellings in sysdeps/x86_64 -- BZ 25337.
- mach: Fix accessing mach_i386.h
- Fix misspellings in sysdeps/x86_64/fpu/multiarch -- BZ 25337.
- mach: Fix installing mach_i386.h
- hurd: Fix making ld.so run static binaries with retry
- Add voice-admit DSCP code point from RFC-5865
- mach: Fix mach_setup_thread_impl with NULL stack_base
- Remove last remnants of have-protected
- S390: Use compile-only instead of also link-tests in configure.
- Fix build for hurd/thread-self.c for i386.
- io: Fix a typo
- htl: Use __hurd_fail () instead of assigning errno
- hurd: Use __hurd_fail () instead of assigning errno
- powerpc:GCC(<10) doesn't allow -mlong-double-64 after -mabi=ieeelongdouble
- hurd: Fix using interposable hurd_thread_self
- hurd 64bit: Re-introduce gai_suspend symbol
- hurd: Fix __TIMESIZE on x86_64
- posix: Reformat Makefile.
- hurd: Fix expected c++ types
- catgets: Reformat Makefile.
- benchtests: Reformat Makefile.
- assert: Reformat Makefile.
- nptl: Reformat Makefile.
- wcsmbs: Reformat Makefile.
- misc: Reformat Makefile.
- stdio-common: Adjust tests in Makefile
- elf: Adjust tests in Makefile.
- scripts: sort-makefile-lines.py
- Add a SECURITY.md
- Add HWCAP2_SME* from Linux 6.3 to AArch64 bits/hwcap.h
- hurd: Also make it possible to call strlen very early
- hurd: Fix setting up pthreads
- hurd: Fix x86_64 _hurd_tls_fork
- hurd: Make sure to not use tcb->self
- hurd: Use __mach_setup_thread_call ()
- mach: Add __mach_setup_thread_call ()
- hurd: Use MACHINE_THREAD_STATE_SETUP_CALL
- mach: Define MACHINE_THREAD_STATE_SETUP_CALL
- Use TASK_THREAD_TIMES_INFO_COUNT when calling task_info with TASK_THREAD_TIMES_INFO
- argp: Reformat Makefile.
- stdlib: Avoid undefined behavior in stdlib/tst-labs
- stdlib: Use long long int in stdlib/tst-llabs
- Update kernel version to 6.3 in header constant tests
- i386: Use pthread_barrier for synchronization on tst-bz21269
- stdlib: Add testcases for llabs(). (BZ #30263)
- stdlib: Add testcases for labs(). (BZ #30263)
- stdlib: Add testcases for abs(). (BZ #30263)
- hurd: Fix computing user stack pointer
- hurd: Fix sc_i386_thread_state layout
- hurd: Align signal stack pointer after allocating stackframe
- hurd: Fix aligning signal stack pointer

* Tue May 16 2023 Carlos O'Donell <carlos@redhat.com> - 2.37.9000-10
- Auto-sync with upstream branch master,
  commit 40b68e8cc00ca40348bc084b651c0561d31feb46:
- wcsmbs: Reformat Makefile.
- linux: Reformat Makefile.
- stdlib: Reformat Makefile.
- stdio-common: Reformat Makefile.
- socket: Reformat Makefile.
- misc: Reformat Makefile.
- debug: Reformat Makefile.
- elf: Reformat Makefile.
- libio: Add __nonnull for FILE * arguments of fclose and freopen
- nss: Reconcile conditional declaration and use of `is_nscd'
- Update syscall lists for Linux 6.3
- hurd: rule out some mach headers when generating errno.h
- Stop checking if MiG supports retcode.
- Added Redirects to longdouble error functions [BZ #29033]
- nptl: Reformat Makefile.
- scripts: Add sort-makefile-lines.py to sort Makefile variables.
- dlopen: skip debugger notification for DSO loaded from sprof (bug 30258)

* Tue May 09 2023 Arjun Shankar <arjun@redhat.com> - 2.37.9000-9
- Auto-sync with upstream branch master,
  commit d1417176a35d27ffb8da0ffb1e33154163b6eeb2:
- aligned_alloc: conform to C17
- testsuite: stdlib/isomac.c: fix REQUIREMENTS
- manual: Remove unsupported line breaks in waiting-with-clock section
- Enable new device_open_new RPC in libmachuser.
- Revert "riscv: Resolve symbols directly for symbols with STO_RISCV_VARIANT_CC."
- Update hurd/hurdselect.c to be more portable.
- hurd: Fix ld.so name
- hurd: Add ioperm symbol on x86_64
- time: Remove alloca() from getdate
- aarch64: More configure checks for libmvec
- aarch64: SVE ACLE configure test cleanups
- hppa: Fix 'concurrency' typo in comment
- Update hurd/intr-msg.c to be more portable
- Update sysdeps/mach/hurd/ioctl.c to make it more portable
- aarch64: fix SVE ACLE check for bootstrap glibc builds
- Enable libmvec support for AArch64
- hurd: Enable x86_64 build script
- hurd 64bit: Make dev_t word type
- malloc: Really fix tst-memalign-3 link against threads
- malloc: Fix tst-memalign-3 link against threads
- Use GCC 13 branch, Linux 6.3 in build-many-glibcs.py
- Mark various cold functions as __COLD
- Fix regex type usage
- hurd 64bit: Fix struct msqid_ds and shmid_ds fields
- hurd 64bit: Fix ipc_perm fields types
- hurd 64bit: Fix flock fields types
- hurd 64bit: Add data for check-c++-types
- hurd 64bit: Fix pthread_t/thread_t type to long
- socket: Fix tst-cmsghdr-skeleton.c use of cmsg_len
- hurd 64bit: Add missing data file for check-localplt test
- hurd 64bit: Add missing libanl
- hurd: Also XFAIL missing SA_NOCLDWAIT on 64bit
- hurd: Fix tst-writev test
- nptl: move tst-x86-64-tls-1 to nptl-only tests
- hurd: Add expected abilist files for x86_64
- hurd: Replace reply port with a dead name on failed interruption
- Define __mig_strlen to support dynamically sized strings in hurd RPCs
- mach: Disable 32bit compatibility mode
- hurd: Make it possible to call memcpy very early
- hurd: Implement longjmp for x86_64
- hurd: Implement sigreturn for x86_64
- Make __mach_msg_destroy portable for x86_64
- hurd: Mark error functions as __COLD
- cdefs.h: Define __COLD
- hurd: Fix FS_RETRY_MAGICAL "machtype" handling
- hurd: Respect existing FD_CLOEXEC in S_msg_set_fd
- hurd: Don't leak the auth port in msg* RPCs
- hurd: Make _exit work during early boot-up
- hurd: Mark various conditions as unlikely
- hurd: Move libc_hidden_def's around
- hurd: Simplify _hurd_critical_section_lock a bit
- __check_pf: Add a cancellation cleanup handler [BZ #20975]
- Remap __GLIBC_FLT_EVAL_METHOD to 0 if __FLT_EVAL_METHOD__ is -1
- riscv: Resolve symbols directly for symbols with STO_RISCV_VARIANT_CC.
- elf.h: add PT_GNU_SFRAME
- Fix Hurd getcwd build with GCC >= 13
- Regenerate sysdeps/mach/hurd/bits/errno.h
- locale/programs/locarchive.c: Remove unnecessary check in add_locale_archive
- manual: document posix_openpt (bug 17010)
- if_index: Remove unneeded alloca.h include
- gethostid: Do not include alloca.h

* Tue Apr 25 2023 Patsy Griffin <patsy@redhat.com> - 2.37.9000-8
- Auto-sync with upstream branch master,
  commit 904b94c07af84b7e4c98de3bbb822ccffcaf8c40.
- socket: Add a test for MSG_CMSG_CLOEXEC
- hurd: Do not take any flag from the CMSG_DATA
- hurd: Implement MSG_CMSG_CLOEXEC
- hurd: Don't pass FD_CLOEXEC in CMSG_DATA
- hurd: Implement prefer_map_32bit_exec tunable
- hurd: Don't attempt to deallocate MACH_PORT_DEAD
- hurd: Only deallocate addrport when it's valid
- hurd: Implement MAP_32BIT
- Use O_CLOEXEC in more places (BZ #15722)
- misc: Convert daemon () to GNU coding style
- wcsmbs: Add wcsdup() tests. (BZ #30266)
- string: Add tests for strndup (BZ #30266)
- string: Add tests for strdup (BZ #30266)
- string: Allow use of test-string.h for non-ifunc implementations.
- hurd: Don't migrate reply port into __init1_tcbhead
- hurd: Make dl-sysdep's open () cope with O_IGNORE_CTTY
- Created tunable to force small pages on stack allocation.
- malloc: Add missing shared thread library flags
- linux: Re-flow and sort multiline Makefile definitions
- posix: Re-flow and sort multiline Makefile definitions

* Mon Apr 24 2023 Florian Weimer <fweimer@redhat.com> - 2.37.9000-7
- Explicitly provide ldconfig paths (#2188550)

* Thu Apr 20 2023 Florian Weimer <fweimer@redhat.com> - 2.37.9000-6
- Auto-sync with upstream branch master,
  commit 65cbd52174f5bc211dd655727c2239e25e55bfce:
- build-many-glibcs.py: --disable-gcov for gcc-first
- malloc: set NON_MAIN_ARENA flag for reclaimed memalign chunk (BZ #30101)
- rcmd.c: Fix indentation in last commit
- inet/rcmd.c: fix warn unused result
- wcsmbs: Re-flow and sort routines, tests variables in Makefile
- debug: Re-flow and sort routines variable in Makefile
- math: Improve fmod(f) performance
- Benchtests: Adjust timing
- malloc: Assure that THP mode read do write OOB end of stringt
- malloc: Assure that THP mode is always null terminated
- aio: Fix freeing memory
- elf: Stop including tls.h in ldsodefs.h
- manual: update AddressSanitizer discussion
- manual: document snprintf truncation better
- manual: improve string section wording
- manual: fix texinfo typo
- <stdio.h>: Make fopencookie, vasprintf, asprintf available by default
- <string.h>: Make strchrnul, strcasestr, memmem available by default
- <sys/platform/x86.h>: Add PREFETCHI support
- <sys/platform/x86.h>: Add AMX-COMPLEX support
- <sys/platform/x86.h>: Add AVX-NE-CONVERT support
- <sys/platform/x86.h>: Add AVX-VNNI-INT8 support
- <sys/platform/x86.h>: Add MSRLIST support
- <sys/platform/x86.h>: Add AVX-IFMA support
- <sys/platform/x86.h>: Add AMX-FP16 support
- <sys/platform/x86.h>: Add WRMSRNS support
- <sys/platform/x86.h>: Add ArchPerfmonExt support
- <sys/platform/x86.h>: Add CMPCCXADD support
- <sys/platform/x86.h>: Add LASS support
- <sys/platform/x86.h>: Add RAO-INT support
- <sys/platform/x86.h>: Add LBR support
- <sys/platform/x86.h>: Add RTM_FORCE_ABORT support
- <sys/platform/x86.h>: Add SGX-KEYS support
- <sys/platform/x86.h>: Add BUS_LOCK_DETECT support
- <sys/platform/x86.h>: Add LA57 support
- platform.texi: Move LAM after LAHF64_SAHF64
- <bits/platform/x86.h>: Rename to x86_cpu_INDEX_7_ECX_15
- hppa: Update struct __pthread_rwlock_arch_t comment.
- hppa: Revise  __TIMESIZE define to use __WORDSIZE
- libio: Remove unused pragma weak on vtable
- malloc: Only set pragma weak for rpc freemem if required
- compare_strings.py : Add --gmean flag
- x86/dl-cacheinfo: remove unsused parameter from handle_amd
- powerpc: Disable stack protector in early static initialization
- nptl: Fix tst-cancel30 on sparc64
- math: Remove the error handling wrapper from fmod and fmodf
- math: Improve fmodf
- math: Improve fmod
- benchtests: Add fmodf benchmark
- benchtests: Add fmod benchmark
- x86: Set FSGSBASE to active if enabled by kernel
- x86_64: Fix asm constraints in feraiseexcept (bug 30305)
- manual: Document __wur usage under _FORTIFY_SOURCE
- x86_64: Add rtld-stpncpy & rtld-strncpy
- stdio-common: Fix building when !IS_IN (libc)
- time: Fix strftime(3) API regarding nullability
- Update arm libm-tests-ulps
- getlogin_r: fix missing fallback if loginuid is unset (bug 30235)
- memalign: Support scanning for aligned chunks.
- malloc: Use C11 atomics on memusage
- Remove --enable-tunables configure option
- Remove --disable-experimental-malloc option

* Fri Mar 31 2023 Arjun Shankar <arjun@redhat.com> - 2.37.9000-5
- Apply glibc-disable-werror-tst-realloc.patch to disable spurious GCC
  warning; and
- Auto-sync with upstream branch master,
  commit 885d3cda907d0dee54b13cbbf61b040c9951d5a2:
- Allow building with --disable-nscd again
- system: Add "--" after "-c" for sh (BZ #28519)
- posix: Fix some crashes in wordexp [BZ #18096]
- LoongArch: ldconfig: Add comments for using EF_LARCH_OBJABI_V1
- elf: Take into account ${sysconfdir} in elf/tst-ldconfig-p.sh
- Fix tst-glibc-hwcaps-prepend-cache with custom configure prefix value
- Fix tst-ldconfig-ld_so_conf-update with custom configure prefix value
- support: introduce support_sysconfdir_prefix
- Remove set-hooks.h from generic includes
- Remove --with-default-link configure option
- libio: Remove the usage of __libc_IO_vtables
- libio: Do not autogenerate stdio_lim.h
- Move libc_freeres_ptrs and libc_subfreeres to hidden/weak functions
- benchtests: Move libmvec benchtest inputs to benchtests directory
- stdio-common: tests: don't double-define _FORTIFY_SOURCE
- LoongArch: ldconfig: Ignore EF_LARCH_OBJABI_V1 in shared objects
- _dl_map_object_from_fd: Remove unnecessary debugger notification in error path
- hppa: Drop 16-byte pthread lock alignment
- Minor: don't call _dl_debug_update (which can have side effects) inside assert
- x86: Don't check PREFETCHWT1 in tst-cpu-features-cpuinfo.c
- Declare wcstofN, wcstofNx for C2x
- Update printf %b/%B C2x support
- ARC: run child from the separate start block in __clone
- ARC: Add the clone3 wrapper

* Mon Mar 13 2023 Florian Weimer <fweimer@redhat.com> - 2.37.9000-4
- Auto-sync with upstream branch master,
  commit 90233f113cc941ef88ce03b7f73221a964dcaca8:
- LoongArch: Add get_rounding_mode.
- LoongArch: Add support for ldconfig.
- linux: fix ntp_gettime abi break (BZ# 30156)
- elf: Add missing dependency between resolvfail and testobj1.so
- elf: Add -z lazy to some more tests
- Benchtests: Remove simple_str(r)chr
- Benchtests: Remove simple_str(n)casecmp
- Benchtests: Remove simple_memcmp
- Benchtests: Remove simple_strcspn/strpbrk/strsep
- Benchtests: Remove memchr_strnlen
- Benchtests: Remove simple_mem(r)chr
- Benchtests: Remove simple_strcpy_chk
- Benchtests: Remove simple_str(n)cmp
- malloc: Fix transposed arguments in sysmalloc_mmap_fallback call
- rt: fix shm_open not set ENAMETOOLONG when name exceeds {_POSIX_PATH_MAX}
- posix: Ensure the initial signal disposition for tst-spawn7
- hurd: fix build of tst-system.c
- x86: Fix bug about glibc.cpu.hwcaps.
- posix: Fix system blocks SIGCHLD erroneously [BZ #30163]
- gshadow: Matching sgetsgent, sgetsgent_r ERANGE handling (bug 30151)

* Mon Mar 06 2023 DJ Delorie <dj@redhat.com> - 2.37.9000-3
- Auto-sync with upstream branch master,
  commit 8390014c2320f94ffd8a8f6088c10c1f64567954.
- Update kernel version to 6.2 in header constant tests
- arm: Remove __builtin_arm_uqsub8 usage on string-fza.h
- alpha: Remove strncmp optimization
- powerpc: Remove powerpc64 strncmp variants
- powerpc: Remove strncmp variants
- C2x scanf binary constant handling
- Fix stringop-overflow warning in test-strncat.
- nis: Fix stringop-truncation warning with -O3 in nis_local_host.
- support: use 64-bit time_t (bug 30111)
- LoongArch: Update libm-test-ulps.
- LoongArch: Further refine the condition to enable static PIE
- hurd: Fix some broken indentation
- hurd: Remove the ecx kludge

* Wed Mar 01 2023 Carlos O'Donell <carlos@redhat.com> - 2.37.9000-2
- Auto-sync with upstream branch master,
  commit 59a6d5e9477695c41d6feef7ef8636f8f744f3c5:
- Add AArch64 HWCAP2 values from Linux 6.2 to bits/hwcap.h
- crypt: Remove invalid end of page test badsalttest
- S390: Fix _FPU_SETCW/GETCW when compiling with Clang [BZ #30130]
- s390x: Regenerate ULPs.
- Add Arm HWCAP values from Linux 6.2 to bits/hwcap.h
- htl: Add pthreadtypes-arch.h for x86_64
- hurd: Implement TLS for x86_64
- htl: Make pthread_mutex_t pointer-aligned
- x86_64: Update libm test ulps
- localedata: de_DE should not use Fräulein
- LoongArch: Add math-barriers.h
- cdefs.h: fix "__clang_major" typo
- hppa: Drop old parisc-specific MADV_* constants
- hurd: Generalize init-first.c to support x86_64
- hurd: Simplify init-first.c further
- hurd: Mark some audit tests as unsupported
- htl: Mark select loop test as unsupported
- hurd: Mark RLIMIT_AS tests as unsupported
- aarch64: update libm test ulps
- powerpc:Regenerate ulps for hypot
- Update syscall lists for Linux 6.2
- tunables.texi: Change \code{1} to @code{1}
- x86-64: Add glibc.cpu.prefer_map_32bit_exec [BZ #28656]
- gmon: fix memory corruption issues [BZ# 30101]
- gmon: improve mcount overflow handling [BZ# 27576]
- gmon: Fix allocated buffer overflow (bug 29444)
- malloc: remove redundant check of unsorted bin corruption
- Use Linux 6.2 in build-many-glibcs.py
- Ignore MAP_VARIABLE in tst-mman-consts.py
- AArch64: Fix HP_TIMING_DIFF computation [BZ# 29329]

* Mon Feb 20 2023 Arjun Shankar <arjun@redhat.com> - 2.37.9000-1
- Drop glibc-printf-grouping-swbz30068.patch; fix applied upstream, and
- Auto-sync with upstream branch master,
  commit 8b014a1b1f7aee1e3348db108aeea396359d481e:
- s390: Fix build for -march=z13
- arm: Support gcc older than 10 for find_zero_all
- Linux: Remove generic Implies
- Linux: Remove unused generic Makefile
- Linux: Assume and consolidate getpeername wire-up syscall
- Linux: Assume and consolidate getsockname wire-up syscall
- Linux: Move wordsize-32 Version to default
- __glob64_time64: Fix typo for stub_warning call (BZ #30146)
- elf: Restore ldconfig libc6 implicit soname logic [BZ #30125]
- stdlib: Undo post review change to 16adc58e73f3 [BZ #27749]
- Define PC, SP and SYSRETURN for hurd x86_64
- mach: Use PAGE_SIZE
- hurd: Simplify init-first.c a bit
- hurd: Make timer_t pointer-sized
- hurd: Fix xattr function return type
- hurd: Use proper integer types
- hurd: Move thread state manipulation into _hurd_tls_new ()
- glob64_time64: Fix typo for stub_warning call (BZ #30146)
- Use uintptr_t instead of performing pointer subtraction with a null pointer
- ARC:fpu: add extra capability check before use of sqrt and fma builtins
- ARC: align child stack in clone
- string: Remove string_private.h
- iconv: Remove _STRING_ARCH_unaligned usage
- iconv: Remove _STRING_ARCH_unaligned usage for get/set macros
- resolv: Remove _STRING_ARCH_unaligned usage
- nscd: Remove _STRING_ARCH_unaligned usage
- stdlib: Simplify getenv
- crypto: Remove _STRING_ARCH_unaligned usage
- Fix ifunc-impl-list.c build for s390
- [hurd] Fix i686 build breakage caused by 4fedebc91108
- C2x strtol binary constant handling
- [hurd] Add MTU_DISCOVER values
- hurd: Fix unwinding over INTR_MSG_TRAP in shared too
- mach: undef ENTRY2
- hurd: i386 TLS tweaks
- stdio: Do not ignore posix_spawn error on popen (BZ #29016)
- update auto-libm-test-out-hypot
- added pair of inputs for hypotf in binary32
- Naming the parameter of dummy_sa_handler
- hurd: Fix tcflag_t and speed_t types on 64-bit
- htl: Remove ./sysdeps/htl/bits/types/struct___pthread_mutex.h
- hurd, htl: Add some x86_64-specific code
- Fix typos in comments
- htl: Generalize i386 pt-machdep.h to x86
- hurd: Set up the basic tree for x86_64-gnu
- mach: Look for mach_i386.defs on x86_64 too
- htl: Fix semaphore reference
- hurd: Fix xattr error value
- mach, hurd: Cast through uintptr_t
- hurd: Use mach_msg_type_number_t where appropriate
- hurd: Refactor readlinkat()
- Use __builtin_FILE instead of __FILE__ in assert in C++.
- hurd: Fix unwinding over INTR_MSG_TRAP
- powerpc64: Add the clone3 wrapper
- string: Disable stack protector in early static initialization
- string: Add libc_hidden_proto for memrchr
- string: Add libc_hidden_proto for strchrnul
- elf: Smoke-test ldconfig -p against system /etc/ld.so.cache
- NEWS: Document CVE-2023-25139.
- Use 64-bit time_t interfaces in strftime and strptime (bug 30053)
- C-SKY: Strip hard float abi from hard float feature.
- S390: Influence hwcaps/stfle via GLIBC_TUNABLES.
- string: Hook up the default implementation on test-strrchr
- string: Hook up the default implementation on test-memrchr
- string: Hook up the default implementation on test-memchr
- string: Hook up the default implementation on test-strcpy
- string: Hook up the default implementation on test-stpcpy
- string: Hook up the default implementation on test-strncmp
- string: Hook up the default implementation on test-strcmp
- string: Hook up the default implementation on test-strchr
- string: Hook up the default implementation on test-strnlen
- string: Hook up the default implementation on test-strlen
- riscv: Add string-fza.h and string-fzi.h
- sh: Add string-fzb.h
- powerpc: Add string-fza.h
- arm: Add string-fza.h
- alpha: Add string-fza, string-fzb.h, string-fzi.h, and string-shift.h
- hppa: Add string-fza.h, string-fzc.h, and string-fzi.h
- hppa: Add memcopy.h
- string: Improve generic strrchr with memrchr and strlen
- string: Improve generic memrchr
- string: Improve generic strnlen with memchr
- string: Improve generic memchr
- string: Improve generic strcpy
- string: Improve generic stpcpy
- string: Improve generic strncmp
- string: Improve generic strcmp
- string: Improve generic strchr
- string: Improve generic strchrnul
- string: Improve generic strlen
- Add string vectorized find and detection functions
- Parameterize OP_T_THRES from memcopy.h
- Parameterize op_t from memcopy.h
- Replace rawmemchr (s, '\0') with strchr
- AArch64: Improve SVE memcpy and memmove
- Account for grouping in printf width (bug 30068)
- Move RETURN_TO to x86/sysdep.h and implement x86_64 version.
- Remove pthread-pi-defines.sym
- stdlib: tests: don't double-define _FORTIFY_SOURCE
- LoongArch: Add new relocation types.
- Remove sysdeps/mach/i386/machine-sp.h
- cdefs: Limit definition of fortification macros
- hurd: Move some i386 bits to x86
- Remove support setting custom demuxers during signal handling.
- hurd: Implement SHM_ANON
- hurd: Implement O_TMPFILE
- hurd: Consolidate file_name_lookup implementation
- Linux: optimize clone3 internal usage
- aarch64: Add the clone3 wrapper
- linux: Add clone3 CLONE_CLEAR_SIGHAND optimization to posix_spawn
- Linux: Do not align the stack for __clone3
- linux: Extend internal clone3 documentation
- linux: Do not reset signal handler in posix_spawn if it is already SIG_DFL
- Open master branch for glibc 2.38 development

* Sat Feb 04 2023 Carlos O'Donell <carlos@redhat.com> - 2.37-1
- Drop already included glibc-dprintf-length.patch patch.
- Apply glibc-printf-grouping-swbz30068.patch to fix swbz#30068.
- Auto-sync with upstream branch release/2.37/master,
  commit a704fd9a133bfb10510e18702f48a6a9c88dbbd5:
- Create ChangeLog.old/ChangeLog.26. (tag: glibc-2.37)
- Prepare for glibc 2.37 release.
- x86: Fix strncat-avx2.S reading past length [BZ #30065]
- Update install.texi, and regenerate INSTALL.
- Update manual/contrib.texi.
- Update NEWS file with bug fixes.
- Regenerate configure.
- Update all PO files in preparation for release.
- doc: correct _FORTIFY_SOURCE doc in features.h
- libio: Update number of written bytes in dprintf implementation

* Tue Jan 31 2023 Florian Weimer <fweimer@redhat.com> - 2.36.9000-25
- Apply glibc-dprintf-length.patch to fix dprintf return value regression.
- Auto-sync with upstream branch master,
  commit 2f39e44a8417b4186a7f15bfeac5d0b557e63e03:
- Account for octal marker in %#o format (rhbz#2165869)
- Use binutils 2.40 branch in build-many-glibcs.py
- Use MPFR 4.2.0, MPC 1.3.1 in build-many-glibcs.py

* Wed Jan 25 2023 Florian Weimer <fweimer@redhat.com> - 2.36.9000-24
- Auto-sync with upstream branch master,
  commit 0d50f477f47ba637b54fb03ac48d769ec4543e8d:
- stdio-common: Handle -1 buffer size in __sprintf_chk & co (bug 30039)
- Document '%F' format specifier
- sparc (64bit): Regenerate ulps
- ia64: Regenerate ulps
- Update libc.pot for 2.37 release.
- x86: Cache computation for AMD architecture.
- manual: Fix typo
- Add STATX_DIOALIGN from Linux 6.1 to bits/statx-generic.h
- Add IPPROTO_L2TP from Linux 6.1 to netinet/in.h
- AArch64: Improve strrchr
- AArch64: Optimize strnlen
- AArch64: Optimize strlen
- AArch64: Optimize strcpy
- AArch64: Improve strchrnul
- AArch64: Optimize strchr
- AArch64: Improve strlen_asimd
- AArch64: Optimize memrchr
- AArch64: Optimize memchr

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.36.9000-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Florian Weimer <fweimer@redhat.com> - 2.36.9000-22
- Auto-sync with upstream branch master,
  commit 569cfcc6bf35c28112ca8d7112e9eb4a22bed5b8:
- hurd: Fix _NOFLSH value
- elf: Fix GL(dl_phdr) and GL(dl_phnum) for static builds [BZ #29864]
- string: Suppress -Wmaybe-unitialized for wordcopy [BZ #19444]
- scripts/build-many-glibcs.py: Remove unused RANLIB and STRIP option
- configure: Move nm, objdump, and readelf to LIBC_PROG_BINUTILS

* Wed Jan 11 2023 Patsy Griffin <patsy@redhat.com> - 2.36.9000-21
- Auto-sync with upstream branch master,
  commit 2d2d7e1a8f2e62b442ae8978f0a6c17f385575c4.
- configure: Allow user override LD, AR, OBJCOPY, and GPROF
- math: Suppress -O0 warnings for soft-fp fsqrt [BZ #19444]
- sunrpc: Suppress GCC -O1 warning on user2netname [BZ #19444]
- locale: Use correct buffer size for utf8_sequence_error [BZ #19444]
- Add HWCAP2_SVE_EBF16 from Linux 6.1 to AArch64 bits/hwcap.h
- Add _FORTIFY_SOURCE implementation documentation [BZ #28998]
- Update copyright dates not handled by scripts/update-copyrights
- Update copyright dates with scripts/update-copyrights
- Remove trailing whitespace in gmp.h
- Remove trailing whitespace
- C2x semantics for <tgmath.h>
- time: Set daylight to 1 for matching DST/offset change (bug 29951)
- Fix ldbl-128 built-in function use
- x86: Check minimum/maximum of non_temporal_threshold [BZ #29953]
- i686: Regenerate ulps

* Mon Jan 02 2023 Arjun Shankar <arjun@redhat.com> - 2.36.9000-20
- Drop glibc-rh2155825.patch; fix applied upstream, and
- Auto-sync with upstream branch master,
  commit 5f55b22f4b3ea14c777a60f239d25dc4555eb804:
- hurd getcwd: Fix memory leak on error
- hurd fcntl: Make LOCKED macro more robust
- hurd: Make dl-sysdep __sbrk check __vm_allocate call
- htl: Drop duplicate check in __pthread_stack_alloc
- hurd hurdstartup: Initialize remaining fields of hurd_startup_data
- hurd _S_msg_add_auth: Initialize new arrays to 0
- htl: Check error returned by __getrlimit
- getdelim: ensure error indicator is set on error (bug 29917)
- htl: Fix sem_wait race between read and gsync_wait
- Avoid use of atoi in malloc
- Linux: Pass size argument of epoll_create to the kernel
- Simplify scripts/cross-test-ssh.sh configuration.
- Define MADV_COLLAPSE from Linux 6.1
- powerpc64: Increase SIGSTKSZ and MINSIGSTKSZ
- Update all PO files in preparation for release.
- Update kernel version to 6.1 in header constant tests
- Update syscall lists for Linux 6.1
- libio: Convert __vswprintf_internal to buffers (bug 27857)
- libio: Convert __obstack_vprintf_internal to buffers (bug 27124)
- libio: Convert __vdprintf_internal to buffers
- libio: Convert __vasprintf_internal to buffers
- libio: Convert __vsprintf_internal to buffers
- stdio-common: Add lock optimization to vfprintf and vfwprintf
- stdio-common: Convert vfprintf and related functions to buffers
- stdio-common: Add __translated_number_width
- stdio-common: Add __printf_function_invoke
- stdio-common: Introduce buffers for implementing printf
- locale: Implement struct grouping_iterator
- Use Linux 6.1 in build-many-glibcs.py
- Avoid use of atoi in some places in libc

* Thu Dec 22 2022 Florian Weimer <fweimer@redhat.com> - 2.36.9000-19
- Fix epoll_create regression (#2155825)

* Mon Dec 19 2022 Florian Weimer <fweimer@redhat.com> - 2.36.9000-18
- Auto-sync with upstream branch master,
  commit c1c0dea38833751f36a145c322ce53c9a08332e1:
- Linux: Remove epoll_create, inotify_init from syscalls.list (#2154747)
- Linux: Reflow and sort some Makefile variables
- mach: Drop remnants of old_CFLAGS
- mach: Fix passing -ffreestanding when checking for gnumach headers
- Force use of -ffreestanding when checking for gnumach headers
- elf: Fix tst-relro-symbols.py argument passing
- x86: Prevent SIGSEGV in memcmp-sse2 when data is concurrently modified [BZ #29863]
- Allow _Qp_fgt in sparc64 localplt.data

* Mon Dec 12 2022 DJ Delorie <dj@redhat.com> - 2.36.9000-17
- Auto-sync with upstream branch master,
  commit 5dcd2d0ad02ff12c76355ef4f40947c1857ac482.
- stdlib: Move _IO_cleanup to call_function_static_weak
- elf: Do not assume symbol order on tst-audit25{a,b}
- time: Use 64 bit time on tzfile
- nscd: Use 64 bit time_t on libc nscd routines (BZ# 29402)
- nis: Build libnsl with 64 bit time_t
- realloc: Return unchanged if request is within usable size
- Linux: Consolidate typesizes.h
- Linux: Make generic fcntl.h the default one
- Linux: make generic xstatver.h the default one
- Linux: Remove generic sysdep
- Linux: Assume and consolidate shutdown wire-up syscall
- Linux: Assume and consolidate listen wire-up syscall
- Linux: Assume and consolidate socketpair wire-up syscall
- Linux: Assume and consolidate socket wire-up syscall
- Linux: Assume and consolidate bind wire-up syscall
- Linux: consolidate ____longjmp_chk
- Linux: consolidate sendfile implementation
- Linux: consolidate unlink implementation
- Linux: consolidate symlink implementation
- Linux: consolidate rmdir implementation
- Linux: consolidate readlink implementation
- Linux: consolidate mkdir implementation
- Linux: consolidate link implementation
- Linux: consolidate lchown implementation
- Linux: consolidate inotify_init implementation
- Lninux: consolidate epoll_create implementation
- Linux: consolidate dup2 implementation
- Linux: consolidate chown implementation
- Linux: consolidate chmod implementation
- linux: Consolidate dl-origin.c
- linux: Use long int for syscall return value
- LoongArch: Use medium cmodel build libc_nonshared.a.
- x86_64: State assembler is being tested on sysdeps/x86/configure
- configure: Remove AS check
- configure: Remove check if ld is GNU
- configure: Remove check if as is GNU
- configure: Move locale tools early

* Mon Dec 05 2022 Arjun Shankar <arjun@redhat.com> - 2.36.9000-16
- Auto-sync with upstream branch master,
  commit 8fb923ddc38dd5f4bfac4869d70fd80483fdb87a:
- hurd: Make getrandom cache the server port
- powerpc64: Remove old strncmp optimization
- x86-64 strncpy: Properly handle the length parameter [BZ# 29839]
- x86-64 strncat: Properly handle the length parameter [BZ# 24097]
- ARC: update definitions in elf/elf.h
- scripts: Add "|" operator support to glibcpp's parsing
- Apply asm redirections in syslog.h before first use [BZ #27087]
- LoongArch: Add support for ilogb[f]
- LoongArch: Add support for scalb[f]
- LoongArch: Add support for scalbn[f]
- LoongArch: Use __builtin_logb{,f} with GCC >= 13
- Use GCC builtins for logb functions if desired.
- LoongArch: Use __builtin_llrint{,f} with GCC >= 13
- Use GCC builtins for llrint functions if desired.
- LoongArch: Use __builtin_lrint{,f} with GCC >= 13
- Use GCC builtins for lrint functions if desired.
- LoongArch: Use __builtin_rint{,f} with GCC >= 13

* Mon Nov 28 2022 Florian Weimer <fweimer@redhat.com> - 2.36.9000-15
- Auto-sync with upstream branch master,
  commit f704192911c6c7b65a54beab3ab369fca7609a5d:
- x86/fpu: Factor out shared avx2/avx512 code in svml_{s|d}_wrapper_impl.h
- x86/fpu: Cleanup code in svml_{s|d}_wrapper_impl.h
- x86/fpu: Reformat svml_{s|d}_wrapper_impl.h
- x86/fpu: Fix misspelled evex512 section in variety of svml files
- x86/fpu: Add missing ISA sections to variety of svml files
- stdio-common: Add missing dependencies (bug 29780)
- i386: Avoid rely on linker optimization to avoid relocation
- elf: Fix rtld-audit trampoline for aarch64
- Define in_int32_t_range to check if the 64 bit time_t syscall should be used

* Mon Nov 14 2022 Arjun Shankar <arjun@redhat.com> - 2.36.9000-14
- Auto-sync with upstream branch master,
  commit 94628de77888c3292fc103840731ff85f283368e:
- elf/tst-tlsopt-powerpc fails when compiled with -mcpu=power10 (BZ# 29776)
- LoongArch: Hard Float Support for fmaximum_mag_num{f/ }, fminimum_mag_num{f/ }.
- LoongArch: Hard Float Support for fmaximum_mag{f/ }, fminimum_mag{f/ }.
- LoongArch: Hard Float Support for fmaxmag{f/ }, fminmag{f/ }.
- LoongArch: Hard Float Support for fmaximum_num{f/ }, fminimum_num{f/ }.
- LoongArch: Hard Float Support for fmaximum{f/ }, fminimum{f/ }.
- LoongArch: Hard Float Support for float-point classification functions.
- LoongArch: Use __builtin_{fma, fmaf} to implement function {fma, fmaf}.

* Thu Nov 10 2022 Florian Weimer <fweimer@redhat.com> - 2.36.9000-13
- Auto-sync with upstream branch master,
  commit 22a46dee24351fd5f4f188ad80554cad79c82524:
- Linux: Support __IPC_64 in sysvctl *ctl command arguments (bug 29771)
- riscv: Get level 3 cache's information
- debug: Fix typo in tests-unsupported rule
- iconvdata/tst-table-charmap.sh: remove handling of old, borrowed format
- Makerules: Generate shlib.lds with -fuse-ld=bfd
- x86: Add avx2 optimized functions for the wchar_t strcpy family
- x86: Add evex optimized functions for the wchar_t strcpy family
- x86: Optimize and shrink st{r|p}{n}{cat|cpy}-avx2 functions
- x86: Optimize and shrink st{r|p}{n}{cat|cpy}-evex functions
- benchtests: Make str{n}{cat|cpy} benchmarks output json
- x86: Use VMM API in memcmpeq-evex.S and minor changes
- x86: Use VMM API in memcmp-evex-movbe.S and minor changes
- string: Add len=0 to {w}memcmp{eq} tests and benchtests
- Linux: Add ppoll fortify symbol for 64 bit time_t (BZ# 29746)
- hurd: Add sigtimedwait and sigwaitinfo support

* Mon Nov 07 2022 DJ Delorie <dj@redhat.com> - 2.36.9000-12
- Auto-sync with upstream branch master,
  commit 8d291eabd541029d7ac705cc1ea112c58dfbb05f.
- Apply asm redirection in gmp.h before first use
- Rewrite find_cxx_header config configure.ac
- elf/tlsdeschtab.h: Add the Malloc return value check in _dl_make_tlsdesc_dynamic()
- elf: Disable some subtests of ifuncmain1, ifuncmain5 for !PIE
- posix: Make posix_spawn extensions available by default
- x86_64: Implement evex512 version of strrchr and wcsrchr
- elf: Introduce <dl-call_tls_init_tp.h> and call_tls_init_tp (bug 29249)
- LoongArch: Fix ABI related macros in elf.h to keep consistent with binutils[1].
- scripts/glibcelf.py: Properly report <elf.h> parsing failures
- elf: Rework exception handling in the dynamic loader [BZ #25486]
- linux: Drop useless include from fstatat.c
- Fix OOB read in stdlib thousand grouping parsing [BZ #29727]
- linux: Fix fstatat on MIPSn64 (BZ #29730)
- elf: Remove allocate use on _dl_debug_printf
- nptl: Fix pthread_create.c build with clang
- allocate_once: Apply asm redirection before first use
- alloc_buffer: Apply asm redirection before first use
- configure: Use -Wno-ignored-attributes if compiler warns about multiple aliases
- Disable use of -fsignaling-nans if compiler does not support it
- intl: Fix clang -Wunused-but-set-variable on plural.c
- Apply asm redirection in not-cancel before first use
- malloc: Use uintptr_t for pointer alignment
- Use uintptr_t in fts for pointer alignment
- Fix build with GCC 13 _FloatN, _FloatNx built-in functions
- elf: Build tst-relr-mod[34]a.so with $(LDFLAGS-rpath-ORIGIN)
- x86-64: Improve evex512 version of strlen functions
- Correctly determine libc.so 'OUTPUT_FORMAT' when cross-compiling.
- Remove unused scratch_buffer_dupfree
- Fix elf/tst-dlmopen-twice not to exhaust static TLS
- Use uintptr_t in string/tester for pointer alignment
- stdlib/strfrom: Add copysign to fix NAN issue on riscv (BZ #29501)
- Fix resource/bug-ulimit1 test
- Fix missing NUL terminator in stdio-common/scanf13 test
- Fix off-by-one OOB read in elf/tst-tls20
- elf: Fix alloca size in _dl_debug_vdprintf
- malloc: Use uintptr_t in alloc_buffer
- Fix invalid pointer dereference in wcpcpy_chk
- Fix invalid pointer dereference in wcscpy_chk
- aarch64: Fix the extension header write in getcontext and swapcontext
- aarch64: Don't build wordcopy
- scripts: Use bool in tunables initializer
- longlong.h: update from GCC for LoongArch clz/ctz support

* Thu Oct 27 2022 Patsy Griffin <patsy@redhat.com> - 2.36.9000-11
- Auto-sync with upstream branch master,
  commit 6f360366f7f76b158a0f4bf20d42f2854ad56264.
- elf: Introduce to _dl_call_fini
- ld.so: Export tls_init_tp_called as __rtld_tls_init_tp_called
- scripts/localplt.awk: Handle DT_JMPREL with empty PLT (for C-SKY)
- Remove lingering libSegfault Makefile entries
- aarch64: Use memcpy_simd as the default memcpy
- aarch64: Cleanup memset ifunc
- elf: Reinstate on DL_DEBUG_BINDINGS _dl_lookup_symbol_x
- x86_64: Implement evex512 version of strchrnul, strchr and wcschr
- linux: Fix generic struct_stat for 64 bit time (BZ# 29657)
- manual: Add missing % in int conversion list
- Avoid undefined behaviour in ibm128 implementation of llroundl (BZ #29488)
- Remove all assembly optimizations for htonl and htons
- Remove htonl.S for i386/x86_64
- Fix BZ #29463 in the ibm128 implementation of y1l too
- Add ADDRB from Linux 6.0 to bits/termios-c_cflag.h
- x86: Use `testb` for FSRM check in memmove-vec-unaligned-erms
- x86: Use `testb` for case-locale check in str{n}casecmp-sse42
- x86: Use `testb` for case-locale check in str{n}casecmp-sse2
- x86: Use `testb` for case-locale check in str{n}casecmp-avx2
- x86: Add support for VEC_SIZE == 64 in strcmp-evex.S impl
- x86: Remove AVX512-BVMI2 instruction from strrchr-evex.S
- sysdeps: arm: Fix preconfigure script for ARMv8/v9 targets [BZ #29698]
- nis: Fix nis_print_directory
- linux: Avoid shifting a negative signed on POSIX timer interface
- Bench: Improve benchtests for memchr, strchr, strnlen, strrchr
- x86: Optimize strrchr-evex.S and implement with VMM headers
- x86: Optimize memrchr-evex.S
- x86: Optimize strnlen-evex.S and implement with VMM headers
- x86: Shrink / minorly optimize strchr-evex and implement with VMM headers
- x86: Optimize memchr-evex.S and implement with VMM headers
- x86_64: Implement evex512 version of memchr, rawmemchr and wmemchr
- String: Improve test coverage for memchr
- Use PTR_MANGLE and PTR_DEMANGLE unconditionally in C sources
- Introduce <pointer_guard.h>, extracted from <sysdep.h>
- x86-64: Move LP_SIZE definition to its own header
- math: Fix asin and acos invalid exception with old gcc
- x86: Update strlen-evex-base to use new reg/vec macros.
- x86: Remove now unused vec header macros.
- x86: Update memset to use new VEC macros
- x86: Update memmove to use new VEC macros
- x86: Update memrchr to use new VEC macros
- x86: Update VEC macros to complete API for evex/evex512 impls
- elf: Do not completely clear reused namespace in dlmopen (bug 29600)
- malloc: Switch global_max_fast to uint8_t
- Add NT_S390_PV_CPU_DATA from Linux 6.0 to elf.h
- Add AArch64 HWCAP2_EBF16 from Linux 6.0 to bits/hwcap.h
- String: Improve test coverage for memchr
- elf: Remove -fno-tree-loop-distribute-patterns usage on dl-support
- socket: Use offsetof in SUN_LEN (bug 29578)
- Expose all MAP_ constants in <sys/mman.h> unconditionally (bug 29375)
- LoongArch: Fix the condition to use PC-relative addressing in start.S
- arm: Enable USE_ATOMIC_COMPILER_BUILTINS (BZ #24774)
- csu: Disable stack protector for static-reloc for static-pie
- NEWS: Fix grammar
- elf: Simplify output of hwcap subdirectories in ld.so help
- elf: Remove _dl_string_hwcap
- Add NEWS entry for legacy hwcaps removal
- elf: Remove hwcap and bits_hwcap fields from struct cache_entry
- elf: Remove hwcap parameter from add_to_cache signature
- elf: Remove legacy hwcaps support from ldconfig
- elf: Remove legacy hwcaps support from the dynamic loader
- x86_64: Remove platform directory library loading test
- Update to Unicode 15.0.0 [BZ #29604]
- Update kernel version to 6.0 in header constant tests
- x86: Fix -Os build (BZ #29576)
- sunrpc: Suppress GCC -Os warning on user2netname
- rt: Initialize mq_send input on tst-mqueue{5,6}
- posix: Suppress -Os may be used uninitialized warnings on regexec
- posix: Suppress -Os warnings on fnmatch
- locale: prevent maybe-uninitialized errors with -Os [BZ #19444]
- Regenerate sysdeps/mach/hurd/bits/errno.h
- Update syscall lists for Linux 6.0
- nscd: Drop local address tuple variable [BZ #29607]
- Use Linux 6.0 in build-many-glibcs.py
- x86-64: Require BMI1/BMI2 for AVX2 strrchr and wcsrchr implementations
- x86-64: Require BMI2 and LZCNT for AVX2 memrchr implementation
- x86-64: Require BMI2 for AVX2 (raw|w)memchr implementations
- x86-64: Require BMI2 for AVX2 wcs(n)cmp implementations
- x86-64: Require BMI2 for AVX2 strncmp implementation
- x86-64: Require BMI2 for AVX2 strcmp implementation
- x86-64: Require BMI2 for AVX2 str(n)casecmp implementations
- x86: include BMI1 and BMI2 in x86-64-v3 level
- x86: Cleanup pthread_spin_{try}lock.S
- Benchtests: Add bench for pthread_spin_{try}lock and mutex_trylock

* Mon Oct 17 2022 Carlos O'Donell <carlos@redhat.com> - 2.36.9000-10
- Enable ELF DT_HASH for shared objects and the dynamic loader (#2129358)

* Mon Oct 03 2022 DJ Delorie <dj@redhat.com> - 2.36.9000-9
- Auto-sync with upstream branch master,
  commit 114e299ca66353fa7be1ee45bb4e1307d3de1fa2.
- x86: Remove .tfloat usage
- nptl: Convert tst-setuid2 to test-driver
- support: Add xpthread_cond_signal wrapper
- hppa: Fix initialization of dp register [BZ 29635]
- Fix iseqsig for _FloatN and _FloatNx in C++ with GCC 13
- malloc: Do not clobber errno on __getrandom_nocancel (BZ #29624)
- stdlib: Fix __getrandom_nocancel type and arc4random usage (BZ #29638)
- LoongArch: Add static PIE support
- Benchtest: Add additional benchmarks for strlen and strnlen
- x86: Fix wcsnlen-avx2 page cross length comparison [BZ #29591]
- Update _FloatN header support for C++ in GCC 13
- hurd: Fix typo
- get_nscd_addresses: Fix subscript typos [BZ #29605]
- hurd: Increase SOMAXCONN to 4096
- Use atomic_exchange_release/acquire

* Fri Sep 23 2022 Patsy Griffin <patsy@redhat.com> - 2.36.9000-8
- Auto-sync with upstream branch master,
  commit c02e29a0ba47d636281e1a026444a1a0a254aa12.
- nss: Use shared prefix in IPv4 address in tst-reload1
- nss: Enhance tst-reload1 coverage and logging
- Use C11 atomics instead of atomic_decrement_and_test
- Use C11 atomics instead of atomic_increment(_val)
- Use C11 atomics instead of atomic_and/or
- malloc: Print error when oldsize is not equal to the current size.
- Use '%z' instead of '%Z' on printf functions
- elf: Extract glibcelf constants from <elf.h>
- scripts: Enhance glibcpp to do basic macro processing
- scripts: Extract glibcpp.py from check-obsolete-constructs.py
- riscv: Remove RV32 floating point functions
- riscv: Consolidate the libm-test-ulps
- hurd: Fix SIOCADD/DELRT ioctls
- hurd: Drop struct rtentry and in6_rtmsg
- hurd: Add _IOT_ifrtreq to <net/route.h>
- elf: Use C11 atomics on _dl_mcount
- hurd: Use IF_NAMESIZE rather than IFNAMSIZ
- hurd: Add ifrtreq structure to net/route.h
- hppa: undef __ASSUME_SET_ROBUST_LIST
- linux: Use same type for MMAP2_PAGE_UNIT
- m68k: Enforce 4-byte alignment on internal locks (BZ #29537)
- nss: Fix tst-nss-files-hosts-long on single-stack hosts (bug 24816)
- nss: Implement --no-addrconfig option for getent
- gconv: Use 64-bit interfaces in gconv_parseconfdir (bug 29583)
- elf: Implement force_first handling in _dl_sort_maps_dfs (bug 28937)
- Linux: Do not skip d_ino == 0 entries in readdir, readdir64 (bug 12165)
- hurd: Factorize at/non-at functions
- tst-sprintf-errno: Update Hurd message length
- RISC-V: Allow long jumps to __syscall_error
- hurd: Make readlink* just reopen the file used for stat
- hurd: Fix readlink() hanging on fifo
- Fix BRE typos in check-safety.sh
- Makerules: fix MAKEFLAGS assignment for upcoming make-4.4 [BZ# 29564]
- Use relaxed atomics since there is no MO dependence

* Wed Sep 14 2022 Florian Weimer <fweimer@redhat.com> - 2.36.9000-7
- Remove .annobin* symbols from ld.so (#2126477)

* Tue Sep 13 2022 Florian Weimer <fweimer@redhat.com> - 2.36.9000-6
- Drop glibc-deprecated-selinux-makedb.patch.  Upstream has been ported
  to new libselinux.
- Auto-sync with upstream branch master,
  commit f278835f594740f5913001430641cf1da4878670:
- makedb: fix build with libselinux >= 3.1 (Bug 26233)
- tst-sprintf-errno: Update Hurd message output
- Use C11 atomics instead of atomic_decrement(_val)
- Use C11 atomics instead atomic_add(_zero)
- mktime: improve heuristic for ca-1986 Indiana DST
- Assume HAVE_TZSET in time/mktime.c
- elf: Fix hwcaps string size overestimation
- errlist: add missing entry for EDEADLOCK (bug 29545)
- Do not define static_assert or thread_local in headers for C2x
- malloc: Use C11 atomics rather than atomic_exchange_and_add
- Add NEWS entry for CVE-2022-39046
- elf: Rename _dl_sort_maps parameter from skip to force_first
- scripts/dso-ordering-test.py: Generate program run-time dependencies
- math: x86: Use prefix for FP_INIT_ROUNDMODE
- scripts/build-many-glibcs.py: Use https:// for sourceware.org Git clones
- debug: test for more required cacellation points (BZ# 29274)
- elf.h: Remove duplicate definition of VER_FLG_WEAK
- syslog: Remove extra whitespace between timestamp and message (BZ#29544)
- LoongArch: Add soft float support.
- elf: Restore how vDSO dependency is printed with LD_TRACE_LOADED_OBJECTS (BZ #29539)
- nptl: x86_64: Use same code for CURRENT_STACK_FRAME and stackinfo_get_sp

* Mon Sep 05 2022 Arjun Shankar <arjun@redhat.com> - 2.36.9000-5
- Co-Authored-By: Benjamin Herrenschmidt <benh@amazon.com>
- Retain .gnu_debuglink section in libc.so.6 (#2090744)
- Remove redundant ld.so debuginfo file (#2090744)

* Tue Aug 30 2022 DJ Delorie <dj@redhat.com> - 2.36.9000-4
- Auto-sync with upstream branch master,
  commit c7509d49c4e8fa494120c5ead21338559dad16f5.
- Apply asm redirections in wchar.h before first use
- resolv: Fix building tst-resolv-invalid-cname for earlier C standards
- syslog: Fix large messages (BZ#29536)
- posix: Fix macro expansion producing 'defined' has undefined behavior
- stdlib: Fix macro expansion producing 'defined' has undefined behavior
- S390: Always use svc 0
- nss_dns: Rewrite _nss_dns_gethostbyname4_r using current interfaces
- resolv: Add new tst-resolv-invalid-cname
- nss_dns: In gaih_getanswer_slice, skip strange aliases (bug 12154)
- nss_dns: Rewrite getanswer_r to match getanswer_ptr (bug 12154, bug 29305)
- nss_dns: Remove remnants of IPv6 address mapping
- nss_dns: Rewrite _nss_dns_gethostbyaddr2_r and getanswer_ptr
- nss_dns: Split getanswer_ptr from getanswer_r
- resolv: Add DNS packet parsing helpers geared towards wire format
- resolv: Add internal __ns_name_length_uncompressed function
- resolv: Add the __ns_samebinaryname function
- resolv: Add internal __res_binary_hnok function
- resolv: Add tst-resolv-aliases
- resolv: Add tst-resolv-byaddr for testing reverse lookup
- LoongArch: Use __builtin_{fmax,fmaxf,fmin,fminf} with GCC >= 13
- LoongArch: Fix ptr mangling/demangling features.
- nscd: Fix netlink cache invalidation if epoll is used [BZ #29415]
- Add test for bug 29530
- Makeconfig: Set pie-ccflag to -fPIE by default [BZ# 29514]
- hurd: Fix vm_size_t incoherencies
- mach: Make xpg_strerror_r set a message on error
- mach: Fix incoherency between perror and strerror
- elf: Call __libc_early_init for reused namespaces (bug 29528)
- csu: Change start code license to have link exception
- s390: Move hwcaps/platform names out of _rtld_global_ro
- Revert "Detect ld.so and libc.so version inconsistency during startup"
- Add NT_LOONGARCH_* from Linux 5.19 to elf.h
- Detect ld.so and libc.so version inconsistency during startup
- Merge getopt patch from Gnulib
- Merge _GL_UNUSED C23 patch from Gnulib
- LoongArch: Fix dl-machine.h code formatting.
- scripts/glibcelf.py: Add hashing support
- hurd: Fix starting static binaries with stack protection enabled
- htl: Make pthread*_cond_timedwait register wref before releasing mutex
- htl: make __pthread_hurd_cond_timedwait_internal check mutex is held
- Add AArch64 HWCAP2_* constants from Linux 5.19

* Mon Aug 22 2022 Arjun Shankar <arjun@redhat.com> - 2.36.9000-3
- Auto-sync with upstream branch master,
  commit a727220b37efc9d4d558a77c5fc57f3af99a4829:
- Add AGROUP from Linux 5.19 to sys/acct.h, remove Alpha version (bug 29502)
- alpha: Fix generic brk system call emulation in __brk_call (bug 29490)
- hurd: Assume non-suid during bootstrap

* Thu Aug 18 2022 Patsy Griffin <patsy@redhat.com> - 2.36.9000-2
- Auto-sync with upstream branch master,
  commit 9125e43daf92e3d4e69044a54b9fe9ed88c861ad.
- Use binutils 2.39 branch in build-many-glibcs.py
- S390: Fix werror=unused-variable in ifunc-impl-list.c.
- Ensure calculations happen with desired rounding mode in y1lf128
- localedata: Convert French language locales (fr_*) to UTF-8
- Linux: Fix enum fsconfig_command detection in <sys/mount.h>
- elf: Run tst-audit-tlsdesc, tst-audit-tlsdesc-dlopen everywhere
- Move ip_mreqn structure from Linux to generic
- malloc: Do not use MAP_NORESERVE to allocate heap segments
- Linux: Terminate subprocess on late failure in tst-pidfd (bug 29485)
- non-linux: bits/in.h: Add more RFC options

* Mon Aug 15 2022 Florian Weimer <fweimer@redhat.com> - 2.36.9000-1
- Auto-sync with upstream branch master,
  commit 453b88efe6fa79f5c7c6fccc3a520c75fdd43074:
- arm: Remove nested functionf rom relocate_pc24
- linux: Fix sys/mount.h usage with kernel headers
- linux: Use compile_c_snippet to check linux/mount.h availability
- linux: Mimic kernel defition for BLOCK_SIZE
- linux: Use compile_c_snippet to check linux/pidfd.h availability
- glibcextract.py: Add compile_c_snippet
- LoongArch: Add pointer mangling support.
- AArch64: Fix typo in sve configure check (BZ# 29394)
- libio: Improve performance of IO locks
- tst-process_madvise: Check process_madvise-syscall support.
- elf.h: Add ELFCOMPRESS_ZSTD
- inet: Turn __ivaliduser into a compatibility symbol
- x86: Fix `#define STRCPY` guard in strcpy-sse2.S
- elf: Replace `strcpy` call with `memcpy` [BZ #29454]
- soft-fp: Add fixhf[uns][di|si] and float[uns][di|si]hf
- i386: Use cmpl instead of cmp
- i386: Use fldt instead of fld on e_logl.S
- i386: Replace movzx with movzbl
- dlfcn: Pass caller pointer to static dlopen implementation (bug 29446)
- malloc: Correct the documentation of the top_pad default
- i386: Remove RELA support
- arm: Remove RELA support
- Remove ldd libc4 support
- Assume only FLAG_ELF_LIBC6 suport
- Remove left over LD_LIBRARY_VERSION usages
- Linux: Remove exit system call from _exit
- LoongArch: Add vdso support for gettimeofday.
- Update kernel version to 5.19 in header constant tests
- assert: Do not use stderr in libc-internal assert
- nptl: Remove uses of assert_perror
- stdio: Clean up __libc_message after unconditional abort
- Update syscall lists for Linux 5.19
- Use Linux 5.19 in build-many-glibcs.py
- socket: Check lengths before advancing pointer in CMSG_NXTHDR
- Don't use unsupported format string in ld.so (bug 29427)
- htl: Let pthread_self and cancellability called early
- stdlib: Simplify arc4random_uniform
- malloc: Use __getrandom_nocancel during tcache initiailization
- Remove spurious references to _dl_open_hook
- Open master branch for glibc 2.37 development

* Wed Aug 03 2022 Carlos O'Donell <carlos@redhat.com> - 2.36-1
- Auto-sync with upstream branch release/2.36/master,
  commit 33f1b4c1452b33991e670f636ebe98b90a405e10:
- wcsmbs: Add missing test-c8rtomb/test-mbrtoc8 dependency
- stdlib: Suppress gcc diagnostic that char8_t is a keyword in C++20 in uchar.h.
- Create ChangeLog.old/ChangeLog.25. (tag: glibc-2.36)
- Prepare for glibc 2.36 release.
- Update install.texi, and regenerate INSTALL.
- Update NEWS bug list.
- Update libc.pot for 2.36 release.
- tst-pidfd.c: UNSUPPORTED if we get EPERM on valid pidfd_getfd call
- stdlib: Tuned down tst-arc4random-thread internal parameters
- LoongArch: Add greg_t and gregset_t.
- LoongArch: Fix VDSO_HASH and VDSO_NAME.
- riscv: Update rv64 libm test ulps
- riscv: Update nofpu libm test ulps
