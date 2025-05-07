%global _description %{expand:
gsl-lite is an implementation of the C++ Core Guidelines Support Library
originally based on Microsoft GSL.
}

%bcond tests 1

# Header only, so no debuginfo is generated
%global debug_package %{nil}

Name:           gsl-lite
Version:        0.43.0
Release:        %autorelease
Summary:        Header-only version of ISO C++ Guidelines Support Library (GSL)

# The entire source is (SPDX) MIT, except the following files, which are
# BSL-1.0 but do not contribute to the licenses of the binary RPMs because they
# belong to the maintainer scripts or test suite.
#   - script/create-cov-rpt.py
#   - script/create-vcpkg.py
#   - script/upload-conan.py
#   - test/lest_cpp03.hpp
License:        MIT
SourceLicense:  %{license} AND BSL-1.0
URL:            https://github.com/gsl-lite/gsl-lite
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description %_description


%package        devel
Summary:        Development files for %{name}
Provides:       %{name}%{?_isa} = %{version}-%{release}
Provides:       %{name}-static = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%build
%cmake -DGSL_LITE_OPT_BUILD_EXAMPLES=ON \
    -DGSL_LITE_OPT_BUILD_TESTS=%{?with_tests:ON}%{?!with_tests:OFF}
%cmake_build


%install
%cmake_install


%check
%if %{with tests}
%ctest
%endif


%files devel
%license LICENSE
%doc README.md CHANGES.txt
%{_includedir}/%{name}/
# Directory is co-owned with gsl-devel and guidelines-support-library-devel:
%dir %{_includedir}/gsl/
%{_includedir}/gsl/%{name}.hpp

%{_libdir}/cmake/%{name}/


%changelog
%autochangelog
