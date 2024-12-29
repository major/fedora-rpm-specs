Name:      schismtracker
Version:   20241226
Release:   1%{?dist}
Summary:   Sound module composer/player
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:   GPL-2.0-only
URL:       http://schismtracker.org/
Source0:   https://github.com/schismtracker/schismtracker/archive/%{version}.tar.gz
Excludearch:   s390x
Requires:      hicolor-icon-theme
BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: perl-open
BuildRequires: SDL2-devel
BuildRequires: desktop-file-utils
BuildRequires: python3
%if 0%{!?_without_x:1}
BuildRequires: libXt-devel
BuildRequires: libXv-devel
%endif
BuildRequires: utf8proc-devel

%description
Schismtracker is a module tracker for the X Window System similar to
the DOS program `Impulse Tracker'. Schismtracker can play/modify various
sound formats such as MOD, S3M, XM, IT, 669 and others.  The user interface
is mostly text-based using SDL for graphical output.

%prep
%setup -q
mkdir auto

%build
autoreconf -i
%configure --disable-dependency-tracking \
%if 0%{?_without_x:1}
--with-x=no \
%endif
;
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

pushd icons
for i in 16 22 24 32 36 48 64 72 96; do
        install -m644 -D schism-icon-${i}.png %{buildroot}/%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done
install -m644 -D schism-icon.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
popd

%files
%doc AUTHORS COPYING NEWS
%{_bindir}/schismtracker
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/schism.desktop
%{_datadir}/pixmaps/schism*.png

%changelog
* Fri Dec 27 2024 josef radinger <cheese@nosuchhost.net> - 20241226-1
- bump version

* Sat Oct 26 2024 josef radinger <cheese@nosuchhost.net> - 20241021-1
- bump version

* Wed Oct 09 2024 josef radinger <cheese@nosuchhost.net> - 20240909-3
- rebuild for utf8proc 2.9.0 (soname bump)

* Tue Oct 01 2024 Jindrich Novy <jnovy@redhat.com> - 20240909-2
- remove duplicate desktop file - prefer upstream one
- Resolves: 2315896

* Sun Sep 15 2024 josef radinger <cheese@nosuchhost.net> - 20240909-1
- bump version
- add BuildRequires on utf8proc-devel

* Mon Aug 12 2024 josef radinger <cheese@nosuchhost.net> - 20240809-1
- bump version

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 20240630-3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20240630-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 8 2024 josef radinger <cheese@nosuchhost.net> - 20240630-1
- bump version

* Tue Jun 18 2024 josef radinger <cheese@nosuchhost.net> - 20240614-1
- bump version

* Mon Jun 10 2024 josef radinger <cheese@nosuchhost.net> - 20240609-1
- bump version
- add perl-open to build-requires

* Fri Jun 07 2024 josef radinger <cheese@nosuchhost.net> - 20240529-1
- bump version

* Mon May 27 2024 josef radinger <cheese@nosuchhost.net> - 20240523-1
- bump version

* Fri May 17 2024 josef radinger <cheese@nosuchhost.net> - 20240515-1
- bump version

* Mon May 13 2024 josef radinger <cheese@nosuchhost.net> - 20240503-1
- bump version

* Wed Apr 10 2024 josef radinger <cheese@nosuchhost.net> - 20240409-1
- bump version

* Thu Apr 04 2024 josef radinger <cheese@nosuchhost.net> - 20240328-1
- bump version

* Tue Mar 12 2024 josef radinger <cheese@nosuchhost.net> - 20240308-1
- bump version

* Fri Mar 08 2024 josef radinger <cheese@nosuchhost.net> - 20240129-1
- bump version

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20231029-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Oct 30 2023 josef radinger <cheese@nosuchhost.net> - 20231029-1
- bump version

* Sun Sep 10 2023 josef radinger <cheese@nosuchhost.net> - 20230906-1
- bump version

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20221201-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20221201-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 28 2022 josef radinger <cheese@nosuchhost.net> - 20221201-1
- bump version

* Tue Oct 25 2022 josef radinger <cheese@nosuchhost.net> - 20221020-1
- bump version

* Mon Sep 19 2022 Jindrich Novy <jnovy@redhat.com> - 20220905-2
- upload new source and remove training spaces

* Thu Sep 08 2022 josef radinger <cheese@nosuchhost.net> - 20220905-1
- bump version
- buildrequires on SDL2-devel
- cleanup

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20200412-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20200412-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20200412-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20200412-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 09 2020 Petr Viktorin <pviktori@redhat.com> - 20200412-4
- Switch BuildRequires to python3

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20200412-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Jindrich Novy <jnovy@redhat.com> - 20200412-2
- exclude s390x arch as windres can't recognize it

* Fri Jul 17 2020 Jindrich Novy <jnovy@redhat.com> - 20200412-1
- update to
  https://github.com/schismtracker/schismtracker/releases/tag/20200412

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20190805-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 24 2019 Jindrich Novy <jnovy@redhat.com> - 20190805-2
- add auto dir to fix build

* Tue Sep 24 2019 Jindrich Novy <jnovy@redhat.com> - 20190805-1
- update to 20190805 (#1736645)
- upstream changed to github
- forwardport spec to new build
- remove legacy bits

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20120105-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20120105-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20120105-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 20120105-15
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20120105-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 20120105-13
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20120105-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20120105-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20120105-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20120105-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120105-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120105-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120105-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120105-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 25 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 20120105-4
- remove --vendor from desktop-file-install for F19+ https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120105-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120105-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Feb 18 2012 Jindrich Novy <jnovy@redhat.com> 20120105-1
- update to 20120105

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110101-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Jindrich Novy <jnovy@redhat.com> 20110101-1
- update to the latest upstream

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100101-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb 18 2010 Jindrich Novy <jnovy@redhat.com> 20100101-1
- update to the latest upstream
- link with -ldl (#564956)

* Sat Nov 07 2009 Jindrich Novy <jnovy@redhat.com> 20090817-1
- update to the latest upstream

* Wed Sep 23 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.5-0.10.rc1
- Update desktop file according to F-12 FedoraStudio feature

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-0.9.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-0.8.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 25 2008 Jindrich Novy <jnovy@redhat.com> 0.5-0.7.rc1
- manual rebuild because of gcc-4.3 (#434193)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.5-0.6.rc1
- Autorebuild for GCC 4.3

* Wed May 09 2007 Jindrich Novy <jnovy@fedoraproject.org> 0.5-0.5.rc1
- update License
- rebuild for BuildID

* Wed May 09 2007 Jindrich Novy <jnovy@fedoraproject.org> 0.5-0.4.rc1
- bump release to avoid EVR problems with FC-5/FC-6

* Fri May 04 2007 Jindrich Novy <jnovy@fedoraproject.org> 0.5-0.3.rc1
- add X dependencies (#238824), thanks to Ville Skyttä
- tune the .desktop file yet more

* Fri May 04 2007 Jindrich Novy <jnovy@fedoraproject.org> 0.5-0.2.rc1
- update GTK icon caches in %%post, %%postun
- remove unneeded dependencies
- update .desktop file

* Wed May 02 2007 Jindrich Novy <jnovy@fedoraproject.org> 0.5-0.1rc1
- package schismtracker
