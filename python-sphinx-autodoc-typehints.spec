%global pypi_name sphinx-autodoc-typehints

Name:           python-%{pypi_name}
Version:        1.17.0
Release:        %autorelease
Summary:        Type hints support for the Sphinx autodoc extension

License:        MIT
URL:            https://github.com/agronholm/sphinx-autodoc-typehints
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This extension allows you to use Python 3 annotations for documenting
acceptable argument types and return value types of functions.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
#BuildRequires:  python3-pytest

Requires:       python3-sphinx
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This extension allows you to use Python 3 annotations for documenting
acceptable argument types and return value types of functions.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -Rf requirements.txt test-requirements.txt *.egg-info

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py3_install

#%check
#export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
#PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests

%files -n python3-%{pypi_name}
%{python3_sitelib}/sphinx_autodoc_typehints-%{version}*.egg-info/
%{python3_sitelib}/sphinx_autodoc_typehints/

%changelog
%autochangelog

