Name:           edgar
Version:        1.37
Release:        6%{?dist}
Summary:        A platform game

# edgar now contains sounds licensed under a "good" Fedora license:
# http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=653813#80
# Automatically converted from old format: GPLv2+ and CC-BY and CC-BY-SA and CC0 and GPLv3 - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY AND LicenseRef-Callaway-CC-BY-SA AND CC0-1.0 AND GPL-3.0-only
URL:            https://www.parallelrealities.co.uk/games/edgar/
Source0:        https://github.com/riksweeney/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: SDL2_image-devel
BuildRequires: SDL2_mixer-devel
BuildRequires: SDL2_ttf-devel
BuildRequires: zlib-devel
BuildRequires: libpng-devel
BuildRequires: gettext
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils
Requires:      hicolor-icon-theme


%description
When his father fails to return home after venturing out one dark and stormy 
night, Edgar fears the worst: he has been captured by the evil sorcerer who 
lives in a fortress beyond the forbidden swamp.

Donning his armor, Edgar sets off to rescue him, but his quest will not be 
easy...


%prep
%setup -q

# Fix Makefile
sed -i 's/LDFLAGS += -s/:/' makefile
sed -i 's:$(PREFIX)/games/:$(PREFIX)/bin/:' makefile
sed -i 's:$(PREFIX)/share/games/edgar/:$(PREFIX)/share/edgar/:' \
  makefile


%build
%set_build_flags
%make_build NO_PAK=1


%install
%make_install NO_PAK=1

desktop-file-validate \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%find_lang %{name}


%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man6/%{name}.6*
%doc %{_pkgdocdir}
%license doc/license


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.37-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.37-5
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.37-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.37-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 01 2024 Andrea Musuruane <musuruan@gmail.com> - 1.37-1
- Updated to new upstream release

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jan 01 2023 Andrea Musuruane <musuruan@gmail.com> - 1.36-1
- Updated to new upstream release

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.35-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 01 2022 Andrea Musuruane <musuruan@gmail.com> - 1.35-1
- Updated to new upstream release

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  1 12:34:03 CET 2021 Andrea Musuruane <musuruan@gmail.com> - 1.34-1
- Updated to new upstream release

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Apr 19 2020 Andrea Musuruane <musuruan@gmail.com> - 1.33-1
- Updated to new upstream release

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 24 2019 Andrea Musuruane <musuruan@gmail.com> - 1.32-1
- Updated to upstream 1.32

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 17 2019 Andrea Musuruane <musuruan@gmail.com> - 1.31-1
- Updated to upstream 1.31-1
- Updated URL
- Used %%set_build_flags macro

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 22 2018 Andrea Musuruane <musuruan@gmail.com> - 1.29-1
- Updated to upstream 1.29-1

* Wed Feb 21 2018 Andrea Musuruane <musuruan@gmail.com> - 1.28-4
- Added gcc dependency

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 13 2018 Andrea Musuruane <musuruan@gmail.com> - 1.28-2
- Fixed LDFLAGS usage
- Disabled PAK
- Cleanup

* Sat Jan 13 2018 Andrea Musuruane <musuruan@gmail.com> - 1.28-1
- Updated to upstream 1.28-1

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.27-4
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Andrea Musuruane <musuruan@gmail.com> - 1.27-1
- Updated to upstream 1.27-1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 01 2017 Andrea Musuruane <musuruan@gmail.com> - 1.26-1
- Updated to upstream 1.26-1

* Sat Oct 01 2016 Andrea Musuruane <musuruan@gmail.com> - 1.25-1
- Updated to upstream 1.25-1

* Tue May 24 2016 Andrea Musuruane <musuruan@gmail.com> - 1.24-1
- Updated to upstream 1.24-1

* Sat Feb 20 2016 Andrea Musuruane <musuruan@gmail.com> - 1.23-1
- Updated to upstream 1.23-1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 07 2015 Andrea Musuruane <musuruan@gmail.com> - 1.22-1
- Updated to upstream 1.22-1
- Minor cleanup

* Sun Jun 21 2015 Andrea Musuruane <musuruan@gmail.com> - 1.21-1
- Updated to upstream 1.21-1
- Updated Source0 URL

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Mar 28 2015 Andrea Musuruane <musuruan@gmail.com> - 1.20-1
- Updated to upstream 1.20-1
- Minor cleanup

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.19-2
- Add an AppData file for the software center

* Fri Dec 19 2014 Andrea Musuruane <musuruan@gmail.com> - 1.19-1
- Updated to upstream 1.19-1

* Tue Oct 14 2014 Andrea Musuruane <musuruan@gmail.com> - 1.18-1
- Updated to upstream 1.18-1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Aug 10 2014 Andrea Musuruane <musuruan@gmail.com> - 1.17-1
- Updated to upstream 1.17-1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jun 01 2014 Andrea Musuruane <musuruan@gmail.com> - 1.16-1
- Updated to upstream 1.16-1

* Sun Mar 02 2014 Andrea Musuruane <musuruan@gmail.com> - 1.15-1
- Updated to upstream 1.15-1

* Thu Jan 02 2014 Andrea Musuruane <musuruan@gmail.com> - 1.14-1
- Updated to upstream 1.14-1

* Mon Oct 28 2013 Andrea Musuruane <musuruan@gmail.com> - 1.13-1
- Updated to upstream 1.13-1

* Sat Aug 31 2013 Andrea Musuruane <musuruan@gmail.com> - 1.12-2
- First import in Fedora
- Dropped no longer needed buildroot cleaning at the beginning of %%install

* Sun Aug 25 2013 Andrea Musuruane <musuruan@gmail.com> - 1.12-1
- Updated to upstream 1.12-1
- Used unversioned docdir
- Sounds are now licensed under a "good" Fedora license

* Wed Jun 19 2013 Andrea Musuruane <musuruan@gmail.com> - 1.09-1
- Updated to upstream 1.09-1

* Thu Apr 04 2013 Andrea Musuruane <musuruan@gmail.com> - 1.08-1
- Updated to upstream 1.08-1

* Sun Mar 03 2013 Andrea Musuruane <musuruan@gmail.com> - 1.07-1
- Updated to upstream 1.07-1

* Fri Feb 08 2013 Andrea Musuruane <musuruan@gmail.com> - 1.06-2
- Updated to upstream 1.06-2

* Sat Jan 26 2013 Andrea Musuruane <musuruan@gmail.com> - 1.06-1
- Updated to upstream 1.06-1

* Thu Dec 06 2012 Andrea Musuruane <musuruan@gmail.com> - 1.05-1
- Updated to upstream 1.05-1

* Sun Oct 28 2012 Andrea Musuruane <musuruan@gmail.com> - 1.04-2
- Fixed license (BZ #2378)

* Sat Sep 22 2012 Andrea Musuruane <musuruan@gmail.com> - 1.04-1
- Updated to upstream 1.04-1

* Wed Aug 08 2012 Andrea Musuruane <musuruan@gmail.com> - 1.03-1
- Updated to upstream 1.03-1

* Sat Jun 23 2012 Andrea Musuruane <musuruan@gmail.com> - 1.02-2
- Updated to upstream 1.02-2

* Sun Jun 17 2012 Andrea Musuruane <musuruan@gmail.com> - 1.02-1
- Updated to upstream 1.02-1

* Wed May 16 2012 Andrea Musuruane <musuruan@gmail.com> - 1.01-1
- Updated to upstream 1.01-2

* Thu Apr 26 2012 Andrea Musuruane <musuruan@gmail.com> - 1.00-1
- First release

