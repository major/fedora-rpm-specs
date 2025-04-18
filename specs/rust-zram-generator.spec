# Generated by rust2rpm 24
%bcond_without check

# RHEL does not have packages for Rust dependencies
%if 0%{?rhel}
%global bundled_rust_deps 1
%else
%global bundled_rust_deps 0
%endif

%global crate zram-generator

Name:           rust-zram-generator
Version:        1.2.1
Release:        %autorelease
Summary:        Systemd unit generator for zram swap devices

License:        MIT
URL:            https://crates.io/crates/zram-generator
Source0:        %{crates_source}
Source1:        zram-generator.conf
# To create the vendor tarball:
#   tar xf %%{crate}-%%{version}.crate ; pushd %%{crate}-%%{version} ; \
#   cargo vendor && tar Jcvf ../%%{crate}-%%{version}-vendor.tar.xz vendor/ ; popd
Source2:        %{crate}-1.2.0-vendor.tar.xz

%if 0%{?bundled_rust_deps}
BuildRequires:  rust-toolset
BuildRequires:  make
BuildRequires:  /usr/bin/ronn
BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd-rpm-macros
%else
BuildRequires:  rust-packaging >= 21
%endif

%global _description %{expand:
This is a systemd unit generator that enables swap on zram.
(With zram, there is no physical swap device. Part of the available RAM
is used to store compressed pages, essentially trading CPU cycles for memory.)

To activate, install %{crate}-defaults subpackage.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
License:        MIT AND (Apache-2.0 OR MIT)
Recommends:     %{_sbindir}/zramctl

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%if 0%{?bundled_rust_deps}
%license cargo-vendor.txt
%endif
%doc zram-generator.conf.example
%doc README.md
%{_systemdgeneratordir}/zram-generator
%{_unitdir}/systemd-zram-setup@.service
%{_mandir}/man8/zram-generator.8*
%{_mandir}/man5/zram-generator.conf.5*

%package     -n %{crate}-defaults
Summary:        Default configuration for %{crate}
Requires:       %{crate} = %{version}-%{release}
Obsoletes:      zram < 0.4-2
BuildArch:      noarch

%description -n %{crate}-defaults
%{summary}.

%files       -n %{crate}-defaults
%{_prefix}/lib/systemd/zram-generator.conf

%if ! 0%{?bundled_rust_deps}
%package        devel
Summary:        %{summary}
BuildArch:      noarch

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
%endif

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1 %{?bundled_rust_deps:-a2}
cp -a %{S:1} .
%if 0%{?bundled_rust_deps}
%cargo_prep -v vendor
%else
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
echo '/usr/bin/make'
echo '/usr/bin/ronn'
echo 'pkgconfig(systemd)'
echo 'systemd-rpm-macros'
%endif

%build
export SYSTEMD_UTIL_DIR=%{_systemd_util_dir}
export LC_ALL=C.UTF-8
%cargo_build
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%if 0%{?bundled_rust_deps}
%cargo_vendor_manifest
%endif
%make_build SYSTEMD_SYSTEM_UNIT_DIR=%{_unitdir} SYSTEMD_SYSTEM_GENERATOR_DIR=%{_systemdgeneratordir} \
  systemd-service man

%install
export SYSTEMD_UTIL_DIR=%{_systemd_util_dir}
%cargo_install

rm %{buildroot}%{_bindir}/zram-generator
%make_install SYSTEMD_SYSTEM_UNIT_DIR=%{_unitdir} SYSTEMD_SYSTEM_GENERATOR_DIR=%{_systemdgeneratordir} \
  NOBUILD=1

install -Dpm0644 -t %{buildroot}%{_prefix}/lib/systemd %{SOURCE1}

%if %{with check}
%check
export SYSTEMD_UTIL_DIR=%{_systemd_util_dir}
%cargo_test

: ==============================================================================
%{buildroot}%{_systemdgeneratordir}/zram-generator --help
: ==============================================================================
%{buildroot}%{_systemdgeneratordir}/zram-generator --help | grep -q %{_systemd_util_dir}/systemd-makefs
%endif

%changelog
%autochangelog
