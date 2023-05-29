# Let’s try to build this as early as we can, since it’s a dependency for
# some important libraries, such as python-platformdirs.
%bcond_with bootstrap
%if %{without bootstrap}
%bcond_without tests
%else
%bcond_with tests
%endif

Name:           python-hatch-vcs
Version:        0.3.0
Release:        %autorelease
Summary:        Hatch plugin for versioning with your preferred VCS

# SPDX
License:        MIT
URL:            https://github.com/ofek/hatch-vcs
Source:         %{pypi_source hatch_vcs}

BuildArch:      noarch

# Work with setuptools_scm 7.1 (fix #25)
# https://github.com/ofek/hatch-vcs/pull/26
Patch:          %{url}/pull/26.patch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  git-core
%endif

%global common_description %{expand:
This provides a plugin for Hatch that uses your preferred version control
system (like Git) to determine project versions.}

%description %{common_description}


%package -n python3-hatch-vcs
Summary:        %{summary}

%description -n python3-hatch-vcs %{common_description}


%prep
%autosetup -n hatch_vcs-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files hatch_vcs


%check
%if %{with tests}
%pytest
%else
%pyproject_check_import
%endif


%files -n python3-hatch-vcs -f %{pyproject_files}
%doc HISTORY.md
%doc README.md


%changelog
%autochangelog
