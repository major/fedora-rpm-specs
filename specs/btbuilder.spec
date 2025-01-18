Summary: Turn based role-playing game builder and engine
Name: btbuilder
Version: 0.5.19
Release: 12%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
Url: http://www.identicalsoftware.com/btbuilder
Source: http://www.identicalsoftware.com/btbuilder/%{name}-%{version}.tgz
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: boost-devel
BuildRequires: expat-devel
BuildRequires: libpng-devel
BuildRequires: physfs-devel
BuildRequires: SDL2-devel
BuildRequires: SDL2_image-devel
BuildRequires: SDL2_mixer-devel
BuildRequires: SDL_mng-devel
BuildRequires: SDL2_ttf-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: make
Requires:       %{name}-data = %{version}
Requires: hicolor-icon-theme

%description
Bt Builder is a turn based role-playing game builder and engine in the style
of the old Bard's Tale series. It completely supports the functionality of the
Bard's Tale Construction Set. The eventual goal is to make a game builder that
can implement the three main Bard's Tale games in addition to Construction Set
games.

%package	data
Summary:	%{summary}
Requires:	%{name} = %{version}
BuildArch:      noarch

%description	data
This package contains the data files for Bt Builder.

%prep
%setup -q

%build
%make_build CFLAGS="%{optflags}"

%install
make prefix=%{buildroot} install

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml

%files
%doc README
%{_bindir}/*
%{_datadir}/icons/hicolor/*/apps/btbuilder.png
%{_datadir}/applications/btbuilder.desktop
%{_datadir}/appdata/btbuilder.appdata.xml

%files data
%license COPYING
%{_datadir}/btbuilder

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.19-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.19-11
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.19-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.19-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.19-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 0.5.19-7
- Rebuilt for Boost 1.83

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 0.5.19-5
- Rebuilt for Boost 1.81

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 0.5.19-2
- Rebuilt for Boost 1.78

* Thu Apr 07 2022 Dennis Payne <dulsi@identicalsoftware.com> - 0.5.19-1
- New version of btbuilder released.

* Sun Jan 26 2020 Dennis Payne <dulsi@identicalsoftware.com> - 0.5.18-1
- New version of btbuilder released.

* Wed May 30 2018 Dennis Payne <dulsi@identicalsoftware.com> - 0.5.17-1
- New version of btbuilder released.

* Sun Feb 18 2018 Dennis Payne <dulsi@identicalsoftware.com> - 0.5.16-2
- Add build requirement of gcc-c++.

* Sat Feb 10 2018 Dennis Payne <dulsi@identicalsoftware.com> - 0.5.16-1
- New version of btbuilder released.
- Removed obsolete scriptlets.

* Thu Jul 13 2017 Dennis Payne <dulsi@identicalsoftware.com> - 0.5.15-1
- New version of btbuilder released.

* Thu Mar 02 2017 Dennis Payne <dulsi@identicalsoftware.com> - 0.5.14-3
- Switching to gnu++11 instead of std++11 for powerpc support.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 11 2016 Dennis Payne <dulsi@identicalsoftware.com> - 0.5.14-1
- New version of btbuilder released.

* Wed Oct 19 2016 Dennis Payne <dulsi@identicalsoftware.com> - 0.5.13-1
- New version of btbuilder released.

* Wed Sep 21 2016 Dennis Payne <dulsi@identicalsoftware.com> - 0.5.12-1
- New version of btbuilder released.
- Add validation of appdata file.
- Require hicolor icons.

* Fri Sep 02 2016 Dennis Payne <dulsi@identicalsoftware.com> - 0.5.11-2
- Separate data files into seperate package.

* Sat Aug 20 2016 Dennis Payne <dulsi@identicalsoftware.com> - 0.5.11-1
- New version of btbuilder released.

* Tue Jul 12 2016 Dennis Payne <dulsi@identicalsoftware.com> - 0.5.9-1
- New version of btbuilder released.

* Thu Apr 14 2016 Dennis Payne <dulsi@identicalsoftware.com> - 0.5.8-1
- New version of btbuilder released.

* Wed Jan 13 2016 Dennis Payne <dulsi@identicalsoftware.com> - 0.5.7-1
- New version of btbuilder released.

* Thu Dec 24 2015 Dennis Payne <dulsi@identicalsoftware.com> - 0.5.6-1
- New version of btbuilder released.
- appdata file added.

* Fri Aug 07 2015 Dennis Payne <dulsi@identicalsoftware.com> - 0.5.5-1
- New version of btbuilder released.

* Mon Jul 20 2015 Dennis Payne <dulsi@identicalsoftware.com> - 0.5.4-1
- New version of btbuilder released.

* Sun May 31 2015 Dennis Payne <dulsi@identicalsoftware.com> - 0.5.3-1
- New version of btbuilder released.

* Fri May 1 2015 Dennis Payne <dulsi@identicalsoftware.com> - 0.5.2-1
- New version of btbuilder released.

* Thu Apr 16 2015 Dennis Payne <dulsi@identicalsoftware.com> - 0.5.1-1
- New version of btbuilder released.

* Mon Sep 29 2014 Dennis Payne <dulsi@identicalsoftware.com> - 0.5.0-1
- New version of btbuilder released.

* Mon Jul 21 2014 Dennis Payne <dulsi@identicalsoftware.com> - 0.4.7-1
- New version of btbuilder released.

* Tue Jun 17 2014 Dennis Payne <dulsi@identicalsoftware.com> - 0.4.6-1
- New version of btbuilder released.

* Fri May 9 2014 Dennis Payne <dulsi@identicalsoftware.com> - 0.4.5-1
- New version of btbuilder released.

* Mon Apr 14 2014 Dennis Payne <dulsi@identicalsoftware.com> - 0.4.4-1
- New version of btbuilder released.

* Mon Mar 24 2014 Dennis Payne <dulsi@identicalsoftware.com> - 0.4.3-1
- Modifications based on review of spec file for Fedora.
- New version of btbuilder released.
