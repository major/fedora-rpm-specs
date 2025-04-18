# Generated by rust2rpm 27
%bcond check 1

%global crate binfmt-dispatcher

Name:           rust-binfmt-dispatcher
Version:        0.1.2
Release:        %autorelease
Summary:        Smart dispatcher for binfmt_misc

License:        MIT
URL:            https://crates.io/crates/binfmt-dispatcher
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  make
BuildRequires:  systemd-rpm-macros

%global _description %{expand:
binfmt-dispatcher is a simple dispatcher for binfmt_misc that dynamically picks the best interpreter to use at runtime.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# ISC
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
License:        ((MIT OR Apache-2.0) AND Unicode-DFS-2016) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND ISC AND MIT AND (MIT OR Apache-2.0) AND (Unlicense OR MIT)
# LICENSE.dependencies contains a full license breakdown
Requires:       polkit
Requires:       systemd
Recommends:     xdg-terminal-exec
Recommends:     zenity

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/binfmt-dispatcher
%doc docs/binfmt-dispatcher.toml.example
%dir %{_prefix}/lib/binfmt-dispatcher.d/
%ifnarch %{ix86} %{x86_64}
%{_binfmtdir}/zz-binfmt-dispatcher-*.conf
%{_prefix}/lib/binfmt-dispatcher.d/*.toml
%endif
%{_datadir}/polkit-1/actions/org.AsahiLinux.binfmt_dispatcher.policy
%config(noreplace) %ghost %{_sysconfdir}/binfmt-dispatcher.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install
make install-data DESTDIR="%{buildroot}"
install -Ddpm0755 %{buildroot}%{_prefix}/lib/binfmt-dispatcher.d
%ifarch %{ix86} %{x86_64}
rm %{buildroot}%{_binfmtdir}/binfmt-dispatcher-*.conf
rm %{buildroot}%{_sysconfdir}/binfmt-dispatcher.toml
%else
for f in %{buildroot}%{_binfmtdir}/binfmt-dispatcher-*.conf; do mv "$f" "$(dirname "$f")/zz-$(basename "$f")"; done
mv %{buildroot}%{_sysconfdir}/binfmt-dispatcher.toml %{buildroot}%{_prefix}/lib/binfmt-dispatcher.d/00-default.toml
%endif

%postun      -n %{crate}
if [ $1 -eq 0 ]; then
/bin/systemctl try-restart systemd-binfmt.service
fi

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
