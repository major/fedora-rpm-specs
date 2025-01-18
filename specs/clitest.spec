%global forgeurl https://github.com/aureliojargas/clitest
%global tag %{version}

Name:    clitest
Version: 0.5.0
Release: 6%{?dist}
Summary: Command Line Tester

License: MIT
URL:     %{forgeurl}

%forgemeta
Source:  %{forgesource}

BuildArch:     noarch
BuildRequires: /usr/bin/perl
BuildRequires: bash dash mksh zsh
BuildRequires: make

Requires: diffutils
Requires: sed
Requires: grep
Suggests: perl

%description
clitest is a portable POSIX shell script that performs automatic testing in \
Unix command lines.

It's the same concept as in Python's doctest module: you document both the \
commands and their expected output, using the familiar interactive prompt \
format, and a specialized tool tests them.

%prep
%forgesetup

%build
#no build, only shell script

%check
make test docker_run=

%install
install -D -m755 -p clitest %{buildroot}%{_bindir}/clitest

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/clitest


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 27 2023 Jonny Heggheim <hegjon@gmail.com> - 0.5.0-1
- Updated to version 0.5.0

* Mon Jun 12 2023 Jonny Heggheim <hegjon@gmail.com> - 0.4.0-8
- Fixed broken tests

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Oct 04 2020 Jonny Heggheim <hegjon@gmail.com> - 0.4.0-2
- Added runtime dependencies

* Fri Oct 02 2020 Jonny Heggheim <hegjon@gmail.com> - 0.4.0-1
- Initial package
