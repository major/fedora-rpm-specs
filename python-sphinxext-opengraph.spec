%global project_name sphinxext-opengraph
%global pypi_name    sphinxext_opengraph

Name:           python-%{project_name}
Version:        0.6.3
Release:        3%{?dist}
Summary:        Sphinx extension to generate unique OpenGraph metadata

# License file is not included in PyPI sources,
#   upstream issue: https://github.com/wpilibsuite/sphinxext-opengraph/issues/51
License:        BSD
URL:            https://%{project_name}.readthedocs.io/en/latest/
Source0:        https://files.pythonhosted.org/packages/source/s/%{project_name}/%{project_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
%{summary}.}

%description %_description

%package -n python3-%{project_name}
Summary:        %{summary}

%description -n python3-%{project_name} %_description

%prep
%autosetup -p1 -n %{project_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

sed -i 's|version = "main"|version = "%{version}"|' setup.py

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files '*'


%files -n python3-%{project_name} -f %{pyproject_files}
#license LICENSE.md
%doc README.md


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.6.3-2
- Rebuilt for Python 3.11

* Tue Mar 29 2022 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.6.3-1
- version 0.6.3

* Wed Mar 09 2022 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.6.2-1
- version 0.6.2

* Wed Feb 23 2022 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.6.1-1
- version 0.6.1

* Tue Feb 22 2022 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.6.0-1
- version 0.6.0

* Tue Feb 01 2022 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.5.1-1
- initial spec for version 0.5.1

