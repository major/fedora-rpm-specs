Name:           mine_detector
Version:        6.0^20160527
# The version numbering upstream is inconsistent and useless. Here the date of
# the newest source file in the zip file is used to identify the version
Release:        5%{?dist}
Summary:        Mine Detector, a mine-finding game
Summary(sv):    Mine Detector, ett minröjningsspel

License:        GPL-2.0-only
URL:            https://pragmada.x10hosting.com/mindet.html
Source:         https://pragmada.x10hosting.com/MD_1.0-GTK3.zip
Source2:        mine_detector.gpr
Source3:        mine_detector.desktop
# The license file was left out from the zipfile by mistake. Source4 corrects
# this mistake. Sources 5 and 6 clarify the situation.
Source4:        mine_detector-license.txt
Source5:        mine_detector-README.Fedora
Source6:        mine_detector-license_clarification.mbox
# manual page stub:
Source7:        mine_detector.1.en
Source8:        mine_detector.1.sv

BuildRequires:  gcc-gnat GtkAda3-devel desktop-file-utils
BuildRequires:  gprbuild
BuildRequires:  fedora-gnat-project-common
# Build only on architectures where GPRbuild is available:
ExclusiveArch:  %{GPRbuild_arches}

%description
Mine Detector is a mine-finding game with somewhat different rules from other
mine-finding games. Mine Detector rarely requires guessing. Only at the higher
levels may guessing sometimes be the only way to win.

%description -l sv
Mine Detector är ett minröjningsspel med litet annorlunda regler än andra
minröjningsspel. I Mine Detector är det sällan nödvändigt att gissa. Det är
bara på de högre nivåerna som en gissning ibland kan vara det enda sättet att
vinna.


# Disable the hardening hack until someone figures out how to make it work for
# Ada. This game doesn't read any input anyway.
# https://bugzilla.redhat.com/show_bug.cgi?id=1197501
%undefine _hardened_build


%prep
%autosetup -c
# -c because there's no top-level directory in the zip file.
cp -p %{SOURCE2} .
cp -p %{SOURCE4} license.txt
cp -p %{SOURCE5} README.Fedora
cp -p %{SOURCE6} license_clarification.mbox


%build
gprbuild -P mine_detector.gpr %{GPRbuild_flags}


%install
mkdir --parents %{buildroot}%{_bindir} \
                %{buildroot}%{_mandir}/man1 %{buildroot}%{_mandir}/sv/man1
cp -p mine_detector %{buildroot}%{_bindir}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE3}
cp -p %{SOURCE7} %{buildroot}%{_mandir}/man1/mine_detector.1
cp -p %{SOURCE8} %{buildroot}%{_mandir}/sv/man1/mine_detector.1


%files
%license license.txt
%license README.Fedora
%license license_clarification.mbox
%{_bindir}/*
%{_datadir}/applications/*
%{_mandir}/man1/*
%{_mandir}/sv/man1/*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.0^20160527-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 14 2025 Björn Persson <Bjorn@Rombobjörn.se> - 6.0^20160527-4
- Rebuilt with GCC 15 prerelease.

* Thu Dec 05 2024 Björn Persson <Bjorn@Rombobjörn.se> - 6.0^20160527-3
- Rebuilt with GTKada 25.

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0^20160527-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 19 2024 Björn Persson <Bjorn@Rombobjörn.se> - 6.0^20160527-1
- Switched to a version of Mine Detector that uses GTK+ 3.

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Björn Persson <Bjorn@Rombobjörn.se> - 6.0-47
- Rebuilt with GCC 14 prerelease.

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Björn Persson <Bjorn@Rombobjörn.se> - 6.0-44
- Rebuilt with GCC 13.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 08 2020 Björn Persson <Bjorn@Rombobjörn.se> - 6.0-39
- Rebuilt with GCC 11.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Björn Persson <Bjorn@Rombobjörn.se> - 6.0-32
- Switched to building with GPRbuild as project file support was removed from
  Gnatmake in GCC 8.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 04 2017 Björn Persson <Bjorn@Rombobjörn.se> - 6.0-28
- Rebuilt with GCC 7 prerelease.

* Fri Aug 12 2016 Björn Persson <Bjorn@Rombobjörn.se> - 6.0-27
- Rebuilt to let it be built on new architectures.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 31 2016 Björn Persson <Bjorn@Rombobjörn.se> - 6.0-25
- Rebuilt with GCC 6 prerelease.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 01 2015 Björn Persson <bjorn@rombobjörn.se> - 6.0-23
- Tagged the license files as such.

* Sat Feb 07 2015 Björn Persson <bjorn@rombobjörn.se> - 6.0-22
- Rebuilt with GCC 5.0.0.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 10 2014 Björn Persson <bjorn@rombobjörn.se> - 6.0-19
- Rebuilt with GCC 4.9.0 prerelease.

* Sun Sep 01 2013 Björn Persson <bjorn@rombobjörn.se> - 6.0-18
- Rebuilt with PragmARC-20130728.

* Sat Aug 03 2013 Björn Persson <bjorn@rombobjörn.se> - 6.0-17
- Build only on architectures where gcc-gnat is available.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 03 2013 Björn Persson <bjorn@rombobjörn.se> - 6.0-15
- Added a manual page stub.

* Mon May 13 2013 Björn Persson <bjorn@rombobjörn.se> - 6.0-14
- Rebuilt with PragmARC-20130311.

* Thu Jan 24 2013 Björn Persson <bjorn@rombobjörn.se> - 6.0-13
- Rebuilt with GCC 4.8.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jul 06 2012 Björn Persson <bjorn@rombobjörn.se> - 6.0-11
- Added a patch to adapt to an API change in GTKada 2.24.2.

* Thu Jan 05 2012 Björn Persson <bjorn@rombobjörn.se> - 6.0-10
- Rebuilt with GCC 4.7.

* Mon Aug 15 2011 Björn Persson <bjorn@rombobjörn.se> - 6.0-9
- Trying again to rebuild with GtkAda-2.18.0.

* Sun Aug 14 2011 Björn Persson <bjorn@rombobjörn.se> - 6.0-8
- Rebuilt with GtkAda-2.18.0.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 24 2011 Björn Persson <bjorn@rombobjörn.se> - 6.0-6
- Removed a workaround that is no longer needed.

* Wed Jan 19 2011 Björn Persson <bjorn@rombobjörn.se> - 6.0-5
- Rebuilt with GtkAda-2.14.1.

* Thu Jul 08 2010 Björn Persson <bjorn@rombobjörn.se> - 6.0-4
- Rebuilt with GCC 4.5.

* Tue Jan 26 2010 Björn Persson <bjorn@rombobjörn.se> - 6.0-3
- Clarified the license situation.
- All source file names begin with "mine_detector".

* Mon Nov 09 2009 Björn Persson <bjorn@rombobjörn.se> - 6.0-2
- Fixed to link libgnat and libgcc dynamically.

* Sat Aug 08 2009 Björn Persson <bjorn@rombobjörn.se> - 6.0-1
- Updated to version 6.0.
- Dropped the two patches.
- The license was changed in version 6.0 from GPLv2+ to GPLv2.
- Updated the URLs because the PragmAda site moved.

* Thu Jul 23 2009 Björn Persson <bjorn@rombobjörn.se> - 5.0-2
- Added a BuildRoot tag even though it's unnecessary.

* Sun Jun 28 2009 Björn Persson <bjorn@rombobjörn.se> - 5.0-1
- ready to be submitted for review
