%global debug_package %{nil}

Name:           pyatspi
Version:        2.46.1
Release:        7%{?dist}
Summary:        Python bindings for at-spi

License:        LGPL-2.0-or-later AND GPL-2.0-or-later
URL:            http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus
Source0:        https://download.gnome.org/sources/pyatspi/2.46/%{name}-%{version}.tar.xz

BuildRequires:  make
BuildRequires:  pkgconfig(atk) >= 2.11.2
BuildRequires:  pkgconfig(atspi-2)
BuildRequires:  pkgconfig(dbus-1) >= 1.0
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.0.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.0.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.0.0
BuildRequires:  pkgconfig(pygobject-3.0) >= 2.90.1

BuildRequires:  python3-dbus
BuildRequires:  python3-devel

BuildArch:      noarch

%description
at-spi allows assistive technologies to access GTK-based
applications. Essentially it exposes the internals of applications for
automation, so tools such as screen readers, magnifiers, or even
scripting interfaces can query and interact with GUI controls.

This package includes a python3 client library for at-spi.


%package -n python3-pyatspi
Summary:        Python3 bindings for at-spi
Requires:       at-spi2-core
Requires:       python3-gobject

%description -n python3-pyatspi
at-spi allows assistive technologies to access GTK-based
applications. Essentially it exposes the internals of applications for
automation, so tools such as screen readers, magnifiers, or even
scripting interfaces can query and interact with GUI controls.

This package includes a python3 client library for at-spi.


%prep
%autosetup -p1


%build
%configure --with-python=python3 --enable-tests
%make_build


%install
%make_install

# Fix up the shebang for python3 example
sed -i '1s|^#!/usr/bin/python|#!%{__python3}|' examples/magFocusTracker.py


%check
# Done by the 'build' step, with --enable-tests


%files -n python3-pyatspi
%license COPYING COPYING.GPL
%doc AUTHORS README.md
%doc examples/magFocusTracker.py
%{python3_sitelib}/pyatspi/


%changelog
* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 2.46.1-7
- Rebuilt for Python 3.14

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.46.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.46.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.46.1-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.46.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.46.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Kalev Lember <klember@redhat.com> - 2.46.1-1
- Update to 2.46.1

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.46.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 2.46.0-5
- Rebuilt for Python 3.12

* Wed May 10 2023 Tomas Popela <tpopela@redhat.com> - 2.46.0-4
- Drop BR on dbus-glib as the project is using plain dbus

* Wed Apr 05 2023 David King <amigadave@amigadave.com> - 2.46.0-3
- Remove obsolete gtk2 BuildRequires
- Use SPDX for license field

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.46.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 21 2022 Kalev Lember <klember@redhat.com> - 2.46.0-1
- Update to 2.46.0

* Mon Aug 08 2022 Kalev Lember <klember@redhat.com> - 2.45.90-1
- Update to 2.45.90

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.45.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 07 2022 David King <amigadave@amigadave.com> - 2.45.1-1
- Update to 2.45.1

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.38.2-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 11 2021 Kalev Lember <klember@redhat.com> - 2.38.2-1
- Update to 2.38.2

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.38.1-2
- Rebuilt for Python 3.10

* Mon Mar 15 2021 Kalev Lember <klember@redhat.com> - 2.38.1-1
- Update to 2.38.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 12 2020 Kalev Lember <klember@redhat.com> - 2.38.0-1
- Update to 2.38.0

* Tue Aug 18 2020 Kalev Lember <klember@redhat.com> - 2.37.90-1
- Update to 2.37.90

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.36.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.36.0-2
- Rebuilt for Python 3.9

* Sun Mar 08 2020 Kalev Lember <klember@redhat.com> - 2.36.0-1
- Update to 2.36.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.35.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Kalev Lember <klember@redhat.com> - 2.35.1-1
- Update to 2.35.1

* Mon Sep 09 2019 Kalev Lember <klember@redhat.com> - 2.34.0-1
- Update to 2.34.0

* Thu Sep 05 2019 Miro Hrončok <mhroncok@redhat.com> - 2.33.92-2
- Subpackage python2-pyatspi has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Tue Sep 03 2019 Kalev Lember <klember@redhat.com> - 2.33.92-1
- Update to 2.33.92

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.33.90-2
- Rebuilt for Python 3.8

* Mon Aug 12 2019 Kalev Lember <klember@redhat.com> - 2.33.90-1
- Update to 2.33.90

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.33.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Kalev Lember <klember@redhat.com> - 2.33.2-1
- Update to 2.33.2

* Tue May 21 2019 Kalev Lember <klember@redhat.com> - 2.33.1-1
- Update to 2.33.1

* Tue Apr 09 2019 Kalev Lember <klember@redhat.com> - 2.32.1-1
- Update to 2.32.1

* Tue Mar 12 2019 Kalev Lember <klember@redhat.com> - 2.32.0-1
- Update to 2.32.0

* Tue Feb 19 2019 Kalev Lember <klember@redhat.com> - 2.31.2-1
- Update to 2.31.2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.31.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Kalev Lember <klember@redhat.com> - 2.31.1-1
- Update to 2.31.1

* Thu Sep 06 2018 Kalev Lember <klember@redhat.com> - 2.30.0-1
- Update to 2.30.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.26.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.26.0-6
- Rebuilt for Python 3.7

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.26.0-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.26.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 20 2017 Merlin Mathesius <mmathesi@redhat.com> - 2.26.0-3
- Cleanup spec file conditionals

* Thu Sep 14 2017 Kalev Lember <klember@redhat.com> - 2.26.0-2
- Update requires for python2-gobject rename

* Wed Sep 13 2017 Kalev Lember <klember@redhat.com> - 2.26.0-1
- Update to 2.26.0

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.25.3-3
- Python 2 binary package renamed to python2-pyatspi
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.25.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 25 2017 Kalev Lember <klember@redhat.com> - 2.25.3-1
- Update to 2.25.3

* Mon Jun 12 2017 Kalev Lember <klember@redhat.com> - 2.25.2-1
- Update to 2.25.2

* Tue Mar 21 2017 Kalev Lember <klember@redhat.com> - 2.24.0-1
- Update to 2.24.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 17 2017 Kalev Lember <klember@redhat.com> - 2.20.3-1
- Update to 2.20.3

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.20.2-3
- Rebuild for Python 3.6
- Rename enum module and Enum class not to conflict with stdlib - BGO #776366

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.20.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon May 09 2016 Kalev Lember <klember@redhat.com> - 2.20.2-1
- Update to 2.20.2

* Wed Apr 13 2016 Kalev Lember <klember@redhat.com> - 2.20.1-1
- Update to 2.20.1

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 2.20.0-1
- Update to 2.20.0

* Tue Mar 01 2016 Richard Hughes <rhughes@redhat.com> - 2.19.91-1
- Update to 2.19.91

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 2.18.0-1
- Update to 2.18.0

* Mon Aug 17 2015 Kalev Lember <klember@redhat.com> - 2.17.90-1
- Update to 2.17.90
- Use make_install macro

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 24 2015 Kalev Lember <kalevlember@gmail.com> - 2.16.0-1
- Update to 2.16.0
- Use license macro for the COPYING files

* Tue Feb 17 2015 Richard Hughes <rhughes@redhat.com> - 2.15.90-1
- Update to 2.15.90

* Tue Feb 03 2015 Richard Hughes <rhughes@redhat.com> - 2.15.4-1
- Update to 2.15.4

* Fri Dec 19 2014 Richard Hughes <rhughes@redhat.com> - 2.15.3-1
- Update to 2.15.3

* Mon Sep 22 2014 Kalev Lember <kalevlember@gmail.com> - 2.14.0-1
- Update to 2.14.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 2.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Mar 24 2014 Kalev Lember <kalevlember@gmail.com> - 2.12.0-1
- Update to 2.12.0

* Tue Mar 18 2014 Richard Hughes <rhughes@redhat.com> - 2.11.92-1
- Update to 2.11.92

* Wed Feb 19 2014 Richard Hughes <rhughes@redhat.com> - 2.11.90-1
- Update to 2.11.90

* Tue Dec 17 2013 Richard Hughes <rhughes@redhat.com> - 2.11.3-1
- Update to 2.11.3

* Tue Nov 19 2013 Richard Hughes <rhughes@redhat.com> - 2.11.2-1
- Update to 2.11.2

* Wed Sep 25 2013 Kalev Lember <kalevlember@gmail.com> - 2.10.0-1
- Update to 2.10.0

* Tue Sep 17 2013 Kalev Lember <kalevlember@gmail.com> - 2.9.92-1
- Update to 2.9.92

* Thu Aug 22 2013 Kalev Lember <kalevlember@gmail.com> - 2.9.90-1
- Update to 2.9.90

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 20 2013 Kalev Lember <kalevlember@gmail.com> - 2.9.3-1
- Update to 2.9.3

* Sun Jun 02 2013 Kalev Lember <kalevlember@gmail.com> - 2.9.2-1
- Update to 2.9.2

* Mon Apr 15 2013 Rui Matos <rmatos@redhat.com> - 2.8.0-2
- Don't depend on python3 in RHEL

* Mon Mar 25 2013 Kalev Lember <kalevlember@gmail.com> - 2.8.0-1
- Update to 2.8.0

* Wed Mar 20 2013 Kalev Lember <kalevlember@gmail.com> - 2.7.91-1
- Update to 2.7.91

* Sat Feb 23 2013 Kalev Lember <kalevlember@gmail.com> - 2.7.5-2
- Build python3-pyatspi with Python 3 support

* Wed Feb 06 2013 Kalev Lember <kalevlember@gmail.com> - 2.7.5-1
- Update to 2.7.5

* Fri Nov 09 2012 Kalev Lember <kalevlember@gmail.com> - 2.7.1-1
- Update to 2.7.1
- Include magFocusTracker.py example in documentation

* Wed Jul 18 2012 Kalev Lember <kalevlember@gmail.com> - 2.5.4-1
- Update to 2.5.4
- Removed python_sitelib definition; no longer needed with recent rpmbuild

* Thu Jun 28 2012 Kalev Lember <kalevlember@gmail.com> - 2.5.3-1
- Update to 2.5.3

* Sat May 05 2012 Kalev Lember <kalevlember@gmail.com> - 2.5.1-1
- Update to 2.5.1

* Wed Mar 28 2012 Richard Hughes <hughsient@gmail.com> - 2.4.0-1
- Update to 2.4.0

* Wed Mar 21 2012 Kalev Lember <kalevlember@gmail.com> - 2.3.92-1
- Update to 2.3.92

* Mon Mar  5 2012 Matthias Clasen <mclasen@redhat.com> - 2.3.91-1
- Update to 2.3.91

* Tue Feb  7 2012 Matthias Clasen <mclasen@redhat.com> - 2.3.5-1
- Update to 2.3.5

* Tue Jan 17 2012 Matthias Clasen <mclasen@redhat.com> - 2.3.4-1
- Update to 2.3.4

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 18 2011 Matthias Clasen <mclasen@redhat.com> - 2.2.1-1
- Update to 2.2.1

* Wed Sep 28 2011 Matthias Clasen <mclasen@redhat.com> - 2.2.0-1
- Update to 2.2.0

* Tue Sep 20 2011 Matthias Clasen <mclasen@redhat.com> - 2.1.91-1
- Update to 2.1.91

* Mon Jul 25 2011 Matthias Clasen <mclasen@redhat.com> - 2.1.4-1
- Update to 2.1.4

* Thu Jun 16 2011 Tomas Bzatek <tbzatek@redhat.com> - 2.1.2-1
- Update to 2.1.2

* Wed May 11 2011 Tomas Bzatek <tbzatek@redhat.com> - 2.1.1-1
- Update to 2.1.1

* Tue Apr 26 2011 Matthias Clasen <mclasen@redhat.com> - 2.0.1-1
- Update to 2.0.1

* Mon Apr  4 2011 Matthias Clasen <mclasen@redhat.com> - 2.0.0-1
- Update to 2.0.0

* Tue Mar 22 2011 Matthias Clasen <mclasen@redhat.com> - 1.91.92-1
- Update to 1.91.92

* Mon Mar  7 2011 Matthias Clasen <mclasen@redhat.com> - 1.91.91-1
- Update to 1.91.91

* Tue Feb 22 2011 Matthias Clasen <mclasen@redhat.com> - 1.91.90-1
- Update to 1.91.90

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.91.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Christopher Aillon <caillon@redhat.com> - 1.91.6-1
- Update to 1.91.6

* Tue Jan 11 2011 Matthias Clasen <mclasen@redhat.com> - 1.91.5-1
- Update to 1.91.5

* Thu Dec  2 2010 Matthias Clasen <mclasen@redhat.com> - 1.91.3-1
- Update to 1.91.3

* Tue Oct  5 2010 Matthias Clasen <mclasen@redhat.com> - 1.91.0-1
- Update to 1.91.0

* Wed Sep 29 2010 Matthias Clasen <mclasen@redhat.com> - 0.4.0-1
- Update to 0.4.0

* Mon Sep 20 2010 Matthias Clasen <mclasen@redhat.com> - 0.3.91-2
- Require python-xlib and and gnome-python2-gconf (#635484)

* Tue Aug 31 2010 Matthias Clasen <mclasen@redhat.com> - 0.3.91-1
- Update to 0.3.91

* Wed Aug 18 2010 Matthias Clasen <mclasen@redhat.com> - 0.3.90-1
- Update to 0.3.90

* Mon Aug  2 2010 Matthias Clasen <mclasen@redhat.com> - 0.3.6-1
- Update to 0.3.6

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jun 29 2010 Matthias Clasen <mclasen@redhat.com> - 0.3.4-1
- Update to 0.3.4

* Tue Jun  8 2010 Matthias Clasen <mclasen@redhat.com> - 0.3.3-1
- Update to 0.3.3

* Fri May 28 2010 Matthias Clasen <mclasen@redhat.com> - 0.3.2-1
- Update to 0.3.2

* Sat May 15 2010 Matthias Clasen <mclasen@redhat.com> - 0.3.1.1-1
- Update to 0.3.1.1

* Tue Mar 30 2010 Matthias Clasen <mclasen@redhat.com> - 0.1.8-1
- Update to 0.1.8

* Sat Feb 20 2010 Matthias Clasen <mclasen@redhat.com> - 0.1.7-1
- Update to 0.1.7

* Wed Feb 10 2010 Tomas Bzatek <tbzatek@redhat.com> - 0.1.6-1
- Update to 0.1.6

* Wed Feb  3 2010 Matthias Clasen <mclasen@redhat.com> - 0.1.5-2
- Relocate

* Sun Jan 17 2010 Matthias Clasen <mclasen@redhat.com> - 0.1.5-1
- Update to 0.1.5

* Thu Jan  7 2010 Matthias Clasen <mclasen@redhat.com> - 0.1.4-3
- Incorporate review feedback

* Thu Jan  7 2010 Matthias Clasen <mclasen@redhat.com> - 0.1.4-2
- Fix License field
- Change CORBA/DBus switching method

* Tue Dec 22 2009 Matthias Clasen <mclasen@redhat.com> - 0.1.4-1
- Update to 0.1.4

* Sat Dec  5 2009 Matthias Clasen <mclasen@redhat.com> - 0.1.3-1
- Initial packaging
