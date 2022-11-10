%global __python %{__python3}
Name:           vulkan-headers
Version:        1.3.231.1
Release:        %autorelease
Summary:        Vulkan Header files and API registry

License:        ASL 2.0
URL:            https://github.com/KhronosGroup/Vulkan-Headers
Source0:        %url/archive/sdk-%{version}.tar.gz#/Vulkan-Headers-sdk-%{version}.tar.gz

BuildRequires:  cmake3
BuildArch:      noarch       

%description
Vulkan Header files and API registry

%prep
%autosetup -n Vulkan-Headers-sdk-%{version}


%build
%cmake3 -DCMAKE_INSTALL_LIBDIR=%{_libdir}
%cmake_build


%install
%cmake_install


%files
%license LICENSE.txt
%doc README.md
%{_includedir}/vulkan/
%{_includedir}/vk_video/
%dir %{_datadir}/vulkan/
%{_datadir}/vulkan/registry/


%changelog
%autochangelog
