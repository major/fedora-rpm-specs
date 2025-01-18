# Start: prod settings
# all *bcond_without* for production builds:
# - performance build (disable for quick build)
%bcond_without perfbuild
%bcond_without build_hadrian
%bcond_without manual
# End: prod settings

# not for production builds
%if %{without perfbuild}
# disable profiling libraries (overriding macros.ghc-srpm)
%undefine with_ghc_prof
# disable haddock documentation (overriding macros.ghc-os)
%undefine with_haddock
%endif

%global ghc_major 9.8
%global ghc_name ghc%{ghc_major}

# to handle RCs
%global ghc_release %{version}

%global base_ver 4.19.2.0
%global ghc_bignum_ver 1.3
%global ghc_compact_ver 0.1.0.0
%global hpc_ver 0.7.0.0
%global rts_ver 1.0.2
%global xhtml_ver 3000.2.2.1

# bootstrap needs 9.4+
%if 0%{?fedora} < 41 && 0%{?rhel} < 10
%global ghcboot_major 9.6
%endif
%global ghcboot ghc%{?ghcboot_major}

# make sure ghc libraries' ABI hashes unchanged
%bcond_with abicheck

# no longer build testsuite (takes time and not really being used)
%bcond_with testsuite

# ld
%bcond ld_gold 0

# 9.8 needs llvm 11-15
# rhel9 binutils too old for llvm13:
# https://bugzilla.redhat.com/show_bug.cgi?id=2141054
# https://gitlab.haskell.org/ghc/ghc/-/issues/22427
%if 0%{?rhel} == 9
%global llvm_major 12
%else
%global llvm_major 15
%endif
%global ghc_llvm_archs s390x riscv64
%global ghc_unregisterized_arches s390 %{mips}

Name: %{ghc_name}
Version: 9.8.4
# Since library subpackages are versioned:
# - release can only be reset if *all* library versions get bumped simultaneously
#   (sometimes after a major release)
# - minor release numbers for a branch should be incremented monotonically
Release: 13%{?dist}
Summary: Glasgow Haskell Compiler

License: BSD-3-Clause AND HaskellReport
URL: https://haskell.org/ghc/
Source0: https://downloads.haskell.org/ghc/%{ghc_release}/ghc-%{version}-src.tar.xz
%if %{with testsuite}
Source1: https://downloads.haskell.org/ghc/%{ghc_release}/ghc-%{version}-testsuite.tar.xz
%endif
Source5: ghc-pkg.man
Source6: haddock.man
Source7: runghc.man

# absolute haddock path (was for html/libraries -> libraries)
Patch1: ghc-gen_contents_index-haddock-path.patch
Patch2: ghc-Cabal-install-PATH-warning.patch
Patch3: ghc-gen_contents_index-nodocs.patch
# https://gitlab.haskell.org/ghc/ghc/-/merge_requests/9604
# needs more backporting to 9.6
Patch9: https://gitlab.haskell.org/ghc/ghc/-/merge_requests/9604.patch

# unregisterised
Patch16: ghc-hadrian-s390x-rts--qg.patch

# Debian patches:
# bad according to upstream
# see eg https://gitlab.haskell.org/ghc/ghc/-/merge_requests/9604
#Patch24: buildpath-abi-stability.patch
Patch26: no-missing-haddock-file-warning.patch
Patch27: haddock-remove-googleapis-fonts.patch

# RISCV64 added to Cabal
# See: https://github.com/haskell/cabal/pull/9062
Patch40: cabal-add-riscv64.patch

# Enable GHCi support on riscv64
# Upstream in >= 9.9.
Patch41: https://gitlab.haskell.org/ghc/ghc/-/commit/dd38aca95ac25adc9888083669b32ff551151259.patch

# https://github.com/haskell/directory/pull/184
Patch50: https://patch-diff.githubusercontent.com/raw/haskell/directory/pull/184.patch
# https://gitlab.haskell.org/ghc/ghc/-/wikis/platforms

# fedora ghc has been bootstrapped on
# %%{ix86} x86_64 s390x ppc64le aarch64 riscv64
# and previously: alpha sparcv9 armv5tel ppc ppc64 s390 armv7hl
# see also deprecated ghc_arches defined in ghc-srpm-macros
# /usr/lib/rpm/macros.d/macros.ghc-srpm

BuildRequires: %{ghcboot}-compiler
# for ABI hash checking
%if %{with abicheck}
BuildRequires: %{name}
%endif
BuildRequires: ghc-rpm-macros-extra >= 2.6.5
BuildRequires: %{ghcboot}-array-devel
BuildRequires: %{ghcboot}-binary-devel
BuildRequires: %{ghcboot}-bytestring-devel
BuildRequires: %{ghcboot}-containers-devel
BuildRequires: %{ghcboot}-deepseq-devel
BuildRequires: %{ghcboot}-directory-devel
BuildRequires: %{ghcboot}-filepath-devel
BuildRequires: %{ghcboot}-ghc-boot-th-devel
BuildRequires: %{ghcboot}-pretty-devel
BuildRequires: %{ghcboot}-process-devel
BuildRequires: %{ghcboot}-stm-devel
BuildRequires: %{ghcboot}-template-haskell-devel
BuildRequires: %{ghcboot}-time-devel
BuildRequires: %{ghcboot}-transformers-devel
BuildRequires: %{ghcboot}-unix-devel
BuildRequires: binutils%{?with_ld_gold:-gold}
BuildRequires: gmp-devel
BuildRequires: libffi-devel
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

# needed for binary-dist-dir
BuildRequires:  autoconf automake
%if %{with build_hadrian}
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base16-bytestring-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-cryptohash-sha256-devel
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
BuildRequires: %{name}-hadrian
%endif

Requires: %{name}-compiler = %{version}-%{release}
Requires: %{name}-devel = %{version}-%{release}
Requires: %{name}-ghc-devel = %{version}-%{release}
Requires: %{name}-ghc-boot-devel = %{version}-%{release}
Requires: %{name}-ghc-compact-devel = %{ghc_compact_ver}-%{release}
Requires: %{name}-ghc-heap-devel = %{version}-%{release}
Requires: %{name}-ghci-devel = %{version}-%{release}
Requires: %{name}-hpc-devel = %{hpc_ver}-%{release}
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


%if %{with haddock} || %{with manual}
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
License: BSD-3-Clause
BuildArch: noarch
Requires: %{name}-filesystem = %{version}-%{release}

%description manual
This package provides the User Guide and Haddock manual.
%endif

# needed for ghc-rpm-macros macros.ghc
%global with_hadrian 1

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
%ghc_lib_subpackage -d -l BSD-3-Clause Cabal-3.10.3.0
%ghc_lib_subpackage -d -l BSD-3-Clause Cabal-syntax-3.10.3.0
%ghc_lib_subpackage -d -l %BSDHaskellReport array-0.5.8.0
%ghc_lib_subpackage -d -l %BSDHaskellReport -c gmp-devel%{?_isa},libffi-devel%{?_isa} base-%{base_ver}
%ghc_lib_subpackage -d -l BSD-3-Clause binary-0.8.9.1
%ghc_lib_subpackage -d -l BSD-3-Clause bytestring-0.12.1.0
%ghc_lib_subpackage -d -l %BSDHaskellReport containers-0.6.8
%ghc_lib_subpackage -d -l %BSDHaskellReport deepseq-1.5.1.0
%ghc_lib_subpackage -d -l %BSDHaskellReport directory-1.3.8.5
%ghc_lib_subpackage -d -l %BSDHaskellReport exceptions-0.10.7
%ghc_lib_subpackage -d -l BSD-3-Clause filepath-1.4.301.0
# in ghc not ghc-libraries:
%ghc_lib_subpackage -d -x ghc-%{ghc_version_override}
%ghc_lib_subpackage -d -x -l BSD-3-Clause ghc-bignum-%{ghc_bignum_ver}
%ghc_lib_subpackage -d -x -l BSD-3-Clause ghc-boot-%{ghc_version_override}
%ghc_lib_subpackage -d -l BSD-3-Clause ghc-boot-th-%{ghc_version_override}
%ghc_lib_subpackage -d -x -l BSD-3-Clause ghc-compact-%{ghc_compact_ver}
%ghc_lib_subpackage -d -x -l BSD-3-Clause ghc-heap-%{ghc_version_override}
# see below for ghc-prim
%ghc_lib_subpackage -d -x -l BSD-3-Clause ghci-%{ghc_version_override}
%ghc_lib_subpackage -d -l BSD-3-Clause haskeline-0.8.2.1
%ghc_lib_subpackage -d -x -l BSD-3-Clause hpc-%{hpc_ver}
# see below for integer-gmp
%ghc_lib_subpackage -d -l BSD-3-Clause mtl-2.3.1
%ghc_lib_subpackage -d -l BSD-3-Clause parsec-3.1.17.0
%ghc_lib_subpackage -d -l BSD-3-Clause pretty-1.1.3.6
%ghc_lib_subpackage -d -l %BSDHaskellReport process-1.6.25.0
# see below for rts
%ghc_lib_subpackage -d -l BSD-3-Clause semaphore-compat-1.0.0
%ghc_lib_subpackage -d -l BSD-3-Clause stm-2.5.3.1
%ghc_lib_subpackage -d -l BSD-3-Clause template-haskell-2.21.0.0
%ghc_lib_subpackage -d -l BSD-3-Clause -c ncurses-devel%{?_isa} terminfo-0.4.1.6
%ghc_lib_subpackage -d -l BSD-3-Clause text-2.1.1
%ghc_lib_subpackage -d -l BSD-3-Clause time-1.12.2
%ghc_lib_subpackage -d -l BSD-3-Clause transformers-0.6.1.0
%ghc_lib_subpackage -d -l BSD-3-Clause unix-2.8.6.0
%ghc_lib_subpackage -d -l BSD-3-Clause xhtml-%{xhtml_ver}
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
%patch -P3 -p1 -b .orig
#%%patch -P2 -p1 -b .orig
#%%patch -P9 -p1 -b .orig

rm libffi-tarballs/libffi-*.tar.gz

%ifarch %{ghc_unregisterized_arches} riscv64
%patch -P16 -p1 -b .orig
%endif
# remove if epel9 ghc using llvm
%ifarch s390x
%if %{defined el9}
%patch -P16 -p1 -b .orig
%endif
%endif

#debian
#%%patch -P24 -p1 -b .orig
%patch -P26 -p1 -b .orig
%patch -P27 -p1 -b .orig

%ifarch riscv64
#RISCV64 cabal support
%patch -P40 -p1 -b .orig
#GHCi support
%patch -P41 -p1 -b .orig
%endif

# https://github.com/haskell/directory/pull/184
(
cd libraries/directory
%patch -P50 -p1 -b .orig
)


%build
# patch4
autoupdate

%ghc_set_gcc_flags
export CC=%{_bindir}/gcc
%if %{with ld_gold}
export LD=%{_bindir}/ld.gold
%endif

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

%if %{defined _ghcdynlibdir}
%undefine _ghcdynlibdir
%endif

%if %{with build_hadrian}
# do not disable debuginfo with ghc_bin_build
%global ghc_debuginfo 1
(
cd hadrian
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
# + hadrian/dist/build/hadrian/hadrian -j224 --flavour=perf --docs=no-sphinx-pdfs binary-dist-dir --hash-unit-ids
# # cabal-read (for OracleQ (PackageDataKey (Package {pkgType = Library, pkgName = "rts", pkgPath = "rts"})))
# rts/include/rts/Messages.h: withFile: resource exhausted (Too many open files)
# https://koji.fedoraproject.org/koji/taskinfo?taskID=111327221
%global _smp_ncpus_max 64
# quickest does not build shared libs
# try release instead of perf
%{hadrian} %{?_smp_mflags} --flavour=%[%{?with_perfbuild} ? "perf" : "quick"]%{!?with_ghc_prof:+no_profiled_libs}%{?hadrian_llvm} %{hadrian_docs} binary-dist-dir --hash-unit-ids


%install
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
./configure --prefix=%{buildroot}%{ghclibdir} --bindir=%{buildroot}%{_bindir} --libdir=%{buildroot}%{_libdir} --mandir=%{buildroot}%{_mandir} --docdir=%{buildroot}%{_docdir}/%{name} \
%if %{without ld_gold}
  --disable-ld-override
%endif
%{nil}
make install
)

%if "%{?_ghcdynlibdir}" != "%_libdir"
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo "%{ghclibplatform}" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}.conf
%else
for i in $(find %{buildroot} -type f -executable -exec sh -c "file {} | grep -q 'dynamically linked'" \; -print); do
  chrpath -d $i
done
%endif

%if %{with haddock}
# remove short hashes
for d in %{buildroot}%{ghc_html_libraries_dir}/*/; do
mv $d $(echo $d | sed -e "s/\(.*\)-.*/\\1/")
done
%endif

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
echo "%%dir %{ghcliblib}" >> %{name}-base%{?_ghcdynlibdir:-devel}.files
echo "%%dir %ghclibplatform" >> %{name}-base%{?_ghcdynlibdir:-devel}.files

%ghc_gen_filelists ghc %{ghc_version_override}
%ghc_gen_filelists ghc-bignum %{ghc_bignum_ver}
%ghc_gen_filelists ghc-boot %{ghc_version_override}
%ghc_gen_filelists ghc-compact %{ghc_compact_ver}
%ghc_gen_filelists ghc-heap %{ghc_version_override}
%ghc_gen_filelists ghci %{ghc_version_override}
%ghc_gen_filelists hpc %{hpc_ver}

%ghc_gen_filelists ghc-prim 0.11.0
%ghc_gen_filelists integer-gmp 1.1
%ghc_gen_filelists rts %{rts_ver}

%define merge_filelist()\
cat %{name}-%1.files >> %{name}-%2.files\
cat %{name}-%1-devel.files >> %{name}-%2-devel.files\
%if %{with haddock}\
cat %{name}-%1-doc.files >> %{name}-%2-doc.files\
%endif\
%if %{with ghc_prof}\
cat %{name}-%1-prof.files >> %{name}-%2-prof.files\
%endif\
if [ "%1" != "rts" ]; then\
cp -p libraries/%1/LICENSE libraries/LICENSE.%1\
echo "%%license libraries/LICENSE.%1" >> %{name}-%2.files\
fi\
%{nil}

%merge_filelist ghc-prim base
%merge_filelist integer-gmp base
%merge_filelist rts base

%if "%{?_ghcdynlibdir}" != "%_libdir"
echo "%{_sysconfdir}/ld.so.conf.d/%{name}.conf" >> %{name}-base.files
%endif

# add rts libs
for i in %{buildroot}%{ghclibplatform}/libHSrts*ghc%{ghc_version}.so; do
if [ "$(basename $i)" != "libHSrts-%{rts_ver}-ghc%{ghc_version}.so" ]; then
echo $i >> %{name}-base.files
fi
done

if [ -f %{buildroot}%{ghcliblib}/package.conf.d/system-cxx-std-lib-1.0.conf ]; then
ls -d %{buildroot}%{ghcliblib}/package.conf.d/system-cxx-std-lib-1.0.conf >> %{name}-base-devel.files
fi

%if %{with ghc_prof}
ls %{buildroot}%{ghclibdir}/bin/ghc-iserv-prof* >> %{name}-base-prof.files
ls %{buildroot}%{ghcliblib}/bin/ghc-iserv-prof >> %{name}-base-prof.files
%endif

sed -i -e "s|^%{buildroot}||g" %{name}-base*.files
sed -i -e "s|%{buildroot}||g" %{buildroot}%{_bindir}/*

mkdir -p %{buildroot}%{_mandir}/man1
install -p -m 0644 %{SOURCE5} %{buildroot}%{_mandir}/man1/ghc-pkg.1
install -p -m 0644 %{SOURCE6} %{buildroot}%{_mandir}/man1/haddock.1
install -p -m 0644 %{SOURCE7} %{buildroot}%{_mandir}/man1/runghc.1

%if %{with haddock}
rm %{buildroot}%{_pkgdocdir}/archives/libraries.html.tar.xz
%endif
%if %{with manual}
rm %{buildroot}%{_pkgdocdir}/archives/Haddock.html.tar.xz
rm %{buildroot}%{_pkgdocdir}/archives/users_guide.html.tar.xz
mv %{buildroot}%{_mandir}/man1/ghc{,-%{ghc_major}}.1
%endif

%if %{with build_hadrian}
mv %{buildroot}%{_bindir}/hadrian{,-%{ghc_major}}
%endif

rm %{buildroot}%{ghcliblib}/package.conf.d/.stamp
rm %{buildroot}%{ghcliblib}/package.conf.d/*.conf.copy

# https://gitlab.haskell.org/ghc/ghc/-/issues/24121
rm %{buildroot}%{ghclibdir}/share/doc/%ghcplatform/*/LICENSE

(cd %{buildroot}%{ghcliblib}/bin
for i in *; do
if [ -f %{buildroot}%{ghclibdir}/bin/$i ]; then
ln -sf ../../bin/$i
fi
done
)

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
export LD_LIBRARY_PATH=%{buildroot}%{ghclibplatform}:
GHC=%{buildroot}%{ghclibdir}/bin/ghc
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
%endif


%files

%files compiler
%license LICENSE
%doc README.md
%{_bindir}/ghc-%{version}
%{_bindir}/ghc-pkg-%{version}
%{_bindir}/ghci-%{version}
%{_bindir}/hp2ps-ghc-%{version}
%{_bindir}/hpc-ghc-%{version}
%{_bindir}/hsc2hs-ghc-%{version}
%{_bindir}/runghc-%{version}
%{_bindir}/runhaskell-%{version}
%{_bindir}/ghc-%{ghc_major}
%{_bindir}/ghc-pkg-%{ghc_major}
%{_bindir}/ghci-%{ghc_major}
%{_bindir}/runghc-%{ghc_major}
%{_bindir}/runhaskell-%{ghc_major}
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
%{ghcliblib}/ghc-interp.js
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

%{_bindir}/haddock-ghc-%{version}
%{ghcliblib}/html
%{ghcliblib}/latex
%if %{with haddock} || %{with manual}
%{ghc_html_libraries_dir}/prologue.txt
%endif
%if %{with haddock}
%verify(not size mtime) %{ghc_html_libraries_dir}/haddock-bundle.min.js
%verify(not size mtime) %{ghc_html_libraries_dir}/linuwial.css
%verify(not size mtime) %{ghc_html_libraries_dir}/quick-jump.css
%verify(not size mtime) %{ghc_html_libraries_dir}/synopsis.png
%endif
%if %{with manual}
%{_mandir}/man1/ghc-%{ghc_major}.1*
%endif

%files compiler-default
%{_bindir}/ghc
%{_bindir}/ghc-pkg
%{_bindir}/ghci
%{_bindir}/haddock
%{_bindir}/hp2ps
%{_bindir}/hpc
%{_bindir}/hsc2hs
%{_bindir}/runghc
%{_bindir}/runhaskell

%files devel

%if %{with haddock} || %{with manual}
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

%if %{with build_hadrian}
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
%{ghc_html_dir}/Haddock
%endif

%if %{with ghc_prof}
%files prof
%endif


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 9.8.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec  2 2024 Jens Petersen <petersen@redhat.com> - 9.8.4-12
- Update to 9.8.4
- https://downloads.haskell.org/~ghc/9.8.4/docs/users_guide/9.8.4-notes.html
- filepath-1.4.301 and unix-2.8.6

* Mon Oct 21 2024 Jens Petersen <petersen@redhat.com> - 9.8.3-11
- Update to 9.8.3
- https://downloads.haskell.org/~ghc/9.8.3/docs/users_guide/9.8.3-notes.html
- use ld.bfd

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.8.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 15 2024 Jens Petersen <petersen@redhat.com> - 9.8.2-9
- explicit requires for binutils
- boot with ghc9.6 for all releases
- ppc64le: NCG fix for ccall target hints (Peter Trommler, #2172771)

* Mon Feb 26 2024 Jens Petersen <petersen@redhat.com> - 9.8.2-8
- https://downloads.haskell.org/~ghc/9.8.2/docs/users_guide/9.8.2-notes.html
- minor bumps to bytestring, filepath, text, unix

* Thu Feb 15 2024 Richard W.M. Jones <rjones@redhat.com> - 9.8.1-7
- Fix generated C for Modern C Initiative

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Jens Petersen <petersen@redhat.com> - 9.8.1-5
- use gcc default ld (ie ld.bfd) for rawhide

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan  5 2024 Jens Petersen <petersen@redhat.com> - 9.8.1-3
- fix llvm alignment in data sections (@stefansf (IBM))
  which should fix certain runtime crashes (#2248097)

* Sun Nov 12 2023 Jens Petersen <petersen@redhat.com> - 9.8.1-2
- rebuild with ghc-rpm-macros-2.6.5 to fix prof deps (thanks mimi1vx)

* Thu Oct 26 2023 Jens Petersen <petersen@redhat.com> - 9.8.1-1
- https://downloads.haskell.org/ghc/9.8.1/docs/users_guide/9.8.1-notes.html

* Fri Aug 11 2023 Jens Petersen <petersen@redhat.com> - 9.8.0.20230809-0.2
- https://downloads.haskell.org/ghc/9.8.1-alpha2/docs/users_guide/9.8.1-notes.html

* Fri Aug  4 2023 Jens Petersen <petersen@redhat.com> - 9.8.0.20230727-0.1
- initial package based on ghc9.6
