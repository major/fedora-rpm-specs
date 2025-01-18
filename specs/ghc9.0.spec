# bcond_without for production builds:
# - performance build (disable for quick build)
%bcond_without perfbuild

# not for production builds
%if %{without perfbuild}
# disable profiling libraries (overriding macros.ghc-srpm)
%undefine with_ghc_prof
# disable haddock documentation (overriding macros.ghc-os)
%undefine with_haddock
%else
%bcond_without haddock
%endif

%global ghc_major 9.0
%global ghc_name ghc%{ghc_major}

%global base_ver 4.15.1.0
%global ghc_bignum_ver 1.1
%global ghc_compact_ver 0.1.0.0
%global hpc_ver 0.6.1.0
%global xhtml_ver 3000.2.2.1

# bootstrap needs 8.8+
%global ghcboot_major 9.0
%global ghcboot ghc%{ghcboot_major}

# locked together since disabling haddock causes no manuals built
# and disabling haddock still created index.html
# https://gitlab.haskell.org/ghc/ghc/-/issues/15190
%{?with_haddock:%bcond_without manual}

# make sure ghc libraries' ABI hashes unchanged
%bcond_without abicheck

# no longer build testsuite (takes time and not really being used)
%bcond_with testsuite

%if %{?fedora} >= 38
%global _ghcdynlibdir %{ghclibdir}
%endif

# 9.0.2 recommends llvm 9-12
%global llvm_major 12
%global ghc_llvm_archs armv7hl aarch64

%global ghc_unregisterized_arches s390 s390x %{mips} riscv64

Name: %{ghc_name}
Version: 9.0.2
# Since library subpackages are versioned:
# - release can only be reset if *all* library versions get bumped simultaneously
#   (sometimes after a major release)
# - minor release numbers for a branch should be incremented monotonically
Release: 19%{?dist}
Summary: Glasgow Haskell Compiler

License: BSD-3-Clause AND HaskellReport
URL: https://haskell.org/ghc/
Source0: https://downloads.haskell.org/ghc/%{version}/ghc-%{version}-src.tar.xz
%if %{with testsuite}
Source1: https://downloads.haskell.org/ghc/%{version}/ghc-%{version}-testsuite.tar.xz
%endif
Source5: ghc-pkg.man
Source6: haddock.man
Source7: runghc.man
# absolute haddock path (was for html/libraries -> libraries)
Patch1: ghc-gen_contents_index-haddock-path.patch
Patch2: ghc-Cabal-install-PATH-warning.patch
Patch3: ghc-gen_contents_index-nodocs.patch
# https://phabricator.haskell.org/rGHC4eebc8016f68719e1ccdf460754a97d1f4d6ef05
Patch6: ghc-8.6.3-sphinx-1.8.patch
# https://gitlab.haskell.org/ghc/ghc/-/merge_requests/7689
Patch7: 7689.patch
# https://fedoraproject.org/wiki/Toolchain/PortingToModernC
# https://gitlab.haskell.org/ghc/ghc/-/merge_requests/9394
Patch8: ghc-configure-c99.patch
# https://gitlab.haskell.org/ghc/ghc/-/issues/23286 (sphinx modern extlinks)
Patch9: https://gitlab.haskell.org/ghc/ghc/-/commit/00dc51060881df81258ba3b3bdf447294618a4de.patch
# distutils gone in python 3.12
# https://gitlab.haskell.org/ghc/ghc/-/merge_requests/10922
Patch10: 10922-9.0.patch

# Arch dependent patches
# arm
Patch12: ghc-armv7-VFPv3D16--NEON.patch

# for unregisterized
# https://gitlab.haskell.org/ghc/ghc/-/issues/15689
Patch15: ghc-warnings.mk-CC-Wall.patch

# llvm
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
Patch25: buildpath-abi-stability-2.patch
Patch26: no-missing-haddock-file-warning.patch
Patch27: haddock-remove-googleapis-fonts.patch

Patch30: https://src.opensuse.org/rpm/ghc/raw/branch/factory/sphinx7.patch

# ppc64le FFI miscompilation
# https://gitlab.haskell.org/ghc/ghc/-/issues/23034
Patch35: https://gitlab.haskell.org/ghc/ghc/-/merge_requests/12885.patch

# https://gitlab.haskell.org/ghc/ghc/-/wikis/platforms

# fedora ghc has been bootstrapped on
# %%{ix86} x86_64 s390x ppc64le aarch64 armv7hl
# and retired arches: alpha sparcv9 armv5tel ppc ppc64 s390
# see also deprecated ghc_arches defined in ghc-srpm-macros
# /usr/lib/rpm/macros.d/macros.ghc-srpm

BuildRequires: %{ghcboot}-compiler
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
BuildRequires: binutils-gold
BuildRequires: gmp-devel
BuildRequires: libffi-devel
BuildRequires: make
# for terminfo
BuildRequires: ncurses-devel
BuildRequires: perl-interpreter
%if %{with testsuite}
BuildRequires: python3
%endif
%if %{with manual}
BuildRequires: python3-sphinx
%endif
%ifarch %{ghc_llvm_archs}
BuildRequires: llvm%{llvm_major}
%endif
# patch8 and patch12
BuildRequires: autoconf automake
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
Requires: binutils-gold
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


%if %{with haddock}
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


# ghclibdir also needs ghc_version_override for bootstrapping
%global ghc_version_override %{version}

%global BSDHaskellReport %{quote:BSD-3-Clause AND HaskellReport}

# use "./libraries-versions.sh" to check versions
%if %{defined ghclibdir}
%ghc_lib_subpackage -d -l BSD-3-Clause Cabal-3.4.1.0
%ghc_lib_subpackage -d -l %BSDHaskellReport array-0.5.4.0
%ghc_lib_subpackage -d -l %BSDHaskellReport -c gmp-devel%{?_isa},libffi-devel%{?_isa} base-%{base_ver}
%ghc_lib_subpackage -d -l BSD-3-Clause binary-0.8.8.0
%ghc_lib_subpackage -d -l BSD-3-Clause bytestring-0.10.12.1
%ghc_lib_subpackage -d -l %BSDHaskellReport containers-0.6.4.1
%ghc_lib_subpackage -d -l %BSDHaskellReport deepseq-1.4.5.0
%ghc_lib_subpackage -d -l %BSDHaskellReport directory-1.3.6.2
%ghc_lib_subpackage -d -l %BSDHaskellReport exceptions-0.10.4
%ghc_lib_subpackage -d -l BSD-3-Clause filepath-1.4.2.1
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
%ghc_lib_subpackage -d -l BSD-3-Clause mtl-2.2.2
%ghc_lib_subpackage -d -l BSD-3-Clause parsec-3.1.14.0
%ghc_lib_subpackage -d -l BSD-3-Clause pretty-1.1.3.6
%ghc_lib_subpackage -d -l %BSDHaskellReport process-1.6.13.2
%ghc_lib_subpackage -d -l BSD-3-Clause stm-2.5.0.0
%ghc_lib_subpackage -d -l BSD-3-Clause template-haskell-2.17.0.0
%ghc_lib_subpackage -d -l BSD-3-Clause -c ncurses-devel%{?_isa} terminfo-0.4.1.5
%ghc_lib_subpackage -d -l BSD-3-Clause text-1.2.5.0
%ghc_lib_subpackage -d -l BSD-3-Clause time-1.9.3
%ghc_lib_subpackage -d -l BSD-3-Clause transformers-0.5.6.2
%ghc_lib_subpackage -d -l BSD-3-Clause unix-2.7.2.2
%if %{with haddock}
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
# ghc-9.0.2 release anomaly
rm -r libraries/containers/containers/dist-install

%patch -P1 -p1 -b .orig
%patch -P3 -p1 -b .orig

%patch -P2 -p1 -b .orig
%patch -P6 -p1 -b .orig
%patch -P7 -p1 -b .orig
%patch -P8 -p1 -b .orig
%patch -P9 -p1 -b .orig
%patch -P10 -p1 -b .orig

rm -r libffi-tarballs

%ifarch armv7hl
%patch -P12 -p1 -b .orig12
%endif

%ifarch %{ghc_unregisterized_arches}
%patch -P15 -p1 -b .orig
%endif

# llvm
%patch -P17 -p1 -b .orig

%ifarch s390x
# bigendian
%patch -P18 -p1 -b .orig
%endif

#debian
%patch -P24 -p1 -b .orig
%patch -P25 -p1 -b .orig
%patch -P26 -p1 -b .orig
%patch -P27 -p1 -b .orig

#sphinx 7
%if 0%{?fedora} >= 40
%patch -P30 -p1 -b .orig
%endif

%ifarch ppc64le
%patch -P 35 -p1 -b .orig
%endif

%if %{with haddock}
%global gen_contents_index gen_contents_index.orig
if [ ! -f "libraries/%{gen_contents_index}" ]; then
  echo "Missing libraries/%{gen_contents_index}, needed at end of %%install!"
  exit 1
fi
%endif

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

%build
# for patch8 and patch12
autoreconf

%ghc_set_gcc_flags
export CC=%{_bindir}/gcc
export LD=%{_bindir}/ld.gold

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
  GHC=%{_bindir}/ghc-%{ghcboot_major} \
%{nil}

# avoid "ghc: hGetContents: invalid argument (invalid byte sequence)"
export LANG=C.utf8
make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install

%if %{defined _ghcdynlibdir}
mv %{buildroot}%{ghclibdir}/*/libHS*ghc%{ghc_version}.so %{buildroot}%{_ghcdynlibdir}/
for i in %{buildroot}%{ghclibdir}/package.conf.d/*.conf; do
  sed -i -e 's!^dynamic-library-dirs: .*!dynamic-library-dirs: %{_ghcdynlibdir}!' $i
done
sed -i -e 's!^library-dirs: %{ghclibdir}/rts!&\ndynamic-library-dirs: %{_ghcdynlibdir}!' %{buildroot}%{ghclibdir}/package.conf.d/rts.conf
%endif

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

%ghc_gen_filelists ghc %{ghc_version_override}
%ghc_gen_filelists ghc-bignum %{ghc_bignum_ver}
%ghc_gen_filelists ghc-boot %{ghc_version_override}
%ghc_gen_filelists ghc-compact %{ghc_compact_ver}
%ghc_gen_filelists ghc-heap %{ghc_version_override}
%ghc_gen_filelists ghci %{ghc_version_override}
%ghc_gen_filelists hpc %{hpc_ver}
%ghc_gen_filelists libiserv %{ghc_version_override}

%ghc_gen_filelists ghc-prim 0.7.0
%ghc_gen_filelists integer-gmp 1.1

%define merge_filelist()\
cat %{name}-%1.files >> %{name}-%2.files\
cat %{name}-%1-devel.files >> %{name}-%2-devel.files\
%if %{with haddock}\
cat %{name}-%1-doc.files >> %{name}-%2-doc.files\
%endif\
%if %{with ghc_prof}\
cat %{name}-%1-prof.files >> %{name}-%2-prof.files\
%endif\
cp -p libraries/%1/LICENSE libraries/LICENSE.%1\
echo "%%license libraries/LICENSE.%1" >> %{name}-%2.files\
%{nil}

%merge_filelist ghc-prim base
%merge_filelist integer-gmp base

%if "%{?_ghcdynlibdir}" != "%_libdir"
echo "%{_sysconfdir}/ld.so.conf.d/%{name}.conf" >> %{name}-base.files
%endif

# add rts libs
%if "%{?_ghcdynlibdir}" == "%_libdir"
echo "%{ghclibdir}/rts" >> %{name}-base-devel.files
%else
echo "%%dir %{ghclibdir}/rts" >> %{name}-base.files
ls -d %{buildroot}%{ghclibdir}/rts/lib*.a >> %{name}-base-devel.files
%endif
ls %{buildroot}%{?_ghcdynlibdir}%{!?_ghcdynlibdir:%{ghclibdir}/rts}/libHSrts*.so >> %{name}-base.files
%if %{defined _ghcdynlibdir}
sed -i -e 's!^library-dirs: %{ghclibdir}/rts!&\ndynamic-library-dirs: %{_ghcdynlibdir}!' %{buildroot}%{ghclibdir}/package.conf.d/rts.conf
%endif
ls -d %{buildroot}%{ghclibdir}/package.conf.d/rts.conf >> %{name}-base-devel.files

ls -d %{buildroot}%{ghclibdir}/include >> %{name}-base-devel.files

%if %{with ghc_prof}
ls %{buildroot}%{ghclibdir}/bin/ghc-iserv-prof* >> %{name}-base-prof.files
%endif

sed -i -e "s|^%{buildroot}||g" %{name}-base*.files

%if %{with haddock}
# generate initial lib doc index
cd libraries
sh %{gen_contents_index} --intree --verbose
cd ..
%endif

# we package the library license files separately
find %{buildroot}%{ghc_html_libraries_dir} -name LICENSE -exec rm '{}' ';'

mkdir -p %{buildroot}%{_mandir}/man1
install -p -m 0644 %{SOURCE5} %{buildroot}%{_mandir}/man1/ghc-pkg.1
install -p -m 0644 %{SOURCE6} %{buildroot}%{_mandir}/man1/haddock.1
install -p -m 0644 %{SOURCE7} %{buildroot}%{_mandir}/man1/runghc.1
%if %{with manual}
mv %{buildroot}%{_mandir}/man1/{ghc,%{name}}.1
%endif

%ifarch armv7hl
export RPM_BUILD_NCPUS=1
%endif

for i in hp2ps hpc hsc2hs runhaskell; do
  mv %{buildroot}%{_bindir}/$i{,-%{version}}
  ln -s $i-%{version} %{buildroot}%{_bindir}/$i
done

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
GHC=inplace/bin/ghc-stage2
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
if [ "%{version}" = "$(ghc-%{version} --numeric-version)" ]; then
  echo "Checking package ABI hashes:"
  for i in %{ghc_packages_list}; do
    old=$(ghc-pkg-%{ghc_version} field $i id --simple-output || :)
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
  echo "ABI hash checks skipped: GHC changed from $(ghc-%{ghc_version} --numeric-version) to %{version}"
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

%transfiletriggerin compiler -- %{ghclibdir}/package.conf.d
%ghc_pkg_recache
%end

%transfiletriggerpostun compiler -- %{ghclibdir}/package.conf.d
%ghc_pkg_recache
%end


%if %{with haddock}
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
%{_bindir}/hp2ps-%{version}
%{_bindir}/hpc-%{version}
%{_bindir}/hsc2hs-%{version}
%{_bindir}/runghc-%{version}
%{_bindir}/runhaskell-%{version}
%{_bindir}/ghc-%{ghc_major}
%{_bindir}/ghc-pkg-%{ghc_major}
%{_bindir}/ghci-%{ghc_major}
%{_bindir}/runghc-%{ghc_major}
%{_bindir}/runhaskell-%{ghc_major}
%{_bindir}/hp2ps-%{ghc_major}
%{_bindir}/hpc-%{ghc_major}
%{_bindir}/hsc2hs-%{ghc_major}
%dir %{ghclibdir}/bin
%{ghclibdir}/bin/ghc
%{ghclibdir}/bin/ghc-iserv
%{ghclibdir}/bin/ghc-iserv-dyn
%if %{with ghc_prof}
%{ghclibdir}/bin/ghc-iserv-prof
%endif
%{ghclibdir}/bin/ghc-pkg
%{ghclibdir}/bin/hpc
%{ghclibdir}/bin/hsc2hs
%{ghclibdir}/bin/runghc
%{ghclibdir}/bin/hp2ps
%{ghclibdir}/bin/unlit
%{ghclibdir}/ghc-usage.txt
%{ghclibdir}/ghci-usage.txt
%{ghclibdir}/llvm-passes
%{ghclibdir}/llvm-targets
%dir %{ghclibdir}/package.conf.d
%ghost %{ghclibdir}/package.conf.d/package.cache
%{ghclibdir}/package.conf.d/package.cache.lock
%{ghclibdir}/platformConstants
%{ghclibdir}/settings
%{ghclibdir}/template-hsc.h
%{_mandir}/man1/ghc-pkg.1*
%{_mandir}/man1/haddock.1*
%{_mandir}/man1/runghc.1*

%if %{with haddock}
%{_bindir}/haddock-ghc-%{version}
%{ghclibdir}/bin/haddock
%{ghclibdir}/html
%{ghclibdir}/latex
%{ghc_html_libraries_dir}/prologue.txt
%verify(not size mtime) %{ghc_html_libraries_dir}/haddock-bundle.min.js
%verify(not size mtime) %{ghc_html_libraries_dir}/linuwial.css
%verify(not size mtime) %{ghc_html_libraries_dir}/quick-jump.css
%verify(not size mtime) %{ghc_html_libraries_dir}/synopsis.png
%endif
%if %{with manual}
%{_mandir}/man1/%{name}.1*
%endif

%files compiler-default
%{_bindir}/ghc
%{_bindir}/ghc-pkg
%{_bindir}/ghci
%if %{with haddock}
%{_bindir}/haddock
%endif
%{_bindir}/hp2ps
%{_bindir}/hpc
%{_bindir}/hsc2hs
%{_bindir}/runghc
%{_bindir}/runhaskell

%files devel

%if %{with haddock}
%files doc

%files doc-index
%{ghc_html_libraries_dir}/gen_contents_index
%verify(not size mtime) %{ghc_html_libraries_dir}/doc-index*.html
%verify(not size mtime) %{ghc_html_libraries_dir}/index*.html

%files filesystem
%dir %_ghc_doc_dir
%dir %ghc_html_dir
%dir %ghc_html_libraries_dir
%endif

%if %{with manual}
%files manual
## needs pandoc
#%%{ghc_html_dir}/Cabal
%if %{with haddock}
%{ghc_html_dir}/haddock
%{ghc_html_dir}/index.html
%{ghc_html_dir}/users_guide
%endif
%endif

%if %{with ghc_prof}
%files prof
%endif


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 15 2024 Jens Petersen <petersen@redhat.com> - 9.0.2-17
- explicit requires binutils-gold
- ppc64le: NCG fix for ccall target hints (Peter Trommler, #2172771)
- llvm patch from @stefansf (IBM) to fix alignment in data sections
  which should fix certain runtime crashes (#2248097)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb 15 2023 Jens Petersen <petersen@redhat.com> - 9.0.2-13
- move shared libraries into ghc libdir

* Sat Feb 11 2023 Jens Petersen <petersen@redhat.com> - 9.0.2-12
- self boot with ghc9.0
- use llvm12 (for ARM)
- sync changes from ghc8.10 and ghc 9.2
- debian buildpath-abi-stability-2 & haddock-remove-googleapis-fonts patches

* Sun Feb 05 2023 Florian Weimer <fweimer@redhat.com> - 9.0.2-11
- Port configure script to C99

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 11 2022 Jens Petersen <petersen@redhat.com> - 9.0.2-9
- add filesystem subpackage

* Tue May 24 2022 Jens Petersen <petersen@redhat.com> - 9.0.2-8
- backport fix from ghc-9.0 branch for CAFfy exception closures
  https://gitlab.haskell.org/ghc/ghc/-/merge_requests/7689

* Sun May  1 2022 Jens Petersen <petersen@redhat.com> - 9.0.2-7
- ghc9.0 now recommends ghc9.0-compiler-default
- recommends zlib-devel was moved to cabal-install/stack

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 Miro Hrončok <mhroncok@redhat.com> - 9.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/LIBFFI34

* Wed Jan  5 2022 Jens Petersen <petersen@redhat.com> - 9.0.2-4
- rebuild with fixed ghc-rpm-macros to fix broken ghc-ghci-devel metadeps

* Fri Dec 31 2021 Jens Petersen <petersen@redhat.com> - 9.0.2-3
- add compiler-default subpackage
- move docs to ghc9.0/ dir
- add 9.0 suffix to ghc.1 manpage

* Sun Dec 26 2021 Jens Petersen <petersen@redhat.com> - 9.0.2-2
- update to 9.0.2
- https://downloads.haskell.org/~ghc/9.0.2/docs/html/users_guide/9.0.2-notes.html
- use llvm11 for ARM

* Thu Dec 23 2021 Jens Petersen <petersen@redhat.com> - 9.0.1-1
- initial package derived from ghc:9.0 and ghc9.2
- https://downloads.haskell.org/ghc/9.0.1/docs/html/users_guide/9.0.1-notes.html
- uses llvm10 on ARM archs
