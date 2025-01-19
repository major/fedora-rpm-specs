%global uvcommit ca3a5a431a1c37859b6508e6b2a288092337029a
%global uvversion 1.48.0

%global llvmversion 16.0.6
%global llvmversionmaj 16
%global llvmcommit julia-16.0.6-2

%global libwhichversion 1.1.0
%global libwhichcommit 81e9723c0273d78493dc8c8ed570f68d9ce7e89e

%global blastrampolineversion 5.11.0
%global blastrampolinecommit 05083d50611b5538df69706f0a952d8e642b0b4b

%global libunwindversion 1.7.2

%global ittapiversion 3.24.0
%global ittapicommit 0014aec56fea2f30c1374f40861e1bccdd53d0cb

%global curlversion 8.6.0

%global libssh2version 1.11.0
%global libssh2commit 1c3f1b7da588f2652260285529ec3c1f1125eb4e

%global gmpversion 6.3.0

%global mbedtlsversion 2.28.6

%global terminfoversion 2023.12.9
%global terminfocommit TermInfoDB-v%{terminfoversion}+0

%global juliasyntaxcommit 4f1731d6ce7c2465fc21ea245110b7a39f34658a
%global juliasyntaxhighlightingcommit 4110caaf4fcdf0c614fd3ecd7c5bf589ca82ac63

%global logocommit 168fb6c1164e341df360ed6ced519e1e0cb7de3a

# List all bundled libraries here
# OpenBLAS is excluded because we set a symlink to libopenblasp
%global _privatelibs lib(openblas_|openblas64_|ccalltest|llvmcalltest|LLVM-.*|uv|blastrampoline|unwind|gmp|gmpxx|ssh2|mbed.*|curl)\\.so.*
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$

# Some binaries confuse debuginfo check
%undefine _missing_build_ids_terminate_build

Name:           julia
Version:        1.11.0
Release:        13.rc3%{?dist}.1
Summary:        High-level, high-performance dynamic language for technical computing
# Julia itself is MIT
# libuv, libwhich, libblastrampoline and libunwind are MIT
# LLVM is Apache-2.0 WITH LLVM-exception
License:        MIT and Apache-2.0-WITH-LLVM-exception
URL:            http://julialang.org/
Source0:        https://github.com/JuliaLang/julia/releases/download/v1.11.0-rc3/julia-1.11.0-rc3.tar.gz
# Julia currently uses a custom version of libuv, patches are not yet upstream
Source1:        https://api.github.com/repos/JuliaLang/libuv/tarball/%{uvcommit}#/libuv-%{uvcommit}.tar.gz
Source2:        https://api.github.com/repos/JuliaLang/llvm-project/tarball/%{llvmcommit}#/llvm-%{llvmcommit}.tar.gz
Source3:        https://api.github.com/repos/vtjnash/libwhich/tarball/%{libwhichcommit}#/libwhich-%{libwhichcommit}.tar.gz
Source4:        https://gmplib.org/download/gmp/gmp-%{gmpversion}.tar.bz2
Source5:        https://api.github.com/repos/JuliaLang/JuliaSyntax.jl/tarball/%{juliasyntaxcommit}#/JuliaSyntax-%{juliasyntaxcommit}.tar.gz
Source6:        https://raw.githubusercontent.com/JuliaLang/julia-logo-graphics/%{logocommit}/images/julia-logo-color.svg
Source7:        https://api.github.com/repos/staticfloat/libblastrampoline/tarball/%{blastrampolinecommit}#/blastrampoline-%{blastrampolinecommit}.tar.gz
Source8:        https://github.com/libunwind/libunwind/releases/download/v%{libunwindversion}/libunwind-%{libunwindversion}.tar.gz
Source9:        https://api.github.com/repos/intel/ittapi/tarball/%{ittapicommit}#/ittapi-%{ittapicommit}.tar.gz
Source10:       https://api.github.com/repos/JuliaLang/JuliaSyntaxHighlighting.jl/tarball/%{juliasyntaxhighlightingcommit}#/JuliaSyntaxHiglighting-%{juliasyntaxhighlightingcommit}.tar.gz
Source11:       https://curl.se/download/curl-%{curlversion}.tar.bz2
Source12:       https://api.github.com/repos/libssh2/libssh2/tarball/%{libssh2commit}#/libssh2-%{libssh2commit}.tar.gz
Source13:       https://github.com/Mbed-TLS/mbedtls/archive/v%{mbedtlsversion}.tar.gz#/mbedtls-%{mbedtlsversion}.tar.gz
# https://github.com/JuliaLang/julia/pull/54367
Patch0:         julia-Build-mbedTLS-libssh2-nghttp2-and-curl-disregarding.patch
Provides:       bundled(libuv) = %{uvversion}
Provides:       bundled(llvm) = %{llvmversion}
Provides:       bundled(libblastrampoline) = %{blastrampolineversion}
Provides:       bundled(libwhich) = %{libwhichversion}
Provides:       bundled(libunwind) = %{libunwindversion}
Provides:       bundled(ittapi) = %{ittapiversion}
Provides:       bundled(gmp) = %{gmpversion}
# Fedora libssh2 and libcurl link to a recent OpenSSL, which creates conflicts
# with packages that load the LTS version and expect Julia not to link to another one
# mbedTLS needs to be bundled too when bundling these two libraries
Provides:       bundled(libssh2) = %{libssh2version}
Provides:       bundled(libcurl) = %{curlversion}
Provides:       bundled(mbedtls) = %{mbedtlsversion}
BuildRequires:  ca-certificates
BuildRequires:  desktop-file-utils
BuildRequires:  dSFMT-devel
BuildRequires:  execstack
BuildRequires:  gcc
BuildRequires:  gcc-gfortran
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel >= 5.0
# Needed for libgit2 test
BuildRequires:  hostname
BuildRequires:  ImageMagick
BuildRequires:  libatomic
BuildRequires:  libunwind-devel >= 1.5
BuildRequires:  openblas-devel
BuildRequires:  openblas-threads
BuildRequires:  openlibm-devel >= 0.4
BuildRequires:  libgit2-devel
# Needed for libgit2 test
BuildRequires:  openssl
BuildRequires:  mbedtls-devel
BuildRequires:  libssh2-devel
BuildRequires:  http-parser-devel
BuildRequires:  openssl-devel
BuildRequires:  libcurl-devel
BuildRequires:  libcurl-full
BuildRequires:  libnghttp2-devel
BuildRequires:  curl-full
BuildRequires:  pcre2-devel
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  mpfr-devel >= 4
# Needed to build gmp
BuildRequires:  m4
BuildRequires:  patchelf
BuildRequires:  perl
BuildRequires:  p7zip-plugins
%if 0%{?__isa_bits} == 64
BuildRequires:  suitesparse64_-devel >= 7.6
%else
BuildRequires:  suitesparse-devel >= 7.6
%endif
BuildRequires:  utf8proc-devel >= 2.1
BuildRequires:  zlib-devel
Requires:       julia-common = %{version}-%{release}
Requires:       ca-certificates
# For terminfo files
Requires:       ncurses-base
Requires:       p7zip-plugins
# Libraries used by CompilerSupportLibraries_jll and blastrampoline
# but not detected as they are dlopen()ed but not linked to
%if 0%{?__isa_bits} == 64
Requires:       libgfortran.so.5()(64bit)
Requires:       libgomp.so.1()(64bit)
Requires:       libopenblasp64_.so.0()(64bit)
Requires:       libquadmath.so.0()(64bit)
Requires:       suitesparse64_
%else
Requires:       libgfortran.so.5
Requires:       libgomp.so.1
Requires:       libopenblasp.so.0
Requires:       libquadmath.so.0
Requires:       suitesparse
%endif
# https://bugzilla.redhat.com/show_bug.cgi?id=1158026
# https://github.com/JuliaLang/julia/issues/30087
ExclusiveArch:  x86_64

%description
Julia is a high-level, high-performance dynamic programming language
for technical computing, with syntax that is familiar to users of
other technical computing environments. It provides a sophisticated
compiler, distributed parallel execution, numerical accuracy, and an
extensive mathematical function library. The library, largely written
in Julia itself, also integrates mature, best-of-breed C and Fortran
libraries for linear algebra, random number generation, signal processing,
and string processing.

This package only contains the essential parts of the Julia environment:
the julia executable and the standard library.

%package common
Summary:        Julia architecture-independent files
BuildArch:      noarch
Requires:       julia = %{version}-%{release}

%description common
Contains architecture-independent files required to run Julia.

%package doc
Summary:        Julia documentation and code examples
BuildArch:      noarch
Requires:       julia = %{version}-%{release}

%description doc
Contains the Julia manual, the reference documentation of the standard library
and code examples.

%package devel
Summary:        Julia development, debugging and testing files
Requires:       julia%{?_isa} = %{version}-%{release}

%description devel
Contains library symbolic links and header files for developing applications
linking to the Julia library, in particular embedding it, as well as
tests. This package is normally not
needed when programming in the Julia language, but rather for embedding
Julia into external programs or debugging Julia itself.

%prep
%setup -q -n julia-1.11.0-rc3

%autopatch -p1

mkdir -p deps/srccache stdlib/srccache

pushd deps/srccache
    # Julia downloads tarballs for external dependencies even when the folder is present:
    # we need to copy the tarball and let the build process unpack it
    # https://github.com/JuliaLang/julia/pull/10280
    cp -p %SOURCE1 .
    cp -p %SOURCE2 .
    cp -p %SOURCE3 .
    cp -p %SOURCE4 .
    cp -p %SOURCE5 .
    cp -p %SOURCE7 .
    cp -p %SOURCE8 .
    cp -p %SOURCE9 .
    cp -p %SOURCE10 .
    cp -p %SOURCE11 .
    cp -p %SOURCE12 .
    cp -p %SOURCE13 .
popd

cp -p %SOURCE6 contrib/julia.svg

# Required so that the image is not optimized for the build CPU
# (i386 does not work yet: https://github.com/JuliaLang/julia/issues/7185)
# Without specifying MARCH, the Julia system image would only work on native CPU
# CPU targets reflect those used upstream at
# https://github.com/JuliaCI/julia-buildbot/blob/master/master/inventory.py
%ifarch %{ix86}
%global march MARCH=pentium4
%global cpu_target JULIA_CPU_TARGET="pentium4;sandybridge,-xsaveopt,clone_all"
%endif
%ifarch x86_64
%global march MARCH=x86-64
%global cpu_target JULIA_CPU_TARGET="generic;sandybridge,-xsaveopt,clone_all;haswell,-rdrnd,base(1)"
%endif
%ifarch %{arm}
# gcc and LLVM do not support the same targets
%global march MARCH=$(echo %build_cflags | grep -Po 'march=\\K[^ ]*')
%global cpu_target JULIA_CPU_TARGET="generic"
%endif
%ifarch armv7hl
%global march MARCH=$(echo %build_cflags | grep -Po 'march=\\K[^ ]*')
%global cpu_target JULIA_CPU_TARGET="armv7-a;armv7-a,neon;armv7-a,neon,vfp4"
%endif
%ifarch aarch64
%global march MARCH=armv8-a
%global cpu_target JULIA_CPU_TARGET="generic"
%endif
%ifarch ppc64le
%global march %{nil}
%global cpu_target JULIA_CPU_TARGET="pwr8"
%endif

# Use the non-threaded OpenBLAS library name internally to match what Julia uses so that
# libraries built using BinaryBuilder (like Arpack.jl) work
# We symlink it to libopenblasp below so that threads are used in the end
%if 0%{?__isa_bits} == 64
%global blas USE_BLAS64=1 OPENBLAS_SYMBOLSUFFIX=64_ LIBBLAS=-lopenblas64_ LIBBLASNAME=libopenblas64_ LIBLAPACK=-lopenblas64_ LIBLAPACKNAME=libopenblas64_
%else
%global blas LIBBLAS=-lopenblas LIBBLASNAME=libopenblas LIBLAPACK=-lopenblas LIBLAPACKNAME=libopenblas
%endif

%if 0%{?__isa_bits} == 64
%global suitesparse_lib SUITESPARSE_LIB="-lumfpack64_ -lcholmod64_ -lamd64_ -lcamd64_ -lcolamd64_ -lspqr64_"
%else
%global suitesparse_lib SUITESPARSE_LIB="-lumfpack -lcholmod -lamd -lcamd -lcolamd -lspqr"
%endif

%if 0%{?el7}
%global cmake CMAKE=cmake3
%else
%global cmake CMAKE=cmake
%endif

# About build, build_libdir and build_bindir, see https://github.com/JuliaLang/julia/issues/5063#issuecomment-32628111
%global commonopts USE_SYSTEM_LLVM=0 USE_SYSTEM_LIBUNWIND=0 USE_SYSTEM_PCRE=1 USE_SYSTEM_BLAS=1 USE_SYSTEM_LAPACK=1 USE_SYSTEM_GMP=0 USE_SYSTEM_MPFR=1 USE_SYSTEM_LIBSUITESPARSE=1 USE_SYSTEM_DSFMT=1 USE_SYSTEM_LIBUV=0 USE_SYSTEM_UTF8PROC=1 USE_SYSTEM_LIBGIT2=1 USE_SYSTEM_LIBSSH2=0 USE_SYSTEM_MBEDTLS=0 USE_SYSTEM_CURL=0 USE_SYSTEM_PATCHELF=1 USE_SYSTEM_LIBM=0 USE_SYSTEM_OPENLIBM=1 USE_SYSTEM_ZLIB=1 USE_SYSTEM_P7ZIP=1 USE_SYSTEM_NGHTTP2=1 USE_SYSTEM_CSL=1 USE_SYSTEM_LIBBLASTRAMPOLINE=0 USE_SYSTEM_LIBWHICH=0 USE_BINARYBUILDER=0 USE_BINARYBUILDER_LLVM=0 WITH_TERMINFO=0 BUNDLE_DEBUG_LIBS=0 JULIA_SPLITDEBUG=1 TAGGED_RELEASE_BANNER="Fedora %{fedora} build" VERBOSE=1 %{march} %{cpu_target} %{blas} %{suitesparse_lib} prefix=%{_prefix} bindir=%{_bindir} libdir=%{_libdir} libexecdir=%{_libexecdir} datarootdir=%{_datarootdir} includedir=%{_includedir} sysconfdir=%{_sysconfdir} build_prefix=%{_builddir}/%{buildsubdir}/build%{_prefix} build_libdir=%{_builddir}/%{buildsubdir}/build%{_libdir} JULIA_CPU_THREADS=$(echo %{?_smp_mflags} | sed s/-j//)


%build
# LTO currently makes building blastrampoline and Julia itself fail
# It is not enabled upstream anyway
%global _lto_cflags %nil

# Workaround for https://github.com/JuliaLang/julia/issues/27118
%global build_cxxflags %(echo %{build_cxxflags} | sed 's/-Wp,-D_GLIBCXX_ASSERTIONS //')
# Workaround for https://github.com/JuliaLang/julia/issues/39822
# and https://bugzilla.redhat.com/show_bug.cgi?id=1928696
%global build_cflags %(echo %{build_cflags} | sed 's/-Wp,-D_GNU_SOURCE //')

# Julia hardcodes the exact SOVERSION it uses when USE_SYSTEM_*=0
# https://github.com/JuliaLang/julia/pull/38347#discussion_r574819534
sed "s/libmbedtls.so.*\"/$(cd %{_libdir} && ls libmbedtls.so.??)\"/" -i stdlib/MbedTLS_jll/src/MbedTLS_jll.jl
sed "s/libmbedcrypto.so.*\"/$(cd %{_libdir} && ls libmbedcrypto.so.?)\"/" -i stdlib/MbedTLS_jll/src/MbedTLS_jll.jl
sed "s/libmbedx509.so.*\"/$(cd %{_libdir} && ls libmbedx509.so.?)\"/" -i stdlib/MbedTLS_jll/src/MbedTLS_jll.jl
sed "s/libopenlibm.so.*\"/$(cd %{_libdir} && ls libopenlibm.so.?)\"/" -i stdlib/OpenLibm_jll/src/OpenLibm_jll.jl
sed "s/libgit2.so.*\"/$(cd %{_libdir} && ls -1 libgit2.so.?.? | sort -nr | head -n1)\"/" -i stdlib/LibGit2_jll/src/LibGit2_jll.jl
sed "/VersionNumber/s/v\".*\"/v\"$(pkg-config --modversion libgit2)\"/" -i stdlib/LibGit2_jll/test/runtests.jl

# Work around build failure with glibc 2.33 when GNU_SOURCE is set
# https://github.com/JuliaLang/julia/issues/39822
sed "s/#if defined(MINSIGSTKSZ) && MINSIGSTKSZ > 131072/#if 0/" -i src/task.c

# Work around bug that prompts zlib to be downloaded even when not used
# https://github.com/JuliaLang/julia/pull/42524/files#r734972945
sed "s/ \$(build_prefix)\\/manifest\\/zlib//" -i deps/llvm.mk

# Work around random failure https://github.com/JuliaLang/julia/issues/42752
sed "s/@test orig == Random.default_rng()//" -i stdlib/Test/test/runtests.jl
sed "s/@test rand(orig) == rand()//" -i stdlib/Test/test/runtests.jl

# Disable test that fails because Julia process doesn't error as expected
sed "s/mktempdir() do pfx/false \&\& mktempdir() do pfx/" -i test/compiler/codegen.jl

# Increase tolerance as times on build machines are not very reliable
sed "s/after_comp - before_comp < 6_000_000_000/after_comp - before_comp < 600_000_000_000/" -i test/misc.jl

# Decrease debuginfo verbosity to reduce memory consumption during final library linking
%ifarch %{arm} %{ix86}
%global build_cflags %(echo %{build_cflags} | sed 's/-g /-g1 /')
%global build_cxxflags %(echo %{build_cxxflags} | sed 's/-g /-g1 /')
%global build_ldflags %(echo %{build_ldflags} | sed 's/-g /-g1 /')
%endif

%ifarch %{ix86}
# Need to repeat -march here to override i686 from build_cflags
%global buildflags CFLAGS="%{build_cflags} -march=pentium4" CXXFLAGS="%{build_cxxflags} -march=pentium4" FFLAGS="%{build_fflags} -march=pentium4" LDFLAGS="%{build_ldflags}"
%else
%global buildflags CFLAGS="%{build_cflags}" CXXFLAGS="%{build_cxxflags}" FFLAGS="%{build_fflags}" LDFLAGS="%{build_ldflags}"
%endif

# Needed when USE_SYSTEM_CSL=1
# https://github.com/JuliaLang/julia/issues/39637
unlink %{_builddir}/%{buildsubdir}/build/usr/lib || true
mkdir -p %{_builddir}/%{buildsubdir}/build/%{_libdir}/
ln -sf %{_libdir}/libgcc_s.so.1 %{_builddir}/%{buildsubdir}/build/%{_libdir}/libgcc_s.so.1

# Work around https://github.com/JuliaLinearAlgebra/libblastrampoline/pull/121
make %{?_smp_mflags} %{commonopts} binlib=../%{_libdir} -C deps install-blastrampoline

# Workaround LLVM being installed in lib and not found
pushd %{_builddir}/%{buildsubdir}/build/%{_libdir}
    ln -sf ../lib/libLLVM-%{llvmversionmaj}jl.so libLLVM-%{llvmversionmaj}jl.so
popd

make %{?_smp_mflags} %{commonopts} release

# Now copy LLVM from lib to lib64
if [ "x%{_lib}" != xlib ] ; then
  rm -f %{_builddir}/%{buildsubdir}/build/%{_libdir}/libLLVM-%{llvmversionmaj}jl.so
  cp -a %{_builddir}/%{buildsubdir}/build/usr/lib/* %{_builddir}/%{buildsubdir}/build/%{_libdir}
  rm -rf %{_builddir}/%{buildsubdir}/build/usr/lib/
  ln -sf %{_lib} %{_builddir}/%{buildsubdir}/build/usr/lib
fi

# Use CA certificates from ca-certificates
# (Mozilla certificates are not installed anyway when USE_SYSTEM_LIBGIT2=1)
# https://github.com/JuliaLang/julia/commit/5dc6201e8dccbf21aeeb1f79fef2d186c7800a4e#r470321788
ln -sf /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem %{_builddir}/%{buildsubdir}/build/%{_datarootdir}/julia/cert.pem

%check
# Disable tests that require Internet access
sed "s/ipa = getipaddr()/error()/" -i test/choosetests.jl

# Too many threads/processes can trigger memory issues in cmdlineargs test
%ifarch %{ix86}
sed "s/cpu_threads = max(2\*cpu_threads, min(200, 10\*cpu_threads))/cpu_threads = 5/" -i test/cmdlineargs.jl
%endif

# Disable tests known to fail currently
# vecelement: https://github.com/JuliaLang/julia/issues/53683
sed -i 's/skip_tests = Set()/skip_tests = Set(["Distributed", "Logging", "cmdlineargs", "loading", "vecelement", "channels"])/' test/choosetests.jl
%ifarch ppc64le %{arm} aarch64
sed -i 's/\"numbers\",//' test/choosetests.jl
sed -i 's/\"ccall\",//' test/choosetests.jl
sed -i 's/\"vecelement\", //' test/choosetests.jl
sed -i 's/\"stress\",//' test/choosetests.jl
sed -i 's/\"errorshow\",//' test/choosetests.jl
sed -i 's/\"threads\",//' test/choosetests.jl
%endif
%ifarch %{arm}
# https://github.com/JuliaLang/julia/issues/29447
sed -i 's/readdir(STDLIB_DIR)/setdiff(readdir(STDLIB_DIR), ["Distributed"])/g' test/choosetests.jl
%endif
%ifarch ppc64le
# LinearAlgebra/lapack is the problematic test
sed -i 's/readdir(STDLIB_DIR)/setdiff(readdir(STDLIB_DIR), ["LibGit2", "LinearAlgebra"])/g' test/choosetests.jl
sed -i 's/\"cmdlineargs\", //' test/choosetests.jl
%endif

# Julia hardcodes the exact SOVERSION it uses when USE_SYSTEM_*=0
# https://github.com/JuliaLang/julia/pull/38347#discussion_r574819534
sed "s/@test vn == v\".*\"//" -i stdlib/PCRE2_jll/test/runtests.jl
sed "s/@test vn == v\".*\"//" -i stdlib/GMP_jll/test/runtests.jl
sed "s/@test vn == v\".*\"//" -i stdlib/MPFR_jll/test/runtests.jl
sed "s/@test vn == v\".*\"//" -i stdlib/MbedTLS_jll/test/runtests.jl
sed "s/@test VersionNumber\(.*\) == v\".*\"//" -i stdlib/Zlib_jll/test/runtests.jl
sed "s/@test VersionNumber(unsafe_string(info.version_str)) == v\".*\"//" -i stdlib/nghttp2_jll/test/runtests.jl
sed "s/@test .*SuiteSparse_version.*==.*//" -i stdlib/SuiteSparse_jll/test/runtests.jl

# JULIA_TEST_USE_MULTIPLE_WORKERS=true enables running tests in parallel despite net_on=false
make %{commonopts} JULIA_TEST_USE_MULTIPLE_WORKERS=true test

%install
make %{commonopts} DESTDIR=%{buildroot} install

pushd %{buildroot}%{_libdir}/julia
    %if 0%{?__isa_bits} == 64
        rm -f libopenblas64_.so
        ln -s ../libopenblasp64_.so.0 libopenblas64_.so
        ln -s ../libopenblasp64_.so.0 libopenblas64_.so.0
        # Raise an error in case of changing files
        test -e %{_libdir}/libopenblas64_.so
        test -e %{_libdir}/libopenblas64_.so.0

        # Julia creates unversioned symlinks to SuiteSparse libraries linking to libopenblas rather than libopenblas64_
        # and it does not create versioned symlinks needed to dlopen() libraries using their unsuffixed names
        for LIB in spqr umfpack colamd cholmod ccolamd camd amd suitesparseconfig btf klu ldl rbio
        do
            rm -f lib${LIB}.so
            LIBVER64=$(readelf -d %{_libdir}/lib${LIB}64_.so | sed -n '/SONAME/s/.*\(lib[^ ]*\.so\.[0-9]*\).*/\1/p')
            LIBVER=$(echo ${LIBVER64} | sed -n 's/64_//p')
            ln -s ../${LIBVER64} lib${LIB}.so
            ln -s ../${LIBVER64} ${LIBVER}
            # Raise an error in case of changing files
            test -e %{_libdir}/lib${LIB}.so
        done
    %else
        rm -f libopenblas.so
        ln -s ../libopenblasp.so.0 libopenblas.so
        ln -s ../libopenblasp.so.0 libopenblas.so.0
        # Raise an error in case of changing files
        test -e %{_libdir}/libopenblas.so
        test -e %{_libdir}/libopenblas.so.0
    %endif
popd

# Prevent find-debuginfo from touching precompiled caches as it
# changes checksums, which invalidates them
chmod -x %{buildroot}%{_datarootdir}/julia/compiled/*/*/*.so

cp -p CONTRIBUTING.md LICENSE.md NEWS.md README.md %{buildroot}%{_docdir}/julia/

pushd %{buildroot}%{_libdir}/julia
    # Some Julia packages rely on being able to use libjulia, but we only
    # ship %%{_libdir}/libjulia.so in the -devel package
    ln -s ../libjulia.so.1.*.* libjulia.so
    # Raise an error in case of failure
    realpath -e libjulia.so

    # Needed when USE_SYSTEM_CSL=1
    # https://github.com/JuliaLang/julia/issues/39637
    ln -sf ../libgcc_s.so.1 libgcc_s.so.1
    # Raise an error in case of changing files
    test -e %{_libdir}/libgcc_s.so.1
popd

# Use CA certificates from ca-certificates
# (Mozilla certificates are not installed anyway when USE_SYSTEM_LIBGIT2=1)
# https://github.com/JuliaLang/julia/commit/5dc6201e8dccbf21aeeb1f79fef2d186c7800a4e#r47032178
ln -sf /etc/pki/tls/cert.pem %{buildroot}%{_datarootdir}/julia/cert.pem

# Mark stack as non executable as the linker isn't able to detect this automatically
# Needed until https://github.com/JuliaLang/julia/pull/43481 is merged
# Also drop BuildRequires when removing this
execstack -c %{buildroot}%{_libdir}/libjulia.so*

# Install .desktop file and icons
mkdir -p %{buildroot}%{_datarootdir}/icons/hicolor/scalable/apps/
mkdir -p %{buildroot}%{_datarootdir}/icons/hicolor/16x16/apps/
mkdir -p %{buildroot}%{_datarootdir}/icons/hicolor/24x24/apps/
mkdir -p %{buildroot}%{_datarootdir}/icons/hicolor/32x32/apps/
mkdir -p %{buildroot}%{_datarootdir}/icons/hicolor/48x48/apps/
mkdir -p %{buildroot}%{_datarootdir}/icons/hicolor/256x256/apps/
cp -p contrib/julia.svg %{buildroot}%{_datarootdir}/icons/hicolor/scalable/apps/%{name}.svg
convert -scale 16x16 -extent 16x16 -gravity center -background transparent \
    contrib/julia.svg %{buildroot}%{_datarootdir}/icons/hicolor/16x16/apps/%{name}.png
convert -scale 24x24 -extent 24x24 -gravity center -background transparent \
    contrib/julia.svg %{buildroot}%{_datarootdir}/icons/hicolor/24x24/apps/%{name}.png
convert -scale 32x32 -extent 32x32 -gravity center -background transparent \
    contrib/julia.svg %{buildroot}%{_datarootdir}/icons/hicolor/32x32/apps/%{name}.png
convert -scale 48x48 -extent 48x48 -gravity center -background transparent \
    contrib/julia.svg %{buildroot}%{_datarootdir}/icons/hicolor/48x48/apps/%{name}.png
convert -scale 256x256 -extent 256x256 -gravity center -background transparent \
    contrib/julia.svg %{buildroot}%{_datarootdir}/icons/hicolor/256x256/apps/%{name}.png
desktop-file-validate %{buildroot}%{_datarootdir}/applications/%{name}.desktop

%files
%dir %{_docdir}/julia/
%{_docdir}/julia/LICENSE.md
%doc %{_docdir}/julia/CONTRIBUTING.md
%doc %{_docdir}/julia/NEWS.md
%doc %{_docdir}/julia/README.md
%{_bindir}/julia
%{_libdir}/julia/
%{_libexecdir}/julia/
%exclude %{_libdir}/julia/*debug*
%{_libdir}/libjulia.so.*
%{_datarootdir}/julia/compiled/*/*/*.ji
# Re-set precompiled caches as executable once find-debuginfo has skipped them (see above)
%attr(755, -, -) %{_datarootdir}/julia/compiled/*/*/*.so
%{_mandir}/man1/julia.1*
%{_datarootdir}/appdata/julia.appdata.xml
%{_datarootdir}/applications/%{name}.desktop
%{_datarootdir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datarootdir}/icons/hicolor/16x16/apps/%{name}.png
%{_datarootdir}/icons/hicolor/24x24/apps/%{name}.png
%{_datarootdir}/icons/hicolor/32x32/apps/%{name}.png
%{_datarootdir}/icons/hicolor/48x48/apps/%{name}.png
%{_datarootdir}/icons/hicolor/256x256/apps/%{name}.png

%files common
%dir %{_datarootdir}/julia/
%{_datarootdir}/julia/*.jl
%{_datarootdir}/julia/base/
%{_datarootdir}/julia/stdlib/
%{_datarootdir}/julia/base.cache
%{_datarootdir}/julia/cert.pem
# files in testhelpers/ subdirectory are needed to precompile sysimages
%{_datarootdir}/julia/test/

%dir %{_sysconfdir}/julia/
%config(noreplace) %{_sysconfdir}/julia/startup.jl

%files doc
%doc %{_docdir}/julia/

%files devel
%{_libdir}/libjulia.so
%{_libdir}/julia/libccalltest.so.debug
%{_includedir}/julia/

%post
/sbin/ldconfig
/bin/touch --no-create %{_datarootdir}/icons/hicolor &>/dev/null || :
exit 0

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-13.rc3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 8 2024 Milan Bouchet-Valat <nalimilan@club.fr> - 1.11.0.13-rc3
- Rebuild for utf8proc 2.9.0.

* Sun Sep 29 2024 Milan Bouchet-Valat <nalimilan@club.fr> - 1.11.0.12-rc3
- Fix path to cert.pem.

* Sun Sep 22 2024 Milan Bouchet-Valat <nalimilan@club.fr> - 1.11.0.11-rc3
- New upstream release.

* Tue Sep 03 2024 Morten Stevens <mstevens@fedoraproject.org> 1.11.0.10-beta1
- Rebuilt for mbedTLS 3.6.1

* Wed Aug 28 2024 Milan Bouchet-Valat <nalimilan@club.fr> - 1.11.0.9-beta1
- Avoid listing bundled libraries as Provides.

* Wed Aug 28 2024 Milan Bouchet-Valat <nalimilan@club.fr> - 1.11.0.8-beta1
- Again really fix error when using CURL with OpenSSL_jll.

* Wed Aug 28 2024 Milan Bouchet-Valat <nalimilan@club.fr> - 1.11.0.7-beta1
- Fix error when precompiling sysimages.
- Fix error when using CURL with OpenSSL_jll.

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-6.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri May 3 2024 Milan Bouchet-Valat <nalimilan@club.fr> - 1.11.0.5-beta1
- Fix missing dependency on libquadmath.

* Fri May 3 2024 Milan Bouchet-Valat <nalimilan@club.fr> - 1.11.0.4-beta1
- Re-fix error when trying to open SuiteSparse libraries.

* Thu May 2 2024 Milan Bouchet-Valat <nalimilan@club.fr> - 1.11.0.3-beta1
- Fix error when trying to open SuiteSparse libraries.

* Thu May 2 2024 Milan Bouchet-Valat <nalimilan@club.fr> - 1.11.0.2-beta1
- Fix error on startup due to unnecessary recompilation.

* Thu May 2 2024 Milan Bouchet-Valat <nalimilan@club.fr> - 1.11.0.1-beta1
- Fix error on startup.

* Wed May 1 2024 Milan Bouchet-Valat <nalimilan@club.fr> - 1.11.0.0-beta1
- New upstream release.
- Fix build failures.

* Sun Feb 04 2024 Orion Poplawski <orion@nwra.com> - 1.9.2-6
- Rebuild with suitesparse 7.6.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 16 2023 Pete Walter <pwalter@fedoraproject.org> - 1.9.2-3
- Rebuild for libgit2 1.7.x

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 7 2023 Milan Bouchet-Valat <nalimilan@club.fr> - 1.9.2-1
- New upstream release.
- Enable ITTAPI.

* Sun Jun 11 2023 Milan Bouchet-Valat <nalimilan@club.fr> - 1.9.1-1
- New upstream release.

* Mon May 15 2023 Milan Bouchet-Valat <nalimilan@club.fr> - 1.9.0-3
- New upstream release.

* Wed Apr 26 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.9.0-2.rc2
- Re-fix dependency on OpenBLAS

* Thu Apr 20 2023 Milan Bouchet-Valat <nalimilan@club.fr> - 1.9.0-1.rc2
- Fix missing dependency on SuiteSparse.
- Re-fix dependency on OpenBLAS.

* Wed Apr 19 2023 Milan Bouchet-Valat <nalimilan@club.fr> - 1.9.0-0.rc2
- New upstream release.
- Fix missing dependency on OpenBLAS.

* Wed Mar 8 2023 Milan Bouchet-Valat <nalimilan@club.fr> - 1.9.0-0.beta4
- New upstream release.
- Drop i686 support due to test failures.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 09 2022 Pete Walter <pwalter@fedoraproject.org> - 1.8.2-2
- Rebuild for libgit2 1.4

* Thu Sep 29 2022 Milan Bouchet-Valat <nalimilan@club.fr> - 1.8.2-1
- New upstream release.

* Wed Aug 24 2022 Milan Bouchet-Valat <nalimilan@club.fr> - 1.8.0-1
- New upstream release.
- Update license information.

* Sat Jul 30 2022 Milan Bouchet-Valat <nalimilan@club.fr> - 1.8.0-0.1.beta3
- New upstream release.
- Disable LTO to fix build failures.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat May 28 2022 Milan Bouchet-Valat <nalimilan@club.fr> - 1.7.3-1
- New upstream release.
- Drop workaround for Downloads.jl/Multl.jl segfault with curl 7.81 (rhbz#2056842).

* Fri Apr  8 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.7.2-5
- Filter out libunwind Provides

* Wed Apr  6 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.7.2-3
- Avoid gcc12 float16 truncation / extension function collision
  (rhbz#2044284, github#44829)

* Tue Feb 22 2022 Mamoru TASAKA <mtasaka@fedoraproject.org>
- Workaround for Downloads.jl/Multl.jl segfault with curl 7.81 (rhbz#2056842)

* Sun Feb 20 2022 Mamoru TASAKA <mtasaka@fedoraproject.org>
- Backport from libunwind 1.5 to fix -fno-common issue
- Fix build_libdir related issue, add LD_LIBRARY_PATH on %%build for now

* Sun Feb 20 2022 Igor Raits <igor.raits@gmail.com> - 1.7.2-2
- Rebuild for libgit2 1.4.x

* Wed Feb 9 2022 Milan Bouchet-Valat <nalimilan@club.fr> - 1.7.2-1
- New upstream release.
- Bundle libunwind 1.3.2 to fix FTBFS (rhbz#2045732).

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 24 2021 Milan Bouchet-Valat <nalimilan@club.fr> - 1.7.1-1
- New upstream release.
- Mark stack as non executable (rhbz#2032655).

* Thu Dec 2 2021 Milan Bouchet-Valat <nalimilan@club.fr> - 1.7.0.0-1
- Fix version so that it compares higher than 1.7.0rc3.

* Thu Dec 2 2021 Milan Bouchet-Valat <nalimilan@club.fr> - 1.7.0-1
- New upstream release.

* Sun Nov 28 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.7.0rc3-2
- Rebuild for libgit2 1.3.x

* Tue Nov 16 2021 Milan Bouchet-Valat <nalimilan@club.fr> - 1.7.0rc3-1
- New upstream release.

* Sat Oct 23 2021 Milan Bouchet-Valat <nalimilan@club.fr> - 1.7.0rc2-1
- New upstream release.

* Mon Aug 30 2021 Milan Bouchet-Valat <nalimilan@club.fr> - 1.7.0beta4-1
- New upstream release.

* Sun Aug 29 2021 Milan Bouchet-Valat <nalimilan@club.fr> - 1.7.0beta3-4
- Proper fix to add back libjulia-internal to Provides to fix installation of cantor (rhbz#1996408).

* Sun Aug 29 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.7.0beta3-3
- Revert the previous change for now, to avoid that julia itself
  cannot be installed

* Thu Aug 26 2021 Milan Bouchet-Valat <nalimilan@club.fr> - 1.7.0beta3-2
- Add back libjulia-internal to Provides to fix installation of cantor (fixes rhbz#1996408).

* Sat Aug 21 2021 Milan Bouchet-Valat <nalimilan@club.fr> - 1.7.0beta3-1
- New upstream release.
- Avoid including private libraries in Provides.

* Thu Jul 29 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.6.1-3
- Rebuild for new openlibm

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Apr 24 2021 Milan Bouchet-Valat <nalimilan@club.fr> - 1.6.1-1
- New upstream release.

* Wed Mar 31 2021 Jonathan Wakely <jwakely@redhat.com> - 1.6.0-2
- Rebuilt for removed libstdc++ symbols (#1937698)

* Thu Mar 25 2021 Milan Bouchet-Valat <nalimilan@club.fr> - 1.6.0-1
- New upstream release.

* Fri Mar 12 2021 Milan Bouchet-Valat <nalimilan@club.fr> - 1.6.0-0.5.rc2
- New upstream release.
- Really fix build on Rawhide.

* Thu Feb 25 2021 Milan Bouchet-Valat <nalimilan@club.fr> - 1.6.0-0.4.rc1
- Fix build on Rawhide.

* Tue Feb 16 2021 Milan Bouchet-Valat <nalimilan@club.fr> - 1.6.0-0.3.rc1
- Fix libgfortran.so dependency on 64-bit.

* Mon Feb 15 2021 Milan Bouchet-Valat <nalimilan@club.fr> - 1.6.0-0.2.rc1
- Fix libgfortran.so version.

* Sun Feb 14 2021 Milan Bouchet-Valat <nalimilan@club.fr> - 1.6.0-0.1.rc1
- New upstream release.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 4 2021 Milan Bouchet-Valat <nalimilan@club.fr> - 1.5.3-3
- Fix build failure.

* Mon Dec 28 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.5.3-2
- Rebuild for libgit2 1.1.x

* Wed Nov 11 2020 Milan Bouchet-Valat <nalimilan@club.fr> - 1.5.3-1
- New upstream release.

* Sun Sep 27 2020 Milan Bouchet-Valat <nalimilan@club.fr> - 1.5.2-1
- New upstream release.

* Mon Aug 10 2020 Milan Bouchet-Valat <nalimilan@club.fr> - 1.5.0-1
- New upstream release.
- No longer include julia-debug to work around build failure (rhbz#1863925).

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Milan Bouchet-Valat <nalimilan@club.fr> - 1.4.2-2
- Fix error on startup due to incorrect libLLVM name.

* Sat May 30 2020 Milan Bouchet-Valat <nalimilan@club.fr> - 1.4.2-1
- New upstream release.

* Sun Apr 19 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.4.0-3
- Rebuild for libgit2 1.0.0

* Fri Mar 27 2020 Milan Bouchet-Valat <nalimilan@club.fr> - 1.4.0-2
- Fix error on startup.

* Tue Mar 24 2020 Milan Bouchet-Valat <nalimilan@club.fr> - 1.4.0-1
- New upstream release.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 5 2019 Milan Bouchet-Valat <nalimilan@club.fr> - 1.2.0-5
- Include libjulia.so symlink in private Julia libdir so that packages
  can call into libjulia even when julia-devel is not installed (fixes rhbz#1764797).

* Mon Oct 21 2019 Milan Bouchet-Valat <nalimilan@club.fr> - 1.2.0-4
- Unbundle SuiteSparse, mpfr and libunwind.

* Tue Oct 8 2019 Milan Bouchet-Valat <nalimilan@club.fr> - 1.2.0-3
- Fix missing libopenblas64_.so.0 symlink to fix rhbz#1758803.

* Tue Aug 27 2019 Milan Bouchet-Valat <nalimilan@club.fr> - 1.2.0-2
- Unbundle PCRE.

* Sun Aug 25 2019 Milan Bouchet-Valat <nalimilan@club.fr> - 1.2.0-1
- New upstream release.
- Use openblas(64_).so as internal library name to fix packages like Arpack.jl.
- Bundle PCRE to work around rhbz#1743863.
- Move libccalltest.so.debug and sys-debug.so to julia-devel.
- Disable ARM architectures for now due to test failures.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 06 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.0-3
- Rebuild for libgit2 0.28.x

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Milan Bouchet-Valat <nalimilan@club.fr> - 1.1.0-1
- New upstream release.

* Wed Dec 19 2018 Milan Bouchet-Valat <nalimilan@club.fr> - 1.0.3-1
- New upstream release.

* Sat Nov 10 2018 Milan Bouchet-Valat <nalimilan@club.fr> - 1.0.2-1
- New upstream release.

* Mon Oct 29 2018 Milan Bouchet-Valat <nalimilan@club.fr> - 1.0.1-5
- Drop unnecessary dependency of julia on julia-devel and openblas-threads.
- Add Fedora to release banner.

* Sat Oct 20 2018 Milan Bouchet-Valat <nalimilan@club.fr> - 1.0.1-4
- Use ILP64 BLAS and bundle SuiteSparse until system packages support it.

* Sat Oct 06 2018 Morten Stevens <mstevens@fedoraproject.org> - 1.0.1-3
- Rebuilt for mbed TLS 2.13.0

* Wed Oct 3 2018 Milan Bouchet-Valat <nalimilan@club.fr> - 1.0.1-2
- Make package installable again by fixing Requires.

* Sun Sep 30 2018 Milan Bouchet-Valat <nalimilan@club.fr> - 1.0.1-1
- New upstream release.
- Remove internal libraries from Provides.
- Enable build on ARM and PPC.

* Fri Sep 7 2018 Milan Bouchet-Valat <nalimilan@club.fr> - 1.0.0-2
- Fix FTBFS by bundling libunwind.

* Fri Sep 7 2018 Milan Bouchet-Valat <nalimilan@club.fr> - 1.0.0-1
- New upstream release 1.0.0.

* Fri Aug 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.3-3
- Rebuild for libgit2 0.27.x

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 3 2018 Milan Bouchet-Valat <nalimilan@club.fr> - 0.6.3-1
- New upstream release.

* Fri Mar 23 2018 Milan Bouchet-Valat <nalimilan@club.fr> - 0.6.2-3
- Work around bug in UNW_VERSION_MINOR not being a single integer by removing redundant check.
- Fix libgit2 test failure due to letter case.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 14 2017 Milan Bouchet-Valat <nalimilan@club.fr> - 0.6.2-1
- New upstream release.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 09 2017 Milan Bouchet-Valat <nalimilan@club.fr> - 0.6.0-2
- Fix build with libgit2 0.26.

* Sat Jul 08 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.6.0-2
- Rebuild for libgit2 0.26.x

* Thu Jun 22 2017 Milan Bouchet-Valat <nalimilan@club.fr> - 0.6.0-1
- New upstream release.

* Sun Jun 11 2017 Milan Bouchet-Valat <nalimilan@club.fr> - 0.6.0-0.5.rc3
- New upstream release.
- Use system libunwind instead of bundling it.

* Thu May 25 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.6.0-0.4.rc2
- Rebuild llvm-4

* Fri May 19 2017 Milan Bouchet-Valat <nalimilan@club.fr> - 0.6.0-0.3.rc2
- New upstream release.

* Sat Apr 1 2017 Milan Bouchet-Valat <nalimilan@club.fr> - 0.6.0-0.2.pre.beta
- New upstream release.

* Thu Mar 2 2017 Milan Bouchet-Valat <nalimilan@club.fr> - 0.6.0-0.1.pre.alpha
- New upstream release, fixes build with libgit 0.25.

* Tue Feb 21 2017 Milan Bouchet-Valat <nalimilan@club.fr> - 0.5.0-3
- Rebuild for GCC7.

* Tue Feb 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.5.0-2
- Rebuild for libgit2-0.25.x

* Tue Sep 20 2016 Milan Bouchet-Valat <nalimilan@club.fr> - 0.5.0-1
- New upstream release.

* Thu Sep 15 2016 Milan Bouchet-Valat <nalimilan@club.fr> - 0.5.0-0.rc4
- New upstream release candidate.

* Mon Jun 20 2016 Milan Bouchet-Valat <nalimilan@club.fr> - 0.4.6-1
- New upstream release.
- Drop tridiag patch, now included upstream.

* Wed Mar 30 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.4.5-2
- Rebuild for libgit2 0.24.0 once more

* Sun Mar 20 2016 Milan Bouchet-Valat <nalimilan@club.fr> - 0.4.5-1
- New upstream release.

* Sun Mar 20 2016 Milan Bouchet-Valat <nalimilan@club.fr> - 0.4.3-9
- Add patch to fix non-deterministic test failure with OpenBLAS 0.2.16.

* Sun Mar 20 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.4.3-8
- Rebuild for libgit2 0.24.0

* Tue Mar 8 2016 Milan Bouchet-Valat <nalimilan@club.fr> - 0.4.3-7
- Fix generation of library symlinks to rely only on major version.
- Rebuild for openlibm SONAME bump.
- Use openlibm on all platforms.

* Wed Mar 2 2016 Milan Bouchet-Valat <nalimilan@club.fr> - 0.4.3-6
- Fix missing PCRE2 dependency, use realpath -e to detect this problem.

* Tue Mar 1 2016 Milan Bouchet-Valat <nalimilan@club.fr> - 0.4.3-5
- Automate generation of library symlinks, and include them in the package instead of
  in %%post so that dependencies on specific library versions are detected.

* Fri Feb 26 2016 Suvayu Ali <fatkasuvayu+linux@gmail.com> - 0.4.3-4
- Fix broken symlinks in libdir

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Milan Bouchet-Valat <nalimilan@club.fr> - 0.4.3-2
- Fix build with GCC 6.

* Thu Jan 28 2016 Milan Bouchet-Valat <nalimilan@club.fr> - 0.4.3-1
- New upstream release.
- Revert to LP64 OpenBLAS until ILP64 works correctly.

* Wed Jan 27 2016 Adam Jackson <ajax@redhat.com> 0.4.2-4
- Rebuild for llvm 3.7.1 library split

* Tue Jan 5 2016 Orion Poplawski <orion@cora.nwra.com> - 0.4.2-3
- Use proper conditional for __isa_bits tests

* Thu Dec 24 2015 Milan Bouchet-Valat <nalimilan@club.fr> - 0.4.2-2
- Use new ILP64 OpenBLAS, suffixed with 64_ (ARPACK and SuiteSparse still use
  the LP64 Atlas).

* Wed Dec 9 2015 Milan Bouchet-Valat <nalimilan@club.fr> - 0.4.2-1
- New upstream release.
- Update bundled libuv to latest Julia fork.

* Mon Nov 9 2015 Milan Bouchet-Valat <nalimilan@club.fr> - 0.4.1-1
- New upstream release.
- Pass explicitly -march to override default -march=i686 with pentium4.
- Get rid of useless build dependencies.

* Fri Oct 9 2015 Milan Bouchet-Valat <nalimilan@club.fr> - 0.4.0-2
- Use LLVM 3.3 to fix bugs and improve compilation performance.
- Run all the tests now that they pass.
- Stop specifying -fsigned-char explicitly, since it is now handled by Julia.
- Refactor architecture checking logic to prepare support for new arches.
- Use upstream .desktop file instead of a custom one.

* Fri Oct 9 2015 Milan Bouchet-Valat <nalimilan@club.fr> - 0.4.0-1
- New upstream release.
- Drop patches now included upstream.
- Drop obsolete rm commands.

* Thu Sep 17 2015 Dave Airlie <airlied@redhat.com> 0.4.0-0.4.rc1
- drag in latest upstream 0.4 branch in hope of fixing i686
- drop out some tests on i686
- build against LLVM 3.7

* Fri Sep 11 2015 Milan Bouchet-Valat <nalimilan@club.fr> - 0.4.0-0.3.rc1
- New upstream release candidate.
- Drop now useless patch.
- Remove libccalltest.so file installed under /usr/share/.

* Fri Aug 28 2015 Nils Philippsen <nils@redhat.com> - 0.4.0-0.2.20150823git
- rebuild against suitesparse-4.4.5, to work around
  https://github.com/JuliaLang/julia/issues/12841

* Sun Aug 23 2015 Milan Bouchet-Valat <nalimilan@club.fr> - 0.4.0-0.1.20150823git
- Update to development version 0.4.0 to fix FTBFS.
- Move to PCRE2, libgit2, utf8proc 1.3, and up-to-date libuv fork.
- Preliminary support for ARM.
- patchelf no longer needed when the same paths are passed to 'make' and 'make install'.
- Building Sphynx documentation no longer needed.
- Fix icons to be square.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Nils Philippsen <nils@redhat.com> - 0.3.7-4
- rebuild for suitesparse-4.4.4

* Fri Apr 10 2015 Milan Bouchet-Valat <nalimilan@club.fr> - 0.3.7-3
- Rebuilt for LLVM 3.6.

* Sat Mar 28 2015 Milan Bouchet-Valat <nalimilan@club.fr> - 0.3.7-2
- Rebuild for utf8proc ABI break.

* Tue Mar 24 2015 Milan Bouchet-Valat <nalimilan@club.fr> - 0.3.7-1
- New upstream release.

* Mon Mar 2 2015 Milan Bouchet-Valat <nalimilan@club.fr> - 0.3.6-2
- Fix loading libcholmod, libfftw3_threads and libumfpack.

* Tue Feb 17 2015 Milan Bouchet-Valat <nalimilan@club.fr> - 0.3.6-1
- New upstream release.

* Fri Jan 9 2015 Milan Bouchet-Valat <nalimilan@club.fr> - 0.3.5-1
- New upstream release.

* Fri Dec 26 2014 Milan Bouchet-Valat <nalimilan@club.fr> - 0.3.4-1
- New upstream release.

* Fri Dec 12 2014 Adam Jackson <ajax@redhat.com> 0.3.3-2
- Rebuild for F21 LLVM 3.5 rebase

* Sun Nov 23 2014 Milan Bouchet-Valat <nalimilan@club.fr> - 0.3.3-1
- New upstream release.
- Bump libuv to follow upstream.

* Wed Nov 05 2014 Adam Jackson <ajax@redhat.com> 0.3.2-4
- Don't BuildRequire: llvm-static

* Tue Oct 28 2014 Milan Bouchet-Valat <nalimilan@club.fr> - 0.3.2-3
- Trigger rebuild to use LLVM 3.5.

* Thu Oct 23 2014 Milan Bouchet-Valat <nalimilan@club.fr> - 0.3.2-2
- New upstream release.

* Sun Oct 12 2014 Milan Bouchet-Valat <nalimilan@club.fr> - 0.3.1-3
- Fix missing symlinks to libarpack, libpcre, libgmp and libmpfr, which could
  prevent Julia from working correcly if the -devel packages were missing.
- Fix invalid hard-coded reference to /usr/lib64.

* Fri Sep 26 2014 Milan Bouchet-Valat <nalimilan@club.fr> - 0.3.1-2
- Add git to dependencies, as it is needed to install packages.

* Mon Sep 22 2014 Milan Bouchet-Valat <nalimilan@club.fr> - 0.3.1-1
- New upstream version.
- Depend on openblas-threads instead of openblas.
- Make source URL automatically depend on version.

* Sat Sep 20 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.3.0-10
- Add dist tag

* Fri Sep 19 2014 Milan Bouchet-Valat <nalimilan@club.fr> - 0.3.0-9
- Use libopenblasp to enable threading.
- Make julia-common depend on julia.

* Fri Sep 19 2014 Milan Bouchet-Valat <nalimilan@club.fr> - 0.3.0-8
- Use versioned OpenBLAS library.so to work without openblas-devel.
- Use LAPACK from OpenBLAS instead of reference implementation.
- Add .desktop file.
- Remove objects.inv feil from HTML documentation.

* Thu Sep 18 2014 Milan Bouchet-Valat <nalimilan@club.fr> - 0.3.0-7
- Fix double inclusion of HTML documentation.
- Improve working directory logic.

* Thu Sep 18 2014 Milan Bouchet-Valat <nalimilan@club.fr> - 0.3.0-6
- Do not remove _sources directory in HTML documentation.
- Make -doc depend on julia to avoid mismatches.

* Wed Sep 17 2014 Milan Bouchet-Valat <nalimilan@club.fr> - 0.3.0-5
- Revert to installing performance suite (needed to run tests).
- Fix double inclusion of some documentation files.
- Move architecture-independent files to a -common subpackage.
- Install HTML documentation instead of .rst files.
- Fix build and install paths.
- Remove dependencies on dSFMT-devel, openlibm-devel and openlibm-devel,
  replacing them with private symbolic links.
- Stop installing libjulia.so to libdir.

* Mon Sep 15 2014 Milan Bouchet-Valat <nalimilan@club.fr> - 0.3.0-4
- Do not install non-functional performance test suite and Makefiles.
- Install documentation to docdir instead of /usr/share/julia/doc.
- Clarify comment about Julia's license.

* Mon Sep 15 2014 Milan Bouchet-Valat <nalimilan@club.fr> - 0.3.0-3
- Remove -xnolibs argument passed by libuv to dtrace (no longer supported
  by systemtap 2.5).

* Fri Sep 5 2014 Milan Bouchet-Valat <nalimilan@club.fr> - 0.3.0-2
- Claim ownership of Julia directories where needed.
- Move libjulia.so to the base package instead of -devel.

* Thu Aug 28 2014 Milan Bouchet-Valat <nalimilan@club.fr> - 0.3.0-1
- New upstream 0.3 final release.
- Set MARCH=pentium4 for 32-bit builds to work on CPUs older than core2.
- Use llvm package instead of requiring llvm3.3.
- Temporarily disable failing backtrace test.

* Sat Jul 26 2014 Milan Bouchet-Valat <nalimilan@club.fr> - 0.3.0-0.6.rc1
- Add dSFMT-devel to Requires.
- Use versioned tarball names for libuv and Rmath.

* Sun Jul 06 2014 Milan Bouchet-Valat <nalimilan@club.fr> - 0.3.0-0.5.git
- Bump libuv and libRmath, simplify tarball names.

* Sat Jun 28 2014 Milan Bouchet-Valat <nalimilan@club.fr> - 0.3.0-0.4.git
- Use system dSFMT instead of bundling it.

* Thu Jun 12 2014 Milan Bouchet-Valat <nalimilan@club.fr> - 0.3.0-0.3.git
- Use llvm3.3 package when llvm is 3.4 to avoid failures.
- Fixes to support EPEL.

* Sun May 4 2014 Milan Bouchet-Valat <nalimilan@club.fr> - 0.3.0-0.2.git
- Automatically use the installed LLVM version.
- Mark dSFMT as bundled library and store version in a macro.

* Tue Apr 29 2014 Milan Bouchet-Valat <nalimilan@club.fr> - 0.3.0-0.1.git
- New upstream version 0.3.0.
- Switch to LLVM 3.4.
- Drop useless %%exclude.
- Add blank lines between changelog entries.

* Thu Dec 12 2013 Milan Bouchet-Valat <nalimilan@club.fr> - 0.2.0-2
- Make julia a meta-package and move essential parts to julia-base.
- Use %%{ix86} in ExclusiveArch rather than i386.
- Use %%{buildroot}/%%{_prefix}, %%{_sysconfdir}, %%{_libdir} and %%{_mandir}
  instead of hardcoding paths.
- Use glob pattern to match compressed or uncompressed man pages.
- Move %%post and %%postun before %%files.
- Add blank lines between Changelog entries.

* Wed Dec 11 2013 Milan Bouchet-Valat <nalimilan@club.fr> - 0.2.0-1
- Update to upstream version 0.2.0 and use system libraries as much as possible.

* Thu Jun 14 2012 Orion Poplawski <orion@cora.nwra.com> - 0-0.1.giteecafbe656863a6a8ad4969f53eed358ec2e7555
- Initial package
