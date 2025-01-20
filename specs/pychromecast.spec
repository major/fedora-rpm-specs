Name:           pychromecast
Version:        13.1.0
Release:        6%{?dist}
Summary:        Python library to communicate with the Google Chromecast

License:        MIT
URL:            https://github.com/home-assistant-libs/pychromecast
Source0:        https://github.com/home-assistant-libs/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

# runtime requires to at least perform an import test in %%check
BuildRequires:  python3-casttube
BuildRequires:  python3-protobuf
BuildRequires:  python3-zeroconf

%description
Library for Python 3 to communicate with the Google Chromecast. It
currently supports:

-  Auto discovering connected Chromecasts on the network
-  Start the default media receiver and play any online media
-  Control playback of current playing media
-  Implement Google Chromecast api v2
-  Communicate with apps via channels
-  Easily extendable to add support for unsupported namespaces
-  Multi-room setups with Audio cast devices

%package -n python3-chromecast
Summary:  Library for Python 3 to communicate with the Google Chromecast
%{?python_provide:%python_provide python3-chromecast}

%description -n python3-chromecast
Library for Python 3 to communicate with the Google Chromecast. It
currently supports:

-  Auto discovering connected Chromecasts on the network
-  Start the default media receiver and play any online media
-  Control playback of current playing media
-  Implement Google Chromecast api v2
-  Communicate with apps via channels
-  Easily extendable to add support for unsupported namespaces
-  Multi-room setups with Audio cast devices

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pychromecast

%check
%py3_check_import pychromecast

%files -n python3-chromecast -f %{pyproject_files}
%license LICENSE
%{python3_sitelib}/pychromecast/
%{python3_sitelib}/PyChromecast-*/

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 13.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 13.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 13 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 13.1.0-4
- Update to newer python build macros, rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 13.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 13.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 15 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 13.1.0-1
- Update to 13.1.0

* Fri Jan 12 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 13.0.8-1
- Update to 13.0.8

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 13.0.7-1
- Rebuilt for Python 3.12

* Tue Mar 21 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 13.0.5-1
- Update to 13.0.5

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 19 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 13.0.4-1
- update to 13.0.4

* Mon Nov 21 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 13.0.1-1
- Update to 13.0.1

* Mon Nov 21 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 12.1.4-1
- Update to 12.1.4

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 12.0.0-2
- Rebuilt for Python 3.11

* Thu Apr 28 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 12.0.0-1
- Update to 12.0.0

* Thu Feb 17 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 10.2.3-1
- Update to 10.2.3

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Oct 23 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 9.3.1-1
- Update to 9.3.1

* Sun Sep 19 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 9.2.1-1
- Update to 9.2.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 12 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 9.2.0-1
- Update to 9.2.0

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 8.1.0-2
- Rebuilt for Python 3.10

* Sun Feb 14 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 8.1.0-1
- Update to 8.1.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 Otto Urpelainen <oturpe@iki.fi> - 7.7.2-1
- Update to 7.7.2

* Wed Nov 11 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 7.5.1-1
- Update to 7.5.1

* Sat Oct 03 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 7.5.0-1
- Update to 7.5.0

* Mon Aug 24 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 7.2.1-1
- Update to 7.2.1

* Sun Aug 02 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 7.2.0-1
- Update to 7.2.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 7.1.2-1
- Update to 7.1.2

* Tue Jul 14 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 7.1.1-1
- Update to 7.1.1

* Thu Jun 04 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 6.0.0-1
- Update to 6.0.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.2.0-2
- Rebuilt for Python 3.9

* Wed May 13 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 5.2.0-1
- Update to 5.2.0

* Sun May 10 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 5.1.0-1
- Update to 5.1.0

* Tue Apr 14 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 4.2.3-1
- Update to 4.2.3

* Tue Mar 17 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 4.2.0-1
- Update to 4.2.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 Peter Robinson <pbrobinson@fedoraproject.org> 4.1.1-1
- Update to 4.1.1

* Thu Oct 17 2019 Peter Robinson <pbrobinson@fedoraproject.org> 4.1.0-1
- Update to 4.1.0

* Wed Sep 11 2019 Peter Robinson <pbrobinson@fedoraproject.org> 4.0.1-1
- Update to 4.0.1
- Add dependency on casttube

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.5.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 18 2019 Peter Robinson <pbrobinson@fedoraproject.org> 2.5.2-1
- Update to 2.5.2

* Wed Feb 13 2019 Peter Robinson <pbrobinson@fedoraproject.org> 2.5.0-1
- Update to 2.5.0

* Thu Feb  7 2019 Peter Robinson <pbrobinson@fedoraproject.org> 2.4.0-1
- Update to 2.4.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 18 2018 Peter Robinson <pbrobinson@fedoraproject.org> 2.3.0-1
- Update to 2.3.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-2
- Rebuilt for Python 3.7

* Tue Apr 10 2018 Peter Robinson <pbrobinson@fedoraproject.org> 2.2.0-1
- Update to 2.2.0
- Drop python2 package (retired upstream, no Fedora users)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.3-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Mon Dec 11 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.0.3-1
- Update to 1.0.3

* Mon Nov 20 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.0.1-1
- Update to 1.0.1

* Sat Jul 29 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.2-1
- Update to 0.8.2

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.1-1
- Update to 0.8.1

* Sat Feb 18 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.0-1
- Update to 0.8.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.7-3
- Fix python3 provides

* Fri Dec  2 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.7-2
- Package updates

* Mon Oct 31 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.7-1
- initial packaging
