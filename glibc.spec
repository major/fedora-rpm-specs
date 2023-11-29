%global glibcsrcdir glibc-2.38.9000-295-g5d7f1bce7d
%global glibcversion 2.38.9000
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

%if %{with bootstrap}
# Disable benchtests, -Werror, docs, and valgrind if we're bootstrapping
%undefine with_benchtests
%undefine with_werror
%undefine with_docs
%undefine with_valgrind
%endif

# The annobin annotations cause binutils to produce broken ARM EABI
# unwinding information.  Symptom is a hang/test failure for
# malloc/tst-malloc-stats-cancellation.  See
# <https://bugzilla.redhat.com/show_bug.cgi?id=1951492>.
%ifarch armv7hl
%undefine _annotated_build
%endif

# We do our own build flags management.  In particular, see
# rpm_inherit_flags below.
%undefine _auto_set_build_flags

##############################################################################
# Any architecture/kernel combination that supports running 32-bit and 64-bit
# code in userspace is considered a biarch arch.
%global biarcharches %{ix86} x86_64 s390 s390x

# Avoid generating a glibc-headers package on architectures which are
# not biarch.
%ifarch %{biarcharches}
%global need_headers_package 1
%if 0%{?rhel} > 0
%global headers_package_name glibc-headers
%else
%ifarch %{ix86} x86_64
%global headers_package_name glibc-headers-x86
%endif
%ifarch s390 s390x
%global headers_package_name glibc-headers-s390
%endif
%dnl !rhel
%endif
%else
%global need_headers_package 0
%dnl !biarcharches
%endif

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
--
-- Note: We use _prefix because Fedora's UsrMove says so.
function call_ldconfig ()
  if not rpm.execute("%{_prefix}/sbin/ldconfig") then
    io.stdout:write ("Error: call to %{_prefix}/sbin/ldconfig failed.\n")
  end
end

function update_gconv_modules_cache ()
  local iconv_dir = "%{_libdir}/gconv"
  local iconv_cache = iconv_dir .. "/gconv-modules.cache"
  local iconv_modules = iconv_dir .. "/gconv-modules"
  if posix.utime(iconv_modules) == 0 then
    if posix.utime (iconv_cache) == 0 then
      if not rpm.execute("%{_prefix}/sbin/iconvconfig",
		         "-o", iconv_cache,
		         "--nostdlib",
		         iconv_dir)
      then
	io.stdout:write ("Error: call to %{_prefix}/sbin/iconvconfig failed.\n")
      end
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
%global baserelease 25
Release: %{baserelease}%{?dist}

# In general, GPLv2+ is used by programs, LGPLv2+ is used for
# libraries.
#
# LGPLv2+ with exceptions is used for things that are linked directly
# into dynamically linked programs and shared libraries (e.g. crt
# files, lib*_nonshared.a).  Historically, this exception also applies
# to parts of libio.
#
# GPLv2+ with exceptions is used for parts of the Arm unwinder.
#
# GFDL is used for the documentation.
#
# Some other licenses are used in various places (BSD, Inner-Net,
# ISC, Public Domain).
#
# HSRL and FSFAP are only used in test cases, which currently do not
# ship in binary RPMs, so they are not listed here.  MIT is used for
# scripts/install-sh, which does not ship, either.
#
# GPLv3+ is used by manual/texinfo.tex, which we do not use.
#
# LGPLv3+ is used by some Hurd code, which we do not build.
#
# LGPLv2 is used in one place (time/timespec_get.c, by mistake), but
# it is not actually compiled, so it does not matter for libraries.
License: LGPLv2+ and LGPLv2+ with exceptions and GPLv2+ and GPLv2+ with exceptions and BSD and Inner-Net and ISC and Public Domain and GFDL

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
  .. " " .. sysroot .. " " .. original)
}

# The wrapper script relies on the fact that debugedit does not change
# build IDs.
%global _no_recompute_build_ids 1
%undefine _unique_build_ids

##############################################################################
# Patches:
# - See each individual patch file for origin and upstream status.
# - For new patches follow template.patch format.
##############################################################################
Patch4: glibc-fedora-linux-tcsetattr.patch
Patch8: glibc-fedora-manual-dircategory.patch
Patch9: glibc-rh827510.patch
Patch13: glibc-fedora-localedata-rh61908.patch
Patch17: glibc-cs-path.patch
Patch23: glibc-python3.patch
Patch24: glibc-benchtests-aarch64.patch
Patch25: glibc-rh2248502.patch

##############################################################################
# Continued list of core "glibc" package information:
##############################################################################
Obsoletes: glibc-profile < 2.4
Obsoletes: nscd < 2.35
Provides: ldconfig
Provides: /sbin/ldconfig
Provides: /usr/sbin/ldconfig

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
%global target %{_target_cpu}-redhat-linux
%ifarch %{arm}
%global target %{_target_cpu}-redhat-linuxeabi
%endif
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
%if %{need_headers_package}
Requires: %{headers_package_name} = %{version}-%{release}
%endif
%if !(0%{?rhel} > 0 && %{need_headers_package})
# For backwards compatibility, when the glibc-headers package existed.
Provides: glibc-headers = %{version}-%{release}
Provides: glibc-headers(%{_target_cpu})
Obsoletes: glibc-headers < %{version}-%{release}
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
# glibc "headers" sub-package
# - The headers package includes all common headers that are shared amongst
#   the multilib builds. It avoids file conflicts between the architecture-
#   specific glibc-devel variants.
#   Files like gnu/stubs.h which have gnu/stubs-32.h (i686) and gnu/stubs-64.h
#   are included in glibc-headers, but the -32 and -64 files are in their
#   respective i686 and x86_64 devel packages.
##############################################################################
%if %{need_headers_package}
%package -n %{headers_package_name}
Summary: Additional internal header files for glibc-devel.
Requires: %{name} = %{version}-%{release}
%if 0%{?rhel} > 0
Provides: %{name}-headers(%{_target_cpu})
Obsoletes: glibc-headers-x86 < %{version}-%{release}
Obsoletes: glibc-headers-s390 < %{version}-%{release}
%else
BuildArch: noarch
%endif

%description -n %{headers_package_name}
The %{headers_package_name} package contains the architecture-specific
header files which cannot be included in glibc-devel package.
%endif

##############################################################################
# glibc "common" sub-package
##############################################################################
%package common
Summary: Common binaries and locale data for glibc
Requires: %{name} = %{version}-%{release}
Recommends: tzdata >= 2003a

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
%global locale_rx eo syr *_*

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
  { code="crh", name="Crimean Turkish", regions={ "UA" } },
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
  { code="kw", name="Cornish", regions={ "GB" } },
  { code="ky", name="Kyrgyz", regions={ "KG" } },
  { code="lb", name="Luxembourgish", regions={ "LU" } },
  { code="lg", name="Ganda", regions={ "UG" } },
  { code="li", name="Limburgish", regions={ "BE", "NL" } },
  { code="lij", name="Ligurian", regions={ "IT" } },
  { code="ln", name="Lingala", regions={ "CD" } },
  { code="lo", name="Lao", regions={ "LA" } },
  { code="lt", name="Lithuanian", regions={ "LT" } },
  { code="lv", name="Latvian", regions={ "LV" } },
  { code="lzh", name="Literary Chinese", regions={ "TW" } },
  { code="mag", name="Magahi", regions={ "IN" } },
  { code="mai", name="Maithili", regions={ "IN", "NP" } },
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
  { code="st", name="Southern Sotho", regions={ "ZA" } },
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
Supplements: (glibc and (]]..suppl..[[))
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

# We build using the native system compilers.
GCC=gcc
GXX=g++

# Part of rpm_inherit_flags.  Is overridden below.
rpm_append_flag ()
{
    BuildFlags="$BuildFlags $*"
}

# Propagates the listed flags to rpm_append_flag if supplied by
# redhat-rpm-config.
BuildFlags="-O2 -g"
rpm_inherit_flags ()
{
	local reference=" $* "
	local flag
	for flag in $RPM_OPT_FLAGS $RPM_LD_FLAGS ; do
		if echo "$reference" | grep -q -F " $flag " ; then
			rpm_append_flag "$flag"
		fi
	done
}

# Propgate select compiler flags from redhat-rpm-config.  These flags
# are target-dependent, so we use only those which are specified in
# redhat-rpm-config.  We keep the -m32/-m32/-m64 flags to support
# multilib builds.
#
# Note: For building alternative run-times, care is required to avoid
# overriding the architecture flags which go into CC/CXX.  The flags
# below are passed in CFLAGS.

rpm_inherit_flags \
	"-Wp,-D_GLIBCXX_ASSERTIONS" \
	"-fasynchronous-unwind-tables" \
	"-fstack-clash-protection" \
	"-fno-omit-frame-pointer" \
	"-funwind-tables" \
	"-m31" \
	"-m32" \
	"-m64" \
	"-march=armv8-a+lse" \
	"-march=armv8.1-a" \
	"-march=haswell" \
	"-march=i686" \
	"-march=x86-64" \
	"-march=x86-64-v2" \
	"-march=x86-64-v3" \
	"-march=x86-64-v4" \
	"-march=z13" \
	"-march=z14" \
	"-march=z15" \
	"-march=zEC12" \
	"-mbackchain" \
	"-mbranch-protection=standard" \
	"-mcpu=power10" \
	"-mcpu=power8" \
	"-mcpu=power9" \
	"-mfpmath=sse" \
	"-mno-omit-leaf-frame-pointer" \
	"-msse2" \
	"-mstackrealign" \
	"-mtune=generic" \
	"-mtune=power10" \
	"-mtune=power8" \
	"-mtune=power9" \
	"-mtune=z13" \
	"-mtune=z14" \
	"-mtune=z15" \
	"-mtune=zEC12" \
	"-specs=/usr/lib/rpm/redhat/redhat-annobin-cc1" \

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
# Save the used compiler and options into the file "Gcc" for use later
# by %%install.
echo "$GCC" > Gcc

##############################################################################
# build()
#	Build glibc in `build-%{target}$1', passing the rest of the arguments
#	as CFLAGS to the build (not the same as configure CFLAGS). Several
#	global values are used to determine build flags, kernel version,
#	system tap support, etc.
##############################################################################
build()
{
	local builddir=build-%{target}${1:+-$1}
	${1+shift}
	rm -rf $builddir
	mkdir $builddir
	pushd $builddir
	../configure CC="$GCC" CXX="$GXX" CFLAGS="$BuildFlags $*" \
		--prefix=%{_prefix} \
		--with-headers=%{_prefix}/include $EnableKernel \
		--with-nonshared-cflags="$BuildFlagsNonshared" \
		--enable-bind-now \
		--build=%{target} \
		--enable-stack-protector=strong \
		--enable-systemtap \
		${core_with_options} \
%ifarch x86_64 %{ix86}
	       --enable-cet \
%endif
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

# Default set of compiler options.
build

##############################################################################
# Install glibc...
##############################################################################
%install

# The built glibc is installed into a subdirectory of $RPM_BUILD_ROOT.
# For a system glibc that subdirectory is "/" (the root of the filesystem).
# This is called a sysroot (system root) and can be changed if we have a
# distribution that supports multiple installed glibc versions.
%global glibc_sysroot $RPM_BUILD_ROOT

# Remove existing file lists.
find . -type f -name '*.filelist' -exec rm -rf {} \;

# Reload compiler and build options that were used during %%build.
GCC=`cat Gcc`

%ifarch riscv64
# RISC-V ABI wants to install everything in /lib64/lp64d or /usr/lib64/lp64d.
# Make these be symlinks to /lib64 or /usr/lib64 respectively.  See:
# https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/DRHT5YTPK4WWVGL3GIN5BF2IKX2ODHZ3/
for d in %{glibc_sysroot}%{_libdir} %{glibc_sysroot}/%{_lib}; do
	mkdir -p $d
	(cd $d && ln -sf . lp64d)
done
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
	for lib in libc math/libm nptl/libpthread rt/librt nptl_db/libthread_db
	do
		libbase=${lib#*/}
		# Take care that `libbaseso' has a * that needs expanding so
		# take care with quoting.
		libbaseso=$(basename %{glibc_sysroot}/%{_lib}/${libbase}-*.so)
		# Only install if different from default build library.
		if cmp -s ${lib}.so ../build-%{target}/${lib}.so; then
			ln -sf "$subdir_up"/$libbaseso $libdestdir/$libbaseso
		else
			cp -a ${lib}.so $libdestdir/$libbaseso
		fi
		dlib=$libdestdir/$(basename %{glibc_sysroot}/%{_lib}/${libbase}.so.*)
		ln -sf $libbaseso $dlib
	done
}

##############################################################################
# Remove the files we don't want to distribute
##############################################################################

# Remove the libNoVersion files.
# XXX: This looks like a bug in glibc that accidentally installed these
#      wrong files. We probably don't need this today.
rm -f %{glibc_sysroot}/%{_libdir}/libNoVersion*
rm -f %{glibc_sysroot}/%{_lib}/libNoVersion*

# Remove the old nss modules.
rm -f %{glibc_sysroot}/%{_lib}/libnss1-*
rm -f %{glibc_sysroot}/%{_lib}/libnss-*.so.1

# This statically linked binary is no longer necessary in a world where
# the default Fedora install uses an initramfs, and further we have rpm-ostree
# which captures the whole userspace FS tree.
# Further, see https://github.com/projectatomic/rpm-ostree/pull/1173#issuecomment-355014583
rm -f %{glibc_sysroot}/{usr/,}sbin/sln

######################################################################
# Run ldconfig to create all the symbolic links we need
######################################################################

# Note: This has to happen before creating /etc/ld.so.conf.

mkdir -p %{glibc_sysroot}/var/cache/ldconfig
truncate -s 0 %{glibc_sysroot}/var/cache/ldconfig/aux-cache

# ldconfig is statically linked, so we can use the new version.
%{glibc_sysroot}/sbin/ldconfig -N -r %{glibc_sysroot}

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
ln -s programs/*.gperf .
popd
pushd iconv
ln -s ../locale/programs/charmap-kw.gperf .
popd

%if %{with docs}
# Remove the `dir' info-heirarchy file which will be maintained
# by the system as it adds info files to the install.
rm -f %{glibc_sysroot}%{_infodir}/dir
%endif

# Move libpcprofile.so and libmemusage.so into the proper library directory.
# They can be moved without any real consequences because users would not use
# them directly.
mkdir -p %{glibc_sysroot}%{_libdir}
mv -f %{glibc_sysroot}/%{_lib}/lib{pcprofile,memusage}.so \
	%{glibc_sysroot}%{_libdir}

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
ar cr %{glibc_sysroot}%{_prefix}/%{_lib}/libpthread_nonshared.a

##############################################################################
# Beyond this point in the install process we no longer modify the set of
# installed files.
##############################################################################

##############################################################################
# Build the file lists used for describing the package and subpackages.
##############################################################################
# There are several main file lists (and many more for
# the langpack sub-packages (langpack-${lang}.filelist)):
# * master.filelist
#	- Master file list from which all other lists are built.
# * glibc.filelist
#	- Files for the glibc packages.
# * common.filelist
#	- Flies for the common subpackage.
# * utils.filelist
#	- Files for the utils subpackage.
# * devel.filelist
#	- Files for the devel subpackage.
# * doc.filelist
#	- Files for the documentation subpackage.
# * headers.filelist
#	- Files for the headers subpackage.
# * static.filelist
#	- Files for the static subpackage.
# * libnsl.filelist
#       - Files for the libnsl subpackage
# * nss_db.filelist
# * nss_hesiod.filelist
#       - File lists for nss_* NSS module subpackages.
# * nss-devel.filelist
#       - File list with the .so symbolic links for NSS packages.
# * compat-libpthread-nonshared.filelist.
#	- File list for compat-libpthread-nonshared subpackage.

# Create the main file lists. This way we can append to any one of them later
# wihtout having to create it. Note these are removed at the start of the
# install phase.
touch master.filelist
touch glibc.filelist
touch common.filelist
touch utils.filelist
touch gconv.filelist
touch devel.filelist
touch doc.filelist
touch headers.filelist
touch static.filelist
touch libnsl.filelist
touch nss_db.filelist
touch nss_hesiod.filelist
touch nss-devel.filelist
touch compat-libpthread-nonshared.filelist

###############################################################################
# Master file list, excluding a few things.
###############################################################################
{
  # List all files or links that we have created during install.
  # Files with 'etc' are configuration files, likewise 'gconv-modules'
  # and 'gconv-modules.cache' are caches, and we exclude them.
  find %{glibc_sysroot} \( -type f -o -type l \) \
       \( \
	 -name etc -printf "%%%%config " -o \
	 -name gconv-modules.cache \
	 -printf "%%%%verify(not md5 size mtime) " -o \
	 -name gconv-modules* \
	 -printf "%%%%verify(not md5 size mtime) %%%%config(noreplace) " \
	 , \
	 ! -path "*/lib/debug/*" -printf "/%%P\n" \)
  # List all directories with a %%dir prefix.  We omit the info directory and
  # all directories in (and including) /usr/share/locale.
  find %{glibc_sysroot} -type d \
       \( -path '*%{_prefix}/share/locale' -prune -o \
       \( -path '*%{_prefix}/share/*' \
%if %{with docs}
	! -path '*%{_infodir}' -o \
%endif
	  -path "*%{_prefix}/include/*" \
       \) -printf "%%%%dir /%%P\n" \)
} | {
  # Also remove the *.mo entries.  We will add them to the
  # language specific sub-packages.
  # libnss_ files go into subpackages related to NSS modules.
  # and .*/share/i18n/charmaps/.*), they go into the sub-package
  # "locale-source":
  sed -e '\,.*/share/locale/\([^/_]\+\).*/LC_MESSAGES/.*\.mo,d' \
      -e '\,.*/share/i18n/locales/.*,d' \
      -e '\,.*/share/i18n/charmaps/.*,d' \
      -e '\,.*/etc/\(localtime\|nsswitch.conf\|ld\.so\.conf\|ld\.so\.cache\|default\|rpc\|gai\.conf\),d' \
      -e '\,.*/%{_libdir}/lib\(pcprofile\|memusage\)\.so,d' \
      -e '\,.*/bin/\(memusage\|mtrace\|xtrace\|pcprofiledump\),d'
} | sort > master.filelist

# The master file list is now used by each subpackage to list their own
# files. We go through each package and subpackage now and create their lists.
# Each subpackage picks the files from the master list that they need.
# The order of the subpackage list generation does not matter.

# Make the master file list read-only after this point to avoid accidental
# modification.
chmod 0444 master.filelist

###############################################################################
# glibc
###############################################################################

# Add all files with the following exceptions:
# - The info files '%{_infodir}/dir'
# - The partial (lib*_p.a) static libraries, include files.
# - The static files, objects, and unversioned DSOs.
# - The bin, locale, some sbin, and share.
#   - We want iconvconfig in the main package and we do this by using
#     a double negation of -v and [^i] so it removes all files in
#     sbin *but* iconvconfig.
# - All the libnss files (we add back the ones we want later).
# - All bench test binaries.
# - The aux-cache, since it's handled specially in the files section.
# - Extra gconv modules.  We add the required modules later.
cat master.filelist \
	| grep -v \
	-e '%{_infodir}' \
	-e '%{_libdir}/lib.*_p.a' \
	-e '%{_prefix}/include' \
	-e '%{_libdir}/lib.*\.a' \
        -e '%{_libdir}/.*\.o' \
	-e '%{_libdir}/lib.*\.so' \
	-e '%{_libdir}/gconv/.*\.so$' \
	-e '%{_libdir}/gconv/gconv-modules.d/gconv-modules-extra\.conf$' \
	-e '%{_prefix}/bin' \
	-e '%{_prefix}/lib/locale' \
	-e '%{_prefix}/sbin/[^i]' \
	-e '%{_prefix}/share' \
	-e '/var/db/Makefile' \
	-e '/libnss_.*\.so[0-9.]*$' \
	-e '/libnsl' \
	-e 'glibc-benchtests' \
	-e 'aux-cache' \
	> glibc.filelist

# Add specific files:
# - The nss_files, nss_compat, and nss_db files.
# - The libmemusage.so and libpcprofile.so used by utils.
for module in compat files dns; do
    cat master.filelist \
	| grep -E \
	-e "/libnss_$module(\.so\.[0-9.]+|-[0-9.]+\.so)$" \
	>> glibc.filelist
done
grep -e "libmemusage.so" -e "libpcprofile.so" master.filelist >> glibc.filelist

###############################################################################
# glibc-gconv-extra
###############################################################################

grep -e "gconv-modules-extra.conf" master.filelist > gconv.filelist

# Put the essential gconv modules into the main package.
GconvBaseModules="ANSI_X3.110 ISO8859-15 ISO8859-1 CP1252"
GconvBaseModules="$GconvBaseModules UNICODE UTF-16 UTF-32 UTF-7"
%ifarch s390 s390x
GconvBaseModules="$GconvBaseModules ISO-8859-1_CP037_Z900 UTF8_UTF16_Z9"
GconvBaseModules="$GconvBaseModules UTF16_UTF32_Z9 UTF8_UTF32_Z9"
%endif
GconvAllModules=$(cat master.filelist |
                 sed -n 's|%{_libdir}/gconv/\(.*\)\.so|\1|p')

# Put the base modules into glibc and the rest into glibc-gconv-extra
for conv in $GconvAllModules; do
    if echo $GconvBaseModules | grep -q $conv; then
	grep -E -e "%{_libdir}/gconv/$conv.so$" \
	    master.filelist >> glibc.filelist
    else
	grep -E -e "%{_libdir}/gconv/$conv.so$" \
	    master.filelist >> gconv.filelist
    fi
done

###############################################################################
# glibc-devel
###############################################################################

# Static libraries that land in glibc-devel, not glibc-static.
devel_static_library_pattern='/lib\(\(c\|nldbl\|mvec\)_nonshared\|g\|ieee\|mcheck\|pthread\|dl\|rt\|util\|anl\)\.a$'
# Static libraries neither in glibc-devel nor in glibc-static.
other_static_library_pattern='/libpthread_nonshared\.a'

grep '%{_libdir}/lib.*\.a' master.filelist \
  | grep "$devel_static_library_pattern" \
  | grep -v "$other_static_library_pattern" \
  > devel.filelist

# Put all of the object files and *.so (not the versioned ones) into the
# devel package.
grep '%{_libdir}/.*\.o' < master.filelist >> devel.filelist
grep '%{_libdir}/lib.*\.so' < master.filelist >> devel.filelist
# The exceptions are:
# - libmemusage.so and libpcprofile.so in glibc used by utils.
# - libnss_*.so which are in nss-devel.
sed -i -e '\,libmemusage.so,d' \
	-e '\,libpcprofile.so,d' \
	-e '\,/libnss_[a-z]*\.so$,d' \
	devel.filelist

%if %{glibc_autorequires}
mkdir -p %{glibc_sysroot}/%{_rpmconfigdir} %{glibc_sysroot}/%{_fileattrsdir}
sed < %{SOURCE3} \
    -e s/@VERSION@/%{version}/ \
    -e s/@RELEASE@/%{baserelease}/ \
    -e s/@SYMVER@/%{glibc_autorequires_symver}/ \
    > %{glibc_sysroot}/%{_rpmconfigdir}/glibc.req
cp %{SOURCE4} %{glibc_sysroot}/%{_fileattrsdir}/glibc.attr
%endif

###############################################################################
# glibc-doc
###############################################################################

%if %{with docs}
# Put the info files into the doc file list, but exclude the generated dir.
grep '%{_infodir}' master.filelist | grep -v '%{_infodir}/dir' > doc.filelist
grep '%{_docdir}' master.filelist >> doc.filelist
%endif

###############################################################################
# glibc-headers
###############################################################################

%if %{need_headers_package}
# The glibc-headers package includes only common files which are identical
# across all multilib packages. We must keep gnu/stubs.h and gnu/lib-names.h
# in the glibc-headers package, but the -32, -64, -64-v1, and -64-v2 versions
# go into glibc-devel.
grep '%{_prefix}/include/gnu/stubs-.*\.h$' < master.filelist >> devel.filelist || :
grep '%{_prefix}/include/gnu/lib-names-.*\.h$' < master.filelist >> devel.filelist || :
# Put the include files into headers file list.
grep '%{_prefix}/include' < master.filelist \
  | grep -E -v '%{_prefix}/include/gnu/stubs-.*\.h$' \
  | grep -E -v '%{_prefix}/include/gnu/lib-names-.*\.h$' \
  > headers.filelist
%else
# If there is no glibc-headers package, all header files go into the
# glibc-devel package.
grep '%{_prefix}/include' < master.filelist >> devel.filelist
%endif

###############################################################################
# glibc-static
###############################################################################

# Put the rest of the static files into the static package.
grep '%{_libdir}/lib.*\.a' < master.filelist \
  | grep -v "$devel_static_library_pattern" \
  | grep -v "$other_static_library_pattern" \
  > static.filelist

###############################################################################
# glibc-common
###############################################################################

# All of the bin and certain sbin files go into the common package except
# iconvconfig which needs to go in glibc.  The iconvconfig binary is kept in
# the main glibc package because we use it in the post-install scriptlet to
# rebuild the gconv-modules.cache.  The makedb binary is in nss_db.
grep '%{_prefix}/bin' master.filelist \
	| grep -v '%{_prefix}/bin/makedb' \
	>> common.filelist
grep '%{_prefix}/sbin' master.filelist \
	| grep -v '%{_prefix}/sbin/iconvconfig' >> common.filelist
# All of the files under share go into the common package since they should be
# multilib-independent.
# Exceptions:
# - The actual share directory, not owned by us.
# - The info files which go into doc, and the info directory.
# - All documentation files, which go into doc.
grep '%{_prefix}/share' master.filelist \
	| grep -v \
	-e '%{_prefix}/share/info/libc.info.*' \
	-e '%%dir %{prefix}/share/info' \
	-e '%%dir %{prefix}/share' \
	-e '%{_docdir}' \
	>> common.filelist

###############################################################################
# glibc-utils
###############################################################################

# Add the utils scripts and programs to the utils subpackage.
cat > utils.filelist <<EOF
%if %{without bootstrap}
%{_prefix}/bin/memusage
%{_prefix}/bin/memusagestat
%endif
%{_prefix}/bin/mtrace
%{_prefix}/bin/pcprofiledump
%{_prefix}/bin/xtrace
EOF

###############################################################################
# nss_db, nss_hesiod
###############################################################################

# Move the NSS-related files to the NSS subpackages.  Be careful not
# to pick up .debug files, and the -devel symbolic links.
for module in db hesiod; do
  grep -E "/libnss_$module\\.so\\.[0-9.]+\$" \
    master.filelist > nss_$module.filelist
done
grep -E "%{_prefix}/bin/makedb$" master.filelist >> nss_db.filelist

###############################################################################
# nss-devel
###############################################################################

# Symlinks go into the nss-devel package (instead of the main devel
# package).
grep '/libnss_[a-z]*\.so$' master.filelist > nss-devel.filelist

###############################################################################
# libnsl
###############################################################################

# Prepare the libnsl-related file lists.
grep -E '/libnsl\.so\.[0-9]+$' master.filelist > libnsl.filelist
test $(wc -l < libnsl.filelist) -eq 1

%if %{with benchtests}
###############################################################################
# glibc-benchtests
###############################################################################

# List of benchmarks.
find build-%{target}/benchtests -type f -executable | while read b; do
	echo "%{_prefix}/libexec/glibc-benchtests/$(basename $b)"
done >> benchtests.filelist
# ... and the makefile.
for b in %{SOURCE1} %{SOURCE2}; do
	echo "%{_prefix}/libexec/glibc-benchtests/$(basename $b)" >> benchtests.filelist
done
# ... and finally, the comparison scripts.
echo "%{_prefix}/libexec/glibc-benchtests/benchout.schema.json" >> benchtests.filelist
echo "%{_prefix}/libexec/glibc-benchtests/compare_bench.py*" >> benchtests.filelist
echo "%{_prefix}/libexec/glibc-benchtests/import_bench.py*" >> benchtests.filelist
echo "%{_prefix}/libexec/glibc-benchtests/validate_benchout.py*" >> benchtests.filelist
%endif

###############################################################################
# compat-libpthread-nonshared
###############################################################################
echo "%{_libdir}/libpthread_nonshared.a" >> compat-libpthread-nonshared.filelist

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

echo ====================TESTING END=====================
PLTCMD='/^Relocation section .*\(\.rela\?\.plt\|\.rela\.IA_64\.pltoff\)/,/^$/p'
echo ====================PLT RELOCS LD.SO================
readelf -Wr %{glibc_sysroot}/%{_lib}/ld-*.so | sed -n -e "$PLTCMD"
echo ====================PLT RELOCS LIBC.SO==============
readelf -Wr %{glibc_sysroot}/%{_lib}/libc-*.so | sed -n -e "$PLTCMD"
echo ====================PLT RELOCS END==================

# Obtain a way to run the dynamic loader.  Avoid matching the symbolic
# link and then pick the first loader (although there should be only
# one).  See wrap-find-debuginfo.sh.
ldso_path="$(find %{glibc_sysroot}/ -regextype posix-extended \
  -regex '.*/ld(-.*|64|)\.so\.[0-9]+$' -type f | LC_ALL=C sort | head -n1)"
run_ldso="$ldso_path --library-path %{glibc_sysroot}/%{_lib}"

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

%post -p <lua>
%glibc_post_funcs
-- (1) Remove multilib libraries from previous installs.
-- In order to support in-place upgrades, we must immediately remove
-- obsolete platform directories after installing a new glibc
-- version.  RPM only deletes files removed by updates near the end
-- of the transaction.  If we did not remove the obsolete platform
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

-- (2) Update /etc/ld.so.conf
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

-- (3) Rebuild ld.so.cache early.
-- If the format of the cache changes then we need to rebuild
-- the cache early to avoid any problems running binaries with
-- the new glibc.

call_ldconfig()

-- (4) Update gconv modules cache.
-- If the /usr/lib/gconv/gconv-modules.cache exists, then update it
-- with the latest set of modules that were just installed.
-- We assume that the cache is in _libdir/gconv and called
-- "gconv-modules.cache".

update_gconv_modules_cache()

-- (5) On upgrades, restart systemd if installed.  "systemctl -q" does
-- not suppress the error message (which is common in chroots), so
-- open-code rpm.execute with standard error suppressed.
if tonumber(arg[2]) >= 2
   and posix.access("%{_prefix}/bin/systemctl", "x")
then
  local pid = posix.fork()
  if pid == 0 then
    posix.redirect2null(2)
    posix.exec("%{_prefix}/bin/systemctl", "daemon-reexec")
  elseif pid > 0 then
    posix.wait(pid)
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
%dir %{_prefix}/%{_lib}/audit
%verify(not md5 size mtime) %config(noreplace) /etc/ld.so.conf
%verify(not md5 size mtime) %config(noreplace) /etc/rpc
%dir /etc/ld.so.conf.d
%dir %{_prefix}/libexec/getconf
%dir %{_libdir}/gconv
%dir %{_libdir}/gconv/gconv-modules.d
%dir %attr(0700,root,root) /var/cache/ldconfig
%attr(0600,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/cache/ldconfig/aux-cache
%attr(0644,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /etc/ld.so.cache
%attr(0644,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /etc/gai.conf
# If rpm doesn't support %license, then use %doc instead.
%{!?_licensedir:%global license %%doc}
%license COPYING COPYING.LIB LICENSES

%files -f common.filelist common
%dir %{_prefix}/lib/locale
%dir %{_prefix}/lib/locale/C.utf8
%{_prefix}/lib/locale/C.utf8/*

%files all-langpacks
%{_prefix}/lib/locale/locale-archive
%{_prefix}/lib/locale/locale-archive.real
%{_prefix}/share/locale/*/LC_MESSAGES/libc.mo

%files locale-source
%dir %{_prefix}/share/i18n/locales
%{_prefix}/share/i18n/locales/*
%dir %{_prefix}/share/i18n/charmaps
%{_prefix}/share/i18n/charmaps/*

%files -f devel.filelist devel
%if %{glibc_autorequires}
%attr(0755,root,root) %{_rpmconfigdir}/glibc.req
%{_fileattrsdir}/glibc.attr
%endif

%if %{with docs}
%files -f doc.filelist doc
%endif

%files -f static.filelist static

%if  %{need_headers_package}
%files -f headers.filelist -n %{headers_package_name}
%endif

%files -f utils.filelist utils

%files -f gconv.filelist gconv-extra

%files -f nss_db.filelist -n nss_db
/var/db/Makefile
%files -f nss_hesiod.filelist -n nss_hesiod
%doc hesiod/README.hesiod
%files -f nss-devel.filelist nss-devel

%files -f libnsl.filelist -n libnsl
/%{_lib}/libnsl.so.1

%if %{with benchtests}
%files benchtests -f benchtests.filelist
%endif

%files -f compat-libpthread-nonshared.filelist -n compat-libpthread-nonshared

%changelog
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
