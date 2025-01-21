Name:    zsh-autosuggestions
Version: 0.7.1
Release: 2%{?dist}

Summary: Fish-like autosuggestions for zsh
License: MIT
URL:     https://github.com/zsh-users/zsh-autosuggestions
Source0: https://github.com/zsh-users/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: make
BuildRequires: zsh

Requires: zsh

%description
This package provides autosuggestions for the shell zsh. It suggests commands
as you type based on history and completions.

%prep
%autosetup

%build
make

%install
install -D --preserve-timestamps --target-directory=%{buildroot}%{_datadir}/%{name} %{name}.zsh

%check

%files
%doc CHANGELOG.md README.md
%license LICENSE
%{_datadir}/%{name}

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Nov 15 2024 Michael Kuhn <suraia@fedoraproject.org> - 0.7.1-1
- Update to 0.7.1

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 05 2021 Michael Kuhn <suraia@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 01 2020 Michael Kuhn <suraia@fedoraproject.org> - 0.6.4-1
- Update to 0.6.4

* Sun Nov 17 2019 Michael Kuhn <suraia@fedoraproject.org> - 0.6.3-1
- Initial package
