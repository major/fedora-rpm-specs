Name:           gnome-epub-thumbnailer
Version:        1.8
Release:        2%{?dist}
Summary:        Thumbnailers for EPub and MOBI books

License:        GPL-2.0-or-later
URL:            https://git.gnome.org/browse/gnome-epub-thumbnailer
Source0:        http://download.gnome.org/sources/%{name}/1.8/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
Buildrequires:  pkgconfig(libarchive)
BuildRequires:  meson

%description
Thumbnailers for EPub and MOBI books


%prep
%setup -q
%autopatch

%build
%meson
%meson_build

%install
%meson_install


%files
%{_bindir}/gnome-epub-thumbnailer
%{_bindir}/gnome-mobi-thumbnailer
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/gnome-epub-thumbnailer.thumbnailer
%{_datadir}/thumbnailers/gnome-mobi-thumbnailer.thumbnailer
%doc COPYING NEWS README



%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Aug  3 2024 Yanko Kaneti <yaneti@declera.com> - 1.8-1
- Update to 1.8

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep 29 2022 Bastien Nocera <bnocera@redhat.com> - 1.7-1
- Update to 1.7

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 30 2019 Yanko Kaneti <yaneti@declera.com> - 1.6-1
- Update to 1.6
- Adds support for SVG covers in ePub 3.0 files
- Adds support for Kindle Format 8 MOBI files

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 19 2015 Yanko Kaneti <yaneti@declera.com> - 1.5-1
- Update to 1.5. Drop patches

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug  5 2014 Yanko Kaneti <yaneti@declera.com> - 1.4-3
- Pick couple uptream fixes. Should help avoid RHBZ 1103325

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 23 2014 Yanko Kaneti <yaneti@declera.com> - 1.4-1
- Update to 1.4. Drop upstream patches.

* Thu Jan 16 2014 Yanko Kaneti <yaneti@declera.com> - 1.3-4
- Yet another crash fix from upstream

* Mon Jan  6 2014 Yanko Kaneti <yaneti@declera.com> - 1.3-3
- Fix crashes on thumbnailing trash/recent files - #1046245
- Get unencrypted cover from otherwise encrypted mobi files

* Sun Oct 27 2013 Yanko Kaneti <yaneti@declera.com> - 1.3-2
- Don't crash on failure to find a cover file - #1001559

* Thu Aug  8 2013 Yanko Kaneti <yaneti@declera.com> - 1.3-1
- New upstream release fixing a number of possible crashers
  in the MOBI thumbnailer

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Yanko Kaneti <yaneti@declera.com> - 1.2-1
- New upstream release adding a MOBI thumbnailer

* Wed Jul 17 2013 Yanko Kaneti <yaneti@declera.com> - 1.1-1
- New upstream release fixing possible crashes or
  excessive warnings on failure

* Tue Jul 16 2013 Yanko Kaneti <yaneti@declera.com> - 1.0-1
- Initial packaging
