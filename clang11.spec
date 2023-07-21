%global compat_build 1

%global maj_ver 11
%global min_ver 1
%global patch_ver 0
%global rc_ver 2
%global baserelease 12

%global clang_tools_binaries \
	%{_bindir}/clang-apply-replacements \
	%{_bindir}/clang-change-namespace \
	%{_bindir}/clang-check \
	%{_bindir}/clang-doc \
	%{_bindir}/clang-extdef-mapping \
	%{_bindir}/clang-format \
	%{_bindir}/clang-include-fixer \
	%{_bindir}/clang-move \
	%{_bindir}/clang-offload-bundler \
	%{_bindir}/clang-offload-wrapper \
	%{_bindir}/clang-query \
	%{_bindir}/clang-refactor \
	%{_bindir}/clang-rename \
	%{_bindir}/clang-reorder-fields \
	%{_bindir}/clang-scan-deps \
	%{_bindir}/clang-tidy \
	%{_bindir}/clangd \
	%{_bindir}/diagtool \
	%{_bindir}/hmaptool \
	%{_bindir}/pp-trace

%global clang_binaries \
	%{_bindir}/clang \
	%{_bindir}/clang++ \
	%{_bindir}/clang-%{maj_ver} \
	%{_bindir}/clang++-%{maj_ver} \
	%{_bindir}/clang-cl \
	%{_bindir}/clang-cpp \

%if 0%{?compat_build}
%global pkg_name clang%{maj_ver}
# Install clang to same prefix as llvm, so that apps that use llvm-config
# will also be able to find clang libs.
%global install_prefix %{_libdir}/llvm%{maj_ver}
%global install_bindir %{install_prefix}/bin
%global install_includedir %{install_prefix}/include
%global install_libdir %{install_prefix}/lib

%global pkg_bindir %{install_bindir}
%global pkg_includedir %{install_includedir}
%global pkg_libdir %{install_libdir}
%else
%global pkg_name clang
%global install_prefix /usr
%global pkg_libdir %{_libdir}
%endif

%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_without python3
%else
%bcond_with python3
%endif

%global build_install_prefix %{buildroot}%{install_prefix}

%ifarch ppc64le
# Too many threads on ppc64 systems causes OOM errors.
%global _smp_mflags -j8
%endif

%global clang_srcdir clang-%{version}%{?rc_ver:rc%{rc_ver}}.src
%global clang_tools_srcdir clang-tools-extra-%{version}%{?rc_ver:rc%{rc_ver}}.src

Name:		%pkg_name
Version:	%{maj_ver}.%{min_ver}.%{patch_ver}
Release:	%{?rc_ver:0.}%{baserelease}%{?rc_ver:.rc%{rc_ver}}%{?dist}
Summary:	A C language family front-end for LLVM

License:	NCSA
URL:		http://llvm.org
Source0:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{version}%{?rc_ver:-rc%{rc_ver}}/%{clang_srcdir}.tar.xz
Source3:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{version}%{?rc_ver:-rc%{rc_ver}}/%{clang_srcdir}.tar.xz.sig
%if !0%{?compat_build}
Source1:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{version}%{?rc_ver:-rc%{rc_ver}}/%{clang_tools_srcdir}.tar.xz
Source2:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{version}%{?rc_ver:-rc%{rc_ver}}/%{clang_tools_srcdir}.tar.xz.sig
%endif
Source4:	tstellar-gpg-key.asc

Patch4:		0002-gtest-reorg.patch
Patch11:	0001-ToolChain-Add-lgcc_s-to-the-linker-flags-when-using-.patch
Patch13:	0001-Make-funwind-tables-the-default-for-all-archs.patch

# Not Upstream
Patch15:	0001-clang-Don-t-install-static-libraries.patch
Patch16:	0001-clang-Fix-spurious-test-failure.patch
Patch17:	0001-Driver-Prefer-gcc-toolchains-with-libgcc_s.so-when-n.patch
Patch18:	0001-scan-view-Remove-Reporter.py-and-associated-AppleScr.patch
Patch19:	0001-Partially-Revert-scan-view-Remove-Reporter.py-and-as.patch

BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	ninja-build
%if 0%{?compat_build}
BuildRequires:	llvm%{maj_ver}-devel = %{version}
BuildRequires:	llvm%{maj_ver}-static = %{version}
%else
BuildRequires:	llvm-devel = %{version}
BuildRequires:	llvm-test = %{version}
# llvm-static is required, because clang-tablegen needs libLLVMTableGen, which
# is not included in libLLVM.so.
BuildRequires:	llvm-static = %{version}
BuildRequires:	llvm-googletest = %{version}
%endif

BuildRequires:	libxml2-devel
BuildRequires:	perl-generators
BuildRequires:	ncurses-devel
# According to https://fedoraproject.org/wiki/Packaging:Emacs a package
# should BuildRequires: emacs if it packages emacs integration files.
BuildRequires:	emacs

# These build dependencies are required for the test suite.
%if %with python3
# The testsuite uses /usr/bin/lit which is part of the python3-lit package.
BuildRequires:	python3-lit
%endif

BuildRequires:	python3-sphinx
BuildRequires:	libatomic

# We need python3-devel for pathfix.py.
BuildRequires:	python3-devel

# Needed for %%multilib_fix_c_header
BuildRequires:	multilib-rpm-config

# For origin certification
BuildRequires:	gnupg2

# scan-build uses these perl modules so they need to be installed in order
# to run the tests.
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(File::Copy)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Temp)
BuildRequires: perl(FindBin)
BuildRequires: perl(Hash::Util)
BuildRequires: perl(lib)
BuildRequires: perl(Term::ANSIColor)
BuildRequires: perl(Text::ParseWords)
BuildRequires: perl(Sys::Hostname)

Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

# clang requires gcc, clang++ requires libstdc++-devel
# - https://bugzilla.redhat.com/show_bug.cgi?id=1021645
# - https://bugzilla.redhat.com/show_bug.cgi?id=1158594
Requires:	libstdc++-devel
Requires:	gcc-c++

Provides:	clang(major) = %{maj_ver}

Conflicts:	compiler-rt < %{version}
Conflicts:	compiler-rt > %{version}

%description
clang: noun
    1. A loud, resonant, metallic sound.
    2. The strident call of a crane or goose.
    3. C-language family front-end toolkit.

The goal of the Clang project is to create a new C, C++, Objective C
and Objective C++ front-end for the LLVM compiler. Its tools are built
as libraries and designed to be loosely-coupled and extensible.

Install compiler-rt if you want the Blocks C language extension or to
enable sanitization and profiling options when building, and
libomp-devel to enable -fopenmp.

%package libs
Summary: Runtime library for clang
Requires: %{name}-resource-filesystem%{?_isa} = %{version}
Recommends: compiler-rt%{?_isa} = %{version}
# libomp-devel is required, so clang can find the omp.h header when compiling
# with -fopenmp.
Recommends: libomp-devel%{_isa} = %{version}
Recommends: libomp%{_isa} = %{version}

%description libs
Runtime library for clang.

%package devel
Summary: Development header files for clang
%if !0%{?compat_build}
Requires: %{name}%{?_isa} = %{version}-%{release}
# The clang CMake files reference tools from clang-tools-extra.
Requires: %{name}-tools-extra%{?_isa} = %{version}-%{release}
Requires: %{name}-libs = %{version}-%{release}
%endif

%description devel
Development header files for clang.

%package resource-filesystem
Summary: Filesystem package that owns the clang resource directory
Provides: %{name}-resource-filesystem(major) = %{maj_ver}

%description resource-filesystem
This package owns the clang resouce directory: $libdir/clang/$version/

%if !0%{?compat_build}
%package analyzer
Summary:	A source code analysis framework
License:	NCSA and MIT
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}

%description analyzer
The Clang Static Analyzer consists of both a source code analysis
framework and a standalone tool that finds bugs in C and Objective-C
programs. The standalone tool is invoked from the command-line, and is
intended to run in tandem with a build of a project or code base.

%package tools-extra
Summary:	Extra tools for clang
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	emacs-filesystem

%description tools-extra
A set of extra tools built using Clang's tooling API.

# Put git-clang-format in its own package, because it Requires git
# and we don't want to force users to install all those dependenices if they
# just want clang.
%package -n git-clang-format
Summary:	Integration of clang-format for git
Requires:	%{name}-tools-extra = %{version}-%{release}
Requires:	git
Requires:	python3

%description -n git-clang-format
clang-format integration for git.


%package -n python3-clang
Summary:       Python3 bindings for clang
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}
Requires:      python3
%description -n python3-clang
%{summary}.


%endif


%prep
%{gpgverify} --keyring='%{SOURCE4}' --signature='%{SOURCE3}' --data='%{SOURCE0}'

%if 0%{?compat_build}
%autosetup -n %{clang_srcdir} -p1
%else

%{gpgverify} --keyring='%{SOURCE4}' --signature='%{SOURCE2}' --data='%{SOURCE1}'
%setup -T -q -b 1 -n %{clang_tools_srcdir}


pathfix.py -i %{__python3} -pn \
	clang-tidy/tool/*.py \
	clang-include-fixer/find-all-symbols/tool/run-find-all-symbols.py

%setup -q -n %{clang_srcdir}

%patch4 -p1 -b .gtest
%patch11 -p1 -b .libcxx-fix
%patch13 -p1 -b .unwind-all
%patch15 -p1 -b .no-install-static
%patch16 -p1 -b .test-fix2
%patch17 -p1 -b .check-gcc_s
%patch18 -p1 -b .scan-view-remove-files
%patch19 -p1 -b .scan-view-remove-files-fix

# Patch does not support binary diffs from git so we have to manually delete
# this:
rm tools/scan-view/share/FileRadar.scpt

mv ../%{clang_tools_srcdir} tools/extra

pathfix.py -i %{__python3} -pn \
	tools/clang-format/*.py \
	tools/clang-format/git-clang-format \
	utils/hmaptool/hmaptool \
	tools/scan-view/bin/scan-view \
	tools/scan-view/share/Reporter.py \
	tools/scan-view/share/startfile.py
%endif

%build

# We run the builders out of memory on armv7 and i686 when LTO is enabled
%ifarch %{arm} i686
%define _lto_cflags %{nil}
%else
# This package does not ship any object files or static libraries, so we
# don't need -ffat-lto-objects.
%global _lto_cflags %(echo %{_lto_cflags} | sed 's/-ffat-lto-objects//')
%endif

# lto builds with gcc 11 fail while running the lit tests.
%define _lto_cflags %{nil}

%if 0%{?__isa_bits} == 64
sed -i 's/\@FEDORA_LLVM_LIB_SUFFIX\@/64/g' test/lit.cfg.py
%else
sed -i 's/\@FEDORA_LLVM_LIB_SUFFIX\@//g' test/lit.cfg.py
%endif

%ifarch s390 s390x %{arm} %ix86 ppc64le
# Decrease debuginfo verbosity to reduce memory consumption during final library linking
%global optflags %(echo %{optflags} | sed 's/-g /-g1 /')
%endif

# -DCMAKE_INSTALL_RPATH=";" is a workaround for llvm manually setting the
# rpath of libraries and binaries.  llvm will skip the manual setting
# if CAMKE_INSTALL_RPATH is set to a value, but cmake interprets this value
# as nothing, so it sets the rpath to "" when installing.
%cmake  -G Ninja \
	-DLLVM_PARALLEL_LINK_JOBS=1 \
	-DLLVM_LINK_LLVM_DYLIB:BOOL=ON \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DPYTHON_EXECUTABLE=%{__python3} \
	-DCMAKE_INSTALL_RPATH:BOOL=";" \
%ifarch s390 s390x %{arm} %ix86 ppc64le
	-DCMAKE_C_FLAGS_RELWITHDEBINFO="%{optflags} -DNDEBUG" \
	-DCMAKE_CXX_FLAGS_RELWITHDEBINFO="%{optflags} -DNDEBUG" \
%endif
%if 0%{?compat_build}
	-DCLANG_BUILD_TOOLS:BOOL=OFF \
	-DLLVM_CONFIG:FILEPATH=%{_bindir}/llvm-config-%{maj_ver} \
	-DCMAKE_INSTALL_PREFIX=%{install_prefix} \
	-DCLANG_INCLUDE_TESTS:BOOL=OFF \
%else
	-DCLANG_INCLUDE_TESTS:BOOL=ON \
	-DLLVM_EXTERNAL_LIT=%{_bindir}/lit \
	-DLLVM_MAIN_SRC_DIR=%{_datadir}/llvm/src \
%if 0%{?__isa_bits} == 64
	-DLLVM_LIBDIR_SUFFIX=64 \
%else
	-DLLVM_LIBDIR_SUFFIX= \
%endif
%endif
	\
%if 0%{compat_build}
	-DLLVM_TABLEGEN_EXE:FILEPATH=%{_bindir}/llvm-tblgen-%{maj_ver} \
%else
	-DLLVM_TABLEGEN_EXE:FILEPATH=%{_bindir}/llvm-tblgen \
%endif
	-DCLANG_ENABLE_ARCMT:BOOL=ON \
	-DCLANG_ENABLE_STATIC_ANALYZER:BOOL=ON \
	-DCLANG_INCLUDE_DOCS:BOOL=ON \
	-DCLANG_PLUGIN_SUPPORT:BOOL=ON \
	-DENABLE_LINKER_BUILD_ID:BOOL=ON \
	-DLLVM_ENABLE_EH=ON \
	-DLLVM_ENABLE_RTTI=ON \
	-DLLVM_BUILD_DOCS=ON \
	-DLLVM_ENABLE_SPHINX=ON \
	-DCLANG_LINK_CLANG_DYLIB=ON \
	-DSPHINX_WARNINGS_AS_ERRORS=OFF \
	\
	-DCLANG_BUILD_EXAMPLES:BOOL=OFF \
	-DBUILD_SHARED_LIBS=OFF \
	-DCLANG_REPOSITORY_STRING="%{?fedora:Fedora}%{?rhel:Red Hat} %{version}-%{release}"

%cmake_build

%install

%cmake_install

%if 0%{?compat_build}

# Remove binaries/other files
rm -Rf %{buildroot}%{install_bindir}
rm -Rf %{buildroot}%{install_prefix}/share
rm -Rf %{buildroot}%{install_prefix}/libexec

# Create sub-directories in the clang resource directory that will be
# populated by other packages
mkdir -p %{buildroot}%{pkg_libdir}/clang/%{version}/{include,lib,share}/

%else

# install clang python bindings
mkdir -p %{buildroot}%{python3_sitelib}/clang/
install -p -m644 bindings/python/clang/* %{buildroot}%{python3_sitelib}/clang/
%py_byte_compile %{__python3} %{buildroot}%{python3_sitelib}/clang

# multilib fix
%multilib_fix_c_header --file %{_includedir}/clang/Config/config.h

# Move emacs integration files to the correct directory
mkdir -p %{buildroot}%{_emacs_sitestartdir}
for f in clang-format.el clang-rename.el clang-include-fixer.el; do
mv %{buildroot}{%{_datadir}/clang,%{_emacs_sitestartdir}}/$f
done

# remove editor integrations (bbedit, sublime, emacs, vim)
rm -vf %{buildroot}%{_datadir}/clang/clang-format-bbedit.applescript
rm -vf %{buildroot}%{_datadir}/clang/clang-format-sublime.py*

# TODO: Package html docs
rm -Rvf %{buildroot}%{_docdir}/clang/html
rm -Rvf %{buildroot}%{_datadir}/clang/clang-doc-default-stylesheet.css
rm -Rvf %{buildroot}%{_datadir}/clang/index.js

# TODO: What are the Fedora guidelines for packaging bash autocomplete files?
rm -vf %{buildroot}%{_datadir}/clang/bash-autocomplete.sh

# Create Manpage symlinks
ln -s clang.1.gz %{buildroot}%{_mandir}/man1/clang++.1.gz
ln -s clang.1.gz %{buildroot}%{_mandir}/man1/clang-%{maj_ver}.1.gz
ln -s clang.1.gz %{buildroot}%{_mandir}/man1/clang++-%{maj_ver}.1.gz

# Add clang++-{version} symlink
ln -s clang++ %{buildroot}%{_bindir}/clang++-%{maj_ver}


# Fix permission
chmod u-x %{buildroot}%{_mandir}/man1/scan-build.1*
chmod a+x %{buildroot}%{_datadir}/scan-view/{Reporter.py,startfile.py}

# create a link to clang's resource directory that is "constant" across minor
# version bumps
# this is required for packages like ccls that hardcode the link to clang's
# resource directory to not require rebuilds on minor version bumps
# Fix for bugs like rhbz#1807574
pushd %{buildroot}%{_libdir}/clang/
ln -s %{version} %{maj_ver}
popd

# Create sub-directories in the clang resource directory that will be
# populated by other packages
mkdir -p %{buildroot}%{_libdir}/clang/%{version}/{include,lib,share}/

%endif

# Remove clang-tidy headers.  We don't ship the libraries for these.
rm -Rvf %{buildroot}%{_includedir}/clang-tidy/

%check
%if !0%{?compat_build}
# requires lit.py from LLVM utilities
# FIXME: Fix failing ARM tests
LD_LIBRARY_PATH=%{buildroot}/%{_libdir} %cmake_build --target check-all || \
%ifarch %{arm}
:
%else
false
%endif

%endif


%if !0%{?compat_build}
%files
%license LICENSE.TXT
%{clang_binaries}
%{_mandir}/man1/clang.1.gz
%{_mandir}/man1/clang++.1.gz
%{_mandir}/man1/clang-%{maj_ver}.1.gz
%{_mandir}/man1/clang++-%{maj_ver}.1.gz
%endif

%files libs
%if !0%{?compat_build}
%{_libdir}/clang/
%{_libdir}/*.so.*
%else
%{pkg_libdir}/*.so.*
%{pkg_libdir}/clang/%{version}
%endif

%files devel
%if !0%{?compat_build}
%{_libdir}/*.so
%{_includedir}/clang/
%{_includedir}/clang-c/
%{_libdir}/cmake/*
%dir %{_datadir}/clang/
%else
%{pkg_libdir}/*.so
%{pkg_includedir}/clang/
%{pkg_includedir}/clang-c/
%{pkg_libdir}/cmake/
%endif

%files resource-filesystem
%dir %{pkg_libdir}/clang/%{version}/
%dir %{pkg_libdir}/clang/%{version}/include/
%dir %{pkg_libdir}/clang/%{version}/lib/
%dir %{pkg_libdir}/clang/%{version}/share/
%if !0%{?compat_build}
%{pkg_libdir}/clang/%{maj_ver}
%endif

%if !0%{?compat_build}
%files analyzer
%{_bindir}/scan-view
%{_bindir}/scan-build
%{_libexecdir}/ccc-analyzer
%{_libexecdir}/c++-analyzer
%{_datadir}/scan-view/
%{_datadir}/scan-build/
%{_mandir}/man1/scan-build.1.*

%files tools-extra
%{clang_tools_binaries}
%{_bindir}/c-index-test
%{_bindir}/find-all-symbols
%{_bindir}/modularize
%{_mandir}/man1/diagtool.1.gz
%{_emacs_sitestartdir}/clang-format.el
%{_emacs_sitestartdir}/clang-rename.el
%{_emacs_sitestartdir}/clang-include-fixer.el
%{_datadir}/clang/clang-format.py*
%{_datadir}/clang/clang-format-diff.py*
%{_datadir}/clang/clang-include-fixer.py*
%{_datadir}/clang/clang-tidy-diff.py*
%{_datadir}/clang/run-clang-tidy.py*
%{_datadir}/clang/run-find-all-symbols.py*
%{_datadir}/clang/clang-rename.py*

%files -n git-clang-format
%{_bindir}/git-clang-format

%files -n python3-clang
%{python3_sitelib}/clang/


%endif
%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.1.0-0.12.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.1.0-0.11.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.1.0-0.10.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.1.0-0.9.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.1.0-0.8.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May 18 2021 sguelton@redhat.com - 11.1.0-0.7.rc2
- Use the alternative-managed version of llvm-config

* Fri Feb 19 2021 sguelton@redhat.com - 11.1.0-0.6.rc2
- Update cmake file to reflect install changes (ter)

* Fri Feb 19 2021 sguelton@redhat.com - 11.1.0-0.5.rc2
- Update cmake file to reflect install changes (bis)

* Thu Feb 18 2021 sguelton@redhat.com - 11.1.0-0.4.rc2
- Update cmake file to reflect install changes

* Thu Feb 18 2021 sguelton@redhat.com - 11.1.0-0.3.rc2
- Remove all tool reference for compat package

* Thu Feb 18 2021 sguelton@redhat.com - 11.1.0-0.2.rc2
- Remove reference to diagtool in compat package

* Fri Feb 12 2021 sguelton@redhat.com - 11.1.0-0.1.rc2
- 11.1.0-rc2 release

