%global commit 9f63f359fab1b5d8e862508e4e51c9dfe339ccb0
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20210207

Name: kmscube
Version: 0
Release: 2.%{commitdate}.git%{shortcommit}%{?dist}
Summary: Example KMS/GBM/EGL application
License: MIT
URL: https://gitlab.freedesktop.org/mesa/kmscube/
Source0: https://gitlab.freedesktop.org/mesa/kmscube/-/archive/%{commit}/kmscube-%{commit}.tar.gz

BuildRequires: gcc gstreamer1-devel gstreamer1-plugins-base-devel
BuildRequires: libdrm-devel libpng-devel mesa-libEGL-devel
BuildRequires: mesa-libgbm-devel mesa-libGLES-devel meson ninja-build

%description
kmscube is a little demonstration program for how to drive bare metal
graphics without a compositor like X11, wayland or similar, using
DRM/KMS (kernel mode setting), GBM (graphics buffer manager) and EGL
for rendering content using OpenGL or OpenGL ES.

%prep
%setup -q -n %{name}-%{commit}

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%{_bindir}/kmscube
%{_bindir}/texturator

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-2.20210207.git9f63f35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb 04 2022 Erico Nunes <nunes.erico@gmail.com> 0-1.20210207.git9f63f35
- Import from copr/enunes kmscube package
- Adjust to Fedora Packaging Guidelines
