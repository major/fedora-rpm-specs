Name:           quearcode
Version:        0.4
Release:        2%{?dist}
Summary:        A tool for creating QR Codes

License:        GPL-3.0-or-later
URL:            https://codeberg.org/gwync/quearcode
Source0:        https://codeberg.org/gwync/quearcode/archive/%{version}.tar.gz
Source1:        quearcode.desktop
BuildArch:      noarch
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-qrcode python3-gobject hicolor-icon-theme

%description
Convert strings and small files to QR Codes

%prep
%setup -qn %{name}

%generate_buildrequires
%pyproject_buildrequires

%build
./t_build.sh
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pyquearcode
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata

install -m 644 quearcode.appdata.xml $RPM_BUILD_ROOT%{_datadir}/appdata/

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 pyquearcode/logo.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/quearcode.png

desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}


%check
%pyproject_check_import


%files
%doc COPYING README.md
%{_bindir}/quearcode
%{_datadir}/applications/quearcode.desktop
%{_datadir}/icons/hicolor/scalable/apps/quearcode.png
%{_datadir}/appdata/quearcode.appdata.xml
%{python3_sitelib}/pyquearcode
%{python3_sitelib}/quearcode-%{version}.dist-info/

%changelog
* Wed Feb 05 2025 Gwyn Ciesla <gwync@protonmail.com> - 0.4-2
- Drop BR -t

* Fri Jan 24 2025 Gwyn Ciesla <gwync@protonmail.com> - 0.4-1
- 0.4

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 27 2024 Gwyn Ciesla <gwync@protonmail.com> - 0.3-1
- 0.3

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.2.7-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.2.7-5
- Rebuilt for Python 3.12

* Sun Mar 05 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.2.7-4
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 12 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.2.7-1
- 0.2.7, german and spanish translations.

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jul 29 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.2.6-1
- 0.2.6, view and save internally.

* Thu Jul 25 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.2.5-2
- Fix requires.

* Wed Jul 24 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.2.5-1
- 0.2.5

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.4-5
- Remove obsolete scriptlets

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-2
- Rebuild for Python 3.6

* Fri Sep 09 2016 Jon Ciesla <limburgher@gmail.com> - 0.2.4-1
- Typo fix, code cleanup.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 28 2015 Jon Ciesla <limburgher@gmail.com> - 0.2.3-1
- Latest upstream, migrated to Python 3.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Sep 18 2014 Jon Ciesla <limburgher@gmail.com> - 0.2.2-1
- Latest upstream, includes appdata.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Sep 13 2012 Jon Ciesla <limburgher@gmail.com> - 0.2.1-1
- 0.2.1, better size error handling.

* Wed Sep 12 2012 Jon Ciesla <limburgher@gmail.com> - 0.2-2
- URL fix for review.

* Tue Sep 11 2012 Jon Ciesla <limburgher@gmail.com> - 0.2-1
- 0.2, deeper control of generation.

* Tue Sep 11 2012 Jon Ciesla <limburgher@gmail.com> - 0.1.2-1
- First build.
