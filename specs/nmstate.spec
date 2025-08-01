%define srcname nmstate
%define libname libnmstate

Name:           nmstate
Version:        2.2.48
Release:        %autorelease
Summary:        Declarative network manager API
License:        Apache-2.0 AND LGPL-2.1-or-later
URL:            https://github.com/%{srcname}/%{srcname}
Source0:        %{url}/releases/download/v%{version}/%{srcname}-%{version}.tar.gz
Source1:        %{url}/releases/download/v%{version}/%{srcname}-%{version}.tar.gz.asc
Source2:        https://nmstate.io/nmstate.gpg
Source3:        %{url}/releases/download/v%{version}/%{srcname}-vendor-%{version}.tar.xz
# Force nmstate-libs upgrade along with nmstate rpm when installed
# https://issues.redhat.com/browse/RHEL-52890
Requires:       (nmstate-libs%{?_isa} = %{version}-%{release} if nmstate-libs)
BuildRequires:  python3-devel
BuildRequires:  gnupg2
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
%if 0%{?rhel}
BuildRequires:  rust-toolset
%else
BuildRequires:  rust-packaging
BuildRequires:  (crate(clap/cargo) >= 3.1 with crate(clap/cargo) < 4.0)
BuildRequires:  (crate(clap/default) >= 3.1 with crate(clap/default) < 4.0)
BuildRequires:  (crate(chrono/default) >= 0.4 with crate(chrono/default) < 0.5)
BuildRequires:  (crate(env_logger/default) >= 0.11 with crate(env_logger/default) < 0.12)
BuildRequires:  (crate(libc/default) >= 0.2 with crate(libc/default) < 0.3)
BuildRequires:  (crate(log/default) >= 0.4 with crate(log/default) < 0.5)
BuildRequires:  (crate(nispor/default) >= 1.2.24 with crate(nispor/default) < 2.0)
BuildRequires:  (crate(serde/default) >= 1.0 with crate(serde/default) < 2.0)
BuildRequires:  (crate(serde/derive) >= 1.0 with crate(serde/derive) < 2.0)
BuildRequires:  (crate(serde_json/default) >= 1.0 with crate(serde_json/default) < 2.0)
BuildRequires:  (crate(serde_yaml/default) >= 0.9 with crate(serde_yaml/default) < 1.0)
BuildRequires:  (crate(uuid/v4) >= 1.1 with crate(uuid/v4) < 2.0)
BuildRequires:  (crate(uuid/v5) >= 1.1 with crate(uuid/v5) < 2.0)
BuildRequires:  (crate(zbus/default) >= 5.1 with crate(zbus/default) < 6.0)
BuildRequires:  (crate(zvariant/default) >= 5.1 with crate(zvariant/default) < 6.0)
BuildRequires:  (crate(nix/default) >= 0.30 with crate(nix/default) < 0.31)
BuildRequires:  (crate(toml/default) >= 0.8 with crate(toml/default) < 0.9)
BuildRequires:  (crate(tokio/default) >= 1.3 with crate(tokio/default) < 2.0)
BuildRequires:  (crate(tokio/net) >= 1.3 with crate(tokio/net) < 2.0)
BuildRequires:  (crate(tokio/rt) >= 1.3 with crate(tokio/rt) < 2.0)
BuildRequires:  (crate(tokio/signal) >= 1.3 with crate(tokio/signal) < 2.0)
BuildRequires:  (crate(once_cell/default) >= 1.12 with crate(once_cell/default) < 2.0)
%endif

%generate_buildrequires
pushd rust/src/python >/dev/null
%pyproject_buildrequires
popd >/dev/null

%description
Nmstate is a library with an accompanying command line tool that manages host
networking settings in a declarative manner and aimed to satisfy enterprise
needs to manage host networking through a northbound declarative API and multi
provider support on the southbound.


%package libs
Summary:        C binding of nmstate
# Use Recommends for NetworkManager because only access to NM DBus is required,
# but NM could be running on a different host
Recommends:     NetworkManager
# Avoid automatically generated profiles
Recommends:     NetworkManager-config-server
License:        Apache-2.0

%description libs
C binding of nmstate.

%package devel
Summary:        Development files for nmstate
Group:          Development/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
License:        Apache-2.0

%description devel
Development files of nmstate C binding.

%package static
Summary:        Static development files for nmstate
Group:          Development/Libraries
License:        Apache-2.0
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description static
Static C library bindings for nmstate.

%package -n python3-%{libname}
Summary:        nmstate Python 3 API library
# Use Recommends for NetworkManager because only access to NM DBus is required,
# but NM could be running on a different host
Recommends:     NetworkManager
# Avoid automatically generated profiles
Recommends:     NetworkManager-config-server
Recommends:     (nmstate-plugin-ovsdb if openvswitch)
# Use Suggests for NetworkManager-ovs and NetworkManager-team since it is only
# required for OVS and team support
Suggests:       NetworkManager-ovs
Suggests:       NetworkManager-team
Provides:       nmstate-plugin-ovsdb = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:      nmstate-plugin-ovsdb < 2.0-1
License:        Apache-2.0

%description -n python3-%{libname}
This package contains the Python 3 library for Nmstate.

%if ! 0%{?rhel}
%package -n rust-%{name}-devel
Summary:        Rust crate of nmstate
BuildArch:      noarch
License:        Apache-2.0

%description -n rust-%{name}-devel
This package contains library source intended for building other packages
which use "%{name}" crate.

%package -n rust-%{name}+default-devel
Summary:        Rust crate of nmstate with default feature
BuildArch:      noarch
License:        Apache-2.0

%description -n rust-%{name}+default-devel
This package contains library source intended for building other packages
which use "%{name}" crate with default feature.

%package -n rust-%{name}+gen_conf-devel
Summary:        Rust crate of nmstate with default feature
BuildArch:      noarch
License:        Apache-2.0

%description -n rust-%{name}+gen_conf-devel
This package contains library source intended for building other packages
which use "%{name}" crate with gen_conf feature.

%package -n rust-%{name}+query_apply-devel
Summary:        Rust crate of nmstate with query_apply feature
BuildArch:      noarch
License:        Apache-2.0
# https://bugzilla.redhat.com/show_bug.cgi?id=2161128
Requires:  (crate(nispor/default) >= 1.2.17 with crate(nispor/default) < 2.0)
Requires:  (crate(nix/default) >= 0.26 with crate(nix/default) < 0.27)
Requires:  (crate(zbus/default) >= 5.1 with crate(zbus/default) < 6.0)

%description -n rust-%{name}+query_apply-devel
This package contains library source intended for building other packages
which use "%{name}" crate with query_apply feature.

%package -n rust-%{name}+gen_revert-devel
Summary:        Rust crate of nmstate with gen_revert feature
BuildArch:      noarch
License:        Apache-2.0

%description -n rust-%{name}+gen_revert-devel
This package contains library source intended for building other packages
which use "%{name}" crate with gen_revert feature.
%endif

%prep
gpg2 --import --import-options import-export,import-minimal \
    %{SOURCE2} > ./gpgkey-mantainers.gpg
gpgv2 --keyring ./gpgkey-mantainers.gpg %{SOURCE1} %{SOURCE0}

%autosetup -n %{name}-%{version_no_tilde} -p1 %{?rhel:-a3}

pushd rust
%if 0%{?rhel}
mv ../vendor ./
%cargo_prep -v vendor
%else
%cargo_prep
%endif
popd

%build
pushd rust
%cargo_build
%cargo_license_summary
%{cargo_license} > ../LICENSE.dependencies
%if 0%{?rhel}
%cargo_vendor_manifest
%endif
popd

pushd rust/src/python
%pyproject_wheel
popd

%install
env SKIP_PYTHON_INSTALL=1 \
    PREFIX=%{_prefix} \
    LIBDIR=%{_libdir} \
    SYSCONFDIR=%{_sysconfdir} \
    %make_install

pushd rust/src/python
%pyproject_install
popd

%if ! 0%{?rhel}
pushd rust/src/lib
# Fedora cargo2rpm has problem when working with worksace dependency
#   https://pagure.io/fedora-rust/cargo2rpm/issue/13
# we use `cargo package` to generate the expanded Cargo.toml which
# is also the one used in crates.io
cargo package --frozen --no-verify --target-dir %{_tmppath}
tar xf %{_tmppath}/package/nmstate-%{version}.crate \
  nmstate-%{version}/Cargo.toml
mv nmstate-%{version}/Cargo.toml ./Cargo.toml
# Remove worksapce Cargo.toml
rm ../../Cargo.toml
%cargo_install
popd
%endif

%files
%doc README.md
%license LICENSE.dependencies
%if 0%{?rhel}
%license rust/cargo-vendor.txt
%endif
%doc examples/
%{_mandir}/man8/nmstatectl.8*
%{_mandir}/man8/nmstate-autoconf.8*
%{_mandir}/man8/nmstate.service.8*
%{_bindir}/nmstatectl
%{_bindir}/nmstate-autoconf
%{_unitdir}/nmstate.service
%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/%{name}/README

%files libs
%{_libdir}/libnmstate.so.*

%files devel
%{_libdir}/libnmstate.so
%{_includedir}/nmstate.h
%{_libdir}/pkgconfig/nmstate.pc

%files -n python3-%{libname}
%license LICENSE
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{srcname}-*.dist-info/

%files static
%{_libdir}/libnmstate.a

%if ! 0%{?rhel}
%files -n rust-%{name}-devel
%license LICENSE
%{cargo_registry}/%{name}-%{version}/

%files -n rust-%{name}+default-devel
%ghost %{cargo_registry}/%{name}-%{version}/Cargo.toml

%files -n rust-%{name}+gen_conf-devel
%ghost %{cargo_registry}/%{name}-%{version}/Cargo.toml

%files -n rust-%{name}+query_apply-devel
%ghost %{cargo_registry}/%{name}-%{version}/Cargo.toml

%files -n rust-%{name}+gen_revert-devel
%ghost %{cargo_registry}/%{name}-%{version}/Cargo.toml
%endif

%changelog
%autochangelog
