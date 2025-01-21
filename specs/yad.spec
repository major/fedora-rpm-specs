Name:      yad
Version:   9.3
Release:   12%{?dist}
Summary:   Display graphical dialogs from shell scripts or command line

Group:     Applications/System
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:   GPL-3.0-or-later
URL:       http://sourceforge.net/projects/yad-dialog/
Source0:   https://github.com/v1cont/yad/releases/download/v%{version}/yad-%{version}.tar.xz

Patch1:    yad-7.3-size-request.patch

BuildRequires:  make
BuildRequires:  gtk3-devel >= 3.22.0
BuildRequires:  webkit2gtk4.1-devel
BuildRequires:  desktop-file-utils
BuildRequires:  perl(XML::Parser)
BuildRequires:  intltool >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  gettext
BuildRequires:  gtksourceview3-devel
BuildRequires:  gspell-devel

BuildRequires:  gcc


%description
Yad (yet another dialog) is a fork of zenity with many improvements, such as
custom buttons, additional dialogs, pop-up menu in notification icon and more.


%prep
%setup -q
%patch -P1 -p1


%build
%configure

make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

rm -f %{buildroot}%{_bindir}/pfd

%find_lang %{name}

# Encoding key in group "Desktop Entry" is deprecated.
# Place the menu entry for yad-icon-browser under "Utilities".
desktop-file-install --remove-key Encoding     \
    --remove-category Development              \
    --add-category    Utility                  \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/%{name}-icon-browser.desktop


%post
update-desktop-database %{_datadir}/applications &>/dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :


%postun
update-desktop-database %{_datadir}/applications &>/dev/null || :
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi


%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files -f %{name}.lang
%doc README.md AUTHORS NEWS THANKS TODO
%license COPYING
%{_bindir}/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/aclocal/%{name}.m4
%{_mandir}/*/*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 9.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 26 2024 David King <amigadave@amigadave.com> - 9.3-11
- Rebuild against gspell

* Thu Jul  25 2024 Miroslav Suchý <msuchy@redhat.com> - 9.3-10
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Aug 20 2023 Dmitry Butskoy <Dmitry@Butskoy.name> - 9.3-7
- build with webkit2gtk4.1 (#2232981)

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Apr 14 2021 Dmitry Butskoy <Dmitry@Butskoy.name> - 9.3-1
- Update to 9.3

* Sat Mar  6 2021 Dmitry Butskoy <Dmitry@Butskoy.name> - 8.0-1
- Update to 8.0

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 26 2020 Dmitry Butskoy <Dmitry@Butskoy.name> - 7.3-1
- Upgrade to 7.3
- add some upstream patches

* Sun Nov 19 2017 Oliver Haessler <oliver@redhat.com> - 0.40.0-2
- added BuildRequires: webkitgtk43-devel for Fedora <=26 and EPEL (#1455282)

* Sun Nov 19 2017 Oliver Haessler <oliver@redhat.com> - 0.40.0-1
- Update to 0.40.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.39.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.39.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 27 2017 Oliver Haessler <oliver@redhat.com> - 0.39.0-1
- Update to 0.39.0

* Sat Apr 08 2017 Oliver Haessler <oliver@redhat.com> - 0.38.2-3
- increment number, as bodhi has issues with the previous version,
so fixing it by updating the minor version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.38.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Oliver Haessler <oliver@redhat.com> - 0.38.2-1
- Update to 0.38.2

* Mon Jan 09 2017 Oliver Haessler <oliver@redhat.com> - 0.38.1-1
- Update to 0.38.1

* Sun Dec 11 2016 Oliver Haessler <oliver@redhat.com> - 0.38.0-1
- Update to 0.38.0

* Tue Aug 23 2016 Oliver Haessler <oliver@redhat.com> - 0.37.0-1
- Update to 0.37.0

* Wed May 18 2016 Oliver Haessler <oliver@redhat.com> - 0.36.3-1
- Update to 0.36.3

* Sun May 01 2016 Oliver Haessler <oliver@redhat.com> - 0.36.2-1
- Update to 0.36.2

* Fri Apr 29 2016 Oliver Haessler <oliver@redhat.com> - 0.36.1-1
- Update to 0.36.1

* Tue Mar 22 2016 Oliver Haessler <oliver@redhat.com> - 0.35.0-1
- Update to 0.35.0

* Mon Feb 29 2016 Oliver Haessler <oliver@redhat.com> - 0.34.2-1
- Update to 0.34.2

* Thu Feb 25 2016 Oliver Haessler <oliver@redhat.com> - 0.34.1-1
- Update to 0.34.1

* Mon Feb 22 2016 Oliver Haessler <oliver@redhat.com> - 0.34.0-1
- Update to 0.34.0

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.33.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Oliver Haessler <oliver@redhat.com> - 0.33.1-1
- Update to 0.33.1

* Fri Jan 08 2016 Oliver Haessler <oliver@redhat.com> - 0.33.0-1
- Update to 0.33.0

* Thu Nov 19 2015 Oliver Haessler <oliver@redhat.com> - 0.32.0-1
- Update to 0.32.0

* Thu Nov 05 2015 Oliver Haessler <oliver@redhat.com> - 0.31.3-1
- Update to 0.31.3

* Mon Oct 12 2015 Elder Marco <eldermarco@fedoraproject.org> - 0.31.2-1
- Update to 0.31.2

* Wed Sep 09 2015 Elder Marco <eldermarco@fedoraproject.org> - 0.30.0-1
- Update to 0.30.0

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 15 2015 Elder Marco <eldermarco@fedoraproject.org> - 0.28.1-1
- update to new version, 0.28.1.
- Build yad with HTML widget enabled
- Removed patch to fix-missing-buttons.patch
- Added patch to fix undefined reference to strip_new_line

* Wed Aug 27 2014 Elder Marco <eldermarco@fedoraproject.org> - 0.27.0-1
- New upstream version
- New branches: el5, el6 and epel7

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.26.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 21 2014 Elder Marco <eldermarco@fedoraproject.org> - 0.26.1-2
- Patch to fix missing buttons (BZ #1111285)

* Tue Jun 10 2014 Elder Marco <eldermarco@fedoraproject.org> - 0.26.1-1
- Update to 0.26.1
- Project moved to SourceForge due to google politics about file hosting
- New address: https://sourceforge.net/projects/yad-dialog/

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Dec 06 2013 Elder Marco <eldermarco@fedoraproject.org> - 0.25.1-1
- Update to 0.25.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Elder Marco <eldermarco@fedoraproject.org> - 0.22.1-1
- Update to 0.22.1

* Sun Jun 09 2013 Elder Marco <eldermarco@fedoraproject.org> - 0.21.0-1
- Update to 0.21.0

* Sat Apr 06 2013 Elder Marco <eldermarco@fedoraproject.org> - 0.20.3-1
- Update to 0.20.3
- Added perl(XML::Parser) as BR

* Sun Mar 24 2013 Elder Marco <eldermarco@fedoraproject.org> - 0.20.1-1
- Update to 0.20.1

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 16 2013 Elder Marco <eldermarco@fedoraproject.org> - 0.19.1-1
- Update to 0.19.1

* Wed Dec 26 2012 Elder Marco <eldermarco@fedoraproject.org> - 0.19.0-1
- Update to 0.19.0

* Sun Dec 09 2012 Elder Marco <eldermarco@fedoraproject.org> - 0.18.0-1
* Update to 0.18.0

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 09 2012 Elder Marco <eldermarco@fedoraproject.org> - 0.17.1.1-1
- Update to 0.17.1.1

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.16.3-1
- Update to new version

* Tue Nov 15 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.15.2-1
- Update to new version
- Removed condition %%if 0%%{?fedora} < 15.

* Sun Nov 06 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.15.1-1
- Update to new version

* Sun Oct 16 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.15.0-1
- Update to new version

* Thu Sep 08 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.14.2-1
- Update to new version

* Sat Aug 13 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.13.0-1
- New upstream release

* Fri Jul 08 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.12.4-2
- Menu entry for yad-icon-browser placed under "Utilities"

* Fri Jul 01 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.12.4-1
- Update to 0.12.4
- Removed patch to fix FSF address (now, it's not necessary)

* Tue Jun 28 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.12.3-3
- Added patch to fix FSF address (from upstream)

* Sun Jun 26 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.12.3-2
- Edited spec file to conform to the fedora guidelines

* Sat Jun 25 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.12.3-1
- New upstream release

* Sat May 21 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.11.0-1
- New upstream release

* Sun May 01 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.10.2-1
- New upstream release

* Tue Apr 12 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.10.1-1
- New upstream release

* Wed Mar 30 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.10.0-1
- New upstream release
- Added build option --disable-deprecated

* Sun Mar 13 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.1-1
- New upstream release
- Added desktop-file-utils as BuildRequires.
- Removed clean section and BuildRoot tag (not required any more).
- Removed Encoding key from .desktop file.

* Tue Mar 08 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.0-1
- Initial package
