%bcond_without tests

%global srcname progressbar2

%global desc %{expand: \
A text progress bar is typically used to display the progress of a long running
operation, providing a visual cue that processing is underway.

The ProgressBar class manages the current progress, and the format of the line
is given by a number of widgets.

The progressbar module is very easy to use, yet very powerful. It will also
automatically enable features like auto-resizing when the system supports it.}

Name:           python-%{srcname}
Version:        4.5.0
Release:        %autorelease
Summary:        Library to provide visual progress to long running operations

# SPDX
License:        BSD-3-Clause
URL:            https://github.com/WoLpH/python-progressbar
Source0:        %pypi_source

BuildArch:      noarch
BuildRequires:  python3-devel

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{summary}
Requires:       %{py3_dist python-utils}
Requires:       %{py3_dist six}
BuildRequires:  %{py3_dist python-utils}
BuildRequires:  %{py3_dist six}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist pytest}
%if %{with tests}
BuildRequires:  %{py3_dist freezegun} >= 0.3.10
%endif

# obsolete python-progressbar
Obsoletes:      python3-progressbar < 2.3-14
Provides:       python3-progressbar == %{version}

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}


%prep
%autosetup -n %{srcname}-%{version} -p1
rm -rfv %{srcname}.egg-info

find . -name '*.pyc' -print -delete
find . -name '*.swp' -print -delete
rm -rfv tests/__pycache__/

# do not run coverage in pytest
sed -i -E '/--(no-)?cov/d' pytest.ini

# remove linters etc from requirements
sed -i \
    -e '/flake8/ d' \
    -e '/pytest-cov/ d' \
    -e '/pytest-mypy/ d' \
    -e '/sphinx/ d' \
    -e '/pywin32/ d' \
    pyproject.toml

cat pyproject.toml

# required for tests, but not included in deps, and apparently no way to
# include stuff from "project.optional-dependencies" using
# pyproject_buildrequires..
cat > requirements.txt << EOF
dill
EOF
cat requirements.txt

%generate_buildrequires
%pyproject_buildrequires requirements.txt

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l progressbar

%check
%if %{with tests}
PYTHONPATH=. %pytest tests
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%{_bindir}/progressbar

%changelog
%autochangelog
