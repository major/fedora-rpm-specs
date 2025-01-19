%global alt_name GPaste

Name:           gpaste
Version:        45.2
Release:        2%{?dist}
Summary:        Clipboard management system

License:        BSD-2-Clause
URL:            https://github.com/Keruspe/%{alt_name}/
Source0:        https://www.imagination-land.org/files/%{name}/%{alt_name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gcr-4)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnome-keybindings)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  systemd-rpm-macros
BuildRequires:  vala
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%{?systemd_requires}
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%description
GPaste is a clipboard management system.

This package provides the D-Bus service and the command-line client.


%package libs
Summary:        Library to manage the clipboard history

%description libs
GPaste is a clipboard management system.

This package contains the shared library used by GPaste.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.


%package ui
Summary:        Graphical interface for GPaste
Requires:       %{name} = %{version}-%{release}
Requires:       control-center-filesystem
%{?systemd_requires}

%description ui
GPaste is a clipboard management system.

This package provides a graphical interface for GPaste, as well as GNOME
integration (control center key bindings and search provider).


%package -n gnome-shell-extension-%{name}
Summary:        GNOME Shell extension for GPaste
Requires:       gnome-shell
Requires:       %{name}-ui = %{version}-%{release}
BuildArch:      noarch

%description -n gnome-shell-extension-%{name}
GPaste is a clipboard management system.

This package provides the GNOME Shell extension for GPaste.



%package bash-completion
Summary:        Bash completion for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)

%description bash-completion
Bash command line completion support for %{name}.



%package zsh-completion
Summary:        Zsh completion for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       zsh
Supplements:    (%{name} and zsh)

%description zsh-completion
Zsh command line completion support for %{name}.


%prep
%autosetup -n %{alt_name}-%{version}


%build
%meson
%meson_build


%install
%meson_install

install -Dpm 0644 */data/systemd/*.service -t $RPM_BUILD_ROOT%{_userunitdir}/

%find_lang %{alt_name}


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.GPaste.*.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/org.gnome.GPaste.Ui.appdata.xml


%post
%systemd_user_post org.gnome.GPaste.Preferences.service
%systemd_user_post org.gnome.GPaste.Ui.service


%post ui
%systemd_user_post org.gnome.GPaste.Preferences.service
%systemd_user_post org.gnome.GPaste.Ui.service


%preun
%systemd_user_preun org.gnome.GPaste.Preferences.service
%systemd_user_preun org.gnome.GPaste.Ui.service


%preun ui
%systemd_user_preun org.gnome.GPaste.Preferences.service
%systemd_user_preun org.gnome.GPaste.Ui.service


%files
%doc AUTHORS NEWS README.md THANKS
%{_bindir}/%{name}-client
%dir %{_libexecdir}/%{name}/
%{_libexecdir}/%{name}/gpaste-daemon
%{_datadir}/dbus-1/services/org.gnome.GPaste.service
%{_datadir}/glib-2.0/schemas/*.xml
%{_userunitdir}/org.gnome.GPaste.service
%{_mandir}/man1/*.1.*


%files libs -f %{alt_name}.lang
%license COPYING
%{_libdir}/girepository-1.0/%{alt_name}*.typelib
%{_libdir}/lib%{name}*.so.*


%files devel
%{_datadir}/gir-1.0/*.gir
%{_datadir}/vala/vapi/*
%{_includedir}/%{name}-2/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%files ui
%{_libexecdir}/%{name}/%{name}-preferences
%{_libexecdir}/%{name}/%{name}-ui
%{_datadir}/applications/org.gnome.GPaste.*.desktop
%{_datadir}/dbus-1/services/org.gnome.GPaste.*.service
%{_datadir}/gnome-control-center/keybindings/*.xml
%{_datadir}/gnome-shell/search-providers/*.ini
%{_datadir}/metainfo/org.gnome.GPaste.Ui.appdata.xml
%{_userunitdir}/org.gnome.GPaste.Ui.service
%{_userunitdir}/org.gnome.GPaste.Preferences.service


%files -n gnome-shell-extension-%{name}
%{_datadir}/gnome-shell/extensions/GPaste@gnome-shell-extensions.gnome.org/


%files bash-completion
%{_datadir}/bash-completion/completions/%{name}-client


%files zsh-completion
%{_datadir}/zsh/site-functions/_%{name}-client


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 45.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Oct 13 2024 Mohamed El Morabity <melmorabity@fedoraproject.org> - 45.2-1
- Update to 45.2

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 45.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 11 2024 Mohamed El Morabity <melmorabity@fedoraproject.org> - 45.1-1
- Update to 45.1

* Sun Feb 25 2024 Mohamed El Morabity <melmorabity@fedoraproject.org> - 45-4
- Drop support for i686

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 45-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Sep 24 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 45-1
- Update to 45

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 44.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 19 2023 Kalev Lember <klember@redhat.com> - 44.0-2
- Rebuilt for gcr soname bump

* Sun Mar 26 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 44.0-1
- Update to 44.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 43.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jan 07 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 43.1-1
- Update to 43.1
- Switch to SPDX in license tag

* Wed Sep 28 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 43.0-1
- Update to 43.0
- Split shell completion files into separate subpackages

* Thu Aug 04 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 42.1-3
- Fix build dependencies for GNOME 43

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 42.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Mar 22 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 42.1-1
- Update to 42.1

* Sun Mar 20 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 42.0-1
- Update to 42.0

* Sun Feb 27 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.42.6-1
- Update to 3.42.6

* Fri Feb 18 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.42.5-1
- Update to 3.42.5

* Wed Feb 02 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.42.2-3
- Fix build dependencies for GNOME 42

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.42.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 24 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.42.2-1
- Update to 3.42.2

* Sun Oct 31 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.42.1-1
- Update to 3.42.1

* Tue Sep 28 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.42.0-1
- Update to 3.42.0

* Mon Sep 27 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.40.3-1
- Update to 3.40.3

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.40.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.40.2-1
- Update to 3.40.2

* Tue Apr 13 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.40.1-1
- Update to 3.40.1

* Sat Mar 20 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.38.6-1
- Update to 3.38.6

* Mon Feb 15 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.38.5-1
- Update to 3.38.5

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 25 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.38.4-1
- Update to 3.38.4

* Mon Nov 02 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.38.3-1
- Update to 3.38.3

* Mon Oct 05 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.38.2-1
- Update to 3.38.2

* Thu Oct 01 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.38.1-1
- Update to 3.38.1

* Thu Sep 17 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.38.0-1
- Update to 3.38.0

* Thu Aug 13 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.36.3-4
- Fix mutter 7 detection

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Mar 28 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.36.3-1
- Update to 3.36.3

* Thu Mar 19 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.36.2-1
- Update to 3.36.2

* Mon Mar 09 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.36.0-1
- Update to 3.36.0

* Fri Feb 07 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.34.1-3
- Fix build with mutter >= 3.35

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 09 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.34.1-1
- Update to 3.34.1

* Tue Sep 10 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.34.0-1
- Update to 3.34

* Mon Sep 02 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.32.1-0.1.20190828gitc3746b9
- Update to a newer snapshot (GNOME 3.34 support)
- Switch to meson

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 13 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.32.0-1
- Update to 3.32.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.30.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 17 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.30.2-1
- Update to 3.30.2

* Sun Sep 09 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.30.1-1
- Update to 3.30.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 16 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.28.2-1
- Update to 3.28.2

* Tue Mar 27 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.28.1-1
- Update to 3.28.1

* Tue Mar 13 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.28.0-1
- Update to 3.28.0

* Thu Mar 08 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.26.2-1
- Update to 3.26.2
- Spec cleanup
- Fix AppData installation path

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 28 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.26.0-1
- Update to 3.26.0

* Tue Sep 19 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.24.3-1
- Update to 3.24.3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild
-
* Sat May 20 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.24.2-1
- Update to 3.24.2

* Sat Apr 08 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.24.1-1
- Update to 3.24.1

* Mon Mar 20 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.23.90-1
- Update to 3.23.90
- Remove applet subpackage (GPaste applet has been removed)

* Tue Feb 28 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.22.3-1
- Update to 3.22.3

* Fri Feb 17 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.22.2-1
- Update to 3.22.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 02 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.22.1-1
- Update to 3.22.1

* Sat Oct 08 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.22.0-2
- Remove no longer needed dependency on gnome-icon-theme-legacy for gpaste-ui

* Sat Oct 08 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.22.0-1
- Update to 3.22.0

* Sun Sep 18 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.21.91-1
- Update to 3.21.91

* Mon Sep 12 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.21.90-1
- Update to 3.21.90

* Tue Jun 28 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.20.4-1
- Update to 3.20.4

* Fri Jun 24 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.20.3-2
- Fix GNOME Shell minimal version for the GPaste extension

* Fri Jun 24 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.20.3-1
- Update to 3.20.3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.18.3-1
- Update to 3.18.3

* Fri Oct 16 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.18.2-1
- Update to 3.18.2

* Sun Sep 27 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.18.1.1-2
- Fix minimal GNOME Shell version for the extension subpackage

* Sun Sep 27 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.18.1.1-1
- Update to 3.18.1.1

* Wed Sep 16 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.16.3-1
- Update to 3.16.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 25 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.16.2.1-1
- Update to 3.16.2.1

* Sun May 03 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.16.1-1
- Update to 3.16.1

* Sun Apr 05 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.16-1
- Update to 3.16

* Sun Apr 05 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.14.3-1
- Update to 3.14.3

* Mon Mar 16 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.14.2-1
- Update to 3.14.2

* Sun Jan 18 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.14.1-1
- Update to 3.14.1

* Sat Oct 11 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.14-1
- Update to 3.14

* Tue Oct 07 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.13-0.2.20140929git80428a8
- Update to a newer snapshot (GNOME 3.14 support)

* Wed Sep 24 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.13-0.1.20140917git8dae0be
- Update to a newer snapshot (GNOME 3.13.92 support)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.1-2
- Rebuilt for gobject-introspection 1.41.4

* Wed Jul 16 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.12.1-1
- Update to 3.12.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 02 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.12-1
- Update to 3.12

* Thu May 01 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.10.1-1
- Update to 3.10.1
- Drop gnome-shell dependency

* Wed Apr 02 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.10-2
- Add gnome-shell as dependency (the gpasted daemon requires the GNOME Shell
  GSetting schemas)

* Tue Mar 25 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.10-1
- Update to 3.10

* Wed Feb 12 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.8-1
- Update to 3.8

* Thu Oct 17 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.6-1
- Update to 3.6

* Wed Sep 25 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.5-1
- Update to 3.5

* Mon Sep 23 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.5-0.2.20130922gitf124a2f
- Update to a newer snapshot

* Wed Sep 18 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.5-0.1.20130918git6ab4033
- Update to a newer snapshot

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 02 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.0.2-1
- Update to 3.0.2

* Fri May 10 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.0.1-2
- Fix bash completion

* Fri May 10 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.0.1-1
- Update to 3.0.1

* Sun Apr 07 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.99.2-3.20130331gitc93a4ac
- Add missing BuildRequires on pkgconfig(gnome-keybindings)

* Sun Apr 07 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.99.2-2.20130331gitc93a4ac
- Update to a newer snapshot
- Move bash completion script to /usr/share/bash-completion/completion/

* Mon Jan 28 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.99.2-1
- Update to 2.99.2
- Drop patch gpaste-2.99.1-fix_gpaste-settings

* Thu Jan 17 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.99.1-1
- Update to 2.99.1

* Sun Dec 30 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.9.1-1
- Update to 2.9.1
- Drop patch gpaste-2.9-gir.patch, fixed upstream

* Sun Sep 30 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.9-1
- Update to 2.9
- Enable GNOME fallback applet

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May 19 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.8.1-1
- Update to 2.8.1

* Thu May 03 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.8-1
- Update to 2.8

* Sun Apr 08 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.5-2
- Fix Group and Requires tags in subpackages

* Fri Mar 30 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.5-1
- Update to 2.5

* Sat Jan 07 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.2.1-1
- Update to 2.2.1

* Fri Dec 09 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.1-1
- Update to 2.1

* Tue Nov 29 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.0-1
- Update to 2.0

* Sun Sep 25 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.6-1
- Update to 1.6
- Remove no longer needed gpaste-1.5-DOS.patch patch

* Wed Sep 14 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.5-1
- Update to 1.5
- Remove gpaste-1.3-remove_applet_refs.patch patch (there is no more reference
  to the GNOME 2 applet in documentation and completion files)
- Add gpaste-1.5-DSO.patch to fix DSO linking

* Sat Sep 03 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.3-1
- Update to 1.3

* Sun Jul 10 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.2-1
- Update to 1.2

* Sat Jun 25 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.99-1.17dd47git
- Initial RPM release
