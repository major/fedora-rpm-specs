%global shortcommit     225927b
%global compiledate     August\ 25,\ 2022

# https://github.com/zyedidia/micro
%global goipath         github.com/zyedidia/micro
Version:                2.0.11

%gometa -f

%global goname          micro

%global common_description %{expand:
Micro is a terminal-based text editor that aims to be easy to use and
intuitive, while also taking advantage of the full capabilities of modern
terminals. It comes as one single, batteries-included, static binary with no
dependencies, and you can download and use it right now.

As the name indicates, micro aims to be somewhat of a successor to the nano
editor by being easy to install and use in a pinch, but micro also aims to be
enjoyable to use full time, whether you work in the terminal because you prefer
it (like me), or because you need to (over ssh).}

%global golicenses      LICENSE LICENSE-THIRD-PARTY
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        A modern and intuitive terminal-based text editor
# Upstream license specification: MIT and Apache-2.0
License:        MIT and ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(gopkg.in/yaml.v2)

%description
%{common_description}

%prep
%goprep
sed -i "s|github.com/zyedidia/json5|github.com/flynn/json5|" $(find . -name "*.go")

%build
export LDFLAGS="-X 'github.com/zyedidia/micro/internal/util.Version=%{version}' \
                -X 'github.com/zyedidia/micro/internal/util.CommitHash=%{shortcommit}' \
                -X 'github.com/zyedidia/micro/internal/util.CompileDate=%{compiledate}' \
                -X 'github.com/zyedidia/micro/internal/util.Debug=OFF'"

# For syntax highlighting
export GOPATH="/usr/share/gocode/"
export GO111MODULE=off
go generate ./runtime

for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%generate_buildrequires
%go_generate_buildrequires

%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%check
%gocheck -d cmd/micro/shellwords -d cmd/micro/terminfo

%files
%license LICENSE LICENSE-THIRD-PARTY
%doc README.md
%{_bindir}/*

%changelog
%autochangelog
