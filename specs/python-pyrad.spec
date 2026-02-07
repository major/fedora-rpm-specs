%global pypi_name pyrad
%global common_description %{expand:
This is an implementation of a RADIUS client as described in RFC2865. It takes
care of all the details like building RADIUS packets, sending them and decoding
responses.}

Name:           python-%{pypi_name}
Version:        2.5.4
Release:        %autorelease
Summary:        Python RADIUS client
License:        BSD-3-Clause
URL:            https://github.com/pyradius/%{pypi_name}
VCS:            git:%{url}.git
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-twisted
Requires:       python3-twisted
BuildSystem:    pyproject
BuildOption(install): -l %{pypi_name}

%description  %{common_description}

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name} %{common_description}

%prep -a
# Fedora-specific - to avoid picking up dependencies from these files
chmod 644 example/acct.py example/auth.py example/client-coa.py example/coa.py example/server.py

%build -a
sphinx-build -b html docs/source docs/_build/html/ -d docs/_build/doctrees/

%install -a
rm -f docs/_build/html/.buildinfo
rm -rf %{buildroot}%{python3_sitelib}/example/
rm -rf %{buildroot}%{python3_sitelib}/docs/

%check -a
%python3 -m unittest -v

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CHANGES.rst README.rst example/ docs/_build/html/

%changelog
%autochangelog
