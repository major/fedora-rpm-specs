# Review: https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=215169

%global minor_version 0.8
%global xfceversion 4.13

Name:           xfce4-dict
Version:        0.8.4
Release:        5%{?dist}
Summary:        A Dictionary Client for the Xfce desktop environment
Summary(de):    Ein Wörterbuch-Client für die Xfce Desktop-Umgebung

License:        GPLv2+
URL:            http://goodies.xfce.org/projects/applications/%{name}
Source0:        http://archive.xfce.org/src/apps/%{name}/%{minor_version}/%{name}-%{version}.tar.bz2
#VCS:           git:git://git.xfce.org/apps/xfce4-dict

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
Requires:       enchant, xdg-utils


%description
Xfce4 Dictionary is a client program to query different dictionaries. It can
query a Dict server (RFC 2229), open online dictionaries in a web browser or
verify the spelling of a word using enchant. This package contains the
stand-alone application, that can be used in different desktop environments
too.

%package        plugin
Summary:        Xfce panel plugin to query a Dict server
Requires:       %{name} = %{version}-%{release}
Requires:       xfce4-panel >= %{xfceversion}

%description    plugin
Xfce4 Dictionary is a client program to query different dictionaries. It can
query a Dict server (RFC 2229), open online dictionaries in a web browser or
verify the spelling of a word using enchant. This package contains the plugin
for the Xfce panel.


%prep
%setup -q


%build
%configure --disable-static
%make_build

%install
%make_install

# remove la file
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# make sure debuginfo is generated properly
chmod -c +x %{buildroot}%{_libdir}/xfce4/panel/plugins/*.so

%find_lang %{name}

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/org.xfce.Dictionary.png
%{_datadir}/icons/hicolor/scalable/apps/org.xfce.Dictionary.svg
%{_mandir}/man1/%{name}.1.gz

%files plugin
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/*.desktop

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Oct 18 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.4-1
- Update to 0.8.4

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 06 2019 Kevin Fenzi <kevin@scrye.com> - 0.8.3-1
- Update to 0.8.3.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 28 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.2-1
- Update to 0.8.2

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.1-20
- Rebuilt (xfce 4.13)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 02 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.1-1
- Update to 0.8.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 05 2017 Filipe Rosset <rosset.filipe@gmail.com> - 0.8.0-1
- Rebuilt to new upstream release 0.8.0 + spec clean up

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Apr 25 2016 Kevin Fenzi <kevin@scrye.com> - 0.7.2-1
- Update to 0.7.2. Translation updates.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 15 2015 Kevin Fenzi <kevin@scrye.com> 0.7.1-1
- Update to 0.7.1 with translation updates and a few bugfixes

* Thu Mar 05 2015 Kevin Fenzi <kevin@scrye.com> 0.7.0-7
- Rebuild again for Xfce 4.12

* Sat Feb 28 2015 Kevin Fenzi <kevin@scrye.com> 0.7.0-6
- Rebuild for Xfce 4.12

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 0.7.0-5
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 21 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0 (fixes #926775 and #962242)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 15 2012 Kevin Fenzi <kevin@scrye.com> - 0.6.0-8
- Rebuild for Xfce 4.10(pre2)

* Thu Apr 05 2012 Kevin Fenzi <kevin@scrye.com> - 0.6.0-7
- Rebuild for Xfce 4.10

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.6.0-5
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Dec 04 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.0-3
- Rebuild for Xfce 4.8pre1

* Wed Feb 17 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.0-2
- Add patch to fix DSO linking (#564640)

* Thu Dec 31 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0
- Drop OnlyShowIn

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 30 2009 Caolán McNamara <caolanm@redhat.com> - 0.5.3-2
- Resolves: rhbz#508633 Require enchant rather than aspell, xfce4-dict
  already prefers it at run-time

* Sat May 09 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.3-1
- Update to 0.5.3
- Update icon-cache scriptlets

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.2-2
- Rebuild for Xfce 4.6 (Beta 3)

* Thu Nov 27 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.2-1
- Update to 0.5.2

* Thu Nov 27 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1
- Update gtk-update-icon-cache scriptlets

* Tue Nov 11 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0
- Only show in Xfce menu

* Tue Sep 30 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.1-2
- BuildRequire intltool

* Tue Sep 30 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1
- Require xdg-utils as xdg-open is the preferred command to open URLs now

* Sat May 24 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0
- Rename to xfce4-dict because we now have a standalone application

* Sun Mar 09 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.2.1-4
- Autorebuild for GCC 4.3

* Sat Aug 25 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.1-3
- Rebuild for BuildID feature
- Update license tag

* Sat Apr 28 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.1-2
- Rebuild for Xfce 4.4.1

* Mon Jan 22 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1 on Xfce 4.4.
- Update gtk-icon-cache scriptlets.

* Sun Nov 12 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.0-2
- Add %%defattr (#215169).

* Sat Nov 11 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0.

* Sat Sep 23 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.0-1
- Initial Fedora Extras version.
