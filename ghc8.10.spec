# disable prof, docs, perf build, debuginfo
# NB This must be disabled (bcond_with) for all koji production builds
%bcond_with quickbuild

# make sure ghc libraries' ABI hashes unchanged
%bcond_with abicheck

%global ghc_name ghc8.10

# to handle RCs
%global ghc_release %{version}

%global base_ver 4.14.3.0

# build profiling libraries
# build haddock
# perf production build (disable for quick build)
%if %{with quickbuild}
%undefine with_ghc_prof
%undefine with_haddock
%bcond_with perf_build
%undefine _enable_debug_packages
%else
%bcond_without ghc_prof
%bcond_without haddock
%bcond_without perf_build
%endif

# locked together since disabling haddock causes no manuals built
# and disabling haddock still created index.html
# https://ghc.haskell.org/trac/ghc/ticket/15190
%{?with_haddock:%bcond_without manual}

# no longer build testsuite (takes time and not really being used)
%bcond_with testsuite

# 8.10 can use llvm 9-12
%if 0%{?fedora} >= 33
%global llvm_major 11
%else
%global llvm_major 10
%endif
%global ghc_llvm_archs armv7hl aarch64

%global ghc_unregisterized_arches s390 s390x %{mips} riscv64

Name: %{ghc_name}
Version: 8.10.7
# Since library subpackages are versioned:
# - release can only be reset if *all* library versions get bumped simultaneously
#   (sometimes after a major release)
# - minor release numbers for a branch should be incremented monotonically
Release: 6%{?dist}
Summary: Glasgow Haskell Compiler

License: BSD and HaskellReport
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
# https://phabricator.haskell.org/rGHC4eebc8016f68719e1ccdf460754a97d1f4d6ef05
Patch6: ghc-8.6.3-sphinx-1.8.patch

# Arch dependent patches
# arm
Patch12: ghc-armv7-VFPv3D16--NEON.patch

# for unregisterized
# https://ghc.haskell.org/trac/ghc/ticket/15689
Patch15: ghc-warnings.mk-CC-Wall.patch

# bigendian (s390x and ppc64)
# https://gitlab.haskell.org/ghc/ghc/issues/15411
# https://gitlab.haskell.org/ghc/ghc/issues/16505
# https://bugzilla.redhat.com/show_bug.cgi?id=1651448
# https://ghc.haskell.org/trac/ghc/ticket/15914
# https://gitlab.haskell.org/ghc/ghc/issues/16973
# https://bugzilla.redhat.com/show_bug.cgi?id=1733030
Patch18: Disable-unboxed-arrays.patch

# Debian patches:
Patch24: buildpath-abi-stability.patch
Patch26: no-missing-haddock-file-warning.patch

Patch27: ghc-configure-c99.patch

# fedora ghc has been bootstrapped on
# %%{ix86} x86_64 ppc ppc64 armv7hl s390 s390x ppc64le aarch64
# and retired arches: alpha sparcv9 armv5tel
# see also deprecated ghc_arches defined in ghc-srpm-macros
# /usr/lib/rpm/macros.d/macros.ghc-srpm

BuildRequires: ghc-compiler > 8.6
# for ABI hash checking
%if %{with abicheck}
BuildRequires: %{name}
%endif
BuildRequires: ghc-rpm-macros-extra
BuildRequires: ghc-binary-devel
BuildRequires: ghc-bytestring-devel
BuildRequires: ghc-containers-devel
BuildRequires: ghc-directory-devel
BuildRequires: ghc-pretty-devel
BuildRequires: ghc-process-devel
BuildRequires: ghc-stm-devel
BuildRequires: ghc-template-haskell-devel
BuildRequires: ghc-transformers-devel
BuildRequires: alex
BuildRequires: gmp-devel
BuildRequires: hscolour
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
%if 0%{?fedora} >= 34
BuildRequires: llvm%{llvm_major}
%else
BuildRequires: llvm = %{llvm_major}
%endif
%endif
%ifarch armv7hl
# patch12
BuildRequires: autoconf, automake
%endif
Requires: %{name}-compiler = %{version}-%{release}
Requires: %{name}-devel = %{version}-%{release}
Requires: %{name}-ghc-devel = %{version}-%{release}
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
%if 0%{?fedora} >= 34
Requires: llvm%{llvm_major}
%else
Requires: llvm = %{llvm_major}
%endif
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

%global BSDHaskellReport %{quote:BSD and HaskellReport}

# use "./libraries-versions.sh" to check versions
%if %{defined ghclibdir}
%ghc_lib_subpackage -d -l BSD Cabal-3.2.1.0
%ghc_lib_subpackage -d -l %BSDHaskellReport array-0.5.4.0
%ghc_lib_subpackage -d -l %BSDHaskellReport -c gmp-devel%{?_isa},libffi-devel%{?_isa} base-%{base_ver}
%ghc_lib_subpackage -d -l BSD binary-0.8.8.0
%ghc_lib_subpackage -d -l BSD bytestring-0.10.12.0
%ghc_lib_subpackage -d -l %BSDHaskellReport containers-0.6.5.1
%ghc_lib_subpackage -d -l %BSDHaskellReport deepseq-1.4.4.0
%ghc_lib_subpackage -d -l %BSDHaskellReport directory-1.3.6.0
%ghc_lib_subpackage -d -l %BSDHaskellReport exceptions-0.10.4
%ghc_lib_subpackage -d -l BSD filepath-1.4.2.1
# in ghc not ghc-libraries:
%ghc_lib_subpackage -d -x ghc-%{ghc_version_override}
%ghc_lib_subpackage -d -x -l BSD ghc-boot-%{ghc_version_override}
%ghc_lib_subpackage -d -l BSD ghc-boot-th-%{ghc_version_override}
%ghc_lib_subpackage -d -l BSD ghc-compact-0.1.0.0
%ghc_lib_subpackage -d -l BSD ghc-heap-%{ghc_version_override}
# see below for ghc-prim
%ghc_lib_subpackage -d -l BSD -x ghci-%{ghc_version_override}
%ghc_lib_subpackage -d -l BSD haskeline-0.8.2
%ghc_lib_subpackage -d -l BSD hpc-0.6.1.0
# see below for integer-gmp
%ghc_lib_subpackage -d -l %BSDHaskellReport libiserv-%{ghc_version_override}
%ghc_lib_subpackage -d -l BSD mtl-2.2.2
%ghc_lib_subpackage -d -l BSD parsec-3.1.14.0
%ghc_lib_subpackage -d -l BSD pretty-1.1.3.6
%ghc_lib_subpackage -d -l %BSDHaskellReport process-1.6.13.2
%ghc_lib_subpackage -d -l BSD stm-2.5.0.1
%ghc_lib_subpackage -d -l BSD template-haskell-2.16.0.0
%ghc_lib_subpackage -d -l BSD -c ncurses-devel%{?_isa} terminfo-0.4.1.4
%ghc_lib_subpackage -d -l BSD text-1.2.4.1
%ghc_lib_subpackage -d -l BSD time-1.9.3
%ghc_lib_subpackage -d -l BSD transformers-0.5.6.2
%ghc_lib_subpackage -d -l BSD unix-2.7.2.2
%if %{with haddock}
%ghc_lib_subpackage -d -l BSD xhtml-3000.2.2.1
%endif
%endif

%global version %{ghc_version_override}

%package devel
Summary: GHC development libraries meta package
License: BSD and HaskellReport
Requires: %{name}-compiler = %{version}-%{release}
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
%patch6 -p1 -b .orig

rm -r libffi-tarballs

%ifarch armv7hl
%patch12 -p1 -b .orig12
%endif

# remove s390x after switching to llvm
%ifarch %{ghc_unregisterized_arches} s390x
%patch15 -p1 -b .orig
%endif

# bigendian
%ifarch ppc64 s390x
%patch18 -p1 -b .orig
%endif

# debian
%patch24 -p1 -b .orig
%patch26 -p1 -b .orig

%patch27 -p1

%if %{with haddock}
%global gen_contents_index gen_contents_index.orig
if [ ! -f "libraries/%{gen_contents_index}" ]; then
  echo "Missing libraries/%{gen_contents_index}, needed at end of %%install!"
  exit 1
fi
%endif

# http://ghc.haskell.org/trac/ghc/wiki/Platforms
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

%build
# for patch12
%ifarch armv7hl
autoreconf
%endif

%ghc_set_gcc_flags
export CC=%{_bindir}/gcc

# only needed for ghc < 8.8
%ifarch %{ghc_unregisterized_arches} && 0%{?fedora} < 33
cat > ghc-unregisterised-wrapper << EOF
#!/usr/bin/sh
exec /usr/bin/ghc -optc-I%{_libdir}/ghc-$(ghc --numeric-version)/include \${1+"\$@"}
EOF
chmod a+x ghc-unregisterised-wrapper
ln -s /usr/bin/ghc-pkg ghc-pkg-unregisterised-wrapper
%endif

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
%ifarch %{ghc_unregisterized_arches} && 0%{?fedora} < 33
  GHC=$PWD/ghc-unregisterised-wrapper \
%endif
%{nil}

# avoid "ghc: hGetContents: invalid argument (invalid byte sequence)"
export LANG=C.utf8
make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install
%if %{defined _ghcdynlibdir}
mv %{buildroot}%{ghclibdir}/*/libHS*ghc%{ghc_version}.so %{buildroot}%{_ghcdynlibdir}/
for i in $(find %{buildroot} -type f -executable -exec sh -c "file {} | grep -q 'dynamically linked'" \; -print); do
  chrpath -d $i
done
for i in %{buildroot}%{ghclibdir}/package.conf.d/*.conf; do
  sed -i -e 's!^dynamic-library-dirs: .*!dynamic-library-dirs: %{_ghcdynlibdir}!' $i
done
sed -i -e 's!^library-dirs: %{ghclibdir}/rts!&\ndynamic-library-dirs: %{_ghcdynlibdir}!' %{buildroot}%{ghclibdir}/package.conf.d/rts.conf
%endif

# containers src moved to a subdir
cp -p libraries/containers/containers/LICENSE libraries/containers/LICENSE

for i in %{ghc_packages_list}; do
name=$(echo $i | sed -e "s/\(.*\)-.*/\1/")
ver=$(echo $i | sed -e "s/.*-\(.*\)/\1/")
%ghc_gen_filelists $name $ver
echo "%%license libraries/$name/LICENSE" >> %{name}-$name.files
done

echo "%%dir %{ghclibdir}" >> %{name}-base%{?_ghcdynlibdir:-devel}.files

%ghc_gen_filelists ghc %{ghc_version_override}
%ghc_gen_filelists ghc-boot %{ghc_version_override}
%ghc_gen_filelists ghci %{ghc_version_override}

%ghc_gen_filelists ghc-prim 0.6.1
%ghc_gen_filelists integer-gmp 1.0.3.0

%define merge_filelist()\
cat %{name}-%1.files >> %{name}-%2.files\
cat %{name}-%1-devel.files >> %{name}-%2-devel.files\
%if %{defined ghc_devel_prof}\
cat %{name}-%1-doc.files >> %{name}-%2-doc.files\
cat %{name}-%1-prof.files >> %{name}-%2-prof.files\
%endif\
cp -p libraries/%1/LICENSE libraries/LICENSE.%1\
echo "%%license libraries/LICENSE.%1" >> %{name}-%2.files\
%{nil}

%merge_filelist ghc-prim base
%merge_filelist integer-gmp base

# add rts libs
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
ls -d %{buildroot}%{ghclibdir}/package.conf.d/rts.conf %{buildroot}%{ghclibdir}/include >> %{name}-base-devel.files

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
%endif

%files filesystem
%dir %_ghc_doc_dir
%dir %ghc_html_dir
%dir %ghc_html_libraries_dir

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
* Mon Jan 16 2023 Florian Weimer <fweimer@redhat.com> - 8.10.7-6
- Port configure script to C99

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.10.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 12 2022 Jens Petersen <petersen@redhat.com> - 8.10.7-4
- add filesystem subpackage
- ghc8.10 now recommends ghc8.10-compiler-default
- recommends zlib-devel was moved to cabal-install/stack

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.10.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 Miro Hrončok <mhroncok@redhat.com> - 8.10.7-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/LIBFFI34

* Wed Jan  5 2022 Jens Petersen <petersen@redhat.com> - 8.10.7-1
- derived from ghc:8.10 module and ghc9.0 package
- the compiler-default subpackage allows making this the default ghc
