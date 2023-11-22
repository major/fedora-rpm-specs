%bcond_without check

# https://github.com/junegunn/fzf
%global goipath         github.com/junegunn/fzf
Version:                0.44.1
%global tag             %{version}

%gometa

Name:           fzf
Release:        %autorelease
Summary:        A command-line fuzzy finder written in Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        README.Fedora

BuildRequires:  golang(github.com/gdamore/tcell/v2) >= 2.5.3
BuildRequires:  golang(github.com/gdamore/tcell/v2/encoding)
BuildRequires:  golang(github.com/mattn/go-isatty) >= 0.0.16
BuildRequires:  golang(github.com/mattn/go-runewidth) >= 0.0.14
BuildRequires:  golang(github.com/mattn/go-shellwords) >= 1.0.12
BuildRequires:  golang(github.com/rivo/uniseg) >= 0.4.4
BuildRequires:  golang(github.com/saracen/walker) >= 0.1.3
BuildRequires:  golang(golang.org/x/term) >= 0.7

%description
fzf is a general-purpose command-line fuzzy finder.

It's an interactive Unix filter for command-line that can be used with any
list; files, command history, processes, hostnames, bookmarks, git commits,
etc.


%prep
%goprep
cp %{SOURCE1} .
%autopatch -p1


%build
export LDFLAGS='-X main.version=%{version} -X main.revision=Fedora '
%gobuild -o %{gobuilddir}/bin/fzf %{goipath}

# Cleanup interpreters
sed -i -e '/^#!\//, 1d' shell/completion.*
sed -i -e '1d;2i#!/bin/bash' bin/fzf-tmux


%install
install -vdm 0755 %{buildroot}%{_bindir}
install -vDpm 0755 %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -Dpm0755 bin/fzf-tmux %{buildroot}%{_bindir}/
install -d -p %{buildroot}%{_mandir}/man1
install -Dpm0644 man/man1/*.1 %{buildroot}%{_mandir}/man1/

install -d %{buildroot}%{_datadir}/fzf

# Install vim plugin
install -d %{buildroot}%{_datadir}/vim/vimfiles/plugin
install -Dpm0644 plugin/fzf.vim %{buildroot}%{_datadir}/vim/vimfiles/plugin/
install -d %{buildroot}%{_datadir}/nvim/site/plugin
install -Dpm0644 plugin/fzf.vim %{buildroot}%{_datadir}/nvim/site/plugin/

# Install shell completion
install -d %{buildroot}%{_sysconfdir}/bash_completion.d/
install -Dpm0644 shell/completion.bash %{buildroot}%{_sysconfdir}/bash_completion.d/fzf
install -d %{buildroot}%{_datadir}/zsh/site-functions
install -Dpm0644 shell/completion.zsh %{buildroot}%{_datadir}/zsh/site-functions/fzf

# Install shell key bindings (not enabled)
install -d %{buildroot}%{_datadir}/fzf/shell
install -Dpm0644 shell/key-bindings.* %{buildroot}%{_datadir}/fzf/shell/


%if %{with check}
%check
%gocheck
%endif


%files
%license LICENSE
%doc README.md README-VIM.md CHANGELOG.md README.Fedora
%{_bindir}/fzf
%{_bindir}/fzf-tmux
%{_mandir}/man1/fzf.1*
%{_mandir}/man1/fzf-tmux.1*
%dir %{_datadir}/fzf
%{_datadir}/fzf/shell
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/fzf
%dir %{_datadir}/vim/vimfiles/plugin
%{_datadir}/vim/vimfiles/plugin/fzf.vim
%dir %{_datadir}/nvim/site/plugin
%{_datadir}/nvim/site/plugin/fzf.vim
%{_sysconfdir}/bash_completion.d/fzf


%changelog
%autochangelog
