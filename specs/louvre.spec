%global basever 2.3.2
%global origrel 1
%global somajor 2

Name:           louvre
Version:        %{basever}%{?origrel:_%{origrel}}
Release:        1%{?dist}
Summary:        C++ library for building Wayland compositors

License:        MIT
URL:            https://cuarzosoftware.github.io/Louvre/
Source0:        https://github.com/CuarzoSoftware/Louvre/archive/v%{basever}%{?origrel:-%{origrel}}/Louvre-%{basever}%{?origrel:-%{origrel}}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(SRM)
BuildRequires:  freeimage-devel
# Examples
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
# TODO: suggest using icu-uc pkgconfig upstream
BuildRequires:  libicu-devel

%description
Louvre is a high-performance C++ library designed for building
Wayland compositors with a strong emphasis on ease of development.

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
%autosetup -n Louvre-%{basever}%{?origrel:-%{origrel}}


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
%{_libdir}/libLouvre.so.%{somajor}
%{_libdir}/Louvre/

%files examples
%{_bindir}/louvre-default
%{_bindir}/louvre-views
%{_bindir}/louvre-weston-clone
%{_datadir}/Louvre/

%files devel
%doc README.md doxygen
%{_includedir}/Louvre/
%{_libdir}/libLouvre.so
%{_libdir}/pkgconfig/Louvre.pc

%changelog
* Sat Jul 13 2024 Neal Gompa <ngompa@fedoraproject.org> - 2.3.2_1-1
- Initial package

