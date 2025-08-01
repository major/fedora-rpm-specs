%global commitdate 20250416
%global commithash 3b276e68136eb10825aa7cabd06abb324897f0e8
%global shortcommit %(c=%{commithash}; echo ${c:0:7})

Name:           VK_hdr_layer
Version:        0~git%{commitdate}.%{shortcommit}
Release:        2%{?dist}
Summary:        Vulkan Wayland HDR WSI Layer

License:        MIT
URL:            https://github.com/zamundaaa/VK_hdr_layer
Source:         %{url}/archive/%{commithash}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  meson >= 0.58
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  vulkan-headers
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(vkroots)
BuildRequires:  pkgconfig(wayland-client)

# KWin is the main reference supported compositor
Enhances:       kwin-wayland >= 6.3

%description
Vulkan layer utilizing a small color management/HDR
protocol for experimentation.
The proposed mainline protocol for color management is
wp_color_management.

This implements the following vulkan extensions,
if the protocol is supported by the compositor.

* VK_EXT_swapchain_colorspace
* VK_EXT_hdr_metadata


%prep
%autosetup -n %{name}-%{commithash} -p1


%conf
%meson --libdir=%{_libdir}/%{name}


%build
%meson_build


%install
%meson_install


%files
%license LICENSE
%doc README.md
%{_libdir}/%{name}/libVkLayer_hdr_wsi.so
%{_datadir}/vulkan/implicit_layer.d/VkLayer_hdr_wsi.*.json


%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0~git20250416.3b276e6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Apr 21 2025 Neal Gompa <ngompa@fedoraproject.org> - 0~git20250416.3b276e6-1
- Update to git snapshot with support for finalized color management protocol

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0~git20241018.e173f26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 18 2024 Neal Gompa <ngompa@fedoraproject.org> - 0~git20241018.e173f26-1
- Update to git snapshot
- Install library to private subdirectory

* Sun Sep 08 2024 Neal Gompa <ngompa@fedoraproject.org> - 0~git20240427.e47dc6d-1
- Initial package
