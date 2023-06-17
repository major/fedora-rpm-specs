%bcond tests 1
%bcond docs 1

%global common_description %{expand:
Use this package if you use pyOpenSSL and don’t want to be MITMed, or if you
want to verify that a PyCA cryptography certificate is valid for a certain
hostname or IP address.  service-identity aspires to give you all the tools you
need for verifying whether a certificate is valid for the intended purposes.
In the simplest case, this means host name verification.  However,
service-identity implements RFC 6125 fully and plans to add other relevant RFCs
too.}

Name:           python-service-identity
Version:        23.1.0
Release:        %autorelease
Summary:        Service identity verification for pyOpenSSL

License:        MIT
URL:            https://github.com/pyca/service-identity
Source:         %{pypi_source service_identity}
# Downstream-only patch to disable coverage
Patch:          0001-Remove-coverage-from-tests-extras.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%description %{common_description}

%package -n     python3-service-identity
Summary:        %{summary}

%description -n python3-service-identity %{common_description}

%package doc
Summary:        Documentation for %{name}

%description doc
%{common_description}

This is the documentation package for %{name}.

%pyproject_extras_subpkg -n python3-service-identity idna

%prep
%autosetup -p1 -n service_identity-%{version}

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x tests,idna} %{?with_docs:-x docs}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files service_identity

%if %{with docs}
# Previously the docs were built with PYTHONPATH=%%{pyproject_build_lib}, but
# that macro is now deprecated.  It also only works with setuptools, and
# upstream switched to hatchling.  Building the docs relies on the library
# being installed, so we have to do it here in %%install instead of in %%build.
PYTHONPATH=%{buildroot}%{python3_sitelib} sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%check
%if %{with tests}
%pytest -v
%else
%pyproject_check_import
%endif

%files -n python3-service-identity -f %{pyproject_files}
%doc README.md

%if %{with docs}
%files doc
%doc html
%license LICENSE
%endif

%changelog
%autochangelog
