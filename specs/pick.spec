Name:           pick
Version:        4.0.0
Release:        10%{?dist}
Summary:        A fuzzy search tool for the command-line

# The entire source code is MIT except for
# compat-reallocarray.c and compat-strtonum.c files which are ISC
License:        MIT AND ISC
URL:            https://github.com/mptre/pick
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  ncurses-devel

# nmh also provides /usr/bin/pick
Conflicts:      nmh

%description
The pick utility allows users to choose one option from a set of choices using
an interface with fuzzy search functionality. pick reads a list of choices on
stdin and outputs the selected choice on stdout. Therefore it is easily used
both in pipelines and subshells.

%prep
%autosetup

%build
export PREFIX=%{_prefix}
export MANDIR=%{_mandir}
export INSTALL_MAN="install -p -m 0644"
%configure
%make_build

%install
%make_install

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb 01 2023 Gustavo Costa <xfgusta@gmail.com> - 4.0.0-5
- Use SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 28 2021 Gustavo Costa <xfgusta@fedoraproject.org> - 4.0.0-1
- Initial package
