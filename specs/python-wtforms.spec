%global srcname WTForms

Name:           python-wtforms
Version:        3.0.1
Release:        15%{?dist}
Summary:        Forms validation and rendering library for python

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://wtforms.simplecodes.com/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel


%description
With wtforms, your form field HTML can be generated for you.
This allows you to maintain separation of code and presentation,
and keep those messy parameters out of your python code.


%package -n python3-wtforms
Summary:        Forms validation and rendering library for python

%description -n python3-wtforms
With wtforms, your form field HTML can be generated for you.
This allows you to maintain separation of code and presentation,
and keep those messy parameters out of your python code.


%pyproject_extras_subpkg -n python3-wtforms email


%generate_buildrequires
%pyproject_buildrequires -rx email


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files wtforms


%check
%py3_check_import wtforms


%files -n python3-wtforms -f %{pyproject_files}
%doc docs/ README.rst CHANGES.rst
%license LICENSE.rst


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 3.0.1-14
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.0.1-12
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 3.0.1-8
- Rebuilt for Python 3.12

* Tue May 02 2023 Jonathan Wright <jonathan@almalinux.org> - 3.0.1-7
- fix epel9 git to track with rawhide

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 3.0.1-4
- Rebuilt for Python 3.11

* Thu May 12 2022 Miro Hrončok <mhroncok@redhat.com> - 3.0.1-3
- Package the email extra

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 07 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 3.0.1-1
- Update to 3.0.1

* Thu Dec 09 2021 Sandro Mani <manisandro@gmail.com> - 3.0.0-1
- Update to 3.0.0

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.3.3-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 14 2020 Pavel Raiskup <praiskup@redhat.com> - 2.3.3-2
- Require python3-email-validator

* Fri Aug 21 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 2.3.3-1
- Update to wtforms 2.3.3

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-7
- Subpackage python2-wtforms has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2.2.1-2
- update some macros

* Sat Jun 30 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2.2.1-1
- new version 2.2.1

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0-15
- Rebuilt for Python 3.7

* Fri Feb 16 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2.0-14
- make spec file compatible with epel7
- remove conditionals, always build for python 3

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0-13
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.0-11
- Python 2 binary package renamed to python2-wtforms
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0-8
- Rebuild for Python 3.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Dec 01 2014 Pierre-Yves Chibon <pingou@pingoured.fr> - 2.0-4
- Move the locale files into /usr/share/locale we will still have the same files
  present in both the py2 and py3 but a) they are completely identical so no
  conflicts from RPM and b) they are now in the proper place, system-wise

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fdoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sat May 24 2014 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 2.0-1
- Upgrade to upstream version
- Add python3 support

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 09 2012 Tim Flink <tflink@fedoraproject.org> - 1.0.2-1
- Upgraded to upstream 1.0.2

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.6.3-1
- Initial RPM release
