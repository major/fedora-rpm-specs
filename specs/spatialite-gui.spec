%global pre beta1

Name:           spatialite-gui
Version:        2.1.0
Release:        0.21%{?pre:.%pre}%{?dist}
Summary:        GUI to manage Spatialite databases

License:        GPL-3.0-or-later
URL:            https://www.gaia-gis.it/fossil/spatialite_gui
Source0:        http://www.gaia-gis.it/gaia-sins/spatialite-gui-sources/spatialite_gui-%{version}%{?pre:-%pre}.tar.gz
# Link agains wx aui
#Patch1:         %{name}-1.7.0-aui_linking.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  CharLS-devel
BuildRequires:  freexl-devel
BuildRequires:  libcurl-devel
BuildRequires:  libpq-devel
BuildRequires:  libspatialite-devel
BuildRequires:  librasterlite2-devel
BuildRequires:  libxlsxwriter-devel
BuildRequires:  libwebp-devel
BuildRequires:  libxml2-devel
BuildRequires:  lz4-devel
BuildRequires:  libzstd-devel
BuildRequires:  minizip-devel
BuildRequires:  openjpeg2-devel
BuildRequires:  wxGTK-devel
BuildRequires:  sqlite-devel
BuildRequires:  geos-devel
BuildRequires:  proj-devel
BuildRequires:  virtualpg-devel

%description
GUI to manage Spatialite databases.


%prep
%autosetup -p1 -n spatialite_gui-%{version}%{?pre:-%pre}


%build
%configure
%make_build


%install
%make_install

#desktop-file-install \
#    --dir=%{buildroot}%{_datadir}/applications \
#    gnome_resource/%{name}.desktop


%files
%doc AUTHORS
%license COPYING
%{_bindir}/spatialite_gui
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-0.21.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-0.20.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Apr 08 2024 Sandro Mani <manisandro@gmail.com> - 2.1.0-0.19.beta1
- Rebuild (libxlsxwriter)

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-0.18.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Aug 15 2023 Sandro Mani <manisandro@gmail.com> - 2.1.0-0.17.beta1
- Rebuild (libspatialite)

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-0.16.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Sandro Mani <manisandro@gmail.com> - 2.1.0-0.15.beta1
- Rebuild (libxlsxwriter)

* Thu Aug 04 2022 Scott Talbert <swt@techie.net> - 2.1.0-0.14.beta1
- Rebuild with wxWidgets 3.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-0.13.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Mar 10 2022 Sandro Mani <manisandro@gmail.com> - 2.1.0-0.12.beta1
- Rebuild for proj-9.0.0

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-0.11.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 21 2021 Sandro Mani <manisandro@gmail.com> - 2.1.0-0.10.beta1
- Rebuild (geos)

* Fri Oct 15 2021 Sandro Mani <manisandro@gmail.com> - 2.1.0-0.9.beta1
- Rebuild (libxlsxwriter)

* Mon Aug 09 2021 Sandro Mani <manisandro@gmail.com> - 2.1.0-0.8.beta1
- Rebuild (libxlsxwriter)

* Fri Jul 23 2021 Sandro Mani <manisandro@gmail.com> - 2.1.0-0.7.beta1
- Rebuild (libxlsxwriter)

* Wed Mar 24 2021 Sandro Mani <manisandro@gmail.com> - 2.1.0-0.6.beta1
- Bump

* Sun Mar 07 2021 Sandro Mani <manisandro@gmail.com> - 2.1.0-0.5.beta1
- Rebuild (proj)

* Sat Feb 13 2021 Sandro Mani <manisandro@gmail.com> - 2.1.0-0.4.beta1
- Rebuild (geos)

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 2.1.0-0.3.beta1
- rebuild for libpq ABI fix rhbz#1908268

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-0.2.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 13 2020 Sandro Mani <manisandro@gmail.com> - 2.1.0-0.1.beta1
- Update to 2.1.0-beta1

* Thu Nov  5 20:23:08 CET 2020 Sandro Mani <manisandro@gmail.com> - 1.7.1-25
- Rebuild (proj)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 14 2020 Sandro Mani <manisandro@gmail.com> - 1.7.1-23
- Fix FTBFS
- Modernize spec
- Drop ExcludeArch

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Björn Esser <besser82@fedoraproject.org> - 1.7.1-20
- rebuilt (proj)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 30 2018 Volker Fröhlich <volker27@gmx.at> - 1.7.1-17
- Build with compat-wxGTK3-gtk2 instead of wxGTK3
  Regular crashes were reported and this is the author's suggestion.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 03 2017 Volker Froehlich <volker27@gmx.at> - 1.7.1-13
- Rebuild for gtk3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Volker Froehlich <volker27@gmx.at> - 1.7.1-11
- Rebuild for libproj

* Tue Dec 20 2016 Volker Froehlich <volker27@gmx.at> - 1.7.1-10
- Correct linking issues with sqlite3 and wx aui

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.7.1-7
- Rebuilt for GCC 5 C++11 ABI change

* Sat Mar 14 2015 Volker Froehlich <volker27@gmx.at> - 1.7.1-6
- Rebuild for proj 4.9.1

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 25 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.7.1-4
- rebuild (libspatialite)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul  1 2013 Volker Fröhlich <volker27@gmx.at> 1.7.1-1
- New upstream release

* Tue Jun  4 2013 Volker Fröhlich <volker27@gmx.at> 1.7.0-1
- New upstream release
- Drop geos linking patch (solved upstream)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan  6 2013 Volker Fröhlich <volker27@gmx.at> 1.6.0-1
- New upstream release
- Patch missing linking instruction

* Sun Dec  2 2012 Bruno Wolff III <bruno@wolff.to> 1.5.0-5
- Rebuild for libspatialite soname bump

* Fri Aug 10 2012 Volker Fröhlich <volker27@gmx.at> 1.5.0-4
- Exclude ppc

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jul  6 2012 Volker Fröhlich <volker27@gmx.at> 1.5.0-2
- Add forgotten BR freexl-devel

* Wed Jan 11 2012 Volker Fröhlich <volker27@gmx.at> 1.5.0-1
- Update for new release
- Update URL and source URL
- Correct license to GPLv3+
- Drop patch for wxwidget (solved)
- Use upstreams desktop file and icon
- Don't modify linker flags anymore (solved)

* Mon Jan  9 2012 Volker Fröhlich <volker27@gmx.at> 1.4.0-3
- Exclude ppc64 architecture

* Sun Jan  8 2012 Volker Fröhlich <volker27@gmx.at> 1.4.0-2
- Remove post and postun sections with useless ldconfig

* Sun Dec  4 2011 Volker Fröhlich <volker27@gmx.at> 1.4.0-1
- Initial packaging 
