# Generated by rust2rpm 26
# * tests are broken: https://github.com/gtk-rs/gtk-rs-core/issues/64
%bcond_with check
%global debug_package %{nil}

%global crate gobject-sys

Name:           rust-gobject-sys0.18
Version:        0.18.0
Release:        %autorelease
Summary:        FFI bindings to libgobject-2.0

License:        MIT
URL:            https://crates.io/crates/gobject-sys
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
FFI bindings to libgobject-2.0.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gobject-2.0) >= 2.56

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

%package     -n %{name}+v2_58-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gobject-2.0) >= 2.58

%description -n %{name}+v2_58-devel %{_description}

This package contains library source intended for building other packages which
use the "v2_58" feature of the "%{crate}" crate.

%files       -n %{name}+v2_58-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+v2_62-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gobject-2.0) >= 2.62

%description -n %{name}+v2_62-devel %{_description}

This package contains library source intended for building other packages which
use the "v2_62" feature of the "%{crate}" crate.

%files       -n %{name}+v2_62-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+v2_66-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gobject-2.0) >= 2.66

%description -n %{name}+v2_66-devel %{_description}

This package contains library source intended for building other packages which
use the "v2_66" feature of the "%{crate}" crate.

%files       -n %{name}+v2_66-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+v2_68-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gobject-2.0) >= 2.68

%description -n %{name}+v2_68-devel %{_description}

This package contains library source intended for building other packages which
use the "v2_68" feature of the "%{crate}" crate.

%files       -n %{name}+v2_68-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+v2_70-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gobject-2.0) >= 2.70

%description -n %{name}+v2_70-devel %{_description}

This package contains library source intended for building other packages which
use the "v2_70" feature of the "%{crate}" crate.

%files       -n %{name}+v2_70-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+v2_72-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gobject-2.0) >= 2.72

%description -n %{name}+v2_72-devel %{_description}

This package contains library source intended for building other packages which
use the "v2_72" feature of the "%{crate}" crate.

%files       -n %{name}+v2_72-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+v2_74-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gobject-2.0) >= 2.74

%description -n %{name}+v2_74-devel %{_description}

This package contains library source intended for building other packages which
use the "v2_74" feature of the "%{crate}" crate.

%files       -n %{name}+v2_74-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+v2_76-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gobject-2.0) >= 2.76

%description -n %{name}+v2_76-devel %{_description}

This package contains library source intended for building other packages which
use the "v2_76" feature of the "%{crate}" crate.

%files       -n %{name}+v2_76-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+v2_78-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gobject-2.0) >= 2.77

%description -n %{name}+v2_78-devel %{_description}

This package contains library source intended for building other packages which
use the "v2_78" feature of the "%{crate}" crate.

%files       -n %{name}+v2_78-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
echo 'pkgconfig(gobject-2.0) >= 2.56'

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
