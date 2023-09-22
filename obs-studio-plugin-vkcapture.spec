%global srcname obs-vkcapture

Name:           obs-studio-plugin-vkcapture
Version:        1.4.3
Release:        2%{?dist}
Summary:        OBS plugin for Vulkan/OpenGL game capture

License:        GPL-2.0-or-later and Zlib
URL:            https://github.com/nowrep/obs-vkcapture
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

# elfhacks FTBFS on IBM Z
ExcludeArch:    s390x

BuildRequires:  cmake
BuildRequires:  gcc

BuildRequires:  cmake(libobs)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  libglvnd-devel
BuildRequires:  vulkan-loader-devel

# For directory ownership
Requires:       vulkan-loader%{?_isa}
Requires:       obs-studio%{?_isa}

Enhances:       obs-studio%{?_isa}

# Replace older packages
Obsoletes:      obs-vkcapture < %{version}-%{release}
Provides:       obs-vkcapture = %{version}-%{release}
Provides:       obs-vkcapture%{?_isa} = %{version}-%{release}

%description
%{name}.

%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%cmake
%cmake_build


%install
%cmake_install


%files
%doc README.md
%license LICENSE
# Preload library wrappers
%{_bindir}/obs-gamecapture
%{_bindir}/obs-glcapture
%{_bindir}/obs-vkcapture
# Preload libraries
%{_libdir}/libobs_glcapture.so
%{_libdir}/libVkLayer_obs_vkcapture.so
%{_datadir}/vulkan/implicit_layer.d/obs_vkcapture_%{__isa_bits}.json
# OBS plugin
%{_libdir}/obs-plugins/linux-vkcapture.so
# OBS plugin data
%{_datadir}/obs/obs-plugins/linux-vkcapture/


%changelog
* Wed Sep 20 2023 Neal Gompa <ngompa@fedoraproject.org> - 1.4.3-2
- Fix build for 32-bit arches and exclude s390x

* Mon Sep 18 2023 Neal Gompa <ngompa@fedoraproject.org> - 1.4.3-1
- Update to 1.4.3

* Sun Sep 17 2023 Neal Gompa <ngompa@fedoraproject.org> - 1.4.2-1
- Initial package
