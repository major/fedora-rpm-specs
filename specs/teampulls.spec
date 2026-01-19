Name:           teampulls
Version:        0.2.7
Release:        3%{?dist}
Summary:        CLI tool that lists pull requests from GitHub

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://github.com/brejoc/teampulls
Source0:        https://files.pythonhosted.org/packages/source/t/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core)
BuildRequires:  python3dist(pip)
BuildRequires:  pyproject-rpm-macros

# Runtime dependencies
#BuildRequires:  python3dist(requests)
#BuildRequires:  python3dist(toml)
#BuildRequires:  python3dist(docopt)

%description
teampulls lists all of the pull requests for a list of users and repositories.
On top of that every pull requests that is older than 14 days is
printed in red.


%prep
%autosetup -n %{name}-%{version}

%build
%pyproject_wheel

%install
%{pyproject_install}
install -Dpm 0644 teampulls.toml %{buildroot}%{_sysconfdir}/teampulls.toml

%files
%doc README.md
%license LICENSE
%{_bindir}/teampulls
%config(noreplace) %{_sysconfdir}/teampulls.toml
%{python3_sitelib}/teampulls
%{python3_sitelib}/teampulls-0.2.6.dist-info/

%changelog
* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 0.2.7-2
- Rebuilt for Python 3.14.0rc3 bytecode

* Thu Aug 28 2025 Jochen Breuer <brejoc@gmail.com> - 0.2.7-1
- Update to version 0.2.7
  - Switch to poetry with gh#22 and some more security updates: gh#23 gh#24
  - Fixes for gh#9 gh#10

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jun 02 2025 Python Maint <python-maint@redhat.com> - 0.2.2-19
- Rebuilt for Python 3.14

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.2-17
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.2.2-15
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.2.2-12
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.2-9
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.2-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-3
- Rebuilt for Python 3.9

* Sat Mar 21 2020 Jochen Breuer <brejoc@gmail.com> - 0.2.2-2
- Rebuild with sources properly uploaded
* Sun Mar 08 2020 Jochen Breuer <brejoc@gmail.com> - 0.2.2-1
- Initial package of version 0.2.2
