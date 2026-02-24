%bcond tests 1
%global forgeurl https://github.com/repo-helper/hatch-requirements-txt
# Includes test fixes for newer hatchling and packaging versions.
%global version0 0.4.1
%global commit caf885b14f7b6515c5a421a6b070e4aea0fd4d0b
%global date 20260127

Name:           python-hatch-requirements-txt
%forgemeta
Version:        %{forgeversion}
Release:        %autorelease
Summary:        Hatchling plugin to read project dependencies from requirements.txt

License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}

BuildArch:      noarch

BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  %{py3_dist coincidence}
BuildRequires:  %{py3_dist pkginfo}
BuildRequires:  %{py3_dist pytest}
%endif


%description
%{summary}.


%package -n python3-hatch-requirements-txt
Summary:        %{summary}

%description -n python3-hatch-requirements-txt
%{summary}.


%prep
%autosetup -p1 %{forgesetupargs}
# pytest-timeout is not needed to run tests in the RPM build environment
sed -i '/^timeout =/d' tox.ini
# Remove unnecessary shebangs
find hatch_requirements_txt/ -type f ! -executable -name '*.py' -print \
    -exec sed -i -e '1{\@^#!.*@d}' '{}' +


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files hatch_requirements_txt


%check
%pyproject_check_import
%if %{with tests}
%pytest
%endif


%files -n python3-hatch-requirements-txt -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
%autochangelog
