# Review request:
# https://bugzilla.redhat.com/show_bug.cgi?id=432701

%define    svn_date 20080213

Name:           ksig
Version:        1.1
Release:        0.39.%{svn_date}%{?dist}
Summary:        A graphical application to manage multiple email signatures

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://extragear.kde.org

# Creation of tarball from svn
#
# Kevin Kofler enhanced the create_tarball.rb script from upstream to also support ksig
# This script also download the translations and docs
# To use it you will need the script itself and a config.ini in the same directory
#
# http://repo.calcforge.org/f9/kde4-tarballs/create_tarball.rb
# http://repo.calcforge.org/f9/kde4-tarballs/config.ini
#
# To create a new checkout use it with anonymous svn access
# ./create_tarball.rb -n
# At the prompt you have to enter "ksig" (without brackets)

Source0:        %{name}-%{version}-svn.tar.bz2
# fix CMakeLists.txt so this builds as a standalone directory (without all of extragear-pim)
Patch0:         ksig-1.1-svn-cmakelists.patch
# Install documentation into the correct subdir
Patch1:         ksig-1.1-svn-docsdir.patch

BuildRequires:  kdelibs4-devel
BuildRequires:  kde-filesystem >= 4
BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  libutempter-devel
BuildRequires: make

%description
KSig is a graphical tool for keeping track of many different email signatures.
The signatures themselves can be edited through KSig's graphical user 
interface. A command-line interface is then available for generating random 
or daily signatures from a list. The command-line interface makes a suitable 
plugin for generating signatures in external mail clients such as KMail.

%prep
%setup -qn %{name}-%{version}-svn
%patch -P0 -p1 -b .cmakelists
%patch -P1 -p1 -b .docsdir


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

%make_build -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

# validate desktop file
desktop-file-install --vendor ""                          \
        --dir %{buildroot}%{_datadir}/applications/kde4   \
        %{buildroot}%{_datadir}/applications/kde4/%{name}.desktop

%find_lang %{name}


%files -f %{name}.lang
%license COPYING COPYING.DOC
%{_docdir}/HTML/en/ksig/
%{_kde4_bindir}/ksig
%{_kde4_appsdir}/ksig/
%{_kde4_iconsdir}/hicolor/*/apps/ksig.png
%{_datadir}/applications/kde4/ksig.desktop


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.39.20080213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1-0.38.20080213
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.37.20080213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.36.20080213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.35.20080213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.34.20080213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.33.20080213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.32.20080213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.31.20080213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.30.20080213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.29.20080213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.28.20080213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.27.20080213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.26.20080213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.25.20080213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.24.20080213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.1-0.23.20080213
- .spec cleanup

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.22.20080213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.21.20080213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.20.20080213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.19.20080213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.18.20080213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-0.17.20080213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1-0.16.20080213
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-0.15.20080213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-0.14.20080213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-0.13.20080213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-0.12.20080213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-0.11.20080213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-0.10.20080213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-0.9.20080213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-0.8.20080213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-0.7.20080213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug 29 2008 Sebastian Vahl <fedora@deadbabylon.de> - 1.1-0.6.20080213
- re-create patches for rpmbuild's fuzz=0
- BR: libutempter-devel

* Thu Apr 03 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.1-0.5.20080213
- rebuild (again) for the fixed %%{_kde4_buildtype}

* Wed Apr 02 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.1-0.4.20080213
- omit hard dep on kdelibs
- add scriptlet deps

* Mon Mar 31 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.1-0.3.20080213
- rebuild for NDEBUG and _kde4_libexecdir

* Fri Feb 15 2008 Sebastian Vahl <fedora@deadbabylon.de> - 1.1-0.2.20080213
- change group to Applications/Internet

* Wed Feb 13 2008 Sebastian Vahl <fedora@deadbabylon.de> - 1.1-0.1.20080213
- initial version
