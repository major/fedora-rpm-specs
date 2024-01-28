%bcond tests 1
%global forgeurl https://github.com/repo-helper/hatch-requirements-txt

Name:           python-hatch-requirements-txt
Version:        0.4.0
%forgemeta
Release:        4%{?dist}
Summary:        Hatchling plugin to read project dependencies from requirements.txt

License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}
Patch:          %{url}/pull/47.patch#/tests-handle-hatchling-dependency-spec-formatting-ch.patch

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
* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 15 2023 Maxwell G <maxwell@gtmx.me> - 0.4.0-2
- Fix test failures with latest hatchling release

* Thu Oct 19 2023 Maxwell G <maxwell@gtmx.me> - 0.4.0-1
- Initial package. Closes rhbz#2244976.
