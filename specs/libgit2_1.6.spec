# libssh2 is not available on RHEL
%if 0%{?rhel}
%bcond_with libssh2
%else
%bcond_without libssh2
%endif

Name:           libgit2_1.6
Version:        1.6.5
Release:        %autorelease
Summary:        C implementation of the Git core methods as a library with a solid API
License:        GPLv2 with exceptions
URL:            https://libgit2.org/
Source0:        https://github.com/libgit2/libgit2/archive/refs/tags/v%{version}.tar.gz#/libgit2-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake >= 3.5.1
BuildRequires:  ninja-build
BuildRequires:  http-parser-devel
BuildRequires:  libcurl-devel
%if %{with libssh2}
BuildRequires:  libssh2-devel
%endif
BuildRequires:  openssl-devel
BuildRequires:  pcre2-devel
BuildRequires:  python3
BuildRequires:  zlib-devel
Provides:       bundled(libxdiff)

%description
libgit2 is a portable, pure C implementation of the Git core methods
provided as a re-entrant linkable library with a solid API, allowing
you to write native speed custom Git applications in any language
with bindings.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
# This compat -devel package provides an older version of libgit2-devel
Provides:       libgit2-devel = %{?epoch:%{epoch}:}%{version}-%{release}
# These devel packages are not installable in parallel
Conflicts:      pkgconfig(libgit2)

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n libgit2-%{version}

# Remove VCS files from examples
find examples -name ".gitignore" -delete -print

# Don't run "online" tests
sed -i '/-sonline/s/^/#/' tests/libgit2/CMakeLists.txt

%if 0%{?fedora} >= 40 || 0%{?rhel} >= 10
# On Fedora 40+ and RHEL 10+, we're using zlib-ng rather than
# zlib for compression. As a result, all of the pack tests fail
# due to checking the hashes of the packed data against static
# values that were created with zlib.
# https://github.com/libgit2/libgit2/issues/6728
sed -i 's/-xonline/-xonline -xpack/' tests/libgit2/CMakeLists.txt
%endif

# Remove bundled libraries
rm -vr deps

%build
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DREGEX_BACKEND=pcre2 \
  -DBUILD_CLI=OFF \
  -DUSE_HTTP_PARSER=system \
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
%{_libdir}/libgit2.so.1.6*

%files devel
%doc AUTHORS docs examples README.md
%{_libdir}/libgit2.so
%{_libdir}/pkgconfig/libgit2.pc
%{_includedir}/git2.h
%{_includedir}/git2/

%changelog
%autochangelog