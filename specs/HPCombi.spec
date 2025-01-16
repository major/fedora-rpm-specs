# There are no ELF objects in this package, so turn off debuginfo generation.
%global debug_package %{nil}

# Install documentation with the devel package documentation
%global _docdir_fmt %{name}-devel

%global giturl  https://github.com/libsemigroups/HPCombi

Name:           HPCombi
Version:        1.0.1
Release:        %autorelease
Summary:        High Performance Combinatorics in C++ using vector instructions

License:        GPL-3.0-or-later
URL:            https://libsemigroups.github.io/HPCombi/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz
# Unbundle simde
Patch:          %{name}-unbundle-simde.patch

# Limited support for architectures.  Recheck this on each release.
ExclusiveArch:  x86_64 %{arm64}

BuildRequires:  cmake
BuildRequires:  cmake(Catch2)
BuildRequires:  doxygen-latex
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libsparsehash)
BuildRequires:  simde-static

%global _desc %{expand:
HPCombi is a C++17 header-only library using the SSE and AVX instruction
sets, and some equivalents, for very fast manipulation of combinatorial
objects such as transformations, permutations, and boolean matrices of
small size.  The goal of this project is to implement various new
algorithms and benchmark them on various compiler and architectures.

HPCombi was initially designed using the SSE and AVX instruction sets,
and did not work on machines without these instructions (such as ARM).
From v1.0.0 HPCombi supports processors with other instruction sets
also, via SIMD Everywhere.  It might be the case that the greatest
performance gains are achieved on processors supporting the SSE and AVX
instruction sets, but the HPCombi benchmarks indicate that there are
also still significant gains on other processors too.}

%description %_desc

%package        devel
Summary:        High Performance Combinatorics in C++ using vector instructions
BuildArch:      noarch
Requires:       simde-static
Provides:       %{name}-static = %{version}-%{release}

%description    devel %_desc

%package        doc
# Doxygen adds files with licenses other than GPL-3.0-or-later.
# GPL-1.0-or-later: *.css, *.png, *.svg
# MIT: cookie.js, dynsections.js, jquery.js, menu.js, menudata.js,
#      search/search.js
License:        GPL-3.0-or-later AND GPL-1.0-or-later AND MIT
Summary:        API documentation for HPCombi
BuildArch:      noarch
Provides:       bundled(js-jquery)

%description    doc
API documentation for HPCombi.

%prep
%autosetup -p1

%conf
# Ensure we can't use the bundled simde
rm -fr third_party

# Install the pkgconfig file in the noarch directory
sed -i 's/lib/share/' CMakeLists.txt

%build
%cmake
%cmake_build

%install
%cmake_install

# We install license and documentation separately
rm -fr %{buildroot}%{_datadir}/hpcombi

fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# Swizzle simde includes
for f in %{buildroot}%{_includedir}/hpcombi/{epu8,perm16}.hpp; do
  sed -i.orig 's,"\(simde.*\)",<\1>,' $f
  fixtimestamp $f
done

# Swizzle hpcombi includes
for f in %{buildroot}%{_includedir}/hpcombi/*.hpp; do
  sed -i.orig 's,\(#include\) "\(.*\)",\1 <hpcombi/\2>,' $f
  fixtimestamp $f
done

# There are currently no tests.  Uncomment this when there are.
#%%check
#%%ctest

%files devel
%doc README.md
%license LICENSE
%{_includedir}/hpcombi/
%{_datadir}/pkgconfig/hpcombi.pc

%files doc
%doc %{_vpath_builddir}/doc/html

%changelog
%autochangelog
