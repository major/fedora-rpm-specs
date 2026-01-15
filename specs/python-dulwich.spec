%global srcname dulwich
%global __provides_exclude_from ^(%{python3_sitearch}/.*\\.so)$

Name:           python-%{srcname}
Version:        0.25.2
Release:        %autorelease
Summary:        Python implementation of the Git file formats and protocols

License:        GPL-2.0-or-later OR Apache-2.0
URL:            https://www.dulwich.io/
Source0:        %{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  cargo-rpm-macros

BuildRequires:  python3-docutils
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-epytext

%description
Dulwich is a Python implementation of the Git file formats and
protocols. The project is named after the village in which Mr. and
Mrs. Git live in the Monty Python sketch.

%package -n python3-%{srcname}
Summary:        %{summary}

# Apache-2.0
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
License:        (GPL-2.0-or-later OR Apache-2.0) AND Apache-2.0 AND MIT AND (MIT OR Apache-2.0) AND (Unlicense OR MIT)

%description -n python3-%{srcname}
Dulwich is a Python implementation of the Git file formats and
protocols. The project is named after the village in which Mr. and
Mrs. Git live in the Monty Python sketch.

%package -n %{name}-doc
Summary:        The %{name} documentation

%description -n %{name}-doc
Documentation for %{name}.

%prep
%autosetup -n %{srcname}-%{version}
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -a -t
%pyproject_buildrequires

%build
%pyproject_wheel
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
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
%doc README.rst
%license COPYING
%license LICENSE.dependencies
%{_bindir}/dul-*
%{_bindir}/%{srcname}
%exclude %{python3_sitearch}/%{srcname}/tests*

%files -n %{name}-doc
%doc README.rst
%license COPYING
%doc html

%changelog
%autochangelog
