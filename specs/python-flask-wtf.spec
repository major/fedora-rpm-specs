%global mod_name flask_wtf

Name:           python-flask-wtf
Version:        1.2.2
Release:        2%{?dist}
Summary:        Simple integration of Flask and WTForms

License:        BSD-3-Clause
URL:            https://github.com/lepture/flask-wtf
Source0:        %{pypi_source %mod_name}

BuildArch:      noarch
BuildRequires:  python3-devel


%description
Flask-WTF offers simple integration with WTForms. This integration
includes optional CSRF handling for greater security.


%package -n python3-flask-wtf
Summary:        Simple integration of Flask and WTForms

%description -n python3-flask-wtf
Flask-WTF offers simple integration with WTForms. This integration 
includes optional CSRF handling for greater security.


%generate_buildrequires
%pyproject_buildrequires -r


%prep
%autosetup -p1 -n %{mod_name}-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files flask_wtf

 
%check
%py3_check_import flask_wtf


%files -n python3-flask-wtf -f %{pyproject_files}
%license LICENSE.rst
%doc README.rst docs/


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 25 2024 Sandro Mani <manisandro@gmail.com> - 1.2.2-1
- Update to 1.2.2

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 1.2.1-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 01 2023 Sandro Mani <manisandro@gmail.com> - 1.2.1-1
- Update to 1.2.1

* Sat Sep 30 2023 Sandro Mani <manisandro@gmail.com> - 1.1.2-1
- Update to 1.1.2

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 1.1.1-2
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Sandro Mani <manisandro@gmail.com> - 1.1.1-1
- Update to 1.1.1

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Sandro Mani <manisandro@gmail.com> - 1.1.0-1
- Update to 1.1.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.0.1-2
- Rebuilt for Python 3.11

* Wed Apr 06 2022 Sandro Mani <manisandro@gmail.com> - 1.0.1-1
- Update to 1.0.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 09 2021 Sandro Mani <manisandro@gmail.com> - 1.0.0-1
- Update to 1.0.0
- Modernize spec

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.14.3-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.14.3-2
- Rebuilt for Python 3.9

* Tue Apr 21 2020 Pavel Raiskup <praiskup@redhat.com> - 0.14.3-1
- rebase to new upstream release, to be compatible with new werkzeug

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Miro Hrončok <mhroncok@redhat.com> - 0.14.2-7
- Subpackage python2-flask-wtf has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.14.2-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.14.2-2
- Rebuilt for Python 3.7

* Sat Mar 03 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.14.2-1
- new version 0.14.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.10.0-11
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sun Dec 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.10.0-10
- Python 2 binary package renamed to python2-flask-wtf
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.10.0-7
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jul 17 2014 Tim Flink <tflink@fedoraproject.org> 0.10.0-2
- Adding missing BuildRequires for %%check
- disabling %%check on python3 due to missing builds
- disabling %%check for rawhide and f21 due to RHBZ 1105819

* Thu Jul 17 2014 Tim Flink <tflink@fedoraproject.org> 0.10.0-1
- Adding support for python-wtforms >= 2.0 to fix RHBZ 1120888
- added %%check

* Wed May 21 2014 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 0.9.5-1
- Updated to new source
- Add python3 support

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 09 2012 Tim Flink <tflink@fedoraproject.org> - 0.8-1
- Upgrade to upstream 0.8

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 4 2012 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.5.2-3
- Added python-wtforms as requires.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.5.2-1
- Initial RPM release
