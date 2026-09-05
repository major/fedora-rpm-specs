Name:           egl-gbm
Epoch:          2
Version:        1.1.4
Release:        %autorelease
Summary:        Nvidia egl gbm libary
License:        MIT
URL:            https://github.com/NVIDIA/%{name}

Source0:        %url/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  eglexternalplatform-devel
BuildRequires:  libdrm-devel
BuildRequires:  libglvnd-devel
BuildRequires:  mesa-libgbm-devel

%description
The GBM EGL external platform library.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
# Delete unversioned .so
rm %{buildroot}%{_libdir}/libnvidia-egl-gbm.so

%files
%license COPYING
%{_libdir}/libnvidia-egl-gbm.so.1*
%{_datadir}/egl/egl_external_platform.d/15_nvidia_gbm.json

%changelog
%autochangelog
