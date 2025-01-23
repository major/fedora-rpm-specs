# Re-generate the header from the template, perhaps with different maximum
# numbers of args and/or types? Packaging guidelines don’t *require* us to do
# this, and there is probably no benefit in this case, but it is nice to
# demonstrate how it can be done if needed.
%bcond regenerate 0
%dnl %global max_types 16
%dnl %global max_types 5

%bcond tests 1

Name:           variant-lite
Version:        2.0.0
Release:        %autorelease
Summary:        Represent a type-safe union

License:        BSL-1.0
URL:            https://github.com/martinmoene/variant-lite
Source:         %{url}/archive/v%{version}/variant-lite-%{version}.tar.gz

# Downstream patch: disable C++17 tests since they fail to compile on GCC 14
# https://github.com/martinmoene/variant-lite/issues/50
Patch:          0001-Downstream-patch-disable-C-17-tests-since-they-fail-.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake

%if %{with regenerate}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist jinja2}
%endif

%if %{with tests}
# Required for testing; bundled upstream, unbundled in %%prep.
# Header-only library (-static required by policy)
BuildRequires:  lest-devel lest-static
%endif

# No compiled binaries are installed, so this would be empty.
%global debug_package %{nil}

%global common_description %{expand:
A single-file header-only library to represent a type-safe union.}

%description %{common_description}


%package devel
Summary:        Development files for %{name}

# Header-only library
Provides:       %{name}-static = %{version}-%{release}

%description devel %{common_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n variant-lite-%{version} -p1

# Unbundle lest
rm -rvf test/lest
ln -s /usr/include/lest test/lest


%if %{with regenerate}
%generate_buildrequires
%pyproject_buildrequires -N
%endif


%conf
%cmake %{?!with_tests:-DVARIANT_LITE_OPT_BUILD_TESTS:BOOL=OFF}


%build
%if %{with regenerate}
%{python3} script/generate_header.py \
    %{?max_types:--max-types %{max_types}} \
    %{?max_args:--max-args %{max_args}} \
    --verbose
%endif

%cmake_build


%install
%cmake_install


%check
%if %{with tests}
%ctest
%endif


%files devel
%license LICENSE.txt
# We don’t package CHANGES.txt because it was never updated after “version
# 0.0.0-alpha 2016-10-23.” If we did, we would need to fix its encoding,
# https://github.com/martinmoene/variant-lite/pull/51.
%doc README.md
%doc example/

# This directory is co-owned with packages for similar libraries, e.g.
# optional-lite, by the same author.
%dir %{_includedir}/nonstd/
%{_includedir}/nonstd/variant.hpp

%{_libdir}/cmake/variant-lite/


%changelog
%autochangelog
