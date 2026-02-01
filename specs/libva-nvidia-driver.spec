%global commit0 c2860cc621ae1ef515c003d43315c63a41529ff4
%global date 20250419
#global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global upstream_name nvidia-vaapi-driver

Name:           libva-nvidia-driver
Version:        0.0.15%{?shortcommit0:^%{date}git%{shortcommit0}}
Release:        %autorelease
Summary:        A VA-API implemention using NVIDIA's NVDEC

License:        MIT
URL:            https://github.com/elFarto/nvidia-vaapi-driver

%if "%{?shortcommit0}"
Source0:        %{url}/archive/%{commit0}/%{upstream_name}-%{commit0}.tar.gz#/%{upstream_name}-%{shortcommit0}.tar.gz
%else
Source0:        %{url}/archive/v%{version}/%{upstream_name}-%{version}.tar.gz
%endif

BuildRequires:  gcc
BuildRequires:  meson >= 0.58.0
BuildRequires:  pkgconfig(ffnvcodec) >= 11.1.5.1
BuildRequires:  pkgconfig(gstreamer-codecparsers-1.0)
BuildRequires:  pkgconfig(libdrm) >= 2.4.60
BuildRequires:  pkgconfig(libva) >= 1.8.0

# Alternative name that better describes the API involved
Provides:       nvdec-vaapi-driver = %{version}-%{release}

# Only one NVIDIA VA-API shim on a system at a time
Conflicts:      libva-vdpau-driver

# NVIDIA driver architectures
ExclusiveArch:  x86_64 aarch64 %{ix86}

%description
This is an VA-API implementation that uses NVDEC as a backend. This
implementation is specifically designed to be used by Firefox for accelerated
decode of web content, and may not operate correctly in other applications.

%prep
%if "%{?shortcommit0}"
%autosetup -p1 -n %{upstream_name}-%{commit0}
%else
%autosetup -p1 -n %{upstream_name}-%{version}
%endif

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc README.md
%license COPYING
%{_libdir}/dri/nvidia_drv_video.so

%changelog
%autochangelog
