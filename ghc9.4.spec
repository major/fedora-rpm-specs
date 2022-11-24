# disable prof, docs, perf build
# bcond_with for production builds: disable quick build
%bcond_with quickbuild

# make sure ghc libraries' ABI hashes unchanged (ghcX.Y not supported yet)
%bcond_with abicheck

# bcond_without for production builds: use Hadrian buildsystem
%if %{defined fedora}
%bcond_without hadrian
%else
# https://bugzilla.redhat.com/show_bug.cgi?id=2141054
# https://gitlab.haskell.org/ghc/ghc/-/issues/22427
%ifarch s390x
%bcond_with hadrian
%else
%bcond_without hadrian
%endif
%endif

# bcond_without for production builds: build hadrian
%bcond_without build_hadrian

# bcond_without for production builds: enable debuginfo
%bcond_without ghc_debuginfo

%if %{without ghc_debuginfo}
%undefine _enable_debug_packages
%endif

%global ghc_major 9.4
%global ghc_name ghc%{ghc_major}

# bootstrap from this package
%global ghcboot ghc9.0
%global ghcbootminor 9.0.2

# to handle RCs
%global ghc_release %{version}

%global base_ver 4.17.0.0
%global ghc_compact_ver 0.1.0.0
%global hpc_ver 0.6.1.0

# build profiling libraries
# build haddock
# perf production build (disable for quick build)
%if %{with quickbuild}
%undefine with_ghc_prof
%undefine with_haddock
%bcond_with perf_build
%else
%bcond_without ghc_prof
# https://gitlab.haskell.org/ghc/ghc/-/issues/19754
# https://github.com/haskell/haddock/issues/1384
%ifarch armv7hl
%undefine with_haddock
%else
%if %{with hadrian}
%bcond_without haddock
%bcond_without manual
%else
%ifarch s390x
%if %{defined fedora}
%bcond_without haddock
%else
%undefine with_haddock
%endif
%else
%bcond_without haddock
%endif
%endif
%endif
%bcond_without perf_build
%endif

%if %{without hadrian}
# locked together since disabling haddock causes no manuals built
# and disabling haddock still created index.html
# https://gitlab.haskell.org/ghc/ghc/-/issues/15190
%{?with_haddock:%bcond_without manual}
%endif

# no longer build testsuite (takes time and not really being used)
%bcond_with testsuite

# 9.4 needs llvm 10-13
%global llvm_major 13
%if %{with hadrian}
%global ghc_llvm_archs armv7hl s390x
%global ghc_unregisterized_arches s390 %{mips} riscv64
%else
%global ghc_llvm_archs armv7hl
%global ghc_unregisterized_arches s390 s390x %{mips} riscv64
%endif

Name: %{ghc_name}
Version: 9.4.3
# Since library subpackages are versioned:
# - release can only be reset if *all* library versions get bumped simultaneously
#   (sometimes after a major release)
# - minor release numbers for a branch should be incremented monotonically
Release: 14%{?dist}
Summary: Glasgow Haskell Compiler

License: BSD and HaskellReport
URL: https://haskell.org/ghc/
Source0: https://downloads.haskell.org/ghc/%{ghc_release}/ghc-%{version}-src.tar.lz
%if %{with testsuite}
Source1: https://downloads.haskell.org/ghc/%{ghc_release}/ghc-%{version}-testsuite.tar.lz
%endif
Source5: ghc-pkg.man
Source6: haddock.man
Source7: runghc.man

# https://bugzilla.redhat.com/show_bug.cgi?id=2083103
ExcludeArch: armv7hl

# absolute haddock path (was for html/libraries -> libraries)
Patch1: ghc-gen_contents_index-haddock-path.patch
Patch2: ghc-Cabal-install-PATH-warning.patch
Patch3: ghc-gen_contents_index-nodocs.patch
# detect ffi.h
# https://gitlab.haskell.org/ghc/ghc/-/issues/21485
Patch5: https://gitlab.haskell.org/ghc/ghc/-/commit/6e12e3c178fe9ad16131eb3c089bd6578976f5d6.patch
Patch7: ghc-compiler-enable-build-id.patch
Patch8: ghc-configure-c99.patch

# arm patches
Patch12: ghc-armv7-VFPv3D16--NEON.patch
# https://github.com/haskell/text/issues/396
# reverts https://github.com/haskell/text/pull/405
Patch13: text2-allow-ghc8-arm.patch

# for unregisterized
# https://gitlab.haskell.org/ghc/ghc/-/issues/15689
Patch15: ghc-warnings.mk-CC-Wall.patch
Patch16: ghc-hadrian-s390x-rts--qg.patch

# Debian patches:
Patch24: buildpath-abi-stability.patch
Patch26: no-missing-haddock-file-warning.patch

# fedora ghc has been bootstrapped on
# %%{ix86} x86_64 ppc ppc64 armv7hl s390 s390x ppc64le aarch64
# and retired arches: alpha sparcv9 armv5tel
# see also deprecated ghc_arches defined in ghc-srpm-macros
# /usr/lib/rpm/macros.d/macros.ghc-srpm

BuildRequires: %{ghcboot}-compiler > 9.0
# for ABI hash checking
%if %{with abicheck}
BuildRequires: %{name}
%endif
BuildRequires: ghc-rpm-macros-extra >= 2.3.16
BuildRequires: %{ghcboot}-binary-devel
BuildRequires: %{ghcboot}-bytestring-devel
BuildRequires: %{ghcboot}-containers-devel
BuildRequires: %{ghcboot}-directory-devel
BuildRequires: %{ghcboot}-pretty-devel
BuildRequires: %{ghcboot}-process-devel
BuildRequires: %{ghcboot}-stm-devel
BuildRequires: %{ghcboot}-template-haskell-devel
%if %{without hadrian}
BuildRequires: %{ghcboot}-text-devel
%endif
BuildRequires: %{ghcboot}-transformers-devel
BuildRequires: alex
BuildRequires: gmp-devel
BuildRequires: happy
BuildRequires: libffi-devel
BuildRequires: lzip
BuildRequires: make
BuildRequires: gcc-c++
# for terminfo
BuildRequires: ncurses-devel
BuildRequires: perl-interpreter
BuildRequires: python3
%if %{with manual}
BuildRequires: python3-sphinx
%endif
%ifarch %{ghc_llvm_archs}
BuildRequires: llvm%{llvm_major}
%endif
BuildRequires: autoconf, automake
%if %{with hadrian}
%if %{with build_hadrian}
BuildRequires:  ghc-Cabal-static
BuildRequires:  ghc-QuickCheck-static
BuildRequires:  ghc-base-static
BuildRequires:  ghc-bytestring-static
BuildRequires:  ghc-containers-static
BuildRequires:  ghc-directory-static
BuildRequires:  ghc-extra-static
BuildRequires:  ghc-filepath-static
BuildRequires:  ghc-mtl-static
BuildRequires:  ghc-parsec-static
BuildRequires:  ghc-shake-static
BuildRequires:  ghc-stm-static
BuildRequires:  ghc-transformers-static
BuildRequires:  ghc-unordered-containers-static
%else
BuildRequires: %{name}-hadrian
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
License: BSD
Requires: gcc%{?_isa}
Requires: %{name}-base-devel%{?_isa} = %{base_ver}-%{release}
%if %{with haddock}
Requires: %{name}-filesystem = %{version}-%{release}
%else
Obsoletes: %{name}-doc-index < %{version}-%{release}
Obsoletes: %{name}-filesystem < %{version}-%{release}
%endif
%ifarch %{ghc_llvm_archs}
Requires: llvm%{llvm_major}
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
License: BSD

%description doc
Installing this package causes %{name}-*-doc packages corresponding to
%{name}-*-devel packages to be automatically installed too.


%package doc-index
Summary: GHC library documentation indexing
License: BSD
Requires: %{name}-compiler = %{version}-%{release}
BuildArch: noarch

%description doc-index
The package enables re-indexing of installed library documention.


%package filesystem
Summary: Shared directories for Haskell documentation
BuildArch: noarch

%description filesystem
This package provides some common directories used for
Haskell libraries documentation.
%endif


%if %{with manual}
%package manual
Summary: GHC manual
License: BSD
BuildArch: noarch
Requires: %{name}-filesystem = %{version}-%{release}

%description manual
This package provides the User Guide and Haddock manual.
%endif


# ghclibdir also needs ghc_version_override for bootstrapping
%global ghc_version_override %{version}

%if %{with hadrian}
%package hadrian
Summary: GHC Hadrian buildsystem tool
License: MIT
Version: 0.1.0.0

%description hadrian
This provides the hadrian tool which can be used to build ghc.
%endif

%global BSDHaskellReport %{quote:BSD and HaskellReport}

# use "./libraries-versions.sh" to check versions
%if %{defined ghclibdir}
%ghc_lib_subpackage -d -l BSD Cabal-3.8.1.0
%ghc_lib_subpackage -d -l BSD Cabal-syntax-3.8.1.0
%ghc_lib_subpackage -d -l %BSDHaskellReport array-0.5.4.0
%ghc_lib_subpackage -d -l %BSDHaskellReport -c gmp-devel%{?_isa},libffi-devel%{?_isa} base-%{base_ver}
%ghc_lib_subpackage -d -l BSD binary-0.8.9.1
%ghc_lib_subpackage -d -l BSD bytestring-0.11.3.1
%ghc_lib_subpackage -d -l %BSDHaskellReport containers-0.6.6
%ghc_lib_subpackage -d -l %BSDHaskellReport deepseq-1.4.8.0
%ghc_lib_subpackage -d -l %BSDHaskellReport directory-1.3.7.1
%ghc_lib_subpackage -d -l %BSDHaskellReport exceptions-0.10.5
%ghc_lib_subpackage -d -l BSD filepath-1.4.2.2
# in ghc not ghc-libraries:
%ghc_lib_subpackage -d -x ghc-%{ghc_version_override}
# see below for ghc-bignum
%ghc_lib_subpackage -d -x -l BSD ghc-boot-%{ghc_version_override}
%ghc_lib_subpackage -d -l BSD ghc-boot-th-%{ghc_version_override}
%ghc_lib_subpackage -d -x -l BSD ghc-compact-%{ghc_compact_ver}
%ghc_lib_subpackage -d -x -l BSD ghc-heap-%{ghc_version_override}
# see below for ghc-prim
%ghc_lib_subpackage -d -x -l BSD ghci-%{ghc_version_override}
%ghc_lib_subpackage -d -l BSD haskeline-0.8.2
%ghc_lib_subpackage -d -x -l BSD hpc-%{hpc_ver}
# see below for integer-gmp
%ghc_lib_subpackage -d -x -l %BSDHaskellReport libiserv-%{ghc_version_override}
%ghc_lib_subpackage -d -l BSD mtl-2.2.2
%ghc_lib_subpackage -d -l BSD parsec-3.1.15.0
%ghc_lib_subpackage -d -l BSD pretty-1.1.3.6
%ghc_lib_subpackage -d -l %BSDHaskellReport process-1.6.16.0
%ghc_lib_subpackage -d -l BSD stm-2.5.1.0
%ghc_lib_subpackage -d -l BSD template-haskell-2.19.0.0
%ghc_lib_subpackage -d -l BSD -c ncurses-devel%{?_isa} terminfo-0.4.1.5
%ghc_lib_subpackage -d -l BSD text-2.0.1
%ghc_lib_subpackage -d -l BSD time-1.12.2
%ghc_lib_subpackage -d -l BSD transformers-0.5.6.2
%ghc_lib_subpackage -d -l BSD unix-2.7.3
%if %{with haddock} || %{with hadrian}
%ghc_lib_subpackage -d -l BSD xhtml-3000.2.2.1
%endif
%endif

%global version %{ghc_version_override}

%package devel
Summary: GHC development libraries meta package
License: BSD and HaskellReport
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
License: BSD
Requires: %{name}-compiler = %{version}-%{release}

%description prof
Installing this package causes %{name}-*-prof packages corresponding to
%{name}-*-devel packages to be automatically installed too.
%endif


%prep
%setup -q -n ghc-%{version} %{?with_testsuite:-b1}

%patch1 -p1 -b .orig
%patch3 -p1 -b .orig

%patch2 -p1 -b .orig
%patch5 -p1 -b .orig
# should be safe but testing in pre-releases first
%if 0%{?fedora} >= 37
%patch7 -p1 -b .orig
%endif
%patch8 -p1 -b .orig

rm libffi-tarballs/libffi-*.tar.gz

%ifarch armv7hl
%patch12 -p1 -b .orig
%endif
%ifarch aarch64 armv7hl
%patch13 -p1 -b .orig
%endif

# remove s390x after complete switching to llvm
%ifarch %{ghc_unregisterized_arches} s390x
%patch15 -p1 -b .orig
%patch16 -p1 -b .orig
%endif

#debian
#%%patch24 -p1 -b .orig
%patch26 -p1 -b .orig

%if %{with haddock} && %{without hadrian}
%global gen_contents_index gen_contents_index.orig
if [ ! -f "libraries/%{gen_contents_index}" ]; then
  echo "Missing libraries/%{gen_contents_index}, needed at end of %%install!"
  exit 1
fi
%endif

%if %{without hadrian}
# https://gitlab.haskell.org/ghc/ghc/-/wikis/platforms
cat > mk/build.mk << EOF
%if %{with perf_build}
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
# patch5 and patch12
autoupdate

%ghc_set_gcc_flags
export CC=%{_bindir}/gcc
# lld breaks build-id
# /usr/bin/debugedit: Cannot handle 8-byte build ID
# https://bugzilla.redhat.com/show_bug.cgi?id=2116508
# https://gitlab.haskell.org/ghc/ghc/-/issues/22195
export LD=%{_bindir}/ld.gold

export GHC=/usr/bin/ghc-%{ghcbootminor}

# * %%configure induces cross-build due to different target/host/build platform names
./configure --prefix=%{_prefix} --exec-prefix=%{_exec_prefix} \
  --bindir=%{_bindir} --sbindir=%{_sbindir} --sysconfdir=%{_sysconfdir} \
  --datadir=%{_datadir} --includedir=%{_includedir} --libdir=%{_libdir} \
  --libexecdir=%{_libexecdir} --localstatedir=%{_localstatedir} \
  --sharedstatedir=%{_sharedstatedir} --mandir=%{_mandir} \
  --docdir=%{_docdir}/%{name} \
  --with-system-libffi \
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
%if %{with ghc_debuginfo}
# do not disable debuginfo with ghc_bin_build
%global ghc_debuginfo 1
%endif
(
cd hadrian
%ghc_bin_build
)
%global hadrian hadrian/dist/build/hadrian/hadrian
%else
%global hadrian %(echo %{_bindir}/hadrian-%{ghc_major}.*)
%endif

%ifarch %{ghc_llvm_archs}
%global hadrian_llvm +llvm
%endif
%define hadrian_docs %{!?with_haddock:--docs=no-haddocks} %{!?with_manual:--docs=no-sphinx}%{?with_manual:--docs=no-sphinx-pdfs --docs=no-sphinx-man}
# quickest does not build shared libs
# try release instead of perf
%{hadrian} %{?_smp_mflags} --flavour=%{?with_quickbuild:quick+no_profiled_libs}%{!?with_quickbuild:perf%{!?with_ghc_prof:+no_profiled_libs}}%{?hadrian_llvm} %{hadrian_docs} binary-dist-dir
%else
# https://gitlab.haskell.org/ghc/ghc/-/issues/22099
# 48 cpus breaks build: Error: ghc-cabal: Encountered missing or private dependencies: rts >=1.0 && <1.1
%global _smp_ncpus_max 16
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
# https://gitlab.haskell.org/ghc/ghc/-/issues/20120#note_366872
(
cd _build/bindist/ghc-%{version}-*
./configure --prefix=%{buildroot}%{ghclibdir} --bindir=%{buildroot}%{_bindir} --libdir=%{buildroot}%{_libdir} --mandir=%{buildroot}%{_mandir} --docdir=%{buildroot}%{_docdir}/%{name}
make install
)
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo "%{ghclibplatform}" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}.conf
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
# avoid 'E: binary-or-shlib-defines-rpath'
for i in $(find %{buildroot} -type f -executable -exec sh -c "file {} | grep -q 'dynamically linked'" \; -print); do
  chrpath -d $i
done

# containers src moved to a subdir
cp -p libraries/containers/containers/LICENSE libraries/containers/LICENSE
# hack for Cabal-syntax/LICENSE
mkdir -p libraries/Cabal-syntax
cp -p libraries/Cabal/Cabal-syntax/LICENSE libraries/Cabal-syntax

rm -f %{name}-*.files

# FIXME replace with ghc_subpackages_list
for i in %{ghc_packages_list}; do
name=$(echo $i | sed -e "s/\(.*\)-.*/\1/")
ver=$(echo $i | sed -e "s/.*-\(.*\)/\1/")
%ghc_gen_filelists $name $ver
echo "%%license libraries/$name/LICENSE" >> %{name}-$name.files
done

echo "%%dir %{ghclibdir}" >> %{name}-base%{?_ghcdynlibdir:-devel}.files

%ghc_gen_filelists ghc %{ghc_version_override}
%ghc_gen_filelists ghc-boot %{ghc_version_override}
%ghc_gen_filelists ghc-compact %{ghc_compact_ver}
%ghc_gen_filelists ghc-heap %{ghc_version_override}
%ghc_gen_filelists ghci %{ghc_version_override}
%ghc_gen_filelists hpc %{hpc_ver}
%ghc_gen_filelists libiserv %{ghc_version_override}

%ghc_gen_filelists ghc-bignum 1.3
%ghc_gen_filelists ghc-prim 0.9.0
%ghc_gen_filelists integer-gmp 1.1
%if %{with hadrian}
%ghc_gen_filelists rts 1.0.2
%endif

%define merge_filelist()\
cat %{name}-%1.files >> %{name}-%2.files\
cat %{name}-%1-devel.files >> %{name}-%2-devel.files\
%if %{defined ghc_devel_prof}\
cat %{name}-%1-doc.files >> %{name}-%2-doc.files\
cat %{name}-%1-prof.files >> %{name}-%2-prof.files\
%endif\
if [ "%1" != "rts" ]; then\
cp -p libraries/%1/LICENSE libraries/LICENSE.%1\
echo "%%license libraries/LICENSE.%1" >> %{name}-%2.files\
fi\
%{nil}

%merge_filelist ghc-bignum base
%merge_filelist ghc-prim base
%merge_filelist integer-gmp base
%if %{with hadrian}
%merge_filelist rts base
%endif

# add rts libs
%if %{with hadrian}
for i in %{buildroot}%{ghclibplatform}/libHSrts*ghc%{ghc_version}.so; do
echo $i >> %{name}-base.files
done
echo "%{_sysconfdir}/ld.so.conf.d/%{name}.conf" >> %{name}-base.files
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

if [ -f %{buildroot}%{ghcliblib}/package.conf.d/system-cxx-std-lib-1.0.conf ]; then
ls -d %{buildroot}%{ghcliblib}/package.conf.d/system-cxx-std-lib-1.0.conf >> %{name}-base-devel.files
fi

%if %{with ghc_prof}
ls %{buildroot}%{ghclibdir}/bin/ghc-iserv-prof* >> %{name}-base-prof.files
%if %{with hadrian}
ls %{buildroot}%{ghclibdir}/lib/bin/ghc-iserv-prof >> %{name}-base-prof.files
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

%if %{with hadrian}
%if %{with haddock}
rm %{buildroot}%{_pkgdocdir}/archives/libraries.html.tar.xz
%endif
%if %{with manual}
rm %{buildroot}%{_pkgdocdir}/archives/Haddock.html.tar.xz
rm %{buildroot}%{_pkgdocdir}/archives/users_guide.html.tar.xz
%endif
%endif

# we package the library license files separately
%if %{without hadrian}
find %{buildroot}%{ghc_html_libraries_dir} -name LICENSE -exec rm '{}' ';'
%endif

mkdir -p %{buildroot}%{_mandir}/man1
install -p -m 0644 %{SOURCE5} %{buildroot}%{_mandir}/man1/ghc-pkg.1
install -p -m 0644 %{SOURCE6} %{buildroot}%{_mandir}/man1/haddock.1
install -p -m 0644 %{SOURCE7} %{buildroot}%{_mandir}/man1/runghc.1

%ifarch armv7hl
export RPM_BUILD_NCPUS=1
%endif

%if %{with hadrian}
%if %{with build_hadrian}
mv %{buildroot}%{_bindir}/hadrian{,-%{version}}
%endif
%else
for i in hp2ps hpc hsc2hs runhaskell; do
  mv %{buildroot}%{_bindir}/$i{,-%{version}}
  ln -s $i-%{version} %{buildroot}%{_bindir}/$i
done
%endif

%if %{with hadrian}
rm %{buildroot}%{ghclibdir}/lib/package.conf.d/.stamp
rm %{buildroot}%{ghclibdir}/lib/package.conf.d/*.conf.copy

(cd %{buildroot}%{ghclibdir}/lib/bin
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
# Do some very simple tests that the compiler actually works
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

$GHC --info

# check the ABI hashes
%if %{with abicheck}
if [ "%{version}" = "$(ghc --numeric-version)" ]; then
  echo "Checking package ABI hashes:"
  for i in %{ghc_packages_list}; do
    old=$(ghc-pkg field $i id --simple-output || :)
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
  echo "ABI hash checks skipped: GHC changed from $(ghc --numeric-version) to %{version}"
fi
%endif

%if %{with testsuite}
make test
%endif


%if %{defined ghclibdir}
%post base -p /sbin/ldconfig
%postun base -p /sbin/ldconfig


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
%{ghclibdir}/lib/bin/ghc-iserv
%{ghclibdir}/lib/bin/ghc-iserv-dyn
%{ghclibdir}/lib/bin/unlit
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
%if %{with haddock} || (%{with hadrian} && %{with manual})
%{ghc_html_libraries_dir}/prologue.txt
%endif
%if %{with haddock}
%if %{without hadrian}
%{ghclibdir}/bin/haddock
%endif
%verify(not size mtime) %{ghc_html_libraries_dir}/haddock-bundle.min.js
%verify(not size mtime) %{ghc_html_libraries_dir}/linuwial.css
%verify(not size mtime) %{ghc_html_libraries_dir}/quick-jump.css
%verify(not size mtime) %{ghc_html_libraries_dir}/synopsis.png
%endif
%if %{with manual} && %{without hadrian}
%{_mandir}/man1/ghc.1*
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
%{ghc_html_libraries_dir}/gen_contents_index
%if %{with haddock}
%verify(not size mtime) %{ghc_html_libraries_dir}/doc-index*.html
%verify(not size mtime) %{ghc_html_libraries_dir}/index*.html
%endif

%files filesystem
%dir %_ghc_doc_dir
%dir %ghc_html_dir
%dir %ghc_html_libraries_dir
%endif

%if %{with hadrian} && %{with build_hadrian}
%files hadrian
%license LICENSE.hadrian
%{_bindir}/hadrian-%{version}
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
* Tue Nov 22 2022 Florian Weimer <fweimer@redhat.com> - 9.4.3-14
- Avoid implicit declaration of exit in configure check

* Fri Nov  4 2022 Jens Petersen <petersen@redhat.com> - 9.4.3-12
- https://www.haskell.org/ghc/blog/20221103-ghc-9.4.3-released.html
- https://downloads.haskell.org/~ghc/9.4.3/docs/users_guide/9.4.3-notes.html
- enable Hadrian for epel9

* Mon Oct 31 2022 Jens Petersen <petersen@redhat.com> - 9.4.2-11
- add ld.so.conf.d file for finding shared libraries under Hadrian
  and remove RPATHs for Hadrian builds to rid rpmlint RUNPATH errors
- export LD to prevent configuring lld (see #2116508)

* Tue Aug 23 2022 Jens Petersen <petersen@redhat.com> - 9.4.2-10
- https://www.haskell.org/ghc/blog/20220822-ghc-9.4.2-released.html
- https://downloads.haskell.org/~ghc/9.4.2/docs/users_guide/9.4.2-notes.html

* Tue Aug 16 2022 Jens Petersen <petersen@redhat.com> - 9.4.1-9
- build the manual (for hadrian)
- various make build fixes (only used for epel9 currently)

* Mon Aug 08 2022 Jens Petersen <petersen@redhat.com> - 9.4.1-8
- https://www.haskell.org/ghc/blog/20220807-ghc-9.4.1-released.html
- https://downloads.haskell.org/ghc/9.4.1/docs/users_guide/9.4.1-notes.html

* Sat Jul 23 2022 Jens Petersen <petersen@redhat.com> - 9.4.0.20220721-7
- 9.4.1-rc1
- https://downloads.haskell.org/ghc/9.4.1-rc1/docs/users_guide/9.4.1-notes.html

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.4.0.20220623-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Jens Petersen <petersen@redhat.com>
- make sure to enable debuginfo always to avoid .build-id conflicts

* Sat Jun 25 2022 Jens Petersen <petersen@redhat.com> - 9.4.0.20220623-5
- 9.4.1-alpha3
- https://downloads.haskell.org/ghc/9.4.1-alpha3/docs/users_guide/9.4.1-notes.html
- add major version symlinks for programs in /usr/bin

* Thu Jun  9 2022 Jens Petersen <petersen@redhat.com> - 9.4.0.20220523-4
- add filesystem subpackage
- backport upstream hadrian patch to allow boot with ghc9.0

* Wed May 25 2022 Jens Petersen <petersen@redhat.com> - 9.4.0.20220523-3
- 9.4.1-alpha2
- https://downloads.haskell.org/ghc/9.4.1-alpha2/docs/users_guide/9.4.1-notes.html
- built with ghc9.2

* Mon May  9 2022 Jens Petersen <petersen@redhat.com> - 9.4.0.20220501-2
- use --with-system-libffi for Hadrian (#2082827)

* Sat May  7 2022 Jens Petersen <petersen@redhat.com> - 9.4.0.20220501-1
- 9.4.1-alpha1
- derived from the ghc9.2 package
