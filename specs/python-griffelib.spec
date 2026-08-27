%bcond_without tests

Name:           python-griffelib
Version:        2.2.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python library to extract the structure and signatures of Python programs

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        ISC
URL:            https://github.com/mkdocstrings/griffe
Source:         %{pypi_source griffelib}

Patch0: 0001-tests-skip-tests-when-running-without-dependencies.patch

BuildArch:      noarch
BuildRequires:  python3-devel
# To pass the git related tests
BuildRequires:  git-core

%if %{with tests}
BuildRequires:  python3-pytest
%endif


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
Griffe is a Python library that extracts the structure, frame, and skeleton of Python projects. It parses source code to compute signatures for entire Python programs, which can be used to generate API documentation or detect breaking changes in an API.}

%description %_description

%package -n     python3-griffelib
Summary:        %{summary}

%description -n python3-griffelib %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-griffelib pypi


%prep
%autosetup -p3 -n griffelib-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x pypi -g dev


%build
%pyproject_wheel


%install
%pyproject_install
# Automatically extracted from wheel
%pyproject_save_files -l griffe


%check
%pyproject_check_import
%if %{with tests}
%pytest -v
%endif


%files -n python3-griffelib -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
