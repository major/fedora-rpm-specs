%global debug_package %{nil}
%global commit ee76e620798612c52fb8dcc32a1058a0a3538930
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global git_date 20260507

Name:           vkroots
Version:        0^%{git_date}git%{shortcommit}
Release:        %autorelease
Summary:        A stupid simple method of making Vulkan layers, at home
License:        LGPL-2.1-or-later AND (Apache-2.0 or MIT)
URL:            https://github.com/Joshua-Ashton/vkroots
BuildArch:      noarch

Source:         %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch0:         https://patch-diff.githubusercontent.com/raw/misyltoad/vkroots/pull/12.patch
Patch1:         vkroots-fix-funcpointer-xml-format.patch

BuildRequires:  meson >= 0.58.0
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  vulkan-headers


%description
vkroots is a framework for writing Vulkan layers that
takes all the complexity/hastle away from you. It's so simple.


%package devel
Summary:        A stupid simple method of making Vulkan layers, at home

%description devel
vkroots is a framework for writing Vulkan layers that
takes all the complexity/hastle away from you. It's so simple.

%prep
%autosetup -p1 -n %{name}-%{commit}

# Autogenerate the header based on the installed Vulkan Headers
cd gen
./make_vkroots -v -x /usr/share/vulkan/registry/vk.xml


%build
%meson
%meson_build


%install
%meson_install


%files devel
%license LICENSE
%doc README.md
%{_includedir}/%{name}.h
%{_datadir}/pkgconfig/%{name}.pc


%changelog
%autochangelog
