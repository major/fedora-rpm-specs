%bcond tests 1
%global forgeurl https://github.com/pydantic/pydantic-extra-types

Name:           python-pydantic-extra-types
Version:        2.4.1
%forgemeta
Release:        1%{?dist}
Summary:        Extra types for Pydantic

License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}

# Allow python-ulid 2.x on Python 3.9 and later
# https://github.com/pydantic/pydantic-extra-types/pull/131
#
# Fixes:
#
# Please support python-ulid 2.x
# https://github.com/pydantic/pydantic-extra-types/issues/130
#
# Cherry-picked to v2.4.0.
Patch:          0001-Allow-python-ulid-2.x-on-Python-3.9-and-later.patch

BuildArch:      noarch

BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  %{py3_dist dirty-equals}
BuildRequires:  %{py3_dist pytest}
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
%autosetup -p1 %{forgesetupargs}


%generate_buildrequires
%pyproject_buildrequires -x all


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pydantic_extra_types


%check
%if %{with tests}
%pytest -Wdefault
%endif


%files -n python3-pydantic-extra-types -f %{pyproject_files}
%doc README.md
%license LICENSE

%pyproject_extras_subpkg -n python3-pydantic-extra-types all


%changelog
* Wed Jan 31 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.4.1-1
- Update to 2.4.1

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Sep 12 2023 Maxwell G <maxwell@gtmx.me> - 2.1.0-1
- Initial package. Closes rhbz#2249133.
