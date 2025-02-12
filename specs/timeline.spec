Name:		timeline
Version:	2.10.0
Release:	1%{?dist}
Summary:	Displays and navigates events on a timeline

License:	GPL-3.0-only
URL:		http://thetimelineproj.sourceforge.net/
Source0:	http://downloads.sourceforge.net/thetimelineproj/%{name}-%{version}.zip
Source1:	timeline.desktop
Patch0:		paths.patch
BuildArch:	noarch
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	python3-devel
Requires:	python3-wxpython4
Requires:	python3-markdown
Requires:	python3-icalendar
Requires:	python3-svg
Requires:	python3-humblewx
Requires:	hicolor-icon-theme

%description
Timeline is a cross-platform application for displaying and navigating 
events on a timeline.

%prep
%setup -q

%patch -P 0 -p0

%build

python3 ./tools/generate-mo-files.py

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/timeline

install -m 755 source/timeline.py $RPM_BUILD_ROOT%{_bindir}/timeline
cp -pr icons $RPM_BUILD_ROOT%{_datadir}/timeline/

mkdir -p $RPM_BUILD_ROOT%{python3_sitelib}/timelinelib
cp -pr source/timelinelib/* $RPM_BUILD_ROOT%{python3_sitelib}/timelinelib/

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 icons/48.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/timeline.png

desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/locale
cp -a translations/*/ $RPM_BUILD_ROOT%{_datadir}/locale/

#Drop bundled python dependencies.
rm -rf $RPM_BUILD_ROOT%{_datadir}/timeline/dependencies

%find_lang %{name}


%files -f %{name}.lang
%license COPYING
%doc AUTHORS README documentation/
%{_bindir}/*
%{_datadir}/timeline
%{_datadir}/applications/timeline.desktop
%{_datadir}/icons/hicolor/48x48/apps/timeline.png
%{python3_sitelib}/timelinelib*

%changelog
* Mon Feb 10 2025 Gwyn Ciesla <gwync@protonmail.com> - 2.10.0-1
- 2.10.0

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.9.0-3
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Sep 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.9.0-1
- 2.9.0

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.8.0-4
- Rebuilt for Python 3.12

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.8.0-3
- migrated to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.8.0-1
- 2.8.0

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Gwyn Ciesla <gwync@protonmail.com> - 2.7.0-1
- 2.7.0

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.6.0-2
- Rebuilt for Python 3.11

* Wed Feb 23 2022 Gwyn Ciesla <gwync@protonmail.com> - 2.6.0-1
- 2.6.0

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct 06 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.5.0-1
- 2.5.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.4.0-2
- Rebuilt for Python 3.10

* Thu Apr 08 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.4.0-1
- 2.4.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 12 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.3.1-1
- 2.3.1

* Mon Oct 19 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.3.0-1
- 2.3.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-2
- Rebuilt for Python 3.9

* Wed May 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.2.0-1
- 2.2.0

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.1.0-1
- 2.1.0

* Mon Nov 04 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.0.0-5
- 2.0.0 final.

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-4.beta.e73292739f1c
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-3.beta.e73292739f1c
- Rebuilt for Python 3.8

* Fri Aug 16 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.0.0-2.beta.e73292739f1c
- Fix versioning.

* Tue Aug 13 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.0.0-1.beta.e73292739f1c
- New beta.

* Tue Aug 13 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.0.0-0.beta.e83ec88dc927
- First 2.0.0 beta, Python 3.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.19.0-1
- 0.19.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 10 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.18.0-2
- Fix shebang handling.

* Wed Aug 01 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.18.0-1
- 1.18.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 27 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.17.0-1
- Latest upstream.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.16.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.16.0-2
- Remove obsolete scriptlets

* Mon Nov 13 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.16.0-1
- Latest upstream.

* Tue Aug 01 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.15.0-1
- Latest upstream.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 08 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.14.0-1
- Latest upstream.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Jon Ciesla <limburgher@gmail.com> - 1.13.0-1
- Latest upstream.

* Mon Oct 31 2016 Jon Ciesla <limburgher@gmail.com> - 1.12.0-1
- Latest upstream.

* Mon Aug 08 2016 Jon Ciesla <limburgher@gmail.com> - 1.11.0-1
- Latest upstream.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon May 02 2016 Jon Ciesla <limburgher@gmail.com> - 1.10.0-1
- Latest upstream.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 31 2016 Rickard Lindberg <ricli85@gmail.com> - 1.9.0-1
- Latest upstream.

* Thu Nov 26 2015 Rickard Lindberg <ricli85@gmail.com> - 1.8.1-1
- Latest upstream.

* Wed Nov 04 2015 Jon Ciesla <limburgher@gmail.com> - 1.5.0-3
- Fix python2 macros and BR, BZ 1277701.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 03 2015 Jon Ciesla <limburgher@gmail.com> - 1.5.0-1
- Latest upstream.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Jon Ciesla <limburgher@gmail.com> - 1.2.4-1
- Latest upstream.

* Mon Oct 21 2013 Jon Ciesla <limburgher@gmail.com> - 1.0.1-1
- Latest upstream.

* Fri Oct 11 2013 Jon Ciesla <limburgher@gmail.com> - 0.20.0-3
- Fix typo, BZ 1018161.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 15 2013 Jon Ciesla <limburgher@gmail.com> - 0.20.0-1
- Latest upstream.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 19 2012 Jon Ciesla <limburgher@gmail.com> - 0.18.0-1
- Latest upstream.
- Fix end-of-line encodings.

* Mon Nov 19 2012 Jon Ciesla <limburgher@gmail.com> - 0.16.0-3
- Use system python libs.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 20 2012 Jon Ciesla <limburgher@gmail.com> - 0.16.0-1
- New upstream.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 28 2011 Jon Ciesla <limb@jcomserv.net> - 0.14.0-3
- Incorporated Mamoru's .po fixes.
- Moved scriptlet back to post.
- Moved update icon cache to postrans.
- Dropped scons BR.

* Wed Oct 26 2011 Jon Ciesla <limb@jcomserv.net> - 0.14.0-2
- Fixed license tag.
- Fixed mandir macro.
- Moved scriptlet to posttrans.
- Dropped INSTALL.

* Thu Oct 20 2011 Jon Ciesla <limb@jcomserv.net> - 0.14.0-1
- First build.
