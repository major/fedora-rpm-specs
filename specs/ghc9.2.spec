# Start: prod settings
# all *bcond_without* for production builds:
# - performance build (disable for quick build)
%bcond_without perfbuild
%bcond_without build_hadrian
%global with_hadrian 1
%if %{with hadrian}
%bcond_without manual
%endif
# End: prod settings

# not for production builds
%if %{without perfbuild}
# disable profiling libraries (overriding macros.ghc-srpm)
%undefine with_ghc_prof
# disable haddock documentation (overriding macros.ghc-os)
%undefine with_haddock
%endif

%global ghc_major 9.2
%global ghc_name ghc%{ghc_major}

%global Cabal_ver 3.6.3.0
%global mtl_ver 2.2.2
%global transformers_ver 0.5.6.2

%global base_ver 4.16.4.0
%global ghc_bignum_ver 1.2
%global ghc_compact_ver 0.1.0.0
%global hpc_ver 0.6.1.0
%global rts_ver 1.0.2
%global xhtml_ver 3000.2.2.1

# bootstrap needs 8.10+
%global ghcboot_major 9.2
%global ghcboot ghc%{?ghcboot_major}

# https://gitlab.haskell.org/ghc/ghc/-/issues/19754
# https://github.com/haskell/haddock/issues/1384
%ifarch armv7hl %{ix86}
%undefine with_haddock
%endif

%if %{without hadrian}
# locked together since disabling haddock causes no manuals built
# and disabling haddock still created index.html
# https://gitlab.haskell.org/ghc/ghc/-/issues/15190
%{?with_haddock:%bcond_without manual}
%endif

# make sure ghc libraries' ABI hashes unchanged
%bcond_without abicheck

# no longer build testsuite (takes time and not really being used)
%bcond_with testsuite

# ld
%ifnarch riscv64
%bcond ld_gold 1
%else
%bcond ld_gold 0
%endif

# 9.2 needs llvm 9-12
%global llvm_major 12
%if %{with hadrian}
%global ghc_llvm_archs armv7hl s390x
%global ghc_unregisterized_arches s390 %{mips} riscv64
%else
%global ghc_llvm_archs armv7hl
%global ghc_unregisterized_arches s390 s390x %{mips} riscv64
%endif

Name: %{ghc_name}
Version: 9.2.8
# Since library subpackages are versioned:
# - release can only be reset if *all* library versions get bumped simultaneously
#   (sometimes after a major release)
# - minor release numbers for a branch should be incremented monotonically
Release: 28%{?dist}
Summary: Glasgow Haskell Compiler

License: BSD-3-Clause AND HaskellReport
URL: https://haskell.org/ghc/
Source0: https://downloads.haskell.org/ghc/%{version}/ghc-%{version}-src.tar.lz
%if %{with testsuite}
Source1: https://downloads.haskell.org/ghc/%{version}/ghc-%{version}-testsuite.tar.lz
%endif
Source5: ghc-pkg.man
Source6: haddock.man
Source7: runghc.man

# https://bugzilla.redhat.com/show_bug.cgi?id=2142238
ExcludeArch: armv7hl

# absolute haddock path (was for html/libraries -> libraries)
Patch1: ghc-gen_contents_index-haddock-path.patch
Patch2: ghc-Cabal-install-PATH-warning.patch
Patch3: ghc-gen_contents_index-nodocs.patch
# https://fedoraproject.org/wiki/Toolchain/PortingToModernC
# https://gitlab.haskell.org/ghc/ghc/-/merge_requests/9394
Patch4: https://gitlab.haskell.org/ghc/ghc/-/merge_requests/9394.patch
# https://gitlab.haskell.org/ghc/ghc/-/issues/25662
Patch5: hp2ps-C-gnu17.patch

# distutils gone in python 3.12
# https://gitlab.haskell.org/ghc/ghc/-/merge_requests/10922
Patch8: https://gitlab.haskell.org/ghc/ghc/-/merge_requests/10922.patch
# https://gitlab.haskell.org/ghc/ghc/-/issues/23286 (sphinx modern extlinks)
Patch9: https://gitlab.haskell.org/ghc/ghc/-/commit/00dc51060881df81258ba3b3bdf447294618a4de.patch

# https://phabricator.haskell.org/rGHC4eebc8016f68719e1ccdf460754a97d1f4d6ef05
# https://gitlab.haskell.org/ghc/ghc/-/issues/19684
# DerivedConstants.h not produced atomically
Patch10: https://gitlab.haskell.org/ghc/ghc/-/commit/9aace0eaf6279f17368a1753b65afbdc466e8291.patch

# https://gitlab.haskell.org/ghc/ghc/-/merge_requests/10928
# allow building hadrian with Cabal-3.8
Patch11: 10928.patch

# armv7hl patches
Patch12: ghc-armv7-VFPv3D16--NEON.patch

# for unregisterized
# https://gitlab.haskell.org/ghc/ghc/-/issues/15689
Patch15: ghc-warnings.mk-CC-Wall.patch
Patch16: ghc-9.2.1-hadrian-s390x-rts--qg.patch

# s390x
# https://gitlab.haskell.org/ghc/ghc/-/issues/24163
# https://gitlab.haskell.org/ghc/ghc/-/merge_requests/11662
Patch17: https://gitlab.haskell.org/ghc/ghc/-/merge_requests/11662.patch

# bigendian (s390x and ppc64)
# https://gitlab.haskell.org/ghc/ghc/issues/15411
# https://gitlab.haskell.org/ghc/ghc/issues/16505
# https://bugzilla.redhat.com/show_bug.cgi?id=1651448
# https://gitlab.haskell.org/ghc/ghc/-/issues/15914
# https://gitlab.haskell.org/ghc/ghc/issues/16973
# https://bugzilla.redhat.com/show_bug.cgi?id=1733030
# https://gitlab.haskell.org/ghc/ghc/-/issues/16998
Patch18: Disable-unboxed-arrays.patch

# Debian patches:
Patch24: buildpath-abi-stability.patch
Patch26: no-missing-haddock-file-warning.patch
Patch27: haddock-remove-googleapis-fonts.patch

Patch30: https://src.opensuse.org/rpm/ghc/raw/branch/factory/sphinx7.patch

# ppc64le FFI miscompilation
# https://gitlab.haskell.org/ghc/ghc/-/issues/23034
Patch35: https://gitlab.haskell.org/ghc/ghc/-/merge_requests/12885.patch

# https://gitlab.haskell.org/ghc/ghc/-/wikis/platforms

# fedora ghc has been bootstrapped on
# %%{ix86} x86_64 s390x ppc64le aarch64 riscv64
# and previously: alpha sparcv9 armv5tel ppc ppc64 s390 armv7hl
# see also deprecated ghc_arches defined in ghc-srpm-macros
# /usr/lib/rpm/macros.d/macros.ghc-srpm

BuildRequires: %{ghcboot}-compiler > 8.10
# for ABI hash checking
%if %{with abicheck}
BuildRequires: %{name}
%endif
BuildRequires: ghc-rpm-macros-extra
BuildRequires: %{ghcboot}-binary-devel
BuildRequires: %{ghcboot}-bytestring-devel
BuildRequires: %{ghcboot}-containers-devel
BuildRequires: %{ghcboot}-directory-devel
BuildRequires: %{ghcboot}-pretty-devel
BuildRequires: %{ghcboot}-process-devel
BuildRequires: %{ghcboot}-stm-devel
BuildRequires: %{ghcboot}-template-haskell-devel
BuildRequires: %{ghcboot}-transformers-devel
BuildRequires: alex
BuildRequires: binutils%{?with_ld_gold:-gold}
BuildRequires: gmp-devel
BuildRequires: libffi-devel
BuildRequires: lzip
BuildRequires: make
BuildRequires: gcc-c++
# for terminfo
BuildRequires: ncurses-devel
BuildRequires: perl-interpreter
# needed for:
# - binary-dist-dir
# - patch7 and patch12
BuildRequires:  autoconf automake
%if %{with testsuite}
BuildRequires: python3
%endif
%if %{with manual}
BuildRequires: python3-sphinx
%endif
BuildRequires: llvm%{llvm_major}

%if %{with hadrian}
BuildRequires:  happy
%if %{with build_hadrian}
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-shake-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unordered-containers-devel
%else
BuildRequires:  %{name}-hadrian
%endif
%endif

Requires: %{name}-compiler = %{version}-%{release}
Requires: %{name}-devel = %{version}-%{release}
Requires: %{name}-ghc-devel = %{version}-%{release}
Requires: %{name}-ghc-boot-devel = %{version}-%{release}
Requires: %{name}-ghc-compact-devel = %{ghc_compact_ver}-%{release}
Requires: %{name}-ghc-heap-devel = %{version}-%{release}
Requires: %{name}-ghci-devel = %{version}-%{release}
Requires: %{name}-hpc-devel = %{hpc_ver}-%{release}
Requires: %{name}-libiserv-devel = %{version}-%{release}
%if %{with haddock}
Suggests: %{name}-doc = %{version}-%{release}
Suggests: %{name}-doc-index = %{version}-%{release}
%endif
%if %{with manual}
Suggests: %{name}-manual = %{version}-%{release}
%endif
%if %{with ghc_prof}
Suggests: %{name}-prof = %{version}-%{release}
%endif
Recommends: %{name}-compiler-default = %{version}-%{release}

%description
GHC is a state-of-the-art, open source, compiler and interactive environment
for the functional language Haskell. Highlights:

- GHC supports the entire Haskell 2010 language plus a wide variety of
  extensions.
- GHC has particularly good support for concurrency and parallelism,
  including support for Software Transactional Memory (STM).
- GHC generates fast code, particularly for concurrent programs.
  Take a look at GHC's performance on The Computer Language Benchmarks Game.
- GHC works on several platforms including Windows, Mac, Linux,
  most varieties of Unix, and several different processor architectures.
- GHC has extensive optimisation capabilities, including inter-module
  optimisation.
- GHC compiles Haskell code either directly to native code or using LLVM
  as a back-end. GHC can also generate C code as an intermediate target for
  porting to new platforms. The interactive environment compiles Haskell to
  bytecode, and supports execution of mixed bytecode/compiled programs.
- Profiling is supported, both by time/allocation and various kinds of heap
  profiling.
- GHC comes with several libraries, and thousands more are available on Hackage.


%package compiler
Summary: GHC compiler and utilities
License: BSD-3-Clause
Requires: gcc%{?_isa}
Requires: %{name}-base-devel%{?_isa} = %{base_ver}-%{release}
%if %{with haddock}
Requires: %{name}-filesystem = %{version}-%{release}
%else
Obsoletes: %{name}-doc-index < %{version}-%{release}
Obsoletes: %{name}-filesystem < %{version}-%{release}
Obsoletes: %{name}-xhtml < %{xhtml_ver}-%{release}
Obsoletes: %{name}-xhtml-devel < %{xhtml_ver}-%{release}
Obsoletes: %{name}-xhtml-doc < %{xhtml_ver}-%{release}
Obsoletes: %{name}-xhtml-prof < %{xhtml_ver}-%{release}
%endif
%if %{without manual}
Obsoletes: %{name}-manual < %{version}-%{release}
%endif
Requires: binutils%{?with_ld_gold:-gold}
%ifarch %{ghc_llvm_archs}
Requires: llvm%{llvm_major}
%else
Suggests: llvm(major) = %{llvm_major}
%endif

%description compiler
The package contains the GHC compiler, tools and utilities.

The ghc libraries are provided by %{name}-devel.
To install all of ghc (including the ghc library),
install the main ghc package.


%package compiler-default
Summary: Makes %{name} default ghc
Requires: %{name}-compiler%{?_isa} = %{version}-%{release}
Conflicts: ghc-compiler

%description compiler-default
The package contains symlinks to make %{name} the default GHC compiler.


%if %{with haddock} || (%{with hadrian} && %{with manual})
%package doc
Summary: Haskell library documentation meta package
License: BSD-3-Clause

%description doc
Installing this package causes %{name}-*-doc packages corresponding to
%{name}-*-devel packages to be automatically installed too.


%package doc-index
Summary: GHC library documentation indexing
License: BSD-3-Clause
Requires: %{name}-compiler = %{version}-%{release}
# due to disabled haddock archs
#BuildArch: noarch

%description doc-index
The package enables re-indexing of installed library documention.


%package filesystem
Summary: Shared directories for Haskell documentation
# due to disabled haddock archs
#BuildArch: noarch

%description filesystem
This package provides some common directories used for
Haskell libraries documentation.
%endif


%if %{with manual}
%package manual
Summary: GHC manual
License: BSD-3-Clause
BuildArch: noarch
Requires: %{name}-filesystem = %{version}-%{release}

%description manual
This package provides the User Guide and Haddock manual.
%endif


# ghclibdir also needs ghc_version_override for bootstrapping
%global ghc_version_override %{version}

%if %{with build_hadrian}
%package hadrian
Summary: GHC Hadrian buildsystem tool
License: MIT
Version: 0.1.0.0

%description hadrian
This provides the hadrian tool which can be used to build ghc.
%endif

%global BSDHaskellReport %{quote:BSD-3-Clause AND HaskellReport}

# use "./libraries-versions.sh" to check versions
%if %{defined ghclibdir}
%ghc_lib_subpackage -d -l BSD-3-Clause Cabal-%{Cabal_ver}
%ghc_lib_subpackage -d -l %BSDHaskellReport array-0.5.4.0
%ghc_lib_subpackage -d -l %BSDHaskellReport -c gmp-devel%{?_isa},libffi-devel%{?_isa} base-%{base_ver}
%ghc_lib_subpackage -d -l BSD-3-Clause binary-0.8.9.0
%ghc_lib_subpackage -d -l BSD-3-Clause bytestring-0.11.4.0
%ghc_lib_subpackage -d -l %BSDHaskellReport containers-0.6.5.1
%ghc_lib_subpackage -d -l %BSDHaskellReport deepseq-1.4.6.1
%ghc_lib_subpackage -d -l %BSDHaskellReport directory-1.3.6.2
%ghc_lib_subpackage -d -l %BSDHaskellReport exceptions-0.10.4
%ghc_lib_subpackage -d -l BSD-3-Clause filepath-1.4.2.2
# in ghc not ghc-libraries:
%ghc_lib_subpackage -d -x ghc-%{ghc_version_override}
%ghc_lib_subpackage -d -x -l BSD-3-Clause ghc-bignum-%{ghc_bignum_ver}
%ghc_lib_subpackage -d -x -l BSD-3-Clause ghc-boot-%{ghc_version_override}
%ghc_lib_subpackage -d -l BSD-3-Clause ghc-boot-th-%{ghc_version_override}
%ghc_lib_subpackage -d -x -l BSD-3-Clause ghc-compact-%{ghc_compact_ver}
%ghc_lib_subpackage -d -x -l BSD-3-Clause ghc-heap-%{ghc_version_override}
# see below for ghc-prim
%ghc_lib_subpackage -d -x -l BSD-3-Clause ghci-%{ghc_version_override}
%ghc_lib_subpackage -d -l BSD-3-Clause haskeline-0.8.2
%ghc_lib_subpackage -d -x -l BSD-3-Clause hpc-%{hpc_ver}
# see below for integer-gmp
%ghc_lib_subpackage -d -x -l %BSDHaskellReport libiserv-%{ghc_version_override}
%ghc_lib_subpackage -d -l BSD-3-Clause mtl-%{mtl_ver}
%ghc_lib_subpackage -d -l BSD-3-Clause parsec-3.1.15.0
%ghc_lib_subpackage -d -l BSD-3-Clause pretty-1.1.3.6
%ghc_lib_subpackage -d -l %BSDHaskellReport process-1.6.16.0
%ghc_lib_subpackage -d -l BSD-3-Clause stm-2.5.0.2
%ghc_lib_subpackage -d -l BSD-3-Clause template-haskell-2.18.0.0
%ghc_lib_subpackage -d -l BSD-3-Clause -c ncurses-devel%{?_isa} terminfo-0.4.1.5
%ghc_lib_subpackage -d -l BSD-3-Clause text-1.2.5.0
%ghc_lib_subpackage -d -l BSD-3-Clause time-1.11.1.1
%ghc_lib_subpackage -d -l BSD-3-Clause transformers-%{transformers_ver}
%ghc_lib_subpackage -d -l BSD-3-Clause unix-2.7.2.2
%if %{with haddock} || %{with hadrian}
%ghc_lib_subpackage -d -l BSD-3-Clause xhtml-%{xhtml_ver}
%endif
%endif

%global version %{ghc_version_override}

%package devel
Summary: GHC development libraries meta package
License: BSD-3-Clause AND HaskellReport
Requires: %{name}-compiler = %{version}-%{release}
Obsoletes: %{name}-libraries < %{version}-%{release}
Provides: %{name}-libraries = %{version}-%{release}
%{?ghc_packages_list:Requires: %(echo %{ghc_packages_list} | sed -e "s/\([^ ]*\)-\([^ ]*\)/%{name}-\1-devel = \2-%{release},/g")}

%description devel
This is a meta-package for all the development library packages in GHC
except the ghc library, which is installed by the toplevel ghc metapackage.


%if %{with ghc_prof}
%package prof
Summary: GHC profiling libraries meta package
License: BSD-3-Clause
Requires: %{name}-compiler = %{version}-%{release}

%description prof
Installing this package causes %{name}-*-prof packages corresponding to
%{name}-*-devel packages to be automatically installed too.
%endif


%prep
%setup -q -n ghc-%{version} %{?with_testsuite:-b1}

%patch -P1 -p1 -b .orig
%patch -P2 -p1 -b .orig
%patch -P3 -p1 -b .orig
%patch -P4 -p1 -b .orig7
%patch -P5 -p1 -b .orig7

%patch -P8 -p1 -b .orig
%patch -P9 -p1 -b .orig
%patch -P10 -p1 -b .orig
%patch -P11 -p1 -b .orig

rm libffi-tarballs/libffi-*.tar.gz

%ifarch armv7hl
%patch -P12 -p1 -b .orig
%endif

%ifarch %{ghc_unregisterized_arches}
%patch -P15 -p1 -b .orig
%endif

%if %{with hadrian}
%ifarch %{ghc_unregisterized_arches}
%patch -P16 -p1 -b .orig
%endif
# remove if epel9 ghc using llvm
%ifarch s390x
%if %{defined el9}
%patch -P16 -p1 -b .orig
%endif
%endif
%endif

%patch -P17 -p1 -b .orig

%ifarch s390x
# bigendian
%patch -P18 -p1 -b .orig
%endif

# debian
%patch -P24 -p1 -b .orig
%patch -P26 -p1 -b .orig
%patch -P27 -p1 -b .orig

#sphinx 7
%if 0%{?fedora} >= 40
%patch -P30 -p1 -b .orig
%endif

%ifarch ppc64le
%patch -P 35 -p1 -b .orig
%endif

%if %{with hadrian}
(cd libraries/Cabal/Cabal
 cabal-tweak-dep-ver unix '< 2.8' '< 2.9')
%endif

%if %{with haddock} && %{without hadrian}
%global gen_contents_index gen_contents_index.orig
if [ ! -f "libraries/%{gen_contents_index}" ]; then
  echo "Missing libraries/%{gen_contents_index}, needed at end of %%install!"
  exit 1
fi
%endif

%if %{without hadrian}
cat > mk/build.mk << EOF
%if %{with perfbuild}
%ifarch %{ghc_llvm_archs}
BuildFlavour = perf-llvm
%else
BuildFlavour = perf
%endif
%else
%ifarch %{ghc_llvm_archs}
BuildFlavour = quick-llvm
%else
BuildFlavour = quick
%endif
%endif
GhcLibWays = v dyn %{?with_ghc_prof:p}
%if %{with haddock}
HADDOCK_DOCS = YES
EXTRA_HADDOCK_OPTS += --hyperlinked-source --hoogle --quickjump
%else
HADDOCK_DOCS = NO
%endif
%if %{with manual}
BUILD_MAN = YES
BUILD_SPHINX_HTML = YES
%else
BUILD_MAN = NO
BUILD_SPHINX_HTML = NO
%endif
BUILD_SPHINX_PDF = NO
EOF
%endif


%build
# for patch11
autoreconf

%ghc_set_gcc_flags
export CC=%{_bindir}/gcc
%if %{with ld_gold}
export LD=%{_bindir}/ld.gold
%endif
export LLC=%{_bindir}/llc-%{llvm_major}
export OPT=%{_bindir}/opt-%{llvm_major}

export GHC=%{_bindir}/ghc%{?ghcboot_major:-%{ghcboot_major}}

# note lld breaks build-id
# /usr/bin/debugedit: Cannot handle 8-byte build ID
# https://bugzilla.redhat.com/show_bug.cgi?id=2116508
# https://gitlab.haskell.org/ghc/ghc/-/issues/22195

# * %%configure induces cross-build due to different target/host/build platform names
./configure --prefix=%{_prefix} --exec-prefix=%{_exec_prefix} \
  --bindir=%{_bindir} --sbindir=%{_sbindir} --sysconfdir=%{_sysconfdir} \
  --datadir=%{_datadir} --includedir=%{_includedir} --libdir=%{_libdir} \
  --libexecdir=%{_libexecdir} --localstatedir=%{_localstatedir} \
  --sharedstatedir=%{_sharedstatedir} --mandir=%{_mandir} \
  --docdir=%{_docdir}/%{name} \
  --with-system-libffi \
%if %{without ld_gold}
  --disable-ld-override \
%endif
%ifarch %{ghc_unregisterized_arches}
  --enable-unregisterised \
%endif
%{nil}

# avoid "ghc: hGetContents: invalid argument (invalid byte sequence)"
export LANG=C.utf8
%if %{with hadrian}
%if %{defined _ghcdynlibdir}
%undefine _ghcdynlibdir
%endif

%if %{with build_hadrian}
# do not disable debuginfo with ghc_bin_build
%global ghc_debuginfo 1
(
cd hadrian
ln -s ../libraries/mtl mtl-%{mtl_ver}
ln -s ../libraries/transformers transformers-%{transformers_ver}
ln -s ../libraries/Cabal/Cabal Cabal-%{Cabal_ver}
%ghc_libs_build -P -W transformers-%{transformers_ver} mtl-%{mtl_ver} Cabal-%{Cabal_ver}
%ghc_bin_build -W
)
%global hadrian hadrian/dist/build/hadrian/hadrian
%else
%global hadrian %{_bindir}/hadrian-%{ghc_major}
%endif

%ifarch %{ghc_llvm_archs}
%global hadrian_llvm +llvm
%endif
%define hadrian_docs %{!?with_haddock:--docs=no-haddocks} --docs=%[%{?with_manual} ? "no-sphinx-pdfs" : "no-sphinx"]
# quickest does not build shared libs
%{hadrian} %{?_smp_mflags} --flavour=%[%{?with_perfbuild} ? "perf" : "quick"]%{!?with_ghc_prof:+no_profiled_libs}%{?hadrian_llvm} %{hadrian_docs} binary-dist-dir
%else
make %{?_smp_mflags}
%endif


%install
%if %{with hadrian}
%if %{with build_hadrian}
(
cd hadrian
%ghc_bin_install
rm %{buildroot}%{_ghclicensedir}/%{name}/LICENSE
cp -p LICENSE ../LICENSE.hadrian
)
%endif
export LLC=%{_bindir}/llc-%{llvm_major}
export OPT=%{_bindir}/opt-%{llvm_major}
(
cd _build/bindist/ghc-%{version}-*
./configure --prefix=%{buildroot}%{ghclibdir} --bindir=%{buildroot}%{_bindir} --libdir=%{buildroot}%{_libdir} --mandir=%{buildroot}%{_mandir} --docdir=%{buildroot}%{_docdir}/%{name} \
%if %{without ld_gold}
  --disable-ld-override
%endif
%{nil}
make install
)
%else
make DESTDIR=%{buildroot} install
%if %{defined _ghcdynlibdir}
mv %{buildroot}%{ghclibdir}/*/libHS*ghc%{ghc_version}.so %{buildroot}%{_ghcdynlibdir}/
for i in %{buildroot}%{ghclibdir}/package.conf.d/*.conf; do
  sed -i -e 's!^dynamic-library-dirs: .*!dynamic-library-dirs: %{_ghcdynlibdir}!' $i
done
sed -i -e 's!^library-dirs: %{ghclibdir}/rts!&\ndynamic-library-dirs: %{_ghcdynlibdir}!' %{buildroot}%{ghclibdir}/package.conf.d/rts.conf
%endif
%endif

# was related https://bugzilla.redhat.com/show_bug.cgi?id=2166028
%if "%{?_ghcdynlibdir}" != "%_libdir"
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo "%{?_ghcdynlibdir}%{!?_ghcdynlibdir:%{ghclibplatform}}" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}.conf
%else
for i in $(find %{buildroot} -type f -executable -exec sh -c "file {} | grep -q 'dynamically linked'" \; -print); do
  chrpath -d $i
done
%endif

# containers src moved to a subdir
cp -p libraries/containers/containers/LICENSE libraries/containers/LICENSE

rm -f %{name}-*.files

# FIXME replace with ghc_subpackages_list
for i in %{ghc_packages_list}; do
name=$(echo $i | sed -e "s/\(.*\)-.*/\1/")
ver=$(echo $i | sed -e "s/.*-\(.*\)/\1/")
%ghc_gen_filelists $name $ver
echo "%%license libraries/$name/LICENSE" >> %{name}-$name.files
done

echo "%%dir %{ghclibdir}" >> %{name}-base%{?_ghcdynlibdir:-devel}.files
echo "%%dir %{ghcliblib}" >> %{name}-base%{?_ghcdynlibdir:-devel}.files
echo "%%dir %ghclibplatform" >> %{name}-base%{?_ghcdynlibdir:-devel}.files

%ghc_gen_filelists ghc %{ghc_version_override}
%ghc_gen_filelists ghc-bignum %{ghc_bignum_ver}
%ghc_gen_filelists ghc-boot %{ghc_version_override}
%ghc_gen_filelists ghc-compact %{ghc_compact_ver}
%ghc_gen_filelists ghc-heap %{ghc_version_override}
%ghc_gen_filelists ghci %{ghc_version_override}
%ghc_gen_filelists hpc %{hpc_ver}
%ghc_gen_filelists libiserv %{ghc_version_override}

%ghc_gen_filelists ghc-prim 0.8.0
%ghc_gen_filelists integer-gmp 1.1
%if %{with hadrian}
%ghc_gen_filelists rts %{rts_ver}
%endif

%ghc_merge_filelist ghc-prim base
%ghc_merge_filelist integer-gmp base
%if %{with hadrian}
%ghc_merge_filelist rts base
%endif

%if "%{?_ghcdynlibdir}" != "%_libdir"
echo "%{_sysconfdir}/ld.so.conf.d/%{name}.conf" >> %{name}-base.files
%endif

# add rts libs
%if %{with hadrian}
for i in %{buildroot}%{ghclibplatform}/libHSrts*ghc%{ghc_version}.so; do
if [ "$(basename $i)" != "libHSrts-%{rts_ver}-ghc%{ghc_version}.so" ]; then
echo $i >> %{name}-base.files
fi
done
%else
%if %{defined _ghcdynlibdir}
echo "%{ghclibdir}/rts" >> %{name}-base-devel.files
%else
echo "%%dir %{ghclibdir}/rts" >> %{name}-base.files
ls -d %{buildroot}%{ghclibdir}/rts/lib*.a >> %{name}-base-devel.files
%endif
ls %{buildroot}%{?_ghcdynlibdir}%{!?_ghcdynlibdir:%{ghclibdir}/rts}/libHSrts*.so >> %{name}-base.files
%if %{defined _ghcdynlibdir}
sed -i -e 's!^library-dirs: %{ghclibdir}/rts!&\ndynamic-library-dirs: %{_libdir}!' %{buildroot}%{ghclibdir}/package.conf.d/rts.conf
%endif
ls -d %{buildroot}%{ghclibdir}/package.conf.d/rts.conf >> %{name}-base-devel.files
%endif

ls -d %{buildroot}%{ghclibdir}/include >> %{name}-base-devel.files

%if %{with ghc_prof}
ls %{buildroot}%{ghclibdir}/bin/ghc-iserv-prof* >> %{name}-base-prof.files
%if %{with hadrian}
ls %{buildroot}%{ghcliblib}/bin/ghc-iserv-prof >> %{name}-base-prof.files
%endif
%endif

sed -i -e "s|^%{buildroot}||g" %{name}-base*.files
%if %{with hadrian}
sed -i -e "s|%{buildroot}||g" %{buildroot}%{_bindir}/*
%endif

%if %{with haddock} && %{without hadrian}
# generate initial lib doc index
cd libraries
sh %{gen_contents_index} --intree --verbose
cd ..
%endif

mkdir -p %{buildroot}%{_mandir}/man1
install -p -m 0644 %{SOURCE5} %{buildroot}%{_mandir}/man1/ghc-pkg.1
install -p -m 0644 %{SOURCE6} %{buildroot}%{_mandir}/man1/haddock.1
install -p -m 0644 %{SOURCE7} %{buildroot}%{_mandir}/man1/runghc.1

%if %{with hadrian}
%if %{with haddock}
rm %{buildroot}%{_pkgdocdir}/archives/libraries.html.tar.xz
%endif
%if %{with manual}
rm %{buildroot}%{_pkgdocdir}/archives/Haddock.html.tar.xz
rm %{buildroot}%{_pkgdocdir}/archives/users_guide.html.tar.xz
mv %{buildroot}%{_ghc_doc_dir}/users_guide/build-man/ghc.1 %{buildroot}%{_mandir}/man1/ghc-%{ghc_major}.1
%endif
%endif

# we package the library license files separately
%if %{without hadrian}
find %{buildroot}%{ghc_html_libraries_dir} -name LICENSE -exec rm '{}' ';'
%endif

%ifarch armv7hl
export RPM_BUILD_NCPUS=1
%endif

%if %{with hadrian}
%if %{with build_hadrian}
mv %{buildroot}%{_bindir}/hadrian{,-%{ghc_major}}
%endif
%else
for i in hp2ps hpc hsc2hs runhaskell; do
  mv %{buildroot}%{_bindir}/$i{,-%{version}}
  ln -s $i-%{version} %{buildroot}%{_bindir}/$i
done
%endif

%if %{with hadrian}
rm %{buildroot}%{ghcliblib}/package.conf.d/.stamp
rm %{buildroot}%{ghcliblib}/package.conf.d/*.conf.copy

(cd %{buildroot}%{ghcliblib}/bin
for i in *; do
if [ -f %{buildroot}%{ghclibdir}/bin/$i ]; then
ln -sf ../../bin/$i
fi
done
)
%endif

(
cd %{buildroot}%{_bindir}
for i in *; do
    case $i in
     *-%{version}) ;;
     *)
        if [ -f $i-%{version} ]; then
           ln -s $i-%{version} $i-%{ghc_major}
        fi
    esac
done
)


%check
export LANG=C.utf8
# stolen from ghc6/debian/rules:
%if %{with hadrian}
export LD_LIBRARY_PATH=%{buildroot}%{ghclibplatform}:
GHC=%{buildroot}%{ghclibdir}/bin/ghc
%else
GHC=inplace/bin/ghc-stage2
%endif
$GHC --info
# simple sanity checks that the compiler actually works
rm -rf testghc
mkdir testghc
echo 'main = putStrLn "Foo"' > testghc/foo.hs
$GHC testghc/foo.hs -o testghc/foo
[ "$(testghc/foo)" = "Foo" ]
rm testghc/*
echo 'main = putStrLn "Foo"' > testghc/foo.hs
$GHC testghc/foo.hs -o testghc/foo -O2
[ "$(testghc/foo)" = "Foo" ]
rm testghc/*
echo 'main = putStrLn "Foo"' > testghc/foo.hs
$GHC testghc/foo.hs -o testghc/foo -dynamic
[ "$(testghc/foo)" = "Foo" ]
rm testghc/*
# no GHC calling convention in LLVM's PowerPC target code
# https://gitlab.haskell.org/ghc/ghc/-/issues/25667
%ifnarch ppc64le
echo 'main = putStrLn "Foo"' > testghc/foo.hs
$GHC testghc/foo.hs -o testghc/foo -fllvm
[ "$(testghc/foo)" = "Foo" ]
rm testghc/*
%endif

# check the ABI hashes
%if %{with abicheck}
if [ "%{version}" = "$(ghc-%{ghc_major} --numeric-version)" ]; then
  echo "Checking package ABI hashes:"
  for i in %{ghc_packages_list}; do
    old=$(ghc-pkg-%{ghc_major} field $i id --simple-output || :)
    if [ -n "$old" ]; then
      new=$(/usr/lib/rpm/ghc-pkg-wrapper %{buildroot}%{ghclibdir} field $i id --simple-output)
      if [ "$old" != "$new" ]; then
        echo "ABI hash for $i changed!:" >&2
        echo "  $old -> $new" >&2
        ghc_abi_hash_change=yes
      else
        echo "($old unchanged)"
      fi
    else
      echo "($i not installed)"
    fi
  done
  if [ "$ghc_abi_hash_change" = "yes" ]; then
     echo "ghc ABI hash change: aborting build!" >&2
     exit 1
  fi
else
  echo "ABI hash checks skipped: GHC changed from $(ghc-%{ghc_major} --numeric-version) to %{version}"
fi
%endif

%if %{with testsuite}
make test
%endif


%if %{defined ghclibdir}
%if "%{?_ghcdynlibdir}" != "%_libdir"
%post base -p /sbin/ldconfig
%postun base -p /sbin/ldconfig
%endif


%transfiletriggerin compiler -- %{ghcliblib}/package.conf.d
%ghc_pkg_recache
%end

%transfiletriggerpostun compiler -- %{ghcliblib}/package.conf.d
%ghc_pkg_recache
%end


%if %{with haddock} && %{without hadrian}
%transfiletriggerin doc-index -- %{ghc_html_libraries_dir}
env -C %{ghc_html_libraries_dir} ./gen_contents_index
%end

%transfiletriggerpostun doc-index -- %{ghc_html_libraries_dir}
env -C %{ghc_html_libraries_dir} ./gen_contents_index
%end
%endif
%endif


%files

%files compiler
%license LICENSE
%doc README.md
%{_bindir}/ghc-%{version}
%{_bindir}/ghc-pkg-%{version}
%{_bindir}/ghci-%{version}
%{_bindir}/hp2ps-%{?with_hadrian:ghc-}%{version}
%{_bindir}/hpc-%{?with_hadrian:ghc-}%{version}
%{_bindir}/hsc2hs-%{?with_hadrian:ghc-}%{version}
%{_bindir}/runghc-%{version}
%{_bindir}/runhaskell-%{version}
%{_bindir}/ghc-%{ghc_major}
%{_bindir}/ghc-pkg-%{ghc_major}
%{_bindir}/ghci-%{ghc_major}
%{_bindir}/runghc-%{ghc_major}
%{_bindir}/runhaskell-%{ghc_major}
%if %{without hadrian}
%{_bindir}/hp2ps-%{ghc_major}
%{_bindir}/hpc-%{ghc_major}
%{_bindir}/hsc2hs-%{ghc_major}
%endif
%dir %{ghclibdir}/bin
%{ghclibdir}/bin/ghc
%{ghclibdir}/bin/ghc-iserv
%{ghclibdir}/bin/ghc-iserv-dyn
%{ghclibdir}/bin/ghc-pkg
%{ghclibdir}/bin/hpc
%{ghclibdir}/bin/hsc2hs
%{ghclibdir}/bin/runghc
%{ghclibdir}/bin/hp2ps
%{ghclibdir}/bin/unlit
%if %{with hadrian}
%{ghclibdir}/bin/ghc-%{version}
%{ghclibdir}/bin/ghc-iserv-ghc-%{version}
%{ghclibdir}/bin/ghc-iserv-dyn-ghc-%{version}
%{ghclibdir}/bin/ghc-pkg-%{version}
%{ghclibdir}/bin/haddock
%{ghclibdir}/bin/haddock-ghc-%{version}
%{ghclibdir}/bin/hp2ps-ghc-%{version}
%{ghclibdir}/bin/hpc-ghc-%{version}
%{ghclibdir}/bin/hsc2hs-ghc-%{version}
%{ghclibdir}/bin/runghc-%{version}
%{ghclibdir}/bin/runhaskell
%{ghclibdir}/bin/runhaskell-%{version}
%{ghclibdir}/bin/unlit-ghc-%{version}
%dir %{ghcliblib}/bin
%{ghcliblib}/bin/ghc-iserv
%{ghcliblib}/bin/ghc-iserv-dyn
%{ghcliblib}/bin/unlit
%{ghcliblib}/DerivedConstants.h
%{ghcliblib}/ghcautoconf.h
%{ghcliblib}/ghcplatform.h
%{ghcliblib}/ghcversion.h
%endif
%{ghcliblib}/ghc-usage.txt
%{ghcliblib}/ghci-usage.txt
%{ghcliblib}/llvm-passes
%{ghcliblib}/llvm-targets
%dir %{ghcliblib}/package.conf.d
%ghost %{ghcliblib}/package.conf.d/package.cache
%{ghcliblib}/package.conf.d/package.cache.lock
%{ghcliblib}/settings
%{ghcliblib}/template-hsc.h
%{_mandir}/man1/ghc-pkg.1*
%{_mandir}/man1/haddock.1*
%{_mandir}/man1/runghc.1*

%if %{with hadrian} || %{with haddock}
%{_bindir}/haddock-ghc-%{version}
%{ghcliblib}/html
%{ghcliblib}/latex
%endif
%if %{with haddock}
%if %{without hadrian}
%{ghclibdir}/bin/haddock
%{ghc_html_libraries_dir}/prologue.txt
%endif
%verify(not size mtime) %{ghc_html_libraries_dir}/haddock-bundle.min.js
%verify(not size mtime) %{ghc_html_libraries_dir}/linuwial.css
%verify(not size mtime) %{ghc_html_libraries_dir}/quick-jump.css
%verify(not size mtime) %{ghc_html_libraries_dir}/synopsis.png
%endif
%if %{with manual}
%if %{with hadrian}
%{_mandir}/man1/ghc-%{ghc_major}.1*
%else
%{_mandir}/man1/ghc.1*
%endif
%endif

%files compiler-default
%{_bindir}/ghc
%{_bindir}/ghc-pkg
%{_bindir}/ghci
%if %{with hadrian} || %{with haddock}
%{_bindir}/haddock
%endif
%{_bindir}/hp2ps
%{_bindir}/hpc
%{_bindir}/hsc2hs
%{_bindir}/runghc
%{_bindir}/runhaskell

%files devel

%if %{with haddock} || (%{with hadrian} && %{with manual})
%files doc
%{ghc_html_dir}/index.html

%files doc-index
%if %{with haddock}
#%%{ghc_html_libraries_dir}/gen_contents_index
%verify(not size mtime) %{ghc_html_libraries_dir}/doc-index*.html
%verify(not size mtime) %{ghc_html_libraries_dir}/index*.html
%endif

%files filesystem
%dir %_ghc_doc_dir
%dir %ghc_html_dir
%if %{with haddock}
%dir %ghc_html_libraries_dir
%endif
%endif

%if %{with hadrian} && %{with build_hadrian}
%files hadrian
%license LICENSE.hadrian
%{_bindir}/hadrian-%{ghc_major}
%endif

%if %{with manual}
%files manual
## needs pandoc
#%%{ghc_html_dir}/Cabal
%{ghc_html_dir}/index.html
%{ghc_html_dir}/users_guide
%if %{with hadrian}
%{ghc_html_dir}/Haddock
%else
%if %{with haddock}
%{ghc_html_dir}/haddock
%endif
%endif
%endif

%if %{with ghc_prof}
%files prof
%endif


%changelog
* Tue Jan 21 2025 Jens Petersen <petersen@redhat.com> - 9.2.8-28
- fix hp2ps failure with gcc15 C23
- setup llvm compiler for all archs not just those defaulting to llvm backend

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.8-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.8-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 15 2024 Jens Petersen <petersen@redhat.com> - 9.2.8-25
- explicit requires binutils-gold
- ppc64le: NCG fix for ccall target hints (Peter Trommler, #2172771)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.8-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.8-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan  5 2024 Jens Petersen <petersen@redhat.com> - 9.2.8-22
- s390x: patch from @stefansf (IBM) to fix llvm alignment in data sections
  which should fix certain runtime crashes (#2248097)
- fixup sphinx links patch

* Mon Aug  7 2023 Jens Petersen <petersen@redhat.com> - 9.2.8-21
- fixup SPDX license tags to use "AND"
- patch hadrian to build with Cabal-3.8

* Tue Jul 25 2023 Jens Petersen <petersen@redhat.com> - 9.2.8-20
- self-bootstrap from ghc9.2
- build the ghc.1 manpage with sphinx and version not to conflict
- backport bcond perfbuild changes from ghc9.4
- fix sphinx flags.py: python 3.12 dropped distutils
- base subpkg now owns ghcliblib and ghclibplatform dirs (#2185357)
- s390x: no longer apply unregisterized patches

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 29 2023 Jens Petersen <petersen@redhat.com> - 9.2.8-18
- update to 9.2.8
- https://downloads.haskell.org/~ghc/9.2.8/docs/html/users_guide/9.2.8-notes.html

* Thu May 25 2023 Jens Petersen <petersen@redhat.com> - 9.2.7-17
- include backport of 9.4 m32_allocator_init changes by Sylvain Henry (#2209162)
- SPDX migration of license tags

* Mon Mar 13 2023 Jens Petersen <petersen@redhat.com> - 9.2.7-16
- https://downloads.haskell.org/~ghc/9.2.7/docs/html/users_guide/9.2.7-notes.html
- bytestring-0.11.4.0

* Sat Dec 17 2022 Florian Weimer <fweimer@redhat.com> - 9.2.5-15
- Port configure script to C99

* Mon Nov  7 2022 Jens Petersen <petersen@redhat.com> - 9.2.5-14
- https://www.haskell.org/ghc/blog/20221107-ghc-9.2.5-released.html
- https://downloads.haskell.org/~ghc/9.2.5/docs/html/users_guide/9.2.5-notes.html
- base-4.16.4.0 and process-1.6.16.0
- backport packaging changes from ghc9.4
- epel9: enable hadrian
- F35,F36: disable armv7hl due to failing (#2142238)

* Fri Jul 29 2022 Jens Petersen <petersen@redhat.com> - 9.2.4-13
- https://downloads.haskell.org/~ghc/9.2.4/docs/html/users_guide/9.2.4-notes.html
- base 4.16.3.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jens Petersen <petersen@redhat.com>
- make sure to enable debuginfo always to avoid .build-id conflicts
- add major version symlinks for programs in /usr/bin

* Fri Jun 10 2022 Jens Petersen <petersen@redhat.com> - 9.2.3-11
- add filesystem subpackage

* Sun May 29 2022 Jens Petersen <petersen@redhat.com> - 9.2.3-10
- https://downloads.haskell.org/~ghc/9.2.3/docs/html/users_guide/9.2.3-notes.html
- base-4.16.2.0 and bytestring-0.11.3.1

* Sun May  1 2022 Jens Petersen <petersen@redhat.com> - 9.2.2-9
- ghc9.2 now recommends ghc9.2-compiler-default
- recommends zlib-devel was moved to cabal-install/stack
- enable system libffi (for Hadrian)
  NB unfortunately this changes all the library ABI hash keys

* Sat Mar 12 2022 Jens Petersen <petersen@redhat.com> - 9.2.2-8
- https://downloads.haskell.org/~ghc/9.2.2/docs/html/users_guide/9.2.2-notes.html
- use llvm12 for aarch64 and s390x

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 Miro Hrončok <mhroncok@redhat.com> - 9.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/LIBFFI34

* Fri Dec 31 2021 Jens Petersen <petersen@redhat.com> - 9.2.1-5
- enable the armv7 VFPv3D16 patch

* Wed Dec 29 2021 Jens Petersen <petersen@redhat.com> - 9.2.1-4
- place docs under ghc9.2, so they can also be parallel installed
- make hadrian perf build respect ghc_prof

* Mon Dec 27 2021 Jens Petersen <petersen@redhat.com> - 9.2.1-3
- compiler-default subpackage can provide the unversioned bindir files

* Mon Dec 20 2021 Jens Petersen <petersen@redhat.com> - 9.2.1-2
- build with ghc's Hadrian buildsystem
- s390x now uses the llvm backend
- manuals created by sphinx disabled for now
- ghc-iserv-prof now lives in ghc-base-prof
- add hadrian subpackage
- move the haddock index files into doc-index

* Wed Dec  8 2021 Jens Petersen <petersen@redhat.com> - 9.2.1-1
- initial ghc9.2 package derived from the ghc:9.2 module
- https://downloads.haskell.org/ghc/9.2.1/docs/html/users_guide/9.2.1-notes.html
- see the Fedora ghc:9.2 branch for earlier packaging changes
