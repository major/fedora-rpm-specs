# cargo test is disabled by default as it requires etherparse, and doesn't do much
# make test / python scapy requires unshare and CLONE_NETNS which aren't allowed on koji
%bcond_with check

%global crate libslirp

Name:           rust-%{crate}
Version:        4.2.2
Release:        14%{?dist}
Summary:        High-level bindings & helper process for libslirp

License:        MIT
URL:            https://crates.io/crates/libslirp
Source:         %{crates_source}
# For rust-ipnetwork 0.17.0
# https://gitlab.freedesktop.org/slirp/libslirp-rs/-/merge_requests/7
Patch0:         libslirp-fix-metadata.diff
Patch1:         0001-Bump-systemd-dependency-rhbz-2027023.patch

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
High-level bindings & helper process for libslirp.}

%description %{_description}

%if ! %{__cargo_skip_build}
%package     -n %{crate}-helper
Summary:        %{summary}
# * ASL 2.0
# * ASL 2.0 or MIT
# * BSD
# * MIT
# * MIT or ASL 2.0
# * Unlicense or MIT
License:        MIT and ASL 2.0 and BSD

%description -n %{crate}-helper %{_description}

%files       -n %{crate}-helper
%license LICENSE
%{_bindir}/libslirp-helper
%endif

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+dbus-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dbus-devel %{_description}

This package contains library source intended for building other packages
which use "dbus" feature of "%{crate}" crate.

%files       -n %{name}+dbus-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+ipnetwork-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ipnetwork-devel %{_description}

This package contains library source intended for building other packages
which use "ipnetwork" feature of "%{crate}" crate.

%files       -n %{name}+ipnetwork-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+lazy_static-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+lazy_static-devel %{_description}

This package contains library source intended for building other packages
which use "lazy_static" feature of "%{crate}" crate.

%files       -n %{name}+lazy_static-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+libc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+libc-devel %{_description}

This package contains library source intended for building other packages
which use "libc" feature of "%{crate}" crate.

%files       -n %{name}+libc-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+libsystemd-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+libsystemd-devel %{_description}

This package contains library source intended for building other packages
which use "libsystemd" feature of "%{crate}" crate.

%files       -n %{name}+libsystemd-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+mio-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+mio-devel %{_description}

This package contains library source intended for building other packages
which use "mio" feature of "%{crate}" crate.

%files       -n %{name}+mio-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+mio-extras-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+mio-extras-devel %{_description}

This package contains library source intended for building other packages
which use "mio-extras" feature of "%{crate}" crate.

%files       -n %{name}+mio-extras-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+nix-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+nix-devel %{_description}

This package contains library source intended for building other packages
which use "nix" feature of "%{crate}" crate.

%files       -n %{name}+nix-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+slab-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+slab-devel %{_description}

This package contains library source intended for building other packages
which use "slab" feature of "%{crate}" crate.

%files       -n %{name}+slab-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+structopt-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+structopt-devel %{_description}

This package contains library source intended for building other packages
which use "structopt" feature of "%{crate}" crate.

%files       -n %{name}+structopt-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+url-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+url-devel %{_description}

This package contains library source intended for building other packages
which use "url" feature of "%{crate}" crate.

%files       -n %{name}+url-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

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
* Sun Feb 05 2023 Fabio Valentini <decathorpe@gmail.com> - 4.2.2-14
- Rebuild for fixed frame pointer compiler flags in Rust RPM macros.

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 15 2022 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.2.2-11
- Rebuild with package notes

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 29 2021 Marc-André Lureau <marcandre.lureau@redhat.com> - 4.2.2-9
- Fix FTBFS rhbz#2027023

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 16 15:01:34 GMT 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 4.2.2-6
- Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Dusty Mabe <dusty@dustymabe.com> - 4.2.2-4
- Respin. We updated rust-ipnetwork to 0.17.0

* Tue May 12 2020 Igor Raits <ignatenkobrain@fedoraproject.org. - 4.2.2-3
- Rename subpackage to a libslirp-helper

* Mon May 11 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 4.2.2-2
- Fixup license

* Wed May 06 21:46:00 CEST 2020 Marc-André Lureau <marcandre.lureau@redhat.com> - 4.2.2-1
- Initial package
