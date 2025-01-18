%define git_head cc6da5b
%define checkout 20081003
%define alphatag %{checkout}git%{git_head}

Name:           echo-icon-theme
Version:        0.3.89.0
Release:        0.43.%{alphatag}%{?dist}
Summary:        Echo icon theme

# Automatically converted from old format: CC-BY-SA - review is highly recommended.
License:        LicenseRef-Callaway-CC-BY-SA
URL:            http://fedoraproject.org/wiki/Artwork/EchoDevelopment
Source0:        %{name}-%{version}.tar.bz2
BuildArch:      noarch
BuildRequires:  icon-naming-utils >= 0.8.7
BuildRequires: make
#BuildRequires:  autoconf automake
Requires(post): gtk2 >= 2.6.0
# The following replacements for gnome-themes don't cover everything.
# Most of Mist (the fallback for echo) was provided by gnome-themes.
# Eventually that should get fixed or echo should be retired.
Requires:       gnome-icon-theme
Requires:       gtk2-engines

%description
This package contains the Echo icon theme.

%prep
%setup -q

%build
%configure

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

touch %{buildroot}%{_datadir}/icons/Echo/icon-theme.cache

%post
touch --no-create %{_datadir}/icons/Echo || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/Echo || :


%files
%doc COPYING ChangeLog AUTHORS
%{_datadir}/icons/Echo
%ghost %{_datadir}/icons/Echo/icon-theme.cache

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.89.0-0.43.20081003gitcc6da5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.89.0-0.42.20081003gitcc6da5b
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.89.0-0.41.20081003gitcc6da5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.89.0-0.40.20081003gitcc6da5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.89.0-0.39.20081003gitcc6da5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.89.0-0.38.20081003gitcc6da5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.89.0-0.37.20081003gitcc6da5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.89.0-0.36.20081003gitcc6da5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.89.0-0.35.20081003gitcc6da5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.89.0-0.34.20081003gitcc6da5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.89.0-0.33.20081003gitcc6da5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Friday Sep 04 2020 Bruno Wolff III <bruno@wolff.to> - 0.3.89.1-0.32.20081003gitcc6da5b
- Mist is provided by gtk2-engines

* Tue Sep 01 2020 Bruno Wolff III <bruno@wolff.to> - 0.3.89.1-0.31.20081003gitcc6da5b
- gnome-themes is retired, hopefully gnome-icon-theme provides enough

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.89.0-0.30.20081003gitcc6da5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.89.0-0.29.20081003gitcc6da5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.89.0-0.28.20081003gitcc6da5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar  7 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 0.3.89.0-0.27.%{checkout}git%{git_head}%{?dist}
- Remove obsolete requirement for %%postun scriptlet

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.89.0-0.26.20081003gitcc6da5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.89.0-0.25.20081003gitcc6da5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.89.0-0.24.20081003gitcc6da5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.89.0-0.23.20081003gitcc6da5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.89.0-0.22.20081003gitcc6da5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.89.0-0.21.20081003gitcc6da5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.89.0-0.20.20081003gitcc6da5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.89.0-0.19.20081003gitcc6da5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.89.0-0.18.20081003gitcc6da5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.89.0-0.17.20081003gitcc6da5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.89.0-0.16.20081003gitcc6da5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.89.0-0.15.20081003gitcc6da5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.89.0-0.14.20081003gitcc6da5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.89.0-0.13.20081003gitcc6da5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.89.0-0.12.20081003gitcc6da5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 06 2008 Martin Sourada <martin.sourada@gmail.com>
- 0.3.89.0-0.11.20081003gitcc6da5b
- New git snapshot

* Thu Sep 11 2008 Martin Sourada <martin.sourada@gmail.com>
- 0.3.89.0-0.10.20080911gita7c752e
- New git snapshot

* Thu Aug 28 2008 Martin Sourada <martin.sourada@gmail.com>
- 0.3.89.0-0.9.20080828git3e5f61d
- New git snapshot

* Sun Aug 03 2008 Martin Sourada <martin.sourada@gmail.com> - 0.3.89.0-0.8.20080803git1c213a2
- New git snapshot
- Fix Release: to follow the Packaging Naming Guidelines
- Require icon-naming-utils >= 0.8.7

* Mon Jul 06 2008 Martin Sourada <martin.sourada@gmail.com> - 0.3.89.0-0.7.git1f550b3
- New git snapshot
- Set license tag to CC-BY-SA

* Sun Jul 06 2008 Martin Sourada <martin.sourada@gmail.com> - 0.3.89.0-0.6.git2e822bf
- New git snapshot

* Sun Jun 29 2008 Martin Sourada <martin.sourada@gmail.com> - 0.3.89.0-0.5.git7ec79f3
- New git snapshot

* Sat Jun 28 2008 Martin Sourada <martin.sourada@gmail.com> - 0.3.89.0-0.4.gitb404252
- New git snapshot

* Mon Jun 23 2008 Martin Sourada <martin.sourada@gmail.com> - 0.3.89.0-0.3.git5d18d86
- New git snapshot

* Fri Jun 20 2008 Martin Sourada <martin.sourada@gmail.com> - 0.3.89.0-0.2.gitd5668098
- New git snapshot

* Sat May 10 2008 Martin Sourada <martin.sourada@gmail.com> - 0.3.89.0-0.1.git51c57605
- New git snapshot
- Introduce Autotools into Echo icon theme
- Use icon-naming-utils to create symlinks
- New icons

* Mon Jan 7 2008 Luya Tshimbalanga <luya@fedoraproject.org> - 0.3.1-2
- Fixes rhbz #244512
- Adds new icons

* Sat Nov 17 2007 Martin Sourada <martin.sourada@gmail.com> - 0.3.1-1
- add missing requires
- new version
- fixes rhbz #333231
- adds new icons

* Thu Oct 04 2007 Martin Sourada <martin.sourada@gmail.com> - 0.3-3.git
- Fix big icons issue

* Wed Oct  3 2007 Matthias Clasenb <mclasen@redhat.com> - 0.3-2.git
- Drop the redhat-artwork dependency  (#309661)

* Tue Oct 02 2007 Luya Tshimbalanga <luya_tfz@thefinalzone.com> - 0.3-1.git
- Newest snapshot
- Included cc-by-sa 3.0 file
- Dropped patch contexts.patch

* Wed Sep 26 2007 Luya Tshimbalanga <luya_tfz@thefinalzone.com> - 0.2.5.20070427wiki
- Updated license to cc-by-sa 3.0

* Mon Jun 04 2007 Luya Tshimbalanga <luya_tfz@thefinalzone.com> - 0.2.4.20070427wiki
- New snapshot

* Mon May 21 2007 Matthias Clasen <mclasen@redhat.com> - 0.2.3.20070419wiki
- Fix context information in index.theme (#217832)

* Thu Apr 19 2007 Matthias Clasen <mclasen@redhat.com> - 0.2.2.20070419wiki
- Drop scalable images again

* Tue Apr 17 2007 Matthias Clasen <mclasen@redhat.com> - 0.2.2.20070417wiki
- New snapshot
- Include scalable images

* Tue Mar 27 2007 Matthias Clasen <mclasen@redhat.com> - 0.2-2.20070326wiki
- Fix n-v-r ordering problem

* Mon Mar 26 2007 Matthias Clasen <mclasen@redhat.com> - 0.2-2.20070326wiki
- New snapshot

* Fri Feb 23 2007 Matthias Clasen <mclasen@redhat.com> - 0.2-2.20070223wiki
- New snapshot
- Fix some scriptlet issues
- Own the icon cache

* Tue Feb  6 2007 Matthias Clasen <mclasen@redhat.com> - 0.2-1.20070206wiki
- New snapshot

* Mon Feb  5 2007 Matthias Clasen <mclasen@redhat.com> - 0.1-7
- Neuter macros in %%changelog

* Thu Oct 26 2006 David Zeuthen <davidz@redhat.com> - 0.1-6
- Make this package own %%{_datadir}/icons/Echo
- Preserve timestamps
- Keep %%build around to document it's intentionally left empty
- Use %%{buildroot} instead of $RPM_BUILD_ROOT

* Thu Oct 26 2006 Luya Tshimbalanga <luya_tfz@thefinalzone.com> - 0.1-5
- Renamed the spec file to respect Packaging Guideline
- Included URL for source
- Cleaned up
- Ajusted permissions
- Removed unneeded build script 

* Wed Oct 25 2006 Luya Tshimbalanga <luya_tfz@thefinalzone.com> - 0.1-2
- Minor fixes

* Mon Oct 23 2006 Christopher Aillon <caillon@redhat.com> - 0.1-1
- Initial RPM.
