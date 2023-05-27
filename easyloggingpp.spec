# We use a git snapshot because the release tag does not contain the
# CHANGELOG.md and README.md updates for the release.
%global commit 8489989bb26c6371df103f6cbced3fbee1bc3c2f
%global snapdate 20210202

# This library is historically header-only. At some point, it gained a C++
# source file in an effort to reduce compile times. The upstream build system
# supports building as a static library, and it could be extended to support a
# shared library; see
#
#   Add shared library support and fix library install path on Linux
#   https://github.com/amrayn/easyloggingpp/pull/815
#
# for a demonstration and commentary. The problem is that there are a
# significant number of compile-time configuration flags controlled by
# preprocessor macros—not only conditional feature enablement, but behavior
# changes—that are expected to be controlled by the code using Easylogging++ as
# a library. See
#
#   https://github.com/amrayn/easyloggingpp/tree/v9.97.0#configuration-macros
#
# for details. Building a system-wide shared library is therefore unlikely to
# be useful, as whichever settings we choose, programs are likely to require
# different ones.
#
# Instead, we treat the easylogging++.cc C++ source file as effectively “just
# another header,” following the lead of the upstream build system—which
# already installs it in “${PREFIX}/include”—and package this as a header-only
# library with one strangely-named header.

Name:           easyloggingpp
Version:        9.97.0^%{snapdate}git%(c='%{commit}'; echo "${c:0:7}")
Release:        %autorelease
Epoch:          1
Summary:        C++ logging library

# SPDX
License:        MIT
URL:            https://github.com/amrayn/easyloggingpp
Source:         %{url}/archive/%{commit}/easyloggingpp-%{commit}.tar.gz

# No shebang = not executable
# https://github.com/amrayn/easyloggingpp/pull/817
Patch:          %{url}/pull/817.patch
# Convert words.txt from ISO-8859-1 to UTF-8
# https://github.com/amrayn/easyloggingpp/pull/818
Patch:          %{url}/pull/818.patch
# Version 1.13.0 of gtest requires C++14
# https://github.com/amrayn/easyloggingpp/issues/830
#   Downstream-only patch switching *only the CMake build system* from C++11 to
#   C++14:
Patch:          0001-Switch-CMake-build-system-from-C-11-to-C-14.patch

# No compiled code is installed, so there are no debugging symbols.
%global debug_package %{nil}

BuildRequires:  gcc-c++
BuildRequires:  cmake
# Our choice; the make backend would work just fine.
BuildRequires:  ninja-build

BuildRequires:  cmake(gtest)

BuildRequires:  hardlink
BuildRequires:  symlinks
BuildRequires:  dos2unix

%global common_description %{expand:
Easylogging++ is an efficient logging library for C++ applications. It is
extremely powerful, highly extendable and configurable to a user’s
requirements. It provides the ability to write your own sinks (via featured
referred as LogDispatchCallback). This library is currently used by hundreds of
open-source projects on github and other open-source source control management
sites.}

%description %{common_description}


%package        devel
Summary:        Development files for Easylogging++

BuildArch:      noarch

# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_packaging_header_only_libraries
Provides:       easyloggingpp-static = %{?epoch:%{epoch}:}%{version}-%{release}

%description    devel %{common_description}

The easyloggingpp-devel package contains libraries and header files for
developing applications that use Easylogging++.


%package        doc
Summary:        Documentation and examples for Easylogging++

BuildArch:      noarch
Requires:       easyloggingpp-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description    doc %{common_description}

The easyloggingpp-doc package contains documentation and examples for
developing applications that use Easylogging++.


%prep
%autosetup -n easyloggingpp-%{commit} -p1
# Remove .gitignore and similar files that might accidentally be packaged,
# especially in the samples.
find . -type f \( -name '.git*' -o -name '.travis*' \) -print -delete
find . -depth -type d -name '.vs' -print -execdir rm -rvf '{}' ';'
# Fix CRNL line endings
dos2unix samples/Qt/fast-dictionary/words.txt
find samples/VC++ -type f -execdir dos2unix '{}' '+'


%build
%set_build_flags
%cmake -GNinja -Dtest:BOOL=TRUE
%cmake_build


%install
%cmake_install

install -d '%{buildroot}%{_pkgdocdir}'
cp -rvp *.md doc samples '%{buildroot}%{_pkgdocdir}'
# Symlink headers to the -devel package: use absolute symlinks in the buildroot
# and then use the symlinks utility to convert them into relative ones.
find '%{buildroot}%{_pkgdocdir}/samples' -type f \
    \( -name 'easylogging++.cc' -o -name 'easylogging++.h' \) |
  while read -r fn
  do
    ln -svf "%{buildroot}%{_includedir}/$(basename "${fn}")" "${fn}"
    symlinks -c -o "${fn}"
  done
# Hardlink duplicate shell scripts and such within the examples
hardlink '%{buildroot}%{_pkgdocdir}/samples'
# The following allows us to mark samples/OpenGL/Cube/LICENCE as an additional
# license file under the package documentation directory, without manually
# listing the contents of the samples directory. That’s perhaps a little fussy,
# but it works nicely.
(
  find samples/ -type d -printf '\045doc \045dir \045{_pkgdocdir}/%p\n'
  find samples/ -type f -name 'LICENCE' \
      -printf '\045license \045{_pkgdocdir}/%p\n'
  find samples/ -type f ! -name 'LICENCE' \
      -printf '\045doc \045{_pkgdocdir}/%p\n'
) | tee samples.files


%check
# Test failures related to --logging-flags
# https://github.com/amrayn/easyloggingpp/issues/816
%{_vpath_builddir}/easyloggingpp-unit-tests \
    --gtest_filter=-CommandLineArgsTest.LoggingFlagsArg


%files devel
%license LICENSE
%{_includedir}/easylogging++.h
# This “source” file is treated as a header; see the notes at the top of the
# spec file.
%{_includedir}/easylogging++.cc
%{_datadir}/pkgconfig/easyloggingpp.pc


%files doc -f samples.files
%license LICENSE
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/*.md
%doc %{_pkgdocdir}/doc


%changelog
%autochangelog
