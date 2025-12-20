Name:           memtailor
Version:        1.1
Release:        %autorelease
Summary:        C++ library of special-purpose memory allocators

License:        BSD-3-Clause
URL:            https://github.com/Macaulay2/memtailor
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(gtest)

%description
Memtailor is a C++ library of special purpose memory allocators.  It currently
offers an arena allocator and a memory pool.

The main motivation to use a memtailor allocator is better and more
predictable performance than you get with new/delete.  Sometimes a memtailor
allocator can also be more convenient due to the ability to free many
allocations at one time.

The Memtailor memory pool is useful if you need to do many allocations of a
fixed size.  For example a memory pool is well suited to allocate the nodes in
a linked list.

You can think of the Memtailor arena allocator as being similar to stack
allocation.  Both kinds of allocation are very fast and require you to
allocate/deallocate memory in last-in-first-out order.  Arena allocation has
the further benefits that it stays within the C++ standard, it will not cause
a stack overflow, you can have multiple arena allocators at the same time and
allocation is not tied to a function invocation.

%package devel
Summary:        Development files for memtailor
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for developing applications that use memtailor.

%prep
%autosetup

%conf
# Fix the URL in the pkgconfig file
sed -i 's/broune/Macaulay2/' build/autotools/memtailor.pc.in

# Upstream doesn't generate the configure script
autoreconf -fi

%build
export GTEST_PATH=%{_prefix}
export GTEST_VERSION=$(gtest-config --version)
%configure --disable-static --enable-shared --with-gtest=yes

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC=.g..|& -Wl,--as-needed|' \
    -i libtool

%make_build

%install
%make_install

%check
LD_LIBRARY_PATH=$PWD/.libs make check

%files
%doc README.md
%license license.txt
%{_libdir}/lib%{name}.so.0*

%files devel
%{_includedir}/%{name}/
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
