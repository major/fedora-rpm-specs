%global desc %{expand: \
Numpoly is a generic library for creating, manipulating and evaluating
arrays of polynomials based on `numpy.ndarray` objects.

- Intuitive interface for users experienced with numpy, as the library
  provides a high level of compatibility with the `numpy.ndarray`,
  including fancy indexing, broadcasting, `numpy.dtype`, vectorized
  operations to name a few
- Computationally fast evaluations of lots of functionality inherent
  from numpy
- Vectorized polynomial evaluation
- Support for arbitrary number of dimensions
- Native support for lots of `numpy.<name>` functions using numpy’s
  compatibility layer (which also exists as `numpoly.<name`> equivalents)
- Support for polynomial division through the operators `/`, `%` and
  `divmod`
- Extra polynomial specific attributes exposed on the polynomial
  objects like `poly.exponents`, `poly.coefficients`,
  `poly.indeterminants` etc.
- Polynomial derivation through functions like `numpoly.derivative`,
  `numpoly.gradient`, `numpoly.hessian` etc.
- Decompose polynomial sums into vector of addends using
  `numpoly.decompose`
- Variable substitution through `numpoly.call`}

%global forgeurl https://github.com/jonathf/numpoly

Name:       python-numpoly
Version:    1.2.11
Release:    %autorelease
Summary:    Polynomials as a numpy datatype
%forgemeta
# spdx
License:    BSD-2-Clause
URL:        %forgeurl

# Use the github source to build this package.
Source0:    %forgesource
BuildArch:  noarch
# Tests fail on 32 bit arches.
# Only chaospy depends on it, and chaospy does not support 32 bit arches.
# So also dropping them here.
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
# extra dev dep for tests, do not include all the linters etc.
BuildRequires:  python3dist(sympy)

%description
%{desc}

%package -n     python3-numpoly
Summary:        %{summary}

%description -n python3-numpoly
%{desc}

%prep
%forgeautosetup
# Workaround for https://github.com/rpm-software-management/rpm/issues/2532:
rm -rf SPECPARTS

%generate_buildrequires
%pyproject_buildrequires -x dev-dependencies

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l numpoly

%check
%pytest

%files -n python3-numpoly -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
