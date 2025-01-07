%global goipath github.com/charmbracelet/gum

Name:           gum
Version:        0.14.5
Release:        %autorelease
Summary:        Tool for glamorous shell scripts
# main source code is MIT
# see comments above provides tags for bundled license breakdown
License:        BSD-3-Clause AND MIT AND OFL-1.1
URL:            https://github.com/charmbracelet/gum

BuildRequires:  go-rpm-macros
ExclusiveArch:  %{golang_arches_future}

# see create-vendor-tarball.sh for how to create this
Source0:        gum-%{version}-vendored.tar.gz

# Script that creates vendor tarball
Source100:      create-vendor-tarball.sh

BuildRequires:  golang

# MIT AND OFL-1.1
Provides:       bundled(golang(github.com/alecthomas/chroma/v2)) = 2.14.0
# MIT
Provides:       bundled(golang(github.com/alecthomas/kong)) = 0.9.0
# MIT
Provides:       bundled(golang(github.com/alecthomas/mango-kong)) = 0.1.0
# BSD-3-Clause
Provides:       bundled(golang(github.com/atotto/clipboard)) = 0.1.4
# MIT
Provides:       bundled(golang(github.com/aymanbagabas/go-osc52/v2)) = 2.0.1
# MIT
Provides:       bundled(golang(github.com/aymerick/douceur)) = 0.2.0
# MIT
Provides:       bundled(golang(github.com/catppuccin/go)) = 0.2.0
# MIT
Provides:       bundled(golang(github.com/charmbracelet/bubbles)) = 0.20.0
# MIT
Provides:       bundled(golang(github.com/charmbracelet/bubbletea)) = 1.1.0
# MIT
Provides:       bundled(golang(github.com/charmbracelet/glamour)) = 0.8.0
# MIT
Provides:       bundled(golang(github.com/charmbracelet/huh)) = 0.6.0
# MIT
Provides:       bundled(golang(github.com/charmbracelet/lipgloss)) = 0.13.0
# MIT
Provides:       bundled(golang(github.com/charmbracelet/log)) = 0.4.0
# MIT
Provides:       bundled(golang(github.com/charmbracelet/x/ansi)) = 0.2.3
# MIT
Provides:       bundled(golang(github.com/charmbracelet/x/exp/strings)) = 212f7b0
# MIT
Provides:       bundled(golang(github.com/charmbracelet/x/term)) = 0.2.0
# MIT
Provides:       bundled(golang(github.com/dlclark/regexp2)) = 1.11.0
# MIT
Provides:       bundled(golang(github.com/dustin/go-humanize)) = 1.0.1
# MIT
Provides:       bundled(golang(github.com/erikgeiser/coninput)) = 1c3628e
# MIT
Provides:       bundled(golang(github.com/go-logfmt/logfmt)) = 0.6.0
# BSD-3-Clause
Provides:       bundled(golang(github.com/gorilla/css)) = 1.0.1
# MIT
Provides:       bundled(golang(github.com/lucasb-eyer/go-colorful)) = 1.2.0
# MIT
Provides:       bundled(golang(github.com/mattn/go-isatty)) = 0.0.20
# MIT
Provides:       bundled(golang(github.com/mattn/go-localereader)) = 0.0.1
# MIT
Provides:       bundled(golang(github.com/mattn/go-runewidth)) = 0.0.16
# BSD-3-Clause
Provides:       bundled(golang(github.com/microcosm-cc/bluemonday)) = 1.0.27
# MIT
Provides:       bundled(golang(github.com/mitchellh/hashstructure/v2)) = 2.0.2
# MIT
Provides:       bundled(golang(github.com/muesli/ansi)) = 276c624
# MIT
Provides:       bundled(golang(github.com/muesli/cancelreader)) = 0.2.2
# MIT
Provides:       bundled(golang(github.com/muesli/mango)) = 0.2.0
# MIT
Provides:       bundled(golang(github.com/muesli/reflow)) = 0.3.0
# MIT
Provides:       bundled(golang(github.com/muesli/roff)) = 0.1.0
# MIT
Provides:       bundled(golang(github.com/muesli/termenv)) = 98d742f
# MIT
Provides:       bundled(golang(github.com/rivo/uniseg)) = 0.4.7
# MIT
Provides:       bundled(golang(github.com/sahilm/fuzzy)) = 0.1.1
# MIT
Provides:       bundled(golang(github.com/yuin/goldmark)) = 1.7.4
# MIT
Provides:       bundled(golang(github.com/yuin/goldmark-emoji)) = 1.0.3
# BSD-3-Clause
Provides:       bundled(golang(golang.org/x/exp)) = 7f521ea
# BSD-3-Clause
Provides:       bundled(golang(golang.org/x/net)) = 0.27.0
# BSD-3-Clause
Provides:       bundled(golang(golang.org/x/sync)) = 0.8.0
# BSD-3-Clause
Provides:       bundled(golang(golang.org/x/sys)) = 0.25.0
# BSD-3-Clause
Provides:       bundled(golang(golang.org/x/term)) = 0.22.0
# BSD-3-Clause
Provides:       bundled(golang(golang.org/x/text)) = 0.18.0


%description
A tool for glamorous shell scripts. Leverage the power of Bubbles and Lip Gloss
in your scripts and aliases without writing any Go code!


%prep
%autosetup
mkdir -p src/$(dirname %{goipath})
ln -s $PWD src/%{goipath}

# set the program version
sed -e '/Version = / s/""/"%{version}"/' -i main.go


%build
export GO111MODULE=off
export GOPATH=$PWD
%gobuild -o bin/gum %{goipath}


%install
# command
install -D -p -m 0755 -t %{buildroot}%{_bindir} bin/gum

# man pages
install -d -m 0755 %{buildroot}%{_mandir}/man1
./bin/gum man > %{buildroot}%{_mandir}/man1/gum.1

# shell completions
install -d -m 0755 %{buildroot}%{bash_completions_dir}
./bin/gum completion bash > %{buildroot}%{bash_completions_dir}/gum
install -d -m 0755 %{buildroot}%{zsh_completions_dir}
./bin/gum completion zsh > %{buildroot}%{zsh_completions_dir}/_gum
install -d -m 0755 %{buildroot}%{fish_completions_dir}
./bin/gum completion fish > %{buildroot}%{fish_completions_dir}/gum.fish


%check
# ensure that the version was embedded correctly
[[ "$(./bin/gum --version)" == "gum version %{version}" ]] || exit 1

# run the upstream tests
export GOPATH=$PWD
cd src/%{goipath}
%gotest ./...


%files
%license LICENSE
%{_bindir}/gum
%{_mandir}/man1/gum.1*
%{bash_completions_dir}/gum
%{zsh_completions_dir}/_gum
%{fish_completions_dir}/gum.fish


%changelog
%autochangelog
