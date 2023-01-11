%global pypi_name xbout

Name:           python-%{pypi_name}
Version:        0.3.4
Release:        %autorelease
Summary:        Collects BOUT++ data from parallelized simulations into xarray

License:        ASL 2.0
URL:            https://github.com/boutproject/xBOUT
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
# Sphinx for docs
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-boutdata
# Testing
BuildRequires:  python3dist(pytest)

%generate_buildrequires
%pyproject_buildrequires -r

%description
xBOUT provides an interface for collecting the output data from a
BOUT++ simulation into an xarray dataset in an efficient and
scalable way, as well as accessor methods for common BOUT++ analysis
and plotting tasks.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%py_provides python3-%{pypi_name}}

Requires:  python3-boutdata

%description -n python3-%{pypi_name}
xBOUT provides an interface for collecting the output data from a
BOUT++ simulation into an xarray dataset in an efficient and
scalable way, as well as accessor methods for common BOUT++ analysis
and plotting tasks.

%package -n python3-%{pypi_name}-doc
Summary:        xBOUT documentation
Recommends:     python3-%{pypi_name}
%description -n python3-%{pypi_name}-doc
Documentation for xBOUT

%prep
%autosetup -n %{pypi_name}-%{version} -p 1
# Remove bundled egg-info
rm -rf xbout.egg-info
# boutdata doesn't have the provides
# animatplot is to old RHBZ#1885115
sed -e 's/boutdata.*//' -e 's/animatplot.*/animatplot/'  -i requirements.txt -i setup.cfg

%build
%py3_build
# generate html docs 
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%pytest xbout --long


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/xbout-%{version}-py?.*.egg-info

%files -n python3-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
%autochangelog
