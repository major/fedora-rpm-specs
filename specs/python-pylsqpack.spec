%if 0%{?fedora} || 0%{?rhel}
%bcond_without pyproject
%else
%bcond_with pyproject
%global __python3 /usr/bin/python3.11
%global __pytest /usr/bin/pytest-3.11
%global python3_version 3.11
%endif

%global pypi_name pylsqpack

Name:           python-%{pypi_name}
Version:        0.3.23
Release:        %autorelease
Summary:        %{pypi_name} is a wrapper around the ls-qpack library
License:        BSD-3-Clause
URL:            https://github.com/aiortc/%{pypi_name}
Source0:        %{pypi_source}
Patch0:         %{name}-unbundle_vendor_libs.patch

%description
It provides Python Decoder and Encoder objects
to read or write HTTP/3 headers compressed with QPACK.

%package -n python3-%{pypi_name}
Summary: %{pypi_name} is a wrapper around the ls-qpack library
BuildRequires:  gcc
BuildRequires:  ls-qpack-devel

%if %{with pyproject}
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%else
BuildRequires:  python%{python3_version}-devel
BuildRequires:  python%{python3_version}-pytest
BuildRequires:  python%{python3_version}-setuptools
BuildRequires:  python%{python3_version}-rpm-macros
%py_provides    python%{python3_version}-%{pypi_name}
%endif

%description -n python3-%{pypi_name}
It provides Python Decoder and Encoder objects
to read or write HTTP/3 headers compressed with QPACK.

%prep
%autosetup -n %{pypi_name}-%{version}

rm -rf src/%{pypi_name}.egg-info
%if %{with pyproject}
%generate_buildrequires
%pyproject_buildrequires -x tests
%endif

%build
%if %{with pyproject}
%pyproject_wheel
%else
%py3_build
%endif


%install
%if %{with pyproject}
%pyproject_install
%pyproject_save_files %{pypi_name}
%else
%py3_install
%endif

%check
export LD_PRELOAD=%{_libdir}/libls-qpack.so
%pytest -v

%if %{with pyproject}
%files -n python3-%{pypi_name} -f %{pyproject_files}
%else
%files -n python3-%{pypi_name}
%{python3_sitearch}/%{pypi_name}/
%{python3_sitearch}/%{pypi_name}-%{version}*.egg-info/
%license LICENSE
%endif
%doc README.rst


%changelog
%autochangelog
