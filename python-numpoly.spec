%global desc %{expand: \
Numpoly is a generic library for creating, manipulating and evaluating arrays
of polynomials.}

Name:       python-numpoly
Version:    1.2.7
Release:    %autorelease
Summary:    Polynomials as a numpy datatype
# spdx
License:    BSD-2-Clause
URL:        https://github.com/jonathf/numpoly

# Use the github source to build this package.
Source0:    %{url}/archive/v%{version}/numpoly-%{version}.tar.gz
BuildArch:  noarch
# Tests fail on 32 bit arches.
# Only chaospy depends on it, and chaospy does not support 32 bit arches.
# So also dropping them here.
ExcludeArch:    %{ix86} %{arm32}

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
%autosetup -n numpoly-%{version}
# Workaround for https://github.com/rpm-software-management/rpm/issues/2532:
rm -rf SPECPARTS

%generate_buildrequires
%pyproject_buildrequires -x dev-dependencies

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files numpoly

%check
%{pytest} test

%files -n python3-numpoly -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
