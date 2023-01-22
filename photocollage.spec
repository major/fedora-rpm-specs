Summary:        Graphical tool to make photo collage posters
Name:           photocollage
Version:        1.4.4
Release:        17%{?dist}
Url:            https://github.com/adrienverge/PhotoCollage
License:        GPLv2+

Source0:        http://adrienverge.fedorapeople.org/packages/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  gettext
BuildRequires:  desktop-file-utils

Requires:       python3-pillow >= 2.0
Requires:       python3-cairo >= 1.10
Requires:       python3-gobject >= 3.0
Requires:       python3-six
Requires:       gettext-runtime >= 0.18

%description
PhotoCollage allows you to create photo collage posters. It assembles
the input photographs it is given to generate a big poster. Photos are
automatically arranged to fill the whole poster, then you can change the
final layout, dimensions, border or swap photos in the generated grid.
Eventually the final poster image can be saved in any size.

%prep
%setup -q

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --root %{buildroot}
%find_lang %{name}
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%doc README.rst
%license LICENSE
%{python3_sitelib}/*
%{_bindir}/photocollage
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 18 2022 Adrien Vergé <adrienverge@gmail.com> - 1.4.4-16
- Rebuild with python3-setuptools (includes distutils) for Python 3.12+
  https://peps.python.org/pep-0632/

* Fri Aug 26 2022  Adrien Vergé <adrienverge@gmail.com> - 1.4.4-15
- Only require gettext-runtime instead of gettext for Fedora 37+
  https://bugzilla.redhat.com/show_bug.cgi?id=2119023

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.4.4-13
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.4.4-10
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.4-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.4-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.4-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 13 2018 Adrien Vergé <adrienverge@gmail.com> - 1.4.4-1
- Update to new upstream version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.3-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.3-4
- Remove obsolete scriptlets

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016  Adrien Vergé <adrienverge@gmail.com> - 1.4.3-1
- Update to new upstream version
- Add missing 'python3-six' dependency

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat Apr 16 2016  Adrien Vergé <adrienverge@gmail.com> - 1.4.2-1
- Update to new upstream version

* Thu Apr 07 2016  Adrien Vergé <adrienverge@gmail.com> - 1.4.0-1
- Update to new upstream version
- Remove unneeded requirements
- Make description up to date

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Adrien Vergé <adrienverge@gmail.com> - 1.3.2-1
- Update to new upstream version

* Sun Nov 15 2015 Adrien Vergé <adrienverge@gmail.com> - 1.3.1-1
- Update to new upstream version

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 02 2015 Adrien Vergé <adrienverge@gmail.com> - 1.3.0-1
- Update to new upstream version

* Tue Jan 28 2015 Adrien Vergé <adrienverge@gmail.com> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Packaging:LicensingGuidelines#License_Text

* Tue Jan 13 2015 Adrien Vergé <adrienverge@gmail.com> - 1.2.2-1
- Update to new upstream version

* Thu Jan 01 2015 Adrien Vergé <adrienverge@gmail.com> - 1.2.1-1
- Update to new upstream version

* Wed Dec 31 2014 Adrien Vergé <adrienverge@gmail.com> - 1.2.0-2
- Fix outdated screenshot

* Tue Dec 30 2014 Adrien Vergé <adrienverge@gmail.com> - 1.2.0-1
- Update to new upstream version

* Sat Dec 13 2014 Adrien Vergé <adrienverge@gmail.com> - 1.1.1-1
- Update to new upstream version

* Wed Jun 18 2014 Adrien Vergé <adrienverge@gmail.com> - 1.1.0-1
- Update to new upstream version

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Fri Mar 21 2014 Adrien Vergé <adrienverge@gmail.com> - 1.0.2-1
- Fix a race condition and restrict image formats

* Thu Mar 20 2014 Adrien Vergé <adrienverge@gmail.com> - 1.0.1-1
- Add license headers in source files

* Wed Mar  5 2014 Adrien Vergé <adrienverge@gmail.com> - 1.0-1
- initial build
