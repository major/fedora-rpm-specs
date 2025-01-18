Name:           feh
Version:        3.10.3
Release:        2%{?dist}
Summary:        Fast command line image viewer using Imlib2
License:        MIT
URL:            https://feh.finalrewind.org
Source0:        https://feh.finalrewind.org/%{name}-%{version}.tar.bz2
Patch0:         feh-1.10.1-dejavu.patch

BuildRequires:  gcc
BuildRequires:  imlib2-devel
BuildRequires:  libcurl-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libXt-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libexif-devel
BuildRequires:  make
BuildRequires:  perl-Test-Command
BuildRequires:  perl-Test-Harness
Requires:       dejavu-sans-fonts
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%description
feh is a versatile and fast image viewer using imlib2, the
premier image file handling library. feh has many features,
from simple single file viewing, to multiple file modes using
a slide-show or multiple windows. feh supports the creation of
montages as index prints with many user-configurable options.

%prep
%autosetup -p1 -n feh-%{version}

%build
# Propagate values into config.mk
sed -i \
  -e "s|^doc_dir =.*$|doc_dir = \$(DESTDIR)%{_pkgdocdir}|" \
  -e "s|^example_dir =.*$|example_dir = \$(doc_dir)/examples|" \
  -e "s|^CFLAGS ?=.*$|CFLAGS = ${RPM_OPT_FLAGS}|" \
  config.mk
%make_build PREFIX="%{_prefix}" VERSION="%{version}" \
    curl=1 exif=1 test=1 xinerama=1


%install
%make_install PREFIX=%{_prefix}
rm %{buildroot}%{_datadir}/%{name}/fonts/yudit.ttf
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
rm %{buildroot}%{_docdir}/%{name}/examples/find-lowres

%check
make test

%files
%license COPYING
%doc %{_docdir}/%{name}
%{_bindir}/*
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/*
%{_datarootdir}/icons/hicolor/48x48/apps/feh.png
%{_datarootdir}/icons/hicolor/scalable/apps/feh.svg

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Filipe Rosset <rosset.filipe@gmail.com> - 3.10.3-1
- Update to 3.10.3 fixes rhbz#2295468

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Ben Boeckel <fedora@me.benboeckel.net> - 3.10.2-1
- update to 3.10.2

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Leigh Scott <leigh123linux@gmail.com> - 3.10-1
- Update to 3.10
- Rebuild fo new imlib2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 24 2022 Filipe Rosset <rosset.filipe@gmail.com> - 3.9.1-1
- Update to 3.9.1 fixes rhbz#2096066

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 15 2022 Fabio Alessandro Locati <fale@fedoraproject.org> - 3.8-1
- Update to 3.8

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Ben Boeckel <fedora@me.benboeckel.net> - 3.6.3-1
- update to 3.6.3

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 01 2020 Ben Boeckel <mathstuf@gmail.com> - 3.4.1-1
- Update to 3.4.1

* Mon Apr 13 2020 Ben Boeckel <mathstuf@gmail.com> - 3.4-1
- Update to 3.4

* Wed Apr 01 2020 Aleksei Bavshin <alebastr89@gmail.com> - 3.3-1
- Update to 3.3 (#1779292)
- Set PREFIX and VERSION during the compilation (#1798743)
- Adjust font patch for f32 dejavu-sans-fonts packaging changes
- Disable debug build; it was overriding optimization flags with -O0
- Remove upstreamed patch

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 29 2019 Ben Boeckel <mathstuf@gmail.com> - 3.2.1-1
- Update to 3.2.1
- Switch to Github for source tarballs

* Tue Oct 29 2019 Ben Boeckel <mathstuf@gmail.com> - 3.1.3-3
- Add patch to fix rhbz#1440503 (crash when editing with large images)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 04 2019 Filipe Rosset <rosset.filipe@gmail.com> - 3.1.3-1
- update to 3.1.3 fixes rhbz #1674926

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 22 2018 Filipe Rosset <rosset.filipe@gmail.com> - 3.1-1
- update to 3.1

* Thu Nov 22 2018 Filipe Rosset <rosset.filipe@gmail.com> - 2.28.1-1
- update to 2.28.1

* Sat Oct 27 2018 Filipe Rosset <rosset.filipe@gmail.com> - 2.28-1
- update to 2.28 fixes rhbz #1438979 #1444077 and #1602421

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 24 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 2.19.3-1
- Update to 2.19.3
- Fix rpmlint complains

* Sun Aug 13 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 2.19.2-1
- Update to 2.19.2

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 05 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 2.18.2-1
- Update to 2.18.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 2.18.1-1
- Update to 2.18.1

* Sun Jan 01 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 2.18-2
- Enable EXIF

* Sun Dec 11 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 2.18-1
- Update to 2.18

* Thu Sep 01 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 2.17.1-1
- Update to 2.17.1

* Mon Aug 29 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 2.17.0-1
- Update to 2.17.0

* Tue Aug 02 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 2.16.2-1
- Update to 2.16.2

* Sat Jul 23 2016 Ben Boeckel <mathstuf@gmail.com> - 2.16.1-1
- update to 2.16.1

* Sat Apr 23 2016 Ben Boeckel <mathstuf@gmail.com> - 2.15.2-1
- update to 2.15.2

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 13 2015 Ben Boeckel <mathstuf@gmail.com> - 2.14-1
- update to 2.14

* Sat Oct 10 2015 Ben Boeckel <mathstuf@gmail.com> - 2.13.1-2
- use license tag
- package examples
- remove defattr line

* Sun Jul 19 2015 Ben Boeckel <mathstuf@gmail.com> - 2.13.1-1
- Update to 2.13.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Dec 10 2014 Ben Boeckel <mathstuf@gmail.com> - 2.12-1
- Update to 2.12

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 20 2013 Ben Boeckel <mathstuf@gmail.com> - 2.9.3-1
- Update to 2.9.3
- Update URL

* Tue Aug 13 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.7-5
- Reflect docdir changes (FTBFS RHBZ#992244).
- Let package acknowledge RPM_OPT_FLAGS.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.7-3
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov 04 2012 Ben Boeckel <mathstuf@gmail.com> - 2.7-1
- Update to 2.7

* Sun Nov 04 2012 Ben Boeckel <mathstuf@gmail.com> - 2.3-3
- Pass PREFIX to the build step

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Feb 18 2012 Ben Boeckel <mathstuf@gmail.com> - 2.3-1
- Update to 2.3

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 22 2011 Ben Boeckel <mathstuf@gmail.com> - 2.1-1
- Update to 2.1

* Mon Jul 25 2011 Ben Boeckel <mathstuf@gmail.com> - 1.14.2-1
- Update to 1.14.2

* Fri Jun 24 2011 Ben Boeckel <mathstuf@gmail.com> - 1.14.1-1
- Update to 1.14.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 29 2010 Andrew Potter <agpotter@gmail.com> 1.10.1-1
- New upstream release
- Closes CVE-2010-2246 by removing option -G, --wget-timestamp

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 1.3.4-11
- Fix font Requires

* Mon Dec 22 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 1.3.4-10
- Fix thinko in DejaVu package name

* Sun Dec 21 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 1.3.4-9
- Switch from included font to DejaVu Sans

* Thu Apr 10 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.3.4-8
- Remove non free menubg_britney.png from sources
- Apply various fixes from svn
- Some makeup fixes to the manpage (courtesy of debian)
- Fix escaping of filenames in "feh --bg-scale" (bz 441527)

* Thu Apr  3 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.3.4-7
- Fix missing prototype compiler warnings

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.3.4-6
- Autorebuild for GCC 4.3

* Mon Aug  6 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.3.4-5
- Update License tag for new Licensing Guidelines compliance

* Thu Aug 31 2006 Aaron Kurtz <a.kurtz@hardsun.net> - 1.3.4-4
- Rebuild for Fedora Extras 6

* Mon Feb 13 2006 Aaron Kurtz <a.kurtz@hardsun.net> - 1.3.4-3
- Rebuild for Fedora Extras 5

* Tue Jan 31 2006 Aaron Kurtz <a.kurtz@hardsun.net> - 1.3.4-2
- change to new modular X devel BuildReqs

* Wed Aug 31 2005 Aaron Kurtz <a.kurtz@hardsun.net> - 1.3.4-1
- bump to 1.3.4

* Thu Jun 16 2005 Aaron Kurtz <a.kurtz@hardsun.net> - 1.3.1-3
- do it right this time

* Wed Jun 01 2005 Aaron Kurtz <a.kurtz@hardsun.net> - 1.3.1-2
- proper dist tag

* Tue May 03 2005 Aaron Kurtz <a.kurtz@hardsun.net> - 1.3.1-1
- Bump to 1.3.1

* Mon Apr 25 2005 Aaron Kurtz <a.kurtz@hardsun.net> - 1.3.0-3
- Spec file cleanup, dist tag

* Wed Mar 30 2005 Aaron Kurtz <a.kurtz@hardsun.net> - 1.3.0-2
- Spec file cleanup, plus would upgrade linuxbrit rpm

* Fri Mar 25 2005 Aaron Kurtz <a.kurtz@hardsun.net> - 1.3.0-1
- Initial Fedora RPM release
