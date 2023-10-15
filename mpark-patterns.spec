%global debug_package %{nil}

Name:           mpark-patterns
Version:        0.3.0
Release:        %autorelease
Summary:        An experimental pattern matching library for C++17

License:        BSL-1.0
URL:            https://github.com/mpark/patterns
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# change installation path for headers
# use system gtest
# disable balance test - requires lots of ram
Patch:          cmake.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  gtest-devel
BuildRequires:  gmock-devel


%description
%{summary}.


%package        devel
Summary:        Header files for %{name}
BuildArch:      noarch
Provides:       %{name}-static = %{version}-%{release}

%description    devel
%{summary}.


%prep
%autosetup -n patterns-%{version} -p1


%build
%cmake -DMPARK_PATTERNS_INCLUDE_TESTS=ON
%cmake_build


%install
%cmake_install


%check
%ctest


%files devel
%license LICENSE.md
%doc README.md
%{_includedir}/mpark/
%{_datadir}/cmake/mpark_patterns/


%changelog
%autochangelog
