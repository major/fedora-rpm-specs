Name:    shdoc
Version: 1.2
Release: %autorelease
Summary: Documentation generator for bash/zsh/sh for generating documentation in Markdown

License:   MIT
URL:       https://github.com/reconquest/shdoc
Source0:   https://github.com/reconquest/shdoc/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch: noarch

Requires:  gawk

%description
shdoc is a documentation generator for bash/zsh/sh for generating API
documentation in Markdown from shell scripts source.

shdoc parses annotations in the beginning of a given file and alongside function
definitions, and creates a markdown file with ready to use documentation.

%prep
%autosetup

%install
mkdir -p %{buildroot}%{_bindir}
cp -a shdoc %{buildroot}%{_bindir}/shdoc

%files
%{_bindir}/shdoc

%doc README.md
%license LICENSE

%changelog
%autochangelog
