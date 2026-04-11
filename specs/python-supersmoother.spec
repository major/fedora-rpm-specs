%global srcname supersmoother

Name:           python-%{srcname}
Version:        0.4
Release:        %autorelease
Summary:        Python implementation of Friedman's Supersmoother

License:        BSD-2-Clause
URL:            https://github.com/jakevdp/supersmoother
Source0:        %{pypi_source %{srcname}}

# Compatibility with pytest 8.4.2
# The patch was modified to make it applicable
# https://github.com/jakevdp/supersmoother/commit/d9ee40a.patch
Patch:          pytest-8.4.2.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist pytest}
# Required for tests
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist scipy}

%description
This is an efficient implementation of Friedman’s SuperSmoother based in
Python. It makes use of numpy for fast numerical computation.

%package -n python3-%{srcname}
Summary:    %{summary}

%description -n python3-%{srcname}
This is an efficient implementation of Friedman’s SuperSmoother based in
Python. It makes use of numpy for fast numerical computation.

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l supersmoother

%check
%pyproject_check_import -t
# test_since_cv is skipped, it also fails in upstream
%pytest -k "not test_sine_cv"

%files -n python3-%{srcname} -f %{pyproject_files}
%doc CHANGES.md README.md

%changelog
%autochangelog
