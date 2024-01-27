%{?mingw_package_header}

%global pkgname vulkan-utility-libraries
%global srcname Vulkan-Utility-Libraries

%define baseversion %(echo %{version} | awk -F'.' '{print $1"."$2"."$3}')

Name:          mingw-%{pkgname}
Version:       1.3.268.0
Release:       4%{?dist}
Summary:       MinGW Windows %{pkgname}

License:       Apache-2.0
BuildArch:     noarch
URL:           https://github.com/KhronosGroup/%{srcname}
Source0:       https://github.com/KhronosGroup/%{srcname}/archive/vulkan-sdk-%{version}/%{srcname}-%{version}.tar.gz

BuildRequires: make
BuildRequires: cmake
BuildRequires: glslang

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-vulkan-headers >= %{baseversion}

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-vulkan-headers >= %{baseversion}


%description
MinGW Windows %{pkgname}


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname}

%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname}.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname}

%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname}.


%prep
%autosetup -p1 -n %{srcname}-vulkan-sdk-%{version}


%build
MINGW32_CMAKE_ARGS="-DVULKAN_HEADERS_INSTALL_DIR=%{mingw32_includedir}" \
MINGW64_CMAKE_ARGS="-DVULKAN_HEADERS_INSTALL_DIR=%{mingw64_includedir}" \
%mingw_cmake -DGLSLANG_INSTALL_DIR=%{_prefix}
%mingw_make_build


%install
%mingw_make_install


%files -n mingw32-%{pkgname}
%license LICENSES/Apache-2.0.txt
%{mingw32_includedir}/vulkan/
%{mingw32_libdir}/libVulkanLayerSettings.a
%{mingw32_libdir}/cmake/VulkanUtilityLibraries/


%files -n mingw64-%{pkgname}
%license LICENSES/Apache-2.0.txt
%{mingw64_includedir}/vulkan/
%{mingw64_libdir}/libVulkanLayerSettings.a
%{mingw64_libdir}/cmake/VulkanUtilityLibraries/


%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.268.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.268.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov 30 2023 Sandro Mani <manisandro@gmail.com> - 1.3.268.0-2
- Mark LICENSES/Apache-2.0.txt as %%license

* Wed Nov 29 2023 Sandro Mani <manisandro@gmail.com> - 1.3.268.0-1
- Initial package
