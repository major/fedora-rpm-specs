%global pypi_name pyserial-asyncio

Name:           %{pypi_name}
Version:        0.6
Release:        %autorelease
Summary:        Asynchronous Python Serial Port Extension

License:        BSD-3-Clause
URL:            https://github.com/pyserial/pyserial-asyncio
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Async I/O extension package for the Python Serial Port Extension.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Async I/O extension package for the Python Serial Port Extension.

%package -n python-%{pypi_name}-doc
Summary:        pyserial-asyncio documentation

BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
%description -n python-%{pypi_name}-doc
Documentation for pyserial-asyncio.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
sed -i -e '/^#!\//, 1d' serial_asyncio/__init__.py
sed -i 's/self.loop = asyncio.get_event_loop()/self.loop = asyncio.new_event_loop(); asyncio.set_event_loop(self.loop)/' test/test_asyncio.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
PYTHONPATH=${PWD} sphinx-build-3 documentation html
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files serial_asyncio

%check
%pytest -v test

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE.txt

%changelog
%autochangelog
