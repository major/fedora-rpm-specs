Name:       python-quantities
Version:    0.14.0
Release:    %autorelease
Summary:    Support for physical quantities with units, based on numpy

License:    BSD-3-Clause
URL:        http://python-quantities.readthedocs.io/
Source0:    %{pypi_source quantities}

BuildArch:      noarch


%global _description\
Quantities is designed to handle arithmetic and conversions of physical\
quantities, which have a magnitude, dimensionality specified by various units,\
and possibly an uncertainty. See the tutorial for examples. Quantities builds\
on the popular numpy library and is designed to work with numpy ufuncs, many of\
which are already supported. Quantities is actively developed, and while the\
current features and API are stable, test coverage is incomplete so the package\
is not suggested for mission-critical applications.

%description %_description

%package -n python3-quantities
Summary:    Support for physical quantities with units, based on numpy
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description -n python3-quantities %_description

%prep
%autosetup -n quantities-%{version}

# remove spurious
sed -i '/python (>=3.7)/ d' setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files quantities

%check
PY_IGNORE_IMPORTMISMATCH=1 %{pytest}

%files -n python3-quantities -f %{pyproject_files}
%doc CHANGES.txt README.rst
%license doc/user/license.rst

%changelog
%autochangelog
