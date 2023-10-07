%global github_name twilio-python
%global pypi_name twilio

Name:           python-%{pypi_name}
Version:        8.9.1
Release:        1%{?dist}
Summary:        Twilio API client and TwiML generator

License:        MIT
URL:            https://github.com/twilio/twilio-python
Source0:        %{url}/archive/%{version}/%{github_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-jwt
# Tests requirements:
BuildRequires:  python3dist(aiounittest)
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(django)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(multidict)
BuildRequires:  python3dist(pytest)

%global desc \
The Twilio REST SDK simplifies the process of making calls using the Twilio \
REST API. \
The Twilio REST API lets to you initiate outgoing calls, list previous calls, \
and much more.

%description
%{desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%{desc}

%prep
%autosetup -p1 -n %{github_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
# avoid 'import file mismatch:'
rm twilio/rest/events/v1/sink/sink_test.py
# Disable checks requiring network access to api.twilio.com
# Disable webbook test requiring proprietary ngrok binary
rm tests/cluster/test_webhook.py
rm tests/cluster/test_cluster.py
%pytest \
  --deselect tests/unit/rest/test_client.py::TestUserAgentClients::test_set_default_user_agent \
  --deselect tests/unit/rest/test_client.py::TestUserAgentClients::test_set_user_agent_extensions


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
* Thu Oct 05 2023 Packit <hello@packit.dev> - 8.9.1-1
- Release 8.9.1 (Twilio)
- [Librarian] Regenerated @ a25fe2e20ee404d8f8642d6e5acceff276916c9e (Twilio)
- chore: Drop dependency on `pytz` by using stdlib `datetime.timezone.utc` (#721) (Zac Hatfield-Dodds)
- chore: twilio help changes (#723) (kridai)
- Update ValidateSslCertificate method in accordance with recent changes to the security testing method (#724) (Athira Sabu)
- Resolves rhbz#2242294

* Tue Sep 26 2023 Packit <hello@packit.dev> - 8.9.0-1
- Release 8.9.0 (Twilio)
- [Librarian] Regenerated @ c9ac9b9736431d573d8dec29ad3095eee969cdea (Twilio)

* Mon Sep 04 2023 Roman Inflianskas <rominf@aiven.io> - 8.7.0-1
- Resolves: rhbz#2234652 Update to 8.7.0

* Sun Aug 13 2023 Roman Inflianskas <rominf@aiven.io> - 8.6.0-1
- Resolves: rhbz#2226999 Update to 8.6.0

* Sun Aug 13 2023 Roman Inflianskas <rominf@aiven.io> - 8.5.1-1
- Resolves: rhbz#2226999 Update to 8.5.1

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 13 2023 Paul Wouters <paul.wouters@aiven.io - 8.5.0-1
- Resolves: rhbz#2181314 Update to 8.5.0

* Fri Jul 07 2023 Roman Inflianskas <rominf@aiven.io> - 7.16.5-2
- Resolves: rhbz#2220542 F39FailsToInstall: python3-twilio
- Simplify testing (don't install linters)

* Wed Mar 15 2023 Paul Wouters <paul.wouters@aiven.io - 7.16.5-1
- Resolves: rhbz#2177268 python-twilio-7.16.5 is available

* Tue Feb 28 2023 Roman Inflianskas <rominf@aiven.io> - 7.16.4-1
- Resolves rhbz#2172974 python-twilio-7.16.4 is available

* Thu Feb 09 2023 Paul Wouters <paul.wouters@aiven.io - 7.16.3-1
- Resolves rhbz#2164705 python-twilio-7.16.3 is available

* Tue Jan 24 2023 Paul Wouters <paul.wouters@aiven.io - 7.16.1-1
- Resolves rhbz#2117470 python-twilio-7.16.1 is available

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 01 2022 Roman Inflianskas <rominf@aiven.io> - 7.12.0-1
- Update to 7.12.0 (resolve rhbz#2088393)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 27 2022 Roman Inflianskas <rominf@aiven.io> - 7.9.3-1
- Update to 7.9.3 (#2088393), re-enable testing

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 7.9.0-2
- Rebuilt for Python 3.11

* Thu May 05 2022 Paul Wouters <paul.wouters@aiven.io> - 7.9.0-1
- Resolves: rhbz#2081949 python-twilio-7.9.0 is available

* Wed Apr 27 2022 Paul Wouters <paul.wouters@aiven.io> - 7.8.2-1
- Resolves: rhbz#2072788 python-twilio-7.8.2 is available

* Tue Mar 29 2022 Roman Inflianskas <rominf@aiven.io> - 7.8.0-1
- Update to 7.8.0 (#2062947), update python macros, enable testing

* Mon Mar 28 2022 Roman Inflianskas <rominf@aiven.io> - 7.7.1-1
- Update to 7.7.1

* Wed Mar 09 2022 Paul Wouters <paul.wouters@aiven.io> - 7.7.0-1
- Revived packge, update to 7.7.0, update python macros`

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.32.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 6.32.0-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.32.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.32.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 6.32.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 17 2019 Michael Cullen <michael@cullen-online.com> - 6.32.0-1
- Updated to 6.32.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 6.29.1-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 6.29.1-2
- Rebuilt for Python 3.8

* Fri Aug 02 2019 Michael Cullen <michael@cullen-online.com> - 6.29.1-1
- Updated to 6.29.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.27.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 20 2019 Michael Cullen <michael@cullen-online.com> - 6.10.3-1
- Updated to 6.27.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.14.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 6.14.7-3
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.14.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Charalampos Stratakis <cstratak@redhat.com> - 6.14.7-1
- Update to 6.14.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 6.10.3-2
- Rebuilt for Python 3.7

* Fri Feb 16 2018 Michael Cullen <michael@cullen-online.com> - 6.10.3-1
- new version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 10 2017 Michael Cullen <michael@cullen-online.com> - 6.9.1-1
- new version

* Tue Nov 21 2017 Michael Cullen <michael@cullen-online.com> - 6.9.0-1
- new version

* Mon Nov 06 2017 Michael Cullen <michael@cullen-online.com> - 6.8.3-1
- new version

* Tue Oct 24 2017 Michael Cullen <michael@cullen-online.com> - 6.8.1-1
- Updated to a new version
* Sat Oct 14 2017 Michael Cullen <michael@cullen-online.com> - 6.8.0-1
- Updated to a new version
- Dealt with some review comments
* Sun Oct 08 2017 Michael Cullen <michael@cullen-online.com> - 6.7.1-1
- Updated to a new version
* Sat Aug 26 2017 Michael Cullen <michael@cullen-online.com> - 6.6.0-2
- Various improvements to match example better
* Sat Aug 26 2017 Michael Cullen <michael@cullen-online.com> - 6.6.0-1
- Intial Packaging
