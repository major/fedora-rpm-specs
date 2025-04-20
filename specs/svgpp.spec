Name: svgpp
Summary: SVG handling library for C++

# This is a header-only package. Any debuginfo we might generate along the way
# will pertain only to test executables.
%global debug_package %{nil}

# svgpp is subject to the Boost Software License.
# It bundles a custom fork of Boost, also subject to the BSL.
#
# The source archive contains some additional bundled libraries:
# - third_party/agg - MIT-like license
# - third_party/googletest - BSD-3-Clause
# - third_party/rapidxml_ns - BSL-1.0 OR MIT
# - third_party/stb - MIT OR Unlicense
# These are used only for building the test suite.
License: BSL-1.0

Version: 1.3.1
Release: 2%{?dist}

URL: https://svgpp.org
Source0: https://github.com/svgpp/svgpp/archive/v%{version}/%{name}-%{version}.tar.gz

# Move the bundled, modified boost from include/exboost to include/svgpp/exboost.
Patch0: svgpp-exboost-path.patch

%global with_tests 1

%if 0%{?with_tests}
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: tree
BuildRequires: boost-devel
%endif

%description
SVG++ is a header-only library for handling SVG files
that can be used with any XML parser.

# -- devel

%package devel
Summary: %{summary}
Provides: %{name}-static = %{version}-%{release}
Requires: boost-devel
BuildArch: noarch

%description devel
SVG++ is a header-only library for handling SVG files
that can be used with any XML parser.

# -- subpackages end


%prep
%autosetup -p1
mv ./include/exboost ./include/svgpp/exboost


%build
# Nothing to do here


%install
install -m 755 -d %{buildroot}%{_includedir}
cp -a include/svgpp %{buildroot}%{_includedir}/%{name}


%if 0%{?with_tests}
%check
pushd src/test/
%cmake
%cmake_build
./%{__cmake_builddir}/ParserGTest
%endif


%files devel
%doc README.md
%license LICENSE_1_0.txt
%{_includedir}/%{name}


%changelog
* Wed Mar 19 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.3.1-2
- Move bundled Boost fork from include/exboost/ to include/svgpp/exboost/

* Wed Feb 05 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.3.1-1
- Initial packagig
