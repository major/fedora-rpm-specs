%global     detectorver 1.1

Name:           unar
Version:        1.10.8
Release:        10%{?dist}
Summary:        Multi-format extractor
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://theunarchiver.com/command-line
Source0:        https://github.com/MacPaw/XADMaster/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/MacPaw/universal-detector/archive/%{detectorver}/universal-detector-%{detectorver}.tar.gz
Patch1: unar-int-conversion.patch
BuildRequires:  bzip2-devel
BuildRequires:  gcc-objc
BuildRequires:  gcc-c++
BuildRequires:  gnustep-base-devel
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(wavpack)

%description
The command-line utilities lsar and unar are capable of listing and extracting
files respectively in several formats including RARv5, RAR support includes
encryption and multiple volumes, unar can serve as a free and open source
replacement of unrar.

%prep
%setup -q -c
tar -xf %{SOURCE1}
%patch -P1 -p1
mv universal-detector-%{detectorver} UniversalDetector
rm -fr __MACOSX The\ Unarchiver
# recursively remove executable bit from every file, skipping directories
find . -type f -print0 | xargs -0 chmod -x

%build
# LTO is able to more thoroughly propagate constants and as a result
# exposes the constant 0 to a point where an Objective-C object with
# a catchable type must be used.  Disable LTO until the package
# gets fixed
%define _lto_cflags %{nil}
export OBJCFLAGS="%{optflags}"
#export OBJCFLAGS=`gnustep-config --objc-flags`
make -C XADMaster-%{version} -f Makefile.linux \
%if 0%{?rhel} >= 8
  OBJCC=gobjc
%endif

%install
pushd XADMaster-%{version}
install -d %{buildroot}%{_bindir}
install -pm755 unar lsar %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
install -pm644 Extra/*.1 %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_datadir}/bash-completion/completions
install -pm644 Extra/lsar.bash_completion %{buildroot}%{_datadir}/bash-completion/completions/lsar
install -pm644 Extra/unar.bash_completion %{buildroot}%{_datadir}/bash-completion/completions/unar
popd

%files
%license XADMaster-%{version}/LICENSE
%{_bindir}/lsar
%{_bindir}/unar
%{_mandir}/man1/*.1*
%{_datadir}/bash-completion/completions/*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 08 2024 Pete Walter <pwalter@fedoraproject.org> - 1.10.8-9
- Rebuild for ICU 76

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.10.8-8
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 16 2024 Antonio Trande <sagitter@fedoraproject.org> - 1.10.8-6
- Rebuild for gnustep-base 1.30.0

* Wed Jan 31 2024 Pete Walter <pwalter@fedoraproject.org> - 1.10.8-5
- Rebuild for ICU 74

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 22 2023 Florian Weimer <fweimer@redhat.com> - 1.10.8-3
- Fix int-conversion error

* Sun Nov 19 2023 Antonio Trande <sagitter@fedoraproject.org> - 1.10.8-2
- Rebuild for gnustep-base-1.29.0

* Thu Oct 12 2023 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1.10.8-1
- Update to 1.10.8 (#2243653)

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 1.10.7-7
- Rebuilt for ICU 73.2

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 1.10.7-5
- Rebuild for ICU 72

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.10.7-4
- Rebuilt for ICU 71.1

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Oct 31 2021 Sérgio Basto <sergio@serjux.com> - 1.10.7-1
- Update unar to 1.10.7 (#2012015)

* Tue Sep 28 2021 Robert Scheck <robert@fedoraproject.org> - 1.10.1-24
- Build using gobjc on EPEL 8 (#2008326)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 20 2021 Pete Walter <pwalter@fedoraproject.org> - 1.10.1-22
- Rebuild for ICU 69

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 17 2020 Jeff Law <law@redhat.com> - 1.10.1-20
- Disable LTO

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-19
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 18 2020 Pete Walter <pwalter@fedoraproject.org> - 1.10.1-17
- Rebuild for ICU 67

* Sat Apr 18 2020 Sérgio Basto <sergio@serjux.com> - 1.10.1-16
- Rebuild for gnustep 1.27.0

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 1.10.1-14
- Rebuild for ICU 65

* Fri Sep 06 2019 Sérgio Basto <sergio@serjux.com> - 1.10.1-13
- Rebuild for new gnustep 1.26.0

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 1.10.1-10
- Rebuild for ICU 63

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild
- https://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 1.10.1-8
- Rebuild for ICU 61.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 1.10.1-6
- Rebuild for ICU 60.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Apr 16 2017 Sérgio Basto <sergio@serjux.com> - 1.10.1-3
- Rebuild (libgnustep-base)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 09 2016 Pete Walter <pwalter@fedoraproject.org> - 1.10.1-1
- Update to 1.10.1

* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 1.8.1-12
- rebuild for ICU 57.1

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 28 2015 David Tardon <dtardon@redhat.com> - 1.8.1-10
- rebuild for ICU 56.1

* Tue Jul 14 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.8.1-9
- Remove LDFLAGS, pass RPM_OPT_FLAGS as OBJCFLAGS
  (Fix F23FTBFS, RHBZ#1240023).
- Add %%license.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 26 2015 David Tardon <dtardon@redhat.com> - 1.8.1-7
- rebuild for ICU 54.1

* Tue Aug 26 2014 David Tardon <dtardon@redhat.com> - 1.8.1-6
- rebuild for ICU 53.1

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jul 20 2014 Christopher Meng <rpm@cicku.me> - 1.8.1-4
- Insert Fedora-specific LDFLAGS for linking

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 14 2014 Adam Williamson <awilliam@redhat.com> - 1.8.1-2
- rebuild for new icu

* Sat Jan 25 2014 Rahul Sundaram <sundaram@fedoraproject.org> - 1.8.1-1
- upstream release 1.8.1 (rhbz#1047226)

* Sun Dec 29 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.8-1
- upstream release 1.8 (rhbz#1047226)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 19 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.6-4
- fix spurious executable permissions 

* Fri Apr 19 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.6-3
- revert dir ownership change and requires on bash-completion

* Thu Apr 18 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.6-2
- fix dir ownership and add requires on bash-completion. 
- fix a couple of typos

* Thu Apr 18 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.6-1
- initial spec file. based on spec from Huaren Zhong <huaren.zhong@gmail.com> 
