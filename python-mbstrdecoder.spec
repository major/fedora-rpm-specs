%global pypi_name mbstrdecoder

Name:           python-%{pypi_name}
Version:        1.1.0
Release:        2%{?dist}
Summary:        multi-byte character string decoder

License:        MIT
URL:            https://github.com/thombashi/mbstrdecoder 
Source0:        https://files.pythonhosted.org/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz 
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description
multi-byte character string decoder

%package -n     python3-%{pypi_name}
Summary:        %{summary}
 
Requires:  python3-chardet

%description -n python3-%{pypi_name}

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
sed -i 's/chardet>=3.0.4,<5/chardet>=3.0.4/g' requirements/requirements.txt

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

* Thu Aug 04 2022 Karolina Kula <kkula@redhat.com> - 1.1.0-2
- Remove chardet <5 requirement
- Remove %python_provide depracated macros
- Add pytest as BR

* Thu May 19 2022 Karolina Kula <kkula@redhat.com> - 1.1.0-1
- initial package build

