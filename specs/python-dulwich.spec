%global srcname dulwich
%global __provides_exclude_from ^(%{python3_sitearch}/.*\\.so)$
%global debug_package %{nil}

Name:           python-%{srcname}
Version:        0.24.7
Release:        %autorelease
Summary:        Python implementation of the Git file formats and protocols

License:        GPL-2.0-or-later OR Apache-2.0
URL:            https://www.dulwich.io/
Source0:        %{pypi_source}

BuildRequires:  gcc
BuildRequires:  crate(pyo3-build-config/default)

%description
Dulwich is a pure-Python implementation of the Git file formats and
protocols. The project is named after the village in which Mr. and
Mrs. Git live in the Monty Python sketch.

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools-rust

%description -n python3-%{srcname}
Dulwich is a pure-Python implementation of the Git file formats and
protocols. The project is named after the village in which Mr. and
Mrs. Git live in the Monty Python sketch.

%package -n %{name}-doc
Summary:        The %{name} documentation

BuildRequires:  python3-sphinx
BuildRequires:  python3-docutils
BuildRequires:  python3-sphinx-epytext

%description -n %{name}-doc
Documentation for %{name}.

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel
PYTHONPATH=${PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{srcname}
# Remove extra copy of text docs
rm -rf %{buildroot}%{python3_sitearch}/docs/tutorial/

%check
# test_copy and test_receive_pack are failing for a long time (https://github.com/jelmer/dulwich/issues/988)
# tests/contrib/test_swift_smoke.py is ignored because geventhttpclient is not packaged in Fedora
# 8 more tests fail on 3.14 for now.
#%{python3} -m pytest tests --ignore=tests/contrib/test_swift_smoke.py -k "not test_copy and not test_receive_pack"

%files -n python3-%{srcname} -f %{pyproject_files}
%doc AUTHORS README.rst
%license COPYING
%{_bindir}/dul-*
%{_bindir}/%{srcname}
%exclude %{python3_sitearch}/%{srcname}/tests*

%files -n %{name}-doc
%doc AUTHORS README.rst
%license COPYING
%doc html

%changelog
%autochangelog
