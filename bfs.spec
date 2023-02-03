Name:           bfs
Version:        2.6.3
Release:        1%{?dist}
Summary:        A breadth-first version of the UNIX find command

License:        0BSD
URL:            https://github.com/tavianator/bfs
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(libattr)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(oniguruma)
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
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%changelog
* Wed Feb 01 2023 Gustavo Costa <xfgusta@gmail.com> - 2.6.3-1
- Update to 2.6.3 (rhbz#2166230)
- Use SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Oct 23 2022 Gustavo Costa <xfgusta@gmail.com> - 2.6.2-1
- Update to 2.6.2 (rhbz#2136941)

* Wed Jul 13 2022 Gustavo Costa <xfgusta@gmail.com> - 2.6.1-1
- Initial package
