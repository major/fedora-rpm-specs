%bcond tests 1
%global forgeurl https://github.com/pydantic/pydantic-extra-types

Name:           python-pydantic-extra-types
Version:        2.10.2
%forgemeta
Release:        2%{?dist}
Summary:        Extra types for Pydantic

License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}

# Assume zoneinfo has system tzdata
#
# Downstream patch: in the system Python installation, zoneinfo is
# guaranteed to be importable and have system time zone data available, so
# we always use it, and do not check for the tzdata PyPI package.
#
# Since they will not be used (and https://pypi.org/project/tzdata/ is not
# packaged, because it "is intended to be a fallback for systems that do not
# have system time zone data installed (or don’t have it installed in a
# standard location"), we patch out the tzdata and pytz dependencies from the
# "all" extra in %%prep.
#
# All of this works because python3-libs depends on the system tzdata package.
Patch0:         0001-Assume-zoneinfo-has-system-tzdata.patch

# For Fedora 40 only: Revert ":sparkles: Adjust `test_json_schema()` for
# Pydantic 2.9 (#215)" (except changes to pyproject.txt, to reduce future
# conflicts). Fedora 40 will remain at Pydantic 2.8 since 2.9 contained a
# breaking change.
Patch140:       0001-Revert-sparkles-Adjust-test_json_schema-for-Pydantic.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  tomcli
%if %{with tests}
BuildRequires:  %{py3_dist dirty-equals}
BuildRequires:  %{py3_dist pytest}
# We patched this out of the “all” extra, but it is still a test dependency.
BuildRequires:  %{py3_dist pytz}
%endif

%global _description %{expand:
A place for pydantic types that probably shouldn't exist in the main pydantic
library.}
# this is here to fix vim's syntax highlighting

%description %_description


%package -n python3-pydantic-extra-types
Summary:        %{summary}

%description -n python3-pydantic-extra-types %_description


%prep
%autosetup %{forgesetupargs} -N
%autopatch -p1 -M99
%if 0%{?fc40}
%patch -P140 -p1
%endif
# See notes above 0001-Assume-zoneinfo-has-system-tzdata.patch.
tomcli set pyproject.toml lists delitem --type regex --no-first \
    project.optional-dependencies.all '(tzdata|pytz)\b.*'


%generate_buildrequires
%pyproject_buildrequires -x all


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pydantic_extra_types


%check
%if %{with tests}
%pytest -Wdefault -v
%endif


%files -n python3-pydantic-extra-types -f %{pyproject_files}
%doc README.md
%license LICENSE

%pyproject_extras_subpkg -n python3-pydantic-extra-types all phonenumbers pycountry semver python_ulid pendulum


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 15 2025 Benjamin A. Beasley <code@musicinmybrain.net> - 2.10.2-1
- Update to 2.10.2. Fixes rhbz#2338374.

* Thu Dec 19 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.10.1-1
- Update to 2.10.1. Fixes rhbz#2330807.

* Mon Oct 21 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.10.0-2
- Another patch for python-ulid 3.0.0 (fix RHBZ#2320153)

* Wed Oct 16 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.10.0-1
- Update to 2.10.0 (close RHBZ#2319061)

* Sun Oct 13 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.9.0-5
- Allow python-ulid 3.0

* Wed Sep 11 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.9.0-4
- Adjust test_json_schema() for Pydantic 2.9

* Fri Aug 16 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.9.0-3
- Add a direct BuildRequires on pytz for the tests

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jul 05 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.9.0-1
- Update to 2.9.0. Fixes rhbz#2295691.
- Add missing extras metapackages

* Sat Jun 29 2024 Python Maint <python-maint@redhat.com> - 2.8.2-2
- Rebuilt for Python 3.13

* Sun Jun 16 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.8.2-1
- Update to 2.8.2. Fixes rhbz#2292564.

* Fri Jun 14 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.8.1-1
- Update to 2.8.1. Fixes rhbz#2292384.

* Tue Jun 04 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.8.0-1
- Update to 2.8.0. Fixes rhbz#2290380.

* Tue Apr 23 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.7.0-1
- Update to 2.7.0. Fixes rhbz#2276774.

* Sat Mar 2 2024 Maxwell G <maxwell@gtmx.me> - 2.6.0-1
- Update to 2.6.0. Fixes rhbz#2267402.

* Tue Feb 13 2024 Maxwell G <maxwell@gtmx.me> - 2.5.0-1
- Update to 2.5.0. Fixes rhbz#2261943.

* Wed Jan 31 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.4.1-1
- Update to 2.4.1

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Sep 12 2023 Maxwell G <maxwell@gtmx.me> - 2.1.0-1
- Initial package. Closes rhbz#2249133.
