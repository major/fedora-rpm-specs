%global forgeurl https://github.com/python-quantities/python-quantities/
Name:       python-quantities
Version:    0.15.0
Release:    %autorelease
Summary:    Support for physical quantities with units, based on numpy

%forgemeta

License:    BSD-3-Clause
URL:        %forgeurl
Source0:    %forgesource

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
%forgesetup
# Work around confusion with SPECPARTS directory looking like a package to
# setuptools automatic discovery:
# https://bugzilla.redhat.com/show_bug.cgi?id=2213013#c2
rm -rf SPECPARTS

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%pyproject_save_files quantities

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
PY_IGNORE_IMPORTMISMATCH=1 %{pytest}

%files -n python3-quantities -f %{pyproject_files}
%doc CHANGES.txt README.rst
%license doc/user/license.rst

%changelog
%autochangelog
