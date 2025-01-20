%global srcname noggin-messages
%global modname noggin_messages

Name:           python-%{srcname}
Version:        1.0.3
Release:        8%{?dist}
Summary:        Fedora Messaging message schemas for Noggin

License:        MIT
URL:            https://github.com/fedora-infra/%{srcname}
Source0:        %{pypi_source}

## Downstream fixes
Patch1001:      0001-Revert-Include-additional-files-in-the-sdist.patch

BuildArch:      noarch
BuildRequires:  pyproject-rpm-macros >= 0-14

%description
This package contains the fedora-messaging message schemas for Noggin.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Fedora Messaging message schemas for Noggin
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
This package contains the fedora-messaging message schemas for Noggin.


%prep
%autosetup -n %{srcname}-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{modname}


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc docs/index.rst


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 1.0.3-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 1.0.3-2
- Rebuilt for Python 3.12

* Tue Mar 28 2023 Packit <hello@packit.dev> - 1.0.3-1
- Version 1.0.3 (Aurélien Bompard)
- Implement review suggestions (Aurélien Bompard)
- Update noggin schemas (Ryan Lerch)
- Bump pytest-cov from 3.0.0 to 4.0.0 (dependabot[bot])
- Bump flake8 from 4.0.1 to 5.0.4 (dependabot[bot])
- Bump automat from 20.2.0 to 22.10.0 (dependabot[bot])
- Bump incremental from 21.3.0 to 22.10.0 (dependabot[bot])
- Bump certifi from 2022.9.24 to 2022.12.7 (dependabot[bot])
- Bump urllib3 from 1.26.12 to 1.26.15 (dependabot[bot])
- Bump liccheck from 0.7.3 to 0.8.3 (dependabot[bot])
- Bump setuptools from 59.6.0 to 67.6.1 (dependabot[bot])
- Bump attrs from 21.4.0 to 22.2.0 (dependabot[bot])
- Update tomli (Aurélien Bompard)
- Update pyproject.toml (Jonathan Wright)
- Use poetry-core (Jonathan Wright)
- Update the dependabot approve action (Aurélien Bompard)
- Don't use tox-poetry, it's deprecated (Aurélien Bompard)
- Add an authorized license (Aurélien Bompard)
- Fix Mergify config (Aurélien Bompard)
- Follow Poetry's dep on platformdirs to fix the licenses check (Aurélien Bompard)
- Drop support for python 3.6 (Aurélien Bompard)
- Bump cryptography from 38.0.3 to 39.0.2 (dependabot[bot])
- Fix compatibility with tox-poetry by pinning tox to 3.X (Aurélien Bompard)
- Bump zope-interface from 5.5.1 to 5.5.2 (dependabot[bot])
- Bump zope-interface from 5.5.0 to 5.5.1 (dependabot[bot])
- Bump liccheck from 0.7.2 to 0.7.3 (dependabot[bot])
- Bump pytz from 2022.5 to 2022.6 (dependabot[bot])
- Bump cryptography from 38.0.1 to 38.0.3 (dependabot[bot])
- Bump babel from 2.10.3 to 2.11.0 (dependabot[bot])
- Bump stevedore from 3.5.1 to 3.5.2 (dependabot[bot])
- Bump pbr from 5.10.0 to 5.11.0 (dependabot[bot])
- Bump pika from 1.3.0 to 1.3.1 (dependabot[bot])
- Bump pytz from 2022.4 to 2022.5 (dependabot[bot])
- Bump fedora-messaging from 3.1.0 to 3.2.0 (dependabot[bot])
- Bump stevedore from 3.5.0 to 3.5.1 (dependabot[bot])
- Bump zope-interface from 5.4.0 to 5.5.0 (dependabot[bot])
- Bump pytz from 2022.2.1 to 2022.4 (dependabot[bot])
- Bump pyopenssl from 22.0.0 to 22.1.0 (dependabot[bot])
- Bump certifi from 2022.9.14 to 2022.9.24 (dependabot[bot])
- Bump idna from 3.3 to 3.4 (dependabot[bot])
- Bump certifi from 2022.6.15.2 to 2022.9.14 (dependabot[bot])
- Bump fedora-messaging from 3.0.2 to 3.1.0 (dependabot[bot])
- Bump certifi from 2022.6.15.1 to 2022.6.15.2 (dependabot[bot])
- Bump certifi from 2022.6.15 to 2022.6.15.1 (dependabot[bot])
- Bump black from 22.6.0 to 22.8.0 (dependabot[bot])
- Bump urllib3 from 1.26.11 to 1.26.12 (dependabot[bot])
- Bump pygments from 2.12.0 to 2.13.0 (dependabot[bot])
- Bump pytz from 2022.2 to 2022.2.1 (dependabot[bot])
- Bump pytz from 2022.1 to 2022.2 (dependabot[bot])
- Bump pbr from 5.9.0 to 5.10.0 (dependabot[bot])
- Bump liccheck from 0.7.1 to 0.7.2 (dependabot[bot])
- Bump urllib3 from 1.26.10 to 1.26.11 (dependabot[bot])
- Bump blinker from 1.4 to 1.5 (dependabot[bot])
- Bump atomicwrites from 1.4.0 to 1.4.1 (dependabot[bot])
- Bump urllib3 from 1.26.9 to 1.26.10 (dependabot[bot])
- Bump cryptography from 37.0.3 to 37.0.4 (dependabot[bot])
- Bump imagesize from 1.3.0 to 1.4.1 (dependabot[bot])
- Bump cffi from 1.15.0 to 1.15.1 (dependabot[bot])
- Bump pika from 1.2.1 to 1.3.0 (dependabot[bot])
- Bump black from 22.3.0 to 22.6.0 (dependabot[bot])
- Bump cryptography from 37.0.2 to 37.0.3 (dependabot[bot])
- Bump babel from 2.10.2 to 2.10.3 (dependabot[bot])
- Bump colorama from 0.4.4 to 0.4.5 (dependabot[bot])
- Bump certifi from 2022.5.18.1 to 2022.6.15 (dependabot[bot])
- Bump babel from 2.10.1 to 2.10.2 (dependabot[bot])
- Bump liccheck from 0.7.0 to 0.7.1 (dependabot[bot])
- Bump liccheck from 0.6.5 to 0.7.0 (dependabot[bot])

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 1.0.2-3
- Rebuilt for Python 3.11

* Fri May 27 2022 Packit <hello@packit.dev> - 1.0.2-2
- Add upstream tag format (Akashdeep Dhar)
- Correct the RPM specfile location (Akashdeep Dhar)
- Bump semantic-version from 2.9.0 to 2.10.0 (dependabot[bot])
- Update dependencies (Aurélien Bompard)
- Version 1.0.2 (Aurélien Bompard)
- Bump typed-ast from 1.5.3 to 1.5.4 (dependabot[bot])
- Bump fedora-messaging from 3.0.1 to 3.0.2 (dependabot[bot])
- Add some checks for installed package (Akashdeep Dhar)
- Add poetry installation and correct URLs (Akashdeep Dhar)
- Correct Packit configuration (Akashdeep Dhar)
- Add Packit configuration (Akashdeep Dhar)
- Bump fedora-messaging from 3.0.0 to 3.0.1 (dependabot[bot])
- Bump more-itertools from 8.12.0 to 8.13.0 (dependabot[bot])
- Bump pbr from 5.8.1 to 5.9.0 (dependabot[bot])
- Bump cryptography from 37.0.1 to 37.0.2 (dependabot[bot])
- Bump wrapt from 1.14.0 to 1.14.1 (dependabot[bot])
- Bump pytz from 2021.3 to 2022.1 (dependabot[bot])
- Bump cryptography from 36.0.2 to 37.0.1 (dependabot[bot])
- Bump pika from 1.2.0 to 1.2.1 (dependabot[bot])
- Bump pygments from 2.11.2 to 2.12.0 (dependabot[bot])
- Bump babel from 2.9.1 to 2.10.1 (dependabot[bot])
- Bump typed-ast from 1.5.2 to 1.5.3 (dependabot[bot])
- Bump twisted from 22.2.0 to 22.4.0 (dependabot[bot])
- Bump black from 22.1.0 to 22.3.0 (dependabot[bot])

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 14 2022 Neal Gompa <ngompa@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.0.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jul 26 18:49:27 EDT 2020 Neal Gompa <ngompa13@gmail.com> - 0.0.1-1
- Update to 0.0.1

* Sun Apr 19 16:50:52 EDT 2020 Neal Gompa <ngompa13@gmail.com> - 0.0.1~git20200416.1e93855-1
- Initial packaging
