%global pypi_name nest_asyncio

Name:           python-nest-asyncio
Version:        1.6.0
Release:        %autorelease
Summary:        Patch asyncio to allow nested event loops

License:        BSD-2-Clause
URL:            https://github.com/erdewit/nest_asyncio
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros


%description
By design asyncio does not allow its event loop to be nested.
This presents a practical problem: When in an environment
where the event loop is already running it's impossible to run tasks
and wait for the result. Trying to do so will give the error
"RuntimeError: This event loop is already running".
The issue pops up in various environments, such as web servers,
GUI applications and in Jupyter notebooks.
This module patches asyncio to allow nested use of asyncio.run
and loop.run_until_complete.


%package -n     python3-nest-asyncio
Summary:        %{summary}

# This package used to be called python3-nest_asyncio
Obsoletes:      python3-nest_asyncio < 1.4.3-100
%py_provides    python3-nest_asyncio

%description -n python3-nest-asyncio
By design asyncio does not allow its event loop to be nested.
This presents a practical problem: When in an environment
where the event loop is already running it's impossible to run tasks
and wait for the result. Trying to do so will give the error
"RuntimeError: This event loop is already running".
The issue pops up in various environments, such as web servers,
GUI applications and in Jupyter notebooks.
This module patches asyncio to allow nested use of asyncio.run
and loop.run_until_complete.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %python3 tests/nest_test.py

%files -n python3-nest-asyncio -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
