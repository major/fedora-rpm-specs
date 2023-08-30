# Architecture compatibility macro shims
%{!?x86_64: %global x86_64 x86_64}
%{!?arm64: %global arm64 aarch64}

Name:           libva-nvidia-driver
Version:        0.0.10
Release:        %autorelease
Summary:        A VA-API implemention using NVIDIA's NVDEC

License:        MIT
URL:            https://github.com/elFarto/nvidia-vaapi-driver
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(ffnvcodec) >= 11.1.5.1
BuildRequires:  pkgconfig(gstreamer-va-1.0)

# Replace the rpmfusion package
Provides:       nvidia-vaapi-driver = %{version}-%{release}
Obsoletes:      nvidia-vaapi-driver < 0.0.10-3
# Alternative name that better describes the API involved
Provides:       nvdec-vaapi-driver = %{version}-%{release}

# Only one NVIDIA VA-API shim on a system at a time
Conflicts:      libva-vdpau-driver

# NVIDIA driver architectures
ExclusiveArch:  %{x86_64} %{ix86} %{arm64} ppc64le

%description
This is an VA-API implementation that uses NVDEC as a backend. This
implementation is specifically designed to be used by Firefox for accelerated
decode of web content, and may not operate correctly in other applications.

%prep
%autosetup -n nvidia-vaapi-driver-%{version}

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
