%define goipath github.com/charmbracelet/glow

Name:           glow
Version:        2.1.0
Release:        %autorelease
Summary:        Terminal based markdown reader
URL:            https://github.com/charmbracelet/glow

# main source code is MIT
# Apache-2.0:
#   github.com/inconshreveable/mousetrap
#   github.com/spf13/afero
#   github.com/spf13/cobra
#   gopkg.in/ini.v1
# BSD-2-Clause:
#   github.com/magiconair/properties
# BSD-3-Clause:
#   github.com/atotto/clipboard
#   github.com/fsnotify/fsnotify
#   github.com/gorilla/css
#   github.com/microcosm-cc/bluemonday
#   github.com/sagikazarmark/slog-shim
#   github.com/spf13/pflag
#   golang.org/x/exp
#   golang.org/x/net
#   golang.org/x/sync
#   golang.org/x/sys
#   golang.org/x/term
#   golang.org/x/text
# MIT:
#   github.com/aymanbagabas/go-osc52/v2
#   github.com/aymerick/douceur
#   github.com/caarlos0/env/v11
#   github.com/charmbracelet/bubbles
#   github.com/charmbracelet/bubbletea
#   github.com/charmbracelet/glamour
#   github.com/charmbracelet/lipgloss
#   github.com/charmbracelet/log
#   github.com/charmbracelet/x/ansi
#   github.com/charmbracelet/x/editor
#   github.com/charmbracelet/x/term
#   github.com/dlclark/regexp2
#   github.com/dustin/go-humanize
#   github.com/erikgeiser/coninput
#   github.com/go-logfmt/logfmt
#   github.com/lucasb-eyer/go-colorful
#   github.com/mattn/go-isatty
#   github.com/mattn/go-localereader
#   github.com/mattn/go-runewidth
#   github.com/mitchellh/go-homedir
#   github.com/mitchellh/mapstructure
#   github.com/muesli/ansi
#   github.com/muesli/cancelreader
#   github.com/muesli/gitcha
#   github.com/muesli/go-app-paths
#   github.com/muesli/mango
#   github.com/muesli/mango-cobra
#   github.com/muesli/mango-pflag
#   github.com/muesli/reflow
#   github.com/muesli/roff
#   github.com/muesli/termenv
#   github.com/pelletier/go-toml/v2
#   github.com/rivo/uniseg
#   github.com/sabhiram/go-gitignore
#   github.com/sagikazarmark/locafero
#   github.com/sahilm/fuzzy
#   github.com/sourcegraph/conc
#   github.com/spf13/cast
#   github.com/spf13/viper
#   github.com/subosito/gotenv
#   github.com/yuin/goldmark
#   github.com/yuin/goldmark-emoji
#   go.uber.org/atomic
#   go.uber.org/multierr
# MPL-2.0:
#   github.com/hashicorp/hcl
# Apache-2.0 AND MIT
#   gopkg.in/yaml.v3
# MIT AND OFL-1.1:
#   github.com/alecthomas/chroma/v2
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND MIT AND MPL-2.0 AND OFL-1.1

Source0:        %{url}/archive/v%{version}/glow-%{version}.tar.gz
Source1:        glow-%{version}-vendor.tar.gz
Source2:        create-vendor-tarball.sh

BuildRequires:  go-rpm-macros
ExclusiveArch:  %{golang_arches_future}
# https://github.com/charmbracelet/glow/commit/546b6287d80af885cc3069de895083af36aa91e3
BuildRequires:  golang >= 1.23.6

Provides:       bundled(golang(github.com/alecthomas/chroma/v2)) = 2.14.0
Provides:       bundled(golang(github.com/atotto/clipboard)) = 0.1.4
Provides:       bundled(golang(github.com/aymanbagabas/go-osc52/v2)) = 2.0.1
Provides:       bundled(golang(github.com/aymerick/douceur)) = 0.2.0
Provides:       bundled(golang(github.com/caarlos0/env/v11)) = 11.3.1
Provides:       bundled(golang(github.com/charmbracelet/bubbles)) = 0.20.0
Provides:       bundled(golang(github.com/charmbracelet/bubbletea)) = 1.3.3
Provides:       bundled(golang(github.com/charmbracelet/glamour)) = 0.8.0
Provides:       bundled(golang(github.com/charmbracelet/lipgloss)) = 1.0.0
Provides:       bundled(golang(github.com/charmbracelet/log)) = 0.4.0
Provides:       bundled(golang(github.com/charmbracelet/x/ansi)) = 0.8.0
Provides:       bundled(golang(github.com/charmbracelet/x/editor)) = 0.1.0
Provides:       bundled(golang(github.com/charmbracelet/x/term)) = 0.2.1
Provides:       bundled(golang(github.com/dlclark/regexp2)) = 1.11.0
Provides:       bundled(golang(github.com/dustin/go-humanize)) = 1.0.1
Provides:       bundled(golang(github.com/erikgeiser/coninput)) = 1c3628e
Provides:       bundled(golang(github.com/fsnotify/fsnotify)) = 1.8.0
Provides:       bundled(golang(github.com/go-logfmt/logfmt)) = 0.6.0
Provides:       bundled(golang(github.com/gorilla/css)) = 1.0.1
Provides:       bundled(golang(github.com/hashicorp/hcl)) = 1.0.0
Provides:       bundled(golang(github.com/inconshreveable/mousetrap)) = 1.1.0
Provides:       bundled(golang(github.com/lucasb-eyer/go-colorful)) = 1.2.0
Provides:       bundled(golang(github.com/magiconair/properties)) = 1.8.7
Provides:       bundled(golang(github.com/mattn/go-isatty)) = 0.0.20
Provides:       bundled(golang(github.com/mattn/go-localereader)) = 0.0.1
Provides:       bundled(golang(github.com/mattn/go-runewidth)) = 0.0.16
Provides:       bundled(golang(github.com/microcosm-cc/bluemonday)) = 1.0.27
Provides:       bundled(golang(github.com/mitchellh/go-homedir)) = 1.1.0
Provides:       bundled(golang(github.com/mitchellh/mapstructure)) = 1.5.0
Provides:       bundled(golang(github.com/muesli/ansi)) = 276c624
Provides:       bundled(golang(github.com/muesli/cancelreader)) = 0.2.2
Provides:       bundled(golang(github.com/muesli/gitcha)) = 0.3.0
Provides:       bundled(golang(github.com/muesli/go-app-paths)) = 0.2.2
Provides:       bundled(golang(github.com/muesli/mango)) = 0.1.0
Provides:       bundled(golang(github.com/muesli/mango-cobra)) = 1.2.0
Provides:       bundled(golang(github.com/muesli/mango-pflag)) = 0.1.0
Provides:       bundled(golang(github.com/muesli/reflow)) = 0.3.0
Provides:       bundled(golang(github.com/muesli/roff)) = 0.1.0
Provides:       bundled(golang(github.com/muesli/termenv)) = 0.16.0
Provides:       bundled(golang(github.com/pelletier/go-toml/v2)) = 2.2.2
Provides:       bundled(golang(github.com/rivo/uniseg)) = 0.4.7
Provides:       bundled(golang(github.com/sabhiram/go-gitignore)) = d310757
Provides:       bundled(golang(github.com/sagikazarmark/locafero)) = 0.4.0
Provides:       bundled(golang(github.com/sagikazarmark/slog-shim)) = 0.1.0
Provides:       bundled(golang(github.com/sahilm/fuzzy)) = 0.1.1
Provides:       bundled(golang(github.com/sourcegraph/conc)) = 0.3.0
Provides:       bundled(golang(github.com/spf13/afero)) = 1.11.0
Provides:       bundled(golang(github.com/spf13/cast)) = 1.6.0
Provides:       bundled(golang(github.com/spf13/cobra)) = 1.9.1
Provides:       bundled(golang(github.com/spf13/pflag)) = 1.0.6
Provides:       bundled(golang(github.com/spf13/viper)) = 1.19.0
Provides:       bundled(golang(github.com/subosito/gotenv)) = 1.6.0
Provides:       bundled(golang(github.com/yuin/goldmark)) = 1.7.4
Provides:       bundled(golang(github.com/yuin/goldmark-emoji)) = 1.0.3
Provides:       bundled(golang(go.uber.org/atomic)) = 1.9.0
Provides:       bundled(golang(go.uber.org/multierr)) = 1.9.0
Provides:       bundled(golang(golang.org/x/exp)) = fc45aab
Provides:       bundled(golang(golang.org/x/net)) = 0.27.0
Provides:       bundled(golang(golang.org/x/sync)) = 0.11.0
Provides:       bundled(golang(golang.org/x/sys)) = 0.30.0
Provides:       bundled(golang(golang.org/x/term)) = 0.29.0
Provides:       bundled(golang(golang.org/x/text)) = 0.22.0
Provides:       bundled(golang(gopkg.in/ini.v1)) = 1.67.0
Provides:       bundled(golang(gopkg.in/yaml.v3)) = 3.0.1


%description
Glow is a terminal based markdown reader designed from the ground up to bring
out the beauty—and power—of the CLI.  Use it to discover markdown files, read
documentation directly on the command line.  Glow will find local markdown
files in subdirectories or a local Git repository.


%prep
%autosetup -p 1 -a 1
mkdir -p src/$(dirname %{goipath})
ln -s $PWD src/%{goipath}

# set the program version
sed -e '/Version = / s/""/"v%{version}"/' -i main.go


%build
export GOPATH=$PWD
%gobuild -o bin/glow %{goipath}


%install
# command
install -D -p -m 0755 -t %{buildroot}%{_bindir} bin/glow

# man pages
install -d -m 0755 %{buildroot}%{_mandir}/man1
./bin/glow man > %{buildroot}%{_mandir}/man1/glow.1

# shell completions
install -d -m 0755 %{buildroot}%{bash_completions_dir}
./bin/glow completion bash > %{buildroot}%{bash_completions_dir}/glow
install -d -m 0755 %{buildroot}%{zsh_completions_dir}
./bin/glow completion zsh > %{buildroot}%{zsh_completions_dir}/_glow
install -d -m 0755 %{buildroot}%{fish_completions_dir}
./bin/glow completion fish > %{buildroot}%{fish_completions_dir}/glow.fish


%check
# ensure that the version was embedded correctly
[[ "$(./bin/glow --version)" == "glow version v%{version}" ]] || exit 1

# run the upstream tests
export GOPATH=$PWD
cd src/%{goipath}
%gotest ./...


%files
%license LICENSE
%{_bindir}/glow
%{_mandir}/man1/glow.1*
%{bash_completions_dir}/glow
%{zsh_completions_dir}/_glow
%{fish_completions_dir}/glow.fish


%changelog
%autochangelog
