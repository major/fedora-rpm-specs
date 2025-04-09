# There are no ELF objects in this package, so turn off debuginfo generation.
%global debug_package %{nil}

Name:           rx-ranges
Version:        2.0.0
Release:        %autorelease
Summary:        Simpler ranges for C++17

License:        MIT
URL:            https://github.com/simonask/rx-ranges
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
## Post-release bug fixes
# Make s_month_names constexpr
Patch:          %{url}/commit/27e5191.patch
# Remove default-constructibility requirement from ChainRange
Patch:          %{url}/commit/a9ab841.patch
# Replace exception by assert
Patch:          %{url}/commit/dc74040.patch
# Help the compiler with empty_range() deduction guide
Patch:          %{url}/commit/36b0614.patch
# Include <limits> for std::numeric_limits
Patch:          %{url}/pull/48.patch
# Include <cmath> for std::sqrt
Patch:          %{url}/pull/49.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++

# Test dependencies
BuildRequires:  boost-devel
BuildRequires:  cmake(doctest)

%global desc %{expand:
This is a ranges-like library for C++17 that provides zero-overhead list
comprehensions with a pipe-like syntax.

Standard containers can be filtered, transformed, passed through various
algorithms, optimizing to loops that would not be more efficient if written by
hand.

The goal is to provide the tools to write more readable loops, where the intent
of the programmer is clearly communicated to the reader.  Mentally simulating
loops is a common but error-prone part of reading other people's code, and
indeed your own code from 3 months ago.

The library makes heavy use of modern C++17 features, so a compliant C++17
compiler is required.

Features:
- Arbitrary composability.
- Constexpr-friendly.
- No unnecessary temporary heap allocations (`foo | sort() | to_vector()` only
  allocates into the resulting container).
- Heap allocation minimization: `reserve()` is used on resulting containers,
  when possible.
- Open-ended generators (non-terminating, infinite ranges).
- Re-entrancy: A non-rvalue range can be used multiple times in a function.
- Compatible with standard containers (anything that supports `std::begin()`
  and `std::end()`).
- Compatible with standard algorithms (implicit conversion to iterator-like
  objects).
- Simple extensibility with custom range adapters. Just implement the
  `InputRange` faux-concept.
- Non-intrusive `operator|`. The ranges `foo | bar | baz` can be expressed as
  `baz(bar(foo))`, if using `operator|` would introduce ambiguous overloads.
- No dependencies beyond the standard library.
- Integration with foreign codebases (override hooks for `std::optional`,
  `std::remove_cvref_t`, assertions, etc.). Can easily be used as a submodule.
- Compiler support for all major compilers (GCC, Clang, MSVC).
- Zero-overhead, compared to manually written loops in optimized builds.
- Header-only, and single-header.

Other than usability concerns, these are the main differences from C++20
ranges:
- Bidirectional ranges.  Ranges can only be consumed linearly in the forward
  direction.
- Random-access ranges.  Ranges can only be consumed linearly in the forward
  direction.
- Internally using iterators.  The internal iteration objects are modeled with
  an "enumerator" concept instead (objects that provide `next()`, `get()`,
  `at_end()`, etc.), which simplifies custom extensions.  Implicit,
  zero-overhead conversion to iterators is provided for compatibility with
  standard algorithms and the range-based for loop syntax.
- Direct access to the data of underlying contiguous ranges (`data()` etc.).}

%description
%desc

%package devel
Summary:        Simpler ranges for C++17
BuildArch:      noarch
Provides:       %{name}-static = %{version}-%{release}

%description devel
%desc

%prep
%autosetup -p1

%conf
%cmake

%build
%cmake_build

%install
#%%cmake_install doesn't do anything
mkdir -p %{buildroot}%{_includedir}
cp -a include/rx %{buildroot}%{_includedir}

%check
#%%ctest doesn't do anything
cd test
CXXFLAGS='%{build_cxxflags} -I../include -DDOCTEST_CONFIG_IMPLEMENT_WITH_MAIN'
g++ $CXXFLAGS %{build_ldflags} -o test_ranges test_ranges.cpp
./test_ranges
g++ $CXXFLAGS %{build_ldflags} -o calendar calendar.cpp
./calendar
cd -

%files devel
%doc AUTHORS.md CHANGELOG.md README.md
%license LICENSE
%{_includedir}/rx/

%changelog
%autochangelog
