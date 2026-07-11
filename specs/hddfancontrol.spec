%global crate hddfancontrol

Name:           %{crate}
Version:        2.1.2
Release:        %autorelease
Summary:        Daemon to regulate fan speed according to hard drive temperature on Linux

License:        GPL-3.0-only AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND MIT AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND (Unlicense OR MIT)
URL:            https://github.com/desbma/hddfancontrol
Source0:        https://github.com/desbma/hddfancontrol/archive/v%{version}/%{crate}-%{version}.tar.gz

# ExclusiveArch for Rust packages in Fedora
ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  systemd-rpm-macros

Requires:       hdparm
Requires:       smartmontools
Recommends:     sdparm
Recommends:     hddtemp

%description
HDD Fan control is a daemon to dynamically control fan speed according to
hard drive temperature on Linux.

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep
# Configure Cargo to use the vendored sources
sed -i 's/replace-with = "local-registry"/replace-with = "vendored-sources"/' .cargo/config.toml
cat >> .cargo/config.toml << EOF

[source.vendored-sources]
directory = "vendor"
EOF

%build
%cargo_build -f generate-extras
%{cargo_license_summary} -f generate-extras
%{cargo_license} -f generate-extras > LICENSE.dependencies

# Generate man pages and shell completions
mkdir -p target/man target/shell-completions
./target/rpm/hddfancontrol gen-man-pages target/man
./target/rpm/hddfancontrol gen-shell-completions target/shell-completions

%install
%cargo_install -f generate-extras

# Install systemd service and configuration file
install -Dpm 0644 systemd/hddfancontrol.service -t %{buildroot}%{_unitdir}/
install -Dpm 0644 systemd/hddfancontrol.conf -t %{buildroot}%{_sysconfdir}/

# Install man pages
install -Dpm 0644 target/man/hddfancontrol.1 -t %{buildroot}%{_mandir}/man1/

# Install shell completions
install -Dpm 0644 target/shell-completions/hddfancontrol.bash %{buildroot}%{bash_completions_dir}/hddfancontrol
install -Dpm 0644 target/shell-completions/hddfancontrol.fish -t %{buildroot}%{fish_completions_dir}/
install -Dpm 0644 target/shell-completions/_hddfancontrol -t %{buildroot}%{zsh_completions_dir}/

%check
%cargo_test -f generate-extras

%post
%systemd_post hddfancontrol.service

%preun
%systemd_preun hddfancontrol.service

%postun
%systemd_postun_with_restart hddfancontrol.service

%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%doc CHANGELOG.md
%doc AGENTS.md
%{_bindir}/hddfancontrol
%{_unitdir}/hddfancontrol.service
%config(noreplace) %{_sysconfdir}/hddfancontrol.conf
%{_mandir}/man1/hddfancontrol.1*
%{bash_completions_dir}/hddfancontrol
%{fish_completions_dir}/hddfancontrol.fish
%{zsh_completions_dir}/_hddfancontrol

%changelog
%autochangelog
