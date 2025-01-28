%bcond_without check

%global binary_name hx
%global runtime_directory_path %{_libdir}/helix/runtime

Name:           helix
Version:        25.01.1
Release:        %autorelease
# Output of %%{cargo_license_summary} + themes specific licenses (Unlicense)
# (Apache-2.0 OR MIT) AND BSD-3-Clause
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# BSD-3-Clause
# ISC
# MIT
# MIT AND Unicode-DFS-2016 AND BSD-2-Clause AND BSD-3-Clause AND LicenseRef-Fedora-Public-Domain
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR Zlib
# MIT OR Zlib OR Apache-2.0
# MIT-0 OR Apache-2.0
# MPL-2.0
# MPL-2.0+
# Unlicense OR MIT
# Zlib
# Zlib OR Apache-2.0 OR MIT
License:        (Apache-2.0 OR MIT) AND BSD-3-Clause AND Unicode-DFS-2016 AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND ISC AND MIT AND (MIT AND Unicode-DFS-2016 AND BSD-2-Clause AND BSD-3-Clause AND LicenseRef-Fedora-Public-Domain) AND (MIT OR Apache-2.0 OR Zlib) AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND MPL-2.0 AND MPL-2.0+ AND (Unlicense OR MIT) AND Zlib AND Unlicense
Summary:        A post-modern modal text editor written in Rust
URL:            https://helix-editor.com/
# This tarball includes grammars because we can't download them at build time
Source:         https://github.com/helix-editor/%{name}/releases/download/%{version}/%{name}-%{version}-source.tar.xz
# A PR for this has been filed upstream but it is unlikely to get merged since upstream
# is dead
Source200:      https://raw.githubusercontent.com/blinxen/tree-sitter-eex/main/LICENSE#/LICENSE-tree-sitter-eex

# Remove windows dependencies
Patch:          remove-windows-dependency.patch
# Compatibility patch for gix 0.70
# * https://github.com/helix-editor/helix/pull/12614/files
Patch:          gix-0.70-compatibility.patch

# Exclude %%{ix86} since the build fails with LLVM ERROR: out of memory Allocation failed error
ExcludeArch: %{ix86}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
# Used to build grammars
BuildRequires:  gcc-c++
BuildRequires:  git-core
# Patch Cargo.toml
BuildRequires:  tomcli

# Required to allow users to fetch and build grammars
Requires:       git-core
Requires:       gcc-c++

# Added manually
Provides:       bundled(tree-sitter-sql)
Provides:       bundled(tree-sitter-v)
Provides:       bundled(tree-sitter-perl)
Provides:       bundled(tree-sitter-pod)
# Created with:
# cd runtime/grammars/sources && fd '^package.json$' --max-depth 2 --exec /bin/sh -c 'cat {} | jq  ". | \"Provides:       bundled(\" + .name + \")\""' | sort | sed s/\"//g
# First 3 provide have "@" at the beginnig of the name, so we just remove it manually
Provides:       bundled(tree-sitter-pkl)
Provides:       bundled(tree-sitter-elm)
Provides:       bundled(tree-sitter-lua)
Provides:       bundled(tree-sitter-latex)
Provides:       bundled(tree-sitter-ada)
Provides:       bundled(tree-sitter-adl)
Provides:       bundled(tree-sitter-agda)
Provides:       bundled(tree-sitter-astro)
Provides:       bundled(tree-sitter-awk)
Provides:       bundled(tree-sitter-bash)
Provides:       bundled(tree-sitter-bass)
Provides:       bundled(tree-sitter-beancount)
Provides:       bundled(tree-sitter-bibtex)
Provides:       bundled(tree-sitter-bicep)
Provides:       bundled(tree-sitter-bitbake)
Provides:       bundled(tree-sitter-blade)
Provides:       bundled(tree-sitter-blueprint)
Provides:       bundled(tree-sitter-c)
Provides:       bundled(tree-sitter-cairo)
Provides:       bundled(tree-sitter-capnp)
Provides:       bundled(tree-sitter-cassette)
Provides:       bundled(tree-sitter-cel)
Provides:       bundled(tree-sitter-clojure)
Provides:       bundled(tree-sitter-cmake)
Provides:       bundled(tree-sitter-comment)
Provides:       bundled(tree-sitter-cpon)
Provides:       bundled(tree-sitter-cpp)
Provides:       bundled(tree-sitter-c-sharp)
Provides:       bundled(tree-sitter-css)
Provides:       bundled(tree-sitter-cue)
Provides:       bundled(tree-sitter-d)
Provides:       bundled(tree-sitter-dart)
Provides:       bundled(tree-sitter-dbml)
Provides:       bundled(tree-sitter-devicetree)
Provides:       bundled(tree-sitter-dhall)
Provides:       bundled(tree-sitter-diff)
Provides:       bundled(tree-sitter-dockerfile)
Provides:       bundled(tree-sitter-dot)
Provides:       bundled(tree-sitter-dtd)
Provides:       bundled(tree-sitter-earthfile)
Provides:       bundled(tree-sitter-edoc)
Provides:       bundled(tree-sitter-eex)
Provides:       bundled(tree-sitter-elisp)
Provides:       bundled(tree-sitter-elixir)
Provides:       bundled(tree-sitter-elvish)
Provides:       bundled(tree-sitter-embedded-template)
Provides:       bundled(tree-sitter-erlang)
Provides:       bundled(tree-sitter-esdl)
Provides:       bundled(tree-sitter-fidl)
Provides:       bundled(tree-sitter-fish)
Provides:       bundled(tree-sitter-forth)
Provides:       bundled(tree-sitter-fortran)
Provides:       bundled(tree-sitter-fsharp)
Provides:       bundled(tree-sitter-gas)
Provides:       bundled(tree-sitter-gdscript)
Provides:       bundled(tree-sitter-gemini)
Provides:       bundled(tree-sitter-gitattributes)
Provides:       bundled(tree-sitter-gitcommit)
Provides:       bundled(tree-sitter-git-config)
Provides:       bundled(tree-sitter-gitignore)
Provides:       bundled(tree-sitter-gleam)
Provides:       bundled(tree-sitter-glimmer)
Provides:       bundled(tree-sitter-glsl)
Provides:       bundled(tree-sitter-gn)
Provides:       bundled(tree-sitter-go)
Provides:       bundled(tree-sitter-godot-resource)
Provides:       bundled(tree-sitter-go-mod)
Provides:       bundled(tree-sitter-go-template)
Provides:       bundled(tree-sitter-go-work)
Provides:       bundled(tree-sitter-markdown)
Provides:       bundled(tree-sitter-graphql)
Provides:       bundled(tree-sitter-groovy)
Provides:       bundled(tree-sitter-hare)
Provides:       bundled(tree-sitter-haskell)
Provides:       bundled(tree-sitter-haskell-persistent)
Provides:       bundled(tree-sitter-hcl)
Provides:       bundled(tree-sitter-heex)
Provides:       bundled(tree-sitter-hocon)
Provides:       bundled(tree-sitter-hoon)
Provides:       bundled(tree-sitter-hosts)
Provides:       bundled(tree-sitter-html)
Provides:       bundled(tree-sitter-hurl)
Provides:       bundled(tree-sitter-hyprlang)
Provides:       bundled(tree-sitter-iex)
Provides:       bundled(tree-sitter-ini)
Provides:       bundled(tree-sitter-inko)
Provides:       bundled(tree-sitter-janet-simple)
Provides:       bundled(tree-sitter-java)
Provides:       bundled(tree-sitter-javascript)
Provides:       bundled(tree-sitter-jinja2)
Provides:       bundled(tree-sitter-jsdoc)
Provides:       bundled(tree-sitter-json)
Provides:       bundled(tree-sitter-json5)
Provides:       bundled(tree-sitter-jsonnet)
Provides:       bundled(tree-sitter-julia)
Provides:       bundled(tree-sitter-just)
Provides:       bundled(tree-sitter-kdl)
Provides:       bundled(tree-sitter-koka)
Provides:       bundled(tree-sitter-kotlin)
Provides:       bundled(tree-sitter-ld)
Provides:       bundled(tree-sitter-ldif)
Provides:       bundled(tree-sitter-lean)
Provides:       bundled(tree-sitter-ledger)
Provides:       bundled(tree-sitter-llvm)
Provides:       bundled(tree-sitter-llvm-mir)
Provides:       bundled(tree-sitter-log)
Provides:       bundled(tree-sitter-lpf)
Provides:       bundled(tree-sitter-make)
Provides:       bundled(tree-sitter-markdoc)
Provides:       bundled(tree-sitter-matlab)
Provides:       bundled(tree-sitter-mermaid)
Provides:       bundled(tree-sitter-meson)
Provides:       bundled(tree-sitter-mojo)
Provides:       bundled(tree-sitter-move)
Provides:       bundled(tree-sitter-nasm)
Provides:       bundled(tree-sitter-nickel)
Provides:       bundled(tree-sitter-nim)
Provides:       bundled(tree-sitter-nix)
Provides:       bundled(tree-sitter-nu)
Provides:       bundled(tree-sitter-ocaml)
Provides:       bundled(tree-sitter-odin)
Provides:       bundled(tree-sitter-ohm)
Provides:       bundled(tree-sitter-opencl)
Provides:       bundled(tree-sitter-openscad)
Provides:       bundled(tree-sitter-org)
Provides:       bundled(tree-sitter-pascal)
Provides:       bundled(tree-sitter-passwd)
Provides:       bundled(tree-sitter-pem)
Provides:       bundled(tree-sitter-pest)
Provides:       bundled(tree-sitter-php)
Provides:       bundled(tree-sitter-po)
Provides:       bundled(tree-sitter-ponylang)
Provides:       bundled(tree-sitter-powershell)
Provides:       bundled(tree-sitter-prisma)
Provides:       bundled(tree-sitter-protobuf)
Provides:       bundled(tree-sitter-prql)
Provides:       bundled(tree-sitter-purescript)
Provides:       bundled(tree-sitter-python)
Provides:       bundled(tree-sitter-qmljs)
Provides:       bundled(tree-sitter-r)
Provides:       bundled(tree-sitter-rebase)
Provides:       bundled(tree-sitter-regex)
Provides:       bundled(tree-sitter-rego)
Provides:       bundled(tree-sitter-rescript)
Provides:       bundled(tree-sitter-robot)
Provides:       bundled(tree-sitter-ron)
Provides:       bundled(tree-sitter-rst)
Provides:       bundled(tree-sitter-ruby)
Provides:       bundled(tree-sitter-rust)
Provides:       bundled(tree-sitter-scala)
Provides:       bundled(tree-sitter-scheme)
Provides:       bundled(tree-sitter-scss)
Provides:       bundled(tree-sitter-slint)
Provides:       bundled(tree-sitter-smali)
Provides:       bundled(tree-sitter-smithy)
Provides:       bundled(tree-sitter-sml)
Provides:       bundled(tree-sitter-solidity)
Provides:       bundled(tree-sitter-spicedb)
Provides:       bundled(tree-sitter-ssh-client-config)
Provides:       bundled(tree-sitter-strace)
Provides:       bundled(tree-sitter-supercollider)
Provides:       bundled(tree-sitter-svelte)
Provides:       bundled(tree-sitter-sway)
Provides:       bundled(tree-sitter-swift)
Provides:       bundled(tree-sitter-t32)
Provides:       bundled(tree-sitter-tablegen)
Provides:       bundled(tree-sitter-tact)
Provides:       bundled(tree-sitter-task)
Provides:       bundled(tree-sitter-tcl)
Provides:       bundled(tree-sitter-templ)
Provides:       bundled(tree-sitter-test)
Provides:       bundled(tree-sitter-todotxt)
Provides:       bundled(tree-sitter-toml)
Provides:       bundled(tree-sitter-tsq)
Provides:       bundled(tree-sitter-twig)
Provides:       bundled(tree-sitter-typescript)
Provides:       bundled(tree-sitter-ungrammar)
Provides:       bundled(tree-sitter-unison)
Provides:       bundled(tree-sitter-uxntal)
Provides:       bundled(tree-sitter-vala)
Provides:       bundled(tree-sitter-verilog)
Provides:       bundled(tree-sitter-vhdl)
Provides:       bundled(tree-sitter-vue)
Provides:       bundled(tree-sitter-wasm)
Provides:       bundled(tree-sitter-wgsl)
Provides:       bundled(tree-sitter-wit)
Provides:       bundled(tree-sitter-wren)
Provides:       bundled(tree-sitter-xit)
Provides:       bundled(tree-sitter-xml)
Provides:       bundled(tree-sitter-XTC)
Provides:       bundled(tree-sitter-yaml)
Provides:       bundled(tree-sitter-yuck)
Provides:       bundled(tree-sitter-zig)


%description
A Kakoune / Neovim inspired editor, written in Rust.


%files
%license LICENSE
%license LICENSE.dependencies
# Theme licenses
%license LICENSE-themes-*
# tree-sitter licenses
%license LICENSE-tree-sitter-*
%doc README.md CHANGELOG.md
%{_bindir}/%{binary_name}
# Added so the parent directory of the runtime directory is owned by this package
%dir %{_libdir}/helix
# We include the whole directory here because we always want to have all grammars + queries installed
%{runtime_directory_path}
%{_datadir}/applications/Helix.desktop
%{_metainfodir}/Helix.appdata.xml
%{_datadir}/pixmaps/helix.png
%{bash_completions_dir}/%{binary_name}
%{fish_completions_dir}/%{binary_name}.fish
%{zsh_completions_dir}/_%{binary_name}
# There is also a completion script for elvish shell but elvish is not packaged for Fedora


%prep
%autosetup -c -p1
# Bump gix to version 0.70
tomcli set helix-vcs/Cargo.toml str dependencies.gix.version 0.70
# Bump tree-sitter to version 0.23
tomcli set Cargo.toml str workspace.dependencies.tree-sitter.version 0.23
# Relax url lower bound
tomcli set helix-core/Cargo.toml str dependencies.url 2.5.2
tomcli set helix-lsp-types/Cargo.toml str dependencies.url.version 2.5.2
tomcli set helix-term/Cargo.toml str dependencies.url 2.5.2
tomcli set helix-view/Cargo.toml str dependencies.url 2.5.2
# Relax unicode-width lower bound
tomcli set helix-core/Cargo.toml str dependencies.unicode-width 0.1.14

# Rename license files for themes so they can be installed
find runtime/themes/licenses -type f -exec /bin/sh -c 'cp -pav {} LICENSE-themes-$(basename {} .LICENSE)' \;
# License for for tree-sitter-eex
cp -pav %{SOURCE200} .
# Rename license files for tree-sitter grammars so they can be installed
find runtime/grammars -name "LICENSE*" -type f -not -path '*/docs/*' -exec /bin/sh -c 'cp -pav {} LICENSE-tree-sitter-$(basename $(dirname {}))' \;
find runtime/grammars -name "LICENCE*" -type f -not -path '*/docs/*' -exec /bin/sh -c 'cp -pav {} LICENSE-tree-sitter-$(basename $(dirname {}))' \;
find runtime/grammars -name "COPYING*" -type f -not -path '*/docs/*' -exec /bin/sh -c 'cp -pav {} LICENSE-tree-sitter-$(basename $(dirname {}))' \;
# Some license files have weird permission bits
chmod -x LICENSE-*
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires


%build
# This will set the default runtime directly in the binary
export HELIX_DEFAULT_RUNTIME=%{runtime_directory_path}
%cargo_build

%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies


%install
# We can't use %%cargo_install here because it does not support setting --path
install -Dpm 0755 target/release/%{binary_name} %{buildroot}%{_bindir}/%{binary_name}

# Install desktop file and icon
# Use absolute paths for binary and icon
sed -i \
    -e "s|Exec=hx %%F|Exec=%{_bindir}/%{binary_name} %%F|g" \
    -e "s|TryExec=hx|TryExec=%{_bindir}/%{binary_name}|g" \
    -e "s|Icon=helix|Icon=%{_datadir}/pixmaps/helix.png|g" contrib/Helix.desktop
desktop-file-install --dir=%{buildroot}%{_datadir}/applications contrib/Helix.desktop
install -Dpm 0644 contrib/helix.png %{buildroot}%{_datadir}/pixmaps/helix.png
# Install AppData
install -Dpm 0644 contrib/Helix.appdata.xml %{buildroot}%{_metainfodir}/Helix.appdata.xml
# Install runtime configuration (includes tutor + queries + compiled grammars)
# Step 1: create directory structure
install -dm 0755 %{buildroot}%{runtime_directory_path}/
install -dm 0755 %{buildroot}%{runtime_directory_path}/grammars
install -dm 0755 %{buildroot}%{runtime_directory_path}/queries
find runtime/queries/ -type d -exec sh -c 'install -dm 0755 $(basename {}) %{buildroot}%{runtime_directory_path}/queries/$(basename {})' \;
install -dm 0755 %{buildroot}%{runtime_directory_path}/themes
# Step 2: install files
install -Dpm 0644 runtime/tutor %{buildroot}%{runtime_directory_path}/tutor
install -Dpm 0755 runtime/grammars/*.so -t %{buildroot}%{runtime_directory_path}/grammars
find runtime/queries/ -type f -exec sh -c 'install -Dpm 0644 {} %{buildroot}%{runtime_directory_path}/queries/$(basename $(dirname {}))' \;
install -Dpm 0644 runtime/themes/*.toml -t %{buildroot}%{runtime_directory_path}/themes

# Add shell completions
install -Dpm 0644 contrib/completion/%{binary_name}.bash %{buildroot}/%{bash_completions_dir}/%{binary_name}
install -Dpm 0644 contrib/completion/%{binary_name}.fish %{buildroot}/%{fish_completions_dir}/%{binary_name}.fish
install -Dpm 0644 contrib/completion/%{binary_name}.zsh %{buildroot}/%{zsh_completions_dir}/_%{binary_name}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/Helix.desktop
# This fails in epel9 because of an old version, so we just skip it
%if %{defined fedora}
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/Helix.appdata.xml
%endif
%if %{with check}
# Grammars are already built
export HELIX_DISABLE_AUTO_GRAMMAR_BUILD=true
%cargo_test
%{buildroot}%{_bindir}/%{binary_name} --health
%endif


%changelog
%autochangelog
