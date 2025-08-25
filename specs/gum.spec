%define goipath github.com/charmbracelet/gum

Name:           gum
Version:        0.16.2
Release:        %autorelease
Summary:        Tool for glamorous shell scripts
URL:            https://github.com/charmbracelet/gum

# main source code is MIT
# see comments above bundled provides for a breakdown of the rest
License:        BSD-3-Clause AND MIT AND OFL-1.1

Source0:        %{url}/archive/v%{version}/gum-%{version}.tar.gz
Source1:        gum-%{version}-vendor.tar.gz
Source2:        create-vendor-tarball.sh

BuildRequires:  go-rpm-macros
ExclusiveArch:  %{golang_arches_future}
# https://github.com/charmbracelet/gum/commit/2e321f57e245147fe55ee58ef9c046db91b76e17
BuildRequires:  golang >= 1.23

# BSD-3-Clause:
Provides:       bundled(golang(github.com/atotto/clipboard)) = 0.1.4
Provides:       bundled(golang(github.com/gorilla/css)) = 1.0.1
Provides:       bundled(golang(github.com/microcosm-cc/bluemonday)) = 1.0.27
Provides:       bundled(golang(golang.org/x/exp)) = 7f521ea
Provides:       bundled(golang(golang.org/x/net)) = 0.40.0
Provides:       bundled(golang(golang.org/x/sync)) = 0.15.0
Provides:       bundled(golang(golang.org/x/sys)) = 0.33.0
Provides:       bundled(golang(golang.org/x/term)) = 0.32.0
Provides:       bundled(golang(golang.org/x/text)) = 0.26.0

# MIT:
Provides:       bundled(golang(github.com/Masterminds/semver/v3)) = 3.3.1
Provides:       bundled(golang(github.com/alecthomas/kong)) = 1.11.0
Provides:       bundled(golang(github.com/alecthomas/mango-kong)) = 0.1.0
Provides:       bundled(golang(github.com/aymanbagabas/go-osc52/v2)) = 2.0.1
Provides:       bundled(golang(github.com/aymerick/douceur)) = 0.2.0
Provides:       bundled(golang(github.com/charmbracelet/bubbles)) = 0.21.0
Provides:       bundled(golang(github.com/charmbracelet/bubbletea)) = 1.3.5
Provides:       bundled(golang(github.com/charmbracelet/colorprofile)) = f60798e
Provides:       bundled(golang(github.com/charmbracelet/glamour)) = 0.10.0
Provides:       bundled(golang(github.com/charmbracelet/lipgloss)) = 76690c6
Provides:       bundled(golang(github.com/charmbracelet/log)) = 0.4.2
Provides:       bundled(golang(github.com/charmbracelet/x/ansi)) = 0.9.3
Provides:       bundled(golang(github.com/charmbracelet/x/cellbuf)) = 0.0.13
Provides:       bundled(golang(github.com/charmbracelet/x/conpty)) = 0.1.0
Provides:       bundled(golang(github.com/charmbracelet/x/editor)) = 0.1.0
Provides:       bundled(golang(github.com/charmbracelet/x/errors)) = e8d8b6e
Provides:       bundled(golang(github.com/charmbracelet/x/exp/slice)) = 2fdc977
Provides:       bundled(golang(github.com/charmbracelet/x/term)) = 0.2.1
Provides:       bundled(golang(github.com/charmbracelet/x/termios)) = 0.1.1
Provides:       bundled(golang(github.com/charmbracelet/x/xpty)) = 0.1.2
Provides:       bundled(golang(github.com/creack/pty)) = 1.1.24
Provides:       bundled(golang(github.com/dlclark/regexp2)) = 1.11.0
Provides:       bundled(golang(github.com/dustin/go-humanize)) = 1.0.1
Provides:       bundled(golang(github.com/erikgeiser/coninput)) = 1c3628e
Provides:       bundled(golang(github.com/go-logfmt/logfmt)) = 0.6.0
Provides:       bundled(golang(github.com/lucasb-eyer/go-colorful)) = 1.2.0
Provides:       bundled(golang(github.com/mattn/go-isatty)) = 0.0.20
Provides:       bundled(golang(github.com/mattn/go-localereader)) = 0.0.1
Provides:       bundled(golang(github.com/mattn/go-runewidth)) = 0.0.16
Provides:       bundled(golang(github.com/muesli/ansi)) = 276c624
Provides:       bundled(golang(github.com/muesli/cancelreader)) = 0.2.2
Provides:       bundled(golang(github.com/muesli/mango)) = 0.2.0
Provides:       bundled(golang(github.com/muesli/reflow)) = 0.3.0
Provides:       bundled(golang(github.com/muesli/roff)) = 0.1.0
Provides:       bundled(golang(github.com/muesli/termenv)) = 0.16.0
Provides:       bundled(golang(github.com/rivo/uniseg)) = 0.4.7
Provides:       bundled(golang(github.com/sahilm/fuzzy)) = 0.1.1
Provides:       bundled(golang(github.com/xo/terminfo)) = abceb7e
Provides:       bundled(golang(github.com/yuin/goldmark)) = 1.7.8
Provides:       bundled(golang(github.com/yuin/goldmark-emoji)) = 1.0.5

# MIT AND OFL-1.1:
Provides:       bundled(golang(github.com/alecthomas/chroma/v2)) = 2.14.0


%description
A tool for glamorous shell scripts. Leverage the power of Bubbles and Lip Gloss
in your scripts and aliases without writing any Go code!


%prep
%autosetup -a 1
mkdir -p src/$(dirname %{goipath})
ln -s $PWD src/%{goipath}

# set the program version
sed -e '/Version = / s/""/"v%{version}"/' -i main.go


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
[[ "$(./bin/gum --version)" == "gum version v%{version}" ]] || exit 1

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
