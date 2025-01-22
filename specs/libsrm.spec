%global basever 0.6.3
%global origrel 1
%global somajor 0

Name:           libsrm
Version:        %{basever}%{?origrel:_%{origrel}}
Release:        2%{?dist}
Summary:        Library for building DRM/KMS applications

License:        MIT
URL:            https://cuarzosoftware.github.io/SRM/
Source0:        https://github.com/CuarzoSoftware/SRM/archive/v%{basever}%{?origrel:-%{origrel}}/SRM-%{basever}%{?origrel:-%{origrel}}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libdisplay-info)
# Examples
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libseat)

%description
SRM is a C library that simplifies the development of Linux DRM/KMS
applications.

With SRM, you can focus on the OpenGL ES 2.0 logic of your application.
For each available display, you can start a rendering thread that triggers
common events like initializeGL(), paintGL(), resizeGL(), pageFlipped()
and uninitializeGL().

SRM allows you to use multiple GPUs simultaneously and automatically finds
the most efficient configuration. It also offers functions for creating OpenGL
textures, which are automatically shared among GPUs.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        examples
Summary:        Example applications using %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    examples
The %{name}-examples package contains example applications using
%{name}.


%prep
%autosetup -n SRM-%{basever}%{?origrel:-%{origrel}}


%build
pushd src
%meson
%meson_build
popd

%install
pushd src
%meson_install
popd

%files
%license LICENSE
%doc BUILD CHANGES VERSION
%{_libdir}/libSRM.so.%{somajor}

%files examples
%{_bindir}/srm-all-connectors
%{_bindir}/srm-basic
%{_bindir}/srm-display-info
%{_bindir}/srm-multi-session

%files devel
%doc README.md doxygen
%{_includedir}/SRM/
%{_libdir}/libSRM.so
%{_libdir}/pkgconfig/SRM.pc


%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3_1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 13 2024 Neal Gompa <ngompa@fedoraproject.org> - 0.6.3_1-1
- Initial package
