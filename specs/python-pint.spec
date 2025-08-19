# There is a dependency cycle with xarray.
# F43FailsToInstall: python3-xarray+io, python3-xarray
# https://bugzilla.redhat.com/show_bug.cgi?id=2372200
%bcond xarray 0
# Not yet packaged: python-uncertainties
%bcond uncertainties 0
# Requires babel <= 2.8; F42 has 2.16.0
%bcond babel 0
# Not yet packaged: python-pint-pandas
%bcond pandas 0
# Not yet packaged: python-mip
%bcond mip 0
# F43FailsToInstall: python3-dask+array, python3-dask+bag,
# python3-dask+dataframe, python3-dask+delayed, python3-dask+distributed,
# python3-dask
# https://bugzilla.redhat.com/show_bug.cgi?id=2371852
%bcond dask 0

Name:           python-pint
Version:        0.25
Release:        %autorelease
Summary:        Physical quantities module

License:        BSD-3-Clause
URL:            https://github.com/hgrecco/pint
Source:         %{pypi_source pint}

BuildArch:      noarch

# To manipulate pyproject.toml
BuildRequires:  tomcli

%global _description %{expand:
Pint is a Python package to define, operate and manipulate physical quantities:
the product of a numerical value and a unit of measurement. It allows
arithmetic operations between them and conversions from and to different units.

It is distributed with a comprehensive list of physical units, prefixes and
constants.}

%description %{_description}

%package -n python3-pint
Summary:        %{summary}

%description -n python3-pint %{_description}

%pyproject_extras_subpkg -n python3-pint numpy
%if %{with xarray}
%pyproject_extras_subpkg -n python3-pint xarray
%endif
%if %{with dask}
%pyproject_extras_subpkg -n python3-pint dask
%endif
%if %{with uncertainties}
%pyproject_extras_subpkg -n python3-pint uncertainties
%endif
%if %{with babel}
%pyproject_extras_subpkg -n python3-pint babel
%endif
%if %{with pandas}
%pyproject_extras_subpkg -n python3-pint pandas
%endif
%if %{with mip}
%pyproject_extras_subpkg -n python3-pint mip
%endif
%pyproject_extras_subpkg -n python3-pint matplotlib

%prep
%autosetup -n pint-%{version} -p1

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
tomcli set pyproject.toml lists delitem project.optional-dependencies.test \
    pytest-cov

# This module is executable in the source, and it might make sense for upstream
# to run it directly as a script during development, but this package will
# install it in site-packages without the executable bit set, so it doesn’t
# make sense for it to have a shebang. Package users will run it via the
# generated pint-convert entry point instead.
sed -r -i '1{/^#!/d}' pint/pint_convert.py

%generate_buildrequires
%{pyproject_buildrequires \
    -x numpy \
%if %{with uncertainties}
    -x uncertainties \
%endif
%if %{with babel}
    -x babel \
%endif
%if %{with pandas}
    -x pandas \
%endif
%if %{with xarray}
    -x xarray \
%endif
%if %{with dask}
    -x dask \
%endif
%if %{with mip}
    -x mip \
%endif
    -x matplotlib \
    -x test-all }

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pint

%check
# -rs: print reasons for skipped tests
%pytest -rs

%files -n python3-pint -f %{pyproject_files}
%{_bindir}/pint-convert

%changelog
%autochangelog
