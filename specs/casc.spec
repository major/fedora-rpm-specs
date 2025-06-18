Name:           casc
Summary:        Colored Abstract Simplicial Complex (CASC) Library
Version:        1.0.5
Release:        %autorelease

URL:            https://github.com/ctlee/casc
License:        LGPL-2.1-or-later
Source:         %{url}/archive/v%{version}/casc-%{version}.tar.gz

# This is a backport of commit 4c094080b7eaccf345dab8d78dde4d75ef51c516 from the
# development branch to the 1.0.5 release.
#
# Support using an external GoogleTest library (#13)
#
# Adds the EXTERNAL_GTEST CMake option, which defaults to OFF, preserving
# the current behavior.
#
# While this is not recommended by the GoogleTest authors, it is useful
# for Linux distribution packaging.
#
# https://github.com/ctlee/casc/pull/13
# https://github.com/ctlee/casc/commit/4c094080b7eaccf345dab8d78dde4d75ef51c516
Patch:          casc-1.0.5-external-gtest.patch
# This backports commit 52f105bf7407e90c8bef10cce2a41b7efcb21679, “fix:
# initialize level_count memory”, from the development branch to release 1.0.5.
#
# https://github.com/ctlee/casc/pull/12
Patch:          casc-1.0.5-levelcount-memory.patch
# This is a backport of commit 0ea03e39961312986b80eac2c9d259fc525e590e, “fix:
# Stop InnerVisitor from reading past end of array”, from the development
# branch to release 1.0.5.
#
# It fixes upstream issue #14, “Tests fail when libstdc++ assertions are
# enabled” (https://github.com/ctlee/casc/issues/14).
Patch:          casc-1.0.5-innervisitor.patch
# Update Free Software Foundation postal addresses
#
# Ref.: https://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html#SEC4
#
# Note that we must not patch the license file for legal reasons
# (https://fedoraproject.org/wiki/Common_Rpmlint_issues#incorrect-fsf-address),
# but also that:
#
#  • The license file (here, COPYING.md) already has the correct address
#  • Upstream has accepted the PR corresponding to this patch
#
# https://github.com/ctlee/casc/pull/16
Patch:          0001-Update-Free-Software-Foundation-postal-addresses.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  cmake
# The make backend would work just as well; Ninja is our choice
BuildRequires:  ninja-build

# For tests:
BuildRequires:  cmake(gtest)

# No compiled binaries are installed, so this would be empty.  However,
# packaging guidelines for header-only libraries insist that the base package
# must not be noarch:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_use_noarch_only_in_subpackages
%global debug_package %{nil}

%global common_description %{expand:
CASC is a modern and header-only C++ library which provides a data structure to
represent arbitrary dimension abstract simplicial complexes with user-defined
classes stored directly on the simplices at each dimension. This is achieved by
taking advantage of the combinatorial nature of simplicial complexes and new
C++ code features such as: variadic templates and automatic function return
type deduction. Essentially CASC stores the full topology of the complex
according to a Hasse diagram. The representation of the topology is decoupled
from interactions of user data through the use of metatemplate programming.}

%description %{common_description}


%package devel
Summary:        %{summary}

BuildArch:  noarch

# Header-only library
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_packaging_header_only_libraries
Provides:       casc-static = %{version}-%{release}

%description devel %{common_description}


%prep
%autosetup -p1


%conf
%cmake -DBUILD_CASCTESTS:BOOL=ON -DEXTERNAL_GTEST:BOOL=ON -GNinja


%build
%cmake_build


%install
%cmake_install


%check
%ctest


%files devel
%license COPYING.md
%{_includedir}/casc/


%changelog
%autochangelog
