%global srcname flake8-builtins

Name:           python-%{srcname}
Version:        2.1.0
Release:        2%{?dist}
Summary:        Check for python builtins being used as variables or parameters

License:        GPL-2.0-only
URL:            https://github.com/gforcada/flake8-builtins
Source0:        https://github.com/gforcada/flake8-builtins/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
Python allows to override builtin names, but although could be useful in some
really specific use cases, the general approach is to not do that as code then
can suddenly break without a clear trace.}

%description %_description


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel


%description -n python%{python3_pkgversion}-%{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files flake8_builtins


%check
%pytest run_tests.py


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.rst


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Scott K Logan <logans@cottsay.net> - 2.1.0-1
- Update to 2.1.0

* Mon Nov 21 2022 Scott K Logan <logans@cottsay.net> - 2.0.1-2
- Define _description variable to reduce duplication
- Drop macro from URL to improve ergonomics

* Thu Nov 10 2022 Scott K Logan <logans@cottsay.net> - 2.0.1-1
- Initial package (rhbz#2141867)
