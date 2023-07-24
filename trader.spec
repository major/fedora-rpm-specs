# ***********************************************************************
# *                                                                     *
# *            Star Traders: A Game of Interstellar Trading             *
# *               Copyright (C) 1990-2022, John Zaitseff                *
# *                                                                     *
# ***********************************************************************

# Author: John Zaitseff <J.Zaitseff@zap.org.au>
# $Id: 4f8a9b2f09a1e5cdac0fc1694a8692dffa46c9cf $

# This file is distributed under the same licence as Star Traders itself:
# the GNU General Public License, version 3 or later.

Name:           trader
Version:        7.18
Release:        3%{?dist}
Summary:        Star Traders, a simple game of interstellar trading
License:        GPLv3+
Url:            https://www.zap.org.au/projects/trader/
Source0:        https://ftp.zap.org.au/pub/trader/unix/trader-%{version}.tar.xz
Source1:        https://ftp.zap.org.au/pub/trader/unix/trader-%{version}.tar.xz.sig
Source2:        https://www.zap.org.au/~john/pubkey.gpg

BuildRequires:  gcc make gettext pkgconfig(ncurses) desktop-file-utils libappstream-glib gperf gnupg2
Provides:       bundled(gnulib)

%description
Star Traders is a simple game of interstellar trading, where the objective
is to create companies, buy and sell shares, borrow and repay money, in
order to become the wealthiest player (the winner).

%global _hardened_build 1

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q

%build
%configure
%make_build

%install
%make_install
%find_lang %{name}
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%files -f %{name}.lang
%doc README NEWS
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_metainfodir}/%{name}.appdata.xml

%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Aug 05 2022 John Zaitseff <J.Zaitseff@zap.org.au> - 7.18-1
- Updated the RPM package for a new release of Star Traders: version 7.18.
- Added verification of upstream signature.

* Wed Jan 20 2021 John Zaitseff <J.Zaitseff@zap.org.au> - 7.16-1
- Updated the RPM package for a new release of Star Traders: version 7.16.
- Added an AppStream-conforming metadata file.

* Tue Jan 12 2021 John Zaitseff <J.Zaitseff@zap.org.au> - 7.15-1
- Updated the RPM package for a new release of Star Traders: version 7.15.
- Added a dependency on make, as per current packaging guidelines.

* Thu Jan 09 2020 John Zaitseff <J.Zaitseff@zap.org.au> - 7.14-1
- Updated the RPM package for a new release of Star Traders: version 7.14.

* Thu Nov 14 2019 John Zaitseff <J.Zaitseff@zap.org.au> - 7.13-2
- Removed obsolete gtk-update-icon-cache scriplets.

* Thu Nov 14 2019 John Zaitseff <J.Zaitseff@zap.org.au> - 7.13-1
- Updated the RPM package for a new release of Star Traders: version 7.13.

* Wed Aug 30 2017 John Zaitseff <J.Zaitseff@zap.org.au> - 7.12-1
- Updated the RPM package for a new release of Star Traders: version 7.12.

* Sun Jun 18 2017 John Zaitseff <J.Zaitseff@zap.org.au> - 7.11-1
- Updated the RPM package for a new release of Star Traders: version 7.11.

* Sun Jun 04 2017 John Zaitseff <J.Zaitseff@zap.org.au> - 7.10-2
- Removed superfluous slash in desktop-file-validate command line.

* Fri Jun 02 2017 John Zaitseff <J.Zaitseff@zap.org.au> - 7.10-1
- Updated the RPM package for a new release of Star Traders: version 7.10.
- Changed a dependency from ncurses-devel to pkgconfig(ncurses), now that
  the Autoconf macro uses pkg-config.
- Added a dependency on gcc, as per the Fedora Packaging Guidelines for C
  programs.
- Added a dependency on desktop-file-utils for the desktop file.
- Install the desktop file and icons now shipped with Star Traders.
- Install the COPYING file to /usr/share/licenses/trader.
- Use generic make_build and make_install macros.

* Tue Jan 05 2016 John Zaitseff <J.Zaitseff@zap.org.au> - 7.9-1
- Updated the RPM package for a new release of Star Traders: version 7.9.

* Thu Sep 10 2015 John Zaitseff <J.Zaitseff@zap.org.au> - 7.8-1
- Updated the RPM package for a new release of Star Traders: version 7.8.

* Tue Aug 18 2015 John Zaitseff <J.Zaitseff@zap.org.au> - 7.7-1
- Updated the RPM package for a new release of Star Traders: version 7.7.

* Wed Aug 13 2014 John Zaitseff <J.Zaitseff@zap.org.au> - 7.6-1
- Updated the RPM package for a new release of Star Traders: version 7.6.

* Sat May 24 2014 John Zaitseff <J.Zaitseff@zap.org.au> - 7.5-1
- Updated the RPM package for a new release of Star Traders: version 7.5.

* Wed Oct 03 2012 John Zaitseff <J.Zaitseff@zap.org.au> - 7.4-3
- Added a dependency on gperf: it may be required for gnulib.

* Thu Sep 20 2012 John Zaitseff <J.Zaitseff@zap.org.au> - 7.4-2
- Simplified the RPM spec file to suit Fedora guidelines.

* Wed May 09 2012 John Zaitseff <J.Zaitseff@zap.org.au> - 7.4-1
- Updated the RPM package for a new release of Star Traders: version 7.4.

* Mon Apr 30 2012 John Zaitseff <J.Zaitseff@zap.org.au> - 7.3.99.2-2
- Changed the RPM spec file to remove OpenSUSE-specific sections

* Mon Apr 16 2012 John Zaitseff <J.Zaitseff@zap.org.au> - 7.3.99.2-1
- Initial RPM package of Star Traders.

