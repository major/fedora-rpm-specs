# Don't add -s to Python shebang
# We want fedora-messaging to be able to load plugins from /usr/local
# https://bugzilla.redhat.com/show_bug.cgi?id=2272526
%undefine _py3_shebang_s

%global pkgname fedora-messaging
%global srcname fedora_messaging

Name:           %{pkgname}
Version:        3.7.0
Release:        2%{?dist}
Summary:        Set of tools for using Fedora's messaging infrastructure

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/fedora-infra/fedora-messaging
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel

# For the docs (don't build on EPEL as we don't have myst-parser)
%if ! 0%{?rhel}
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-myst-parser
%endif

Requires:       python%{python3_pkgversion}-%{pkgname} = %{version}-%{release}

BuildRequires: systemd-rpm-macros

%{?python_enable_dependency_generator}

%global _description \
Tools and APIs to make working with AMQP in Fedora easier.

%description %{_description}

%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkgname}}


%description -n python%{python3_pkgversion}-%{pkgname} %{_description}


%if ! 0%{?rhel}
%package doc
Summary:        Documentation for %{pkgname}
%description doc
Documentation for %{pkgname}.
%endif


%prep
%autosetup -n %{srcname}-%{version} -p0


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
# generate docs
%if ! 0%{?rhel}
PYTHONPATH=${PWD} sphinx-build-3 -M html -d docs/_build/doctrees docs docs/_build/html
PYTHONPATH=${PWD} sphinx-build-3 -M man -d docs/_build/doctrees docs docs/_build/man
# remove the sphinx-build leftovers
rm -rf docs/_build/*/.buildinfo
%endif


%install
%pyproject_install
%pyproject_save_files %{srcname}
install -D -p -m 644 config.toml.example $RPM_BUILD_ROOT%{_sysconfdir}/fedora-messaging/config.toml
install -D -p -m 644 configs/fedora.toml $RPM_BUILD_ROOT%{_sysconfdir}/fedora-messaging/fedora.toml
install -D -p -m 644 configs/fedora.stg.toml $RPM_BUILD_ROOT%{_sysconfdir}/fedora-messaging/fedora.stg.toml
install -D -p -m 644 configs/cacert.pem $RPM_BUILD_ROOT%{_sysconfdir}/fedora-messaging/cacert.pem
# Yes, this is supposed to be a world-readable private key. It's for public Fedora broker access.
install -D -p -m 644 configs/fedora-key.pem $RPM_BUILD_ROOT%{_sysconfdir}/fedora-messaging/fedora-key.pem
install -D -p -m 644 configs/fedora-cert.pem $RPM_BUILD_ROOT%{_sysconfdir}/fedora-messaging/fedora-cert.pem
install -D -p -m 644 configs/stg-cacert.pem $RPM_BUILD_ROOT%{_sysconfdir}/fedora-messaging/stg-cacert.pem
install -D -p -m 644 configs/fedora.stg-key.pem $RPM_BUILD_ROOT%{_sysconfdir}/fedora-messaging/fedora.stg-key.pem
install -D -p -m 644 configs/fedora.stg-cert.pem $RPM_BUILD_ROOT%{_sysconfdir}/fedora-messaging/fedora.stg-cert.pem
install -D -p -m 644 fm-consumer@.service $RPM_BUILD_ROOT%{_unitdir}/fm-consumer@.service
%if ! 0%{?rhel}
install -D -p -m 644 docs/_build/man/fedora-messaging.1 $RPM_BUILD_ROOT%{_mandir}/man1/fedora-messaging.1
%endif


%check
# We need pytest-twisted but it's not in Fedora (yet)
#%%tox


%files
%license LICENSE
%doc README.rst
%dir %{_sysconfdir}/fedora-messaging/
%config(noreplace) %{_sysconfdir}/fedora-messaging/config.toml
%config(noreplace) %{_sysconfdir}/fedora-messaging/fedora.toml
%config(noreplace) %{_sysconfdir}/fedora-messaging/fedora.stg.toml
%config(noreplace) %{_sysconfdir}/fedora-messaging/cacert.pem
%config(noreplace) %{_sysconfdir}/fedora-messaging/fedora-key.pem
%config(noreplace) %{_sysconfdir}/fedora-messaging/fedora-cert.pem
%config(noreplace) %{_sysconfdir}/fedora-messaging/stg-cacert.pem
%config(noreplace) %{_sysconfdir}/fedora-messaging/fedora.stg-key.pem
%config(noreplace) %{_sysconfdir}/fedora-messaging/fedora.stg-cert.pem
%{_bindir}/%{name}
%{_unitdir}/fm-consumer@.service
%if ! 0%{?rhel}
%{_mandir}/man1/%{name}.*
%endif

%files -n python%{python3_pkgversion}-%{pkgname} -f %{pyproject_files}
%license LICENSE

%if ! 0%{?rhel}
%files doc
%license LICENSE
%doc README.rst docs/*.rst docs/_build/html docs/sample_schema_package
%endif


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 03 2025 Packit <hello@packit.dev> - 3.7.0-1
- Update to version 3.7.0
- Drop patches that were merged upstream

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 3.5.0-5
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 3.5.0-3
- Rebuilt for Python 3.13

* Thu Apr 04 2024 Aurelien Bompard <abompard@fedoraproject.org> - 3.5.0-2
- Remove "-s" from the script shebangs (https://bugzilla.redhat.com/2272526)
- Relax the dependency on jsonschema (https://bugzilla.redhat.com/2272967)

* Wed Mar 20 2024 Aurelien Bompard <abompard@fedoraproject.org> - 3.5.0-1
- Version 3.5.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 3.4.1-2
- Rebuilt for Python 3.12

* Fri May 26 2023 Packit <hello@packit.dev> - 3.4.1-1
- Version 3.4.1 (Aurélien Bompard)
- Fix CI for python 3.6, again (Aurélien Bompard)
- Fix CI for python 3.6, again (Aurélien Bompard)
- Fix CI on python 3.6 (Aurélien Bompard)
- Fix integration tests after eba336ba (Aurélien Bompard)

* Fri Mar 31 2023 Packit <hello@packit.dev> - 3.3.0-1
- Version 3.3.0 (Aurélien Bompard)
- Add a Github action to update pre-commit linters (Aurélien Bompard)
- Update pre-commit linters (Aurélien Bompard)
- Add koji-fedoramessaging-messages in the known schemas list (Aurélien Bompard)
- Update linters (Aurélien Bompard)
- Add support for asyncio-based callbacks in the consumer (Aurélien Bompard)
- Improve documentation (Aurélien Bompard)
- Upgrade the github action for integration tests (Aurélien Bompard)
- Add a `message.load_message()` function (Aurélien Bompard)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 17 2022 Packit <hello@packit.dev> - 3.2.0-5
- Version 3.2.0 (Aurélien Bompard)
- Use tomllib from the standard library on Python 3.11 (Miro Hrončok)
- Support for message priorities (Aurélien Bompard)
- CI: run the checks with fedora-python's tox action (Aurélien Bompard)
- Add a clear way to deprecate message schemas (Aurélien Bompard)

* Tue Sep 13 2022 Packit <hello@packit.dev> - 3.1.0-5
- Version 3.1.0 (Aurélien Bompard)
- Use the new `app_name` property in the schema documentation (Aurélien Bompard)
- Add the `app_name` and `agent_name` properties to message schemas (Aurélien Bompard)
- add groups property to message (Erol Keskin)
- Add the CI message schemas (Aurélien Bompard)
- Schema docs: handle Google-style docstrings (Aurélien Bompard)
- Fix docs configuration (Aurélien Bompard)
- Schema docs: fix the venv activation to exclude system-site-packages (Aurélien Bompard)
- Add upstream version format (Akashdeep Dhar)
- Fix changelog generation with towncrier (Aurélien Bompard)
- Fix changelog (Aurélien Bompard)

* Sun Jul 31 2022 Maxwell G <gotmax@e.email> - 3.0.2-5
- Remove python3-mock BR
- Preserve mtimes

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 3.0.2-3
- Rebuilt for Python 3.11

* Mon May 23 2022 Packit <hello@packit.dev> - 3.0.2-2
- prep for release of 3.0.2 (Stephen Coady)
- Correct sync list, add issue repo and version info (Akashdeep Dhar)
- Remove fixi for rstcheck in Github CI (Aurélien Bompard)
- Fix CI for real this time (Aurélien Bompard)
- Ignore weird RST warnings in CI for now (Aurélien Bompard)
- Fix formatting with Black (Aurélien Bompard)
- Update pre-commit checkers (Aurélien Bompard)
- Fix Github actions (Aurélien Bompard)

* Thu May 12 2022 Packit <hello@packit.dev> - 3.0.1-2
- prep for the release of 3.0.1 (Stephen Coady)
- Added Packit configuration (#259) (Akashdeep Dhar)
- Add a badge for the tests status (Aurélien Bompard)
- Adjust to a message change in Python 3.10 (Aurélien Bompard)
- Change the example email addresses (Aurélien Bompard)
- Add some schema packages to the docs (Aurélien Bompard)
- Add copr-messaging to the known schemas (Aurélien Bompard)
- Don't build universal wheels since we don't run on Python 2 anymore (Aurélien Bompard)
- Improve the mergify config (Aurélien Bompard)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 04 2022 Aurelien Bompard <abompard@fedoraproject.org> - 3.0.0-1
- Update to 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1.0-2
- Rebuilt for Python 3.10

* Wed May 12 2021 Aurelien Bompard <abompard@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 04 2020 Aurelien Bompard <abompard@fedoraproject.org> - 2.0.2-1
- Update to 2.0.2

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 03 2020 Aurelien Bompard <abompard@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1

* Tue Dec 03 2019 Aurelien Bompard <abompard@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0
- Until pytest-twisted is packaged, disable the tests in %%check.

* Tue Sep 03 2019 Kevin Fenzi <kevin@scrye.com> - 1.7.2-1
- Update to 1.7.2. Fixes bug #1742459

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.1-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Jeremy Cline <jcline@redhat.com> - 1.7.1-1
- Update to v1.7.1

* Wed Jun 19 2019 Pavel Raiskup <praiskup@redhat.com> - 1.7.0-3
- install sample schema documentation cited by
  https://fedora-messaging.readthedocs.io/en/latest/tutorial/schemas.html

* Mon Jun 10 2019 Jeremy Cline <jcline@redhat.com> - 1.7.0-2
- Include the stage config and credentials

* Tue May 21 2019 Jeremy Cline <jcline@redhat.com> - 1.7.0-1
- Update to v1.7.0

* Wed Apr 17 2019 Jeremy Cline <jcline@redhat.com> - 1.6.1-1
- Update to v1.6.1

* Thu Apr 04 2019 Jeremy Cline <jcline@redhat.com> - 1.6.0-1
- Update to v1.6.0

* Thu Mar 07 2019 Aurelien Bompard <abompard@fedoraproject.org> - 1.5.0-2
- Add the Systemd service template file.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Jeremy Cline <jeremy@jcline.org> - 1.3.0-1
- Update to v1.3.0

* Mon Jan 21 2019 Jeremy Cline <jeremy@jcline.org> - 1.2.0-1
- Update to v1.2.0

* Thu Nov 15 2018 Jeremy Cline <jeremy@jcline.org> - 1.1.0-1
- Update to v1.1.0

* Wed Oct 10 2018 Jeremy Cline <jeremy@jcline.org> - 1.0.1-1
- Update to v1.0.1

* Wed Oct 10 2018 Jeremy Cline <jeremy@jcline.org> - 1.0.0-1
- Update to v1.0.0

* Fri Sep 07 2018 Jeremy Cline <jeremy@jcline.org> - 1.0.0-0.2b1
- Move dependency generator macro to top of file
- Depend on version + release for the library
- Add python_provide macro

* Wed Aug 29 2018 Jeremy Cline <jeremy@jcline.org> - 1.0.0-0.1b1
- Update to 1.0.0b1
- Drop Python 2 package for Rawhide

* Wed Aug 15 2018 Aurelien Bompard <abompard@fedoraproject.org> - 1.0.0-0.1.a1
- Initial package
