%global         soversion 3.2
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
BuildArch:      noarch

%description
The Vulkan Memory Allocator (VMA) library provides a simple and easy to
integrate API to help you allocate memory for Vulkan buffer and image storage.

%package devel
Summary:        The Vulkan Memory Allocator development package
Provides:       %{name}-static = %{version}-%{release}

%description devel
The Vulkan Memory Allocator development package.

%package doc
Summary:        The Vulkan Memory Allocator documentation package

%description doc
The Vulkan Memory Allocator documentation package.

%prep
%autosetup -p1
#We don't need this :)
rm -f bin/*.exe
#Delete pre-generated docs (we will regenerate):
rm -r docs/html

%build
%cmake -DVMA_BUILD_DOCUMENTATION=ON
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE.txt
%doc CHANGELOG.md
%{_includedir}/vk_mem_alloc.h
%{_datadir}/cmake/%{name}

%files doc
%doc %{_docdir}/%{name}

%changelog
%autochangelog
