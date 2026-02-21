%bcond check 1
# server tests require pgsql 14
# el9 has ursine pgsql 13 and the newer ones are modular
%bcond pgtests %{undefined el9}

%global forgeurl https://github.com/atuinsh/atuin

Name:           atuin
Version:        18.11.0
Release:        %autorelease
Summary:        Magical shell history

SourceLicense:  MIT
# (MIT OR Apache-2.0) AND Unicode-3.0
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 AND ISC AND (MIT OR Apache-2.0)
# Apache-2.0 AND MIT
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR BSL-1.0 OR MIT
# Apache-2.0 OR ISC OR MIT
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# BSD-3-Clause
# BSD-3-Clause OR Apache-2.0
# CDLA-Permissive-2.0
# ISC
# MIT
# MIT AND (MIT OR Apache-2.0)
# MIT AND Apache-2.0
# MIT AND BSD-3-Clause
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR Zlib
# MIT OR Zlib OR Apache-2.0
# MPL-2.0
# Unicode-3.0
# Unlicense OR MIT
# Zlib
# Zlib OR Apache-2.0 OR MIT
License:        %{shrink:
    MIT AND
    Apache-2.0 AND
    BSD-3-Clause AND
    CDLA-Permissive-2.0 AND
    ISC AND
    MPL-2.0 AND
    Unicode-3.0 AND
    Unicode-DFS-2016 AND
    Zlib AND
    (0BSD OR MIT OR Apache-2.0) AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 OR BSL-1.0 OR MIT) AND
    (Apache-2.0 OR ISC OR MIT) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    (BSD-3-Clause OR Apache-2.0) AND
    (MIT OR Apache-2.0 OR Zlib) AND
    (Unlicense OR MIT)
}
# LICENSE.dependencies contains a full license breakdown

%forgemeta

URL:            https://atuin.sh
Source0:        %forgesource
# Script to enable atuin for all users
Source1:        atuin.sh.in
# Relax MSRV. Atuin always tries to use the latest rust version, but that
# breaks epel9 builds. Sometimes we can get away with just relaxing the MSRV
# when they haven't started to use the latest rust syntax. If that doesn't work
# try to package the latest version supported for epel and wait for rhel9 to
# catch up.
Patch:          atuin-relax-MSRV.patch
# * Remove divan, seems like it's a benchmark-only dependency
Patch:          atuin-remove-divan.patch
# * Update tiny-bip39 to 2.0.0
# * Cherry-picked https://github.com/atuinsh/atuin/pull/2643
Patch:          atuin-Update-tiny-bip39.patch
# * chore(deps): update whoami dependency to v2
# * https://github.com/atuinsh/atuin/pull/3118
# * Without changes to Cargo.lock
Patch:          atuin-whoami2.patch

BuildRequires:  cargo-rpm-macros >= 24
%if %{with check} && %{with pgtests}
BuildRequires:  postgresql-test-rpm-macros
%endif

%global _description %{expand:
Atuin replaces your existing shell history with a SQLite database, and records
additional context for your commands. Additionally, it provides optional and
fully encrypted synchronization of your history between machines, via an Atuin
server.
}

%description %{_description}

%package        all-users
Summary:        atuin init script for all users
Requires:       atuin = %{version}-%{release}
BuildArch:      noarch

# TODO: Add Requires/Recommends to bash-preexec

%description    all-users %{_description}

This package contains the init script to enable atuin for all users.

%prep
%forgeautosetup -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -a

%build
%cargo_build -a
%{cargo_license_summary -a}
%{cargo_license -a} > LICENSE.dependencies
# Create auxiliary files
mkdir -p other_installs/shell_completion
# Generate all shell-completions
for shell in bash fish zsh; do
  ./target/rpm/atuin gen-completions --shell ${shell} -o other_installs/shell_completion
done

# Write the atuin init scripts statically
mkdir -p other_installs/libexec/atuin
for shell in bash fish zsh; do
  ./target/rpm/atuin init ${shell} > other_installs/libexec/atuin/atuin-init.${shell}
done

# Generate the profile.d files enabling atuin for all users
mkdir -p other_installs/profile.d
sed "s|@ATUIN_SCRIPTS_DIR@|%{_libexecdir}/atuin|" %SOURCE1 > other_installs/profile.d/atuin.sh

%install
install -Dpm 0755 target/rpm/atuin -t %{buildroot}%{_bindir}
# Install the auxiliary files
# Shell completions
install -Dpm 0644 other_installs/shell_completion/atuin.bash -t %{buildroot}%{bash_completions_dir}
install -Dpm 0644 other_installs/shell_completion/atuin.fish -t %{buildroot}%{fish_completions_dir}
install -Dpm 0644 other_installs/shell_completion/_atuin -t %{buildroot}%{zsh_completions_dir}

# Static atuin init scripts
for shell in bash fish zsh; do
  install -Dpm 0755 other_installs/libexec/atuin/atuin-init.${shell} %{buildroot}%{_libexecdir}/atuin/atuin-init.${shell}
done
# Profile.d init script for all users
install -Dpm 0755 other_installs/profile.d/atuin.sh %{buildroot}%{_sysconfdir}/profile.d/atuin.sh

%if %{with check}
%check
%if %{with pgtests}
# start a postgres instance for the tests to use
export PGTESTS_LOCALE="C.UTF-8"
export PGTESTS_USERS="atuin:pass"
export PGTESTS_DATABASES="atuin:atuin"
export PGTESTS_PORT=5432
%postgresql_tests_run
%cargo_test -a
%else
%cargo_test -a -- -- --skip sync --skip change_password --skip multi_user_test --skip registration
%endif
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%doc CHANGELOG.md
%doc CODE_OF_CONDUCT.md
%doc CONTRIBUTING.md
%doc CONTRIBUTORS
%doc README.md
%{_bindir}/atuin
%{bash_completions_dir}/atuin.bash
%{fish_completions_dir}/atuin.fish
%{zsh_completions_dir}/_atuin
%{_libexecdir}/atuin

%files all-users
%config %{_sysconfdir}/profile.d/atuin.sh

%changelog
%autochangelog
