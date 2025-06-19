%define goipath github.com/charmbracelet/vhs

Name:           vhs
Version:        0.10.0
Release:        %autorelease
Summary:        Your CLI home video recorder
URL:            https://github.com/charmbracelet/vhs

# main source code is MIT
# Apache-2.0:
#   github.com/inconshreveable/mousetrap
#   github.com/spf13/cobra
# BSD-3-Clause:
#   github.com/atotto/clipboard
#   github.com/charmbracelet/ssh
#   github.com/gorilla/css
#   github.com/microcosm-cc/bluemonday
#   github.com/spf13/pflag
#   golang.org/x/crypto
#   golang.org/x/exp
#   golang.org/x/net
#   golang.org/x/sync
#   golang.org/x/sys
#   golang.org/x/term
#   golang.org/x/text
# MIT:
#   github.com/agnivade/levenshtein
#   github.com/anmitsu/go-shlex
#   github.com/aymanbagabas/go-osc52/v2
#   github.com/aymerick/douceur
#   github.com/caarlos0/env/v11
#   github.com/charmbracelet/bubbletea
#   github.com/charmbracelet/colorprofile
#   github.com/charmbracelet/glamour
#   github.com/charmbracelet/keygen
#   github.com/charmbracelet/lipgloss
#   github.com/charmbracelet/log
#   github.com/charmbracelet/wish
#   github.com/charmbracelet/x/ansi
#   github.com/charmbracelet/x/cellbuf
#   github.com/charmbracelet/x/conpty
#   github.com/charmbracelet/x/errors
#   github.com/charmbracelet/x/exp/slice
#   github.com/charmbracelet/x/term
#   github.com/charmbracelet/x/termios
#   github.com/creack/pty
#   github.com/dlclark/regexp2
#   github.com/erikgeiser/coninput
#   github.com/go-logfmt/logfmt
#   github.com/go-rod/rod
#   github.com/lucasb-eyer/go-colorful
#   github.com/mattn/go-isatty
#   github.com/mattn/go-localereader
#   github.com/mattn/go-runewidth
#   github.com/mitchellh/go-homedir
#   github.com/muesli/ansi
#   github.com/muesli/cancelreader
#   github.com/muesli/go-app-paths
#   github.com/muesli/mango
#   github.com/muesli/mango-cobra
#   github.com/muesli/mango-pflag
#   github.com/muesli/reflow
#   github.com/muesli/roff
#   github.com/muesli/termenv
#   github.com/rivo/uniseg
#   github.com/xo/terminfo
#   github.com/ysmood/fetchup
#   github.com/ysmood/goob
#   github.com/ysmood/got
#   github.com/ysmood/gson
#   github.com/ysmood/leakless
#   github.com/yuin/goldmark
#   github.com/yuin/goldmark-emoji
# MPL-2.0:
#   github.com/hashicorp/go-version
# MIT AND OFL-1.1:
#   github.com/alecthomas/chroma/v2
License:        Apache-2.0 AND BSD-3-Clause AND MIT AND MPL-2.0 AND OFL-1.1

Source0:        %{url}/archive/v%{version}/vhs-%{version}.tar.gz
Source1:        vhs-%{version}-vendor.tar.gz
Source2:        create-vendor-tarball.sh

BuildRequires:  go-rpm-macros
ExclusiveArch:  %{golang_arches_future}
# https://github.com/charmbracelet/vhs/blob/v0.10.0/go.mod#L3
BuildRequires:  golang >= 1.24.1

Provides:       bundled(golang(github.com/agnivade/levenshtein)) = 1.2.1
Provides:       bundled(golang(github.com/alecthomas/chroma/v2)) = 2.14.0
Provides:       bundled(golang(github.com/anmitsu/go-shlex)) = 38f4b40
Provides:       bundled(golang(github.com/atotto/clipboard)) = 0.1.4
Provides:       bundled(golang(github.com/aymanbagabas/go-osc52/v2)) = 2.0.1
Provides:       bundled(golang(github.com/aymerick/douceur)) = 0.2.0
Provides:       bundled(golang(github.com/caarlos0/env/v11)) = 11.3.1
Provides:       bundled(golang(github.com/charmbracelet/bubbletea)) = 1.3.4
Provides:       bundled(golang(github.com/charmbracelet/colorprofile)) = f60798e
Provides:       bundled(golang(github.com/charmbracelet/glamour)) = 0.10.0
Provides:       bundled(golang(github.com/charmbracelet/keygen)) = 0.5.3
Provides:       bundled(golang(github.com/charmbracelet/lipgloss)) = 76690c6
Provides:       bundled(golang(github.com/charmbracelet/log)) = 0.4.1
Provides:       bundled(golang(github.com/charmbracelet/ssh)) = 98fd5ae
Provides:       bundled(golang(github.com/charmbracelet/wish)) = 1.4.7
Provides:       bundled(golang(github.com/charmbracelet/x/ansi)) = 0.8.0
Provides:       bundled(golang(github.com/charmbracelet/x/cellbuf)) = 0.0.13
Provides:       bundled(golang(github.com/charmbracelet/x/conpty)) = 0.1.0
Provides:       bundled(golang(github.com/charmbracelet/x/errors)) = e8e43e1
Provides:       bundled(golang(github.com/charmbracelet/x/exp/slice)) = 2fdc977
Provides:       bundled(golang(github.com/charmbracelet/x/term)) = 0.2.1
Provides:       bundled(golang(github.com/charmbracelet/x/termios)) = 0.1.0
Provides:       bundled(golang(github.com/creack/pty)) = 1.1.24
Provides:       bundled(golang(github.com/dlclark/regexp2)) = 1.11.0
Provides:       bundled(golang(github.com/erikgeiser/coninput)) = 1c3628e
Provides:       bundled(golang(github.com/go-logfmt/logfmt)) = 0.6.0
Provides:       bundled(golang(github.com/go-rod/rod)) = 0.116.2
Provides:       bundled(golang(github.com/gorilla/css)) = 1.0.1
Provides:       bundled(golang(github.com/hashicorp/go-version)) = 1.7.0
Provides:       bundled(golang(github.com/inconshreveable/mousetrap)) = 1.1.0
Provides:       bundled(golang(github.com/lucasb-eyer/go-colorful)) = 1.2.0
Provides:       bundled(golang(github.com/mattn/go-isatty)) = 0.0.20
Provides:       bundled(golang(github.com/mattn/go-localereader)) = 0.0.1
Provides:       bundled(golang(github.com/mattn/go-runewidth)) = 0.0.16
Provides:       bundled(golang(github.com/microcosm-cc/bluemonday)) = 1.0.27
Provides:       bundled(golang(github.com/mitchellh/go-homedir)) = 1.1.0
Provides:       bundled(golang(github.com/muesli/ansi)) = 276c624
Provides:       bundled(golang(github.com/muesli/cancelreader)) = 0.2.2
Provides:       bundled(golang(github.com/muesli/go-app-paths)) = 0.2.2
Provides:       bundled(golang(github.com/muesli/mango)) = 0.2.0
Provides:       bundled(golang(github.com/muesli/mango-cobra)) = 1.2.0
Provides:       bundled(golang(github.com/muesli/mango-pflag)) = 0.1.0
Provides:       bundled(golang(github.com/muesli/reflow)) = 0.3.0
Provides:       bundled(golang(github.com/muesli/roff)) = 0.1.0
Provides:       bundled(golang(github.com/muesli/termenv)) = 0.16.0
Provides:       bundled(golang(github.com/rivo/uniseg)) = 0.4.7
Provides:       bundled(golang(github.com/spf13/cobra)) = 1.9.1
Provides:       bundled(golang(github.com/spf13/pflag)) = 1.0.6
Provides:       bundled(golang(github.com/xo/terminfo)) = abceb7e
Provides:       bundled(golang(github.com/ysmood/fetchup)) = 0.2.3
Provides:       bundled(golang(github.com/ysmood/goob)) = 0.4.0
Provides:       bundled(golang(github.com/ysmood/got)) = 0.40.0
Provides:       bundled(golang(github.com/ysmood/gson)) = 0.7.3
Provides:       bundled(golang(github.com/ysmood/leakless)) = 0.9.0
Provides:       bundled(golang(github.com/yuin/goldmark)) = 1.7.8
Provides:       bundled(golang(github.com/yuin/goldmark-emoji)) = 1.0.5
Provides:       bundled(golang(golang.org/x/crypto)) = 0.39.0
Provides:       bundled(golang(golang.org/x/exp)) = 8a7402a
Provides:       bundled(golang(golang.org/x/net)) = 0.39.0
Provides:       bundled(golang(golang.org/x/sync)) = 0.15.0
Provides:       bundled(golang(golang.org/x/sys)) = 0.33.0
Provides:       bundled(golang(golang.org/x/term)) = 0.32.0
Provides:       bundled(golang(golang.org/x/text)) = 0.26.0

Requires:       ttyd
Requires:       ffmpeg-free


%description
Write terminal GIFs as code for integration testing and demoing your CLI tools.


%prep
%autosetup -p 1 -a 1
mkdir -p src/$(dirname %{goipath})
ln -s $PWD src/%{goipath}


%build
export GOPATH=$PWD
export LDFLAGS="-X main.Version=v%{version}"
%gobuild -o bin/vhs %{goipath}


%install
# command
install -D -p -m 0755 -t %{buildroot}%{_bindir} bin/vhs

# man pages
install -d -m 0755 %{buildroot}%{_mandir}/man1
./bin/vhs man > %{buildroot}%{_mandir}/man1/vhs.1

# shell completions
install -d -m 0755 %{buildroot}%{bash_completions_dir}
./bin/vhs completion bash > %{buildroot}%{bash_completions_dir}/vhs
install -d -m 0755 %{buildroot}%{zsh_completions_dir}
./bin/vhs completion zsh > %{buildroot}%{zsh_completions_dir}/_vhs
install -d -m 0755 %{buildroot}%{fish_completions_dir}
./bin/vhs completion fish > %{buildroot}%{fish_completions_dir}/vhs.fish


%check
# ensure that the version was embedded correctly
[[ "$(./bin/vhs --version)" == "vhs version v%{version}" ]] || exit 1

# run the upstream tests
export GOPATH=$PWD
cd src/%{goipath}
%gotest ./...


%files
%license LICENSE
%{_bindir}/vhs
%{_mandir}/man1/vhs.1*
%{bash_completions_dir}/vhs
%{zsh_completions_dir}/_vhs
%{fish_completions_dir}/vhs.fish


%changelog
%autochangelog
