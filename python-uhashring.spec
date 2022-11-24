%global module uhashring

Name:           python-%{module}
Version:        2.1
Release:        1%{?dist}
Summary:        Python module uhashring

License:        BSD-3-Clause
URL:            https://github.com/ultrabug/uhashring/
Source:         https://github.com/ultrabug/%{module}/archive/refs/tags/%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
uhashring implements consistent hashing in pure Python.}

%description %_description

%package -n python3-%{module}
Summary:        %{summary}

%description -n python3-%{module}
%_description

%prep
%autosetup -p1 -n %{module}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files %{module}

%check
%pytest

%files -n python3-%{module} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
* Fri Nov 18 2022 Alfredo Moralejo <amoralej@redhat.com> - 2.1-1
- Initial build with version 2.1 

