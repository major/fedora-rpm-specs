Name:           pokerth
Version:        1.1.2
Release:        31%{?dist}
Summary:        A Texas-Holdem poker game
License:        AGPL-3.0-or-later WITH GPL-3.0-linking-source-exception
URL:            http://www.pokerth.net
Source0:        http://downloads.sourceforge.net/%{name}/pokerth-%{version}.tar.gz

BuildRequires: make
BuildRequires:  desktop-file-utils
BuildRequires:  qt4-devel
BuildRequires:  qtsingleapplication-devel
BuildRequires:  zlib-devel
BuildRequires:  libcurl-devel
BuildRequires:  gnutls-devel
BuildRequires:  boost-devel >= 1.37
BuildRequires:  SDL_mixer-devel
BuildRequires:  libgsasl-devel
BuildRequires:  sqlite-devel
BuildRequires:  libircclient-devel
BuildRequires:  tinyxml-devel
# src/third_party/protobuf/pokerth.pb.h includes google/protobuf/stubs/common.h
BuildRequires:  protobuf-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  gcc-c++
# Removed bundled fonts
Requires:       dejavu-sans-fonts
Requires:       urw-fonts
Patch0:         pokerth-1.1.2.patch
Patch1:         pokerth-1.1.2.patch.2019
Patch2:         396.patch

%description
PokerTH is a poker game written in C++/Qt4. You can play the popular
"Texas Hold'em" poker variant against up to six computer-opponents or
play network games with people all over the world. This poker engine
is available for Linux, Windows, and MacOSX.

%prep
%setup -q -n pokerth-%{version}-rc
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build

%{qmake_qt4} pokerth.pro
make %{?_smp_mflags}
%{qmake_qt4} pokerth_game.pro
make %{?_smp_mflags}


%install
make install INSTALL_ROOT=%{buildroot} COPY="cp -p -f"
# Ugh, binary isn't automatically installed
#install -D -p -m 755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -p -m 755 bin/%{name}_server %{buildroot}%{_bindir}/%{name}_server

# and replace them with symlinks
#ln -s %{_datadir}/fonts/default/Type1/c059013l.pfb %{buildroot}%{_datadir}/%{name}/data/fonts/
#ln -s %{_datadir}/fonts/default/Type1/n019003l.pfb %{buildroot}%{_datadir}/%{name}/data/fonts/
#ln -s %{_datadir}/fonts/dejavu/DejaVuSans-Bold.ttf %{buildroot}%{_datadir}/%{name}/data/fonts/VeraBd.ttf

# Install desktop file
desktop-file-install --remove-category="Qt" --dir=%{buildroot}%{_datadir}/applications %{name}.desktop 

%files
%doc COPYING ChangeLog TODO
%{_bindir}/%{name}
%{_bindir}/%{name}_server
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 1.1.2-27
- Rebuilt for Boost 1.83

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 1.1.2-25
- Rebuilt for Boost 1.81

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 1.1.2-22
- Rebuilt for Boost 1.78

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 06 2021 Adrian Reber <adrian@lisas.de> - 1.1.2-20
- Rebuilt for protobuf 3.19.0

* Tue Oct 26 2021 Adrian Reber <adrian@lisas.de> - 1.1.2-19
- Rebuilt for protobuf 3.18.1

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 1.1.2-18
- Rebuilt for Boost 1.76

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 1.1.2-15
- Rebuilt for Boost 1.75

* Wed Jan 13 16:41:39 CET 2021 Adrian Reber <adrian@lisas.de> - 1.1.2-14
- Rebuilt for protobuf 3.14

* Mon Sep 28 22:57:04 -03 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.1.2-13
- apply patch from archlinux and gentoo to make it build again

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-12
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 1.1.2-10
- Rebuilt for protobuf 3.12

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Orion Poplawski <orion@nwra.com> - 1.1.2-8
- Rebuild for protobuf 3.11

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Jonathan Wakely <jwakely@redhat.com> - 1.1.2-5
- Rebuilt for Boost 1.69

* Wed Nov 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.2-4
- Rebuild for protobuf 3.6

* Sat Jul 14 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.1.2-3
- apply patch from archlinux to make it build again

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.1.2-1
- add gcc-c++ into buildrequires
- 1.1.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 29 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.1.1-28
- Rebuild for protobuf 3.5

* Mon Nov 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.1-27
- Rebuild for protobuf 3.4

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 1.1.1-24
- Rebuilt for s390x binutils bug

* Tue Jul 04 2017 Jonathan Wakely <jwakely@redhat.com> - 1.1.1-23
- Rebuilt for Boost 1.64

* Tue Jun 13 2017 Orion Poplawski <orion@cora.nwra.com> - 1.1.1-22
- Rebuild for protobuf 3.3.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.1.1-20
- Rebuilt for Boost 1.63

* Thu Jan 26 2017 Orion Poplawski <orion@cora.nwra.com> - 1.1.1-19
- Rebuild for protobuf 3.2.0

* Sat Nov 19 2016 Orion Poplawski <orion@cora.nwra.com> - 1.1.1-18
- Rebuild for protobuf 3.1.0

* Thu Jul 21 2016 Jonathan Wakely <jwakely@redhat.com> - 1.1.1-17
- Rebuild to switch back to old sendmsg/recvmsg symbols (#1344830)

* Tue May 17 2016 Jonathan Wakely <jwakely@redhat.com> - 1.1.1-16
- Rebuilt for linker errors in boost (#1331983)

* Fri Feb 19 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 1.1.1-15
- Fix build with Boost >= 1.50 now that CXXFLAGS are respected (#1305225)

* Wed Feb 03 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.1.1-14
- use %%qmake_qt4 macro to ensure proper build flags

* Fri Jan 29 2016 Jonathan Wakely <jwakely@redhat.com> 1.1.1-13
- Patched and rebuilt for GCC 6 and Boost 1.60.0

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.1.1-12
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.1.1-10
- rebuild for Boost 1.58

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 29 2015 Kalev Lember <kalevlember@gmail.com> - 1.1.1-8
- Rebuilt for protobuf soname bump

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 1.1.1-7
- Rebuild for boost 1.57.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Ryan Rix <ry@n.rix.si> - 1.1.1-5
- Re-generate Ville's patch to work with PokerTH 1.1.1

* Fri Jun 13 2014 Ville Skyttä <ville.skytta@iki.fi> - 1.1.1-4
- Use system qtsingleappliaction instead of bundled one

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 1.1.1-2
- Rebuild for boost 1.55.0

* Tue Apr 15 2014 Luke Macken <lmacken@redhat.com> - 1.1.1-1
- Update to 1.1.1 (#949463)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 29 2013 Adam Williamson <awilliam@redhat.com> - 1.0.1-2
- buildrequires libgcrypt-devel

* Sat Jul 27 2013 pmachata@redhat.com
- Rebuild for boost 1.54.0

* Tue Jul 02 2013 Adam Williamson <awilliam@redhat.com> - 1.0.1-1
- new upstream bugfix release 1.0.1
- correct license to 'AGPLv3+ with exceptions'
- re-diff fix-libircclient-include.patch

* Tue Mar 12 2013 Ryan Rix <ry@n.rix.si> - 1.0-2
- Rebuild for protobuf soname bump

* Mon Feb 18 2013 Adam Williamson <awilliam@redhat.com> - 1.0-1
- new release 1.0

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.9.5-6
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.9.5-5
- Rebuild for Boost-1.53.0

* Sun Aug 12 2012 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.9.5-4
- rebuilt for new boost

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 19 2012 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.9.5-2
- add missing BR tinyxml-devel

* Tue Jul 17 2012 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.9.5-1
- new version

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3-13
- Rebuilt for c++ ABI breakage

* Mon Jan 30 2012 Bruno Wolff III <bruno@wolff.to> - 0.8.3-12
- Fix for gcc 4.7

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 26 2011 Bruno Wolff III <bruno@wolff.to> - 0.8.3-10
- Rebuild for boost 1.48 soname bump

* Sun Oct 9 2011 Ryan Rix <ry@n.rix.si> - 0.8.3-9
- Grammar and update to personal specifications
- Apply patch to fix GNUTLS issues from Paul Frields <pfrields at fedoraproject dot org>

* Fri Jul 29 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.8.3-8
- Bump spec due to new gnutls.

* Fri Jul 22 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.8.3-7
- Bump spec due to new boost.

* Tue Apr 26 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.8.3-6
- Bump due to libgnutls update.

* Wed Apr 06 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.8.3-5
- Bump spec due to boost upgrade.

* Sun Feb 20 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.8.3-4
- Fix build against new boost.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 07 2011 Thomas Spura <tomspur@fedoraproject.org> - 0.8.3-2
- rebuild for new boost

* Tue Jan 18 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.8.3-1
- Update to 0.8.3.

* Wed Jan 05 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.8.2-1
- Update to 0.8.2.

* Sun Oct 17 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.8.1-1
- Update to 0.8.1.

* Tue Sep 07 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.8-0.1.beta3
- Upgrade to 0.8 series due to boost incompatibility.

* Mon Aug 02 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.7.1-5
- Bump spec due to boost upgrade.

* Thu Jun 03 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.7.1-4
- Fix FTBFS caused by implicit DSO linking in rawhide.

* Thu Jan 21 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.7.1-3
- Bump spec due to change of boost soname.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 01 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.7.1-1
- Update to upstream 0.7.1.

* Sun Jun 21 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.7-5
- Use bold style instead of book style.

* Sun Jun 21 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.7-4
- Fix BZ #507131.

* Sun Jun 14 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.7-3
- Removed BR: asio-devel.
- Changed BR on boost to >= 1.37.

* Sat Jun 13 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.7-2
- Fix spelling error in font symlink, conserve time stamps.

* Wed May 27 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.7-1
- First release.
