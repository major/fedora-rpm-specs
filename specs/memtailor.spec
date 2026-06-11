Name:           memtailor
Version:        1.4
Release:        %autorelease
Summary:        C++ library of special-purpose memory allocators

License:        BSD-3-Clause
URL:            https://github.com/Macaulay2/memtailor
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildSystem:    cmake
BuildOption(conf): -DBUILD_SHARED_LIBS:BOOL=ON
BuildOption(conf): -DBUILD_TESTING:BOOL=ON

BuildRequires:  cmake(GTest)
BuildRequires:  gcc-c++

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

# Fix the installation directory
sed -i 's,lib,${LIB_INSTALL_DIR},' CMakeLists.txt

# Add an soname
sed -e '/Threads/iset_target_properties(memtailor PROPERTIES VERSION 0.0.4 SOVERSION 0)' \
    -i src/CMakeLists.txt

%install -a
# This file is not installed by cmake
cp -p src/memtailor.h %{buildroot}%{_includedir}

# Install the pkgconfig file for backwards compatibility
# Fix the URL in the pkgconfig file
mkdir -p %{buildroot}%{_libdir}/pkgconfig
sed -e 's,@prefix@,%{_prefix},' \
    -e 's,@exec_prefix@,%{_prefix},' \
    -e 's,@libdir@,%{_libdir},' \
    -e 's,@includedir@,%{_includedir},' \
    -e 's,@PACKAGE_VERSION@,%{version},' \
    -e 's,broune,Macaulay2,' \
    build/autotools/memtailor.pc.in \
    > %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

# We install these files in a different place
rm -fr %{buildroot}%{_prefix}/licenses

%check
%{_vpath_builddir}/src/memtailor-unit-tests

%files
%doc README.md
%license license.txt
%{_libdir}/lib%{name}.so.0{,.*}

%files devel
%{_includedir}/%{name}/
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
