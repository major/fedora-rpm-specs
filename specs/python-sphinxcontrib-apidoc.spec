%global pypi_name sphinxcontrib-apidoc


Name:           python-%{pypi_name}
Version:        0.5.0
Release:        %autorelease
Summary:        A Sphinx extension for running 'sphinx-apidoc' on each build

License:        LicenseRef-Callaway-BSD
URL:            http://www.sphinx-doc.org/
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-sphinx

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-pytest
BuildRequires:  python3-sphinx
BuildRequires:  python3-setuptools

%global common_desc \
This package contains Sphinx extension for running sphinx-apidoc_ \
on each build.Overview *sphinx-apidoc* is a tool for automatic generation \
of Sphinx sources that, using the autodoc <sphinx_autodoc>_ extension, \
documents a whole package in the style of other automatic API documentation \
tools. *sphinx-apidoc* does not actually build documentation - rather it \
simply generates it.

%description
%common_desc

%package -n python3-%{pypi_name}
Summary:    %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:   python3-pbr
Requires:   python3-sphinx

%description -n python3-%{pypi_name}
%common_desc


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build

%py3_build

%install

%py3_install

# %check
# FIXME(chkumar246): Tests are broken in current version, So
# disabling it, Once new version will be available. We will
# add it.
# py.test ||
# %if %{with python3}
# py.test-3 ||
# %endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/sphinxcontrib_apidoc*nspkg.pth
%{python3_sitelib}/sphinxcontrib/apidoc
%{python3_sitelib}/sphinxcontrib_apidoc-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
