%global git_commit cab8248e5ea7d3c0c8aad2b0fb11f5750de8e13a
%global git_date 20240429

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

%global version_strip_caret %(VER='%{version}'; echo "${VER/^*/}")

Name:		chirp
Version:	0.4.0^%{git_suffix}
Release:	11%{?dist}
Summary:	A tool for programming two-way radio equipment

License:	GPL-3.0-or-later
URL:		http://chirp.danplanet.com/
#Source0:	https://github.com/kk7ds/chirp/archive/%%{git_commit}/%%{name}-%%{git_commit}.tar.gz
Source0:	https://archive.chirpmyradio.com/chirp_next/next-%{version}/%{name}-%{version}.tar.gz
Source1:	com.danplanet.CHIRP.metainfo.xml
# reported upstream
Patch0:		chirp-0.4.0-drop-future.patch

BuildArch:	noarch

BuildRequires:	coreutils
BuildRequires:	sed
BuildRequires:	gettext
BuildRequires:	make
BuildRequires:	python3-devel
BuildRequires:	desktop-file-utils
BuildRequires:	hicolor-icon-theme
Requires:	hicolor-icon-theme

%description
Chirp is a tool for programming two-way radio equipment It provides a generic
user interface to the programming data and process that can drive many radio
models under the hood.


%prep
%autosetup -p1 -n %{name}-%{git_commit}

# Fix version
sed -i 's/\(\bversion\s*=\s*\)0\b/\1"%{version_strip_caret}"/' setup.py

# Rename package to avoid pypi conflict
sed -i 's/\(\bname\s*=\s*'"'"'\)chirp'"'"'/\1chirp-project'"'"'/' setup.py


%generate_buildrequires
%pyproject_buildrequires -t -x wx


%build
%pyproject_wheel
%make_build -C chirp/locale


%install
%pyproject_install
%pyproject_save_files chirp

# Locale
mkdir -p %{buildroot}%{_datadir}/locale
pushd chirp/locale
cp -prt %{buildroot}%{_datadir}/locale `ls -d */`
popd
ln -frs %{buildroot}%{_datadir}/locale \
  %{buildroot}%{python3_sitelib}/chirp/locale
%find_lang CHIRP

# Install files to correct location
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}%{python3_sitelib}/chirp/share/chirp.desktop
install -Dpm 0644 %{buildroot}%{python3_sitelib}/chirp/share/chirp.svg \
  %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/chirp.svg
install -Dpm 0644 %{SOURCE1} \
  %{buildroot}%{_metainfodir}/com.danplanet.CHIRP.metainfo.xml
install -Dpm 0644 %{buildroot}%{python3_sitelib}/chirp/share/chirpw.1 \
  %{buildroot}%{_mandir}/man1/chirp.1
# Symlink to resources
ln -frs %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/chirp.svg \
  %{buildroot}%{python3_sitelib}/chirp/share/chirp.svg
ln -frs %{buildroot}%{_datadir}/applications/chirp.desktop \
  %{buildroot}%{python3_sitelib}/chirp/share/chirp.desktop
ln -frs %{buildroot}%{_mandir}/man1/chirp.1.gz \
  %{buildroot}%{python3_sitelib}/chirp/share/chirpw.1


%check
%tox


%files -f %{pyproject_files} -f CHIRP.lang
%license COPYING
%doc README.chirpc README.developers
%{_bindir}/chirpc
%{python3_sitelib}/chirp/locale

%pyproject_extras_subpkg -n chirp wx
%{_bindir}/chirp
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/chirp.svg
%{_metainfodir}/com.danplanet.CHIRP.metainfo.xml
%{_mandir}/man1/chirp.1.gz


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0^20240429gitcab8248e-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0^20240429gitcab8248e-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.4.0^20240429gitcab8248e-9
- Rebuilt for Python 3.13

* Thu May  2 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4.0^20240429gitcab8248e-8
- Dropped python3-future requirement from the tox
  Related: rhbz#2276608

* Mon Apr 29 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4.0^20240429gitcab8248e-7
- New snapshot
  Resolves: rhbz#2276608

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0^20231101git35c8a1c0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0^20231101git35c8a1c0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 20 2023 Daniel Rusek <mail@asciiwolf.com> - 0.4.0^20231101git35c8a1c0-4
- Added AppStream metadata

* Mon Nov  6 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4.0^20231101git35c8a1c0-3
- Updated according to the review

* Thu Nov  2 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4.0^20231101git35c8a1c0-2
- Updated according to the review

* Wed Nov  1 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4.0^20231101git35c8a1c0-1
- New version
- Updated according to the review

* Sun Oct 22 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4.0^20231010git68f6a46f-3
- Updated according to the review

* Tue Oct 17 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4.0^20231010git68f6a46f-2
- Updated according to the review

* Tue Oct 10 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4.0^20231010git68f6a46f-1
- New version

* Mon Sep  5 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.3.0^20220905git8bc8553c-1
- Switched to github, which is also offical upstream source

* Sun Aug 28 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.3.0^20220828hg3608-1
- New version

* Thu May 14 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0.3.0-0.1.20200514hg3351
- New experimental python3 version

* Thu Apr 30 2020 Richard Shaw <hobbes1069@gmail.com> - 20200430-1
- Update to 20200430.

* Mon Apr 13 2020 Richard Shaw <hobbes1069@gmail.com> - 20200409-1
- Update to 20200409.

* Thu Feb 27 2020 Richard Shaw <hobbes1069@gmail.com> - 20200227-1
- Update to 20200227.

* Tue Feb 18 2020 Richard Shaw <hobbes1069@gmail.com> - 20200213-1
- Update to 20200213.

* Fri Jan 03 2020 Richard Shaw <hobbes1069@gmail.com> - 20200103-1
- Update to 20200103.

* Mon Dec 23 2019 Richard Shaw <hobbes1069@gmail.com> - 20191221-1
- Update to 20191221.

* Fri Dec 06 2019 Richard Shaw <hobbes1069@gmail.com> - 20191206-1
- Update to 20191206.
- Unretire chirp on f31 only.
- Remove tk8180 driver as it relies on python2-future which is not available.

* Mon Aug 12 2019 Richard Shaw <hobbes1069@gmail.com> - 20190812-1
- Update to 20190812.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20190718-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Richard Shaw <hobbes1069@gmail.com> - 20190718-1
- Update to 20190718.

* Sat Jul 13 2019 Richard Shaw <hobbes1069@gmail.com> - 20190713-1
- Update to 20190713.

* Fri Jul 05 2019 Richard Shaw <hobbes1069@gmail.com> - 20190703-1
- Update to 20190703.

* Thu May 30 2019 Richard Shaw <hobbes1069@gmail.com> - 20190524-1
- Update to 20190524.

* Wed Apr 10 2019 Richard Shaw <hobbes1069@gmail.com> - 20190410-1
- Update to 20190410.

* Tue Mar 19 2019 Richard Shaw <hobbes1069@gmail.com> - 20190319-1
- Update to 20190319.

* Mon Mar 04 2019 Richard Shaw <hobbes1069@gmail.com> - 20190304-1
- Update to 20190304.

* Sun Mar 03 2019 Richard Shaw <hobbes1069@gmail.com> - 20190303-1
- Update to 20190303.

* Thu Feb 28 2019 Richard Shaw <hobbes1069@gmail.com> - 20190227-1
- Update to 20190227.

* Sun Feb 24 2019 Richard Shaw <hobbes1069@gmail.com> - 20190222-1
- Update to 20190222.

* Wed Feb 20 2019 Richard Shaw <hobbes1069@gmail.com> - 20190220-1
- Update to 20190220.

* Tue Feb 19 2019 Richard Shaw <hobbes1069@gmail.com> - 20190219-1
- Update to 20190219.

* Mon Feb 18 2019 Richard Shaw <hobbes1069@gmail.com> - 20190218-1
- Update to 20190218.

* Sun Feb 17 2019 Richard Shaw <hobbes1069@gmail.com> - 20190217-1
- Update to 20190217.

* Fri Feb 15 2019 Richard Shaw <hobbes1069@gmail.com> - 20190215-1
- Update to 20190215.

* Sat Feb 09 2019 Richard Shaw <hobbes1069@gmail.com> - 20190209-1
- Update to 20190209.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20190120-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Richard Shaw <hobbes1069@gmail.com> - 20190120-1
- Update to 20190120.

* Sat Jan 19 2019 Richard Shaw <hobbes1069@gmail.com> - 20190112-1
- Update to 20190112.

* Fri Jan 04 2019 Richard Shaw <hobbes1069@gmail.com> - 20190104-1
- Update to 20190104.

* Wed Jan 02 2019 Richard Shaw <hobbes1069@gmail.com> - 20190102-1
- Update to 20190102.

* Mon Dec 17 2018 Richard Shaw <hobbes1069@gmail.com> - 20181214-1
- Update to 20181214.

* Thu Dec 06 2018 Richard Shaw <hobbes1069@gmail.com> - 20181205-1
- Update to 20181205.

* Fri Nov 30 2018 Richard Shaw <hobbes1069@gmail.com> - 20181128-1
- Update to 20181128.

* Mon Sep 10 2018 Richard Shaw <hobbes1069@gmail.com> - 20180906-2
- Fix install requirements.

* Sat Sep 08 2018 Richard Shaw <hobbes1069@gmail.com> - 20180906-1
- Update to 20180906.
- Initial build for epel7.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20180614-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Richard Shaw <hobbes1069@gmail.com> - 20180614-1
- Update to 20180614.
- Add appdata file.

* Wed Jun 06 2018 Richard Shaw <hobbes1069@gmail.com> - 20180606-1
- Update to 20180606.

* Tue Mar 13 2018 Richard Shaw <hobbes1069@gmail.com> - 20180313-1
- Update to 20180313

* Sat Feb 10 2018 Richard Shaw <hobbes1069@gmail.com> - 20180210-1
- Update to 20180210.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20171204-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 15 2017 Iryna Shcherbina <ishcherb@redhat.com> - 20171204-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Dec 06 2017 Richard Shaw <hobbes1069@gmail.com> - 20171204-1
- Update to latest upstream release.
- Fix ambiguous Python 2 dependency declarations
  https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170711-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 11 2017 Richard Shaw <hobbes1069@gmail.com> - 20170711-1
- Update to latest upstream release.

* Sat Mar  4 2017 Richard Shaw <hobbes1069@gmail.com> - 20170222-1
- Update to latest upstream release.
- Add pygtk2 as a runtime requirement, fixes RHBZ#1428979.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170115-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 15 2017 Richard Shaw <hobbes1069@gmail.com> - 20170115-1
- Update to latest upstream release.

* Tue Oct 18 2016 Richard Shaw <hobbes1069@gmail.com> - 20161018-1
- Update to latest upstream release.

* Tue Aug 23 2016 Richard Shaw <hobbes1069@gmail.com> - 20160819-1
- Update to latest upstream release.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20160706-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jul  7 2016 Richard Shaw <hobbes1069@gmail.com> - 20160706-1
- Update to latest upstream release.

* Mon May 23 2016 Richard Shaw <hobbes1069@gmail.com> - 20160517-1
- Update to latest upstream release.

* Wed May  4 2016 Richard Shaw <hobbes1069@gmail.com> - 20160504-1
- Update to latest upstream release.

* Wed Apr  6 2016 Richard Shaw <hobbes1069@gmail.com> - 20160402-1
- Update to latest upstream release.

* Wed Mar  9 2016 Richard Shaw <hobbes1069@gmail.com> - 20160309-1
- Update to latest upstream release.

* Mon Feb 29 2016 Richard Shaw <hobbes1069@gmail.com> - 20160229-1
- Update to latest upstream release.

* Thu Feb 18 2016 Richard Shaw <hobbes1069@gmail.com> - 20160215-1
- Update to latest upstream release.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20151130-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 30 2015 Richard Shaw <hobbes1069@gmail.com> - 20151130-1
- Update to new rolling release.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct  9 2014 Richard Shaw <hobbes1069@gmail.com> - 0.4.1-1
- Update to latest bugfix release.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 26 2014 Richard Shaw <hobbes1069@gmail.com> - 0.4.0-1
- Update to latest upstream release.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 06 2013 Richard Shaw <hobbes1069@gmail.com> - 0.3.1-1
- Update to latest upstream release.

* Sat Feb 16 2013 Richard Shaw <hobbes1069@gmail.com> - 0.3.0-1
- Update to latest upstream release.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 04 2012 Richard Shaw <hobbes1069@gmail.com> - 0.2.2-1
- Update to latest upstream release.

* Sun Mar 18 2012 Richard Shaw <hobbes1069@gmail.com> - 0.2.0-1
- Update to latest upstream release.

* Sun Nov 20 2011 Randall "Randy" Berry, N3LRX <dp67@fedoraproject.org> - 0.1.12-5
- Add source for .desktop, per review

* Sun Nov 20 2011 Randall "Randy" Berry, N3LRX <dp67@fedoraproject.org> - 0.1.12-4
- Add source for patches, per review

* Sun Nov 20 2011 Randall "Randy" Berry, N3LRX <dp67@fedoraproject.org> - 0.1.12-3
- Submit for review

* Sat Nov 19 2011 Randall "Randy" Berry, N3LRX <dp67@fedoraproject.org> - 0.1.12-2
- Own unowned directories
- Add correct .desktop file
- Apply patch to move COPYING file to proper directory
- Add shebang patch removes shebang from unnecessary files

* Sat Nov 19 2011 Randall "Randy" Berry, N3LRX <dp67@fedoraproject.org> - 0.1.12-1
- Initial Build and testing
