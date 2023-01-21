Name:           fedora-gather-easyfix
Version:        0.2.1
Release:        90%{?dist}
Summary:        Gather easyfix tickets across fedorahosted projects

License:        GPLv2+
URL:            https://pagure.io/fedora-gather-easyfix/
Source0:        https://releases.pagure.org/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
Requires:       python3-jinja2
Requires:       python3-bugzilla
Requires:       python3-mwclient

%description
The aims of this project is to offer a simple overview of where help
is needed for people coming to Fedora.

There are a number of project hosted on  fedorahosted.org which are
participating in this process by marking tickets as 'easyfix'.
fedora-gather-easyfix find them and gather them in a single place.

A new contributor can thus consult this page and find a place/task
she/he would like to help with, contact the person in charge and get
started.

%prep
%setup -q

%build
%{__python3} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%files
%doc LICENSE README
%{python3_sitelib}/*
%{_bindir}/gather_easyfix.py
%{_datadir}/%{name}/
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/template.html

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-90
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-89
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.1-88
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-87
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-86
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.1-85
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-84
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-83
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-82
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-81
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-80
- rebuilt

* Thu Jan 09 2020 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-79
- rebuilt

* Thu Jan 09 2020 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-78
- rebuilt

* Wed Jan 08 2020 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-77
- rebuilt

* Wed Jan 08 2020 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-76
- rebuilt

* Wed Jan 08 2020 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-75
- rebuilt

* Wed Jan 08 2020 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-74
- rebuilt

* Wed Jan 08 2020 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-73
- rebuilt

* Tue Jan 07 2020 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-72
- rebuilt

* Tue Jan 07 2020 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-71
- rebuilt

* Wed Dec 11 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-70
- rebuilt

* Wed Dec 11 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-69
- rebuilt

* Tue Dec 10 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-68
- rebuilt

* Tue Dec 10 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-67
- rebuilt

* Mon Dec 09 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-66
- rebuilt

* Thu Dec 05 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-65
- rebuilt

* Mon Dec 02 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-64
- rebuilt

* Thu Nov 28 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-63
- rebuilt

* Thu Nov 28 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-62
- rebuilt

* Wed Nov 27 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-61
- rebuilt

* Wed Nov 27 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-60
- rebuilt

* Tue Nov 26 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-59
- rebuilt

* Wed Nov 13 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-58
- rebuilt

* Wed Nov 13 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-57
- rebuilt

* Wed Nov 13 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-56
- rebuilt

* Wed Nov 13 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-55
- rebuilt

* Wed Nov 13 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-54
- rebuilt

* Wed Nov 13 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-53
- rebuilt

* Wed Nov 13 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-52
- rebuilt

* Tue Nov 12 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-51
- rebuilt

* Tue Nov 12 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-50
- rebuilt

* Tue Nov 12 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-49
- rebuilt

* Tue Nov 12 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-48
- rebuilt

* Tue Nov 12 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-47
- rebuilt

* Tue Nov 12 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-46
- rebuilt

* Thu Nov 07 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-45
- rebuilt

* Thu Nov 07 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-44
- rebuilt

* Fri Oct 25 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-43
- rebuilt

* Fri Oct 25 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-42
- rebuilt

* Fri Oct 25 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-41
- rebuilt

* Fri Oct 18 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-40
- rebuilt

* Tue Oct 15 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-39
- rebuilt

* Fri Oct 11 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-38
- rebuilt

* Thu Oct 10 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-37
- rebuilt

* Wed Oct 09 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-36
- rebuilt

* Wed Oct 09 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-35
- rebuilt

* Wed Oct 09 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-34
- rebuilt

* Wed Oct 09 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-33
- rebuilt

* Tue Oct 08 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-32
- rebuilt

* Tue Oct 08 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-31
- rebuilt

* Thu Sep 26 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-30
- rebuilt

* Tue Sep 24 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-29
- rebuilt

* Mon Sep 23 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-28
- rebuilt

* Fri Sep 13 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-27
- rebuilt

* Fri Sep 13 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-26
- rebuilt

* Fri Sep 13 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-25
- rebuilt

* Thu Sep 12 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-24
- rebuilt

* Thu Sep 12 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-23
- rebuilt

* Wed Sep 11 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-22
- rebuilt

* Tue Sep 10 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-21
- rebuilt

* Tue Sep 10 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-20
- rebuilt

* Mon Sep 09 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-19
- rebuilt

* Mon Sep 09 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-18
- rebuilt

* Mon Sep 09 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-17
- rebuilt

* Mon Sep 09 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-16
- rebuilt

* Fri Sep 06 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-15
- rebuilt

* Fri Sep 06 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-14
- rebuilt

* Thu Sep 05 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-13
- rebuilt

* Thu Sep 05 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-12
- rebuilt

* Thu Sep 05 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-11
- rebuilt

* Thu Sep 05 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-10
- rebuilt

* Wed Sep 04 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-9
- rebuilt

* Tue Sep 03 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-8
- rebuilt

* Tue Sep 03 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-7
- rebuilt

* Tue Sep 03 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-6
- rebuilt

* Tue Sep 03 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-5
- rebuilt

* Tue Sep 03 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-4
- rebuilt

* Mon Sep 02 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-3
- rebuilt

* Fri Aug 30 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-2
- rebuilt

* Fri Aug 30 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.1-1
- Upgrade to 0.2.1

* Fri Aug 30 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.2.0-1
- Upgrade to 0.2.0
- Port to python3

* Thu Aug 29 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.1-39
- rebuilt

* Thu Aug 29 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.1-38
- rebuilt

* Fri Aug 02 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.1-37
- rebuilt

* Thu Aug 01 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.1-36
- rebuilt

* Wed Jul 31 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.1-35
- rebuilt

* Wed Jul 31 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.1-34
- rebuilt

* Tue Jul 30 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.1-33
- rebuilt

* Mon Jul 29 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.1-32
- rebuilt

* Mon Jul 29 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.1-31
- rebuilt

* Fri Jul 26 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.1-30
- rebuilt

* Fri Jul 26 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.1-29
- rebuilt

* Fri Jul 26 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.1-28
- rebuilt

* Thu Jul 25 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.1-27
- rebuilt

* Thu Jul 25 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.1-26
- rebuilt

* Thu Jul 25 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.1-25
- rebuilt

* Thu Jul 25 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.1-24
- rebuilt

* Thu Jul 25 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.1-23
- rebuilt

* Thu Jul 25 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.1-22
- rebuilt

* Thu Jul 25 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.1-21
- rebuilt

* Thu Jul 25 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.1-20
- rebuilt

* Thu Jul 25 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.1-19
- rebuilt

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.1-17
- rebuilt

* Wed Jul 17 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.1-16
- rebuilt

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.1-14
- Fix URL and Source0 tag

* Wed Jul 18 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.1-13
- Use the py2 version of the macros

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.1.1-11
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 27 2012 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.1-1
- Update to 0.1.1
- Fix Source0 by adding the link to the fedorahosted release folder

* Mon Feb 20 2012 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.0-1
- Initial packaging for Fedora
