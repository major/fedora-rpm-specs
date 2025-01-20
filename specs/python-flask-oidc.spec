%global project_name flask-oidc
%global mod_name flask_oidc

Name:           python-%{project_name}
Version:        2.2.2
Release:        2%{?dist}
Summary:        OpenID Connect extension for Flask

License:        BSD-2-Clause
URL:            https://github.com/fedora-infra/flask-oidc
Source0:        %pypi_source %{mod_name}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-responses

%global _description %{expand:
OpenID Connect support for Flask.
This library should work with any standards compliant
OpenID Connect provider. It has been tested with
Ipsilon.}

%description %_description

%package -n python3-%{project_name}
Summary:        %{summary}

%description -n python3-%{project_name} %_description


%prep
%autosetup -p1 -n %{mod_name}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{mod_name}

%check
%pytest

%files -n python3-%{project_name} -f %{pyproject_files}
%doc README.rst
%license LICENSES/BSD-2-Clause.txt


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Oct 24 2024 Packit <hello@packit.dev> - 2.2.2-1
- Update to version 2.2.2

* Wed Oct 23 2024 Packit <hello@packit.dev> - 2.2.1-1
- Update to version 2.2.1

* Tue Jul 30 2024 Gwyn Ciesla <gwync@protonmail.com> - 2.2.0-1
- 2.2.0

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 2.1.1-5
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Dec 19 2023 Miro Hrončok <mhroncok@redhat.com> - 2.1.1-2
- Reduce unneeded build dependencies

* Fri Nov 03 2023 Aurelien Bompard <abompard@fedoraproject.org> - 2.1.1-1
- Version 2.1.1

* Mon Oct 09 2023 Packit <hello@packit.dev> - 2.1.0-1
- Version 2.1.0 (Aurélien Bompard)
- Handle token expiration when there is no ``refresh_token`` or no token URL (Aurélien Bompard)
- Don't force `redirect_uri` to HTTPS (Aurélien Bompard)
- Update dependencies in lockfile (renovate[bot])
- Update dependencies in lockfile (renovate[bot])
- Update pre-commit hook charliermarsh/ruff-pre-commit to v0.0.292 (renovate[bot])
- Update pre-commit hook charliermarsh/ruff-pre-commit to v0.0.291 (renovate[bot])
- Update dependencies in lockfile (renovate[bot])
- Update pre-commit hook charliermarsh/ruff-pre-commit to v0.0.290 (renovate[bot])
- Update dependencies in lockfile (renovate[bot])
- Update pre-commit hook charliermarsh/ruff-pre-commit to v0.0.289 (renovate[bot])
- Update pre-commit hook charliermarsh/ruff-pre-commit to v0.0.288 (renovate[bot])
- Update pre-commit hook psf/black to v23.9.1 (renovate[bot])
- Update dependencies in lockfile (renovate[bot])
- Update pre-commit hook psf/black to v23.9.0 (renovate[bot])
- Fix workflow definition (Aurélien Bompard)

* Fri Sep 08 2023 Packit <hello@packit.dev> - 2.0.3-1
- Version 2.0.3 (Aurélien Bompard)
- Update actions/checkout action to v4 (renovate[bot])
- Don't request the `profile` scope by default, as version 1.x used to do (Aurélien Bompard)
- Redirect URIs must always be https (Aurélien Bompard)
- Refactor the tests to use the new make_test_app fixture (Aurélien Bompard)
- Use the `OIDC_CALLBACK_ROUTE` to build the `request_url` when defined (Aurélien Bompard)
- Also clear g.oidc_id_token on logout (Aurélien Bompard)
- Clarify the resource server docs (Aurélien Bompard)
- Add a workflow to let contributors know when a fix is released (Aurélien Bompard)
- Update pre-commit hook charliermarsh/ruff-pre-commit to v0.0.287 (renovate[bot])
- Auto-update expired tokens if possible (Aurélien Bompard)
- Fix sub-lists in the changelog (Aurélien Bompard)
- Update dependencies in lockfile (renovate[bot])
- Update pre-commit hook charliermarsh/ruff-pre-commit to v0.0.286 (renovate[bot])
- Update dependencies in lockfile (renovate[bot])

* Wed Aug 23 2023 Packit <hello@packit.dev> - 2.0.2-1
- Version 2.0.2 (Aurélien Bompard)
- Avoid a redirect loop on logout when the token is expired (Aurélien Bompard)
- Add a reference to the issue in the changelog (Aurélien Bompard)
- We don't actually use `OIDC_USERINFO_URL` (Aurélien Bompard)
- Update pre-commit hook charliermarsh/ruff-pre-commit to v0.0.285 (renovate[bot])

* Tue Aug 22 2023 Packit <hello@packit.dev> - 2.0.1-1
- Version 2.0.1 (Aurélien Bompard)
- Add the extlinks extension to sphinx (Aurélien Bompard)
- Disable user info collection if the `client_secrets` don't contain the URL (Aurélien Bompard)
- Fix README (Aurélien Bompard)
- Add test status in README (Aurélien Bompard)
- Add Packit config (Aurélien Bompard)
- Handle older versions of Werkzeug (Aurélien Bompard)
- Some doc fixes (Aurélien Bompard)

* Mon Aug 21 2023 Aurelien Bompard <abompard@fedoraproject.org> - 2.0.0-1
- Version 2.0.0
- Modernize by following https://docs.fedoraproject.org/en-US/packaging-guidelines/Python

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 1.5.0-4
- Rebuilt for Python 3.12

* Tue Mar 07 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.5.0-3
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 11 2023 David Kirwan <dkirwan@redhat.com> - 1.5.0-1
- Switch rpm to point at Fork, release 1.5.0 with PyJWT fix PR: puiterwijk/flask-oidc/pull/144

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 1.4.0-14
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-12
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.4.0-11
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 08 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.4.0-3
- Drop python2 support.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep 08 2018 Ralph Bean <rbean@redhat.com> - 1.4.0-1
- new version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.1-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 30 2017 Ralph Bean <rbean@redhat.com> - 1.1.1-1
- new version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jul 13 2016 Simon M <skrzepto@gmail.com> - 1.0.1
- Working on initial spec file
- Typo in version in this change log
- Updating email address of author

* Wed Jul 13 2016 Simon M <skrzepto@gmail.com> - 1.0.3
- Updating package version
