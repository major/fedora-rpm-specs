# Upstream doesn't make releases.  We have to check the code out of git.
%global commit0 daad9ede0137dc58487a0abc126253e671a85b14
%global shortcommit0 %%(c=%%{commit0}; echo ${c:0:7})
%global snapdate 20231006

# This is a fork of github.com/berkeley-abc/abc.git maintained by YosysHQ
%global prjname abc

# WARNING: When updating to a newer snapshot, because upstream doesn't do
# shared library versioning, run abipkgdiff (from libabigail) against the
# old and new binary and debuginfo packages to detect abi changes that would
# require bumping the shared library version, e.g.,
#   abipkgdiff --d1 abc-libs-debuginfo-<old>.rpm \
#              --d1 abc-debuginfo-<old>.rpm \
#              --d2 abc-libs-debuginfo-<new>.rpm \
#              --d2 abc-debuginfo-<new>.rpm \
#              --devel1 abc-devel-<old>.rpm \
#              --devel2 abc-devel-<new>.rpm \
#              abc-libs-<old>.rpm abc-libs-<new>.rpm
# If the shared library version is bumped, remember to rebuild dependent
# packages, finding them using e.g.
#   repoquery --whatrequires abc-libs
# This should be done for each branch in which abc-libs will be updated.

Name:           yosyshq-%{prjname}
Version:        0.34
Release:        1.%{snapdate}git%{shortcommit0}%{?dist}
Summary:        Sequential logic synthesis and formal verification
# The ABC code itself is MIT-Modern-Variant.
# The bundled CUDD code is BSD-3-Clause.
# The bundled glucose code is MIT.
# The bundled minisat code is MIT.
# The bundled satoko code is BSD-2-Clause
License:        MIT-Modern-Variant AND MIT AND BSD-2-Clause AND BSD-3-Clause
URL:            http://github.com/YosysHQ/%{prjname}
Source0:        https://github.com/YosysHQ/%{prjname}/archive/%{commit0}/%{prjname}-%{shortcommit0}.tar.gz
# Man page created by Jerry James using upstream text; hence, it is covered by
# the same copyright and license as the code.
Source1:        %{prjname}.1
# Fedora-specific patches:
Patch1:         0001-do-not-use-bundled-libraries.patch
Patch2:         0002-build-shared-instead-of-static-library.patch
Patch3:         0003-fix-minor-header-issue.patch
Patch4:         0004-set-soname-on-the-library.patch
Patch5:         0005-fix-sprintf-calls-that-may-overflow-their-buf.patch
Patch6:         0006-fix-out-of-bounds-array-access-in-gia-code-be.patch
Patch7:         0007-weaken-overzealous-assert.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(zlib)

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

Provides:       %{prjname} = 1.01-40.%{version}.%{release}
Obsoletes:      %{prjname} < 1.01-41

%description
ABC is a growing software system for synthesis and verification of
binary sequential logic circuits appearing in synchronous hardware
designs.  ABC combines scalable logic optimization based on And-Inverter
Graphs (AIGs), optimal-delay DAG-based technology mapping for look-up
tables and standard cells, and innovative algorithms for sequential
synthesis and verification.

ABC provides an experimental implementation of these algorithms and a
programming environment for building similar applications.  Future
development will focus on improving the algorithms and making most of
the packages stand-alone.  This will allow the user to customize ABC for
their needs as if it were a toolbox rather than a complete tool.

%package libs
Summary:        Library for sequential synthesis and verification
# ABC includes a bundled and modified version of CUDD 2.4.2.  The CUDD package
# is no longer available from Fedora since the disappearance of the upstream
# web site (and the last released version was 3.0.0).
Provides:       bundled(cudd) = 2.4.2
# ABC includes a bundled and modified version of glucose (which version?)
Provides:       bundled(glucose)
# ABC includes a bundled and modified version of minisat (which version?).
Provides:       bundled(minisat2)
# ABC includes a bundled and modified version of satoko (which version?).
Provides:       bundled(satoko)

Provides:       %{prjname}-libs = 1.01-40.%{version}.%{release}
Obsoletes:      %{prjname}-libs < 1.01-41

%description libs
This package contains the core functionality of ABC as a shared library.

%package devel
Summary:        Headers and libraries for developing with ABC
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

Provides:       %{prjname}-devel = 1.01-40.%{version}.%{release}
Obsoletes:      %{prjname}-devel < 1.01-41

%description devel
Headers and libraries for developing applications that use ABC.

%prep
%autosetup -p1 -n %{prjname}-%{commit0}

# Do not use the bundled bzip2 or zlib libraries
rm -rf lib src/misc/{bzlib,zlib}

# Set the version number in the man page
sed 's/@VERSION@/%{version} (%{gitdate})/' %{SOURCE1} > %{prjname}.1
touch -r %{SOURCE1} %{prjname}.1

# Do not override Fedora optimization flags
sed -i 's/ -O//' Makefile

%build
export CFLAGS='%{build_cflags} -DNDEBUG'
export CXXFLAGS='%{build_cxxflags} -DNDEBUG'
%ifarch s390x
CFLAGS="$CFLAGS -DEPD_BIG_ENDIAN"
CXXFLAGS="$CXXFLAGS -DEPD_BIG_ENDIAN"
%endif
export ABC_MAKE_VERBOSE=1
export ABC_USE_STDINT_H=1
%cmake -DCMAKE_SKIP_RPATH:BOOL=YES -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES
%cmake_build

%install
# %%cmake_install does not install anything.  Install by hand.

# Install the binary
cd %{_vpath_builddir}
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 %{prjname} %{buildroot}%{_bindir}

# Install the library
mkdir -p %{buildroot}%{_libdir}
cp -pd lib%{prjname}.so* %{buildroot}%{_libdir}
cd -

# Install the header files
cd src
mkdir -p %{buildroot}%{_includedir}/%{prjname}
tar -cf - $(find -O3 . -name \*.h) | \
  (cd %{buildroot}%{_includedir}/%{prjname}; tar -xf -)
cd -

# Install the man page
mkdir -p %{buildroot}%{_mandir}/man1
install -p -m 0644 %{prjname}.1 %{buildroot}%{_mandir}/man1

%files
%doc README.md readmeaig
%{_bindir}/%{prjname}
%{_mandir}/man1/%{prjname}*

%files libs
%license copyright.txt
%{_libdir}/lib%{prjname}.so.0*

%files devel
%{_includedir}/%{prjname}/
%{_libdir}/lib%{prjname}.so

%changelog
* Fri Oct 06 2023 Gabriel Somlo <gsomlo@gmail.com> - 0.34-1.20231006gitdaad9ed
- update to 0.34 snapshot

* Fri Aug 04 2023 Gabriel Somlo <gsomlo@gmail.com> - 0.31-1.20230804gitbb64142
- Initial RPM
