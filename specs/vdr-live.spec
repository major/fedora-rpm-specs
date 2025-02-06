# https://github.com/MarkusEh/vdr-plugin-live/commit/9967f1d6757a4f4855a6b07abf526258838dd5ac
%global commit0 9967f1d6757a4f4855a6b07abf526258838dd5ac
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gitdate 20241103
# version we want to build against
%global vdr_version 2.6.3
# Set vdr_version based on Fedora version
%if 0%{?fedora} >= 42
%global vdr_version 2.7.2
%elif 0%{?fedora} >= 40
%global vdr_version 2.6.9
%endif

Name:           vdr-live
Version:        3.4.1
# Release:        0.2.%%{gitdate}git%%{shortcommit0}%%{?dist}
Release:        1%{?dist}
Summary:        An interactive web interface with HTML5 live stream support for VDR

# The entire source code is GPL-2.0-or-later except live/js/mootools/ which is LicenseRef-Callaway-MIT
License:        GPL-2.0-or-later AND LicenseRef-Callaway-MIT
URL:            https://github.com/MarkusEh/vdr-plugin-live
# Source0:        https://github.com/MarkusEh/vdr-plugin-live/archive/%%{commit0}/%%{name}-%%{version}-%%{shortcommit0}.tar.gz
Source0:        https://github.com/MarkusEh/vdr-plugin-live/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  vdr-devel >= %{vdr_version}
BuildRequires:  pcre2-devel
BuildRequires:  tntnet-devel
BuildRequires:  cxxtools-devel
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}
Requires:       %{name}-data = %{version}-%{release}

%description
New version with HTML5 live stream support.
Live, the "Live Interactive VDR Environment", is a plugin providing the
possibility to interactively control the VDR and some of it's plugins by
a web interface.

Unlike external utility programs that communicate with VDR and it's plugins
by SVDRP, Live has direct access to VDR's data structures and is thus very
fast.

%package data
Summary:       Images, themes and JavaScript for %{name}
BuildArch:     noarch
Requires:      %{name} = %{version}-%{release}

%description data
This package contains images, themes and JavaScript.

%prep
#%%autosetup -p1 -n vdr-plugin-live-%{commit0}
%autosetup -p1 -n vdr-plugin-live-%{version}

# delete unused directories and files
find -name .git -type d -or -name gitignore -type d | xargs rm -rfv

# remove bundled tntnet libraries
rm -rf httpd

iconv -f iso-8859-1 -t utf-8 README > README.utf8 ; mv README.utf8 README

%build
%make_build CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC"

%install
%make_install

# live.conf
install -Dpm 644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/sysconfig/vdr-plugins.d/live.conf

%find_lang %{name}

%files -f %{name}.lang
%doc CONTRIBUTORS README
%license COPYING
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/live.conf
%config(noreplace) %{_sysconfdir}/vdr/plugins/live/ffmpeg.conf
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}

%files data
%{vdr_resdir}/plugins/live/

%changelog
* Tue Feb 04 2025 Martin Gansser <martinkg@fedoraproject.org> - 3.4.1-1
- Update to 3.4.1

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 02 2025 Martin Gansser <martinkg@fedoraproject.org> - 3.4.0-1
- Update to 3.4.0

* Sun Dec 22 2024 Martin Gansser <martinkg@fedoraproject.org> - 3.3.12-1
- Update to 3.3.12

* Wed Dec 11 2024 Martin Gansser <martinkg@fedoraproject.org> - 3.3.11-1
- Update to 3.3.11

* Tue Nov 19 2024 Martin Gansser <martinkg@fedoraproject.org> - 3.3.10-1
- Update to 3.3.10

* Tue Nov 05 2024 Martin Gansser <martinkg@fedoraproject.org> - 3.3.9-1
- Update to 3.3.9

* Sun Nov 03 2024 Martin Gansser <martinkg@fedoraproject.org> - 3.3.9-0.2.20241103git9967f1d
- Update to 3.3.9-0.2.20241103git9967f1d

* Sat Nov 02 2024 Martin Gansser <martinkg@fedoraproject.org> - 3.3.9-0.1.20241101gitf67dfc0
- Update to 3.3.9-0.1.20241101gitf67dfc0

* Sat Oct 26 2024 Martin Gansser <martinkg@fedoraproject.org> - 3.3.8-1
- Update to 3.3.8

* Tue Oct 22 2024 Martin Gansser <martinkg@fedoraproject.org> - 3.3.8-0.2.20241022git8b97db3
- Update to 3.3.8-0.2.20241022git8b97db3

* Wed Oct 09 2024 Martin Gansser <martinkg@fedoraproject.org> - 3.3.8-0.1.20241008git80b8da8
- Rebuilt for new VDR API version 2.7.2
- Update to 3.3.8-0.1.20241008git80b8da8

* Mon Sep 30 2024 Martin Gansser <martinkg@fedoraproject.org> - 3.3.7-1
- Update to 3.3.7

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 3.3.5-5
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 15 2024 Martin Gansser <martinkg@fedoraproject.org> - 3.3.5-3
- Rebuilt for new VDR API version 2.6.9

* Fri Jul 12 2024 Martin Gansser <martinkg@fedoraproject.org> - 3.3.5-2
- Rebuilt for new VDR API version 2.6.8

* Fri Apr 12 2024 Martin Gansser <martinkg@fedoraproject.org> - 3.3.5-1
- Update to 3.3.5
- Rebuilt for new VDR API version

* Fri Jan 26 2024 Martin Gansser <martinkg@fedoraproject.org> - 3.3.4-2
- Rebuilt for new VDR API version

* Fri Jan 05 2024 Martin Gansser <martinkg@fedoraproject.org> - 3.3.4-1
- Rebuilt for new VDR API version
- Add BR gettext for rawhide

* Wed Dec 20 2023 Martin Gansser <martinkg@fedoraproject.org> - 3.3.3-1
- Update to 3.3.3

* Mon Nov 27 2023 Martin Gansser <martinkg@fedoraproject.org> - 3.3.2-1
- Update to 3.3.2

* Tue Nov 21 2023 Martin Gansser <martinkg@fedoraproject.org> - 3.3.1-1
- Update to 3.3.1

* Sun Nov 19 2023 Martin Gansser <martinkg@fedoraproject.org> - 3.3.0-1
- Update to 3.3.0

* Tue Oct 03 2023 Martin Gansser <martinkg@fedoraproject.org> - 3.2.1-1
- Update to 3.2.1

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jun 11 2023 Martin Gansser <martinkg@fedoraproject.org> - 3.2.0-1
- Update to 3.2.0

* Sun Jun 11 2023 Martin Gansser <martinkg@fedoraproject.org> - 3.1.12-1
- Update to 3.1.12
- Add %{name}-timerconflict.patch

* Tue Jan 24 2023 Martin Gansser <martinkg@fedoraproject.org> - 3.1.11-3
- Rebuilt

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 18 2023 Martin Gansser <martinkg@fedoraproject.org> - 3.1.11-1
- Update to 3.1.11

* Fri Jan 06 2023 Martin Gansser <martinkg@fedoraproject.org> - 3.1.10-2
- Rebuilt

* Mon Dec 26 2022 Martin Gansser <martinkg@fedoraproject.org> - 3.1.10-1
- Update to 3.1.10

* Wed Dec 14 2022 Martin Gansser <martinkg@fedoraproject.org> - 3.1.9-3
- Rebuilt for new VDR API version

* Thu Dec 01 2022 Martin Gansser <martinkg@fedoraproject.org> - 3.1.9-2
- Rebuilt for new VDR API version

* Sun Nov 27 2022 Martin Gansser <martinkg@fedoraproject.org> - 3.1.9-1
- Updatae to 3.1.9

* Thu Nov 17 2022 Martin Gansser <martinkg@fedoraproject.org> - 3.1.8-2
- Rebuilt due undefined symbol: _ZN7vdrlive6cUsers14logged_in_userB5cxx11E

* Mon Oct 10 2022 Martin Gansser <martinkg@fedoraproject.org> - 3.1.8-1
- Updatae to 3.1.8

* Thu Jul 28 2022 Martin Gansser <martinkg@fedoraproject.org> - 3.1.7-1
- Updatae to 3.1.7

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Martin Gansser <martinkg@fedoraproject.org> - 3.1.6-2
- Built against correct vdr-devel version

* Sun Jun 19 2022 Martin Gansser <martinkg@fedoraproject.org> - 3.1.6-1
- Updatae to 3.1.6

* Sat Feb 12 2022 Martin Gansser <martinkg@fedoraproject.org> - 3.1.5-2
- Rebuilt

* Thu Feb 03 2022 Martin Gansser <martinkg@fedoraproject.org> - 3.1.5-1
- Update to 3.1.5

* Sat Jan 29 2022 Martin Gansser <martinkg@fedoraproject.org> - 3.1.4-0.4.20211228git0fbd9b3
- Add %%undefine _package_note_flags to vdr main package
- rebuild for rawhide

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-0.3.20211228git0fbd9b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 30 2021 Martin Gansser <martinkg@fedoraproject.org> - 3.1.4-0.2.20211228git0fbd9b3
- Build compatibility to g++11

* Tue Dec 28 2021 Martin Gansser <martinkg@fedoraproject.org> - 3.1.4-0.1.20211228git0fbd9b3
- Replace obsolete pcre by pcre2
- Update to 3.1.4-0.1.20211228git0fbd9b3

* Mon Nov 15 2021 Martin Gansser <martinkg@fedoraproject.org> - 3.1.3-1
- Update to 3.1.3

* Fri Nov  5 2021 Dirk Nehring <dnehring@gmx.net> - 3.1.1-2
- Build compatibility to g++11

* Mon Nov 01 2021 Martin Gansser <martinkg@fedoraproject.org> - 3.1.1-1
- Update to 3.1.1

* Thu Oct 28 2021 Martin Gansser <martinkg@fedoraproject.org> - 3.1.0-1
- Update to 3.1.0

* Fri Oct 15 2021 Martin Gansser <martinkg@fedoraproject.org> - 3.0.12-1
- Update to 3.0.12

* Sat Sep 11 2021 Martin Gansser <martinkg@fedoraproject.org> - 3.0.10-3
- Add vdr-plugin-live-noCopyTimer.patch to avoid copying vdr timer objects

* Fri Aug 06 2021 Martin Gansser <martinkg@fedoraproject.org> - 3.0.10-2
- Rebuilt fixes unresolved symbol

* Sun Jul 18 2021 Martin Gansser <martinkg@fedoraproject.org> - 3.0.10-1
- Update to 3.0.10

* Mon Jun 07 2021 Martin Gansser <martinkg@fedoraproject.org> - 3.0.9-1
- Update to 3.0.9

* Mon May 24 2021 Martin Gansser <martinkg@fedoraproject.org> - 3.0.8-1
- Update to 3.0.8

* Wed Apr 28 2021 Martin Gansser <martinkg@fedoraproject.org> - 3.0.7-0.2.20210307git075080a
- Rebuilt for new VDR API version

* Sun Mar 07 2021 Martin Gansser <martinkg@fedoraproject.org> - 3.0.7-0.1.20210307git075080a
- Update to 3.0.7-0.1.20210307git075080a

* Wed Mar 03 2021 Martin Gansser <martinkg@fedoraproject.org> - 3.0.6-1
- Update to 3.0.6

* Mon Mar 01 2021 Martin Gansser <martinkg@fedoraproject.org> - 3.0.5-1
- Rebuilt for cxxtools/tntnet-3.0 support
- Update to 3.0.5

* Sun Jan 31 2021 Martin Gansser <martinkg@fedoraproject.org> - 3.0.4-1
- Update to 3.0.4

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 2021 Martin Gansser <martinkg@fedoraproject.org> - 3.0.2-1
- Update to 3.0.2

* Thu Jan 21 2021 Martin Gansser <martinkg@fedoraproject.org> - 3.0.1-1
- Update to 3.0.1

* Sat Jan 16 2021 Martin Gansser <martinkg@fedoraproject.org> - 3.0.0-1
- Update to 3.0.0

* Sat Jan 16 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.3.1-20.20210111gitf6cfefa
- Add check_existing_recording.patch

* Mon Jan 11 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.3.1-19.20210111gitf6cfefa
- Update to 2.3.1-19.20210111gitf6cfefa

* Mon Jan 11 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.3.1-18.20201122git3b24485
- Use fork because its under maintenance
- Update to 2.3.1-18.20201122git3b24485 

* Sun Jan 03 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.3.1-17.20170623gite582514
- Rebuilt for new VDR API version

* Tue Dec 08 2020 Jonathan Wakely <jwakely@redhat.com> - 2.3.1-16.20170623gite582514
- Patched for GCC 11 compatibility.
- Remove sed command that is no longer needed.

* Thu Aug 27 2020 Martin Gansser <martinkg@fedoraproject.org> - 2.3.1-15.20170623gite582514
- Rebuilt for new VDR API version

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-14.20170623gite582514
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-13.20170623gite582514
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-12.20170623gite582514
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Martin Gansser <martinkg@fedoraproject.org> - 2.3.1-11.20170623gite582514
- Update to last git version 20170623gite582514
- Rebuilt for new VDR API version

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-10.20170519git5cb665d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 05 2018 Martin Gansser <martinkg@fedoraproject.org> - 2.3.1-9.20170519git5cb665d
- Add vdr-plugin-live_2018-11-04.diff

* Wed Oct 10 2018 Martin Gansser <martinkg@fedoraproject.org> - 2.3.1-8.20170519git5cb665d
- Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-7.20170519git5cb665d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 17 2018 Martin Gansser <martinkg@fedoraproject.org> - 2.3.1-6.20170619git5cb665d
- Rebuilt for vdr-2.4.0

* Wed Feb 14 2018 Martin Gansser <martinkg@fedoraproject.org> - 2.3.1-5.20170619git5cb665d
- Disable parallel make due build error on rawhide

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-4.20170519git5cb665d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3.20170519git5cb665d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2.20170519git5cb665d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 23 2017 Martin Gansser <martinkg@fedoraproject.org> - 2.3.1-1.20170619git5cb665d
- Update to recent git 2.3.1-1.20170619git5cb665d

* Tue Feb 14 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-25.20150213git6ea279a
- added %%{name}-libpages-build.patch

* Sat Feb 06 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-24.20150213git6ea279a
- added %%{name}-gcc6.patch

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-23.20150213git6ea279a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 08 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-22.20150213git6ea279a
- Rebuilt

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-21.20150213git6ea279a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.0-20.20150213git6ea279a
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 19 2015 Ville Skyttä <ville.skytta@iki.fi> - 0.3.0-19.20150213git6ea279a
- Rebuild

* Sat Feb 14 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-18.20150213git6ea279a
- rebuild for new git version

* Thu Feb 12 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-17.20150211git894daa8
- rebuild for new git version
- added Fedora %%optflags for CFLAGS and CXXFLAGS
- cleanup spec file
- mark license files as %%license where available

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-16.20130504git69f84f9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-15.20130504git69f84f9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Ville Skyttä <ville.skytta@iki.fi> - 0.3.0-14.20130504git69f84f9
- Rebuild

* Sat Mar 22 2014 Ville Skyttä <ville.skytta@iki.fi> - 0.3.0-13.20130504git69f84f9
- Rebuild

* Thu Feb 06 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-12.20130504git69f84f9
- rebuild against tntnet-2.2.1

* Tue Jan 21 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-11.20130504git69f84f9
- changed to %%{buildroot} macro
- rebuild against tntnet-2.2.1

* Fri Jan 17 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-10.20130504git69f84f9
- added vdr-live-data as requirement
- added gitdate
- added tarball download instructions

* Tue Jan 07 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-9.69f84f9
- rebuild
- changed global spec file declarations

* Sat Jan 04 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-8.20130504git69f84f9
- rebuild
- spec file cleanup

* Fri Jan 03 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-7.69f84f9
- add correct source file

* Sun Dec 29 2013 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-6.69f84f9
- Capitalized first letter
- Fixed spelling

* Sun Dec 29 2013 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-5.69f84f9
- unmark files in sub-package as %%config

* Sun Dec 29 2013 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-4.69f84f9
- added live directory to noarch sub-package 

* Fri Dec 27 2013 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-3.69f84f9
- change release tag
- change license tag

* Sat Dec 21 2013 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-2.20130504git
- rebuild for new git version
- remove bundled tntnet libraries

* Sat May 4 2013 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-1.20130504git
- rebuild for new git version

* Wed Apr 24 2013 Martin Gansser <linux4martin@gmx.de> - 0.3.0-1.20130412git
- rebuild for new git version
- spec file cleanup

* Fri Nov 2 2012 Martin Gansser <linux4martin@gmx.de> - 0.2.0-8.20121009git
- listed BuildRequirements one per line.

* Tue Oct 9 2012 Martin Gansser <linux4martin@gmx.de> - 0.2.0-7.20121009git
- added vdr-1.7.28 compile fix
- added API patch version >= 1.7.30
- rebuild for Fedora 18.

* Mon Aug 6 2012 Martin Gansser <linux4martin@gmx.de> - 0.2.0-6.20120325git
- added live.conf file

* Mon Aug 6 2012 Martin Gansser <linux4martin@gmx.de> - 0.2.0-5.20120325git
- removed Buildroot

* Mon May 14 2012 Martin Gansser <linux4martin@gmx.de> - 0.2.0-4.20120325git
- new release
- more cleanups

* Sun Apr 29 2012 Martin Gansser <linux4martin@gmx.de> - 0.2.0-3.20120218git
- first build for Fedora 17
- fixed vdr macro names
- fixed README file utf encoding

* Mon Sep 19 2011 Sebastian Vahl <fedora@deadbabylon.de> - 0.2.0-2.20110917git
- fix some rpmlint issues and cleanup spec

* Sat Sep 17 2011 Sebastian Vahl <fedora@deadbabylon.de> - 0.2.0-1.20110917git
- initial release
