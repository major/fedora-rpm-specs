%global commit 311eaaaa473d593c30d118799aa19ac4ad53cd65
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20241006

Name: kmscube
Version: 0
Release: 10.%{commitdate}.git%{shortcommit}%{?dist}
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
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-10.20241006.git311eaaa
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 11 2024 Erico Nunes <ernunes@redhat.com> - 0-9.20241006.git311eaaa
- Update snapshot to 20241006.git311eaaa

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-8.20230609.git0be1681
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-7.20230609.git0be1681
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-6.20230609.git0be1681
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-5.20230609.git0be1681
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 09 2023 Erico Nunes <ernunes@redhat.com> - 0-4.20230609.git0be1681
- Update snapshot to 20230609.git0be1681

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-3.20210207.git9f63f35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-2.20210207.git9f63f35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb 04 2022 Erico Nunes <nunes.erico@gmail.com> 0-1.20210207.git9f63f35
- Import from copr/enunes kmscube package
- Adjust to Fedora Packaging Guidelines
