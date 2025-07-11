%global pypi_name pymeeus

Name:           python-%{pypi_name}
Version:        0.5.11
Release:        %autorelease
Summary:        Python implementation of Jean Meeus astronomical routines

# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:        LGPL-3.0-only
URL:            https://github.com/architest/pymeeus
Source0:        %{pypi_source PyMeeus}
Patch0:         0001-Fix-documentation-build-with-sphinx-8.patch
Patch1:         0002-fix-pytest-7-2-compatibility.patch
BuildArch:      noarch

%description
PyMeeus is a Python implementation of the astronomical algorithms described
in the classical book "Astronomical Algorithms, 2nd Edition, Willmann-Bell
Inc. (1998)" by Jean Meeus.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%generate_buildrequires
%pyproject_buildrequires

%description -n python3-%{pypi_name}
PyMeeus is a Python implementation of the astronomical algorithms described
in the classical book "Astronomical Algorithms, 2nd Edition, Willmann-Bell
Inc. (1998)" by Jean Meeus.

%package -n python-%{pypi_name}-doc
Summary:        %{name} documentation

BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

%description -n python-%{pypi_name}-doc
Documentation for %{name}.

%prep
%autosetup -n PyMeeus-%{version} -p1
rm -rf %{pypi_name}.egg-info

%build
%pyproject_wheel
PYTHONPATH=${PWD} sphinx-build-3 docs/source html
rm -rf html/.{doctrees,buildinfo,nojekyll}

%install
%pyproject_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests

%files -n python3-%{pypi_name}
%license LICENSE.txt COPYING.LESSER
%doc docs/README.txt README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/pymeeus-%{version}.dist-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE.txt COPYING.LESSER

%changelog
%autochangelog
