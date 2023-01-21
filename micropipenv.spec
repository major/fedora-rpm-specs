Name:           micropipenv
Version:        1.4.5
Release:        2%{?dist}
Summary:        A simple wrapper around pip to support Pipenv and Poetry files

License:        LGPLv3+
URL:            https://github.com/thoth-station/%{name}
Source0:        %{url}/archive/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%py_provides    python3-%{name}

Recommends:     micropipenv+toml

%description
A lightweight wrapper for pip to support Pipenv and Poetry lock files or
converting them to pip-tools compatible output.

%pyproject_extras_subpkg -n %{name} toml

%prep
%autosetup
# Remove shebang line from the module
sed -i '1{\@^#!/usr/bin/env python@d}' %{name}.py

%generate_buildrequires
%pyproject_buildrequires -r -t -x toml

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}

%check
# skipped tests requires internet or checks pip version
%pytest -m "not online" -k "not test_check_pip_version and not test_install_invalid_toml_file"

%files -f %pyproject_files
%doc README.rst
%{_bindir}/micropipenv

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 11 2023 Lumír Balhar <lbalhar@redhat.com> - 1.4.5-1
- Update to 1.4.5 (rhbz#2159707)

* Mon Oct 31 2022 Lumír Balhar <lbalhar@redhat.com> - 1.4.4-1
- Update to 1.4.4
Resolves: rhbz#2138859

* Wed Oct 05 2022 Lumír Balhar <lbalhar@redhat.com> - 1.4.3-1
- Update to 1.4.3
Resolves: rhbz#2131986

* Mon Oct 03 2022 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-2
- Remove manual requirement of python3dist(toml),
  package and Recommend the [toml] extra instead

* Tue Aug 02 2022 Lumír Balhar <lbalhar@redhat.com> - 1.4.2-1
- Update to 1.4.2
Resolves: rhbz#2110900

* Tue Jul 26 2022 Lumír Balhar <lbalhar@redhat.com> - 1.4.1-1
- Update to 1.4.1
Resolves: rhbz#2110900

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 1.3.0-2
- Rebuilt for Python 3.11

* Wed Jun 08 2022 Lumír Balhar <lbalhar@redhat.com> - 1.3.0-1
- Update to 1.3.0
Resolves: rhbz#2083779

* Mon Feb 21 2022 Lumír Balhar <lbalhar@redhat.com> - 1.2.1-1
- Update to 1.2.1
Resolves: rhbz#2056449

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 05 2022 Lumír Balhar <lbalhar@redhat.com> - 1.2.0-1
- Update to 1.2.0

* Mon Oct 25 2021 Lumír Balhar <lbalhar@redhat.com> - 1.1.3-1
- Update to 1.1.3
Resolves: rhbz#2016285

* Wed Oct 06 2021 Lumír Balhar <lbalhar@redhat.com> - 1.1.2-1
- Update to 1.1.2
Resolves: rhbz#2006696

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 21 2021 Lumír Balhar <lbalhar@redhat.com> - 1.1.0-1
- Update to 1.1.0
Resolves: rhbz#1974255

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.4-2
- Rebuilt for Python 3.10

* Tue May 04 2021 Lumír Balhar <lbalhar@redhat.com> - 1.0.4-1
- Update to 1.0.4
Resolves: rhbz#1955039

* Fri Mar 12 2021 Karolina SUrma <ksurma@redhat.com> - 1.0.3-1
- Update to 1.0.3
Resolves: rhbz#1937471

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 11 2020 Lumír Balhar <lbalhar@redhat.com> - 1.0.2-1
- Update to 1.0.2 (#1906430)

* Tue Nov 10 2020 Lumír Balhar <lbalhar@redhat.com> - 1.0.1-1
- Update to 1.0.1

* Fri Oct 02 2020 Lumír Balhar <lbalhar@redhat.com> - 1.0.0-1
- Update to 1.0.0 (#1884346)

* Thu Sep 03 2020 Lumír Balhar <lbalhar@redhat.com> - 0.6.0-1
- Update to 0.6.0 (#1875250)

* Thu Jul 30 2020 Lumír Balhar <lbalhar@redhat.com> - 0.5.1-1
- Update to 0.5.1 (#1859995)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 09 2020 Lumír Balhar <lbalhar@redhat.com> - 0.4.0-1
- Update to 0.4.0 (#1854424)

* Mon Jun 15 2020 Lumír Balhar <lbalhar@redhat.com> - 0.3.0-1
- Update to 0.3.0 (#1846944)

* Fri Jun 05 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-2
- Correct the license tag (GPLv3+ to LGPLv3+)
- Include the actual LICENSE files in the package

* Thu Jun 04 2020 Lumír Balhar <lbalhar@redhat.com> - 0.2.0-1
- Update to 0.2.0 (#1838278, #1841641)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.6-2
- Rebuilt for Python 3.9

* Tue May 05 2020 Lumír Balhar <lbalhar@redhat.com> - 0.1.6-1
- Update to 0.1.6 (#1831328)

* Tue Apr 07 2020 Lumír Balhar <lbalhar@redhat.com> - 0.1.5-1
- Update to 0.1.5 (#1821807)

* Thu Mar 12 2020 Lumír Balhar <lbalhar@redhat.com> - 0.1.4-1
- Initial package.
