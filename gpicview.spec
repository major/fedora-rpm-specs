Name:           gpicview
Version:        0.2.5
Release:        17%{?dist}
Summary:        Simple and fast Image Viewer for X

License:        GPLv2+
URL:            http://lxde.sourceforge.net/gpicview/
Source0:        http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  intltool
%if 0%{?fedora} >= 37
BuildRequires:  pkgconfig(gtk+-3.0)
%else
BuildRequires:  pkgconfig(gtk+-2.0)
%endif
BuildRequires:  libjpeg-devel
BuildRequires:  desktop-file-utils
BuildRequires:  make
Requires:       xdg-utils

%description
Gpicview is an simple and image viewer with a simple and intuitive interface.
It's extremely lightweight and fast with low memory usage. This makes it 
very suitable as default image viewer of desktop system. Although it is 
developed as the primary image viewer of LXDE, the Lightweight X11 Desktop 
Environment, it only requires GTK+ and can be used in any desktop environment.

%prep
%setup -q

%build
%configure \
%if 0%{?fedora} >= 37
	--enable-gtk3 \
%endif
	--disable-silent-rules \
	%{nil}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

desktop-file-install --delete-original      \
  --dir=${RPM_BUILD_ROOT}%{_datadir}/applications               \
  --remove-category=Application                                 \
  --remove-category=Utility                                     \
  --remove-category=Photography                                 \
   $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING AUTHORS
%{_bindir}/gpicview
%{_datadir}/applications/*gpicview.desktop
%{_datadir}/gpicview/
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Aug 27 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.5-16
- Use gtk3 on F-37+

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.5-5
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 28 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.5-1
- 0.2.5

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 15 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.4-1
- 0.2.4

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Jon Ciesla <limburgher@gmail.com> - 0.2.1-11
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 0.2.1-9
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 0.2.1-8
- rebuild against new libjpeg

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.2.1-5
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 17 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.1-3
- Add patch to fix DSO linking (#564627)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 29 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1

* Sun May 31 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Sun May 17 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.99-1
- Update to 0.1.99 (0.2.0 Beta)
- Require xdg-utils
- Fix URL of Source0
- Run update-desktop-database in %%post and %%postun

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 20 2008 Marc Wiriadisastra <marc@mwiriadi.id.au> - 0.1.11-1
- New upstream release

* Tue Dec 2 2008 Marc Wiriadisastra <marc@mwiriadi.id.au> - 0.1.10-2
- Rebuild of gpicview after updates from Patrice. Thanks and credit
 go to Patrice.

* Sun Sep 14 2008 Marc Wiriadisastra <marc@mwiriadi.id.au> - 0.1.10-1
- New upstream release

* Sat Feb 23 2008 Marc Wiriadisastra <marc@mwiriadi.id.au> - 0.1.9-1
- New upstream release

* Sat Feb 2 2008 Marc Wiriadisastra <marc@mwiriadi.id.au> - 0.1.8-1
- New upstream release

* Fri Jan 11 2008 parag <paragn@fedoraproject.org> - 0.1.7-3
- Spec cleanup

* Thu Jan 10 2008 Marc Wiriadisastra <marc@mwiriadi.id.au> - 0.1.7-2
- Removed zero size files
- added lang in spec file

* Thu Jan 10 2008 Marc Wiriadisastra <marc@mwiriadi.id.au> - 0.1.7-1
- Initial release
