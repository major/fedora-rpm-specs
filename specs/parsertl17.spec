Name:           parsertl17
Summary:        The Modular Parser Generator
# Upstream switched away from calendar-based versioning, and the new version
# scheme sorts older than the calendar-based one, so we cannot avoid an Epoch.
Epoch:          1
Version:        1.0.0
Release:        %autorelease

License:        BSL-1.0
URL:            https://github.com/BenHanson/parsertl17
Source:         %{url}/archive/%{version}/parsertl17-%{version}.tar.gz

# No compiled binaries are installed, so this would be empty.
%global debug_package %{nil}

# This choice is somewhat arbitrary, but it’s safest to combine versions
# released around the same time. Note that this includes an epoch.
%global min_lexertl17 1:1.1.3

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  dos2unix

# Header-only library:
# (Technically, dependent packages should have this BuildRequires too.)
BuildRequires:  lexertl17-static >= %{min_lexertl17}

# No compiled binaries are installed, so this would be empty.
%global debug_package %{nil}

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package devel
Summary:        %{summary}

# Header-only library:
Provides:       parsertl17-static = %{epoch}:%{version}-%{release}
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Conflicts/#_compat_package_conflicts
Conflicts:      parsertl14-devel

Requires:       lexertl17-devel >= %{min_lexertl17}

%description devel %{common_description}


%prep
%autosetup -n parsertl17-%{version}

# Fix line terminations (particularly for files that may be installed)
find . -type f -exec file '{}' '+' |
  grep -E '\bCRLF\b' |
  cut -d ':' -f 1 |
  xargs -r dos2unix --keepdate


%conf
# While the top-level CMakeLists.txt supports a BUILD_TESTING option, there are
# not yet any tests that can be built or run via CMake.
%cmake


%build
%cmake_build


%install
%cmake_install


%check
%ctest
# There are not yet any tests that can be built or run via CMake. This is a
# compile-only “smoke test.”
%set_build_flags
${CXX-g++} -I"${PWD}/include" ${CPPFLAGS} ${CXXFLAGS} -o include_test ${LDFLAGS} \
    tests/include_test/*.cpp


%files devel
%license include/parsertl/licence_1_0.txt
%doc README.md

%{_includedir}/parsertl/

%{_libdir}/cmake/parsertl/


%changelog
%autochangelog
