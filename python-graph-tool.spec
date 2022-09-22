# Koji has two types of builders:
# 16Gb + 6 cores
# 128Gb + 48 cores
# There's no way to choose either, so we rely on luck
#
# This needs about 15 gigs per thread, otherwise OOMs. So, we calculate the number of threads we can afford to use for make:
# meminfo gives output in kB (1000 bytes)
%global numthreads %(awk '/MemTotal:/ {print int($2/15e6)}' /proc/meminfo)
# But make sure it is > 0
%if 0%{numthreads} == 0
%global numthreads 1
%endif

# If _smp_build_ncpus is not defined (on older rpms)
# assume there's only one
%if 0%{?_smp_build_ncpus} == 0
%global _smp_build_ncpus 1
%endif

# Use the smaller number of threads
%if 0%{numthreads} > 0%{?_smp_build_ncpus}
%global numthreads %{?_smp_build_ncpus}
%endif

%global modname graph-tool
%global pymodname graph_tool

# Builds fail with LTO
%global _lto_cflags %{nil}

%global _description %{expand:
Graph-tool is an efficient Python module for manipulation and statistical
analysis of graphs (a.k.a. networks). Contrary to most other python modules
with similar functionality, the core data structures and algorithms are
implemented in C++, making extensive use of template metaprogramming, based
heavily on the Boost Graph Library. This confers it a level of performance that
is comparable (both in memory usage and computation time) to that of a pure
C/C++ library.

Please refer to https://graph-tool.skewed.de/static/doc/index.html for
documentation.}

Name:           python-%{modname}
Version:        2.43
Release:        %autorelease
Summary:        Efficient network analysis tool written in Python

License:        LGPLv3+
URL:            https://graph-tool.skewed.de/
Source0:        https://downloads.skewed.de/%{modname}/%{modname}-%{version}.tar.bz2
# Remove the compilation flags upstream sets
Patch0:         0001-remove-upstream-compilation-flags.patch

# Need to reduce debugging symbols to make compiling possible on these
# architectures at all. See:
#   https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/GIBNORLNGSUHAMX6PZ7XUPQ2SQUK7AX4/
#
# Works around:
# Fails on armv7hl:
#   virtual memory exhausted
# https://bugzilla.redhat.com/show_bug.cgi?id=1771024
%ifarch armv7hl
%global optflags %(echo %{optflags} | sed 's/-g /-g1 /')
%endif

# Fails on i686, armv7hl
#   ../../../src/pcg-cpp/include/pcg_random.hpp:1247:40: error: call to
#       non-'constexpr' function 'pcg_extras::uint_x4<U, V>
#       pcg_extras::operator-(const pcg_extras::uint_x4<U, V>&, const
#       pcg_extras::uint_x4<U, V>&) [with UInt = unsigned int; UIntX2 = long
#       long unsigned int]'
#    1247 |         (state_type(1U) << table_pow2) - state_type(1U);
#         |         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~
#   In file included from ../../../src/pcg-cpp/include/pcg_extras.hpp:84,
#                    from ../../../src/pcg-cpp/include/pcg_random.hpp:114,
#                    from ../../../src/graph/random.hh:21,
#                    from graph_motifs.hh:26,
#                    from graph_motifs.cc:24:
#   ../../../src/pcg-cpp/include/pcg_uint128.hpp:642:22: note:
#       'pcg_extras::uint_x4<U, V> pcg_extras::operator-(const
#       pcg_extras::uint_x4<U, V>&, const pcg_extras::uint_x4<U, V>&) [with
#       UInt = unsigned int; UIntX2 = long long unsigned int]' declared here
#     642 | uint_x4<UInt,UIntX2> operator-(const uint_x4<UInt,UIntX2>& a,
#         |                      ^~~~~~~~
# issue filed: https://git.skewed.de/count0/graph-tool/issues/617
# https://bugzilla.redhat.com/show_bug.cgi?id=1771023
# https://bugzilla.redhat.com/show_bug.cgi?id=1771024
#
# Takes ~23 hours on x86_64 if we get unlucky and get a 6 core 16gig machine,
#   ~4 hours if we get a 48 core 128gig machine
# Takes ~45 hours on aarch64
ExcludeArch:    %{ix86} armv7hl

BuildRequires:  make
BuildRequires:  git-core
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gawk

%description %_description


%package -n python3-%{modname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  boost-devel
BuildRequires:  boost-python3-devel
BuildRequires:  CGAL-devel
# CGAL is header-only since version 5.4.0, so we must BR the virtual -static
# subpackage for tracking, per Fedora guidelines
BuildRequires:  CGAL-static
BuildRequires:  pkgconfig(cairomm-1.0)
BuildRequires:  expat-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  gtk3-devel
BuildRequires:  python3-cairo-devel
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist scipy}
BuildRequires:  %{py3_dist matplotlib}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  sparsehash-devel
# BR -static package of header-only libraries for tracking per guidelines
BuildRequires:  pcg-cpp-devel
BuildRequires:  pcg-cpp-static

Provides:       graph-tool%{?_isa} = %{version}-%{release}

%description -n python3-%{modname} %_description


%package -n python3-%{modname}-devel
Summary:        %{summary}

Requires:       python3-%{modname}%{?_isa} = %{version}-%{release}
# Since this header-only package is re-exposed as part of the extension API,
# dependent packages should ideally also BuildRequire pcg-cpp-static for
# tracking, per guidelines.
Requires:       pcg-cpp-devel

Provides:       graph-tool-devel%{?_isa} = %{version}-%{release}

%description -n python3-%{modname}-devel %_description


%prep
%autosetup -S git -n %{modname}-%{version}
# Remove shebangs from non-script sources
#
# The pattern of selecting files before modifying them with sed keeps us from
# unnecessarily discarding the original mtimes on unmodified files.
find 'src' -type f -name '*.py' \
    -exec gawk '/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r sed -r -i '1{/^#!/d}'
# Fix shebang(s) in sample script(s)
%py3_shebang_fix doc

# Unbundle pcg-cpp. To avoid having to patch the Makefiles, we use symbolic
# links from the original locations. Note that these are followed when the
# extension API headers are installed, so we need to re-create them afterwards.
rm -vf src/pcg-cpp/include/*
ln -sv \
    '%{_includedir}/pcg_extras.hpp' \
    '%{_includedir}/pcg_random.hpp' \
    '%{_includedir}/pcg_uint128.hpp' \
    'src/pcg-cpp/include/'

# Drop intersphinx mappings, since we can’t download remote inventories and
# can’t easily produce working hyperlinks from inventories in local
# documentation packages.
echo 'intersphinx_mapping.clear()' >> doc/conf.py


%build
./autogen.sh
%configure --with-python-module-path=%{python3_sitearch} --with-boost-libdir=%{_libdir} --enable-debug
echo "Building with %{numthreads} of %{?_smp_build_ncpus} available CPUs"
# Uses the latest value set by -j
%make_build -j%{numthreads}


%install
%make_install

# Remove installed doc sources
rm -rf %{buildroot}/%{_datadir}/doc/%{modname}

# Remove static objects
find %{buildroot} -name '*.la' -print -delete

# Restore symbolic links that were followed in “wheelification”
ln -svf \
    '%{_includedir}/pcg_extras.hpp' \
    '%{_includedir}/pcg_random.hpp' \
    '%{_includedir}/pcg_uint128.hpp' \
    '%{buildroot}%{python3_sitearch}/%{pymodname}/include/pcg-cpp/'


%files -n python3-%{modname}
%license COPYING
%doc README.md ChangeLog AUTHORS
%{python3_sitearch}/%{pymodname}
%exclude %{python3_sitearch}/%{pymodname}/include


%files -n python3-%{modname}-devel
%{python3_sitearch}/%{pymodname}/include
%{_libdir}/pkgconfig/%{modname}-py%{python3_version}.pc


%changelog
%autochangelog
