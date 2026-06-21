# libssh2 is not available on RHEL
%bcond libssh2 %{undefined rhel}

Name:           libgit2_1.9
Version:        1.9.4
Release:        %autorelease
Summary:        C implementation of the Git core methods as a library with a solid API
# The main code is GPL-2.0-only WITH GCC-exception-2.0
# The bundled PCRE implementation is BSD-3-Clause - but not used
# The bundled winhttp definition is LGPL-2.1-or-later - but not used
# The bundled ntlmclient is MIT - but not used
# Zlib is Zlib - but not used
# The bundled SHA1 collision detection and
#    the bundled llhttp dependency (which is not used) and
#    portions of this software derived from Team Explorer Everywhere are MIT
# The bundled wildmatch code and xoroshiro256 are LicenseRef-Fedora-Public-Domain
# OpenSSL headers are Apache-2.0
# built-in SHA256 support is SSLeay-standalone
# The built-in git_fs_path_basename_r() is BSD-2-Clause
# Portions of this software derived from the LLVM Compiler Infrastructure is NCSA
# Portions of this software derived from sheredom/utf8.h is Unlicense
# The Clar framework is ISC - but used only in tests
License:        GPL-2.0-only WITH GCC-exception-2.0 AND MIT AND LicenseRef-Fedora-Public-Domain AND Apache-2.0 AND SSLeay-standalone AND BSD-2-Clause AND NCSA AND Unlicense
URL:            https://libgit2.org/
Source0:        https://github.com/libgit2/libgit2/archive/refs/tags/v%{version_no_tilde}.tar.gz#/libgit2-%{version_no_tilde}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake >= 3.5.1
BuildRequires:  ninja-build
BuildRequires:  llhttp-devel
BuildRequires:  krb5-devel
BuildRequires:  libcurl-devel
%if %{with libssh2}
BuildRequires:  libssh2-devel
%endif
BuildRequires:  openssl-devel
BuildRequires:  pcre2-devel
BuildRequires:  python3
BuildRequires:  zlib-devel

Provides:       bundled(libxdiff)

# renamed in Fedora 45
Obsoletes:      libgit2 < 1.9.4-3

%description
libgit2 is a portable, pure C implementation of the Git core methods
provided as a re-entrant linkable library with a solid API, allowing
you to write native speed custom Git applications in any language
with bindings.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

# explicitly conflict with other libgit2 devel packages
Conflicts:      pkgconfig(libgit2)

# renamed in Fedora 45
Obsoletes:      libgit2-devel < 1.9.4-3

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n libgit2-%{version_no_tilde}

# Remove VCS files from examples
find examples -name ".gitignore" -delete -print

# Don't run "online" tests
sed -i '/-sonline/s/^/#/' tests/libgit2/CMakeLists.txt

# Remove bundled libraries (except libxdiff)
pushd deps
find . -maxdepth 1 -not -name xdiff -exec rm -rf {} ';'
popd

%build
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DREGEX_BACKEND=pcre2 \
  -DBUILD_CLI=OFF \
  -DUSE_HTTP_PARSER=llhttp \
  -DUSE_SHA1=HTTPS \
  -DUSE_HTTPS=OpenSSL \
  -DUSE_NTLMCLIENT=OFF \
%if %{with libssh2}
  -DUSE_SSH=ON \
%else
  -DUSE_SSH=OFF \
%endif
  %{nil}
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license COPYING
%{_libdir}/libgit2.so.1.9*

%files devel
%doc AUTHORS docs examples README.md
%{_libdir}/libgit2.so
%{_libdir}/cmake/libgit2/
%{_libdir}/pkgconfig/libgit2.pc
%{_includedir}/git2.h
%{_includedir}/git2/

%changelog
%autochangelog
