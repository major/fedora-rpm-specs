Name:    sugar-artwork
Summary: Artwork for Sugar look-and-feel
Version: 0.121
Release: 5%{?dist}
URL:     http://sugarlabs.org
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
Source0: http://download.sugarlabs.org/sources/sucrose/glucose/%{name}/%{name}-%{version}.tar.xz
Patch0: empy-fix.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: gtk3-devel
BuildRequires: perl-XML-Parser
BuildRequires: python3
BuildRequires: python3-empy
BuildRequires: icon-naming-utils
BuildRequires: xcursorgen
BuildRequires: autoconf automake libtool
Requires: gtk3

# Disable generation of useless debuginfo package, which fails to build, causing an abort
# See https://fedoraproject.org/wiki/Packaging:Debuginfo?rd=Packaging/Debuginfo#Debuginfo_packages
%global debug_package %{nil}


%description
sugar-artwork contains the themes and icons that make up the Sugar default
look and feel.

%prep
%autosetup -p1

%build
autoreconf -vif
%configure --without-gtk2
%make_build

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete

%post
touch --no-create %{_datadir}/icons/sugar || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/sugar || :

%postun
touch --no-create %{_datadir}/icons/sugar || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/sugar || :

%files
%license COPYING
%{_datadir}/icons/sugar
%{_datadir}/icons/sugar-lh

#gtk3
%{_datadir}/themes/sugar-100/gtk-3.0/gtk.css
%{_datadir}/themes/sugar-100/gtk-3.0/gtk-widgets.css
%{_datadir}/themes/sugar-100/gtk-3.0/settings.ini
%{_datadir}/themes/sugar-100/gtk-3.0/assets/*
%{_datadir}/themes/sugar-100/gtk-3.20/gtk.css
%{_datadir}/themes/sugar-100/gtk-3.20/gtk-widgets.css
%{_datadir}/themes/sugar-100/gtk-3.20/assets/*
%{_datadir}/themes/sugar-72/gtk-3.0/gtk.css
%{_datadir}/themes/sugar-72/gtk-3.0/gtk-widgets.css
%{_datadir}/themes/sugar-72/gtk-3.0/settings.ini
%{_datadir}/themes/sugar-72/gtk-3.0/assets/*
%{_datadir}/themes/sugar-72/gtk-3.20/gtk.css
%{_datadir}/themes/sugar-72/gtk-3.20/gtk-widgets.css
%{_datadir}/themes/sugar-72/gtk-3.20/assets/*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.121-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 27 2024 Ibiam Chihurumnaya <ibiam@sugarlabs.org> - 0.121-4
- Apply empy-fix patch

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.121-3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.121-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Feb 07 2024 Ibiam Chihurumnaya <ibiam@sugarlabs.org> - 0.121-1
- Update to 0.121 release

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.120-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.120-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.120-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Oct 21 2022 Ibiam Chihurumnaya <ibiam@sugarlabs.org> - 0.120-1
- Update to 0.120 release

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.119-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri May 27 2022 Ibiam Chihurumnaya <ibiam@sugarlabs.org> - 0.119-1
- Change release

* Fri May 27 2022 Ibiam Chihurumnaya <ibiam@sugarlabs.org> - 0.119-1
- New Release 0.119

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.118-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.118-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Feb 7 2021 Alex Perez <aperez@sugarlabs.org> - 0.118-1
- New release 0.118

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.116-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Adam Jackson <ajax@redhat.com> - 0.116-4
- BuildRequires: xcursorgen, not xorg-x11-apps

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.116-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Peter Robinson <pbrobinson@fedoraproject.org> 0.116-2
- Move gtk2 theme to a sub package

* Sat Nov 16 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.116-1
- Update to 0.116 release

* Wed Aug 28 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.114-1
- Update to 0.114 release

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.113-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.113
- Update to sugar 0.113 release

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.112-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 28 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.112-1
- Upgrade to sugar 0.112 stable release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.110.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.110.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.110.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan  9 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.110.0-1
- Upgrade to sugar 0.110.0 stable release

* Sun Mar  6 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.108.1-1
- Sugar 0.108.1 stable release

* Fri Feb 19 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.108.0-2
- Add patch for gtk3.20 theme changes

* Sat Feb 13 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.108.0-1
- Sugar 0.108.0 stable release

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.107.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.107.2-1
- Sugar 0.107.2 devel release

* Mon Jan 4  2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.107.1-1
- Sugar 0.107.1 devel release

* Fri Nov 27 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.107.0-1
- Sugar 0.107.0 devel release

* Tue Jul  7 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.106.0-1
- Sugar 0.106.0 stable release

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.105.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.105.2-1
- Sugar 0.105.2 development release

* Tue May 19 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.105.1-1
- Sugar 0.105.1 development release

* Tue Mar 10 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.104.1-1
- Sugar 0.104.1 stable release

* Sat Feb 14 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.104.0-1
- Sugar 0.104.0 stable release

* Sat Jan 17 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.103.2-1
- New upstream 0.103.2 development release

* Thu Dec 11 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.103.1-1
- New upstream 0.103.1 development release

* Thu Nov 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.103.0-1
- New upstream 0.103.0 development release

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.102.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul  2 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.102.0-1
- Sugar 0.102.0 stable release

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.101.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.101.4-1
- 0.101.4 devel release

* Sun Mar  9 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.101.3-1
- 0.101.3 devel release

* Sat Feb 15 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.101.2-1
- 0.101.2 devel release

* Sun Dec  8 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.101.0-1
- 0.101.0 devel release

* Fri Nov  1 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.100.0-1
- Sugar 0.100.0 stable release

* Tue Oct 8  2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.99.2-1
- 0.99.2 devel release
- Changes license to Apache 2.0

* Wed Jul 31 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.99.1-1
- 0.99.1 devel release

* Fri Jun 28 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.99.0-1
- 0.99.0 devel release
- Trim changelog

* Fri May 24 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.85.5-1
- Sugar 0.98.5 stable release

* Sat Feb 16 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.4-1
- Sugar 0.98.4 stable release

* Thu Jan 24 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.3-1
- Sugar 0.98.3 stable release

* Tue Dec 18 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.2-1
- Sugar 0.98.2 stable release

* Mon Dec 10 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.1-1
- Sugar 0.98.1 stable release

* Thu Nov 29 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.0-1
- Sugar 0.98.0 stable release

* Tue Nov 27 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.12-1
- 0.97.12 devel release

* Sat Nov 24 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.11-1
- 0.97.11 devel release

* Sat Nov 10 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.10-1
- 0.97.10 devel release

* Wed Nov  7 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.9-1
- 0.97.9 devel release

* Thu Oct 25 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.8-1
- 0.97.8 devel release

* Tue Oct 16 2012 Daniel Drake <dsd@laptop.org> 0.97.7-1
- 0.97.7 devel release

* Thu Oct 11 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.6-1
- 0.97.6 devel release

* Fri Oct  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.97.5-1
- 0.97.5 devel release

* Wed Sep 26 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.97.4-1
- 0.97.4 devel release

* Thu Sep 20 2012 Daniel Drake <dsd@laptop.org> - 0.97.3-1
- Ne development release

* Thu Sep 13 2012 Daniel Drake <dsd@laptop.org> - 0.97.2-1
- New development release

* Tue Aug 28 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.97.1-1
- 0.97.2 devel release

* Wed Aug 15 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.97.0-1
- 0.97.0 devel release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 25 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.4-1
- 0.96.4 stable release

* Sat Jun  2 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.3-1
- 0.96.3 stable release

* Sat May  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.2-1
- 0.96.2 stable release

* Mon Apr 30 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.1-1
- 0.96.1 stable release

* Tue Apr 24 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.0-1
- 0.96.0 stable release

* Thu Apr 19 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.5-1
- devel release 0.95.5

* Fri Mar 23 2012 Simon Schampijer <simon@laptop.org> - 0.95.4-1
- devel release 0.95.4

* Wed Mar 14 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.3-1
- devel release 0.95.3

* Mon Feb  6 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.2-3
- Update 0.95.2 tarball

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 22 2011 Simon Schampijer <simon@laptop.org> - 0.95.2-1
- include the gtk3 theme

* Tue Oct 25 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.1-1
- devel release 0.95.1
