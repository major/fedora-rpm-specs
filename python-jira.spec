Name:               python-jira
Version:            3.5.1
Release:            2%{?dist}
Summary:            Python library for interacting with JIRA via REST APIs

License:            BSD-2-Clause
URL:                https://pypi.io/project/jira
Source0:            %{pypi_source jira}

BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-keyring

%global _description %{expand:
Python library for interacting with JIRA via REST APIs
}
%description %_description

%package -n python3-jira
Summary:        %{summary}

%description -n python3-jira %_description


%package -n jirashell
Requires: python3-ipython
Requires: python3-keyring
Requires: python3-jira == %{version}
Summary: Interactive Jira shell
%description -n jirashell
Interactive Jira shell using jira Python library.


%prep
%autosetup -p1 -n jira-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files jira

# clone file list to split off jirashell things (will be part of jirashell.rpm)
grep -v -w 'jirashell' "%{pyproject_files}" >python3-jira.files
grep    -w 'jirashell' "%{pyproject_files}" >jirashell.files


%check
# no useful tests to run from upstream; also the packaging is a bit
# broken.  See https://github.com/pycontribs/jira/discussions/1263
%pyproject_check_import

%files -n python3-jira -f python3-jira.files
%doc PKG-INFO
%license LICENSE

%files -n jirashell -f jirashell.files
%{_bindir}/jirashell


%changelog
* Sat Jul 01 2023 Python Maint <python-maint@redhat.com> - 3.5.1-2
- Rebuilt for Python 3.12

* Mon Jun 05 2023 Lukáš Zaoral <lzaoral@redhat.com> - 3.5.1-1
- Update to version 3.5.1 (rhbz#2211639)
- Use SPDX license format

* Mon Mar 13 2023 Alois Mahdal <netvor@vornet.cz> - 3.5.0-1
- Update to version 3.5.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Dec 04 2022 Alois Mahdal <netvor@vornet.cz> - 3.4.1-2
- Split jirashell to own sub-package with proper dependencies (close RHBZ#2149660)

* Sun Nov 06 2022 Alois Mahdal <netvor@vornet.cz> - 3.4.1-1
- Update to version 3.4.1

* Wed Jul 27 2022 Alois Mahdal <netvor@vornet.cz> - 3.3.1-1
- Update to version 3.3.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 3.2.0-2
- Rebuilt for Python 3.11

* Thu Apr 28 2022 Hunor Csomortáni <csomh@redhat.com> - 3.2.0-1
- Update to version 3.2.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 13 2021 Alois Mahdal <netvor@vornet.cz> - 2.0.0-13
- Rewrote spec for PyPI and rebased to 3.1.1

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.0-12
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 13 2020 Matt Prahl <mprahl@redhat.com> - 2.0.0-10
- Add support for Python 3.8

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Steve Traylen <steve.traylen@cern.ch> - 2.0.0-6
- Add new BR of pbr.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 31 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-2
- Subpackage python2-jira has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Tue Jul 17 2018 Iryna Shcherbina <shcherbina.iryna@gmail.com> - 2.0.0-1
- Update to 2.0.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.15-3
- Rebuilt for Python 3.7

* Fri Jun 08 2018 Ralph Bean <rbean@redhat.com> - 1.0.15-2
- Add missing deps.  https://bugzilla.redhat.com/show_bug.cgi?id=1589006

* Fri May 25 2018 Ralph Bean <rbean@redhat.com> - 1.0.15-1
- new version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.7-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Nov 21 2016 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.7-1
- Update to 1.0.7 version
- Provide Python 3 subpackage

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue May 10 2016 Ralph Bean <rbean@redhat.com> - 0.50-1
- new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 30 2015 Ralph Bean <rbean@redhat.com> - 0.13-7
- Fix upstream url for https://bugzilla.redhat.com/1285760

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 21 2015 Ralph Bean <rbean@redhat.com> - 0.13-5
- Change dep from the ipython meta package to just python-ipython-console.
- Move the /tools/ module into the jira namespace to avoid potential conflict.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Nov 22 2013 Ralph Bean <rbean@redhat.com> - 0.13-3
- Patch out mime type detection as per review feedback.

* Fri Nov 01 2013 Ralph Bean <rbean@redhat.com> - 0.13-2
- Modernize python2 rpm macros.

* Thu Oct 31 2013 Ralph Bean <rbean@redhat.com> - 0.13-1
- Initial package for Fedora
