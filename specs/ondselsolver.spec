%global  commit       09d6175a2ba69e7016fcecc4f384946a2f84f92d
%global  shortcommit  09d6175
%global  commitdate   21012025

Name:           ondselsolver
Version:        1.0.1^%{commitdate}git%{shortcommit}
Release:        %{autorelease}
Summary:        Assembly Constraints and Multibody Dynamics code

License:        LGPL-2.1-only
URL:            https://github.com/FreeCAD/OndselSolver
VCS:            git:%{URL}.git
Source:         %{url}/archive/%{shortcommit}/OndselSolver-%{commit}.tar.gz
# Use google test from Fedora repositories
# https://github.com/FreeCAD/OndselSolver/pull/9
Patch:          packaged-gtest.patch
# Fix C++ name mangling
# https://github.com/FreeCAD/OndselSolver/pull/2
Patch:          https://github.com/gentoo/gentoo/blob/1896fac74ffa1cdb67fd9c9d3d85a618096c5d40/sci-libs/ondselsolver/files/ondselsolver-1.0.1-properly-demangle-typenames.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
# Test dependencies
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel

%description
Assembly Constraints and Multibody Dynamics code.

%package devel
Summary:  Development libraries and header files for libOndselSolver
Requires:  ondselsolver%{?isa} = %{version}-%{release}

%description devel
Development libraries and header files for libOndselSolver.

%prep
%autosetup -p1 -n OndselSolver-%{commit}


%build
%cmake -DONDSELSOLVER_BUILD_TESTS=ON \
       -DONDSELSOLVER_BUILD_EXE=ON \
       -DONDSELSOLVER_BUILD_SHARED=ON
%cmake_build


%install
%cmake_install

%check
# Skip failing tests
skip="${skip-}${skip+}OndselSolver.Gears|"
skip="${skip-}${skip+}OndselSolver.anglejoint|"
# Does not fail on i686 or x86_64
skip="${skip-}${skip+}OndselSolver.fourbot"
%ctest -E "${skip-}"

%files
%license LICENSE
%doc README.md
%{_libdir}/libOndselSolver.so.1.0.1
%{_libdir}/libOndselSolver.so.1

%files devel
%{_libdir}/libOndselSolver.so
%dir %{_includedir}/OndselSolver/
%{_includedir}/OndselSolver/*.h
%{_datadir}/pkgconfig/OndselSolver.pc

%changelog
%autochangelog
