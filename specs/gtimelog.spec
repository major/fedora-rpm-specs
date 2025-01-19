Name:           gtimelog
Version:        0.12.0
Release:        4%{?dist}
Summary:        Unobtrusively keep track of your time

License:        GPL-2.0-or-later
URL:            https://gtimelog.org/
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-freezegun
BuildRequires:  python3-mock
BuildRequires:  python3-setuptools
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-install
BuildRequires:  /usr/bin/msgfmt
BuildRequires:  /usr/bin/rst2man
Requires:       gtk3
Requires:       libsecret
Requires:       libsoup3
Requires:       python3-gobject
Recommends:     yelp

%description
GTimeLog is a small GTK+ app for keeping track of your time. It's main goal is
to be as unobtrusive as possible.

%prep
%autosetup -p1


%build
%{__python3} setup.py build
# Generates the man pages.
make all


%install
%{__python3} setup.py install --skip-build --root %{buildroot}
desktop-file-install %{name}.desktop
# Needed for the desktop file.
install -d %{buildroot}/%{_datadir}/pixmaps
mv %{buildroot}%{python3_sitelib}/%{name}/*.png %{buildroot}/%{_datadir}/pixmaps
install -Dpm 644 %{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1
install -Dpm 644 %{name}.appdata.xml %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
install -Dpm 644 src/gtimelog/data/org.gtimelog.gschema.xml %{buildroot}/%{_datadir}/glib-2.0/schemas/org.gtimelog.gschema.xml


%check
# Runs tests on the source tree.
%{__python3} ./runtests
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml


%files
%doc CHANGES.rst CONTRIBUTING.rst src/gtimelog/CONTRIBUTORS.rst README.rst TODO.rst
%license COPYING
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.gtimelog.gschema.xml
%{_datadir}/pixmaps/%{name}*.png
%{_mandir}/man1/%{name}.1*
%{python3_sitelib}/%{name}*



%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.12.0-2
- Rebuilt for Python 3.13

* Thu Apr 04 2024 David King <amigadave@amigadave.com> - 0.12.0-1
- Update to 0.12.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.11.3-17
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.11.3-14
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 08 2021 David King <amigadave@amigadave.com> - 0.11.3-12
- Fix check_reload attribute error (#1901776)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.11.3-10
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 David King <amigadave@amigadave.com> - 0.11.3-7
- BuildRequire python3-setuptools explicitly

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.11.3-6
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11.3-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11.3-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 David King <amigadave@amigadave.com> - 0.11.3-1
- Update to 0.11.3 (#1602976)

* Sun Feb 17 2019 Till Hofmann <thofmann@fedoraproject.org> - 0.11.2-2
- Add patch to correctly deal with three asterisks

* Sun Feb 17 2019 Till Hofmann <thofmann@fedoraproject.org> - 0.11.2-1
- Update to 0.11.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.11-3
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 19 2017 David King <amigadave@amigadave.com> - 0.11-1
- Update to 0.11 (#1381205)

* Tue Oct 31 2017 David King <amigadave@amigadave.com> - 0.10.3-1
- Update to 0.10.3 (#1419155)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.10.2-2
- Rebuild for Python 3.6

* Mon Oct 03 2016 David King <amigadave@amigadave.com> - 0.10.2-1
- Update to 0.10.2 (#1381205)

* Mon Sep 26 2016 David King <amigadave@amigadave.com> - 0.10.1-1
- Update to 0.10.1 (#1378640)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Sep 30 2015 David King <amigadave@amigadave.com> - 0.10.0-1
- Update to 0.10.0 (#1267408)

* Wed Sep 30 2015 David King <amigadave@amigadave.com> - 0.9.3-1
- Update to 0.9.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 09 2015 David King <amigadave@amigadave.com> - 0.9.2-1
- Initial packaging (#1210252)
