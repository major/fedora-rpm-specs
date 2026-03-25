%global pypi_name stestr
%global with_doc 1

%global common_desc \
stestr is a fork of the testrepository that concentrates on being a \
dedicated test runner for python projects. The generic abstraction layers \
which enabled testr to work with any subunit emitting runner are gone. \
stestr hard codes python-subunit-isms into how it works.

Name:       python-%{pypi_name}
Version:    4.2.1
Release:    %autorelease
Summary:    A test runner runner similar to testrepository

License:    Apache-2.0
URL:        https://pypi.python.org/pypi/stestr
Source0:    %pypi_source
BuildArch:  noarch


%description
%{common_desc}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        A test runner runner similar to testrepository

BuildRequires:    python%{python3_pkgversion}-devel
BuildRequires:    git-core
# Required for testing
BuildRequires:    python%{python3_pkgversion}-pytest
BuildRequires:    python%{python3_pkgversion}-ddt


%description -n python%{python3_pkgversion}-%{pypi_name}
%{common_desc}


%if 0%{?with_doc}
%package -n python-%{pypi_name}-doc
Summary:        stestr documentation


%description -n python-%{pypi_name}-doc
%{common_desc}

It contains the documentation for stestr.
%endif


%prep
%autosetup -n %{pypi_name}-%{version} -S git


%generate_buildrequires
%pyproject_buildrequires -x sql


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{pypi_name}
# compat symlinks
ln -s stestr %{buildroot}/%{_bindir}/stestr-3
ln -s stestr-3 %{buildroot}/%{_bindir}/stestr-%{python3_version}


%check
%pyproject_check_import -e stestr.tests.*
%pytest -k "not test_empty_with_pretty_out"


%files -n python%{python3_pkgversion}-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%{_bindir}/stestr*


# Retaining doc package for now, though upstream docs are stale.
%if 0%{?with_doc}
%files -n python-%{pypi_name}-doc
%license LICENSE
%doc README.rst
%endif


%changelog
%autochangelog
