# This needs about 15 gigs per thread, otherwise OOMs.
%constrain_build -m 15360

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

Name:           python-graph-tool
Version:        2.88
Release:        %autorelease
Summary:        Efficient network analysis tool written in Python

# The entire source is LGPL-3.0-or-later, except:
#   - BSL-1.0: src/boost-workaround/
#              src/graph/graphml.cpp
#              src/graph/read_graphviz_new.cpp
#   - LGPL-3.0-or-later AND BSD-3-Clause: src/graph_tool/collection/small.py
# Additionally, the following libraries are header-only and are therefore
# treated as static libraries; their licenses do contribute to that of the
# binary RPMs:
#   - CGAL is: LGPL-3.0-or-later AND GPL-3.0-or-later AND BSL-1.0 AND MIT
#     (and possibly a few tiny bits of other things – this package could use a
#     good license audit – but it is a sprawling package, and the preceding
#     expression is slightly better than the one it currently carries)
#   - pcg-cpp is: MIT OR Apache-2.0
# Additionally, the following are under other licenses but do not contribute to
# the licenses of the binary RPMs:
#   - FSFULLR: aclocal.m4
#   - FSFUL (or perhaps FSFUL AND LGPL-3.0-or-later): configure
#   - GPL-2.0-or-later: build-aux/compile
#                       build-aux/depcomp
#                       build-aux/ltmain.sh
#                       build-aux/py-compile
#                       m4/ax_boost_python.m4
#   - GPL-3.0-or-later: build-aux/config.guess
#                       build-aux/config.sub
#                       m4/ax_create_pkgconfig_info.m4
#                       m4/ax_openmp.m4
#                       m4/ax_python_devel.m4
#   - X11: build-aux/install-sh
#   - FSFAP: m4/ax_boost_base.m4
#            m4/ax_boost_context.m4
#            m4/ax_boost_coroutine.m4
#            m4/ax_boost_graph.m4
#            m4/ax_boost_iostreams.m4
#            m4/ax_boost_regex.m4
#            m4/ax_boost_thread.m4
#            m4/ax_cxx_compile_stdcxx.m4,
#            m4/ax_cxx_compile_stdcxx_17.m4
#            m4/ax_lib_cgal_core.m4
#            m4/ax_python_module.m4
License:        %{shrink:
                LGPL-3.0-or-later AND
                BSL-1.0 AND
                BSD-3-Clause AND
                GPL-3.0-or-later AND
                MIT AND
                (MIT OR Apache-2.0)
                }
URL:            https://graph-tool.skewed.de/
Source:         https://downloads.skewed.de/graph-tool/graph-tool-%{version}.tar.bz2

# Note that upstream sets the optimization flag -O3. Per
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_compiler_flags,
# we should normally patch this out in order to fully respect the system
# default compiler flags. However, upstream writes in
# https://git.skewed.de/count0/graph-tool/-/blob/release-2.86/configure.ac#L67-L69:
#
#   Enforce -O3. It makes a substantial difference, e.g. 12x speed improvement
#   over -O2 in benchmarks.
#
# It’s not obvious how we should validate upstream’s claim with downstream
# benchmarking; nevertheless, we consider it adequate justification for
# allowing -O3.

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  make
BuildRequires:  git-core
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gawk

%description %_description


%package -n python3-graph-tool
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  boost-devel
BuildRequires:  boost-python3-devel
BuildRequires:  CGAL-devel
# CGAL is header-only since version 5.4.0, so we must BR the virtual -static
# subpackage for tracking, per Fedora guidelines
BuildRequires:  CGAL-static
BuildRequires:  pkgconfig(cairomm-1.16)
BuildRequires:  expat-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  gtk3-devel
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist scipy}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist pycairo}
BuildRequires:  python3-cairo-devel
BuildRequires:  %{py3_dist matplotlib}
BuildRequires:  sparsehash-devel
# BR -static package of header-only libraries for tracking per guidelines
BuildRequires:  pcg-cpp-devel
BuildRequires:  pcg-cpp-static

Recommends:     %{py3_dist pycairo}
Recommends:     %{py3_dist matplotlib}

Provides:       graph-tool%{?_isa} = %{version}-%{release}

%description -n python3-graph-tool %_description


%package -n python3-graph-tool-devel
Summary:        %{summary}

# This package does not contain compiled binaries, so its license does not
# include the licenses of header-only “static” dependencies. The headers of
# pcg-cpp are “re-exposed” in this package, but it uses symbolic links rather
# than installing additional copies. Additionally, no .py source files are
# included.
License:        LGPL-3.0-or-later AND BSL-1.0

Requires:       python3-graph-tool%{?_isa} = %{version}-%{release}
# Since this header-only package is re-exposed as part of the extension API,
# dependent packages should ideally also BuildRequire pcg-cpp-static for
# tracking, per guidelines.
Requires:       pcg-cpp-devel

Provides:       graph-tool-devel%{?_isa} = %{version}-%{release}

%description -n python3-graph-tool-devel %_description


%prep
%autosetup -S git -n graph-tool-%{version}
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
# We get a few thousand warnings like:
#   warning: 'always_inline' attribute does not apply to types [-Wattributes]
# and since each is very verbose, with a lot of context, the build log explodes
# to many gigabytes, which ends up failing the build. Disable this class of
# warnings as a pragmatic matter.
export CXXFLAGS="${CXXFLAGS-} -Wno-attributes"
%configure \
    --with-python-module-path=%{python3_sitearch} \
    --with-boost-libdir=%{_libdir} \
    --enable-debug
%make_build

# Provide Python metadata
%global graph_tool_distinfo graph_tool-%{version}.dist-info
mkdir %{graph_tool_distinfo}
cat > %{graph_tool_distinfo}/METADATA << EOF
Metadata-Version: 2.1
Name: graph-tool
Version: %{version}
Requires-dist: numpy
Requires-dist: scipy
EOF
echo rpm > %{graph_tool_distinfo}/INSTALLER


%install
%make_install

# Remove installed doc sources
rm -rf %{buildroot}/%{_datadir}/doc/graph-tool

# Remove static objects
find %{buildroot} -name '*.la' -print -delete

# Restore symbolic links that were followed in “wheelification”
ln -svf \
    '%{_includedir}/pcg_extras.hpp' \
    '%{_includedir}/pcg_random.hpp' \
    '%{_includedir}/pcg_uint128.hpp' \
    '%{buildroot}%{python3_sitearch}/graph_tool/include/pcg-cpp/'

# Install Python metadata
cp -a %{graph_tool_distinfo} %{buildroot}%{python3_sitearch}


%files -n python3-graph-tool
%license COPYING src/boost-workaround/LICENSE_1_0.txt
%doc README.md ChangeLog AUTHORS
%{python3_sitearch}/graph_tool/
%{python3_sitearch}/%{graph_tool_distinfo}/
%exclude %{python3_sitearch}/graph_tool/include/


%files -n python3-graph-tool-devel
%{python3_sitearch}/graph_tool/include/
%{_libdir}/pkgconfig/graph-tool-py%{python3_version}.pc


%changelog
%autochangelog
