Name:               python-slackclient
Version:            3.34.0
Release:            2%{?dist}
Summary:            Slack Developer Kit for Python

# SPDX
License:            MIT
URL:                https://github.com/slackapi/python-slack-sdk
Source0:            %{url}/archive/v%{version}/python-slack-sdk-%{version}.tar.gz
BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-aiohttp
BuildRequires:      python3-websockets
BuildRequires:      python3-websocket-client
BuildRequires:      python3-sqlalchemy

%description
%{summary}.

%package -n python3-slackclient
Summary:            %{summary}

%py_provides python3-slack
%py_provides python3-slack-sdk

# Drop after f41
Provides: python3-slackclient+optional = %{version}-%{release}
Obsoletes: python3-slackclient+optional < 3.26.2-1

%description -n python3-slackclient
%{summary}.

%prep
%autosetup -n python-slack-sdk-%{version} -p0
# Remove prebuilt HTML documentation with bundled and precompiled JavaScript
rm -rf docs docs-v*
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i \
    's/^([[:blank:]]*)("(pytest-cov|codecov|flake8|black)[<>=";])/\1# \2/' \
    setup.py
# Not yet packaged; we will just skip the tests that require them:
sed -r -i 's/^([[:blank:]]*)("(moto|Flask-Sockets)[<>=";])/\1# \2/' setup.py
# Direct dependencies on these are only to pin versions to work around issues
# in dependencies we have already removed above for various reasons. We cannot
# respect the upper bounds on these versions; remove the direct dependencies
# entirely.
sed -r -i \
    's/^([[:blank:]])*("(click|Flask|Werkzeug|itsdangerous|Jinja2)[<>=";])/\1# \2/' \
    setup.py
# Remove preemptive version upper-bounds that we cannot respect.
sed -r -i 's/^([[:blank:]]*"(pytest).*),<.*"/\1"/' setup.py

%generate_buildrequires
%pyproject_buildrequires -x testing

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files slack slack_sdk

%check
# These require network access:
k="${k-}${k+ and }not test_start_raises_an_error_if_rtm_ws_url_is_not_returned"
# Integration tests require network access and secret tokens for API access.
# Amazon S3 tests require python3dist(moto), which is not packaged. Socket
# mode interaction tests require python3dist(moto), which is not packaged.
%pytest -k "${k-}" \
    --ignore-glob='integration_tests/*' \
    --ignore-glob='*/test_amazon_s3.py' \
    --ignore-glob='*/socket_mode/test_interactions_*' \
    --ignore-glob='*/rtm/test_rtm_client*'

%files -n python3-slackclient -f %{pyproject_files}
%doc README.md

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 18 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.34.0-1
- 3.34.0

* Thu Dec 05 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.33.5-1
- 3.33.5

* Tue Nov 19 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.33.4-1
- 3.33.4

* Wed Oct 30 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.33.3-1
- 3.33.3

* Mon Oct 28 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.33.2-1
- 3.33.2

* Fri Sep 20 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.33.1-1
- 3.33.1

* Mon Sep 09 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.32.0-1
- 3.32.0

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jul 05 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.31.0-1
- 3.31.0

* Mon Jun 24 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.30.0-1
- 3.30.0

* Fri Jun 14 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.29.0-1
- 3.29.0

* Wed Jun 12 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.28.0-1
- 3.28.0

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 3.27.2-2
- Rebuilt for Python 3.13

* Fri May 17 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.27.2-1
- 3.27.2

* Wed Feb 28 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.27.1-1
- 3.27.1

* Tue Feb 13 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.27.0-1
- 3.27.0

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 10 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.26.2-1
- 3.26.2

* Fri Dec 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.26.1-1
- 3.26.1

* Mon Nov 27 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.26.0-1
- 3.26.0

* Wed Nov 22 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.25.0-1
- 3.25.0

* Fri Nov 17 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.24.0-1
- 3.24.0

* Tue Nov 14 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.23.1-1
- 3.23.1

* Thu Oct 05 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.23.0-1
- 3.23.0

* Tue Sep 12 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.22.0-1
- 3.22.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.21.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 10 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.21.3-2
- Fix FTI.

* Mon May 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.21.3-1
- 3.21.3

* Wed Apr 26 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.21.2-2
- Unpin websockets ceiling

* Wed Apr 19 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.21.2-1
- 3.21.2

* Thu Apr 13 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.21.1-1
- 3.21.1

* Tue Apr 11 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.21.0-1
- 3.21.0

* Fri Mar 10 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.20.2-1
- 3.20.2

* Wed Mar 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.20.1-2
- migrated to SPDX license

* Tue Mar 07 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.20.1-1
- 3.20.1

* Thu Mar 02 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 3.20.0-3
- Confirm License is SPDX MIT
- Drop prebuilt HTML documentation due to bundled/precompiled JavaScript
- Update URLs
- Port to pyproject-rpm-macros
- Add a metapackage for the “optional” extra
- Run the tests

* Tue Feb 28 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 3.20.0-2
- Add Provides for importable modules

* Tue Feb 21 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.20.0-1
- 3.20.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 05 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.19.5-1
- 3.19.5

* Thu Nov 17 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.19.4-1
- 3.19.4

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
