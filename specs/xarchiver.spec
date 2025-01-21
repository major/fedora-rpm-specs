Name:           xarchiver
Version:        0.5.4.23
Release:        3%{?dist}
Summary:        Archive manager for Xfce

License:        GPL-2.0-or-later AND BSD-4-Clause-UC AND (LGPL-2.1-or-later OR AFL-2.0)
URL:            https://github.com/ib/xarchiver
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gtk3-devel
BuildRequires:  libxml2-devel
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  gtk-doc
BuildRequires:  desktop-file-utils

# Using Debian's list of recommendations vs suggestions:
# https://salsa.debian.org/debian/xarchiver/blob/master/debian/control
%if 0%{?rhel} && 0%{?rhel} < 8
Requires:       arj, binutils, bzip2, cpio, gzip, xdg-utils, tar, unzip, zip
%else
Recommends:     bzip2, p7zip-plugins, unzip, xdg-utils, xz
Suggests:       arj, binutils, cpio, lz4, lzop, ncompress, unar, zstd, zip
%endif

%description
Xarchiver is a lightweight GTK frontend for manipulating 7z, arj, bzip2,
gzip, iso, rar, lha, tar, zip, RPM and deb files. It allows you to create
archives and add, extract, and delete files from them. Password protected
archives in the arj, 7z, rar, and zip formats are supported.


%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%find_lang %{name}
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# remove useless docs
rm %{buildroot}%{_docdir}/%{name}/ChangeLog

%files -f %{name}.lang
%license COPYING
%doc %{_docdir}/%{name}/
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/pixmaps/%{name}/
%{_libexecdir}/thunar-archive-plugin/
%{_mandir}/man1/%{name}.1*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Mar 01 2024 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 0.5.4.23-1
- Update to 0.5.4.23 (rhbz#2267148)

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Dec 30 2023 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 0.5.4.22-1
- Update to 0.5.4.22 (rhbz#2256261)

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 18 2023 Dan Horák <dan[at]danny.cz> - 0.5.4.21-1
- Update to 0.5.4.21 (rhbz#2085266, rhbz#2163672)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 12 2021 Dan Horák <dan[at]danny.cz> - 0.5.4.17-1
- Update to 0.5.4.17 (#1963756, #1943121, #1943121)
- Switch to gtk3 (#1790918)
- Drop obsolete distro support

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 14 2019 Mike DePaulo <mikedep333@gmail.com> - 0.5.4.14-2
- Add an upstream patch to fix RHEL7 builds

* Fri Oct 11 2019 Mike DePaulo <mikedep333@gmail.com> - 0.5.4.14-1
- Update to 0.5.4.14
- New upstream - now on GitHub
- Use weak dependencies, and refresh the list of them for archiving commands.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 04 2018 Niels de Vos <devos@fedoraproject.org> - 0.5.4-9
- prevent segfault on certain drag-and-drop actions (#1635869)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 31 2015 Jaromir Capik <jcapik@redhat.com> - 0.5.4-1
- Update to 0.5.4 (#1147466)

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 0.5.2-22
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.5.2-20
- Fix FTBFS with -Werror=format-security (#1037390, #1107209)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 10 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.2-17
- Fix thunar-archive-plugin integration (#961626)
- Conditionalize vendor tag

* Thu Apr 04 2013 Jaromir Capik <jcapik@redhat.com> - 0.5.2-16
- aarch64 support (#926742)
- fixing bogus date in the changelog

* Sun Feb 10 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 0.5.2-15
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 26 2012 Jaromir Capik <jcapik@redhat.com> - 0.5.2-13
- Fix extraction failures when the Drag'n'Drop target path contains spaces (#784075)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.5.2-11
- Rebuild for new libpng

* Sun Jun 19 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.2-10
- Fix xz MIME types

* Sat Jun 11 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.2-9
- Fix xz support. A big thanks to Daniel Hokka Zakrisson (#577480)

* Thu Jun 02 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.2-8
- Fix 7zip. Encrypted archives are still not supported.

* Thu Jun 02 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.2-7
- Add xz support. Thanks to Robby Workman and Daniel Hokka Zakrisson (#577480)
- Remove mime-type multipart/x-zip (#666066)
- Fix crash in IA__gtk_tree_model_get_valist. Thanks to Bastiaan Jacques (#690012)
- Update icon-cache scriptlets

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 22 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.2-4
- Gui fixes (#491115)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Nov 25 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.2-2
- Include HTML documentation

* Tue Nov 25 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.2-1
- Update to 0.5.2

* Sun Nov 09 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1 stable release

* Sun Oct 26 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.0-0.1.rc1
- Update to 0.5.0rc1
- Fix crash when opening zipped PDF files (#467619)
- Update gtk-icon-cache scriptlets

* Sat Oct 11 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.0-0.1.beta2
- Update to 0.5.0beta2

* Sun Aug 31 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.0-0.1.beta1
- Update to 0.5.0beta1
- Remove xdg-open.patch as xarchiver now uses xdg-open by default

* Sat Apr 19 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.9-0.6.20070103svn24249
- Remove additional mime-types from desktop-file-install to make sure we don't break livecds

* Fri Mar 14 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.9-0.5.20070103svn24249
- Use xdg-open instead of htmlview (#437554)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.9-0.4.20070103svn24249
- Autorebuild for GCC 4.3

* Tue Aug 28 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.9-0.3.20070103svn24249
- Rebuild for BuildID feature
- Update license tag

* Fri Mar 02 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.9-0.2.20070103svn24249
- Downgrade to SVN release 24249 in order to fix #230154 temporarily.

* Sun Jan 28 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.9-0.1.20070128svn24772
- Update to SVN release 24772 of January 28th 2007.

* Wed Jan 03 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.9-0.1.20070103svn
- Update to SVN r24249 of January 3rd 2007.
- Add mimetype application/x-deb again since opening of debs now is secure.

* Wed Dec 13 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.9-0.1.20061213svn
- Update to SVN r24096 of December 13th 2006.

* Wed Dec 06 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.6-3
- Add deb.patch to prevent opening of .a files as debs.
- Don't add mimetype for x-ar (archiver can't handle ar archive).

* Wed Nov 29 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.6-2
- Add htmlview.patch.

* Tue Nov 28 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.6-1
- Update to 0.4.6.
- Update %%description.
- Require binutils, cpio and htmlview.
- Add mimetypes application/x-ar, application/x-cd-image and application/x-deb.

* Mon Nov 27 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.4-1
- Update to 0.4.4.

* Sat Nov 25 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.2-0.3.rc2
- Install xarchiver.png also in %%{_datadir}/icons/hicolor/48x48/apps/.

* Sat Nov 25 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.2-0.2.rc2
- Drop subpackage and own %%{_libexecdir}/thunar-archive-plugin/ (#198098).

* Sun Nov 12 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.2-0.1.rc2
- Update to 0.4.2.RC2.

* Wed Sep 13 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0.

* Tue Sep 05 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.9.2-0.beta2
- Initial package.
