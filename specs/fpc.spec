# Workaround LTO related issue when stripping the target files
# See related issue for cross-gcc: #1863378
%global __brp_strip_lto %{nil}

Name:           fpc
Summary:        Free Pascal Compiler
License:        GPL-2.0-or-later AND LGPL-2.1-or-later WITH Independent-modules-exception
URL:            http://www.freepascal.org/

%global version_code 3.2.3

%global beta 1
%global version_beta 3.2.4
%global version_suffix rc1

%if ! 0%{?beta}
Version:        %{version_code}
%else
Version:        %{version_beta}~%{version_suffix}
%endif
Release:        1%{?dist}

%if ! 0%{?beta}
  %global archive_type dist
  %global archive_suffix %{version_code}
%else
  %global archive_type beta
  %global archive_suffix %{version_beta}-%{version_suffix}
%endif
Source0:        https://downloads.freepascal.org/fpc/%{archive_type}/%{archive_suffix}/source/fpcbuild-%{archive_suffix}.tar.gz

# Bootstrap the compiler for a new architecture. Set this to 0 after we've bootstrapped.
%global bootstrap 0

# This is only needed when we're bootstrapping.
# But it's not in an 'if defined' block, since the file has to be included in the srpm
# Thus you should enable this line when we're bootstrapping for any target
#
# Last used for aaarch64 and ppc64le bootstrap.
# For the aarch64 bootstrap, a compiler has been used that has been cross-compiled on a x86_64 system using:
#   make all CPU_TARGET=aarch64 OS_TARGET=linux BINUTILSPREFIX=aarch64-linux-gnu-
# For the ppc64 boostrap, a compiler has been used that has been cross-compiled on a x86_64 system using:
#   make all CPU_TARGET=powerpc64 OS_TARGET=linux BINUTILSPREFIX=powerpc64le-linux-gnu- CROSSOPT="-Cb- -Caelfv2"
#
# in the main directory of fpc-r44016. The compilers were then copied using:
#   cp compiler/ppca64    ~/fpc-3.2.0-bin/ppca64-3.2.0-bootstrap
#   cp compiler/ppcppc64  ~/fpc-3.2.0-bin/ppcppc64-3.2.0-bootstrap
# The zip file was then created using:
#   zip -9 fpc-3.2.0-bin.zip -r fpc-3.2.0-bin/
#
# Source100:	https://suve.fedorapeople.org/fpc-3.2.0-bin--patch0.zip

# Configuration templates:
Source10:        fpc.cft
Source11:        fppkg.cfg
Source12:        default.cft

# On Fedora we do not want stabs debug-information. (even on 32 bit platforms)
# https://bugzilla.redhat.com/show_bug.cgi?id=1475223 
Patch0:         fpc-3.2.0--dwarf-debug.patch

# Allow for reproducible builds
# https://bugzilla.redhat.com/show_bug.cgi?id=1778875
Patch1:         fpc-3.2.0--honor_SOURCE_DATE_EPOCH_in_date.patch

# The "pas2jni" util program shipped with FPC uses threads,
# but is compiled without thread support and fails to actually do anything useful when run.
# Submitted upstream: https://gitlab.com/freepascal.org/fpc/source/-/merge_requests/185
Patch5:         fpc-3.2.2--pas2jni-cthreads.patch

# By default, the textmode IDE installs some data files (templates, ASCII art)
# in the same directory as the executable (i.e. /usr/bin). This patch moves
# the data files inside the main FPC install directory (LIBDIR/fpc/VERSION/ide).
Patch6:         fpc-3.2.2--fix-IDE-data-files-locations.patch

# "man 5 resolv.conf" states that, should the file be missing or empty,
# then C stdlib functions dealing with name resolution should fall back
# to querying the DNS server running on the local machine.
#
# FPC, by default, does not link to libc, providing its own standard library;
# said code does not contain this fallback logic.
#
# Backport of upstream commit:
# https://gitlab.com/freepascal.org/fpc/source/-/commit/1cd1415df746ecaf9603bb0afb8660d3af3ea1f1
Patch8:         fpc-3.2.2--fallback-to-localhost-when-no-dns-server-specified.patch

# The compiler produces incorrect "unit unused" hints
# if symbols from a unit are used only for compile-time checks.
#
# Backport of upstream commits:
# https://gitlab.com/freepascal.org/fpc/source/-/commit/22ec4a20332f8208273604b46e727e481f6502eb.patch
# https://gitlab.com/freepascal.org/fpc/source/-/commit/397293f09f7a3e116119ab629687c64aae507539.patch
Patch9:         fpc-3.2.2--compiletime-check-is-usage.patch

# FPC uses its own architecture names that do not align with the ones used by Fedora.
%global arm_ppc ppcarm
%global arm_ppcross ppcrossarm
%global arm_arch arm
%global arm_opts -dFPC_ARMHF

%global aarch64_ppc ppca64
%global aarch64_ppcross ppcrossa64
%global aarch64_arch aarch64
%global aarch64_opts %{nil}

%global ppc64le_ppc ppcppc64
%global ppc64le_ppcross ppcrossppc64
%global ppc64le_arch powerpc64
%global ppc64le_opts -Cb- -Caelfv2

%global i386_ppc ppc386
%global i386_ppcross ppcross386
%global i386_arch i386
%global i386_opts %{nil}

%global x86_64_ppc ppcx64
%global x86_64_ppcross ppcrossx64
%global x86_64_arch x86_64
%global x86_64_opts %{nil}

ExclusiveArch: aarch64 %{ix86} x86_64 ppc64le

%ifarch aarch64
  %global native_ppc %{aarch64_ppc}
  %global native_arch %{aarch64_arch}
  %global native_opts %{aarch64_opts}
%else
  %ifarch %{ix86}
    %global native_ppc %{i386_ppc}
    %global native_arch %{i386_arch}
    %global native_opts %{i386_opts}
  %else
    %ifarch ppc64 ppc64le
      %global native_ppc %{ppc64le_ppc}
      %global native_arch %{ppc64le_arch}
      %global native_opts %{ppc64le_opts}
    %else
      %ifarch x86_64
        %global native_ppc %{x86_64_ppc}
        %global native_arch %{x86_64_arch}
        %global native_opts %{x86_64_opts}
      %else
        # Unsupported host arch. Not using %%{error} here because
        # SRPM rebuilds do not care about ExclusiveArch.
      %endif
    %endif
  %endif
%endif

# Helper macro to reduce amount of typing
%global units_native units-%{native_arch}-linux

Requires:       binutils
Requires:       %{name}-%{units_native}%{?_isa} = %{version}-%{release}

%if ! 0%{?bootstrap}
BuildRequires:  fpc
%endif

# Not strictly needed, apart from finding out the path to libgcc
BuildRequires:  gcc

BuildRequires:  glibc-devel
BuildRequires:  make
BuildRequires:  tex(imakeidx.sty)
BuildRequires:  tex(latex)
BuildRequires:  tex(tex)
BuildRequires:  tex(upquote.sty)
BuildRequires:  tetex-fonts

# Cross-compiling for i386 is currently supported only on x86_64,
# as it requires support for 80-bit floating point numbers,
# and there's no softfloat80 implementation in the compiler.
%ifarch x86_64
%global cross_i386 1
%endif

# Cross-compiling for x86_64 is currently supported only on i686.
# Same 80-bit float issue as above.
%ifarch %{ix86}
%global cross_x86_64 1
%endif

%ifnarch %{arm}
%global cross_arm 1
%endif

%ifnarch aarch64
%global cross_aarch64 1
%endif

%ifnarch ppc64le
%global cross_ppc64le 1
%endif

%ifarch %{ix86}
%global cross_win32 1
%else
%global cross_win32 0%{?cross_i386}
%endif

%ifarch x86_64
%global cross_win64 1
%else
%global cross_win64 0%{?cross_x86_64}
%endif


%description
Free Pascal is a free 32/64bit Pascal Compiler. It comes with a run-time
library and is fully compatible with Turbo Pascal 7.0 and nearly Delphi
compatible. Some extensions are added to the language, like function
overloading and generics. Shared libraries can be linked. This package
contains the command-line compiler and utilities.

# -- Native units

%package %{units_native}
Summary: Free Pascal Compiler - units for %{native_arch}-linux
Requires: %{name}%{?_isa} = %{version}-%{release}

%description %{units_native}
This package provides pre-compiled unit files for developing Free Pascal
applications for Linux (%{native_arch} processor architecture). It includes
the runtime library (RTL) and the free component library (FCL).

# -- Cross-compilers

%if 0%{?cross_arm}
%package cross-arm
Summary: Free Pascal Compiler - arm cross-compiler
Requires: %{name}%{?_isa} = %{version}-%{release}
Recommends: %{name}-units-arm-linux%{?_isa} = %{version}-%{release}

Requires: binutils-arm-linux-gnu
BuildRequires: binutils-arm-linux-gnu

%description cross-arm
This package provides a cross-compiler for building Free Pascal applications
for the arm processor architecture.

%package units-arm-linux
Summary: Free Pascal Compiler - units for arm-linux
Requires: %{name}-cross-arm%{?_isa} = %{version}-%{release}

%description units-arm-linux
This package provides pre-compiled unit files for developing Free Pascal
applications for Linux (arm processor architecture). It includes
the runtime library (RTL) and the free component library (FCL).
%endif

%if 0%{?cross_aarch64}
%package cross-aarch64
Summary: Free Pascal Compiler - aarch64 cross-compiler
Requires: %{name}%{?_isa} = %{version}-%{release}
Recommends: %{name}-units-aarch64-linux%{?_isa} = %{version}-%{release}

Requires: binutils-aarch64-linux-gnu
BuildRequires: binutils-aarch64-linux-gnu

%description cross-aarch64
This package provides a cross-compiler for building Free Pascal applications
for the aarch64 processor architecture.

%package units-aarch64-linux
Summary: Free Pascal Compiler - units for aarch64-linux
Requires: %{name}-cross-aarch64%{?_isa} = %{version}-%{release}

%description units-aarch64-linux
This package provides pre-compiled unit files for developing Free Pascal
applications for Linux (aarch64 processor architecture). It includes
the runtime library (RTL) and the free component library (FCL).
%endif

%if 0%{?cross_i386}
%package cross-i386
Summary: Free Pascal Compiler - i386 cross-compiler
Requires: %{name}%{?_isa} = %{version}-%{release}
Recommends: %{name}-units-i386-linux%{?_isa} = %{version}-%{release}

Requires: binutils-x86_64-linux-gnu
BuildRequires: binutils-x86_64-linux-gnu

%description cross-i386
This package provides a cross-compiler for building Free Pascal applications
for the i386 processor architecture.

%package units-i386-linux
Summary: Free Pascal Compiler - units for i386-linux
Requires: %{name}-cross-i386%{?_isa} = %{version}-%{release}

%description units-i386-linux
This package provides pre-compiled unit files for developing Free Pascal
applications for Linux (i386 processor architecture). It includes
the runtime library (RTL) and the free component library (FCL).
%endif

%if 0%{?cross_ppc64le}
%package cross-powerpc64
Summary: Free Pascal Compiler - powerpc64 cross-compiler
Requires: %{name}%{?_isa} = %{version}-%{release}
Recommends: %{name}-units-powerpc64-linux%{?_isa} = %{version}-%{release}

Requires: binutils-powerpc64le-linux-gnu
BuildRequires: binutils-powerpc64le-linux-gnu

%description cross-powerpc64
This package provides a cross-compiler for building Free Pascal applications
for the powerpc64 processor architecture.

%package units-powerpc64-linux
Summary: Free Pascal Compiler - units for powerpc64-linux
Requires: %{name}-cross-powerpc64%{?_isa} = %{version}-%{release}

%description units-powerpc64-linux
This package provides pre-compiled unit files for developing Free Pascal
applications for Linux (powerpc64 processor architecture). It includes
the runtime library (RTL) and the free component library (FCL).
%endif

%if 0%{?cross_x86_64}
%package cross-x86_64
Summary: Free Pascal Compiler - x86_64 cross-compiler
Requires: %{name}%{?_isa} = %{version}-%{release}
Recommends: %{name}-units-x86_64-linux%{?_isa} = %{version}-%{release}

Requires: binutils-x86_64-linux-gnu
BuildRequires: binutils-x86_64-linux-gnu

%description cross-x86_64
This package provides a cross-compiler for building Free Pascal applications
for the x86_64 processor architecture.

%package units-x86_64-linux
Summary: Free Pascal Compiler - units for x86_64-linux
Requires: %{name}-cross-x86_64%{?_isa} = %{version}-%{release}

%description units-x86_64-linux
This package provides pre-compiled unit files for developing Free Pascal
applications for Linux (x86_64 processor architecture). It includes
the runtime library (RTL) and the free component library (FCL).
%endif

# -- MS Windows units

%if 0%{?cross_win32}
%package units-i386-win32
Summary: Free Pascal Compiler - units for i386-win32
%ifarch %{ix86}
Requires: %{name}%{?_isa} = %{version}-%{release}
%else
Requires: %{name}-cross-i386%{?_isa} = %{version}-%{release}
%endif

%description units-i386-win32
This package provides pre-compiled unit files for developing Free Pascal
applications for MS Windows (i386 processor architecture). It includes
the runtime library (RTL) and the free component library (FCL).
%endif

%if 0%{?cross_win64}
%package units-x86_64-win64
Summary: Free Pascal Compiler - units for x86_64-win64
%ifarch x86_64
Requires: %{name}%{?_isa} = %{version}-%{release}
%else
Requires: %{name}-cross-x86_64%{?_isa} = %{version}-%{release}
%endif

%description units-x86_64-win64
This package provides pre-compiled unit files for developing Free Pascal
applications for MS Windows (x86_64 processor architecture). It includes
the runtime library (RTL) and the free component library (FCL).
%endif

# -- Other sub-packages

%package ide
Summary: Free Pascal Compiler - terminal-based IDE
Requires: %{name}-%{units_native}%{?_isa} = %{version}-%{release}
Requires: gpm
Requires: ncurses

%description ide
The fpc-ide package provides "fp", the official terminal-based IDE
for the Free Pascal Compiler.

%package doc
Summary: Free Pascal Compiler - documentation and examples

%description doc
The fpc-doc package contains the documentation (in pdf format) and examples
of Free Pascal.

%package src
Summary:   Free Pascal Compiler - sources
BuildArch: noarch

%description src
The fpc-src package contains the sources of Free Pascal, for documentation or
automatical-code generation purposes.


%global smart _smart
%global fpmakeopt %{?_smp_build_ncpus:--threads=%{_smp_build_ncpus}}
%global fpcopt -gl -gw -k--build-id


%prep
%setup -n fpcbuild-%{archive_suffix} -q

%if 0%{?bootstrap}
unzip %{SOURCE100}
%endif

pushd fpcsrc
%patch -P0
%patch -P1
%patch -P5 -p1
%patch -P6 -p2
%patch -P8 -p1
%patch -P9 -p1
popd


%build
# The source-files:
mkdir -p fpc_src
cp -a fpcsrc/rtl fpc_src
cp -a fpcsrc/packages fpc_src

# Remove some unused units
rm -rf fpc_src/packages/amunits/    # Amiga (Motorola 64k CPU)
rm -rf fpc_src/packages/arosunits/  # AROS
rm -rf fpc_src/packages/morphunits/ # MorphOS
rm -rf fpc_src/packages/os2units/   # OS/2
rm -rf fpc_src/packages/os4units/   # Amiga OS4
rm -rf fpc_src/packages/palmunits/  # PalmOS
rm -rf fpc_src/packages/tosunits/   # Atari TOS/GEM
rm -rf fpc_src/packages/winceunits/ # MS Windows CE


%if 0%{?bootstrap}
STARTPP=$(pwd)/fpc-%{version_code}-bin/%{native_ppc}-%{version_code}-bootstrap
%else
STARTPP=%{native_ppc}
%endif

function build_fpcross() {
	TARGET_ARCH="$1"
	TARGET_OPTS="$2"
	TARGET_BINUTILS="$3"

	make compiler_cycle \
		FPC=${NEWPP} OPT='%{fpcopt}' FPMAKEOPT='%{fpmakeopt}' NoNativeBinaries=1 \
		CROSSOPT="${TARGET_OPTS}" CPU_TARGET="${TARGET_ARCH}" BINUTILSPREFIX="${TARGET_BINUTILS}"
}

function build_units() {
	TARGET_ARCH="$1"
	TARGET_OPTS="$2"
	TARGET_BINUTILS="$3"
	TARGET_PPCROSS="$4"
	TARGET_SYSTEM="$5"

	# No -j here as it has no effect. Parallel compilation is controlled via FPMAKEOPT
	if [[ "${TARGET_ARCH}" == "%{native_arch}" ]]; then
		make rtl%{smart} \
			FPC=${NEWPP} OPT="%{fpcopt} ${TARGET_OPTS}" FPMAKEOPT='%{fpmakeopt}' OS_TARGET="${TARGET_SYSTEM}"
		make packages%{smart} \
			FPC=${NEWPP} OPT="%{fpcopt} ${TARGET_OPTS}" FPMAKEOPT='%{fpmakeopt} --NoIDE=1' OS_TARGET="${TARGET_SYSTEM}"
	else
		TARGET_PPCROSS="$(pwd)/compiler/${TARGET_PPCROSS}"
		make rtl%{smart} \
			FPC="${TARGET_PPCROSS}" OPT='%{fpcopt}' FPMAKEOPT='%{fpmakeopt}' \
			CROSSOPT="${TARGET_OPTS}" CPU_TARGET="${TARGET_ARCH}" OS_TARGET="${TARGET_SYSTEM}" BINUTILSPREFIX="${TARGET_BINUTILS}"
		make packages%{smart} \
			FPC="${TARGET_PPCROSS}" OPT='%{fpcopt}' FPMAKEOPT='%{fpmakeopt} --NoIDE=1' \
			CROSSOPT="${TARGET_OPTS}" CPU_TARGET="${TARGET_ARCH}" OS_TARGET="${TARGET_SYSTEM}" BINUTILSPREFIX="${TARGET_BINUTILS}"
	fi
}

NEWPP=$(pwd)/fpcsrc/compiler/%{native_ppc}
DATA2INC=$(pwd)/fpcsrc/utils/data2inc

# -- Native compiler & units

pushd fpcsrc
make compiler_cycle FPC=${STARTPP} OPT='%{fpcopt} %{native_opts}'

# Clean the run-time library files to force a rebuild with the new compiler
make rtl_clean

make rtl%{smart}      FPC=${NEWPP} OPT='%{fpcopt} %{native_opts}' FPMAKEOPT='%{fpmakeopt}'
make packages%{smart} FPC=${NEWPP} OPT='%{fpcopt} %{native_opts}' FPMAKEOPT='%{fpmakeopt}'
make utils_all        FPC=${NEWPP} OPT='%{fpcopt} %{native_opts}' FPMAKEOPT='%{fpmakeopt}' DATA2INC=${DATA2INC}
popd

# -- Cross-compilers

# ! DIRTY HACK !
# Building units for non-Linux OSes in the same directory as the native ones
# seems to mess up the build process somehow, causing rpmbuild to reject
# the resulting packages due to missing build-ids.
#
# Create a copy of the fpcsrc directory (containing compiler sources,
# but also the native compiler we've just built) and perform all work
# related to cross-compilation inside this copy.
cp -a fpcsrc fpcsrc-cross
pushd fpcsrc-cross

%if 0%{?cross_arm}
	build_fpcross '%{arm_arch}' '%{arm_opts}' 'arm-linux-gnu-'
	build_units   '%{arm_arch}' '%{arm_opts}' 'arm-linux-gnu-' '%{arm_ppcross}' linux
%endif
%if 0%{?cross_aarch64}
	build_fpcross '%{aarch64_arch}' '%{aarch64_opts}' 'aarch64-linux-gnu-'
	build_units   '%{aarch64_arch}' '%{aarch64_opts}' 'aarch64-linux-gnu-' '%{aarch64_ppcross}' linux
%endif
%if 0%{?cross_i386}
	build_fpcross '%{i386_arch}' '%{i386_opts}' 'x86_64-linux-gnu-'
	build_units   '%{i386_arch}' '%{i386_opts}' 'x86_64-linux-gnu-' '%{i386_ppcross}' linux
%endif
%if 0%{?cross_ppc64le}
	build_fpcross '%{ppc64le_arch}' '%{ppc64le_opts}' 'powerpc64le-linux-gnu-'
	build_units   '%{ppc64le_arch}' '%{ppc64le_opts}' 'powerpc64le-linux-gnu-' '%{ppc64le_ppcross}' linux
%endif
%if 0%{?cross_x86_64}
	build_fpcross '%{x86_64_arch}' '%{x86_64_opts}' 'x86_64-linux-gnu-'
	build_units   '%{x86_64_arch}' '%{x86_64_opts}' 'x86_64-linux-gnu-' '%{x86_64_ppcross}' linux
%endif

%if 0%{?cross_win32}
	build_units '%{i386_arch}' '%{i386_opts}' 'x86_64-linux-gnu-' '%{i386_ppcross}' win32
%endif
%if 0%{?cross_win64}
	build_units '%{x86_64_arch}' '%{x86_64_opts}' 'x86_64-linux-gnu-' '%{x86_64_ppcross}' win64
%endif

popd

# -- Documentation

# Output is redirected to /dev/null as building the PDFs produces a gargantuan
# number of warnings, bloating persistent logs and making local development
# tedious due exceeding terminal scrollback buffers.
#
# FIXME: -j1 as there is a race - seen on "missing" `rtl.xct'.
make -j1 -C fpcdocs pdf FPC=${NEWPP} >/dev/null 2>/dev/null


%install
NEWPP="$(pwd)/fpcsrc/compiler/%{native_ppc}"
NEWFPCMAKE="$(pwd)/fpcsrc/utils/fpcm/bin/%{native_arch}-linux/fpcmake"
INSTALLOPTS="-j1 FPC=${NEWPP} FPCMAKE=${NEWFPCMAKE} \
                INSTALL_PREFIX=%{buildroot}%{_prefix} \
                INSTALL_LIBDIR=%{buildroot}%{_libdir} \
                INSTALL_BASEDIR=%{buildroot}%{_libdir}/%{name}/%{version_code} \
                CODPATH=%{buildroot}%{_libdir}/%{name}/lexyacc \
                INSTALL_DOCDIR=%{buildroot}%{_defaultdocdir}/%{name} \
                INSTALL_BINDIR=%{buildroot}%{_bindir}
                INSTALL_EXAMPLEDIR=%{buildroot}%{_defaultdocdir}/%{name}/examples"

function install_compiler() {
	TARGET_ARCH="$1"
	TARGET_COMPILER="$2"

	if [[ "${TARGET_ARCH}" == "%{native_arch}" ]]; then
		make compiler_distinstall ${INSTALLOPTS}
	else
		make compiler_distinstall CROSSINSTALL=1 CPU_TARGET="${TARGET_ARCH}" ${INSTALLOPTS}
	fi

	ln -srf "%{buildroot}/%{_libdir}/%{name}/%{version_code}/${TARGET_COMPILER}" "%{buildroot}%{_bindir}/${TARGET_COMPILER}"
}

function install_units() {
	TARGET_ARCH="$1"
	TARGET_SYSTEM="$2"

	if [[ "${TARGET_ARCH}" == "%{native_arch}" ]]; then
		make rtl_distinstall      OS_TARGET="${TARGET_SYSTEM}" ${INSTALLOPTS}
		make packages_distinstall OS_TARGET="${TARGET_SYSTEM}" ${INSTALLOPTS} FPMAKEOPT='--NoIDE=1'
	else
		make rtl_distinstall      CROSSINSTALL=1 CPU_TARGET="${TARGET_ARCH}" OS_TARGET="${TARGET_SYSTEM}" ${INSTALLOPTS}
		make packages_distinstall CROSSINSTALL=1 CPU_TARGET="${TARGET_ARCH}" OS_TARGET="${TARGET_SYSTEM}" ${INSTALLOPTS} FPMAKEOPT='--NoIDE=1'
	fi
}

# -- Native compiler

pushd fpcsrc
install_compiler '%{native_arch}' '%{native_ppc}'
make rtl_distinstall      ${INSTALLOPTS}
make packages_distinstall ${INSTALLOPTS}
make utils_distinstall    ${INSTALLOPTS}
popd

# -- Cross-compilers

pushd fpcsrc-cross

%if 0%{?cross_arm}
	install_compiler '%{arm_arch}' '%{arm_ppcross}'
	install_units    '%{arm_arch}' linux
%endif
%if 0%{?cross_aarch64}
	install_compiler '%{aarch64_arch}' '%{aarch64_ppcross}'
	install_units    '%{aarch64_arch}' linux
%endif
%if 0%{?cross_i386}
	install_compiler '%{i386_arch}' '%{i386_ppcross}'
	install_units    '%{i386_arch}' linux
%endif
%if 0%{?cross_ppc64le}
	install_compiler '%{ppc64le_arch}' '%{ppc64le_ppcross}'
	install_units    '%{ppc64le_arch}' linux
%endif
%if 0%{?cross_x86_64}
	install_compiler '%{x86_64_arch}' '%{x86_64_ppcross}'
	install_units    '%{x86_64_arch}' linux
%endif

%if 0%{?cross_win32}
	install_units '%{i386_arch}' win32
%endif
%if 0%{?cross_win64}
	install_units '%{x86_64_arch}' win64
%endif

popd

# -- Other

pushd install
make -C doc ${INSTALLOPTS}
make -C man ${INSTALLOPTS} INSTALL_MANDIR=%{buildroot}%{_mandir}
popd

make -C fpcdocs pdfinstall ${INSTALLOPTS}

# Remove the version-number from the documentation-directory
mv %{buildroot}%{_defaultdocdir}/%{name}-%{version_code}/* %{buildroot}%{_defaultdocdir}/%{name}
rmdir %{buildroot}%{_defaultdocdir}/%{name}-%{version_code}

# Create a version independent compiler-configuration file with build-id
# enabled by default. For this purpose some non-default templates are used.
# So the samplecfg script could not be used and fpcmkcfg is called directly.
%{buildroot}%{_bindir}/fpcmkcfg -p -t %{SOURCE10} \
	-d "libdir=%{_libdir}" \
	-d "sharedir=%{_datadir}" \
	-o %{buildroot}%{_sysconfdir}/fpc.cfg
# Create the IDE configuration files
%{buildroot}%{_bindir}/fpcmkcfg -p -1 -d "basepath=%{_libdir}/%{name}/\$fpcversion" -o %{buildroot}%{_libdir}/%{name}/%{version_code}/ide/text/fp.cfg
%{buildroot}%{_bindir}/fpcmkcfg -p -2 -o %{buildroot}%{_libdir}/%{name}/%{version_code}/ide/text/fp.ini
# Create the fppkg configuration files
%{buildroot}%{_bindir}/fpcmkcfg -p -t %{SOURCE11} -d CompilerConfigDir=%{_sysconfdir}/fppkg -d arch=%{_arch} -o %{buildroot}%{_sysconfdir}/fppkg.cfg
%{buildroot}%{_bindir}/fpcmkcfg -p -t %{SOURCE12} -d fpcbin=%{_bindir}/fpc -d GlobalPrefix=%{_exec_prefix} -d lib=%{_lib} -o %{buildroot}%{_sysconfdir}/fppkg/default_%{_arch}

# Include the COPYING-information for the compiler/rtl/fcl in the documentation
cp -a fpcsrc/compiler/COPYING.txt %{buildroot}%{_defaultdocdir}/%{name}/COPYING
cp -a fpcsrc/rtl/COPYING.txt %{buildroot}%{_defaultdocdir}/%{name}/COPYING.rtl
cp -a fpcsrc/rtl/COPYING.FPC %{buildroot}%{_defaultdocdir}/%{name}/COPYING.FPC

# The source-files:
mkdir -p %{buildroot}%{_datadir}/fpcsrc
cp -a fpc_src/* %{buildroot}%{_datadir}/fpcsrc/

# Workaround:
# newer rpm versions do not allow garbage
# delete lexyacc (The hardcoded library path is necessary because 'make
# install' places this file hardcoded at usr/lib)
rm -rf %{buildroot}/usr/lib/%{name}/lexyacc


%files
%{_bindir}/*
%exclude %{_bindir}/ppcross*
%{_libdir}/%{name}
%{_libdir}/libpas2jslib.so*
%exclude %{_libdir}/%{name}/%{version_code}/ppcross*
%config(noreplace) %{_sysconfdir}/%{name}.cfg
%config(noreplace) %{_sysconfdir}/fppkg.cfg
%config(noreplace) %{_sysconfdir}/fppkg/default_%{_arch}
%dir %{_defaultdocdir}/%{name}/
%doc %{_defaultdocdir}/%{name}/NEWS
%doc %{_defaultdocdir}/%{name}/README
%doc %{_defaultdocdir}/%{name}/faq*
%license %{_defaultdocdir}/%{name}/COPYING*
%{_mandir}/*/*
# Exclude units
%exclude %{_libdir}/%{name}/%{version_code}/fpmkinst/
%exclude %{_libdir}/%{name}/%{version_code}/units/
# Exclude IDE-specific files
%exclude %{_bindir}/fp
%exclude %{_bindir}/fp.rsj
%exclude %{_libdir}/%{name}/%{version_code}/fpmkinst/%{native_arch}-linux/ide.fpm
%exclude %{_libdir}/%{name}/%{version_code}/ide
%exclude %{_mandir}/man1/fp.1*

# -- Native units

%files %{units_native}
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/%{version_code}/
%dir %{_libdir}/%{name}/%{version_code}/fpmkinst/
%dir %{_libdir}/%{name}/%{version_code}/units/
%{_libdir}/%{name}/%{version_code}/fpmkinst/%{native_arch}-linux/
%{_libdir}/%{name}/%{version_code}/units/%{native_arch}-linux/
# Don't forget about the IDE
%exclude %{_libdir}/%{name}/%{version_code}/fpmkinst/%{native_arch}-linux/ide.fpm

# -- Cross-compilers

%if 0%{?cross_arm}
%files cross-arm
%{_bindir}/%{arm_ppcross}
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/%{version_code}/
     %{_libdir}/%{name}/%{version_code}/%{arm_ppcross}

%files units-arm-linux
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/%{version_code}/
%dir %{_libdir}/%{name}/%{version_code}/units/
%{_libdir}/%{name}/%{version_code}/units/%{arm_arch}-linux/
%endif

%if 0%{?cross_aarch64}
%files cross-aarch64
%{_bindir}/%{aarch64_ppcross}
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/%{version_code}/
     %{_libdir}/%{name}/%{version_code}/%{aarch64_ppcross}

%files units-aarch64-linux
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/%{version_code}/
%dir %{_libdir}/%{name}/%{version_code}/units/
%{_libdir}/%{name}/%{version_code}/units/%{aarch64_arch}-linux/
%endif

%if 0%{?cross_i386}
%files cross-i386
%{_bindir}/%{i386_ppcross}
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/%{version_code}/
     %{_libdir}/%{name}/%{version_code}/%{i386_ppcross}

%files units-i386-linux
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/%{version_code}/
%dir %{_libdir}/%{name}/%{version_code}/units/
%{_libdir}/%{name}/%{version_code}/units/%{i386_arch}-linux/
%endif

%if 0%{?cross_ppc64le}
%files cross-powerpc64
%{_bindir}/%{ppc64le_ppcross}
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/%{version_code}/
     %{_libdir}/%{name}/%{version_code}/%{ppc64le_ppcross}

%files units-powerpc64-linux
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/%{version_code}/
%dir %{_libdir}/%{name}/%{version_code}/units/
%{_libdir}/%{name}/%{version_code}/units/%{ppc64le_arch}-linux/
%endif

%if 0%{?cross_x86_64}
%files cross-x86_64
%{_bindir}/%{x86_64_ppcross}
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/%{version_code}/
     %{_libdir}/%{name}/%{version_code}/%{x86_64_ppcross}

%files units-x86_64-linux
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/%{version_code}/
%dir %{_libdir}/%{name}/%{version_code}/units/
%{_libdir}/%{name}/%{version_code}/units/%{x86_64_arch}-linux/
%endif

# -- MS Windows units

%if 0%{?cross_win32}
%files units-i386-win32
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/%{version_code}/
%dir %{_libdir}/%{name}/%{version_code}/units/
%{_libdir}/%{name}/%{version_code}/units/%{i386_arch}-win32/
%endif

%if 0%{?cross_win64}
%files units-x86_64-win64
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/%{version_code}/
%dir %{_libdir}/%{name}/%{version_code}/units/
%{_libdir}/%{name}/%{version_code}/units/%{x86_64_arch}-win64/
%endif

# -- Others

%files ide
%{_bindir}/fp
%{_bindir}/fp.rsj
%{_libdir}/%{name}/%{version_code}/fpmkinst/%{native_arch}-linux/ide.fpm
%{_libdir}/%{name}/%{version_code}/ide
%{_mandir}/man1/fp.1*

%files doc
%dir %{_defaultdocdir}/%{name}/
%doc %{_defaultdocdir}/%{name}/*.pdf
%doc %{_defaultdocdir}/%{name}/*/*

%files src
%{_datadir}/fpcsrc


%changelog
* Sun Aug 17 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 3.2.4~rc1-1
- Update to v3.2.4~rc1

* Sat Aug 02 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 3.2.2-20
- Add cross-compilers
- Add MS Windows units

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat May 10 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 3.2.2-18
- Fix Patch9 causing internal compiler errors

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 14 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 3.2.2-16
- Convert License tag to SPDX
- Add a patch to make generated code fallback to localhost if no DNS servers are specified
- Add a patch to fix symbols being wrongly marked as unused

* Sat Jul 27 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 3.2.2-15
- Add a patch to fix broken stack trace handling on aarch64

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 18 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 3.2.2-9
- Add a patch to fix docs failing to build with Texlive 2022

* Tue Jan 17 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 3.2.2-8
- Move the TUI IDE to a subpackage
- Add a patch to fix IDE-related non-executable files being installed to /usr/bin
- Move units to a separate sub-package
- Use FPMAKEOPT for parallel compilation
- Remove some non-Linux units from the "fpc-src" subpackage

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Mar 16 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 3.2.2-6
- Add a patch to fix pas2jni failing to run properly

* Mon Feb 07 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 3.2.2-5
- Add a patch to fix linking errors on ppc64le

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 21 2021 Dan Horák <dan[at]danny.cz> - 3.2.2-3
- Update for new glibc >= 2.34

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 3.2.2-1
- Update to v3.2.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 20 2020 Artur Iwicki <fedora@svgames.pl> - 3.2.0-1
- Update to v3.2.0 (official release - no longer using SVN snapshots)
- Drop Patch3 (missing consts - merged upstream)

* Wed Jun 03 2020 Artur Iwicki <fedora@svgames.pl> - 3.2.0-0.20200530svn45533.1
- Update to latest upstream SVN revision

* Mon May 04 2020 Artur Iwicki <fedora@svgames.pl> - 3.2.0-0.20200503svn45235.1
- Update to latest upstream SVN revision

* Sun Apr 12 2020 Artur Iwicki <fedora@svgames.pl> - 3.2.0-0.20200410svn44680.1
- Update to latest upstream SVN revision

* Sat Mar 28 2020 Artur Iwicki <fedora@svgames.pl> - 3.2.0-0.20200327svn44375.1
- Update to latest upstream SVN revision

* Mon Mar 16 2020 Artur Iwicki <fedora@svgames.pl> - 3.2.0-0.20200314svn44301.1
- Update to latest upstream SVN revision

* Mon Feb 24 2020 Artur Iwicki <fedora@svgames.pl> - 3.2.0-0.20200222svn44232.1
- Update to latest upstream SVN revision

* Wed Feb 12 2020 Artur Iwicki <fedora@svgames.pl> - 3.2.0-0.20200212svn44160.1
- Update to latest upstream SVN revision

* Sat Feb 08 2020 Artur Iwicki <fedora@svgames.pl> - 3.2.0-0.20200203svn44109.1
- Update to latest upstream SVN revision

* Sun Feb 02 2020 Artur Iwicki <fedora@svgames.pl> - 3.2.0-0.20200202svn44092.5
- Update to latest upstream SVN revision

* Sat Feb 01 2020 Artur Iwicki <fedora@svgames.pl> - 3.2.0-0.20200130svn44069.4
- Unmark the aarch64 build as requiring bootstrap
- Update to latest upstream SVN revision

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-0.20200122svn44016.3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 28 2020 Artur Iwicki <fedora@svgames.pl> - 3.2.0-0.20200122svn44016.3
- Bootstrap the compiler for aarch64

* Mon Jan 27 2020 Artur Iwicki <fedora@svgames.pl> - 3.2.0-0.20200122svn44016.2
- Bootstrap the compiler for ppc64le

* Sun Jan 26 2020 Artur Iwicki <fedora@svgames.pl> - 3.2.0-0.20200122svn44016.1
- Update to latest upstream SVN revision
- Drop r1448 and r38400 patches (backports from upstream)

* Sat Dec 21 2019 Artur Iwicki <fedora@svgames.pl> - 3.0.4-8
- Allow for reproducible builds by honoring the SOURCE_DATE_EPOCH variable
  (patch imported from Debian)
- Mark the fpc-src package as noarch

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Artur Iwicki <fedora@svgames.pl> - 3.0.4-5
- Add BuildRequires: for glibc-devel

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 03 2018 Richard Shaw <hobbes1069@gmail.com> - 3.0.4-2
- Add patch to fix assembly alignment code, fixes #1526848.

* Thu Mar 01 2018 Joost van der Sluis <joost@cnoc.nl> - 3.0.4-1
- Generate Dwarf debug by default on 32-bit targets (rhbz#1475223)
- Use the %%license macro instead of %%doc for licence files

* Fri Feb 09 2018 Joost van der Sluis <joost@cnoc.nl> - 3.0.4-1
- Upgrade to upstream release 3.0.4.
- Generate Dwarf- instead of Stabs-debuginfo on i686 and ARMHF
- Force armhf on arm-architectures

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 18 2017 Joost van der Sluis <joost@cnoc.nl> - 3.0.2-1
- Upgrade to upstream release 3.0.2.
- Attempt to fix race-problem during compiler-compilation on ARM

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 4 2017 Joost van der Sluis <joost@cnoc.nl> - 3.0.0-5
- Drop powerpc64-arm binary added for bootstrapping on powerpc64,
  completing the bootstrap procedure

* Mon Jan 30 2017 Joost van der Sluis <joost@cnoc.nl> - 3.0.0-4
- Bootstrap ppc64 using cross-compiled compiler binary

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Joost van der Sluis <joost@cnoc.nl> - 3.0.0-2
- Drop fpc-arm binary added for bootstrapping on ARM, completing the
  bootstrap procedure

* Sat Jan 9 2016 Joost van der Sluis <joost@cnoc.nl> - 3.0.0-1
- Upgrade to upstream release 3.0.0.
- Bootstrap ARM using cross-compiled armhl binaries, because the
  (patched) 2.6.4-ARM compiler in the repository is not able to compile the
  3.0.0 release.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Mar 7 2015 Joost van der Sluis <joost@cnoc.nl> - 2.6.4-1
- Upgrade to upstream release 2.6.4.

* Tue Jan 20 2015 Dan Horák <dan[at]danny.cz> - 2.6.2-7
- switch to ExclusiveArch

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 08 2013 Hans de Goede <hdegoede@redhat.com> - 2.6.2-4
- Drop fpc binaries added to the src.rpm for bootstrapping on ARM, completing
  the boostrap procedure (rhbz#992285)

* Thu Aug 08 2013 Hans de Goede <hdegoede@redhat.com> - 2.6.2-3
- Bootstrap for arm using Debian fpc-2.6.2 armhf binaries (rhbz#992285)
- Use an unversioned docdir (rhbz#993758)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 24 2013 Joost van der Sluis <joost@cnoc.nl> - 2.6.2-1
- Upgrade to upstream release 2.6.2.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 24 2012 Bruno Wolff III <bruno@wolff.to> - 2.6.2-0.1.rc1
- Use standard versioning, so non-rc versions will be higher
- Fix issue with some things using 'rc1' appended to version name and others not

* Sat Nov 3 2012 Joost van der Sluis <joost@cnoc.nl> - 2.6.2rc1-1
- Upgrade to upstream release 2.6.2rc1.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 14 2012 Karsten Hopp <karsten@redhat.com> 2.6.0-2
- define ppcname on ppc64

* Fri Jan 27 2012 Joost van der Sluis <joost@cnoc.nl> - 2.6.0-1
- Upgrade to upstream release 2.6.0.
- Do not use samplecfg for generating the configuration files anymore, but
  call fpcmkcfg directly.
- Changed the name of the project from Freepascal to Free Pascal

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 5 2011 Joost van der Sluis <joost@cnoc.nl> - 2.4.2-1
- Upgrade to upstream release 2.4.2.

* Sat Oct 23 2010 Joost van der Sluis <joost@cnoc.nl> - 2.4.2-0.1.rc1
- Upgrade to upstream release 2.4.2rc1.

* Wed May  5 2010 Joost van der Sluis <joost@cnoc.nl> - 2.4.0-1.fc14
- Drop fpc-2.2.4-stackexecute.patch since bug was fixed in 2.4.0

* Tue May  4 2010 Jan Kratochvil <jan.kratochvil@redhat.com> - 2.4.0-0.fc14
- Upgrade to upstream release 2.4.0.
  - Drop fpc-2.2.4-r12475.patch as present in 2.4.0.
- Base the .spec build on upstream released archive (fpcbuild-2.4.0.tar.gz).
- Remove the obsolete .spec BuildRoot tag.
- Remove BuildRequires for binutils and glibc-devel as guaranteed as always
  provided in Fedora Packaging Guidlines.
- Remove Requires glibc as guaranteed on a Fedora system.
- Add %%{?_smp_mflags} and -j1 appropriately, applied one -j1 workaround.
- Change {compiler,rtl}/COPYING to COPYING.txt.

* Tue Oct 6 2009 Joost van der Sluis <joost@cnoc.nl> 2.2.4-4
- fixed procvar parameter passing on ppc/sysv (by value instead of by
  reference -- except for method procvars, for tmethod record compatibility) 

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 18 2009 Dan Horak <dan[at]danny.cz> 2.2.4-2
- Exclude s390/s390x architectures

* Sun Apr 19 2009 Joost van der Sluis <joost@cnoc.nl> 2.2.4-1
- Updated to version 2.2.4

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Oct 25 2008 Joost van der Sluis <joost@cnoc.nl> 2.2.2-3
- Do not distribute the RTL and packages with debug-info included
- Fix the location of the fpc-binary in the samplecfg script

* Sun Oct 19 2008 Joost van der Sluis <joost@cnoc.nl> 2.2.2-2
- Pass -z noexecstack to the linker from within the configuration file fpc.cfg (fpc-bug #11563)
- Added patch to fix fpc-bug #11837 for usage with newer gtk2-versions

* Wed Aug 13 2008 Joost van der Sluis <joost@cnoc.nl> 2.2.2-1
- Updated to version 2.2.2
- Disabled debuginfo for ppc64 again
- Detect 32 or 64 bit compilation in the configuration file fpc.cfg

* Sun Jun 22 2008 Joost van der Sluis <joost@cnoc.nl> 2.2.2rc1-1
- Updated to version 2.2.2rc1
- Enabled debuginfo for ppc64 again
- Do not strip the debugdata on x86_64 anymore
- Packages_base, packages_fcl and packages_extra are merged into packages
- Don't install packages_fv separately anymore
- Fix for incorrect path in official fpc 2.2.2rc1-sourcefile
- Updated licence-tag from "GPL and modified LGPL" to fedora-tag "GPLv2+ and LGPLv2+ with exceptions"
- Removed UsePrebuildcompiler define for ppc64

* Wed Apr 16 2008 Joost van der Sluis <joost@cnoc.nl> 2.2.0-12
- Fix for DWARF-debug generation - fixes some more build problems on x86_64 and F9, bugzilla 337051

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.2.0-11
- Autorebuild for GCC 4.3

* Tue Oct 16 2007 Joost van der Sluis <joost@cnoc.nl> 2.2.0-10
- Strip the debuginfo from grab_vcsa and ppudump, since debugedit chokes on it
- Only strip debugdata on x86_64

* Tue Oct 16 2007 Joost van der Sluis <joost@cnoc.nl> 2.2.0-9
- Strip the debuginfo from mkxmlrpc, since debugedit chokes on it

* Tue Oct 16 2007 Joost van der Sluis <joost@cnoc.nl> 2.2.0-8
- Strip the debuginfo from h2pas, since debugedit chokes on it

* Tue Oct 16 2007 Joost van der Sluis <joost@cnoc.nl> 2.2.0-7
- Include the startcompiler on all targets, for the srpm-building

* Tue Oct 16 2007 Joost van der Sluis <joost@cnoc.nl> 2.2.0-6
- Disabled debuginfo for ppc64 only
- Enabled smart-linking on ppc64
- Added a patch for building documentation without fpc already installed

* Tue Oct 16 2007 Joost van der Sluis <joost@cnoc.nl> 2.2.0-5
- Disabled debuginfo

* Tue Oct 16 2007 Joost van der Sluis <joost@cnoc.nl> 2.2.0-4
- Enabled BuildId, added it to fpc.cfg

* Tue Oct 16 2007 Joost van der Sluis <joost@cnoc.nl> 2.2.0-3
- Disabled smart-linking on ppc64

* Tue Oct 16 2007 Joost van der Sluis <joost@cnoc.nl> 2.2.0-2
- Buildrequirement fpc is not needed when using a pre-built compiler binary

* Sun Oct 14 2007 Joost van der Sluis <joost@cnoc.nl> 2.2.0-1
- Updated to version 2.2.0
- Updated description
- Enabled smart-linking for ppc
- Do not include the built binary-files in fpc-src
- Added support for ppc64
- Added support to configuration file for dual 32/64 bit installations
- Fixed and enabled debug-package 

* Sat Sep 16 2006 Joost van der Sluis <joost@cnoc.nl> 2.0.4-2
- Fixed documentation building on powerpc

* Fri Sep 15 2006 Joost van der Sluis <joost@cnoc.nl> 2.0.4-1
- Updated to version 2.0.4

* Wed Mar 1 2006 Joost van der Sluis <joost@cnoc.nl> 2.0.2-4
- Rebuild for Fedora Extras 5

* Tue Dec 20 2005 Joost van der Sluis <joost@cnoc.nl> 2.0.2-3
- Disabled smart-linking for ppc

* Tue Dec 20 2005 Joost van der Sluis <joost@cnoc.nl> 2.0.2-2
- Updated fpc-2.0.2-G5.patch

* Tue Dec 20 2005 Joost van der Sluis <joost@cnoc.nl> 2.0.2-1
- Updated to version 2.0.2

* Wed Aug 17 2005 Joost van der Sluis <joost@cnoc.nl> 2.0.0-4
- Added %%{?dist} to release.

* Wed Aug 17 2005 Joost van der Sluis <joost@cnoc.nl> 2.0.0-3
- replaced the ppcpcc-2.1.1 startcompilercompiler for the
  ppcppc-2.0.0 startcompiler 

* Wed Aug 17 2005 Joost van der Sluis <joost@cnoc.nl> 2.0.0-2
- Added a patch for compilation on POWER5, and provided
  the new ppcppc binary/startcompiler

* Fri Aug 5 2005 Joost van der Sluis <joost@cnoc.nl> 2.0.0-1
- Removed gpm-devel requirement
- Fixed a type in the -src description

* Thu Jul 28 2005 Joost van der Sluis <joost@cnoc.nl> 2.0.0-1
- Added some requirements
- Added COPYING-info to %%doc

* Tue Jun 28 2005 Joost van der Sluis <joost@cnoc.nl> 2.0.0-0.6
- Only rtl, fcl and packages are added to src-subpackage
- Silenced post-script
- disabled the debuginfo-package

* Sun Jun 5 2005 Joost van der Sluis <joost@cnoc.nl> 2.0.0-0.5
- Added doc-subpackage
- Added src-subpackage

* Fri Jun 3 2005 Joost van der Sluis <joost@cnoc.nl> 2.0.0-0.4
- New fix for lib64 on x86_64
- small patches from Jens Petersen <petersen@redhat.com>

* Thu May 26 2005 Joost van der Sluis <joost@cnoc.nl> 2.0.0-0.3
- replaced 'lib' and 'lib64' by %%{_lib}

* Tue May 24 2005 Joost van der Sluis <joost@cnoc.nl> 2.0.0-0.2
- Fixed for lib64 on x86_64
- Changed summary, description and license
- Removed examples from installation
- Make clean removed from clean-section
- Clean-up
- replaced $RPM_BUILD_ROOT by %%{buildroot}

* Mon May 23 2005 Joost van der Sluis <joost@cnoc.nl> 2.0.0-0.1
- Initial build.
