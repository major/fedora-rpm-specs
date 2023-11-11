%bcond_without check

%global binary_name hx
%global runtime_directory_path %{_libdir}/helix/runtime

Name:           helix
Version:        23.10
Release:        %autorelease
# Output of %%{cargo_license_summary}
# (Apache-2.0 OR MIT) AND BSD-3-Clause
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# BSD-3-Clause
# CC0-1.0 OR MIT-0 OR Apache-2.0
# ISC
# MIT
# MIT AND Unicode-DFS-2016 AND BSD-2-Clause AND BSD-3-Clause AND LicenseRef-Fedora-Public-Domain
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR Zlib
# MIT OR Zlib OR Apache-2.0
# MPL-2.0
# MPL-2.0+
# Unlicense OR MIT
# Zlib
# Zlib OR Apache-2.0 OR MIT
License:        (Apache-2.0 OR MIT) AND BSD-3-Clause AND Unicode-DFS-2016 AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND ISC AND MIT AND (MIT AND Unicode-DFS-2016 AND BSD-2-Clause AND BSD-3-Clause AND LicenseRef-Fedora-Public-Domain) AND (MIT OR Apache-2.0 OR Zlib) AND MPL-2.0 AND MPL-2.0+ AND (Unlicense OR MIT) AND Zlib
Summary:        A post-modern modal text editor written in Rust
URL:            https://helix-editor.com/
# This tarball includes grammars because we can't download them at build time
Source:         https://github.com/helix-editor/%{name}/releases/download/%{version}/%{name}-%{version}-source.tar.xz
# License files for themes, this should not be required in the next release as the PR is merged upstream
Source100:      https://raw.githubusercontent.com/helix-editor/helix/master/runtime/themes/licenses/everforest.LICENSE
Source102:      https://raw.githubusercontent.com/helix-editor/helix/master/runtime/themes/licenses/serika-syntax.LICENSE
Source103:      https://raw.githubusercontent.com/helix-editor/helix/master/runtime/themes/licenses/sonokai.LICENSE
# License files for grammars, this should not be required in the next release as the upstream PR will be merged soon
Source200:      https://raw.githubusercontent.com/DerekStride/tree-sitter-sql/main/LICENSE#/LICENSE-tree-sitter-sql
Source201:      https://raw.githubusercontent.com/benwilliamgraham/tree-sitter-llvm/main/LICENSE#/LICENSE-tree-sitter-llvm
Source202:      https://raw.githubusercontent.com/stsewd/tree-sitter-comment/master/LICENSE#/LICENSE-tree-sitter-comment
Source203:      https://raw.githubusercontent.com/polarmutex/tree-sitter-beancount/master/LICENSE#/LICENSE-tree-sitter-beancount
Source204:      https://raw.githubusercontent.com/Philipp-M/tree-sitter-ungrammar/main/LICENSE#/LICENSE-tree-sitter-ungrammar
Source205:      https://raw.githubusercontent.com/tree-sitter-perl/tree-sitter-perl/master/LICENSE#/LICENSE-tree-sitter-perl
Source206:      https://raw.githubusercontent.com/virchau13/tree-sitter-astro/master/LICENSE#/LICENSE-tree-sitter-astro
Source207:      https://raw.githubusercontent.com/Jummit/tree-sitter-uxntal/master/LICENSE#/LICENSE-tree-sitter-uxntal
Source209:      https://raw.githubusercontent.com/AlexanderBrevig/tree-sitter-forth/main/LICENSE#/LICENSE-tree-sitter-forth
Source210:      https://raw.githubusercontent.com/FallenAngel97/tree-sitter-rego/master/LICENSE#/LICENSE-tree-sitter-rego
Source212:      https://raw.githubusercontent.com/Maskhjarna/tree-sitter-purescript/main/LICENSE#/LICENSE-tree-sitter-purescript
# License files for grammars
Source208:      https://raw.githubusercontent.com/kylegoetz/tree-sitter-unison/master/LICENSE#/LICENSE-tree-sitter-unison
# PRs for the next license files have already been filed
Source211:      https://raw.githubusercontent.com/blinxen/tree-sitter-eex/main/LICENSE#/LICENSE-tree-sitter-eex
Source213:      https://raw.githubusercontent.com/blinxen/tree-sitter-pod/main/LICENSE#/LICENSE-tree-sitter-pod
Source214:      https://raw.githubusercontent.com/blinxen/tree-sitter-vhs/main/LICENSE#/LICENSE-tree-sitter-vhs
Source215:      https://raw.githubusercontent.com/blinxen/tree-sitter-smithy/main/LICENSE#/LICENSE-tree-sitter-smithy

# Remove windows dependencies
Patch:          remove-windows-dependency.patch

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
# Used to build grammars
BuildRequires:  gcc-c++
BuildRequires:  git-core

# Required to allow users to fetch and build grammars
Requires:       git-core
Requires:       gcc-c++

# Added manually
Provides:       bundled(tree-sitter-sql)
Provides:       bundled(tree-sitter-v)
Provides:       bundled(tree-sitter-perl)
Provides:       bundled(tree-sitter-pod)
# Created with:
# cd runtime/grammars/source && fd package.json --max-depth 2 --exec /bin/sh -c 'cat {} | sed s/@.*\//g | jq  ". | \"Provides:       bundled(\" + .name + \")\""' | sort | sed s/\"//g
# First 3 provides have "@" at the beginnig of the name, so we just remove it manually
Provides:       bundled(tree-sitter-elm)
Provides:       bundled(tree-sitter-lua)
Provides:       bundled(tree-sitter-latex)
Provides:       bundled(tree-sitter-astro)
Provides:       bundled(tree-sitter-awk)
Provides:       bundled(tree-sitter-bash)
Provides:       bundled(tree-sitter-bass)
Provides:       bundled(tree-sitter-beancount)
Provides:       bundled(tree-sitter-bibtex)
Provides:       bundled(tree-sitter-bicep)
Provides:       bundled(tree-sitter-blueprint)
Provides:       bundled(tree-sitter-c)
Provides:       bundled(tree-sitter-capnp)
Provides:       bundled(tree-sitter-cassette)
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
Provides:       bundled(tree-sitter-devicetree)
Provides:       bundled(tree-sitter-dhall)
Provides:       bundled(tree-sitter-diff)
Provides:       bundled(tree-sitter-dockerfile)
Provides:       bundled(tree-sitter-dot)
Provides:       bundled(tree-sitter-dtd)
Provides:       bundled(tree-sitter-edoc)
Provides:       bundled(tree-sitter-eex)
Provides:       bundled(tree-sitter-elixir)
Provides:       bundled(tree-sitter-elvish)
Provides:       bundled(tree-sitter-embedded-template)
Provides:       bundled(tree-sitter-erlang)
Provides:       bundled(tree-sitter-esdl)
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
Provides:       bundled(tree-sitter-glsl)
Provides:       bundled(tree-sitter-go)
Provides:       bundled(tree-sitter-godot-resource)
Provides:       bundled(tree-sitter-go-mod)
Provides:       bundled(tree-sitter-go-template)
Provides:       bundled(tree-sitter-go-work)
Provides:       bundled(tree-sitter-graphql)
Provides:       bundled(tree-sitter-hare)
Provides:       bundled(tree-sitter-haskell)
Provides:       bundled(tree-sitter-haskell-persistent)
Provides:       bundled(tree-sitter-hcl)
Provides:       bundled(tree-sitter-heex)
Provides:       bundled(tree-sitter-hosts)
Provides:       bundled(tree-sitter-html)
Provides:       bundled(tree-sitter-hurl)
Provides:       bundled(tree-sitter-iex)
Provides:       bundled(tree-sitter-ini)
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
Provides:       bundled(tree-sitter-kotlin)
Provides:       bundled(tree-sitter-lean)
Provides:       bundled(tree-sitter-ledger)
Provides:       bundled(tree-sitter-llvm)
Provides:       bundled(tree-sitter-llvm-mir)
Provides:       bundled(tree-sitter-make)
Provides:       bundled(tree-sitter-markdoc)
Provides:       bundled(tree-sitter-markdown)
Provides:       bundled(tree-sitter-markdown)
Provides:       bundled(tree-sitter-matlab)
Provides:       bundled(tree-sitter-mermaid)
Provides:       bundled(tree-sitter-meson)
Provides:       bundled(tree-sitter-nasm)
Provides:       bundled(tree-sitter-nickel)
Provides:       bundled(tree-sitter-nim)
Provides:       bundled(tree-sitter-nix)
Provides:       bundled(tree-sitter-nu)
Provides:       bundled(tree-sitter-ocaml)
Provides:       bundled(tree-sitter-ocaml)
Provides:       bundled(tree-sitter-odin)
Provides:       bundled(tree-sitter-opencl)
Provides:       bundled(tree-sitter-openscad)
Provides:       bundled(tree-sitter-org)
Provides:       bundled(tree-sitter-pascal)
Provides:       bundled(tree-sitter-passwd)
Provides:       bundled(tree-sitter-pem)
Provides:       bundled(tree-sitter-php)
Provides:       bundled(tree-sitter-po)
Provides:       bundled(tree-sitter-ponylang)
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
Provides:       bundled(tree-sitter-rst)
Provides:       bundled(tree-sitter-ruby)
Provides:       bundled(tree-sitter-rust)
Provides:       bundled(tree-sitter-scala)
Provides:       bundled(tree-sitter-scheme)
Provides:       bundled(tree-sitter-scss)
Provides:       bundled(tree-sitter-slint)
Provides:       bundled(tree-sitter-smithy)
Provides:       bundled(tree-sitter-sml)
Provides:       bundled(tree-sitter-solidity)
Provides:       bundled(tree-sitter-ssh-client-config)
Provides:       bundled(tree-sitter-strace)
Provides:       bundled(tree-sitter-svelte)
Provides:       bundled(tree-sitter-sway)
Provides:       bundled(tree-sitter-swift)
Provides:       bundled(tree-sitter-t32)
Provides:       bundled(tree-sitter-tablegen)
Provides:       bundled(tree-sitter-task)
Provides:       bundled(tree-sitter-templ)
Provides:       bundled(tree-sitter-todotxt)
Provides:       bundled(tree-sitter-toml)
Provides:       bundled(tree-sitter-tsq)
Provides:       bundled(tree-sitter-twig)
Provides:       bundled(tree-sitter-typescript)
Provides:       bundled(tree-sitter-typescript)
Provides:       bundled(tree-sitter-ungrammar)
Provides:       bundled(tree-sitter-unison)
Provides:       bundled(tree-sitter-uxntal)
Provides:       bundled(tree-sitter-vala)
Provides:       bundled(tree-sitter-verilog)
Provides:       bundled(tree-sitter-vhdl)
Provides:       bundled(tree-sitter-vue)
Provides:       bundled(tree-sitter-wasm)
Provides:       bundled(tree-sitter-wasm)
Provides:       bundled(tree-sitter-wgsl)
Provides:       bundled(tree-sitter-wit)
Provides:       bundled(tree-sitter-wren)
Provides:       bundled(tree-sitter-xit)
Provides:       bundled(tree-sitter-xml)
Provides:       bundled(tree-sitter-yaml)
Provides:       bundled(tree-sitter-yuck)
Provides:       bundled(tree-sitter-zig)


%description
A Kakoune / Neovim inspired editor, written in Rust.

%files
%license LICENSE
%license LICENSE.dependencies
# Theme licenses
%license everforest.LICENSE
%license serika-syntax.LICENSE
%license sonokai.LICENSE
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
# Add themes license files
cp -pav %{SOURCE100} %{SOURCE102} %{SOURCE103} .
# License files for grammars
cp -pav %{SOURCE200} %{SOURCE201} %{SOURCE202} %{SOURCE203} %{SOURCE204} %{SOURCE205} %{SOURCE206} %{SOURCE207} %{SOURCE208} %{SOURCE209} %{SOURCE210} %{SOURCE212} .
cp -pav %{SOURCE211} %{SOURCE213} %{SOURCE214} %{SOURCE215} .
# Rename license files for tree-sitter grammars so they can be installed
find runtime -name "LICENSE*" -type f -not -path '*/docs/*' -exec /bin/sh -c 'cp -pav {} LICENSE-tree-sitter-$(basename $(dirname {}))' \;
find runtime -name "LICENCE*" -type f -not -path '*/docs/*' -exec /bin/sh -c 'cp -pav {} LICENSE-tree-sitter-$(basename $(dirname {}))' \;
find runtime -name "COPYING*" -type f -not -path '*/docs/*' -exec /bin/sh -c 'cp -pav {} LICENSE-tree-sitter-$(basename $(dirname {}))' \;
# Some license files have weird permission bits
chmod -x LICENSE-tree-sitter-*
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
