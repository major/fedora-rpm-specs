%global tag 0.7-3
Version:        %(echo %{tag} | sed 's/-/./')

Name:           foonathan-memory
Release:        %autorelease
Summary:        STL compatible C++ memory allocator library
License:        Zlib
URL:            https://github.com/foonathan/memory
Source0:        %{url}/archive/v%{tag}/%{name}-%{tag}.tar.gz

# Fix install location of CMake config files and header files
# Add FOONATHAN_MEMORY_USE_SYSTEM_DOCTEST option to use system doctest package
# Add soversion to shared library
# Resolve the tool is not included in CMake exported target
Patch0:         foonathan-memory-fix-cmake.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  cmake(doctest)

%description
STL compatible C++ memory allocator library using a new RawAllocator concept
that is similar to an Allocator but easier to use and write.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%package        tools
Summary:        Tools about %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tools
This package contains tools about %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains the documentation for %{name}.

%prep
%autosetup -p1 -n memory-%{tag}

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
    -DFOONATHAN_MEMORY_USE_SYSTEM_DOCTEST=ON \
    -DFOONATHAN_MEMORY_BUILD_TESTS=ON \

%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_docdir}/%{name}/
cp -r example/ %{buildroot}%{_docdir}/%{name}/

rm -rf %{buildroot}%{_datadir}/foonathan_memory/

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_libdir}/libfoonathan_memory.so.0*

%files devel
%{_includedir}/foonathan/
%{_libdir}/cmake/foonathan_memory/
%{_libdir}/libfoonathan_memory.so

%files tools
%{_bindir}/nodesize_dbg

%files doc
%license LICENSE
%{_docdir}/%{name}/

%changelog
%autochangelog
