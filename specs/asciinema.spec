Name:           asciinema
Version:        3.0.0
Release:        %autorelease
Summary:        Terminal session recorder, streamer and player

# https://github.com/asciinema/asciinema/issues/699
SourceLicense:  GPL-3.0-or-later
# Rust dependencies:
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 AND ISC AND (MIT OR Apache-2.0)
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR ISC OR MIT
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# BSD-3-Clause
# GPL-3.0-or-later
# ISC
# MIT
# MIT AND BSD-3-Clause
# MIT OR Apache-2.0
# MIT OR Zlib OR Apache-2.0
# Unicode-3.0
# Unlicense OR MIT
# Zlib OR Apache-2.0 OR MIT
License:        %{shrink:
    GPL-3.0-or-later AND
    Apache-2.0 AND
    BSD-3-Clause AND
    ISC AND
    MIT AND
    Unicode-3.0 AND
    Unicode-DFS-2016 AND
    (0BSD OR MIT OR Apache-2.0) AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 OR ISC OR MIT) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    (MIT OR Zlib OR Apache-2.0) AND
    (Unlicense OR MIT)
}
# LICENSE.dependencies contains a full license breakdown

URL:            https://asciinema.org
Source:         https://github.com/asciinema/asciinema/archive/v%{version}/asciinema-%{version}.tar.gz

# Update tokio-tungstenite from 0.26 to 0.28
#
# This matches the verison used by the latest axum, 0.8.6.
#
# This was proposed upstream as part of a larger set of updates, “chore:
# update dependencies” at https://github.com/asciinema/asciinema/pull/698.
#
# In this minimal downstream patch, only Cargo.toml is adjusted.
Patch:          0001-Update-tokio-tungstenite-from-0.26-to-0.28.patch

BuildRequires:  cargo-rpm-macros

%description
asciinema (aka asciinema CLI or asciinema recorder) is a command-line
tool for recording and live streaming terminal sessions.

%prep
%autosetup -n asciinema-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -t

%build
export ASCIINEMA_GEN_DIR=assets
%cargo_build
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies

%install
install -Dpm 0755 target/rpm/asciinema -t %{buildroot}/%{_bindir}/
install -Dpm 0644 assets/man/*.1 -t %{buildroot}/%{_mandir}/man1/
install -Dpm 0644 assets/completion/asciinema.bash -t %{buildroot}/%{bash_completions_dir}/
install -Dpm 0644 assets/completion/asciinema.fish -t %{buildroot}/%{fish_completions_dir}/
install -Dpm 0644 assets/completion/_asciinema -t %{buildroot}/%{zsh_completions_dir}

%check
%cargo_test -- -- --test-threads 1

%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%doc CHANGELOG.md
%{_bindir}/asciinema
%{_mandir}/man1/asciinema*.1*
%{bash_completions_dir}/asciinema.bash
%{fish_completions_dir}/asciinema.fish
%{zsh_completions_dir}/_asciinema

%changelog
%autochangelog
