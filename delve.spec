# Run tests in check section
%bcond_without check

# https://github.com/go-delve/delve
%global goipath         github.com/go-delve/delve
Version:                1.20.2

%global common_description %{expand:
Delve is a debugger for the Go programming language. The goal of the project 
is to provide a simple, full featured debugging tool for Go. Delve should be 
easy to invoke and easy to use. Chances are if you're using a debugger, things 
aren't going your way. With that in mind, Delve should stay out of your way as 
much as possible.}

# Currently Delve only supports x86_64 and aarch64
%global golang_arches x86_64 aarch64

%gometa

Name:           delve
Release:        %autorelease
Summary:        A debugger for the Go programming language
# Detected licences
# - Expat License at 'LICENSE'
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

# This dependencies are only in use in x86_64
%ifarch x86_64
BuildRequires:  golang(github.com/cilium/ebpf)
BuildRequires:  golang(github.com/cilium/ebpf/link)
BuildRequires:  golang(github.com/cilium/ebpf/ringbuf)
%endif
BuildRequires:  golang(github.com/cosiner/argv)
BuildRequires:  golang(github.com/creack/pty)
BuildRequires:  golang(github.com/derekparker/trie)
BuildRequires:  golang(github.com/go-delve/liner)
BuildRequires:  golang(github.com/google/go-dap)
BuildRequires:  golang(github.com/hashicorp/golang-lru/simplelru)
BuildRequires:  golang(github.com/mattn/go-isatty)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/spf13/cobra/doc)
BuildRequires:  golang(golang.org/x/arch/arm64/arm64asm)
BuildRequires:  golang(golang.org/x/arch/ppc64/ppc64asm)
BuildRequires:  golang(golang.org/x/arch/x86/x86asm)
BuildRequires:  golang(golang.org/x/sys/unix)
BuildRequires:  golang(golang.org/x/tools/go/packages)
BuildRequires:  golang(gopkg.in/yaml.v2)
BuildRequires:  golang(go.starlark.net/resolve)
BuildRequires:  golang(go.starlark.net/starlark)
BuildRequires:  golang(go.starlark.net/syntax)
BuildRequires:  lsof
BuildRequires:  git

%description
%{common_description}

%prep
echo "=== Start prep ==="
%goprep

%generate_buildrequires
%go_generate_buildrequires

%build
echo "=== Start build ==="
%gobuild -o %{gobuilddir}/bin/dlv %{goipath}/cmd/dlv
echo "=== End build ==="

%install
%gopkginstall
install -m 0755 -vd %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
export GO111MODULE=off
export GOPATH=%{buildroot}/%{gopath}:%{gopath}
delvepath=%{buildroot}/%{gopath}/src/%{goipath}
cp -r _fixtures $delvepath
cp -r pkg/dwarf/line/_testdata $delvepath/pkg/dwarf/line
cp -r pkg/proc/internal/ebpf $delvepath/pkg/proc/internal/

pushd $delvepath
echo "=== Start tests ==="
%gotest $(go list ./... | awk '!/(cmd|scripts)/ {print $1}')
echo "=== End tests ==="
rm -rf $delvepath
popd
%endif

%files
%license LICENSE
%doc CONTRIBUTING.md CHANGELOG.md
%doc Documentation/*
%{_bindir}/dlv

%changelog
%autochangelog
