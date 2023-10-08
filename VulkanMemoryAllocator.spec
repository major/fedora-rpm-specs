%global         soversion 3.0
%global         patchversion 1

Summary:        Easy to integrate Vulkan memory allocation library
Name:           VulkanMemoryAllocator
Version:        %{soversion}.%{patchversion}
Release:        %autorelease
License:        MIT
URL:            https://gpuopen.com/vulkan-memory-allocator/
Source0:        https://github.com/GPUOpen-LibrariesAndSDKs/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  vulkan-headers
BuildRequires:  vulkan-loader-devel

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%description
The Vulkan Memory Allocator (VMA) library provides a simple and easy to
integrate API to help you allocate memory for Vulkan buffer and image storage.

%package devel
Summary:        The Vulkan Memory Allocator development package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The Vulkan Memory Allocator development package.

%package doc
Summary:        The Vulkan Memory Allocator documentation package
BuildArch:      noarch

%description doc
The Vulkan Memory Allocator documentation package.

%prep
%autosetup -p1
#Fix newer gcc issue (fixed upstream)
sed -i '/#include <cstdint>/a #include <cstdio>' include/vk_mem_alloc.h
#Fix install location (fixed upstream)
sed -i 's|"lib"|"%{_libdir}"|' src/CMakeLists.txt
#We don't need this :)
rm -f bin/*.exe
#Upstream distributes this as a static lib, so soname is not set by upstream:
echo "set_target_properties(%{name} PROPERTIES VERSION %{version} SOVERSION %{soversion})" \
    >> CMakeLists.txt
#Delete pre-generated docs (we will regenerate):
rm -r docs/html

%build
%cmake -DBUILD_DOCUMENTATION=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE.txt
%doc CHANGELOG.md
%{_libdir}/lib%{name}.so.%{soversion}{,.*}

%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/vk_mem_alloc.h

%files doc
%doc docs/html

%changelog
%autochangelog
