%global github_name twilio-python
%global pypi_name twilio
%global version 7.12.0

Name:           python-%{pypi_name}
Version:        %{version}
Release:        1%{?dist}
Summary:        Twilio API client and TwiML generator

License:        MIT
URL:            https://github.com/twilio/%{github_name}/
Source0:        %{url}/archive/%{version}/%{github_name}-%{version}.tar.gz
# Relax testing requirements
# Upstream report: https://github.com/twilio/twilio-python/issues/595
Patch1:         0001-python-twilio-7.8.0-tests-requirements.patch
# Nose is deprecated, use pytest instead.
# Upstream report: https://github.com/twilio/twilio-python/issues/594
Patch2:         0002-python-twilio-7.8.0-pytest-instead-nose.patch
BuildArch:      noarch

BuildRequires:  python3-devel

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
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
# Check requires network access to api.twilio.com
%pytest \
  --deselect tests/unit/rest/test_client.py::TestUserAgentClients::test_set_default_user_agent \
  --deselect tests/unit/rest/test_client.py::TestUserAgentClients::test_set_user_agent_extensions

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
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
