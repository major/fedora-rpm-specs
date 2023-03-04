%global pypi_name typepy

Name:           python-%{pypi_name}
Version:        1.3.0
Release:        2%{?dist}
Summary:        Python library for variable type checker/validator/converter at a run time

License:        MIT
URL:            https://github.com/thombashi/typepy 
Source0:        %{pypi_source %{pypi_name}}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

#test requirements
BuildRequires:  python3-tcolorpy
BuildRequires:  python3-pytz
BuildRequires:  python3-dateutil
%description
Python library for variable type checker/validator/converter at a run time.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
 
Requires:  python3-mbstrdecoder >= 1.0.0

%description -n python3-%{pypi_name}
Python library for variable type checker/validator/converter at a run time.

%pyproject_extras_subpkg -n python3-%{pypi_name} datetime

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest -v

%files -n python3-%{pypi_name} -f %{pyproject_files} 
%license LICENSE
%doc README.rst

%changelog
* Thu Mar 02 2023 Karolina Kula <kkula@redhat.com> - 1.3.0-2
- Add datetime subpackage
* Thu Oct 13 2022 Karolina Kula <kkula@redhat.com> - 1.3.0-1
- Update to 1.3.0
* Fri Sep 23 2022 Karolina Kula <kkula@redhat.com> - 1.2.0-2
- fix rpmlint issues
* Thu Sep 08 2022 Karolina Kula <kkula@redhat.com> - 1.2.0-1
- initial package build

