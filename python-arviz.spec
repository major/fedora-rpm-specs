
%global srcname arviz

Name:           python-%{srcname}
Version:        0.12.0
Release:        4%{?dist}
Summary:        Exploratory analysis of Bayesian models

License:        ASL 2.0
URL:            https://python.arviz.org/
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
ArviZ is a Python package for exploratory analysis of Bayesian models. 
Includes functions for posterior analysis, sample diagnostics, 
model checking, and comparison.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-setuptools
# Some optional dependencies
Recommends:  python3dist(bokeh)
Recommends:  python3dist(ujson)

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files arviz

%check
%pyproject_check_import -t


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Python Maint <python-maint@redhat.com> - 0.12.0-2
- Rebuilt for Python 3.11

* Sun Apr 24 2022 Sergio Pascual <sergiopr@fedoraproject.org> - 0.12.0-1
- New upstream release (0.12.0)
- Rewrite to use new macros

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct 06 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 0.11.4-1
- New upstream release (0.11.4)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.11.2-2
- Rebuilt for Python 3.10

* Tue Feb 16 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 0.11.2-1
- New upstream release (0.11.2)

* Tue Feb 16 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 0.11.1-1
- New upstream release (0.11.1)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 29 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 0.10.0-1
- New upstream release (0.10.0)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 28 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 0.9.0-1
- New upstream release (0.9.0)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-2
- Rebuilt for Python 3.9

* Sat May 23 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 0.8.0-1
- New upstream release (0.8.0)

* Mon Mar 09 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 0.7.0-1
- New upstream release (0.7.0)

* Sun Feb 09 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 0.6.1-1
- New upstream release (0.6.1)

* Mon Nov 11 2019 Sergio Pascual <sergio.pasra at gmail.com> - 0.5.1-1
- Initial spec file

