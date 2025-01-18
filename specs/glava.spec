Name:           glava
Version:        1.6.3
Release:        18%{?dist}
Summary:        OpenGL audio spectrum visualizer

# See license note in README.md
License:        GPL-3.0-only and MIT
URL:            https://github.com/jarcode-foss/glava
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Fedora-specific
Patch0001:      0001-Make-build-reproducible-and-verbose.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  gcc
BuildRequires:  glfw-devel >= 3.1
BuildRequires:  make
BuildRequires:  mesa-libGL-devel
BuildRequires:  libX11-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXext-devel
BuildRequires:  libXrender-devel
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  python3dist(glad)
BuildRequires:  xorg-x11-proto-devel

%description
GLava is an OpenGL audio spectrum visualizer primarily used for desktop windows
or backgrounds. Multiple visualization styles are provided and new ones may be
written in GLSL. Development is active, and reporting issues is encouraged.

See https://github.com/jarcode-foss/glava/wiki for more documentation.


%prep
%autosetup -p1

# Remove bundled glad files.
rm glad.?


%build
%set_build_flags
make PYTHON=%{python3} glad
%make_build GLAVA_VERSION='\"%{version}\"' ENABLE_GLFW=1 SHADERDIR=%{_datadir}/glava/


%install
%make_install SHADERDIR=%{_datadir}/glava


%files
%doc README.md
%license LICENSE LICENSE_ORIGINAL
%{_bindir}/glava
%{_datadir}/glava


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Apr 09 2023 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.6.3-13
- Switch to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 19 2022 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.6.3-11
- Drop support for i686

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 06 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.6.3-8
- Update URLs

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.6.3-2
- Add xrandr dependency to fix FTBFS (#1733432)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 14 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.6.3-1
- Initial package of glava
