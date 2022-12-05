%global pypi_name adafruit-platformdetect

Name:           python-%{pypi_name}
Version:        3.32.0
Release:        %autorelease

Summary:        Platform detection module

License:        MIT
URL:            https://github.com/adafruit/Adafruit_Python_PlatformDetect
Source0:        %{pypi_source Adafruit-PlatformDetect}
BuildArch:      noarch

%description
This library provides best-guess platform detection for a range of
single-board computers and (potentially) other platforms.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This library provides best-guess platform detection for a range of
single-board computers and (potentially) other platforms.

%package -n python-%{pypi_name}-doc
Summary:        Documentation for adafruit-platformdetect

BuildRequires:  python3dist(sphinx)
%description -n python-%{pypi_name}-doc
Documentation for adafruit-platformdetect.

%prep
%autosetup -n Adafruit-PlatformDetect-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build
PYTHONPATH=${PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%ifarch %{arm} %{arm64}
%check
%pytest -v tests
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/adafruit_platformdetect/
%{python3_sitelib}/Adafruit_PlatformDetect-%{version}-py%{python3_version}.egg-info/

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
%autochangelog

