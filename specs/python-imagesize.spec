%bcond_without tests

%global pypi_name imagesize
%global sum  Python module for analyzing image file headers and returning image sizes

Name:           python-%{pypi_name}
Version:        2.0.0
Release:        1%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://github.com/shibukawa/imagesize_py
Source0:        https://files.pythonhosted.org/packages/source/i/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-devel
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pytest
%endif

%description
The imagesize package parses image file headers and returns the image sizes.

* PNG
* JPEG
* JPEG2000
* GIF

This is a pure Python library.

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
The imagesize package parses image file headers and returns the image sizes.

* PNG
* JPEG
* JPEG2000
* GIF

This is a pure Python library.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import
%if %{with tests}
# test_get_filelike requires internet connection, hence we disable it
%pytest -v -k 'not test_get_filelike'
%endif

%files -n python%{python3_pkgversion}-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog