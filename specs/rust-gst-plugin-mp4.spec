# Generated by rust2rpm 27
# * missing dev-dependency: gstreamer-check ^0.23
%bcond check 0

%global crate gst-plugin-mp4

Name:           rust-gst-plugin-mp4
Version:        0.13.6
Release:        %autorelease
Summary:        GStreamer Rust MP4 Plugin

License:        MPL-2.0
URL:            https://crates.io/crates/gst-plugin-mp4
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  cargo-c >= 0.9.21

%global _description %{expand:
GStreamer Rust MP4 Plugin.}

%description %{_description}

%package     -n gstreamer1-plugin-mp4
Summary:        %{summary}
# Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# MPL-2.0
# Unlicense OR MIT
License:        (Apache-2.0 OR MIT) AND MIT AND MPL-2.0 AND (Unlicense OR MIT)
# LICENSE.dependencies contains a full license breakdown

%description -n gstreamer1-plugin-mp4 %{_description}

%files       -n gstreamer1-plugin-mp4
%license LICENSE
%license LICENSE.dependencies
%{_libdir}/gstreamer-1.0/libgstmp4.so

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+capi-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+capi-devel %{_description}

This package contains library source intended for building other packages which
use the "capi" feature of the "%{crate}" crate.

%files       -n %{name}+capi-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+doc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+doc-devel %{_description}

This package contains library source intended for building other packages which
use the "doc" feature of the "%{crate}" crate.

%files       -n %{name}+doc-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+static-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+static-devel %{_description}

This package contains library source intended for building other packages which
use the "static" feature of the "%{crate}" crate.

%files       -n %{name}+static-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%cargo_cbuild

%install
%cargo_install
%cargo_cinstall
# remove statically linked library
rm -v %{buildroot}/%{_libdir}/gstreamer-1.0/libgstmp4.a
# remove unnecessary pkgconfig file
rm -v %{buildroot}/%{_libdir}/pkgconfig/gstmp4.pc

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
