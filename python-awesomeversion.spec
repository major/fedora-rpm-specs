%global pypi_name awesomeversion

Name:           python-%{pypi_name}
Version:        22.9.0
Release:        %autorelease
Summary:        Python module to deal with versions

License:        MIT
URL:            https://github.com/ludeeus/awesomeversion
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description
Python module to deal with versions if it comes to comparing them. Make
anything a version object, and compare against a vast section of other
version formats.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Python module to deal with versions if it comes to comparing them. Make
anything a version object, and compare against a vast section of other
version formats.

%prep
%autosetup -n %{pypi_name}-%{version}
# Only the PyPI source set the version properly
sed -i -e 's/version = "0"/version = "%{version}"/g' pyproject.toml
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}
rm %{buildroot}/%{python3_sitelib}/LICENCE.md

%check
%pytest -v tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENCE.md

%changelog
%autochangelog

