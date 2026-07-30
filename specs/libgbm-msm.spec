%global prj_name gbm-msm-backend

Name:		libgbm-msm
Version:	1.2.6
Release:	%autorelease
Summary:	Generic Buffer Management API

License:	GPL-2.0-only AND MIT AND BSD-3-Clause
URL:		https://github.com/qualcomm-linux/gbm-msm-backend
Source:		%{url}/archive/v%{version}/%{prj_name}-%{version}.tar.gz

Patch0:		meson-build.patch

ExclusiveArch:	%{arm64}

BuildRequires:	dpkg-dev
BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:	pkgconfig(gbm)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(libxml-2.0)

%description
Generic buffer manager backend library provides hardware-accelerated buffer
allocation and management for Qualcomm Adreno GPUs on MSM platforms. 

It implements the GBM backend ABI to integrate seamlessly with Mesa's 
GBM loader, enabling efficient graphics buffer operations for display and
rendering pipelines.

%prep
%autosetup -p1 -n %{prj_name}-%{version}

%conf
%meson

%build
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%dir %{_libdir}/gbm
%{_libdir}/gbm/msm_gbm.so
%{_libdir}/gbm/default_fmt_alignment.xml

%changelog
