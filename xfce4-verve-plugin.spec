# Review at https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=238348
%global _hardened_build 1
%global minor_version 2.0

Name:		xfce4-verve-plugin
Version:	2.0.1
Release:	7%{?dist}
Summary:	Comfortable command line plugin for the Xfce panel

License:	GPLv2+
URL:		http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:	http://archive.xfce.org/src/panel-plugins/%{name}/%{minor_version}/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:	gcc-c++
BuildRequires:	xfce4-panel-devel
BuildRequires:	libxfce4ui-devel
BuildRequires:	exo-devel >= 0.5.0
BuildRequires:	pcre-devel >= 5.0
BuildRequires:	dbus-glib-devel >= 0.34
BuildRequires:	libxml2-devel, gettext, intltool, perl(XML::Parser)

Requires:	xfce4-panel
Provides:	verve-plugin = %{version}
# Retire xfce4-minicmd-plugin
Provides:	xfce4-minicmd-plugin = 0.4-9
Obsoletes:	xfce4-minicmd-plugin =< 0.4-8.fc9


%description
This plugin is like the (quite old) xfce4-minicmd-plugin, except that it ships 
more cool features, such as:
* Command history
* Auto-completion (including command history)
* Open URLs and eMail addresses in your favourite applications
* Focus grabbing via D-BUS (so you can bind a shortcut to it)
* Custom input field width


%prep
%autosetup

%build
%configure --disable-static --enable-dbus
%make_build

%install
%make_install

rm -f %{buildroot}/%{_libdir}/xfce4/panel/plugins/libverve.la
%find_lang %{name}


%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog THANKS
%{_libdir}/xfce4/panel/plugins/libverve.so
%{_datadir}/xfce4/panel/plugins/*.desktop

%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 27 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-25
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.0.0-20
- Rebuilt (xfce 4.13)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 15 2018 Filipe Rosset <rosset.filipe@gmail.com> - 2.0.0-2
- drop verve-focus binary

* Sun Apr 15 2018 Filipe Rosset <rosset.filipe@gmail.com> - 2.0.0-1
- new upstream version 2.0.0, first GTK+3 release
- drop verve-focus

* Sun Apr 15 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.1.1-1
- new upstream 1.1.1 release

* Sun Feb 11 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.1.0-6
- Spec cleanup / modernization

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 11 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1.1.0-1
- Update to 1.1.0
- Removed upstreamed patch + spec cleanup

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 28 2015 Kevin Fenzi <kevin@scrye.com> 1.0.1-3
- Rebuild for Xfce 4.12

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 1.0.1-2
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Sat Feb 14 2015 Kevin Fenzi <kevin@scrye.com> 1.0.1-1
- Update to 1.0.1. 
- Fix format-security issue. 

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 23 2013 Kevin Fenzi <kevin@scrye.com> 1.0.0-10
- Add patch for aarch64 support. Fixes bug #926794

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 15 2012 Kevin Fenzi <kevin@scrye.com> - 1.0.0-7
- Rebuild for Xfce 4.10(pre2)

* Thu Apr 05 2012 Kevin Fenzi <kevin@scrye.com> - 1.0.0-6
- Rebuild for Xfce 4.10

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 1.0.0-5
- Rebuild against PCRE 8.30

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.0.0-3
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 23 2010 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.6-2
- Rebuild for Xfce 4.6 (Beta 3)

* Thu Nov 27 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.6-1
- Update to 0.3.6
- Remove "verve-plugin" provides because package name now matches upstream

* Thu Jul 10 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.5-6
- Obsolte the xfce4-minicmd-plugin

* Wed Jun 11 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.5-5
- BuildRequire dbus-glib-devel for all releases (#449438)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.3.5-4
- Autorebuild for GCC 4.3

* Sat Aug 25 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.5-3
- Rebuild for BuildID feature
- Update license tag

* Sun Apr 29 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.5-2
- Rebuild for Xfce 4.4.1

* Sat Feb 24 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.5-1
- Update to 0.3.5

* Sat Sep 23 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.4-1
- Initial Fedora Extras version
