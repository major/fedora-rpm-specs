%global goipath github.com/charmbracelet/gum

Name:           gum
Version:        0.15.2
Release:        %autorelease
Summary:        Tool for glamorous shell scripts
# main source code is MIT
# BSD-3-Clause:
#   - golang(github.com/atotto/clipboard)
#   - golang(github.com/gorilla/css)
#   - golang(github.com/microcosm-cc/bluemonday)
#   - golang(golang.org/x/exp)
#   - golang(golang.org/x/net)
#   - golang(golang.org/x/sync)
#   - golang(golang.org/x/sys)
#   - golang(golang.org/x/term)
#   - golang(golang.org/x/text)
# MIT:
#   - golang(github.com/alecthomas/kong)
#   - golang(github.com/alecthomas/mango-kong)
#   - golang(github.com/aymanbagabas/go-osc52/v2)
#   - golang(github.com/aymerick/douceur)
#   - golang(github.com/charmbracelet/bubbles)
#   - golang(github.com/charmbracelet/bubbletea)
#   - golang(github.com/charmbracelet/glamour)
#   - golang(github.com/charmbracelet/lipgloss)
#   - golang(github.com/charmbracelet/log)
#   - golang(github.com/charmbracelet/x/ansi)
#   - golang(github.com/charmbracelet/x/editor)
#   - golang(github.com/charmbracelet/x/term)
#   - golang(github.com/dlclark/regexp2)
#   - golang(github.com/dustin/go-humanize)
#   - golang(github.com/erikgeiser/coninput)
#   - golang(github.com/go-logfmt/logfmt)
#   - golang(github.com/lucasb-eyer/go-colorful)
#   - golang(github.com/Masterminds/semver/v3)
#   - golang(github.com/mattn/go-isatty)
#   - golang(github.com/mattn/go-localereader)
#   - golang(github.com/mattn/go-runewidth)
#   - golang(github.com/muesli/ansi)
#   - golang(github.com/muesli/cancelreader)
#   - golang(github.com/muesli/mango)
#   - golang(github.com/muesli/reflow)
#   - golang(github.com/muesli/roff)
#   - golang(github.com/muesli/termenv)
#   - golang(github.com/rivo/uniseg)
#   - golang(github.com/sahilm/fuzzy)
#   - golang(github.com/yuin/goldmark)
#   - golang(github.com/yuin/goldmark-emoji)
# MIT AND OFL-1.1:
#   - golang(github.com/alecthomas/chroma/v2)
License:        BSD-3-Clause AND MIT AND OFL-1.1
URL:            https://github.com/charmbracelet/gum
Source0:        %{url}/archive/v%{version}/gum-%{version}.tar.gz

# see create-vendor-tarball.sh for how to create this
Source1:        gum-%{version}-vendor.tar.gz

# script that creates vendor tarball
Source100:      create-vendor-tarball.sh

BuildRequires:  go-rpm-macros
ExclusiveArch:  %{golang_arches_future}

Provides:       bundled(golang(github.com/alecthomas/chroma/v2)) = 2.14.0
Provides:       bundled(golang(github.com/alecthomas/kong)) = 1.6.1
Provides:       bundled(golang(github.com/alecthomas/mango-kong)) = 0.1.0
Provides:       bundled(golang(github.com/atotto/clipboard)) = 0.1.4
Provides:       bundled(golang(github.com/aymanbagabas/go-osc52/v2)) = 2.0.1
Provides:       bundled(golang(github.com/aymerick/douceur)) = 0.2.0
Provides:       bundled(golang(github.com/charmbracelet/bubbles)) = 0.20.0
Provides:       bundled(golang(github.com/charmbracelet/bubbletea)) = e0515bc
Provides:       bundled(golang(github.com/charmbracelet/glamour)) = 0.8.0
Provides:       bundled(golang(github.com/charmbracelet/lipgloss)) = ecc1bd0
Provides:       bundled(golang(github.com/charmbracelet/log)) = 0.4.0
Provides:       bundled(golang(github.com/charmbracelet/x/ansi)) = 0.8.0
Provides:       bundled(golang(github.com/charmbracelet/x/editor)) = 0.1.0
Provides:       bundled(golang(github.com/charmbracelet/x/term)) = 0.2.1
Provides:       bundled(golang(github.com/dlclark/regexp2)) = 1.11.0
Provides:       bundled(golang(github.com/dustin/go-humanize)) = 1.0.1
Provides:       bundled(golang(github.com/erikgeiser/coninput)) = 1c3628e
Provides:       bundled(golang(github.com/go-logfmt/logfmt)) = 0.6.0
Provides:       bundled(golang(github.com/gorilla/css)) = 1.0.1
Provides:       bundled(golang(github.com/lucasb-eyer/go-colorful)) = 1.2.0
Provides:       bundled(golang(github.com/Masterminds/semver/v3)) = 3.3.1
Provides:       bundled(golang(github.com/mattn/go-isatty)) = 0.0.20
Provides:       bundled(golang(github.com/mattn/go-localereader)) = 0.0.1
Provides:       bundled(golang(github.com/mattn/go-runewidth)) = 0.0.16
Provides:       bundled(golang(github.com/microcosm-cc/bluemonday)) = 1.0.27
Provides:       bundled(golang(github.com/muesli/ansi)) = 276c624
Provides:       bundled(golang(github.com/muesli/cancelreader)) = 0.2.2
Provides:       bundled(golang(github.com/muesli/mango)) = 0.2.0
Provides:       bundled(golang(github.com/muesli/reflow)) = 0.3.0
Provides:       bundled(golang(github.com/muesli/roff)) = 0.1.0
Provides:       bundled(golang(github.com/muesli/termenv)) = 0d230cb
Provides:       bundled(golang(github.com/rivo/uniseg)) = 0.4.7
Provides:       bundled(golang(github.com/sahilm/fuzzy)) = 0.1.1
Provides:       bundled(golang(github.com/yuin/goldmark)) = 1.7.4
Provides:       bundled(golang(github.com/yuin/goldmark-emoji)) = 1.0.4
Provides:       bundled(golang(golang.org/x/exp)) = 7f521ea
Provides:       bundled(golang(golang.org/x/net)) = 0.33.0
Provides:       bundled(golang(golang.org/x/sync)) = 0.10.0
Provides:       bundled(golang(golang.org/x/sys)) = 0.28.0
Provides:       bundled(golang(golang.org/x/term)) = 0.27.0
Provides:       bundled(golang(golang.org/x/text)) = 0.21.0


%description
A tool for glamorous shell scripts. Leverage the power of Bubbles and Lip Gloss
in your scripts and aliases without writing any Go code!


%prep
%autosetup -a 1
mkdir -p src/$(dirname %{goipath})
ln -s $PWD src/%{goipath}

# set the program version
sed -e '/Version = / s/""/"%{version}"/' -i main.go


%build
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
