%global pypi_name spyder-kernels

Name:           python-%{pypi_name}
Version:        2.4.4
Release:        %autorelease
Epoch:          1
Summary:        Jupyter kernels for the Spyder console

License:        MIT
URL:            https://github.com/spyder-ide/spyder-kernels
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(cloudpickle)
BuildRequires:  python3dist(ipykernel)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wurlitzer)

# for tests
# python3
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(flaky)
BuildRequires:  python3dist(jupyter-client)
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pyzmq)
BuildRequires:  python3dist(scipy)
BuildRequires:  python3dist(xarray)

%description
This package provides jupyter kernels used by spyder on its IPython console.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(cloudpickle)
Requires:       python3dist(ipykernel)
Requires:       python3dist(jupyter-client)
Requires:       python3dist(pyzmq)
Requires:       python3dist(wurlitzer)

%description -n python3-%{pypi_name}
This package provides python3 version of jupyter kernels used by spyder on its
 IPython console.


%prep
%autosetup -n %{pypi_name}-%{version}

# spyder-kernel 2.2.1 - relax ipython version
sed -i '\@ipython@s|>=7.31.1,<8|>=7.31.1|' setup.py

# relax ipykernel dependency for now (bug 2070644)
sed -i '\@ipykernel@s|6.9.2|6.6.1|' setup.py

# relax jupyter-client version
sed -i '\@jupyter-client@s|>=7.3.4,<8|>7|' setup.py

rm -rfv spyder_kernels.egg-info

%build
%py3_build

%install
%py3_install

%check
# tests not present in pypi source
#export PYTHONPATH={buildroot}{python3_sitelib} pytest-3

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/spyder_kernels
%{python3_sitelib}/spyder_kernels-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
