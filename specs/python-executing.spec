# Running the tests requires ipython which requires python-stack-data which
# introduces a circular dependency back on python-executing
%bcond bootstrap 0
# When tests are enabled, should we also run “very slow” tests?
%bcond slow_tests 1

%global forgeurl https://github.com/alexmojaki/executing

Name:           python-executing
Version:        2.2.1
Release:        %autorelease
Summary:        Python library for inspecting the current frame run footprint

%forgemeta

License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Get information about what a Python frame is currently doing, particularly the
AST node being executed}

%description %_description

%package -n python3-executing
Summary:        %{summary}

%description -n python3-executing %_description


%prep
%dnl %autosetup -p1 -n executing-%{version}
%autosetup -p1 -n executing-%{version}
# Remove coverage and coverage-enable-subprocess
# from testing deps.
sed -Ei "/coverage-?/d" setup.cfg


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION="%(echo '%{version}' | cut -d '^' -f 1)"
%pyproject_buildrequires %{!?with_bootstrap:-t}


%build
export SETUPTOOLS_SCM_PRETEND_VERSION="%(echo '%{version}' | cut -d '^' -f 1)"
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files executing


%check
%pyproject_check_import
%if %{without bootstrap}
%if %{with slow_tests}
export EXECUTING_SLOW_TESTS=1
%endif
%tox -- -- -rs
%endif


%files -n python3-executing -f %{pyproject_files}
%doc README.md
%license LICENSE.txt


%changelog
%autochangelog
