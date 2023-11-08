%global pypi_name resolvelib
%global forgeurl https://github.com/sarugaku/resolvelib
%bcond tests 1

Name:           python-%{pypi_name}
Version:        1.0.1
%global tag %{version}
%forgemeta
Release:        1%{?dist}
Summary:        Resolve abstract dependencies into concrete ones

License:        ISC
URL:            %{forgeurl}
Source:         %{forgesource}
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
ResolveLib at the highest level provides a Resolver class that
includes dependency resolution logic. You give it some things, and a little
information on how it should interact with them, and it will spit out a
resolution result. Intended Usage :: import resolvelib Things I want to
resolve. requirements [...] Implement logic so the resolver understands the
requirement format. class...}

%description %_description


%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{_description}


%prep
%autosetup %{forgesetupargs}
# Use already packaged json5 instead of commentjson
sed -i 's|commentjson|json5|' \
    setup.cfg tests/functional/cocoapods/test_resolvers_cocoapods.py


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x test}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest -v


%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
* Fri Oct 20 2023 Maxwell G <maxwell@gtmx.me> - 1.0.1-1
- Update to 1.0.1.

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.5.5-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.5.5-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.5.5-2
- Rebuilt for Python 3.10

* Sat Apr 10 2021 Kevin Fenzi <kevin@scrye.com> - 0.5.5-1
- Initial package.
