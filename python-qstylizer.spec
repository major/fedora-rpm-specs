%global pypi_name qstylizer

%global _description %{expand:
qstylizer is a python package designed to help with the construction of 
PyQt/PySide stylesheets.
}

Name:           python-%{pypi_name}
Version:        0.2.2
Release:        4%{?dist}
Summary:        Qt stylesheet generation utility for PyQt/PySide

License:        MIT
URL:            https://github.com/blambright/qstylizer
# This URL does not seem to work
#Source0:        https://files.pythonhosted.org/packages/source/q/{pypi_name}/{pypi_name}-{version}.tar.gz
Source0:        https://github.com/blambright/qstylizer/archive/refs/tags/%{version}.tar.gz#/%{pypi_name}-%{version}.tar.gz
# python 3.12 complains:
# AttributeError: 'called_once_with' is not a valid assertion
Patch0:         qstylizer-0.2.2-called_once_with_not_valid_assertion.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

#for tests
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-mock)

%description
%_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%_description


%prep
%autosetup -n %{pypi_name}-%{version} -p1
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
export PBR_VERSION=%{version}
%pyproject_buildrequires -r

%build
export PBR_VERSION=%{version}
%pyproject_wheel

%install
export PBR_VERSION=%{version}
%pyproject_install

%pyproject_save_files qstylizer

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 12 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.2-3
- Modify calling called_once_with which seems typo

* Sat Jul 01 2023 Python Maint <python-maint@redhat.com> - 0.2.2-2
- Rebuilt for Python 3.12

* Thu Apr 13 2023 Jonathan Wright <jonathan@almalinux.org> - 0.2.2-1
- Update to 0.2.2

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.0-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 30 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.2.0-2
- Use pyproject-rpm-macros
- Add readme  in doc

* Sun Jun 27 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.2.0-1
- Initial package.
