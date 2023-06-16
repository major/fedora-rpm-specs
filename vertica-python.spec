Name:           vertica-python
Version:        1.3.1
Release:        2%{?dist}
Summary:        Native Python adapter for the Vertica database

License:        MIT
URL:            https://github.com/vertica/vertica-python
Source0:        %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
vertica-python is a native Python adapter for the Vertica database.}

%description %{_description}

%package -n python3-vertica
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-vertica %{_description}

%prep
%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files vertica_python

%check
%pyproject_check_import -e vertica_python.tests*
 
%files -n python3-vertica -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.3.1-2
- Rebuilt for Python 3.12

* Sun Mar 12 2023 Igor Raits <igor@gooddata.com> - 1.3.1-1
- Update to 1.3.1

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.5-2
- Rebuilt for Python 3.11

* Sat May 14 2022 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 1.0.5-1
- Bump to new version

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 29 2020 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 1.0.1
- Bump to new version

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.10.3-2
- Rebuilt for Python 3.9

* Tue Mar 31 2020 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.10.3-1
- Update to version 0.10.3

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 29 2019 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.10.1-1
- Update to version 0.10.1

* Fri Nov 29 2019 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.10.0-1
- Update to version 0.10.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.2-3
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 19 2019 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.8.2-1
- Upgrade to version 0.8.2

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.4-2
- Subpackage python2-vertica has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Sep 03 2018 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.7.4-1
- Upgrade to version 0.7.4
- Build python 3 subpackage even on RHEL >= 7

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7.3-2
- Rebuilt for Python 3.7

* Tue Mar 27 2018 Jan Beran <jberan@redhat.com> - 0.7.3-1
- Update to version 0.7.3 including Python 3 subpackage

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.6.14-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.6.14-3
- Python 2 binary package renamed to python2-vertica
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr 21 2017 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.6.14-1
- Update to version 0.6.14

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 11 2015 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.5.5-1
- update to version 0.5.5

* Tue Dec 01 2015 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.5.4-1
- update to version 0.5.4

* Wed Sep 23 2015 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.5.1-1
- update to version 0.5.1

* Fri Jul 03 2015 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.5.0-1
- update to version 0.5.0

* Mon Jun 22 2015 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.4.6-1
- update to version 0.4.6

* Tue Jun 16 2015 Jakub Jedelsky <jakub.jedelsky@gamil.com> - 0.4.5-1
- update to version 0.4.5

* Wed Apr 15 2015 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.3.6-1
- update to version 0.3.6

* Wed Apr 08 2015 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.3.5-1
- update to version 0.3.5

* Wed Jan 21 2015 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.3.4-1
- update to version 0.3.4

* Wed Oct 15 2014 Jakub Jedelsky <jakub.jedelsky@gooddata.com> - 0.3.0-1
- update to version 0.3.0

* Fri Jun 13 2014 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.2.3-1
- update to new version

* Thu Apr 24 2014 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.2.1-1
- new version update

* Fri Mar 28 2014 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.2.0-4
- remove buildrood tag
- edit dateutil patch for el6

* Wed Mar 26 2014 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.2.0-3
- package is not ready for python3 

* Wed Mar 26 2014 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.2.0-2
- python-setuptools is required only on rhel<=6

* Mon Mar 24 2014 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.2.0-1
- Initial package
