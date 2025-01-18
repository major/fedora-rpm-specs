%bcond bootstrap      0
%bcond bundle_sqlite  0
%bcond check          1
%bcond network_checks 0
%bcond static         0

%undefine _auto_set_build_flags

Name:           build2
Version:        0.17.0
Release:        4%{?dist}
Summary:        Cross-platform build toolchain for developing and packaging C++ code

License:        MIT
URL:            https://build2.org/
Source0:        https://pkg.cppget.org/1/alpha/%{name}/%{name}-%{version}.tar.gz
Source1:        https://pkg.cppget.org/1/alpha/%{name}/libbutl-%{version}.tar.gz
Source2:        https://pkg.cppget.org/1/alpha/%{name}/libbpkg-%{version}.tar.gz
Source3:        https://pkg.cppget.org/1/alpha/%{name}/bpkg-%{version}.tar.gz
Source4:        https://pkg.cppget.org/1/alpha/%{name}/bdep-%{version}.tar.gz
Source5:        macros.%{name}

# Upstream: https://git.build2.org/cgit/bpkg/commit/?id=57d6cdd051ff1d92817e335a70e2d7d8c89b7306
Patch3000:      bpkg-fedora-dnf.patch
# Upstream: https://git.build2.org/cgit/bpkg/commit/?id=950cf3cea8075e3347d72aecbdfb26c8bb2832d4
Patch3001:      bpkg-fedora-dnf5-0.patch
# Upstream: https://git.build2.org/cgit/bpkg/commit/?id=6c96322189619c5c2eddd5645d2a6477a95dd435
Patch3002:      bpkg-fedora-dnf5-1.patch

# libpkgconf and libodb{,-sqlite} are bundled with libbutl since v0.17.0 [1]
# [1] https://lists.build2.org/archives/users/2024-June/001117.html
%global         libodb_bundle_version 2.5.0-b.27
%if %{with bundle_sqlite}
%global         sqlite_bundle_version 3.45.3
%endif

BuildRequires:  gcc-c++
%if %{with bootstrap}
BuildRequires:  make
BuildRequires:  pkgconf
%else
BuildRequires:  %{name}
BuildRequires:  %{name}-rpm-macros
%endif
%if %{with check}
# libbuild2, bpkg
BuildRequires:  bzip2
# install: libbuild2; readlink: libbuild2; sha256sum: bpkg, bdep
BuildRequires:  coreutils
# libbuild2, libbutl
BuildRequires:  diffutils
%if %{with network_checks}
# libbutl, bpkg, bdep
BuildRequires:  curl
%endif
# libbuild2, bpkg, bdep
BuildRequires:  git
# libbuild2, bpkg
BuildRequires:  gzip
# libbutl, bpkg
BuildRequires:  openssl
# libbuild2, bpkg
BuildRequires:  tar
# libbuild2, bpkg
BuildRequires:  xz
%endif
Recommends:     %{name}-rpm-macros

%description
%{name} is an open source (MIT), cross-platform build toolchain for developing
and packaging C++ code. It is a hierarchy of tools that includes the build
system, package dependency manager (for package consumption), and project
dependency manager (for project development). Key features:

 * Next-generation, Cargo-like integrated build toolchain for C++.
 * Covers entire project life cycle: creation, development, testing, and
   delivery.
 * Uniform and consistent interface across all platforms and compilers.
 * Fast, multi-threaded build system with parallel building and testing.
 * Archive and version control-based package repositories.
 * Dependency-free, all you need is a C++ compiler.

%package -n     %{name}-doc
Summary:        %{name} documentation
BuildArch:      noarch

%description -n %{name}-doc
This package contains the %{name} documentation.

%package -n     lib%{name}
Summary:        %{name} library
# libbuild2-dist
Requires:       bzip2
# install: libbuild2-install; readlink: libbuild2-bash
Requires:       coreutils
# libbuild2-test
Requires:       diffutils
# libbuild2-version
Requires:       git
# libbuild2-dist
Requires:       gzip
# libbuild2-dist
Requires:       tar
# libbuild2-dist
Requires:       xz

%description -n lib%{name}
This package contains the %{name} library.

%package -n     lib%{name}-devel
Summary:        Development files for %{name} library
Requires:       lib%{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description -n lib%{name}-devel
The lib%{name}-devel package contains libraries and header files for
developing applications that use lib%{name}.

%if %{with static}
%package -n     lib%{name}-static
Summary:        Static libraries for %{name} library
Requires:       lib%{name}-devel%{?_isa} = %{version}-%{release}

%description -n lib%{name}-static
The lib%{name}-static package contains static libraries for developing
applications that use lib%{name}.
%endif

%package -n     libbutl
Summary:        %{name} utility library
# BSD-2-Clause:
#   libbutl/lz4.{c,h}
#   libbutl/lz4hc.{c,h}
#   libbutl/mingw-*.hxx
#   libbutl/sha256c.c
#   libbutl/strptime.c
#   libbutl/timelocal.{c,h}
#   libbutl/xxhash.{c,h}
# BSD-3-Clause:
#   libbutl/sha1.c
# ISC:
#   libbutl/libbutl-pkg-config/libpkg-config
# ISC-Veillard:
#   libbutl/libbutl-pkg-config/libpkg-config/bsdstubs.c
# blessing:
#   libbutl/libbutl-odb/sqlite/sqlite3.{c,h}
%if %{with bundle_sqlite}
%global         libbutl_license MIT AND BSD-2-Clause AND BSD-3-Clause AND ISC AND ISC-Veillard AND blessing
%else
%global         libbutl_license MIT AND BSD-2-Clause AND BSD-3-Clause AND ISC AND ISC-Veillard
%endif
License:        %{libbutl_license}
Provides:       bundled(libodb) = %{libodb_bundle_version}
Provides:       bundled(libodb-sqlite) = %{libodb_bundle_version}
Provides:       bundled(libpkgconf)
%if %{with bundle_sqlite}
Provides:       bundled(sqlite) = %{sqlite_bundle_version}
%else
BuildRequires:  pkgconfig(sqlite3)
%endif
Requires:       curl
Requires:       openssl

%description -n libbutl
This package contains the %{name} utility library.

%package -n     libbutl-devel
Summary:        Development files for %{name} utility library
License:        %{libbutl_license}
Requires:       libbutl%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description -n libbutl-devel
The libbutl-devel package contains libraries and header files for
developing applications that use libbutl.

%if %{with static}
%package -n     libbutl-static
Summary:        Static libraries for %{name} utility library
License:        %{libbutl_license}
Requires:       libbutl-devel%{?_isa} = %{version}-%{release}

%description -n libbutl-static
The libbutl-static package contains static libraries for developing
applications that use libbutl.
%endif

%package -n     libbpkg
Summary:        %{name} package dependency manager library

%description -n libbpkg
This package contains the %{name} package dependency manager library.

%package -n     libbpkg-devel
Summary:        Development files for %{name} package dependency manager library
Requires:       libbpkg%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description -n libbpkg-devel
The libbpkg-devel package contains libraries and header files for
developing applications that use libbpkg.

%if %{with static}
%package -n     libbpkg-static
Summary:        Static libraries for %{name} package dependency manager library
Requires:       libbpkg-devel%{?_isa} = %{version}-%{release}

%description -n libbpkg-static
The libbpkg-static package contains static libraries for developing
applications that use libbpkg.
%endif

%package -n     bpkg
Summary:        %{name} package dependency manager
%if ! %{with bundle_sqlite}
BuildRequires:  pkgconfig(sqlite3)
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       bzip2
Requires:       coreutils
Requires:       curl
Requires:       git
Requires:       gzip
Requires:       openssl
Requires:       tar
Requires:       xz

%description -n bpkg
The %{name} package dependency manager is used to manipulate build
configurations, packages, and repositories.

%package -n     bpkg-doc
Summary:        bpkg documentation
BuildArch:      noarch

%description -n bpkg-doc
This package contains the bpkg documentation.

%package -n     bdep
Summary:        %{name} project dependency manager
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       bpkg%{?_isa} = %{version}-%{release}
Requires:       coreutils
Requires:       curl
Requires:       git

%description -n bdep
The %{name} project dependency manager is used to manage the dependencies of a
project during development.

%package -n     bdep-doc
Summary:        bdep documentation
BuildArch:      noarch

%description -n bdep-doc
This package contains the bdep documentation.

%package -n     %{name}-rpm-macros
Summary:        %{name} RPM macros
BuildArch:      noarch
Requires:       %{name}

%description -n %{name}-rpm-macros
This package contains the %{name} RPM macros.

%prep
%setup -q -c -n %{name}-toolchain-%{version} -a 1 -a 2 -a 3 -a 4
pushd bpkg-%{version}
%patch -p 1 -P 3000
%patch -p 1 -P 3001
%patch -p 1 -P 3002
popd
mv libbutl-%{version} %{name}-%{version}

%build
# Define basic installation configuration. Note that this does not include:
#  %%{_libexecdir}           %%{_exec_prefix}/libexec
#  %%{_sharedstatedir}       /var/lib
#  %%{_datadir}              %%{_prefix}/share
#  %%{_infodir}              /usr/share/info
#  %%{_localstatedir}        /var
# config.install.data and config.install.libexec seems to default to a value
# like %%{_datadir}/${project} and %%{_libexecdir}/${project} so that data files
# are not installed directly in %%{_datadir} or %%{_libexecdir}
# By specifying the installation location, the default file install mode will be
# 644, so we should set mode 755 for executable target install directories
# explicitly
%global config_install                                                          \\\
  config.install.root=%{_prefix}                                                \\\
  config.install.exec_root=%{_exec_prefix}                                      \\\
  config.install.bin=%{_bindir}                                                 \\\
  config.install.sbin=%{_sbindir}                                               \\\
  config.install.include=%{_includedir}                                         \\\
  config.install.lib=%{_libdir}                                                 \\\
  config.install.etc=%{_sysconfdir}                                             \\\
  config.install.man=%{_mandir}                                                 \\\
  config.install.legal=%{_defaultlicensedir}/"<project>"                        \\\
  config.install.pkgconfig=%{_libdir}/pkgconfig                                 \\\
  config.install.bin.mode=755                                                   \\\
  config.install.sbin.mode=755                                                  \\\
  config.install.lib.mode=755                                                   \\\
  config.install.chroot=%{?buildroot}
%if %{with bootstrap}
CC=gcc
CXX=g++
CFLAGS="${CFLAGS:-%{build_cflags}}"
CXXFLAGS="${CXXFLAGS:-%{build_cxxflags}}"
LDFLAGS="${LDFLAGS:-%{build_ldflags}}"
%ifarch %{ix86} %{arm32}
CFLAGS+=" -Wp,-D_FILE_OFFSET_BITS=64 -Wp,-D_TIME_BITS=64"
CXXFLAGS+=" -Wp,-D_FILE_OFFSET_BITS=64 -Wp,-D_TIME_BITS=64"
%endif
%ifarch %{arm32}
CFLAGS+=" -Wno-use-after-free"
CXXFLAGS+=" -Wno-use-after-free"
%endif
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/bash:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/bin:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/c:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/cc:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/cli:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/cxx:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/in:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/version:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/libbutl-%{version}/libbutl:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/libbutl-%{version}/libbutl-odb:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/libbutl-%{version}/libbutl-pkg-config:${LD_LIBRARY_PATH}
pushd %{name}-%{version}
# bootstrap, phase 1: minimal build system
export CC
export CXX
export CFLAGS
export CXXFLAGS
export LDFLAGS
%make_build -f bootstrap.gmake
# bootstrap, phase 2: statically linked build system
build2/b-boot                                                                   \
  config.bin.lib=static                                                         \
  config.c=${CC}                                                                \
  config.cxx=${CXX}                                                             \
  config.c.coptions="${CFLAGS}"                                                 \
  config.cxx.coptions="${CXXFLAGS}"                                             \
  config.cxx.loptions="${LDFLAGS}"                                              \
%if ! %{with bundle_sqlite}
  config.cxx.poptions+="$(pkgconf --cflags-only-I sqlite3)"                     \
  config.cxx.loptions+="$(pkgconf --libs-only-L sqlite3)"                       \
  config.libbutl.system_libsqlite3=true                                         \
%endif
  build2/exe{b}
mv build2/b build2/b-boot
# configure and build final, shared library build system
build2/b-boot configure                                                         \
%if ! %{with static}
  config.bin.lib=shared                                                         \
%endif
  config.bin.rpath.auto=false                                                   \
  config.bin.rpath_link.auto=true                                               \
  config.c=${CC}                                                                \
  config.cxx=${CXX}                                                             \
  config.c.coptions="${CFLAGS}"                                                 \
  config.cxx.coptions="${CXXFLAGS}"                                             \
  config.cxx.loptions="${LDFLAGS}"                                              \
%if ! %{with bundle_sqlite}
  config.libbutl.system_libsqlite3=true                                         \
%endif
%{config_install}
build2/b-boot
popd
# configure bpkg and bdep and their dependencies
%{name}-%{version}/build2/b configure:                                          \
  libbpkg-%{version}/                                                           \
  bpkg-%{version}/                                                              \
  bdep-%{version}/                                                              \
%if ! %{with static}
  config.bin.lib=shared                                                         \
%endif
  config.bin.rpath.auto=false                                                   \
  config.bin.rpath_link.auto=true                                               \
  config.c=${CC}                                                                \
  config.cxx=${CXX}                                                             \
  config.c.coptions="${CFLAGS}"                                                 \
  config.cxx.coptions="${CXXFLAGS}"                                             \
  config.cxx.loptions="${LDFLAGS}"                                              \
  config.import.%{name}="%{name}-%{version}/"                                   \
  config.import.libbutl="%{name}-%{version}/libbutl-%{version}/"                \
  config.import.libbpkg="libbpkg-%{version}/"                                   \
%{config_install}
# build bpkg and bdep and their dependencies
%{name}-%{version}/build2/b                                                     \
  libbpkg-%{version}/                                                           \
  bpkg-%{version}/                                                              \
  bdep-%{version}/
%else
# ! %%{with bootstrap}
# configure build2, bpkg, and bdep and their dependencies
%build2_configure                                                               \
  %{name}-%{version}/                                                           \
  libbpkg-%{version}/                                                           \
  bpkg-%{version}/                                                              \
  bdep-%{version}/                                                              \
%if %{with static}
  config.bin.lib=both                                                           \
%endif
%ifarch %{ix86} %{arm32}
  config.c.coptions+="-Wp,-D_FILE_OFFSET_BITS=64 -Wp,-D_TIME_BITS=64"           \
  config.cxx.coptions+="-Wp,-D_FILE_OFFSET_BITS=64 -Wp,-D_TIME_BITS=64"         \
%endif
%ifarch %{arm32}
  config.c.coptions+="-Wno-use-after-free"                                      \
  config.cxx.coptions+="-Wno-use-after-free"                                    \
%endif
  config.import.%{name}="%{name}-%{version}/"                                   \
  config.import.libbutl="%{name}-%{version}/libbutl-%{version}/"                \
  config.import.libbpkg="libbpkg-%{version}/"
# build build2, bpkg, and bdep and their dependencies
b %{name}-%{version}/                                                           \
  libbpkg-%{version}/                                                           \
  bpkg-%{version}/                                                              \
  bdep-%{version}/
%endif

%install
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/bash:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/bin:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/c:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/cc:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/cli:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/cxx:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/in:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/version:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/libbutl-%{version}/libbutl:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/libbutl-%{version}/libbutl-odb:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/libbutl-%{version}/libbutl-pkg-config:${LD_LIBRARY_PATH}
%if %{with bootstrap}
%{name}-%{version}/build2/b-boot install:                                       \
%else
b install:                                                                      \
%endif
  %{name}-%{version}/libbutl-%{version}/                                        \
  %{name}-%{version}/                                                           \
  libbpkg-%{version}/                                                           \
  bpkg-%{version}/                                                              \
  bdep-%{version}/                                                              \
# copy licenses from build2 package to libbuild2 subpackage
mkdir -p %{buildroot}%{_defaultlicensedir}/lib%{name}
cp %{buildroot}%{_defaultlicensedir}/%{name}/{AUTHORS,LICENSE} %{buildroot}%{_defaultlicensedir}/lib%{name}
install -Dpm0644 %{SOURCE5} %{buildroot}%{_rpmmacrodir}/macros.%{name}

%check
%if %{with check}
export PATH=$PWD/bpkg-%{version}/bpkg:$PATH
export PATH=$PWD/%{name}-%{version}/build2:$PATH
export LD_LIBRARY_PATH=$PWD/libbpkg-%{version}/libbpkg:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/bash:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/bin:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/c:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/cc:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/cli:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/cxx:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/in:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/lib%{name}/version:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/libbutl-%{version}/libbutl:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/libbutl-%{version}/libbutl-odb:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=$PWD/%{name}-%{version}/libbutl-%{version}/libbutl-pkg-config:${LD_LIBRARY_PATH}
b test:                                                                         \
  %{name}-%{version}/libbutl-%{version}/                                        \
  %{name}-%{version}/                                                           \
  libbpkg-%{version}/                                                           \
  bpkg-%{version}/                                                              \
  bdep-%{version}/                                                              \
%if ! %{with network_checks}
  config.bdep.tests.ci.server=''                                                \
  config.bdep.tests.publish.repository=''
%endif
%endif

%files
%dir %{_defaultlicensedir}/%{name}
%dir %{_docdir}/%{name}
%license %{_defaultlicensedir}/%{name}/AUTHORS
%license %{_defaultlicensedir}/%{name}/LICENSE
%doc %{_docdir}/%{name}/NEWS
%doc %{_docdir}/%{name}/README
%{_bindir}/b
%{_mandir}/man1/b.1*

%files -n       %{name}-doc
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/%{name}-build-system-manual*
%doc %{_docdir}/%{name}/b.xhtml
%doc %{_docdir}/%{name}/manifest

%files -n       lib%{name}
%dir %{_defaultlicensedir}/lib%{name}
%license %{_defaultlicensedir}/lib%{name}/AUTHORS
%license %{_defaultlicensedir}/lib%{name}/LICENSE
%{_datadir}/%{name}/lib%{name}/cc/std{,.compat}.cppm
%{_libdir}/lib%{name}-0.17.so
%{_libdir}/lib%{name}-bash-0.17-0.17.so
%{_libdir}/lib%{name}-bin-0.17-0.17.so
%{_libdir}/lib%{name}-c-0.17-0.17.so
%{_libdir}/lib%{name}-cc-0.17-0.17.so
%{_libdir}/lib%{name}-cli-0.17-0.17.so
%{_libdir}/lib%{name}-cxx-0.17-0.17.so
%{_libdir}/lib%{name}-in-0.17-0.17.so
%{_libdir}/lib%{name}-version-0.17-0.17.so

%files -n       lib%{name}-devel
%{_includedir}/lib%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}-bash{,-0.17}.so
%{_libdir}/lib%{name}-bin{,-0.17}.so
%{_libdir}/lib%{name}-c{,-0.17}.so
%{_libdir}/lib%{name}-cc{,-0.17}.so
%{_libdir}/lib%{name}-cli{,-0.17}.so
%{_libdir}/lib%{name}-cxx{,-0.17}.so
%{_libdir}/lib%{name}-in{,-0.17}.so
%{_libdir}/lib%{name}-version{,-0.17}.so
%{_libdir}/pkgconfig/lib%{name}{,.shared}.pc
%{_libdir}/pkgconfig/lib%{name}-bash{,.shared}.pc
%{_libdir}/pkgconfig/lib%{name}-bin{,.shared}.pc
%{_libdir}/pkgconfig/lib%{name}-c{,.shared}.pc
%{_libdir}/pkgconfig/lib%{name}-cc{,.shared}.pc
%{_libdir}/pkgconfig/lib%{name}-cli{,.shared}.pc
%{_libdir}/pkgconfig/lib%{name}-cxx{,.shared}.pc
%{_libdir}/pkgconfig/lib%{name}-in{,.shared}.pc
%{_libdir}/pkgconfig/lib%{name}-version{,.shared}.pc

%if %{with static}
%files -n       lib%{name}-static
%{_libdir}/lib%{name}.a
%{_libdir}/lib%{name}-bash.a
%{_libdir}/lib%{name}-bin.a
%{_libdir}/lib%{name}-c.a
%{_libdir}/lib%{name}-cc.a
%{_libdir}/lib%{name}-cli.a
%{_libdir}/lib%{name}-cxx.a
%{_libdir}/lib%{name}-in.a
%{_libdir}/lib%{name}-version.a
%{_libdir}/pkgconfig/lib%{name}.static.pc
%{_libdir}/pkgconfig/lib%{name}-bash.static.pc
%{_libdir}/pkgconfig/lib%{name}-bin.static.pc
%{_libdir}/pkgconfig/lib%{name}-c.static.pc
%{_libdir}/pkgconfig/lib%{name}-cc.static.pc
%{_libdir}/pkgconfig/lib%{name}-cli.static.pc
%{_libdir}/pkgconfig/lib%{name}-cxx.static.pc
%{_libdir}/pkgconfig/lib%{name}-in.static.pc
%{_libdir}/pkgconfig/lib%{name}-version.static.pc
%endif

%files -n       libbutl
%dir %{_defaultlicensedir}/libbutl
%license %{_defaultlicensedir}/libbutl/AUTHORS
%license %{_defaultlicensedir}/libbutl/COPYRIGHT
%license %{_defaultlicensedir}/libbutl/LICENSE
%{_libdir}/libbutl-0.17.so
%{_libdir}/libbutl-odb-0.17.so
%{_libdir}/libbutl-pkg-config-0.17.so

%files -n       libbutl-devel
%dir %{_docdir}/libbutl
%doc %{_docdir}/libbutl/manifest
%doc %{_docdir}/libbutl/NEWS
%doc %{_docdir}/libbutl/README
%{_includedir}/libbutl
%{_libdir}/libbutl.so
%{_libdir}/libbutl-odb.so
%{_libdir}/libbutl-pkg-config.so
%{_libdir}/pkgconfig/libbutl{,.shared}.pc
%{_libdir}/pkgconfig/libbutl-odb{,.shared}.pc
%{_libdir}/pkgconfig/libbutl-pkg-config{,.shared}.pc

%if %{with static}
%files -n       libbutl-static
%{_libdir}/libbutl.a
%{_libdir}/libbutl-odb.a
%{_libdir}/libbutl-pkg-config.a
%{_libdir}/pkgconfig/libbutl.static.pc
%{_libdir}/pkgconfig/libbutl-odb.static.pc
%{_libdir}/pkgconfig/libbutl-pkg-config.static.pc
%endif

%files -n       libbpkg
%dir %{_defaultlicensedir}/libbpkg
%license %{_defaultlicensedir}/libbpkg/AUTHORS
%license %{_defaultlicensedir}/libbpkg/LICENSE
%{_libdir}/libbpkg-0.17.so

%files -n       libbpkg-devel
%dir %{_docdir}/libbpkg
%doc %{_docdir}/libbpkg/manifest
%doc %{_docdir}/libbpkg/NEWS
%doc %{_docdir}/libbpkg/README
%{_includedir}/libbpkg
%{_libdir}/libbpkg.so
%{_libdir}/pkgconfig/libbpkg{,.shared}.pc

%if %{with static}
%files -n       libbpkg-static
%{_libdir}/libbpkg.a
%{_libdir}/pkgconfig/libbpkg.static.pc
%endif

%files -n       bpkg
%dir %{_defaultlicensedir}/bpkg
%dir %{_docdir}/bpkg
%license %{_defaultlicensedir}/bpkg/AUTHORS
%license %{_defaultlicensedir}/bpkg/LEGAL
%license %{_defaultlicensedir}/bpkg/LICENSE
%doc %{_docdir}/bpkg/NEWS
%doc %{_docdir}/bpkg/README
%{_bindir}/bpkg
%{_mandir}/man1/bpkg.1*
%{_mandir}/man1/bpkg-*1.*

%files -n       bpkg-doc
%dir %{_docdir}/bpkg
%doc %{_docdir}/bpkg/%{name}-package-manager-manual*
%doc %{_docdir}/bpkg/bpkg*.xhtml
%doc %{_docdir}/bpkg/manifest

%files -n       bdep
%dir %{_defaultlicensedir}/bdep
%dir %{_docdir}/bdep
%license %{_defaultlicensedir}/bdep/AUTHORS
%license %{_defaultlicensedir}/bdep/LEGAL
%license %{_defaultlicensedir}/bdep/LICENSE
%doc %{_docdir}/bdep/NEWS
%doc %{_docdir}/bdep/README
%{_bindir}/bdep
%{_mandir}/man1/bdep.1*
%{_mandir}/man1/bdep-*1.*

%files -n       bdep-doc
%dir %{_docdir}/bdep
%doc %{_docdir}/bdep/bdep*.xhtml
%doc %{_docdir}/bdep/manifest

%files -n       %{name}-rpm-macros
%{_rpmmacrodir}/macros.%{name}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 11 2024 Matthew Krupcale <mkrupcale@gmail.com> - 0.17.0-3
- Add bpkg patches for dnf5

* Sat Sep  7 2024 Matthew Krupcale <mkrupcale@gmail.com> - 0.17.0-2
- Disable bootstrap

* Sun Aug 18 2024 Matthew Krupcale <mkrupcale@gmail.com> - 0.17.0-1
- Update to v0.17.0

* Wed Aug 07 2024 Neal Gompa <ngompa@fedoraproject.org> - 0.16.0-7
- Rebuild for pkgconf 2.3.0

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Jens Petersen <petersen@redhat.com> - 0.16.0-5
- rebuild (against pkgconf-2.1.1) for F40+

* Sat Apr 20 2024 Matthew Krupcale <mkrupcale@gmail.com> - 0.16.0-4
- Rebuild for libpkgconf ABI changes
- Apply patch to silence OpenSSL v3.2.0 warnings in bpkg

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 31 2023 Matthew Krupcale <mkrupcale@matthewkrupcale.com> - 0.16.0-1
- Update to v0.16.0

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Mar  4 2023 Matthew Krupcale <mkrupcale@matthewkrupcale.com> - 0.15.0-2
- Add and remove required patches for Fedora 38
- Use SPDX license expressions

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 30 2022 Matthew Krupcale <mkrupcale@matthewkrupcale.com> - 0.15.0-1
- Update to v0.15.0

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jan 23 2022 Matthew Krupcale <mkrupcale@matthewkrupcale.com> - 0.14.0-1
- Update to v0.14.0

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Matthew Krupcale <mkrupcale@matthewkrupcale.com> - 0.13.0-1
- Update to v0.13.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 20 2019 Matthew Krupcale <mkrupcale@matthewkrupcale.com> - 0.12.0-1
- Update to v0.12.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Matthew Krupcale <mkrupcale@matthewkrupcale.com> - 0.11.0-1
- Initial package
