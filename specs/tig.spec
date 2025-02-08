%global bash_completion_dir %(pkg-config --variable=completionsdir bash-completion || echo /etc/bash_completion.d)/

Name:           tig
Version:        2.5.12
Release:        %autorelease
Summary:        Text-mode interface for the git revision control system

License:        GPL-2.0-or-later
URL:            https://jonas.github.io/tig/
Source0:        https://github.com/jonas/tig/releases/download/tig-%version/tig-%version.tar.gz

BuildRequires:  asciidoc
BuildRequires:  bash-completion
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
BuildRequires:  xmlto
Requires:       git-core

%description
Tig is a repository browser for the git revision control system that
additionally can act as a pager for output from various git commands.

When browsing repositories, it uses the underlying git commands to present the
user with various views, such as summarized revision log and showing the commit
with the log message, diffstat, and the diff.

Using it as a pager, it will display input from stdin and colorize it.


%prep
%autosetup


%build
%configure
%make_build all doc-man doc-html

#Convert to unix line endings
sed -i -e 's/\r//' *.html

# Remove shebang from bash-completion script
sed -i '/^#!bash/,+1 d' contrib/%{name}-completion.bash


%install
%make_install install-doc-man

# Setup bash completion
install -Dpm 644 contrib/%{name}-completion.bash %{buildroot}%{bash_completion_dir}/%{name}


%files
%license COPYING
%doc COPYING NEWS.adoc README.adoc *.html
%{_bindir}/tig
%{bash_completion_dir}
%config(noreplace) %{_sysconfdir}/%{name}rc
%{_mandir}/man1/tig.1*
%{_mandir}/man5/tigrc.5*
%{_mandir}/man7/tigmanual.7*


%changelog
%autochangelog
