# Enable (1 = enabled/0 = disabled) if configure regeneration etc. is required.
%define run_autogen 1

# Needs not yet packaged storj/uplink-c
%bcond_with storj

Name: filezilla
Version: 3.68.1
Release: 2%{?dist}
Summary: FTP, FTPS and SFTP client
License: GPL-2.0-or-later
URL: https://filezilla-project.org/

Source0: https://download.filezilla-project.org/FileZilla_%{version}_src.tar.xz

%if 0%{?rhel} == 8
# libuv-devel not present on s390x on EL-8
ExcludeArch: s390x
%endif

%if 0%{?run_autogen}
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
%endif
BuildRequires: boost-devel
BuildRequires: boost-regex
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: glib2-devel
BuildRequires: cppunit-devel >= 1.13.0
BuildRequires: dbus-devel
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: gnutls-devel >= 2.8.3
BuildRequires: libappstream-glib
BuildRequires: libfilezilla-devel >= 0.35.0
BuildRequires: libidn-devel
%if %{with storj}
BuildRequires: golang-storj-uplink-c-devel
%endif
BuildRequires: nettle-devel
BuildRequires: pugixml-devel >= 1.7
BuildRequires: sqlite-devel
BuildRequires: wxGTK-devel
BuildRequires: xdg-utils
BuildRequires: make

Requires: xdg-utils

%description
FileZilla is a FTP, FTPS and SFTP client for Linux with a lot of features.
- Supports FTP, FTP over SSL/TLS (FTPS) and SSH File Transfer Protocol (SFTP)
- Cross-platform
- Available in many languages
- Supports resume and transfer of large files greater than 4GB
- Easy to use Site Manager and transfer queue
- Drag & drop support
- Speed limits
- Filename filters
- Network configuration wizard 

%prep
%autosetup -p0 -n %{name}-%{version}
%if 0%{?run_autogen}
autoreconf -if
%endif

%build
# For wxGTK3 - needed to find wxrc
export WXRC=%{_bindir}/wxrc-3.2

# Do not use '--enable-buildtype=official' in configure. That option enables the
# "check for updates" dialog to download new binaries from the official website.
%configure \
  --disable-static \
  --enable-locales \
  --disable-manualupdatecheck \
  --with-pugixml=system \
  --with-wx-config=wx-config-3.2 \
  --with-dbus \
  --enable-gnutlssystemciphers \
%if %{with storj}
  --enable-storj \
%endif
  --disable-autoupdatecheck
%make_build

%install
%make_install

# Update the screenshot shown in the software center
#
# NOTE: It would be *awesome* if this file was pushed upstream.
#
# See http://people.freedesktop.org/~hughsient/appdata/#screenshots for more details.
#
appstream-util replace-screenshots $RPM_BUILD_ROOT%{_datadir}/appdata/filezilla.appdata.xml \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/filezilla/a.png 

for i in 16x16 32x32 48x48 ; do
  mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${i}/apps
  ln -sf ../../../../%{name}/resources/${i}/%{name}.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${i}/apps/%{name}.png
done

rm -rf $RPM_BUILD_ROOT%{_datadir}/pixmaps

desktop-file-install \
  --delete-original \
  --dir ${RPM_BUILD_ROOT}%{_datadir}/applications \
  ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop

appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT/%{_datadir}/appdata/%{name}.appdata.xml

# Create directory for system wide settings.
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
# Ghost configuration file.
touch $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/fzdefaults.xml
# This is not the usual docdir.
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/docs

%find_lang %{name}

%check
%make_build check

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS
%doc docs/fzdefaults.xml.example
%license COPYING
%dir %{_sysconfdir}/%{name}
%ghost %{_sysconfdir}/%{name}/fzdefaults.xml
%{_bindir}/%{name}
%{_bindir}/fzputtygen
%{_bindir}/fzsftp
%if %{with storj}
%{_bindir}/fzstorj
%endif
%{_datadir}/%{name}/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_libdir}/libfzclient-private*
%{_libdir}/libfzclient-commonui*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.68.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 04 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.68.1-1
- 3.68.1

* Thu Oct 31 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.68.0-1
- 3.68.0

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.67.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 10 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.67.1-2
- 3.67.1 final

* Wed Jul 10 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.67.1-1
- libfilezilla rebuild

* Fri Jul 05 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.67.1-0
- 3.67.1-rc1

* Wed Jun 26 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.67.0-2
- libfilezilla rebuild

* Mon Apr 15 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.67.0-1
- 3.67.0

* Mon Apr 15 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.66.5-2
- libfilezilla rebuild

* Wed Feb 07 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.66.5-1
- 3.66.5

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.66.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.66.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 20 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.66.4-1
- 3.66.4

* Mon Nov 06 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.66.1-1
- 3.66.1

* Thu Oct 26 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.66.0-1
- 3.66.0

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.63.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 27 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.63.2.1-1
- 3.63.2.1

* Tue Mar 07 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.62.2-4
- migrated to SPDX license

* Thu Jan 19 2023 Scott Talbert <swt@techie.net> - 3.62.2-3
- Rebuild with wxWidgets 3.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.62.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.62.2-1
- 3.62.2

* Fri Jul 22 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.60.2-1
- 3.60.2

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.60.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.60.1-3
- libfilezilla rebuild

* Tue Jul 12 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.60.1-2
- libfilezilla rebuild

* Thu Jun 02 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.60.1-1
- 3.60.1

* Tue May 31 2022 Orion Poplawski <orion@nwra.com> - 3.60.0-2
- Make storj conditional and fixup deps for it

* Fri May 27 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.60.0-1
- 3.60.0

* Fri Apr 08 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.59.0-1
- 3.59.0

* Fri Feb 11 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.58.0-1
- 3.58.0

* Thu Feb 03 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.57.0-3
- libfilezilla rebuild.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.57.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 13 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.57.0-1
- 3.57.0

* Thu Dec 09 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.56.2-2
- libfilezilla rebuild.

* Wed Oct 27 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.56.2-1
- 3.56.2

* Tue Oct 26 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.56.1-1
- 3.56.1

* Tue Oct 12 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.56.0-1
- 3.56.0

* Wed Sep 29 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.55.1-3
- libfilezilla rebuild.

* Tue Sep 14 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.55.1-2
- libfilezilla rebuild.

* Mon Aug 09 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.55.1-1
- 3.55.1

* Wed Jul 28 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.55.0-3
- libfilezilla rebuild.

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.55.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 09 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.55.0-3
- 3.55.0.

* Fri Jul 02 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.54.1-2
- libfilezilla rebuild.

* Fri May 14 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.54.1-1
- 3.54.1

* Tue May 04 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.53.1-2
- libfilezilla rebuild.

* Mon Mar 22 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.53.1-1
- 3.53.1

* Mon Mar 15 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.53.0-1
- 3.53.0

* Thu Mar 04 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.52.2-3
- libfilezilla rebuild.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.52.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.52.2-1
- 3.52.2

* Fri Jan 08 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.52.0.5-1
- 3.52.0.5

* Thu Jan 07 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.52.0.4-1
- 3.52.0.4

* Wed Jan 06 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.52.0.3-1
- 3.52.0.3

* Tue Jan 05 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.52.0.1-1
- 3.52.0.1

* Mon Jan 04 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.52.0-1
- 3.52.0

* Thu Dec 17 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.51.0-2
- libfilezilla rebuild.

* Tue Oct 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.51.0-1
- 3.51.0

* Tue Oct 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.50.0-1
- 3.50.0

* Fri Aug 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.49.1-4
- libfilezilla rebuild

* Wed Aug 12 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.49.1-3
- Exclude s390x on EL-8 due to missing libuv-devel

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.49.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.49.1-1
- 3.49.1

* Tue Jul 14 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.49.0-1
- 3.49.0 final

* Tue Jul 07 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.49.0-0.rc1
- 3.49.0 rc1

* Tue May 19 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.48.1-1
- 3.48.1 final

* Tue May 12 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.48.1-0.rc1
- 3.48.1 rc1

* Tue Apr 28 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.48.0-1
- 3.48.0 final

* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 3.48.0-0.1.rc1
- Rebuild (json-c)

* Mon Apr 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.48.0-0.rc1
- 3.48.0 rc1

* Mon Apr 13 2020 Björn Esser <besser82@fedoraproject.org> - 3.47.2.1-3
- Add patch to fix error: 'std::list' has not been declared
- Build and run tests in parallel

* Thu Mar 12 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.47.2.1-2
- EVR bump.

* Wed Mar 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.47.2.1-1
- 3.47.2.1

* Tue Feb 25 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.47.1-1
- 3.47.1

* Mon Feb 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.47.0-1
- 3.47.0

* Fri Feb 14 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.46.3-4
- Rebuild for new libfilezilla.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.46.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 26 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.46.3-2
- Bump NVR for koji error.

* Thu Dec 26 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.46.3-1
- 3.46.3

* Tue Nov 26 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.46.0-1
- 3.46.0

* Mon Nov 18 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.45.1-2
- Rebuild for new libfilezilla.

* Wed Sep 25 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.45.1-1
- 3.45.1

* Tue Sep 24 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.45.0-1
- 3.45.0

* Thu Aug 15 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.44.2-1
- 3.44.2

* Fri Aug 09 2019 Phil Wyett <philwyett@kathenas.org> - 3.44.1-2
- Correct 'libfilezilla' minimum version requirement.

* Fri Aug 09 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.44.1-1
- 3.44.1

* Fri Aug 02 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.44.0-1.rc1
- 3.44.0-rc1

* Wed Jul 31 2019 Phil Wyett <philwyett@kathenas.org> - 3.43.0-3
- Delete unused patches.
- Fix, modernize and cleanup spec file.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.43.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.43.0-1
- 3.43.0

* Wed May 08 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.42.1-1
- 3.42.1

* Mon May 06 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.42.0-1
- 3.42.0 final.

* Tue Apr 30 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.42.0-0.rc1
- 3.42.0rc1

* Mon Mar 18 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.41.2-1
- 3.41.2

* Wed Mar 06 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.41.1-1
- 3.41.1

* Wed Mar 06 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.41.0-1
- 3.41.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.40.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Gwyn Ciesla <limburgher@gmail.com> - 3.40.0-1
- 3.40.0 final.

* Tue Jan 22 2019 Gwyn Ciesla <limburgher@gmail.com> - 3.40.0-0.rc2
- 3.40.0 rc2

* Fri Nov 30 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.39.0-1
- 3.39.0 final.

* Mon Nov 26 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.39.0-0.rc1
- 3.39.0-rc1

* Sun Oct 28 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.38.1-1
- 3.38.1

* Fri Oct 26 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.38.0-1
- 3.38.0

* Fri Oct 19 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.38.0-0.rc1
- 3.38.0-rc1

* Fri Oct 05 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.37.4-1
- 3.37.4

* Fri Sep 21 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.37.1-1
- 3.37.1

* Mon Sep 17 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.37.0-1
- 3.37.0 final

* Tue Sep 11 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.37.0-0.rc1
- 3.37.0 rc1

* Mon Aug 27 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.36.0-1
- 3.36.0 final

* Mon Aug 20 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.36.0-0.rc1
- 3.36.0 rc1

* Mon Aug 06 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.35.2-1
- 3.35.2

* Mon Jul 23 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.35.1-1
- Latest upstream.

* Tue Jul 17 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.35.0-0.rc2
- Latest upstream.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.34.0-1
- Latest upstream.

* Mon Jun 11 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.34.0-0.rc1
- Latest upstream.

* Mon May 07 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.33.0-1
- Latest upstream.

* Fri Apr 27 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.33.0-0.rc1
- Latest upstream.

* Wed Apr 04 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.32.0-1
- Latest upstream.

* Tue Mar 27 2018 Björn Esser <besser82@fedoraproject.org> - 3.32.0-0.rc1.1
- Rebuilt for libjson-c.so.4 (json-c v0.13.1) on fc28

* Fri Mar 23 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.32.0-0.rc1
- Latest upstream.

* Tue Mar 06 2018 Björn Esser <besser82@fedoraproject.org> - 3.31.0-2
- Rebuilt for libjson-c.so.4 (json-c v0.13.1)

* Fri Feb 23 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.31.0-1
- Latest upstream.

* Tue Feb 20 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.31.0-0.rc1
- Latest upstream.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.30.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.30.0-1
- Latest upstream.

* Thu Jan 04 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.30.0-0.rc1
- Latest upstream.

* Sun Dec 10 2017 Björn Esser <besser82@fedoraproject.org> - 3.29.0-3
- Rebuilt for libjson-c.so.3

* Wed Nov 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.29.0-2
- rebuild

* Mon Nov 06 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.29.0-1
- Latest upstream.

* Wed Nov 01 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.29.0-0.rc1
- Latest upstream.

* Wed Oct 25 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.28.0-2
- Enable storj client.

* Fri Sep 29 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.28.0-1
- Latest upstream.

* Fri Sep 22 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.28.0-0.rc1
- Latest upstream.

* Tue Aug 15 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.27.1-1
- Latest upstream.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.27.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.27.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.27.0.1-1
- Latest upstream.

* Wed Jul 12 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.27.0-0.rc1
- Latest upstream.

* Wed Jun 14 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.26.2-1
- Latest upstream.

* Mon Jun 05 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.26.1-1
- Latest upstream.

* Fri Jun 02 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.26.0-1
- Latest upstream.

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.25.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Mon May 01 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.25.2-1
- Latest upstream.

* Mon Apr 24 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.25.2-0.rc1
- Latest upstream.

* Tue Mar 21 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.25.1-1
- Latest upstream.

* Tue Mar 14 2017 Jon Ciesla <limburgher@gmail.com> - 3.25.0-1
- Latest upstream.

* Mon Mar 06 2017 Jon Ciesla <limburgher@gmail.com> - 3.25.0-0.rc1
- Latest upstream.

* Mon Feb 27 2017 Jon Ciesla <limburgher@gmail.com> - 3.25.0-0.beta1
- Latest upstream.

* Wed Feb 22 2017 Jon Ciesla <limburgher@gmail.com> - 3.24.1-1
- Latest upstream.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 14 2017 Jon Ciesla <limburgher@gmail.com> - 3.24.0-1
- Latest upstream.

* Mon Jan 09 2017 Jon Ciesla <limburgher@gmail.com> - 3.24.0-0.rc1
- Latest upstream.

* Tue Dec 06 2016 Jon Ciesla <limburgher@gmail.com> - 3.23.0.2-1
- Latest upstream.

* Tue Dec 06 2016 Jon Ciesla <limburgher@gmail.com> - 3.23.0.1-1
- Latest upstream.

* Thu Nov 03 2016 Jon Ciesla <limburgher@gmail.com> - 3.22.2.2-1
- Latest upstream.

* Tue Nov 01 2016 Jon Ciesla <limburgher@gmail.com> - 3.22.2-1
- Latest upstream.

* Mon Oct 31 2016 Jon Ciesla <limburgher@gmail.com> - 3.22.2-0.rc2
- Latest upstream.

* Wed Oct 26 2016 Jon Ciesla <limburgher@gmail.com> - 3.22.2-0.rc1
- Latest upstream.

* Tue Oct 04 2016 Jon Ciesla <limburgher@gmail.com> - 3.22.1-1
- Latest upstream.

* Mon Oct 03 2016 Jon Ciesla <limburgher@gmail.com> - 3.22.0-1
- Latest upstream.

* Mon Sep 26 2016 Jon Ciesla <limburgher@gmail.com> - 3.22.0-0.rc1
- Latest upstream.

* Tue Aug 23 2016 Jon Ciesla <limburgher@gmail.com> - 3.21.0-1
- Latest upstream.

* Thu Aug 04 2016 Jon Ciesla <limburgher@gmail.com> - 3.20.1-1
- Latest upstream.

* Thu Jul 28 2016 Jon Ciesla <limburgher@gmail.com> - 3.20.0-1
- Latest upstream.

* Thu Jul 21 2016 Jon Ciesla <limburgher@gmail.com> - 3.20.0-0.rc1
- Latest upstream.

* Fri Jul 08 2016 Jon Ciesla <limburgher@gmail.com> - 3.19.0-2
- Patch for gtk bug, BZ 1351308

* Mon Jun 27 2016 Jon Ciesla <limburgher@gmail.com> - 3.19.0-1
- Latest upstream.

* Tue Jun 21 2016 Jon Ciesla <limburgher@gmail.com> - 3.19.0-0.rc1
- Latest upstream.

* Mon May 30 2016 Jon Ciesla <limburgher@gmail.com> - 3.18.0-1
- Latest upstream.

* Sun May 22 2016 Jon Ciesla <limburgher@gmail.com> - 3.18.0-0.rc1
- Latest upstream.

* Mon May 09 2016 Jon Ciesla <limburgher@gmail.com> - 3.17.0.1-1
- Latest upstream, BZ 1334341.
- Patch for wxString conversion bug.

* Mon Apr 25 2016 Jon Ciesla <limburgher@gmail.com> - 3.17.0-1
- Latest upstream.

* Tue Mar 22 2016 Jon Ciesla <limburgher@gmail.com> - 3.16.1-1
- Latest upstream.

* Tue Mar 15 2016 Jon Ciesla <limburgher@gmail.com> - 3.16.0-1
- Latest upstream, now uses libfilezilla.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 23 2015 Nicolas Chauvet <kwizart@gmail.com> - 3.14.1-2
- Use system pugixml by f24
- Explicitely enable dbus
- Enable system ciphers with upstreamed patch - rhbz#1179288

* Fri Oct 16 2015 Jon Ciesla <limburgher@gmail.com> - 3.14.1-1
- Update to 3.14.1.
- System ciphers patch upstremed.

* Tue Sep 22 2015 Jon Ciesla <limburgher@gmail.com> - 3.14.0-1
- Update to 3.14.0.

* Tue Sep 01 2015 Nicolas Chauvet <kwizart@gmail.com> - 3.13.1-1
- Update to 3.13.1
- Switch from builtin tinyxml to builtin pugixml

* Mon Aug 03 2015 Nicolas Chauvet <kwizart@gmail.com> - 3.12.0.2-2
- Update to system certificate for gnutls - rhbz#1179288

* Wed Jul 22 2015 Nicolas Chauvet <kwizart@gmail.com> - 3.12.0.2-1
- Update to 3.12.0.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jon Ciesla <limburgher@gmail.com> - 3.11.0.2-1
- Update to 3.11.0.2.

* Tue May 26 2015 Jon Ciesla <limburgher@gmail.com> - 3.11.0.1-1
- Update to 3.11.0.1.

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.10.3-2
- Rebuilt for GCC 5 C++11 ABI change

* Thu Apr 02 2015 Nicolas Chauvet <kwizart@gmail.com> - 3.10.3-1
- Update to 3.10.3

* Mon Mar 30 2015 Richard Hughes <rhughes@redhat.com> - 3.10.3-0.3
- Use better AppData screenshots

* Tue Mar 17 2015 Nicolas Chauvet <kwizart@gmail.com> - 3.10.3-0.2
- Update to 3.10.3-beta2

* Thu Mar 12 2015 Nicolas Chauvet <kwizart@gmail.com> - 3.10.2-1
- Update to 3.10.2

* Wed Feb 25 2015 Nicolas Chauvet <kwizart@gmail.com> - 3.10.2-0.1
- Update to 3.10.2-rc2

* Mon Jan 19 2015 Nicolas Chauvet <kwizart@gmail.com> - 3.10.0.2-1
- Update to 3.10.0.2

* Wed Jan 07 2015 Nicolas Chauvet <kwizart@gmail.com> - 3.10.0-1
- Update to 3.10.0
- Add appdata support for fedora

* Sun Jan 04 2015 Nicolas Chauvet <kwizart@gmail.com> - 3.10.0-0.1_rc2
- Update to 3.10.0-rc2

* Wed Nov 12 2014 Nicolas Chauvet <kwizart@gmail.com> - 3.9.0.6-2
- Rebuilt with fixed wxGTK3 - rhbz#1124402

* Mon Oct 20 2014 kwizart <kwizart@gmail.com> - 3.9.0.6-1
- Update to 3.9.0.6

* Fri Oct 03 2014 kwizart <kwizart@gmail.com> - 3.9.0.5-1
- Update to 3.9.0.5

* Fri Aug 29 2014 Nicolas Chauvet <kwizart@gmail.com> - 3.9.0.3-1
- Update to 3.9.0.3

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 29 2014 Nicolas Chauvet <kwizart@gmail.com> - 3.9.0.1-1
- Update to 3.9.0.1

* Thu Jul 10 2014 Nicolas Chauvet <kwizart@gmail.com> - 3.9.0-0.1_rc2
- Update to 3.9.0 rc2
- Switch to wxGTK3 (use wx-config-3.0)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun 02 2014 Nicolas Chauvet <kwizart@gmail.com> - 3.8.1-1
- Update to 3.8.1

* Tue Apr 01 2014 Nicolas Chauvet <kwizart@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Wed Feb 12 2014 Nicolas Chauvet <kwizart@gmail.com> - 3.7.4.1-1
- Update to 3.7.4.1

* Wed Feb 12 2014 Nicolas Chauvet <kwizart@gmail.com> - 3.7.4-1
- Update to 3.7.4

* Mon Aug 12 2013 Nicolas Chauvet <kwizart@gmail.com> - 3.7.3-1
- Update to 3.7.3 - Security fixes
 CVE-2013-4206, CVE-2013-4207, CVE-2013-4208, CVE-2013-4852

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Nicolas Chauvet <kwizart@gmail.com> - 3.7.1-1
- Update to 3.7.1

* Mon May 27 2013 Nicolas Chauvet <kwizart@gmail.com> - 3.7.0.2-1
- Update to 3.7.0.2

* Mon May 13 2013 Nicolas Chauvet <kwizart@gmail.com> - 3.7.0.1-1
- Update to 3.7.0.1

* Tue Feb 12 2013 Jon Ciesla <limburgher@gmail.com> - 3.6.0.2-2
- Drop desktop vendor tag.

* Mon Dec 03 2012 Nicolas Chauvet <kwizart@gmail.com> - 3.6.0.2-1
- Update to 3.6.0.2

* Fri Nov 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 3.6.0-1_rc1
- Update to 3.6.0-rc1

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.3-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan 11 2012 Nicolas Chauvet <kwizart@gmail.com> - 3.5.3-1
- Update to 3.5.3

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 3.5.2-1.1
- Rebuild for new libpng

* Sun Nov 27 2011 Nicolas Chauvet <kwizart@gmail.com> - 3.5.2-1
- Update to 3.5.2

* Wed Aug 31 2011 Nicolas Chauvet <kwizart@gmail.com> - 3.5.1-1
- Update to 3.5.1

* Wed May 25 2011 Nicolas Chauvet <kwizart@gmail.com> - 3.5.0-1
- Update to 3.5.0 (final)

* Tue May 10 2011 Nicolas Chauvet <kwizart@gmail.com> - 3.5.0-0.1_rc1
- Update to 3.5.0-rc1

* Mon Mar 28 2011 Nicolas Chauvet <kwizart@gmail.com> - 3.4.0-1
- Update to 3.4.0 (final)

* Sat Mar 26 2011 Nicolas Chauvet <kwizart@gmail.com> - 3.4.0-0.1_rc1
- Update to 3.4.0-rc1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.5.1-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 29 2010 Nicolas Chauvet <kwizart@gmail.com> - 3.3.5.1-2
- Keep docs in the appropriate place
- Improve summary

* Sun Nov 28 2010 Nicolas Chauvet <kwizart@gmail.com> - 3.3.5.1-1
- Update to 3.3.5.1

* Thu Nov 18 2010 Nicolas Chauvet <kwizart@gmail.com> - 3.3.5-0.1
- Update to 3.3.5
- Add RPM registration for system wide settings

* Sun Aug 22 2010 Nicolas Chauvet <kwizart@gmail.com> - 3.3.4.1-1
- Update to 3.3.4.1

* Fri Aug 13 2010 Nicolas Chauvet <kwizart@gmail.com> - 3.3.4-1
- Update to 3.3.4

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 3.3.3-1.1
- rebuilt against wxGTK-2.8.11-2

* Mon Jun 21 2010 Nicolas Chauvet <kwizart@gmail.com> - 3.3.3-1
- Update to 3.3.3

* Sat Mar 27 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 3.3.2.1-1
- Update to 3.3.2.1

* Sun Feb 21 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 3.3.2-1
- Update to 3.3.2

* Sun Jan 10 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 3.3.1-1
- Update to 3.3.1

* Sun Jan  3 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 3.3.1-0.1_rc1
- Update to 3.3.1-rc1
- Add Requires xdg-utils

* Sun Nov 22 2009 Nicolas Chauvet <kwizart@fedoraproject.org> - 3.3.0.1-1
- Update to 3.3.0.1

* Wed Nov 11 2009 kwizart < kwizart at gmail.com > - 3.3.0-1
- Update to 3.3.0

* Wed Nov  4 2009 kwizart < kwizart at gmail.com > - 3.3.0-0.3_rc1
- Update to 3.3.0-rc1

* Mon Nov  2 2009 kwizart < kwizart at gmail.com > - 3.3.0-0.2_beta2
- Update to 3.3.0-beta2

* Tue Oct 27 2009 kwizart < kwizart at gmail.com > - 3.3.0-0.1_beta1
- Update to 3.3.0-beta1

* Fri Oct 16 2009 kwizart < kwizart at gmail.com > - 3.2.8.1-1
- Update to 3.2.8.1

* Wed Oct  7 2009 kwizart < kwizart at gmail.com > - 3.2.8-1
- Update to 3.2.8

* Sat Oct  3 2009 kwizart < kwizart at gmail.com > - 3.2.8-0.1-rc1
- Update to 3.2.8-rc1

* Sat Aug 29 2009 kwizart < kwizart at gmail.com > - 3.2.7.1-1
- Update to 3.2.7.1

* Thu Aug 20 2009 kwizart < kwizart at gmail.com > - 3.2.7-2
- Update to 3.2.7
- Backport Fix for ipaddress.cpp at make check

* Mon Aug  3 2009 kwizart < kwizart at gmail.com > - 3.2.7-0.1_rc1
- Update to 3.2.7-rc1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.6.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul  6 2009 kwizart < kwizart at gmail.com > - 3.2.6-1
- Update to 3.2.6.1

* Mon Jun 29 2009 kwizart < kwizart at gmail.com > - 3.2.6-1
- Update to 3.2.6 stable

* Tue Jun 23 2009 kwizart < kwizart at gmail.com > - 3.2.6-0.1_rc1
- Update to 3.2.6-rc1

* Tue Jun 16 2009 kwizart < kwizart at gmail.com > - 3.2.5-1
- Update to 3.2.5 stable

* Thu Jun 11 2009 kwizart < kwizart at gmail.com > - 3.2.5-0.1_rc1
- Update to 3.2.5-rc1

* Tue Apr 28 2009 kwizart < kwizart at gmail.com > - 3.2.4.1-1
- Update to 3.2.4.1

* Tue Apr 21 2009 kwizart < kwizart at gmail.com > - 3.2.4-1
- Update to 3.2.4

* Thu Apr  2 2009 kwizart < kwizart at gmail.com > - 3.2.3.1-1
- Update to 3.2.3.1 stable

* Mon Mar 23 2009 kwizart < kwizart at gmail.com > - 3.2.3-1
- Update to 3.2.3 stable

* Mon Mar 16 2009 kwizart < kwizart at gmail.com > - 3.2.3-0.1_rc1
- Update to 3.2.3-rc1

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 kwizart < kwizart at gmail.com > - 3.2.2.1-1
- Update to 3.2.2.1 stable

* Fri Feb 20 2009 kwizart < kwizart at gmail.com > - 3.2.2-1
- Update to 3.2.2 stable

* Tue Feb 10 2009 kwizart < kwizart at gmail.com > - 3.2.1-1
- Update to 3.2.1 stable

* Tue Feb  3 2009 kwizart < kwizart at gmail.com > - 3.2.1-0.1_rc1
- Update to 3.2.1-rc1

* Thu Jan  8 2009 kwizart < kwizart at gmail.com > - 3.2.0-1
- Update to 3.2.0 stable

* Tue Jan  6 2009 kwizart < kwizart at gmail.com > - 3.2.0-0.1_rc2
- Update to 3.2.0-rc2
- Add BR dbus-devel - Needs a fix for gnome-session
  see http://bugzilla.gnome.org/show_bug.cgi?id=559469

* Thu Dec  4 2008 kwizart < kwizart at gmail.com > - 3.1.6-1
- Update to 3.1.6

* Tue Nov 18 2008 kwizart < kwizart at gmail.com > - 3.1.5.1-1
- Update to 3.1.5.1

* Fri Oct 24 2008 kwizart < kwizart at gmail.com > - 3.1.5-1
- Update to 3.1.5

* Fri Oct 17 2008 kwizart < kwizart at gmail.com > - 3.1.4.1-1
- Update to 3.1.4.1

* Sat Oct 11 2008 kwizart < kwizart at gmail.com > - 3.1.4-0.1.rc1
- Update to 3.1.4-rc1

* Mon Sep 29 2008 kwizart < kwizart at gmail.com > - 3.1.3.1-1
- Update to 3.1.3.1

* Tue Sep 23 2008 kwizart < kwizart at gmail.com > - 3.1.3-1
- Update to 3.1.3

* Mon Sep  1 2008 kwizart < kwizart at gmail.com > - 3.1.2-1
- Update to 3.1.2

* Thu Aug 14 2008 kwizart < kwizart at gmail.com > - 3.1.1.1-1
- Update to 3.1.1.1

* Mon Aug 11 2008 kwizart < kwizart at gmail.com > - 3.1.1-1
- Update to 3.1.1

* Fri Jul 25 2008 kwizart < kwizart at gmail.com > - 3.1.0.1-1
- Update to 3.1.0.1 - Security update

* Mon Jul 14 2008 kwizart < kwizart at gmail.com > - 3.1.0-0.1.beta2
- Update to 3.1.0-beta2

* Tue Jul  8 2008 kwizart < kwizart at gmail.com > - 3.0.11.1-1
- Update to 3.0.11.1

* Mon Jun 16 2008 kwizart < kwizart at gmail.com > - 3.0.11-1
- Update to 3.0.11
- Create patch for a shared tinyxml.
- Add support for hicolor icons.

* Wed May 21 2008 kwizart < kwizart at gmail.com > - 3.0.10-1
- Update to 3.0.10

* Wed May  7 2008 kwizart < kwizart at gmail.com > - 3.0.9.3-1
- Update to 3.0.9.3

* Sat Apr 19 2008 kwizart < kwizart at gmail.com > - 3.0.9.2-1
- Update to 3.0.9.2

* Mon Apr  7 2008 kwizart < kwizart at gmail.com > - 3.0.9.1-1
- Update to 3.0.9.1

* Mon Apr  7 2008 kwizart < kwizart at gmail.com > - 3.0.9-1
- Update to 3.0.9

* Mon Mar 31 2008 kwizart < kwizart at gmail.com > - 3.0.9-0.1.rc1
- Update to 3.0.9-rc1

* Tue Mar 18 2008 kwizart < kwizart at gmail.com > - 3.0.8.1-1
- Update to 3.0.8.1
- Add patch for make check

* Fri Mar 14 2008 kwizart < kwizart at gmail.com > - 3.0.8-1
- Update to 3.0.8

* Fri Mar  7 2008 kwizart < kwizart at gmail.com > - 3.0.8-0.1.rc1
- Update to 3.0.8-rc1

* Wed Feb 20 2008 kwizart < kwizart at gmail.com > - 3.0.7.1-1
- Update to 3.0.7.1

* Thu Jan 31 2008 kwizart < kwizart at gmail.com > - 3.0.6-1
- Update to 3.0.6

* Thu Jan 17 2008 kwizart < kwizart at gmail.com > - 3.0.5.2-1
- Update to 3.0.5.2
- Drop update desktop file in post and postun

* Thu Jan 10 2008 kwizart < kwizart at gmail.com > - 3.0.4-1
- Update to 3.0.4

* Wed Nov  7 2007 kwizart < kwizart at gmail.com > - 3.0.3-1
- Update to 3.0.3

* Fri Oct 19 2007 kwizart < kwizart at gmail.com > - 3.0.2.1-1
- Update to 3.0.2.1

* Sat Sep 22 2007 kwizart < kwizart at gmail.com > - 3.0.1-1
- Update to 3.0.1

* Sun Sep  9 2007 kwizart < kwizart at gmail.com > - 3.0.0-1
- Update to 3.0.0 (final)
- Add vendor field for .desktop

* Mon Sep  3 2007 kwizart < kwizart at gmail.com > - 3.0.0-0.3.rc3
- Update to 3.0.0rc3
- Add BR gawk
- Improve description/summary
- Removed dual listed doc file

* Mon Aug 27 2007 kwizart < kwizart at gmail.com > - 3.0.0-0.2.rc2
- Update to 3.0.0-rc2
- Upstream now install their own desktop file and pixmap

* Mon Aug 13 2007 kwizart < kwizart at gmail.com > - 3.0.0-0.2.rc1
- Update to 3.0.0-rc1
- Enable make check

* Fri Jul 27 2007 kwizart < kwizart at gmail.com > - 3.0.0-0.1.beta11
- Update to beta11

* Tue Jun  5 2007 kwizart < kwizart at gmail.com > - 3.0.0-0.1.beta10
- Update to beta10

* Sat May 26 2007 kwizart < kwizart at gmail.com > - 3.0.0-0.1.beta8
- Update to beta8

* Tue Mar 13 2007 kwizart < kwizart at gmail.com > - 3.0.0-0.1.beta7
- Update to beta7

* Tue Mar 13 2007 kwizart < kwizart at gmail.com > - 3.0.0-0.1.beta6
- Initial package.
