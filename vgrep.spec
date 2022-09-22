# https://github.com/vrothberg/vgrep
%global goipath         github.com/vrothberg/vgrep
Version:                2.6.0

%gometa

%global common_description %{expand:
vgrep is a pager for grep, git-grep, ripgrep and similar grep implementations,
and allows for opening the indexed file locations in a user-specified editor
such as vim or emacs. vgrep is inspired by the ancient cgvg scripts but
extended to perform further operations such as listing statistics of files and
directory trees or showing the context lines before and after the matches.}

%global golicenses      LICENSE
%global godocs          README.md

%bcond_without check

Name:           vgrep
Release:        %autorelease
Summary:        User-friendly pager for grep
License:        GPLv3
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/jessevdk/go-flags)
BuildRequires:  golang(github.com/json-iterator/go)
BuildRequires:  golang(github.com/mattn/go-shellwords)
BuildRequires:  golang(github.com/nightlyone/lockfile)
BuildRequires:  golang(github.com/peterh/liner)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(golang.org/x/term)

BuildRequires:  go-md2man

%description
%{common_description}

%gopkg

%prep
%goprep

%build
export LDFLAGS="-X main.version=%{version} "
%gobuild -o %{gobuilddir}/bin/vgrep %{goipath}
go-md2man -in docs/vgrep.1.md -out docs/vgrep.1

%install
%gopkginstall
install -D -p -m 0755 %{gobuilddir}/bin/vgrep %{buildroot}%{_bindir}/vgrep
install -D -p -m 0644 docs/vgrep.1 %{buildroot}%{_mandir}/man1/vgrep.1

%if %{with check}
%check
%gocheck
%endif

%files
%license %{golicenses}
%doc %{godocs}
%{_bindir}/vgrep
%{_mandir}/man1/vgrep.1*

%gopkgfiles

%changelog
%autochangelog
