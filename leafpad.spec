%if (%{?fedora} && %{?fedora}) < 19
%global with_desktop_vendor_tag 1
%endif

Name:           leafpad
Version:        0.8.18.1
Release:        30%{?dist}

Summary:        GTK+ based simple text editor

License:        GPLv2+
URL:            http://tarot.freeshell.org/leafpad/
Source0:        http://savannah.nongnu.org/download/leafpad/%{name}-%{version}.tar.gz
Patch0:         01-gcc-format.patch

BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel >= 2.4
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires: make

%description
Leafpad is a GTK+ based simple text editor. The user interface is similar to
Notepad. It aims to be lighter than GEdit and KWrite, and to be as useful as
them.


%prep
%setup -q
sed -i 's/g_strcasecmp/g_ascii_strcasecmp/g' src/main.c
sed -i 's/g_strcasecmp/g_ascii_strcasecmp/g' src/dnd.c
sed -i 's/g_strcasecmp/g_ascii_strcasecmp/g' src/selector.c
%patch0

%build
%configure --enable-chooser

%make_build


%install
%make_install

desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
%if (0%{?fedora} && 0%{?fedora} < 19) || (0%{?rhel} && 0%{?rhel} < 7)
  --vendor fedora \
%endif
  %{buildroot}%{_datadir}/applications/leafpad.desktop

%find_lang %{name}


%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/pixmaps/leafpad.*

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.18.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.18.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.18.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.18.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.18.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.18.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.18.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.18.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.18.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 28 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.18.1-21
- Add BR:gcc-c++

* Mon May 28 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.18.1-20
- Add gcc patch to fix FTBFS
- Modernize spec

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.18.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.18.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.18.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.18.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.18.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.18.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 0.8.18.1-13
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.18.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.18.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 14 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.18.1-9
- Fix desktop vendor conditionals
- Spec file clean-up

* Wed Apr 24 2013 Jon Ciesla <limburgher@gmail.com> - 0.8.18.1-8
- Added conditionals.

* Wed Apr 24 2013 Jon Ciesla <limburgher@gmail.com> - 0.8.18.1-7
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.18.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.18.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.18.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.8.18.1-3
- Rebuild for new libpng

* Fri Jun 03 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.18.1-2
- Add docs (AUTHORS ChangeLog COPYING README)
- Really drop unnecessary BuildRequires for libgnomeprintui22-devel this time
- Drop Requires(post,pustun) for desktop-file-utils

* Fri May 20 2011 Orion Poplawski <orion@cora.nwra.com> - 0.8.18.1-1
- Update to 0.8.18.1
- Add BR intltool

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 01 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.17-1
- Update to 0.8.17
- Drop unnecessary BuildRequires for libgnomeprintui22-devel
- Update icon-cache scriptlets

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 10 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 0.8.13-1
- Upstream update

* Tue Aug 21 2007 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 0.8.11-2
- Fix License tag
- Rebuild for F8t2

* Fri Jul 20 2007 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 0.8.11-1
- Upstream update

* Fri May 11 2007 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 0.8.10le-1
- Upstream update

* Wed Sep 06 2006 Michael J. Knox <michael[AT]knox.net.nz> - 0.8.9-3
- Rebuild for FC6
- added BR of gettext

* Mon Apr 17 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.8.9-1
- Upstream update

* Mon Feb 13 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.8.7-2
- Rebuild for Fedora Extras 5

* Fri Feb  3 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.8.7-1
- Upstream update

* Sat Nov 26 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.8.5-1
- Upstream update

* Sat Oct  1 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.8.4-1
- Upstream update

* Thu Aug 18 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.8.3-2
- Rebuild for new Cairo

* Sat Jul 23 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.8.3-1
- Upstream update

* Thu May 19 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.8.1-1
- Upstream update

* Fri Apr 29 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.8.0-1
- Upstream update

* Fri Apr 22 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.7.9-7
- Used %%find_lang
- Cleaned up desktop entry generation a bit

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sat Mar 19 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.7.9-5
- %%

* Sat Mar 19 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.7.9-4
- Added desktop-file-utils to BuildRequires

* Wed Mar 16 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.7.9-3
- Broke %%description at 80 columns

* Wed Mar 16 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.7.9-2
- Removed explicit Requires

* Tue Mar 15 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.7.9-1
- Bump release to 1

* Thu Feb  3 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0:0.7.9-0.iva.0
- Initial RPM release.
