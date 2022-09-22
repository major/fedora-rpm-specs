%global srcname noggin-messages
%global modname noggin_messages

Name:           python-%{srcname}
Version:        1.0.2
Release:        4%{?dist}
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
