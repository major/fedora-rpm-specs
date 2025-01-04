%global goipath github.com/charmbracelet/glow

Name:           glow
Version:        2.0.0
Release:        %autorelease
Summary:        Terminal based markdown reader
# main source code is MIT
# see comments above provides tags for bundled license breakdown
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND MIT AND MPL-2.0 AND OFL-1.1
URL:            https://github.com/charmbracelet/glow

BuildRequires:  go-rpm-macros
ExclusiveArch:  %{golang_arches_future}

# see create-vendor-tarball.sh for how to create this
Source0:        glow-%{version}-vendored.tar.gz

# Script that creates vendor tarball
Source100:      create-vendor-tarball.sh

# https://github.com/charmbracelet/glow/pull/661
Patch:          0001-test-skip-networked-tests-if-no-connection-661.patch

BuildRequires:  golang

# MIT AND OFL-1.1
Provides:       bundled(golang(github.com/alecthomas/chroma/v2)) = 2.14.0
# BSD-3-Clause
Provides:       bundled(golang(github.com/atotto/clipboard)) = 0.1.4
# MIT
Provides:       bundled(golang(github.com/aymanbagabas/go-osc52/v2)) = 2.0.1
# MIT
Provides:       bundled(golang(github.com/aymerick/douceur)) = 0.2.0
# MIT
Provides:       bundled(golang(github.com/caarlos0/env/v11)) = 11.0.1
# MIT
Provides:       bundled(golang(github.com/charmbracelet/bubbles)) = 0.18.0
# MIT
Provides:       bundled(golang(github.com/charmbracelet/bubbletea)) = ea13ffb
# MIT
Provides:       bundled(golang(github.com/charmbracelet/glamour)) = 0.8.0
# MIT
Provides:       bundled(golang(github.com/charmbracelet/lipgloss)) = 87dd58d
# MIT
Provides:       bundled(golang(github.com/charmbracelet/log)) = 0.4.0
# MIT
Provides:       bundled(golang(github.com/charmbracelet/x/ansi)) = 0.1.4
# MIT
Provides:       bundled(golang(github.com/charmbracelet/x/editor)) = 2627ec1
# MIT
Provides:       bundled(golang(github.com/charmbracelet/x/input)) = 0.1.2
# MIT
Provides:       bundled(golang(github.com/charmbracelet/x/term)) = 0.1.1
# MIT
Provides:       bundled(golang(github.com/charmbracelet/x/windows)) = 0.1.2
# MIT
Provides:       bundled(golang(github.com/dlclark/regexp2)) = 1.11.0
# MIT
Provides:       bundled(golang(github.com/dustin/go-humanize)) = 1.0.1
# MIT
Provides:       bundled(golang(github.com/erikgeiser/coninput)) = 1c3628e
# BSD-3-Clause
Provides:       bundled(golang(github.com/fsnotify/fsnotify)) = 1.6.0
# MIT
Provides:       bundled(golang(github.com/go-logfmt/logfmt)) = 0.6.0
# BSD-3-Clause
Provides:       bundled(golang(github.com/gorilla/css)) = 1.0.1
# MPL-2.0
Provides:       bundled(golang(github.com/hashicorp/hcl)) = 1.0.0
# Apache-2.0
Provides:       bundled(golang(github.com/inconshreveable/mousetrap)) = 1.1.0
# MIT
Provides:       bundled(golang(github.com/lucasb-eyer/go-colorful)) = 1.2.0
# BSD-2-Clause
Provides:       bundled(golang(github.com/magiconair/properties)) = 1.8.7
# MIT
Provides:       bundled(golang(github.com/mattn/go-isatty)) = 0.0.20
# MIT
Provides:       bundled(golang(github.com/mattn/go-localereader)) = 0.0.1
# MIT
Provides:       bundled(golang(github.com/mattn/go-runewidth)) = 0.0.15
# BSD-3-Clause
Provides:       bundled(golang(github.com/microcosm-cc/bluemonday)) = 1.0.27
# MIT
Provides:       bundled(golang(github.com/mitchellh/go-homedir)) = 1.1.0
# MIT
Provides:       bundled(golang(github.com/mitchellh/mapstructure)) = 1.5.0
# MIT
Provides:       bundled(golang(github.com/muesli/ansi)) = 276c624
# MIT
Provides:       bundled(golang(github.com/muesli/cancelreader)) = 0.2.2
# MIT
Provides:       bundled(golang(github.com/muesli/gitcha)) = 0.3.0
# MIT
Provides:       bundled(golang(github.com/muesli/go-app-paths)) = 0.2.2
# MIT
Provides:       bundled(golang(github.com/muesli/mango)) = 0.1.0
# MIT
Provides:       bundled(golang(github.com/muesli/mango-cobra)) = 1.2.0
# MIT
Provides:       bundled(golang(github.com/muesli/mango-pflag)) = 0.1.0
# MIT
Provides:       bundled(golang(github.com/muesli/reflow)) = 0.3.0
# MIT
Provides:       bundled(golang(github.com/muesli/roff)) = 0.1.0
# MIT
Provides:       bundled(golang(github.com/muesli/termenv)) = 98d742f
# MIT
Provides:       bundled(golang(github.com/pelletier/go-toml/v2)) = 2.0.6
# MIT
Provides:       bundled(golang(github.com/rivo/uniseg)) = 0.4.7
# MIT
Provides:       bundled(golang(github.com/sabhiram/go-gitignore)) = d310757
# MIT
Provides:       bundled(golang(github.com/sahilm/fuzzy)) = 0.1.1
# Apache-2.0
Provides:       bundled(golang(github.com/spf13/afero)) = 1.9.3
# MIT
Provides:       bundled(golang(github.com/spf13/cast)) = 1.5.0
# Apache-2.0
Provides:       bundled(golang(github.com/spf13/cobra)) = 1.7.0
# MIT
Provides:       bundled(golang(github.com/spf13/jwalterweatherman)) = 1.1.0
# BSD-3-Clause
Provides:       bundled(golang(github.com/spf13/pflag)) = 1.0.5
# MIT
Provides:       bundled(golang(github.com/spf13/viper)) = 1.15.0
# MIT
Provides:       bundled(golang(github.com/subosito/gotenv)) = 1.4.2
# MIT
Provides:       bundled(golang(github.com/xo/terminfo)) = abceb7e
# MIT
Provides:       bundled(golang(github.com/yuin/goldmark)) = 1.7.4
# MIT
Provides:       bundled(golang(github.com/yuin/goldmark-emoji)) = 1.0.3
# BSD-3-Clause
Provides:       bundled(golang(golang.org/x/exp)) = fc45aab
# BSD-3-Clause
Provides:       bundled(golang(golang.org/x/net)) = 0.27.0
# BSD-3-Clause
Provides:       bundled(golang(golang.org/x/sync)) = 0.7.0
# BSD-3-Clause
Provides:       bundled(golang(golang.org/x/sys)) = 0.22.0
# BSD-3-Clause
Provides:       bundled(golang(golang.org/x/term)) = 0.22.0
# BSD-3-Clause
Provides:       bundled(golang(golang.org/x/text)) = 0.16.0
# Apache-2.0
Provides:       bundled(golang(gopkg.in/ini.v1)) = 1.67.0
# Apache-2.0 AND MIT
Provides:       bundled(golang(gopkg.in/yaml.v3)) = 3.0.1


%description
Glow is a terminal based markdown reader designed from the ground up to bring
out the beauty—and power—of the CLI.  Use it to discover markdown files, read
documentation directly on the command line.  Glow will find local markdown
files in subdirectories or a local Git repository.


%prep
%autosetup -p 1
mkdir -p src/$(dirname %{goipath})
ln -s $PWD src/%{goipath}

# set the program version
sed -e '/Version = / s/""/"%{version}"/' -i main.go


%build
export GO111MODULE=off
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
[[ "$(./bin/glow --version)" == "glow version %{version}" ]] || exit 1

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
