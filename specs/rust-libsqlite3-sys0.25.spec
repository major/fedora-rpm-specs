# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate libsqlite3-sys

Name:           rust-libsqlite3-sys0.25
Version:        0.25.2
Release:        %autorelease
Summary:        Native bindings to the libsqlite3 library

License:        MIT
URL:            https://crates.io/crates/libsqlite3-sys
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * bump bindgen from 0.60 to 0.63
# * remove features for building vendored sqlite3 and sqlcipher sources
# * drop Windows- and WASM-specific features
# * exclude files that are only useful for upstream development
Patch:          libsqlite3-sys-fix-metadata.diff
# * unconditionally enable building with bindgen and pkg-config
Patch:          0001-unconditionally-enable-building-with-bindgen-and-pkg.patch

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  pkgconfig(sqlcipher)
BuildRequires:  pkgconfig(sqlite3) >= 3.7.16

%global _description %{expand:
Native bindings to the libsqlite3 library.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(sqlite3) >= 3.7.16

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+buildtime_bindgen-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+buildtime_bindgen-devel %{_description}

This package contains library source intended for building other packages which
use the "buildtime_bindgen" feature of the "%{crate}" crate.

%files       -n %{name}+buildtime_bindgen-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+min_sqlite_version_3_6_23-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+min_sqlite_version_3_6_23-devel %{_description}

This package contains library source intended for building other packages which
use the "min_sqlite_version_3_6_23" feature of the "%{crate}" crate.

%files       -n %{name}+min_sqlite_version_3_6_23-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+min_sqlite_version_3_6_8-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+min_sqlite_version_3_6_8-devel %{_description}

This package contains library source intended for building other packages which
use the "min_sqlite_version_3_6_8" feature of the "%{crate}" crate.

%files       -n %{name}+min_sqlite_version_3_6_8-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+min_sqlite_version_3_7_16-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+min_sqlite_version_3_7_16-devel %{_description}

This package contains library source intended for building other packages which
use the "min_sqlite_version_3_7_16" feature of the "%{crate}" crate.

%files       -n %{name}+min_sqlite_version_3_7_16-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+min_sqlite_version_3_7_7-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+min_sqlite_version_3_7_7-devel %{_description}

This package contains library source intended for building other packages which
use the "min_sqlite_version_3_7_7" feature of the "%{crate}" crate.

%files       -n %{name}+min_sqlite_version_3_7_7-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+preupdate_hook-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+preupdate_hook-devel %{_description}

This package contains library source intended for building other packages which
use the "preupdate_hook" feature of the "%{crate}" crate.

%files       -n %{name}+preupdate_hook-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+session-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+session-devel %{_description}

This package contains library source intended for building other packages which
use the "session" feature of the "%{crate}" crate.

%files       -n %{name}+session-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+sqlcipher-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(sqlcipher)

%description -n %{name}+sqlcipher-devel %{_description}

This package contains library source intended for building other packages which
use the "sqlcipher" feature of the "%{crate}" crate.

%files       -n %{name}+sqlcipher-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unlock_notify-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unlock_notify-devel %{_description}

This package contains library source intended for building other packages which
use the "unlock_notify" feature of the "%{crate}" crate.

%files       -n %{name}+unlock_notify-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+with-asan-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+with-asan-devel %{_description}

This package contains library source intended for building other packages which
use the "with-asan" feature of the "%{crate}" crate.

%files       -n %{name}+with-asan-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep
# * remove bundled copies of sqlite and sqlcipher
rm -vr sqlite3/ sqlcipher/

%generate_buildrequires
%cargo_generate_buildrequires

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