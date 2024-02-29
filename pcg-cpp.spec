# The last tagged release was 0.98.1 in 2015, but there have been many
# essential bug fixes since then, so we package a snapshot. See
# https://github.com/imneme/pcg-cpp/issues/73.
%global commit 428802d1a5634f96bcd0705fab379ff0113bcf13
%global snapdate 20220408

Name:           pcg-cpp
Summary:        PCG Random Number Generation, C++ Edition
Version:        0.98.1^%{snapdate}git%{sub %{commit} 1 7}
Release:        %autorelease

# The entire package is (MIT OR Apache-2.0), except that any data files are
# CC0-1.0. As far as we can tell, the binary RPMs do not contain any content
# derived from “data” files.
#
# See: LICENSE.spdx
License:        MIT OR Apache-2.0
URL:            https://github.com/imneme/pcg-cpp
Source:         %{url}/archive/%{commit}/pcg-cpp-%{commit}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  make

# No compiled binaries are installed, so this would be empty.
%global debug_package %{nil}

%global common_description %{expand:
This code provides an implementation of the PCG family of random number
generators, which are fast, statistically excellent, and offer a number of
useful features.

Full details can be found at the PCG-Random website
(http://www.pcg-random.org/). This version of the code provides many family
members – if you just want one simple generator, you may prefer the minimal C
version of the library.

There are two kinds of generator, normal generators and extended generators.
Extended generators provide k dimensional equidistribution and can perform
party tricks, but generally speaking most people only need the normal
generators.

There are two ways to access the generators, using a convenience typedef or by
using the underlying templates directly (similar to C++11’s std::mt19937
typedef vs its std::mersenne_twister_engine template). For most users, the
convenience typedef is what you want, and probably you’re fine with pcg32 for
32-bit numbers. If you want 64-bit numbers, either use pcg64 (or, if you’re on
a 32-bit system, making 64 bits from two calls to pcg32_k2 may be faster).}

%description %{common_description}


%package devel
Summary:        %{summary}

BuildArch:      noarch

# Header-only library:
Provides:       pcg-cpp-static = %{version}-%{release}

%description devel %{common_description}


%package doc
Summary:        Documentation and examples for pcg-cpp

BuildArch:      noarch

%description doc
%{summary}.


%prep
%autosetup -n pcg-cpp-%{commit}
find . -name '.gitignore' -print -delete
# Make a copy of the sample/ directory that will not contain compiled
# executables, since we would like to install the sources as documentation.
cp -rp sample examples


%build
%make_build


%install
%make_install PREFIX=%{_prefix}


%check
%make_build test


%files devel
%license LICENSE-APACHE.txt LICENSE-MIT.txt LICENSE.spdx
%{_includedir}/pcg_extras.hpp
%{_includedir}/pcg_random.hpp
%{_includedir}/pcg_uint128.hpp


%files doc
%license LICENSE-APACHE.txt LICENSE-MIT.txt LICENSE.spdx
%doc CONTRIBUTING.md
%doc README.md
%doc examples/


%changelog
%autochangelog
