Name:           gummi
Version:        0.8.3
Release:        2%{?dist}
Summary:        A simple LaTeX editor

License:        MIT
URL:            https://github.com/alexandervdm/gummi
Source0:        https://github.com/alexandervdm/gummi/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gtk3-devel
BuildRequires:  gtksourceview3-devel
BuildRequires:  poppler-glib-devel
BuildRequires:  gtkspell3-devel
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  texlive-lib-devel
BuildRequires:  tex-synctex

Requires:       texlive-latex

%description
Gummi is a LaTeX editor written in the C programming language using the
GTK+ interface toolkit. It was designed with simplicity and the novice
user in mind, but also offers features that speak to the more advanced user.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install
%find_lang %{name}
desktop-file-install                                 \
    --remove-key="Version"                           \
    --add-category="Publishing;"                     \
    --dir=%{buildroot}%{_datadir}/applications       \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%doc AUTHORS ChangeLog
%license COPYING
%{_mandir}/man*/*.1*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/
%{_libdir}/%{name}/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 25 2024 Sérgio Basto <sergio@serjux.com> - 0.8.3-1
- Bump the version to 0.8.3 (Fabio Ribeiro PR)
- Move build to gtk3, gtksourceview3 and gtkspell3

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 0.6.6-10
- Rebuild for poppler-0.84.0

* Mon Sep 02 2019 Fabian Affolter <fabian-affolter.ch> - 0.6.6-9
- Update URL
- Fix bogus date 

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 14 2016 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.6-1
- Fix CVE-2015-7758 (rhbz#1270816, rhbz#1270816)
- Update to latest upstream release 0.6.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 21 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.5-5
- Update description

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 26 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.5-3
- Spec file updated

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 15 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.5-1
- Updated to new upstream version 0.6.5

* Fri Aug 10 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.4-1
- Updated to new upstream version 0.6.4

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 16 2012 Marek Kasik <mkasik@redhat.com> - 0.6.3-2
- Rebuild (poppler-0.20.0)

* Sat Apr 07 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.3-1
- Updated to new upstream version 0.6.3

* Fri Mar 23 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.2-1
- Patch removed
- Updated to new upstream version 0.6.2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 08 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.1-1
- Updated to new upstream version 0.6.1

* Mon Nov 28 2011 Marek Kasik <mkasik@redhat.com> - 0.6.0-2
- Add output of "pkg-config --libs gthread-2.0" to Makefile.in to fix build

* Thu Nov 17 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.0-1
- Updated to new upstream version 0.6.0

* Fri Oct 28 2011 Rex Dieter <rdieter@fedoraproject.org> - 0.5.8-6
- rebuild(poppler)

* Fri Sep 30 2011 Marek Kasik <mkasik@redhat.com> - 0.5.8-5
- Rebuild (poppler-0.18.0)

* Mon Sep 19 2011 Marek Kasik <mkasik@redhat.com> - 0.5.8-4
- Rebuild (poppler-0.17.3)

* Fri Aug 12 2011 Fabian Affolter <fabian@bernewireless.net> - 0.5.8-3
- Rebuild (libgtksourceview)

* Fri Jul 15 2011 Marek Kasik <mkasik@redhat.com> - 0.5.8-2
- Rebuild (poppler-0.17.0)

* Wed Mar 23 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.8-1
- Updated to new upstream version 0.5.8

* Sun Mar 13 2011 Marek Kasik <mkasik@redhat.com> - 0.5.5-4
- Rebuild (poppler-0.16.3)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 02 2011 Rex Dieter <rdieter@fedoraproject.org> - 0.5.5-2
- rebuild (poppler)

* Mon Dec 27 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.5-1
- Updated to new upstream version 0.5.5

* Fri Nov 12 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.3-2
- Texlive added

* Mon Nov 01 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.3-1
- BRs adjusted
- Updated to new upstream version 0.5.3

* Sat Oct 23 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.2-1
- Updated to new upstream version 0.5.2

* Sun Oct 10 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.1-1
- Updated to new upstream version 0.5.1

* Sat Sep 25 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.0-1
- New BRs added
- It's no longer a python package, no longer noarch
- Updated to new upstream version 0.5.0

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jun 02 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.8-1
- Updated to new upstream version 0.4.8

* Fri Mar 05 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.5-1
- Added man page
- Updated to new upstream version 0.4.5

* Mon Dec 07 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.2-2
- Changed requirements and BR
- Added license file to doc
- Changed group

* Mon Nov 02 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.2-1
- Remove shebangs 
- Updated to new upstream version 0.4.2

* Mon Oct 12 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.3-1.b
- Initial spec for Fedora
