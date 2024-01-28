Name:           python-zeroconf
Version:        0.118.0
Release:        5%{?dist}
Summary:        Pure Python Multicast DNS Service Discovery Library

License:        LGPL-2.1-or-later
URL:            https://github.com/jstasiak/python-zeroconf
Source0:        %{url}/archive/%{version}/zeroconf-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio


%description
A pure Python implementation of multicast DNS service discovery
supporting Bonjour/Avahi.

%package -n     python3-zeroconf
Summary:        %{summary}

%description -n python3-zeroconf
A pure Python 3 implementation of multicast DNS service discovery
supporting Bonjour/Avahi.


%prep
%autosetup -p1
# Upstream requires this for https://github.com/python-poetry/poetry/issues/7505
# But it's not relevant for the RPM package
sed -i 's/poetry-core>=1.5.2/poetry-core/' pyproject.toml
# We don't measure coverage in tests
sed -Ei 's/--cov(-|=)[^ "]+//g' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires


%build
# Explicitly choose to compile the Cython extensions
export REQUIRE_CYTHON=1
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files zeroconf


%check
# IPv6 tests fail in Koji/mock, test_sending_unicast uses IPv6
%pytest -v -k "not test_sending_unicast and not test_integration_with_listener_ipv6"


%files -n python3-zeroconf -f %{pyproject_files}
%doc README.rst


%changelog
* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.118.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.118.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 26 2023 Miro Hrončok <mhroncok@redhat.com> - 0.118.0-3
- Compile the optional Python extension modules

* Wed Oct 25 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 0.118.0-2
- Make the package arched since it installs to %%{python3_sitearch}
  (fix RHBZ#2245957)
- Make the choice not to compile the Cython extension explicit

* Tue Oct 17 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 0.118.0-1
- Update to 0.118.0

* Sat Sep 09 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 0.102.0-1
- Update to 0.102.0

* Mon Aug 28 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 0.86.0-1
- Update to 0.86.0

* Fri Aug 04 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 0.74.0-1
- Update to 0.74.0

* Wed Aug 02 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 0.72.0-1
- Update to 0.72.0

* Mon Jul 24 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 0.71.3-1
- Update to 0.71.3

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.58.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.58.0-2
- Rebuilt for Python 3.12

* Tue Apr 25 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 0.58.0-1
- Update to 0.58.0

* Mon Apr 10 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 0.56.0-1
- Update to 0.56.0

* Mon Mar 20 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 0.47.4-1
- Update to 0.47.4

* Wed Feb 01 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 0.47.1-1
- Update to 0.47.1

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.39.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 30 2022 Karolina Surma <ksurma@redhat.com> - 0.39.4-1
- Update to 0.39.4
Resolves: rhbz#2116022

* Thu Jul 28 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 0.38.7-1
- Update to 0.38.7

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.38.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.38.4-2
- Rebuilt for Python 3.11

* Tue Apr 26 2022 Lumír Balhar <lbalhar@redhat.com> - 0.38.4-1
- Update to 0.38.4
Resolves: rhbz#2059530

* Wed Feb 02 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 0.38.3-1
- Update to 0.38.3

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.37.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 30 2021 Tomáš Hrnčiar <thrnciar@redhat.com> - 0.37.0-1
- Update to 0.37.0

* Sat Oct 23 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.36.9-1
- Update to 0.36.9

* Sun Sep 19 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.36.5-1
- Update to 0.36.5

* Mon Aug 09 2021 Miro Hrončok <mhroncok@redhat.com> - 0.33.4-1
- Update to 0.33.4
- Fixes: rhbz#1974240

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 07 2021 Python Maint <python-maint@redhat.com> - 0.30.0-2
- Rebuilt for Python 3.10

* Sat Jun 05 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.30.0-1
- Update to 0.30

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.29.0-2
- Rebuilt for Python 3.10

* Thu Apr 01 2021 Tomas Hrnciar <thrnciar@redhat.com> - 0.29.0-1
- Update to 0.29.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.28.8-1
- Update to 0.28.8

* Wed Nov 11 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.28.6-1
- Update to 0.28.6

* Fri Sep 11 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.28.5-1
- Update to 0.28.5

* Wed Sep 09 2020 Yatin Karel <ykarel@redhat.com> - 0.28.4-1
- Update to 0.28.4 (#1874041)

* Thu Aug 27 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.28.2-1
- Update to 0.28.2

* Mon Aug 24 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.28.1-1
- Update to 0.28.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.28.0-1
- Update to 0.28.0

* Fri Jun 05 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.27.1-1
- Update to 0.27.1

* Sat May 30 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.27.0-1
- Update to 0.27.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.26.1-2
- Rebuilt for Python 3.9

* Sun May 10 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.26.1-1
- Update to 0.26.1

* Wed Apr 15 2020 Miro Hrončok <mhroncok@redhat.com> - 0.25.1-1
- Update to 0.25.1 (#1823981)

* Tue Apr 14 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.25.0-1
- Update to 0.25.0

* Sun Mar 08 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.24.5-1
- Update to 0.24.5

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 05 2020 Miro Hrončok <mhroncok@redhat.com> - 0.24.4-1
- New version 0.24.4 (#1787774)

* Wed Dec 18 2019 Miro Hrončok <mhroncok@redhat.com> - 0.24.2-1
- New version 0.24.2

* Tue Dec 17 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.24.1-1
- New version 0.24.1

* Wed Nov 20 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.24.0-1
- New version 0.24.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.23.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.23.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.23.0-1
- New version 0.23.0

* Sun Apr 28 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.22.0-1
- New version 0.22.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.21.3-2
- Enable python dependency generator

* Mon Dec 24 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.21.3-1
- New version 0.21.3

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.20.0-2
- Rebuilt for Python 3.7

* Tue Apr 10 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.20.0-1
- New version 0.20.0
- Drop python2 package (retired upstream, no more Fedora users)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 08 2017 Iryna Shcherbina <ishcherb@redhat.com> - 0.19.1-3
- Fix ambiguous Python 2 dependency declarations
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 14 2017 Miro Hrončok <mhroncok@redhat.com> - 0.19.1-1
- New version 0.19.1 (#1461043)
- Updated (B)Rs to use python2- where possible

* Tue Mar 14 2017 Miro Hrončok <mhroncok@redhat.com> - 0.18.0-2
- Remove enum-compat from install_requires (#1432165)

* Sat Feb 18 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.18.0-1
- Update to 0.18.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 21 2016 Miro Hrončok <mhroncok@redhat.com> - 0.17.6-3
- Rebuild for Python 3.6

* Wed Dec 21 2016 Miro Hrončok <mhroncok@redhat.com> - 0.17.6-2
- Add Python 2 subpackage

* Sun Dec 04 2016 Miro Hrončok <mhroncok@redhat.com> - 0.17.6-1
- Initial package
