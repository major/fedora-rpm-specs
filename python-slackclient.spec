%global modname slackclient

Name:               python-%{modname}
Version:            3.19.3
Release:            1%{?dist}
Summary:            Slack Developer Kit for Python

License:            MIT
URL:                https://github.com/slackapi/python-%{modname}
Source0:            %{url}/archive/v%{version}/python-%{modname}-%{version}.tar.gz
BuildArch:          noarch

%description
%{summary}.

%package -n python%{python3_pkgversion}-%{modname}
Summary:            %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}
BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      python%{python3_pkgversion}-setuptools
BuildRequires:      python3-websocket-client
BuildRequires:      python3-six
BuildRequires:      python3-requests
BuildRequires:      python3-pytest-runner
BuildRequires:      python3-aiodns
BuildRequires:      python3-aiohttp
Requires:           python3-websocket-client
Requires:           python3-six
Requires:           python3-requests

%description -n python%{python3_pkgversion}-%{modname}
%{summary}.

Python %{python3_pkgversion} version.

%prep
%autosetup -n python-slack-sdk-%{version}

%build
%py3_build

%install
%py3_install

# re-enable once we have python3-codecov
#%check
#%{__python3} setup.py test

%files -n python%{python3_pkgversion}-%{modname}
%doc README.md docs/
%license LICENSE
%{python3_sitelib}/slack/
%{python3_sitelib}/slack_sdk/
%{python3_sitelib}/slack_sdk-*.egg-info/

%changelog
* Thu Nov 10 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.19.3-1
- 3.19.3

* Fri Oct 28 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.19.2-1
- 3.19.2

* Thu Oct 06 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.19.1-1
- 3.19.1

* Wed Oct 05 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.19.0-1
- 3.19.0

* Tue Oct 04 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.18.5-1
- 3.18.5

* Fri Sep 30 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.18.4-1
- 3.18.4

* Tue Sep 06 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.18.3-1
- 3.18.3

* Tue Sep 06 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.18.2-1
- 3.18.2

* Wed Jul 27 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.18.1-1
- 3.18.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.18.0-1
- 3.18.0

* Wed Jul 06 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.17.2-1
- 3.17.2

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 3.17.0-2
- Rebuilt for Python 3.11

* Tue May 31 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.17.0-1
- 3.17.0

* Thu May 19 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.16.2-1
- 3.16.2

* Thu May 12 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.16.1-1
- 3.16.1

* Thu May 05 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.16.0-1
- 3.16.0

* Thu Mar 03 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.15.2-1
- 3.15.2

* Wed Feb 23 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.15.1-1
- 3.15.1

* Thu Feb 17 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.15.0-1
- 3.15.0

* Wed Feb 09 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.14.1-1
- 3.14.1

* Tue Feb 08 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.14.0-1
- 3.14.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 13 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.13.0-1
- 3.13.0

* Wed Sep 22 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.11.2-1
- 3.11.2

* Mon Sep 20 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.11.1-1
- 3.11.1

* Wed Sep 15 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.11.0-1
- 3.11.0

* Sat Aug 28 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.10.1-1
- 3.10.1

* Thu Aug 26 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.10.0-1
- 3.10.0

* Tue Aug 17 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.9.1-1
- 3.9.1

* Mon Aug 16 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.9.0-1
- 3.9.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 16 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.8.0-1
- 3.8.0

* Wed Jun 16 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.7.0-1
- 3.7.0

* Thu Jun 10 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.6.0-1
- 3.6.0

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.5.1-2
- Rebuilt for Python 3.10

* Mon May 03 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.5.1-1
- 3.5.1

* Tue Apr 20 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.5.0-1
- 3.5.0

* Fri Mar 05 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.4.2-1
- 3.4.2

* Wed Mar 03 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.4.1-1
- 3.4.1

* Sat Feb 20 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.4.0-1
- 3.4.0

* Fri Feb 12 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.3.2-1
- 3.3.2

* Tue Feb 09 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.3.1-1
- 3.3.1

* Fri Feb 05 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.3.0-1
- 3.3.0

* Wed Jan 27 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.2.1-1
- 3.2.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.7.3-1
- 2.7.3

* Wed Jun 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.7.2-1
- 2.7.2

* Fri Jun 05 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.7.1-1
- 2.7.1

* Thu Jun 04 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.7.0-1
- 2.7.0

* Fri May 29 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.6.2-1
- 2.6.2

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.6.0-2
- Rebuilt for Python 3.9

* Fri May 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.6.0-1
- 2.6.0

* Wed May 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.6.0-0.rc2
- 2.6.0 rc2

* Fri May 15 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.6.0-0.rc1
- 2.6.0 rc1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.5.0-1
- 2.5.0

* Mon Dec 02 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.4.0-1
- 2.4.0

* Wed Oct 30 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.3.1-1
- 2.3.1

* Wed Oct 23 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.3.0-1
- 2.3.0

* Tue Oct 08 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.2.1-1
- 2.2.1

* Wed Sep 25 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.2.0-1
- 2.2.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 08 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.1.0-1
- 2.1.0

* Mon May 06 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.0.1-1
- 2.0.1

* Fri Mar 01 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.3.1-1
- 1.3.1

* Thu Jan 31 2019 Gwyn Ciesla <limburgher@gmail.com> - 1.3.0-1
- 1.3.0

* Mon Sep 17 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.2.1-4
- Drop Python 2.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-2
- Rebuilt for Python 3.7

* Tue Mar 27 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.2.1-1
- 1.2.1

* Thu Mar 22 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.2.0-1
- 1.2.0

* Fri Mar 02 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.1.3-1
- 1.1.3

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.1.2-1
- 1.1.2

* Tue Jan 30 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Mon Nov 27 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.1.0-1
- 1.1.0

* Fri Sep 01 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.0.9-1
- 1.0.9

* Thu Aug 03 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.0.7-1
- 1.0.7

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 14 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.0.6-2
- Require python-requests.

* Wed Jul 05 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.0.6-1
- Initial package.
