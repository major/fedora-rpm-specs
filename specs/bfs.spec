Name:           bfs
Version:        4.0.6
Release:        %autorelease
Summary:        A breadth-first version of the UNIX find command

License:        0BSD
URL:            https://github.com/tavianator/bfs
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(oniguruma)
BuildRequires:  pkgconfig(liburing)
BuildRequires:  pkgconfig(libselinux)
# needed to run check
BuildRequires:  acl

%description
bfs is a breadth-first version of the UNIX find(1) command.

bfs supports almost every feature from every major find(1)
implementation, so your existing command lines should work as-is.
It also adds some features of its own, such as a more forgiving
command line parser and some additional options.

%prep
%autosetup

%build
./configure --enable-release
%make_build

%install
%make_install

%check
%make_build check

%files
%license LICENSE
%doc README.md docs/{CHANGELOG,USAGE}.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{bash_completions_dir}/%{name}
%{fish_completions_dir}/%{name}.fish
%{zsh_completions_dir}/_%{name}

%changelog
%autochangelog
