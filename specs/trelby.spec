Name:           trelby
Version:        2.4.13
Release:        1%{?dist}
Summary:        The free, multiplatform, feature-rich screenwriting program

License:        GPL-2.0-only AND GPL-3.0-or-later
URL:            https://github.com/trelby/trelby
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  make
BuildRequires:  python3dist(pytest)
Requires:       hicolor-icon-theme

%description
Trelby is simple, fast and elegantly laid out to make
screenwriting simple. It is infinitely configurable.

%prep
%setup -q

%generate_buildrequires
%pyproject_buildrequires

%build
make
%pyproject_wheel
rm -rf doc/.gitignore

%install
%pyproject_install

mkdir -p %{buildroot}%{_datadir}/pixmaps
cp %{buildroot}%{python3_sitelib}/trelby/resources/icon256.png %{buildroot}%{_datadir}/pixmaps/trelby256.png

desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications trelby/resources/trelby.desktop

desktop-file-validate %{buildroot}/%{_datadir}/applications/trelby.desktop

mkdir -p %{buildroot}%{_mandir}/man1/
install -m644 trelby/trelby.1.gz %{buildroot}%{_mandir}/man1/

%check
%pytest

%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{_datadir}/applications/trelby.desktop
%{python3_sitelib}/trelby*
%{_mandir}/man1/trelby.1.gz
%{_datadir}/pixmaps/trelby256.png
%exclude %{python3_sitelib}/tests/

%changelog
* Fri Jan 03 2025 Gwyn Ciesla <gwync@protonmail.com> - 2.4.13-1
- 2.4.13

* Tue Dec 31 2024 Gwyn Ciesla <gwync@protonmail.com> - 2.4.12-1
- 2.4.12

* Thu Dec 12 2024 Gwyn Ciesla <gwync@protonmail.com> - 2.4.11-1
- 2.4.11

* Mon Sep 09 2024 Gwyn Ciesla <gwync@protonmail.com> - 2.4.10-1
- 2.4.10

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 2.4.9-3
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Sep 21 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.4.9-1
- 2.4.9

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 19 2023 Python Maint <python-maint@redhat.com> - 2.4.8-3
- Rebuilt for Python 3.12

* Sun Mar 05 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.4.8-2
- migrated to SPDX license

* Tue Jan 31 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.4.8-1
- 2.4.8

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 24 2022 Gwyn Ciesla <gwync@protonmail.com> - 2.4.7-1
- 2.4.7

* Wed Aug 31 2022 Gwyn Ciesla <gwync@protonmail.com> - 2.4.6-1
- 2.4.6

* Mon Aug 15 2022 Gwyn Ciesla <gwync@protonmail.com> - 2.4.5-1
- 2.4.5

* Fri Jul 22 2022 Gwyn Ciesla <gwync@protonmail.com> - 2.4.4-1
- 2.4.4

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 2.4.3-4
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 08 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.4.3-1
- 2.4.3

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.4.2-2
- Rebuilt for Python 3.10

* Thu Mar 04 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.4.2-1
- Fix license tag, validate desktop file, move to unittest.mock.

* Thu Mar 04 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.4.1-2
- Use macro for prefix.

* Tue Mar 02 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.4.1-1
- 2.4.1

* Mon Feb 22 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.4-3
- Fix man page, manual, tests, 2.4 final.

* Wed Dec 18 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.4-2
- Fix for title page editing.

* Thu Aug 15 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.4-1
- Python3

* Fri Mar 16 2018 Gwyn Ciesla <limburgher@gmail.com> - 2.3-0.dev
- First build.
