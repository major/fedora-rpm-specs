%bcond tests 1

Name:           python-platformdirs
Version:        4.13.3
Release:        %autorelease
Summary:        A small Python package for determining appropriate platform-specific dirs
License:        MIT
URL:            https://github.com/platformdirs/platformdirs
Source:         %{pypi_source platformdirs}
BuildArch:      noarch

%global common_description %{expand:
When writing desktop application, finding the right location to store user data
and configuration varies per platform.  Even for single-platform apps, there
may by plenty of nuances in figuring out the right location.  This kind of
thing is what the platformdirs package is for.}


%description %{common_description}


%package -n python3-platformdirs
Summary:        %{summary}

%description -n python3-platformdirs %{common_description}


%prep
%autosetup -n platformdirs-%{version}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
%pyproject_patch_dependency covdefaults:ignore
%pyproject_patch_dependency diff-cover:ignore
%pyproject_patch_dependency pytest-cov:ignore


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:--dependency-groups test}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files --assert-license platformdirs


%check
%pyproject_check_import
%if %{with tests}
# Upstream uses tox, but we don’t use it, to avoid a build dependency loop
# platformdirs <- virtualenv <- tox
%pytest
%endif


%files -n python3-platformdirs -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
