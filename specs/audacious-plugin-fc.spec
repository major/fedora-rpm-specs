%global aud_plugin_api %(grep '[ ]*#define[ ]*_AUD_PLUGIN_VERSION[ ]\\+' %{_includedir}/libaudcore/plugin.h 2>/dev/null | sed 's!.*_AUD_PLUGIN_VERSION[ ]*\\([0-9]\\+\\).*!\\1!')
%if 0%{aud_plugin_api} > 0
%global aud_plugin_dep Requires: audacious(plugin-api)%{?_isa} = %{aud_plugin_api}
%endif
%{?aud_plugin_dep}

%global plugindir %(%___build_pre; pkg-config audacious --variable=plugin_dir 2>/dev/null)

Summary: Future Composer input plugin for Audacious
Name: audacious-plugin-fc
Version: 0.8.4
Release: 2%{?dist}
Provides: audacious-plugins-fc = %{version}-%{release}
URL: https://github.com/mschwendt/audacious-plugins-fc
License: GPL-2.0-or-later
Source0: https://github.com/mschwendt/audacious-plugins-fc/releases/download/%{version}/audacious-plugins-fc-%{version}.tar.bz2

BuildRequires: pkgconfig(audacious) >= 3.8
BuildRequires: libfc14audiodecoder-devel
BuildRequires: pkgconfig
BuildRequires: libtool automake
BuildRequires: gcc-c++ make

# for /usr/bin/appstream-util
BuildRequires: libappstream-glib


%description
This is an input plugin for Audacious which can play back Future Composer
music files from AMIGA. Song-length detection and seek are implemented, too.


%prep
# Enforce availability of the audacious(plugin-api) dependency.
%{!?aud_plugin_dep:echo 'No audacious(plugin-api) dependency!' && exit -1}

# just a guard
pkg-config --print-variables audacious | grep ^plugin_dir

%setup -q -n audacious-plugins-fc-%{version}


%build
%configure
make %{?_smp_mflags}


%install
make DESTDIR=${RPM_BUILD_ROOT} install
appstream-util validate-relax --nonet ${RPM_BUILD_ROOT}%{_datadir}/appdata/*.xml


%files
%license COPYING
%doc README
%{plugindir}/Input/fcdecoder.so
#exclude %%{plugindir}/Input/fcdecoder.la
%{_datadir}/appdata/*.xml


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Oct 27 2024 Michael Schwendt <mschwendt@fedoraproject.org> - 0.8.4-1
- update to 0.8.4

* Tue Jul 30 2024 Michael Schwendt <mschwendt@fedoraproject.org> - 0.8.3.8-4
- update URL, merge flatpak build_pre from XMP plugin package

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.3.8-3
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 12 2024 Michael Schwendt <mschwendt@fedoraproject.org> - 0.8.3.8-1
- Update to 0.8.3.8.

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3.6-0.24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3.6-0.23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3.6-0.22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3.6-0.21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3.6-0.20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3.6-0.19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3.6-0.18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3.6-0.17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3.6-0.16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3.6-0.15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3.6-0.14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3.6-0.13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Michael Schwendt <mschwendt@fedoraproject.org> - 0.8.3.6-0.12
- use %%license macro
- add BuildRequires gcc-c++

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3.6-0.12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3.6-0.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Sep  3 2017 Michael Schwendt <mschwendt@fedoraproject.org> - 0.8.3.6-0.10
- Rebuild for libaudcore SONAME bump.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3.6-0.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3.6-0.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3.6-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 22 2016 Michael Schwendt <mschwendt@fedoraproject.org> - 0.8.3.6-0.6
- Patch for Audacious plugin API 48.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3.6-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3.6-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.8.3.6-0.3
- Rebuilt for GCC 5 C++11 ABI change

* Wed Mar  4 2015 Michael Schwendt <mschwendt@fedoraproject.org> - 0.8.3.6-0.2
- Following Fedora Packaging:AppData guidelines and validate the appdata
  file in %%install. No (re)build just for this change.

* Thu Dec 11 2014 Michael Schwendt <mschwendt@fedoraproject.org> - 0.8.3.6-0.1
- Use pkgconfig notation in BuildRequires.
- Preliminary upgrade to the Audacious 3.6-alpha1 API 46 port.

* Wed Dec 10 2014 Michael Schwendt <mschwendt@fedoraproject.org> - 0.7.3.5-1
- Update to 0.7.3.5 release tarball for Audacious 3.5.x.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 12 2014 Michael Schwendt <mschwendt@fedoraproject.org> - 0.7-7
- Install plugin appdata metainfo file.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 27 2014 Michael Schwendt <mschwendt@fedoraproject.org>
- Add a guard for pkg-config based plugin_dir in %%prep

* Sat Mar  1 2014 Michael Schwendt <mschwendt@fedoraproject.org> - 0.7-5
- Run autoreconf -fi to prevent build failure with Rawhide.

* Fri Feb 28 2014 Michael Schwendt <mschwendt@fedoraproject.org> - 0.7-4
- Update aud_plugin_api global to examine api.h header.

* Tue Sep 24 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 0.7-3
- Port to Audacious 3.5 Plugin API version 45.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 16 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 0.7-1
- Update to 0.7.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 18 2012 Michael Schwendt <mschwendt@fedoraproject.org> - 0.6-18
- Rebuild for Audacious 3.3-alpha1 generic plugin API/ABI bump.
- Patch for Audacious 3.3-alpha1 API changes.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jan  2 2012 Michael Schwendt <mschwendt@fedoraproject.org> - 0.6-16
- Rebuild for Audacious 3.2-beta1 generic plugin API/ABI bump.
- Patch for Audacious 3.2-beta1 glib/gtk related header changes.

* Fri Dec 23 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 0.6-15
- Rebuild for Audacious 3.2-alpha1 generic plugin API/ABI bump.
- Patch for Audacious 3.2-alpha1 API changes.

* Wed Oct 26 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 0.6-14
- Rebuild for Audacious 3.1-beta3 generic plugin API/ABI bump.

* Fri Oct 14 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 0.6-13
- Set config defaults, which helps with cleaning up the config file.
- Include missing misc.h for the config database API.
- Port to Audacious 3.1 Preferences API.
- Rebuild for Audacious 3.1-beta1 generic plugin API/ABI bump.

* Fri Sep 16 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 0.6-10
- Depend on audacious(plugin-api)%%{?_isa}.
- Drop %%defattr line.

* Wed Jul  6 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 0.6-9
- Add missing preferences widget config types.

* Mon Jul  4 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 0.6-8
- Rebuild for Audacious 3.0-beta1 generic plugin API/ABI bump.

* Wed Jun 15 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 0.6-7
- Patch for Audacious 3.0-alpha1 GUI API.

* Wed Feb 23 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 0.6-6
- Update the audacious(plugin-api) stuff in the spec file, so the new
  _AUD_PLUGIN_VERSION_MIN is not taken by mistake.
- Merge from 0.6-3.0.1:
- Patch and rebuild for Audacious 2.5-alpha1 generic plugin API bump.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb  4 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 0.6-4
- No build: wait for mass-rebuild in Rawhide.
- Enhance the audacious(plugin-api) stuff in the spec file.

* Thu Jan 27 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 0.6-3
- Require specific audacious(plugin-api) capability.

* Thu Dec  9 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 0.6-2
- Rebuild for Audacious 2.4.2 generic plugin API/ABI bump.

* Sun Aug 22 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 0.6-1
- Update to 0.6 (merged API patches).

* Fri Jul 23 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 0.5.1-4
- Larger patch, also to remove deprecated API usage.

* Wed Jul 21 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 0.5.1-3
- Patch and rebuild for Audacious 2.4 beta1 generic plugin API/ABI bump.

* Thu Jul 15 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 0.5.1-2
- Rebuild for Audacious 2.4 alpha3 generic plugin API/ABI bump.

* Sun Jul 11 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1 (should fix big-endian platforms).

* Sat Jul 10 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 0.5-2
- Display "4 channels".

* Sun Jun 20 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 0.5-1
- Upgrade to 0.5 for libfc14audiodecoder.

* Sat Jun 12 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 0.4-4
- Patch for Audacious 2.4 API changes.

* Sun Jan 17 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 0.4-3
- Rebuild for audacious.pc --libs changes.

* Sat Oct 24 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 0.4-2
- Set empty/unknown initial songtime instead of 0:00.

* Fri Oct 23 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 0.4-1
- Upgrade to 0.4 for Audacious 2.2 InputPlugin API changes.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun  7 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 0.3-4
- Patch for Audacious 2.

* Fri Jun  5 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 0.3-3
- Rebuild for libmowgli SONAME dependency.
- Add audacious-plugins-fc Provides.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct 16 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 0.3-1
- Update to 0.3 for Audacious >= 1.4.0.

* Fri Aug 29 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 0.2-7
- in %%build add work-around for #454364 (libSAD API headers are broken)

* Fri Feb 08 2008 Michael Schwendt <mschwendt@fedoraproject.org>
- rebuilt for GCC 4.3 as requested by Fedora Release Engineering

* Wed Nov 21 2007 Michael Schwendt <mschwendt@fedoraproject.org> - 0.2-5
- patch for new API
- rebuilt for SONAME changes in Audacious 1.4.x

* Tue Aug 21 2007 Michael Schwendt <mschwendt@fedoraproject.org>
- rebuilt

* Thu Aug  2 2007 Michael Schwendt <mschwendt@fedoraproject.org> - 0.2-2
- clarify licence (GPLv2+)

* Thu Mar  8 2007 Michael Schwendt <mschwendt@fedoraproject.org> - 0.2-1
- Upstream update to 0.2 for Audacious >= 1.3.0.

* Thu Jan 18 2007 Michael Schwendt <mschwendt@fedoraproject.org> - 0.1-2
- Initial package submission for Fedora Package Review (#222648).
