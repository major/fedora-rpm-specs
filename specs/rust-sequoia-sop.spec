# Generated by rust2rpm 27
%bcond check 1

%global crate sequoia-sop

Name:           rust-sequoia-sop
Version:        0.37.2
Release:        %autorelease
Summary:        Implementation of the Stateless OpenPGP Interface using Sequoia

License:        GPL-2.0-or-later
URL:            https://crates.io/crates/sequoia-sop
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * switch crypto backend from Nettle to OpenSSL
# * exclude files that are only useful for upstream development
Patch:          sequoia-sop-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
An implementation of the Stateless OpenPGP Interface using Sequoia.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-3-Clause
# BSL-1.0
# GPL-2.0-or-later
# LGPL-2.0-or-later
# MIT
# MIT OR Apache-2.0
# MIT OR Zlib OR Apache-2.0
# MPL-2.0
# Unicode-3.0
# Unlicense OR MIT
# Zlib
License:        %{shrink:
    GPL-2.0-or-later AND
    Apache-2.0 AND
    BSD-3-Clause AND
    BSL-1.0 AND
    LGPL-2.0-or-later AND
    MIT AND
    MPL-2.0 AND
    Unicode-3.0 AND
    Unicode-DFS-2016 AND
    Zlib AND
    (0BSD OR MIT OR Apache-2.0) AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (MIT OR Zlib OR Apache-2.0) AND
    (Unlicense OR MIT)
}
# LICENSE.dependencies contains a full license breakdown

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE.txt
%license LICENSE.dependencies
%doc README.md
%{_bindir}/sqop
%{_bindir}/sqopv
%{_mandir}/man1/sqop*
%{bash_completions_dir}/sqop.bash
%{fish_completions_dir}/sqop.fish
%{zsh_completions_dir}/_sqop
%{bash_completions_dir}/sqopv.bash
%{fish_completions_dir}/sqopv.fish
%{zsh_completions_dir}/_sqopv

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE.txt
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

%package     -n %{name}+cli-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cli-devel %{_description}

This package contains library source intended for building other packages which
use the "cli" feature of the "%{crate}" crate.

%files       -n %{name}+cli-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+cliv-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cliv-devel %{_description}

This package contains library source intended for building other packages which
use the "cliv" feature of the "%{crate}" crate.

%files       -n %{name}+cliv-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+crypto-nettle-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+crypto-nettle-devel %{_description}

This package contains library source intended for building other packages which
use the "crypto-nettle" feature of the "%{crate}" crate.

%files       -n %{name}+crypto-nettle-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+crypto-openssl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+crypto-openssl-devel %{_description}

This package contains library source intended for building other packages which
use the "crypto-openssl" feature of the "%{crate}" crate.

%files       -n %{name}+crypto-openssl-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+crypto-rust-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+crypto-rust-devel %{_description}

This package contains library source intended for building other packages which
use the "crypto-rust" feature of the "%{crate}" crate.

%files       -n %{name}+crypto-rust-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -f cli,cliv

%build
export ASSET_OUT_DIR=target/assets
%cargo_build -f cli,cliv
%{cargo_license_summary -f cli,cliv}
%{cargo_license -f cli,cliv} > LICENSE.dependencies

%install
%cargo_install -f cli,cliv
# install manual pages
mkdir -p %{buildroot}/%{_mandir}/man1
cp -pav target/assets/man-pages/sqop*.1 %{buildroot}/%{_mandir}/man1/
# install shell completions
install -Dpm 0644 target/assets/shell-completions/sqop.bash \
    %{buildroot}/%{bash_completions_dir}/sqop.bash
install -Dpm 0644 target/assets/shell-completions/sqopv.bash \
    %{buildroot}/%{bash_completions_dir}/sqopv.bash
install -Dpm 0644 target/assets/shell-completions/sqop.fish \
    %{buildroot}/%{fish_completions_dir}/sqop.fish
install -Dpm 0644 target/assets/shell-completions/sqopv.fish \
    %{buildroot}/%{fish_completions_dir}/sqopv.fish
install -Dpm 0644 target/assets/shell-completions/_sqop \
    %{buildroot}/%{zsh_completions_dir}/_sqop
install -Dpm 0644 target/assets/shell-completions/_sqopv \
    %{buildroot}/%{zsh_completions_dir}/_sqopv

%if %{with check}
%check
%cargo_test -f cli,cliv
%endif

%changelog
%autochangelog
