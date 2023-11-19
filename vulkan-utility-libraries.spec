%global debug_package %{nil}

Name:           vulkan-utility-libraries
Version:        1.3.268.0
Release:        %autorelease
Summary:        Vulkan utility libraries

License:        Apache-2.0
URL:            https://github.com/KhronosGroup/Vulkan-Utility-Libraries
Source0:        %url/archive/vulkan-sdk-%{version}.tar.gz#/Vulkan-Utility-Libraries-sdk-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake3
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  vulkan-headers

%description
%{summary}

%package        devel
Summary:        Development files for %{name}
Requires:       vulkan-headers

%description    devel
%{summary}

%prep
%autosetup -p1 -n Vulkan-Utility-Libraries-vulkan-sdk-%{version}

%build
%cmake3 -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
        -DBUILD_TESTS:BOOL=OFF \
        -DVUL_WERROR:BOOL=OFF \
        -DUPDATE_DEPS:BOOL=OFF
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE.md
%doc README.md
%{_includedir}/vulkan/
%{_libdir}/cmake/VulkanUtilityLibraries/*.cmake
%{_libdir}/libVulkanLayerSettings.a

%changelog
%autochangelog
