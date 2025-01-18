Name:           autodownloader
Version:        0.5.0
Release:        13%{?dist}
Summary:        GUI-tool to automate the download of certain files
License:        GPL-2.0-or-later
URL:            https://github.com/frenzymadness/AutoDownloader
Source0:        https://github.com/frenzymadness/AutoDownloader/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires: make
Requires:       python3-gobject python3-six gtk3 hicolor-icon-theme

%description
Some software (usually games) requires certain data files to operate, sometimes
these datafiles can be freely downloaded but may not be redistributed and thus
cannot be put into so called packages as part of a distro.

autodownloader is a tool which can be used as part of a package to automate the
download of the needed files. It will prompt the user explaining to him the
need of the download and asking if it is ok to make an internet connection,
after this it will show the license of the to be downloaded files and last it
will do the actual download and md5 verification off these files. This whole
process can be configured by the packager through a simple configuration file.

Notice that Autodownloader while open source itself, may download files which
are not permitted to be (re)distributed unlike most files in Fedora.


%prep
%setup -q -n AutoDownloader-%{version}
%py3_shebang_fix .

# Avoid hardcoding /usr prefix
sed -i -e 's!/usr/bin!%{_bindir}!' Makefile
sed -i -e 's!/usr/share!%{_datadir}!' Makefile


%build
# nothing to build pure python code only


%install
make install DESTDIR=$RPM_BUILD_ROOT


%files
%license COPYING
%doc ChangeLog README.txt examples/example.autodlrc
%{_bindir}/autodl
%{_datadir}/autodl
%{_datadir}/icons/hicolor/*/apps/autodl.png


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Mar 05 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.5.0-8
- migrated to SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Lumír Balhar <lbalhar@redhat.com> - 0.5.0-1
- Update to 0.5.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Pete Walter <pwalter@fedoraproject.org> - 0.4.0-2
- Avoid hardcoding /usr prefix

* Mon Nov 04 2019 Lumír Balhar <lbalhar@redhat.com> - 0.4.0-1
- New upstream, new release
- Python 3 & GTK 3 compatibility

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 12 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.3.0-19
- Fix shebang.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 10 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.3.0-17
- Fix shebang handling.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.0-14
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jun  1 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3.0-1
- New upstream release (all patches merged)
- Includes new icons by Michael Beckwith

* Thu Dec 13 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2.0-6
- Add 2 more patches from Ivo Manca:
  * Make ask to start configurable
  * Some trailing whitespace cleanups

* Thu Nov 29 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2.0-5
- Apply patch from Ivo Manca fixing the downloading of files with an
  unknown size, thanks!

* Thu Oct  4 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2.0-4
- Check if files exist (and have the correct md5sum) from a previous download
  and skip downloading them (bz 309381)

* Fri Aug  3 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2.0-3
- Update License tag for new Licensing Guidelines compliance

* Wed May 16 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2.0-2
- Make the timeout for stalled mirror detection larger, this fixes the use of
  autodownloader for those with slow links

* Sun Apr 29 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2.0-1
- Initial Fedora Extras package
