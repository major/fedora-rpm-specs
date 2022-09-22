# Let’s try to build this as early as we can, since it’s a dependency for
# python-userpath.
%bcond_with bootstrap
%if %{without bootstrap}
%bcond_without tests
%else
%bcond_with tests
%endif

Name:           python-hatch-vcs
Version:        0.2.0
Release:        %autorelease
Summary:        Hatch plugin for versioning with your preferred VCS

License:        MIT
URL:            https://github.com/ofek/hatch-vcs
Source0:        %{pypi_source hatch_vcs}

BuildArch:      noarch

# Fix test compatibility with setuptools_scm 7
# https://github.com/ofek/hatch-vcs/pull/9
#
# Fixes:
#
# Compatibility with setuptools_scm 7
# https://github.com/ofek/hatch-vcs/issues/8
Patch:          %{url}/pull/9.patch

BuildRequires:  python3-devel
# RHBZ#1985340, RHBZ#2076994
BuildRequires:  pyproject-rpm-macros >= 1.2.0

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
%license LICENSE.txt
%doc HISTORY.md
%doc README.md


%changelog
%autochangelog
