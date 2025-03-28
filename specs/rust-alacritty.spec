# Generated by rust2rpm 27
%bcond check 1

%global crate alacritty

Name:           rust-alacritty
Version:        0.15.1
Release:        %autorelease
Summary:        Fast, cross-platform, OpenGL terminal emulator

License:        Apache-2.0
URL:            https://crates.io/crates/alacritty
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          alacritty-fix-metadata-auto.diff

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  scdoc

%global _description %{expand:
A fast, cross-platform, OpenGL terminal emulator.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause
# BSD-2-Clause OR Apache-2.0 OR MIT
# BSD-3-Clause
# CC0-1.0
# ISC
# MIT
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR Zlib
# MIT OR Zlib OR Apache-2.0
# Unlicense OR MIT
# Zlib OR Apache-2.0 OR MIT
License:        %{shrink:
                (0BSD OR MIT OR Apache-2.0)
                AND Apache-2.0
                AND (Apache-2.0 OR BSL-1.0)
                AND (Apache-2.0 OR MIT)
                AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
                AND BSD-2-Clause
                AND (BSD-2-Clause OR Apache-2.0 OR MIT)
                AND BSD-3-Clause
                AND CC0-1.0
                AND ISC
                AND MIT
                AND (MIT OR Apache-2.0 OR Zlib)
                AND Unicode-DFS-2016
                AND (Unlicense OR MIT)
                }
# LICENSE.dependencies contains a full license breakdown

# libwayland-egl is dlopened when running on a wayland compositor
Requires:       libwayland-egl

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE-APACHE
%license LICENSE.dependencies
%doc CHANGELOG.md
%doc README.md
%{_bindir}/alacritty
%{_mandir}/man1/alacritty-msg.1*
%{_mandir}/man1/alacritty.1*
%{_mandir}/man5/alacritty-bindings.5*
%{_mandir}/man5/alacritty.5*
%{_metainfodir}/org.alacritty.Alacritty.appdata.xml
%{_datadir}/applications/Alacritty.desktop
%{_datadir}/pixmaps/Alacritty.svg
%{bash_completions_dir}/alacritty
%{zsh_completions_dir}/_alacritty
%{fish_completions_dir}/alacritty.fish

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
for fname in alacritty-bindings.5 alacritty-msg.1 alacritty.1 alacritty.5; do
    scdoc <extra/man/$fname.scd >extra/man/$fname
done

%install
%cargo_install
desktop-file-install --dir=%{buildroot}%{_datadir}/applications extra/linux/Alacritty.desktop
install -m644 -pvD extra/completions/alacritty.bash %{buildroot}%{bash_completions_dir}/alacritty
install -m644 -pvD extra/completions/_alacritty     %{buildroot}%{zsh_completions_dir}/_alacritty
install -m644 -pvD extra/completions/alacritty.fish %{buildroot}%{fish_completions_dir}/alacritty.fish
install -m644 -pvD extra/logo/alacritty-term.svg    %{buildroot}%{_datadir}/pixmaps/Alacritty.svg
install -m644 -pvD -t %{buildroot}%{_metainfodir}   extra/linux/org.alacritty.Alacritty.appdata.xml
for fname in alacritty-bindings.5 alacritty-msg.1 alacritty.1 alacritty.5; do
    install -m644 -pvD "extra/man/$fname" "%{buildroot}%{_mandir}/man${fname##*.}/$fname"
done

%if %{with check}
%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
# * expects workspace paths
%cargo_test -- -- --skip cli::tests::completions
%endif

%changelog
%autochangelog
