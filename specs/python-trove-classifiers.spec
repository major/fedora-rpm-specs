Name:           python-trove-classifiers
Version:        2025.1.10.15
Release:        2%{?dist}
Summary:        Canonical source for classifiers on PyPI (pypi.org)

License:        Apache-2.0
URL:            https://github.com/pypa/trove-classifiers
Source:         %{pypi_source trove_classifiers}

# Drop dependency on calver which is not packaged in Fedora.
# This patch is rebased version of upstream PR:
# https://github.com/pypa/trove-classifiers/pull/126/commits/809156bb35852bcaa1c753e0165f1814f2bcedf6
Patch:          Move-to-PEP-621-declarative-metadata.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
Canonical source for classifiers on PyPI.
Classifiers categorize projects per PEP 301. Use this package to validate
classifiers in packages for PyPI upload or download.
}

%description %_description

%package -n python3-trove-classifiers
Summary:        %{summary}

%description -n python3-trove-classifiers %_description


%prep
%autosetup -p1 -n trove_classifiers-%{version}
# Replace @@VERSION@@ with %%version
%writevars -f pyproject.toml version


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files trove_classifiers


%check
%pytest


%files -n python3-trove-classifiers -f %{pyproject_files}
%doc README.*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2025.1.10.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 10 2025 Packit <hello@packit.dev> - 2025.1.10.15-1
- Update to 2025.1.10.15
- Resolves rhbz#2336967

* Tue Jan 07 2025 Packit <hello@packit.dev> - 2025.1.7.14-1
- Update to 2025.1.7.14
- Resolves rhbz#2335883

* Fri Nov 01 2024 Tomáš Hrnčiar <thrnciar@redhat.com> - 2024.10.21.16-2
- Update to 2024.10.21.16
- Resolves rhbz#2319232

* Sun Oct 13 2024 Packit <hello@packit.dev> - 2024.10.13-1
- Update to 2024.10.13
- Resolves rhbz#2318030

* Thu Sep 12 2024 Packit <hello@packit.dev> - 2024.9.12-1
- Update to 2024.9.12
- Resolves rhbz#2312038

* Wed Aug 21 2024 Packit <hello@packit.dev> - 2024.7.2-1
- Update to 2024.7.2
- Resolves rhbz#2295582

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2024.5.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2024.5.22-2
- Rebuilt for Python 3.13

* Fri May 31 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2024.5.22-1
- Update to 2024.5.22. Closes RBHZ#2271418

* Sun Mar 3 2024 Packit <hello@packit.dev> - 2024.3.3-1
- Update to 2024.3.3
- Resolves rhbz#2248519

* Tue Feb 27 2024 Packit <hello@packit.dev> - 2024.2.23-1
- Update to 2024.2.23
- Resolves rhbz#2248519

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.10.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.10.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 19 2023 Maxwell G <maxwell@gtmx.me> - 2023.10.18-1
- Update to 2023.10.18. Fixes rhbz#2244676.

* Wed Oct 4 2023 Maxwell G <maxwell@gtmx.me> - 2023.9.19-1
- Update to 2023.9.19. Fixes rhbz#2239555.

* Mon Aug 7 2023 Maxwell G <maxwell@gtmx.me> - 2023.8.7-1
- Update to 2023.8.7. Fixes rhbz#2229834.

* Thu Jul 27 2023 Maxwell G <maxwell@gtmx.me> - 2023.7.6-1
- Update to 2023.7.6. Fixes rhbz#2220945.

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2023.5.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2023.5.24-2
- Rebuilt for Python 3.12

* Wed Jun 7 2023 Maxwell G <maxwell@gtmx.me> - 2023.5.24-1
- Update to 2023.5.24. Fixes rhbz#2189711.

* Wed Apr 26 2023 Tomáš Hrnčiar <thrnciar@redhat.com> - 2023.4.25-1
- Update to 2023.4.25
Fixes: rhbz#2177081
Fixes: rhbz#2187710

* Tue Feb 21 2023 Tomáš Hrnčiar <thrnciar@redhat.com> - 2023.2.20-1
Initial package

