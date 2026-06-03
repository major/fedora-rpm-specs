Name:    shdoc
Version: 1.4
Release: %autorelease
Summary: Documentation generator for bash/zsh/sh for generating documentation in Markdown

License:   MIT
URL:       https://github.com/reconquest/shdoc
Source0:   https://github.com/reconquest/shdoc/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: vim-filesystem
Requires:  gawk
Requires:  vim-filesystem

%description
shdoc is a documentation generator for bash/zsh/sh for generating API
documentation in Markdown from shell scripts source.

shdoc parses annotations in the beginning of a given file and alongside function
definitions, and creates a markdown file with ready to use documentation.

%prep
%autosetup

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 -vp shdoc %{buildroot}%{_bindir}/shdoc
mkdir -p %{buildroot}%{_mandir}/man1/
install -m 0644 -vp contrib/shdoc.1 %{buildroot}%{_mandir}/man1/
mkdir -p %{buildroot}%{vimfiles_root}/syntax/
install -m 0644 -vp contrib/vim/after/syntax/sh.vim %{buildroot}%{vimfiles_root}/syntax/sh.vim

%files
%{_bindir}/shdoc
%{_mandir}/man1/%{name}.1*
%{vimfiles_root}/syntax/sh.vim

%doc README.md
%license LICENSE

%changelog
%autochangelog
