Name: clamtk
Version: 6.18
Release: 3%{dist}
Summary: Easy to use graphical user interface for Clam anti virus
License: GPL-1.0-or-later AND Artistic-2.0
URL: https://github.com/dave-theunsub/clamtk

Source0: https://github.com/dave-theunsub/clamtk/releases/download/v%{version}/clamtk-%{version}.tar.xz
BuildArch: noarch

BuildRequires: desktop-file-utils
BuildRequires: perl-generators
Requires: perl(LWP::UserAgent), perl(LWP::Protocol::https)
Requires: perl(Text::CSV), perl(Time::Piece), perl(Locale::gettext), perl(JSON)
Requires: clamav >= 0.95, clamav-update, data(clamav)
Requires: gnome-icon-theme-legacy, cronie

%description
ClamTk is a front end for ClamAV anti virus.
It is meant to be lightweight and easy to use.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}/
install -p -D -m0755 clamtk %{buildroot}/%{_bindir}/clamtk
install -p -D -m0644 images/clamtk.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png

# For appdata.xml
install -p -D -m0644 images/%{name}.png %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

install -p -D -m0644 clamtk.1.gz %{buildroot}/%{_mandir}/man1/%{name}.1.gz
install -p -D -m0644 clamtk.desktop %{buildroot}/%{_datadir}/applications/%{name}.desktop
install -p -d %{buildroot}/%{perl_vendorlib}/ClamTk
install -p -m0644 lib/*.pm %{buildroot}/%{perl_vendorlib}/ClamTk/

install -p -D -m0644 com.github.davetheunsub.clamtk.appdata.xml %{buildroot}/%{_datadir}/metainfo/com.github.davetheunsub.clamtk.appdata.xml

# Install locale files
for n in po/*.mo ; do
    install -p -D -m0644 $n %{buildroot}/%{_datadir}/locale/`basename $n .mo`/LC_MESSAGES/clamtk.mo
done

    desktop-file-install --delete-original  \
	--add-category="GTK"                    \
    --add-category="GNOME"                  \
	--add-category="Utility"                \
    --dir %{buildroot}/%{_datadir}/applications %{buildroot}/%{_datadir}/applications/*

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc CHANGES DISCLAIMER.md LICENSE README.md credits.md

# The main executable
%{_bindir}/%{name}

# Main Perl libraries
%{perl_vendorlib}/ClamTk

# Images
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

# Desktop file
%{_datadir}/applications/%{name}.desktop

# Man pages
%{_mandir}/man1/%{name}.1*

# Appdata
%{_datadir}/metainfo/com.github.davetheunsub.clamtk.appdata.xml

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Dave M. <dave.nerd@gmail.com> - 6.18-1
- Updated to release 6.18.

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Dec 19 2023 Dave M. <dave.nerd@gmail.com> - 6.17-1
- Updated to release 6.17.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 2 2023 Dave M. <dave.nerd@gmail.com> - 6.16-1
- Updated to release 6.16.

* Sat Apr 22 2023 Dave M. <dave.nerd@gmail.com> - 6.15-1
- Updated to release 6.15.

* Wed Mar 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 6.14-6
- migrate to SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 6.14-3
- Perl 5.36 rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 20 2021 Dave M. <dave.nerd@gmail.com> - 6.14-1
- Updated to release 6.14.

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 7 2021 Dave M. <dave.nerd@gmail.com> - 6.13-1
- Updated to release 6.13.

* Mon Jul 5 2021 Dave M. <dave.nerd@gmail.com> - 6.12-1
- Updated to release 6.12.

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 6.11-2
- Perl 5.34 rebuild

* Fri Apr 9 2021 Dave M. <dave.nerd@gmail.com> - 6.11-1
- Updated to release 6.11.

* Sat Mar 13 2021 Dave M. <dave.nerd@gmail.com> - 6.10-1
- Updated to release 6.10.
- Add appdata.xml.

* Sat Feb 27 2021 Dave M. <dave.nerd@gmail.com> - 6.09-1
- Update URLs in specs.
- Updated to release 6.09.

* Thu Feb 18 2021 Dave M. <dave.nerd@gmail.com> - 6.08-1
- Updated to release 6.08.

* Fri Feb 5 2021 Dave M. <dave.nerd@gmail.com> - 6.07-1
- Updated to release 6.07.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 16 2020 Dave M. <dave.nerd@gmail.com> - 6.06-1
- Updated to release 6.06.

* Sun Aug 9 2020 Dave M. <dave.nerd@gmail.com> - 6.05-1
- Updated to release 6.05.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Dave M. <dave.nerd@gmail.com> - 6.04-1
- Updated to release 6.04.

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 6.03-3
- Perl 5.32 re-rebuild of bootstrapped packages

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 6.03-2
- Perl 5.32 rebuild

* Thu Apr 23 2020 Dave M. <dave.nerd@gmail.com> - 6.03-1
- Updated to release 6.03.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 28 2019 Dave M. <dave.nerd@gmail.com> - 6.02-1
- Updated to release 6.02.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 6.01-2
- Perl 5.30 rebuild

* Sat Apr 6 2019 Dave M. <dave.nerd@gmail.com> - 6.01-1
- Updated to release 6.01.
- Minor dependency changes.

* Sat Feb 23 2019 Dave M. <dave.nerd@gmail.com> - 6.00-1
- Updated to release 6.00.
- Update sources URL to clamtk-gtk3 link.
- Updated to use Gtk3.

* Sat Feb 9 2019 Dave M. <dave.nerd@gmail.com> - 5.27-1
- Updated to release 5.27.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep 15 2018 Dave M. <dave.nerd@gmail.com> - 5.26-1
- Updated to release 5.26.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 5.25-4
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 9 2017 Dave M. <dave.nerd@gmail.com> - 5.25-2
- Remove .fc

* Sat Sep 9 2017 Dave M. <dave.nerd@gmail.com> - 5.25-1
- Updated to release 5.25.
- Switched source from gz to xz.
- Updated bitbucket links.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 5.24-5
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 19 2016 Dave M. <dave.nerd@gmail.com> - 5.24-3
- Updated to release 5.24.
- Remove help docs.
- Update other documentation names, add new credits.md

* Sat Oct 29 2016 Dave M. <dave.nerd@gmail.com> - 5.23-1
- Updated to release 5.23.

* Sun Sep 18 2016 Dave M. <dave.nerd@gmail.com> - 5.22-1
- Updated to release 5.22.

* Sun Aug 21 2016 Dave M. <dave.nerd@gmail.com> - 5.21-1
- Updated to release 5.21.

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 5.20-3
- Perl 5.24 rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 Dave M. <dave.nerd@gmail.com> - 5.20-1
- Updated to release 5.20.
- Remove nautilus dependency.

* Sun Jun 28 2015 Dave M. <dave.nerd@gmail.com> - 5.19-1
- Updated to release 5.19.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 5.18-2
- Perl 5.22 rebuild

* Sun May 10 2015 Dave M. <dave.nerd@gmail.com> - 5.18-1
- Updated to release 5.18.

* Sun Apr 12 2015 Dave M. <dave.nerd@gmail.com> - 5.17-1
- Updated to release 5.17.

* Sat Apr 11 2015 Dave M. <dave.nerd@gmail.com> - 5.16-1
- Updated to release 5.16.

* Fri Mar 06 2015 Dave M. <dave.nerd@gmail.com> - 5.15-1
- Updated to release 5.15.

* Sat Feb 14 2015 Dave M. <dave.nerd@gmail.com> - 5.14-1
- Updated to release 5.14.

* Sun Jan 04 2015 Dave M. <dave.nerd@gmail.com> - 5.13-1
- Updated to release 5.13.

* Thu Dec 25 2014 Dave M. <dave.nerd@gmail.com> - 5.12-1
- Updated to release 5.12.

* Sat Nov 01 2014 Dave M. <dave.nerd@gmail.com> - 5.11-1
- Updated to release 5.11.

* Fri Oct 03 2014 Dave M. <dave.nerd@gmail.com> - 5.10-1
- Updated to release 5.10.

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 5.09-2
- Perl 5.20 rebuild

* Fri Aug 29 2014 Dave M. <dave.nerd@gmail.com> - 5.09-1
- Updated to release 5.09.

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 5.08-2
- Perl 5.20 rebuild

* Sun Aug 24 2014 Dave M. <dave.nerd@gmail.com> - 5.08-1
- Updated to release 5.08.

* Fri Jun 13 2014 Dave M. <dave.nerd@gmail.com> - 5.07-1
- Updated to release 5.07.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 3 2014 Dave M. <dave.nerd@gmail.com> - 5.06-1
- Updated to release 5.06.
- Remove zenity from dependencies.

* Sat Mar 15 2014 Dave M. <dave.nerd@gmail.com> - 5.05-1
- Updated to release 5.05.

* Sat Feb 15 2014 Dave M. <dave.nerd@gmail.com> - 5.04-1
- Updated to release 5.04.

* Sun Jan 19 2014 Dave M. <dave.nerd@gmail.com> - 5.03-1
- Updated to release 5.03.
- Added gnome-icon-theme-legacy, cronie as dependencies.

* Sun Dec 29 2013 Dave M. <dave.nerd@gmail.com> - 5.02-1
- Updated to release 5.02.

* Sat Nov 23 2013 Dave M. <dave.nerd@gmail.com> - 5.01-1
- Updated to release 5.01.
- Minor spec cleanup.

* Sun Nov 10 2013 Dave M. <dave.nerd@gmail.com> - 5.00-1
- Updated to release 5.00.
- Added help files.
- Added nautilus-python and perl-LWP-Protocol-https to dependencies.
- Removed cronie dependency.
- Updated Url and Source.
- Updated License field to Artistic 2.0.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.45-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 4.45-3
- Perl 5.18 rebuild

* Tue Jul 16 2013 Jon Ciesla <limburgher@gmail.com> - 4.45-2
- Fix Source0 URL, BZ 984816.

* Sat May 25 2013 Dave M. <dave.nerd@gmail.com> - 4.45-1
- Updated to release 4.45.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 23 2012 Dave M. <dave.nerd@gmail.com> - 4.44-1
- Updated to release 4.44.

* Tue Dec 4 2012 Dave M. <dave.nerd@gmail.com> - 4.43-1
- Updated to release 4.43.

* Wed Sep 12 2012 Dave M. <dave.nerd@gmail.com> - 4.42-1
- Updated to release 4.42.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.41-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 4.41-3
- Perl 5.16 rebuild

* Tue Jun 05 2012 Jon Ciesla <limburgher@gmail.com> - 4.41-2
- Drop udev Requires.

* Sat Jun 2 2012 Dave M. <dave.nerd@gmail.com> - 4.41-1
- Updated to release 4.41.

* Sat May 26 2012 Dave M. <dave.nerd@gmail.com> - 4.40-1
- Updated to release 4.40.
- Images are grouped under images/ now.

* Sat Apr 21 2012 Dave M. <dave.nerd@gmail.com> - 4.39-1
- Updated to release 4.39.

* Sun Mar 25 2012 Dave M. <dave.nerd@gmail.com> - 4.38-1
- Updated to release 4.38.

* Sat Feb 4 2012 Dave M. <dave.nerd@gmail.com> - 4.37-1
- Updated to release 4.37.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Oct 15 2011 Dave M. <dave.nerd@gmail.com> - 4.36-1
- Updated to release 4.36.

* Sat Sep 10 2011 Dave M. <dave.nerd@gmail.com> - 4.35-1
- Updated to release 4.35.

* Sat Aug 13 2011 Dave M. <dave.nerd@gmail.com> - 4.34-1
- Updated to release 4.34.
- desktop-file-install categories updated.

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 4.33-2
- Perl mass rebuild

* Sat Jun 11 2011 Dave M. <dave.nerd@gmail.com> - 4.33-1
- Updated to release 4.33.

* Fri Jun 10 2011 Marcela Mašláňová <mmaslano@redhat.com> - 4.32-2
- Perl 5.14 mass rebuild

* Mon Apr 25 2011 Dave M. <dave.nerd@gmail.com> - 4.32-1
- Updated to release 4.32.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 8 2011 Dave M. <dave.nerd@gmail.com> - 4.31-1
- Updated to release 4.31.
- Dependency clamav-data changed to data(clamav).

* Sun Nov 7 2010 Dave M. <dave.nerd@gmail.com> - 4.30-1
- Updated to release 4.30.

* Sat Sep 11 2010 Dave M. <dave.nerd@gmail.com> - 4.29-1
- Updated to release 4.29.
- ClamAV dependency is bumped to >= 0.95.

* Tue Aug 17 2010 Dave M. <dave.nerd@gmail.com> - 4.28-1
- Updated to release 4.28.
- Removed dependency for hal (deprecated).
- Added dependency for udev.

* Sat Jul 10 2010 Dave M. <dave.nerd@gmail.com> - 4.27-1
- Updated to release 4.27.
- Added dependency for hal.

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 4.26-2
- Mass rebuild with perl-5.12.0

* Sat May 1 2010 Dave M. <dave.nerd@gmail.com> - 4.26-1
- Updated to release 4.26.

* Sun Mar 7 2010 Dave M. <dave.nerd@gmail.com> - 4.25-1
- Updated to release 4.25.

* Sun Feb 28 2010 Dave M. <dave.nerd@gmail.com> - 4.24-1
- Updated to release 4.24.
- Spelling of Antivirus changed to accomodate rpmlint
  (mood: irritated).

* Tue Jan 19 2010 Dave M. <dave.nerd@gmail.com> - 4.23-1
- Updated to release 4.23.
- Removed perl(gettext) from Requires.
- Replaced perl(libwww-perl) with perl(LWP::UserAgent).

* Fri Dec 25 2009 Dave M. <dave.nerd@gmail.com> - 4.22-1
- Updated to release 4.22.
- License updated as GPL+ or Artistic.
- desktop-file-utils is now BuildRequires.

* Sat Dec 5 2009 Dave M. <dave.nerd@gmail.com> - 4.21-1
- Updated to release 4.21.

* Wed Nov 11 2009 Dave M. <dave.nerd@gmail.com> - 4.20-2
- desktop-file-utils is now Required
- Source URL now honors guidelines
- files in files section standardized in style

* Sun Nov 8 2009 Dave M. <dave.nerd@gmail.com> - 4.20-1
- Updated to release 4.20.
- install is now install -p

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Mar 07 2009 Jerome Soyer <saispo@gmail.com> - 4.10-1
- New upstream release

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 15 2009 Jerome Soyer <saispo@gmail.com> - 4.09-1
- New upstream release

* Wed Jan 07 2009 Jerome Soyer <saispo@gmail.com> - 4.08-4
- Remove script from prep section

* Wed Jan 07 2009 Jerome Soyer <saispo@gmail.com> - 4.08-3
- Add Perl Provides and Requires in prep section
- Add Requires on Perl

* Tue Jan 06 2009 Jerome Soyer <saispo@gmail.com> - 4.08-2
- Change Licence tag
- Remove unneeded Requires and BuildRequires
- Remove scriptlets "update-mime-database"
- Move *.pm into regular Perl modules

* Fri Jan 02 2009 Jerome Soyer <saispo@gmail.com> - 4.08-1
- New upstream release

* Wed Dec 10 2008 Jerome Soyer <saispo@gmail.com> - 4.06-2
- Fix RPM Group
- Bump Release

* Tue Dec 09 2008 Jerome Soyer <saispo@gmail.com> - 4.06-1
- First Fedora Package
