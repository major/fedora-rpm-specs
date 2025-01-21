Name:           xcowsay
Version:        1.6
Release:        8%{?dist}
Summary:        Displays a cute cow and message on your desktop

License:        GPL-3.0-or-later
URL:            http://www.doof.me.uk/xcowsay
Source0:        http://www.nickg.me.uk/files/%{name}-%{version}.tar.gz
Source1:        xcowfortune.desktop
#Patch23:        xcowsay-aarch64.patch



BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gtk3-devel
BuildRequires:  gettext
BuildRequires:  dbus-glib-devel
BuildRequires:  desktop-file-utils
Requires:       fortune-mod

%description
xcowsay displays a cute cow and message on your desktop.
The message can be text or images (with xcowdream)
xcowsay can run in daemon mode for sending
your cow message with DBus.
Inspired by the original cowsay.

%prep
%setup -q
#%patch23 -p1 -b .aarch64
iconv -f iso-8859-1 -t utf-8 NEWS -o NEWS

%build
%configure --enable-dbus
make %{?_smp_mflags} 


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

%find_lang %{name}

desktop-file-install --vendor=""     \
       --dir=%{buildroot}%{_datadir}/applications/   \
       %{SOURCE1}
# xcowfortune is the only .desktop file because the other program 
#(xcowsay, xcowthink and xcowdream) need an argument



%files -f %{name}.lang
%license COPYING
%doc NEWS README AUTHORS ChangeLog 
%{_bindir}/xcowdream
%{_bindir}/xcowfortune
%{_bindir}/xcowsay
%{_bindir}/xcowthink
%{_datadir}/man/man6/xcowsay.6.gz
%{_datadir}/xcowsay/
%{_datadir}/applications/xcowfortune.desktop


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.6-4
- migrated to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jan 25 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.6-1
- 1.6

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 01 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.5.1-1
- 1.5.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 07 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.5-1
- 1.5

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 04 2016 Jon Ciesla <limburgher@gmail.com> - 1.4-1
- 1.4, aarch64 patch no longer needed.

* Mon May 16 2016 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.3-12
- remove useless %%defattr for clarity

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Nov 16 2013 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.3-7
- Fix aarch64 build (#926757)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 10 2011 Jon Ciesla <limb@jcomserv.net> - 1.3-2
- Rebuild for libpng 1.5.

* Wed Jun 22 2011 Jon Ciesla <limb@jcomserv.net> - 1.3-1
- New upstream.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 14 2010 Fabien Georget <fabien.georget@gmail.com> - 1.2-1
- Update to 1.2

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 28 2009 Fabien Georget <fabien.georget@gmail.com> 1.1-1
- change license to GPLv3+
- add /usr/share/xcowsay/ in files
- add dbus-glib-devel in BR for daemon mode of xcowsay
- add fortune-mod in Requires for xcowfortune
- add xcowfortune.desktop

* Mon Mar 30 2009 Fabien Georget <fabien.georget@gmail.com> 1.1-0.1
- Creation
