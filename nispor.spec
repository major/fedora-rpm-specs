# The check need root privilege
%bcond_with check

Name:           nispor
Version:        1.2.8
Release:        1%{?dist}
Summary:        Unified interface for Linux network state querying
License:        ASL 2.0
URL:            https://github.com/nispor/nispor
Source:         https://github.com/nispor/nispor/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         use-clap-3.patch
ExclusiveArch:  %{rust_arches}
BuildRequires:  make
BuildRequires:  pkg-config
BuildRequires:  python3-devel
BuildRequires:  python-setuptools
BuildRequires:  rust-packaging
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  patchelf
BuildRequires:  (crate(clap/cargo) >= 3.1.0 with crate(clap/cargo) < 4.0)
BuildRequires:  (crate(clap/default) >= 3.1.0 with crate(clap/default) < 4.0)
BuildRequires:  (crate(env_logger/default) >= 0.9 with crate(env_logger/default) < 0.10)
BuildRequires:  (crate(ethtool/default) >= 0.2.2 with crate(ethtool/default) < 0.3)
BuildRequires:  (crate(futures/default) >= 0.3 with crate(futures/default) < 0.4)
BuildRequires:  (crate(libc/default) >= 0.2.126 with crate(libc/default) < 0.3)
BuildRequires:  (crate(log/default) >= 0.4 with crate(log/default) < 0.5)
BuildRequires:  (crate(mptcp-pm/default) >= 0.1.1 with crate(mptcp-pm/default) < 0.2)
BuildRequires:  (crate(netlink-packet-route/default) >= 0.13.0 with crate(netlink-packet-route/default) < 0.14)
BuildRequires:  (crate(netlink-packet-utils/default) >= 0.5.1 with crate(netlink-packet-utils/default) < 0.6)
BuildRequires:  (crate(netlink-sys/default) >= 0.8.3 with crate(netlink-sys/default) < 0.9)
BuildRequires:  (crate(rtnetlink/default) >= 0.11.0 with crate(rtnetlink/default) < 0.12)
BuildRequires:  (crate(serde/default) >= 1.0 with crate(serde/default) < 2.0)
BuildRequires:  (crate(serde/derive) >= 1.0 with crate(serde/derive) < 2.0)
BuildRequires:  (crate(serde_json/default) >= 1.0 with crate(serde_json/default) < 2.0)
BuildRequires:  (crate(serde_yaml/default) >= 0.9 with crate(serde_yaml/default) < 0.10)
BuildRequires:  (crate(tokio/macros) >= 1.18 with crate(tokio/macros) < 2.0)
BuildRequires:  (crate(tokio/rt) >= 1.18 with crate(tokio/rt) < 2.0)

%description
Unified interface for Linux network state querying.

%package -n     rust-%{name}-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n rust-%{name}-devel

This package contains library source intended for building other packages
which use "%{name}" crate.

%package -n     rust-%{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n rust-%{name}+default-devel

This package contains library source intended for building other packages
which use "%{name}" crate with default feature.

%package -n     python3-%{name}
Summary:        %{summary}
Requires:       nispor = %{?epoch:%{epoch}:}%{version}-%{release}
BuildArch:      noarch

%description -n python3-%{name}

This package contains python3 binding of %{name}.

%package        devel
Summary:        %{summary}
Requires:       nispor%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel

This package contains C binding of %{name}.

%prep
%autosetup -n %{name}-%{version_no_tilde} -p1
# Drop the upstream fix on SONAME as fedora %cargo_xxx marcos override it,
# we use patchelf to set the SONAME.
rm .cargo/config.toml

%cargo_prep

%build
%cargo_build

pushd src/python
%py3_build
popd

%install
pushd src/lib
%cargo_install
popd

env SKIP_PYTHON_INSTALL=1 PREFIX=%{_prefix} LIBDIR=%{_libdir} %make_install

pushd src/python
%py3_install
popd

patchelf --set-soname libnispor.so.1 \
    %{buildroot}/%{_libdir}/libnispor.so.%{version}

%if %{with check}
%check
%cargo_test
%endif

%files
%doc AUTHORS CHANGELOG DEVEL.md README.md
%license LICENSE
%{_bindir}/npc
%{_libdir}/libnispor.so.*

%files -n       python3-%{name}
%license LICENSE
%{python3_sitelib}/nispor*

%files devel
%license LICENSE
%{_libdir}/libnispor.so
%{_includedir}/nispor.h
%{_libdir}/pkgconfig/nispor.pc

%files -n       rust-%{name}-devel
%license LICENSE
%{cargo_registry}/%{name}-%{version_no_tilde}/

%files -n       rust-%{name}+default-devel
%ghost %{cargo_registry}/%{name}-%{version_no_tilde}/Cargo.toml

%changelog
%autochangelog
