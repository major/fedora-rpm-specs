
%define snap 20120723

Name:           kpartsplugin
Version:        0.0.1
Release:        0.35.%{snap}%{?dist}
Summary:        KParts technology to embed file viewers into non-KDE browsers

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://kde-apps.org/content/show.php?content=125066
Source0:        http://www.unix-ag.uni-kl.de/~fischer/%{name}/%{name}-%{snap}.tar.bz2

BuildRequires:  kdelibs4-devel
BuildRequires: make

Requires:       kde-runtime%{?_kde4_version: >= %{_kde4_version}}
# for directory ownership
Requires:	mozilla-filesystem


%description
This software implements a plug-in for Netscape-compatible browsers in a Unix 
environment. This plug-in uses KDE's KParts technology to embed file viewers 
(e.g. for PDF files) into non-KDE browsers. Tested browsers include both 
Mozilla Firefox and Opera.
With this plug-in, you can e.g. view PDF files in Firefox using Okular as an 
embedded plug-in.


%prep
%setup -q -n %{name}-%{snap}


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} \
  -DNSPLUGIN_INSTALL_DIR:PATH="%{_libdir}/mozilla/plugins" \
   ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast -C %{_target_platform} DESTDIR=%{buildroot}


%files 
%doc ChangeLog README.txt
%{_libdir}/mozilla/plugins/libkpartsplugin.so
%{_kde4_libdir}/kde4/kcm_kpartsplugin.so
%{_kde4_datadir}/kde4/services/kcm_kpartsplugin.desktop


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.35.20120723
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.0.1-0.34.20120723
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.33.20120723
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.32.20120723
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.31.20120723
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.30.20120723
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.29.20120723
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.28.20120723
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.27.20120723
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.26.20120723
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.25.20120723
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.24.20120723
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.23.20120723
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.22.20120723
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.21.20120723
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.20.20120723
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.19.20120723
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.18.20120723
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.17.20120723
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.16.20120723
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.15.20120723
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-0.14.20120723
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.0.1-0.13.20120723
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-0.12.20120723
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-0.11.20120723
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 06 2013 Rex Dieter <rdieter@fedoraproject.org> 0.0.1-0.10.20120723
- update to 20120723

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-0.9.20120419
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-0.8.20120419
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-0.7.20120419
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 20 2012 Rex Dieter <rdieter@fedoraproject.org> 0.0.1-0.6.20120419
- update to 20120419

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-0.5.20110606
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 08 2011 Rex Dieter <rdieter@fedoraproject.org> 0.0.1-0.4.20110606
- update to 20110606 
- Various issues with java (#659360)
- BR: gettext (translations)
- Requires: kdebase-runtime (instead of kdebase)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-0.3.20101216
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 02 2011 Thomas Janssen <thomasj@fedoraproject.org> 0.0.1-0.2.20101216
- update to 20101216

* Sun Aug 08 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.0.1-0.2.20100723
- update to 20100723

* Thu Jul 01 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.0.1-0.2.20100629
- kpartsplugin 20100629

* Thu Jun 24 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.0.1-0.2.20100604a
- kpartsplugin 20100604a

* Wed May 26 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.0.1-0.2.20100521
- fixed the installpath

* Fri May 21 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.0.1-0.1.20100521
- Initial Release
