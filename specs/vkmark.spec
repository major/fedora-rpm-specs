# vkamrk dynamicly loads modules that reference static functions in the main binary
%undefine _strict_symbol_defs_build

%global codate 20250123
%global commit0 2bf2ca7f1623db7ad7840a4dd626444d11830815
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Some tests fail on s390x
# https://bugzilla.redhat.com/show_bug.cgi?id=1475561
ExcludeArch:    s390x

Name:           vkmark
Version:        2025.01
Release:        1.%{codate}git%{shortcommit0}%{?dist}
Summary:        Vulkan benchmarking suite

License:        LGPL-2.1-or-later
URL:            https://github.com/vkmark/vkmark
Source0:        https://github.com/vkmark/vkmark/archive/%{commit0}.tar.gz#/%{name}-%{version}-%{shortcommit0}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  meson

BuildRequires:  vulkan-loader-devel
BuildRequires:  glm-devel
BuildRequires:  assimp-devel

BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  libdrm-devel
BuildRequires:  mesa-libgbm-devel


%description
vkmark is an extensible Vulkan benchmarking suite with targeted,
configurable scenes.

%prep
%autosetup -p1 -n %{name}-%{commit0}


%build
%meson
%meson_build


%install
%meson_install


%check
%meson_test


%files
%license COPYING-LGPL2.1
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*


%autochangelog
