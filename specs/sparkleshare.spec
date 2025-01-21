# https://docs.fedoraproject.org/en-US/packaging-guidelines/Mono/#_empty_debuginfo
%global debug_package %{nil}

Name:           sparkleshare
Version:        3.38
Release:        5%{?dist}
Summary:        Share and collaborate by syncing with any Git repository instantly

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://www.sparkleshare.org/
Source0:        https://github.com/hbons/SparkleShare/archive/%{version}/SparkleShare-%{version}.tar.gz

BuildRequires:  pkgconfig(mono)
BuildRequires:  pkgconfig(appindicator-sharp-0.1)
BuildRequires:  pkgconfig(gapi-3.0)
BuildRequires:  pkgconfig(gtk-sharp-3.0)
BuildRequires:  pkgconfig(notify-sharp-3.0)
BuildRequires:  pkgconfig(soup-sharp-2.4)
BuildRequires:  pkgconfig(webkit2-sharp-4.0)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  meson
Requires:       curl
Requires:       git >= 1.7.12
Requires:       git-lfs
Requires:       gvfs

ExclusiveArch:  %{mono_arches}
ExcludeArch: %{ix86}

%description
SparkleShare creates a special folder on your computer. You can add remotely
hosted folders (or "projects") to this folder. These projects will be
automatically kept in sync with both the host and all of your peers when someone
adds, removes or edits a file.


%prep
%autosetup -p1 -n SparkleShare-%{version}
# Disable post-install script
sed -i "/meson.add_install_script('scripts\/post-install.sh')/d" meson.build
# Fix bash shebang
sed -i "1!b;s/env bash/bash/" SparkleShare/Linux/sparkleshare.in

%build
%meson
%meson_build

%install
%meson_install

desktop-file-validate %{buildroot}/%{_datadir}/applications/org.sparkleshare.SparkleShare.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/org.sparkleshare.SparkleShare.appdata.xml

%files
%doc README.md RELEASE_NOTES.txt
%license LICENSE.md LICENSE_Sparkles.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/org.sparkleshare.SparkleShare.Invites.desktop
%{_datadir}/applications/org.sparkleshare.SparkleShare.desktop
%{_datadir}/applications/SparkleShare.Autostart.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/symbolic/apps/*.svg
%{_metainfodir}/org.sparkleshare.SparkleShare.appdata.xml

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.38-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 3.38-4
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Aug 12 2023 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 3.38-1
- Release 3.38 (#2227570) and dropping i686 support

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.28-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.28-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.28-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.28-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 05 2021 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 3.28-5
- Fix AppStream metadata validation

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 14 19:32:51 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 3.28-1
- Release 3.28 (#1731619, #1736694)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5.0-2
- Remove obsolete scriptlets

* Sun Sep 24 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.5.0-1
- Update to 1.5.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-7
- mono rebuild for aarch64 support

* Mon Jun 06 2016 Nikos Roussos <comzeradd@fedoraproject.org> 1.2.0-6
- Fix mcs path

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 6 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> 1.2.0-4
- Another fix for mono4

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.0-2
- Rebuild (mono4)

* Tue Sep 23 2014 Nikos Roussos <comzeradd@fedoraproject.org> 1.2.0-1
- Update to 1.2.0

* Thu Sep 19 2013 Nikos Roussos <comzeradd@fedoraproject.org> 1.1.0-3
- Add appdata file.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 26 2013 Nikos Roussos <comzeradd@fedoraproject.org> 1.1.0-1
- Update to 1.1.0

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 10 2012 Nikos Roussos <comzeradd@fedoraproject.org> 1.0.0-1
- Update to 1.0.9

* Mon Dec 03 2012 Nikos Roussos <comzeradd@fedoraproject.org> 0.9.9-1
- Update to 0.9.9

* Tue Nov 20 2012 Nikos Roussos <comzeradd@fedoraproject.org> 0.9.8-1
- Update to 0.9.8

* Wed Nov 07 2012 Nikos Roussos <comzeradd@fedoraproject.org> 0.9.6-1
- Update to 0.9.6

* Sat Oct 20 2012 Nikos Roussos <comzeradd@fedoraproject.org> 0.9.4-1
- Update to 0.9.4

* Sun Sep 30 2012 Nikos Roussos <comzeradd@fedoraproject.org> 0.9.3-1
- Update to 0.9.3

* Sun Sep 02 2012 Nikos Roussos <comzeradd@fedoraproject.org> 0.9.2-1
- Update to 0.9.2

* Tue Aug 28 2012 Nikos Roussos <comzeradd@fedoraproject.org> 0.9.1-1
- Update to 0.9.1

* Thu Jul 05 2012 Nikos Roussos <comzeradd@fedoraproject.org> 0.9.0-1
- Update to 0.9.0

* Wed Mar 21 2012 Nikos Roussos <comzeradd@fedoraproject.org> 0.8.4-2
- Patch to comment the misplaced update-desktop-database

* Mon Mar 19 2012 Nikos Roussos <comzeradd@fedoraproject.org> 0.8.4-1
- Update to 0.8.4

* Mon Mar 12 2012 Nikos Roussos <comzeradd@fedoraproject.org> 0.8.3-1
- Update to 0.8.3

* Fri Mar 02 2012 Dan Horák <dan[at]danny.cz> 0.8.0-4
- set ExclusiveArch

* Thu Mar 01 2012 Nikos Roussos <comzeradd@fedoraproject.org> 0.8.0-3
- added nautilus-python as dependency

* Tue Feb 14 2012 Nikos Roussos <comzeradd@fedoraproject.org> 0.8.0-2
- gettext added as buildrequirement, permissions error fixes

* Wed Feb 01 2012 Nikos Roussos <comzeradd@fedoraproject.org> 0.8.0-1
- Update to 0.8.0

* Wed Jun 29 2011 fedora@alexhudson.com - 0.2.4-1
- rebuilt for new upstrema 0.2.4

* Wed Jun 15 2011 Alex Hudson <fedora@alexhudson.com> - 0.2.2-1
- rebuilt for new upstream 0.2.2

* Wed Jun 08 2011 Alex Hudson <fedora@alexhudson.com> - 0.2.1-1
- rebuilt for new upstream 0.2.1

* Tue Jun 07 2011 Alex Hudson - 0.2.0-1
- initial release of 0.2!

* Sat May 21 2011 Alex Hudson <fedora@alexhudson.com> - 0.2.beta2rc2-3
- remove nautilus extension for now; causes segfaults in F15 :(

* Fri May 20 2011 Alex Hudson <fedora@alexhudson.com> - 0.2.beta2rc2-2
- rebuilt to address python errors in F15

* Fri Mar 25 2011 Alex Hudson - 0.2.beta2rc1-1
- Initial build of 0.2rc1

* Mon Nov 22 2010 Alex Hudson - 0.2.beta1-7
- rebuilt

* Sat Nov 20 2010 Alex Hudson - 0.2.beta1-3
- rebuilt

* Thu Sep 02 2010 Alex Hudson - 0.2.alpha2-5
- update from git; now includes end-user help

* Tue Aug 17 2010 Alex Hudson - 0.2.alpha2-4
- now includes man page and new icons

* Mon Aug 16 2010 Alex Hudson - 0.2.alpha2-3
- slightly cleaner wrt. rpmlint

* Sat Aug 07 2010 Alex Hudson - 0.2.alpha1-2
- various fixes from git post-alpha release

* Tue Aug 03 2010 Alex Hudson - 0.2.alpha1-1
- Initial release of the 0.2alpha series of SparkleShare
