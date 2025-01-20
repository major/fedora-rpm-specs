%global srcname docstring-parser

Name:           python-%{srcname}
Version:        0.16
Release:        2%{?dist}
Summary:        Parse Python docstrings
License:        MIT
URL:            https://github.com/rr-/docstring_parser
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Fix removal of ast.Str, ast.NameConstant and ast.Num in Python 3.14
# Upstream discussion https://github.com/rr-/docstring_parser/pull/91
Patch0001:      0001-Fix_3.14_Ast_changes.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}


%global _description %{expand:
Parse Python docstrings. Currently support ReST, Google, Numpydoc-style and Epydoc docstrings.}


%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}


%description -n python3-%{srcname} %{_description}


%prep
%autosetup -p 1 -n docstring_parser-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files docstring_parser


%check
%{pytest}


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%license LICENSE.md


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 04 2024 Federico Pellegrin <fede@evolware.org> - 0.16-1
- Bump to 0.16, fix build for Python 3.14(pre)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.15-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.15-2
- Rebuilt for Python 3.12

* Wed Jan 18 2023 Piotr Szubiakowski <pszubiak@eso.org> - 0.15-1
- Update to 0.15

* Wed Jul 20 2022 Piotr Szubiakowski <pszubiak@eso.org> - 0.14.1-2
- Apply code review fixes

* Thu May 19 2022 Piotr Szubiakowski <pszubiak@eso.org> - 0.14.1-1
- Init
