%global srcname flake8-comprehensions

Name:           python-%{srcname}
Version:        3.10.1
Release:        11%{?dist}
Summary:        Flake8 plugin that helps you write better list/set/dict comprehensions

License:        MIT
URL:            https://github.com/adamchainz/flake8-comprehensions
Source0:        https://github.com/adamchainz/flake8-comprehensions/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
A flake8 plugin to identify the following patterns:

- C400-402: Unnecessary generator - rewrite as a <list/set/dict> comprehension.
- C403-404: Unnecessary list comprehension - rewrite as a <set/dict>
  comprehension.
- C405-406: Unnecessary <list/tuple> literal - rewrite as a <set/dict> literal.
- C408: Unnecessary <dict/list/tuple> call - rewrite as a literal.
- C409-410: Unnecessary <list/tuple> passed to <list/tuple>() - (remove the
  outer call to <list/tuple>``()/rewrite as a ``<list/tuple> literal).
- C411: Unnecessary list call - remove the outer call to list().
- C413: Unnecessary <list/reversed> call around sorted().
- C414: Unnecessary <list/reversed/set/sorted/tuple> call within
  <list/set/sorted/tuple>().
- C415: Unnecessary subscript reversal of iterable within
  <reversed/set/sorted>().
- C416: Unnecessary <list/set> comprehension - rewrite using <list/set>().
- C417: Unnecessary map usage - rewrite using a generator
  expression/<list/set/dict> comprehension.}

%description %_description


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel

%description -n python%{python3_pkgversion}-%{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires requirements/requirements.in


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files flake8_comprehensions


%check
%pytest


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc HISTORY.rst README.rst


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 3.10.1-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 14 2023 Python Maint <python-maint@redhat.com> - 3.10.1-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 21 2022 Scott K Logan <logans@cottsay.net> - 3.10.1-3
- Install test dependencies using pyproject_buildrequires
- Enable pytest check

* Thu Nov 17 2022 Scott K Logan <logans@cottsay.net> - 3.10.1-2
- Define _description variable to reduce duplication
- Drop macro from URL to improve ergonomics

* Thu Nov 10 2022 Scott K Logan <logans@cottsay.net> - 3.10.1-1
- Initial package (rhbz#2141869)
