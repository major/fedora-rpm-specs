Name:           ghasher
Version:        1.2.1
Release:        42%{?dist}
Summary:        GUI hasher for GTK+ 2
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://asgaard.homelinux.org/code/ghasher/
Source0:        http://asgaard.homelinux.org/code/ghasher/ghasher-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  gtk2-devel >= 2.4 openssl-devel desktop-file-utils libglade2-devel
BuildRequires: make
Patch0:         %{name}-format-security.patch
Patch1:         %{name}-openssl-1.1.0.patch

%description
ghasher can easily show the MD5 sum (or md2, md4, sha1, sha, ripemd160, dss1)
of a file. Motivation for this utility was that users shouldn't need to open a
command line for checking the MD5 sum of files they download.

%prep
%autosetup

%build
%make_build

%install
#make_install
install -D -m 0755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D -m 0644 hash.xpm $RPM_BUILD_ROOT%{_datadir}/pixmaps/hash.xpm
cat > %{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=MD5 Sum Utility
Comment=Calculate the md5 sum of a file
Exec=ghasher %%F
Terminal=false
Type=Application
Icon=hash
Categories=Utility;GTK;Application;
EOF
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{name}.desktop

%files
%doc AUTHORS NEWS README TODO
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/pixmaps/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.1-41
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.2.1-33
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 25 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.2.1-26
- rebuilt to fix FTBFS + spec cleanup + fixes rhbz #1555763 and #1604078

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 10 2013 Jon Ciesla <limburgher@gmail.com> - 1.2.1-15
- Drop desktop vendor tag.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.2.1-11
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.2.1-9
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 Tomas Mraz <tmraz@redhat.com> - 1.2.1-6
- rebuild with new openssl

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.1-5
- Autorebuild for GCC 4.3

* Wed Dec  5 2007 Denis Leroy <denis@poolshark.org> - 1.2.1-4
- Rebuild for newer version of openssl
- Fixed desktop entry

* Wed Aug 22 2007 Denis Leroy <denis@poolshark.org> - 1.2.1-3
- F8 rebuild

* Mon Sep  4 2006 Denis Leroy <denis@poolshark.org> - 1.2.1-2
- Fixed compile option, bug 192618

* Mon Sep  4 2006 Denis Leroy <denis@poolshark.org> - 1.2.1-1
- Update to version 1.2.1

* Mon Feb 13 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.2.0-8
- Rebuild for Fedora Extras 5

* Thu Nov 10 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.2.0-7
- Rebuild for new OpenSSL

* Thu Oct  6 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.2.0-6
- Add support for files >2GiB

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sat Mar 19 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.2.0-4
- %%

* Wed Mar 16 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.2.0-3
- Broke %%description at 80 columns

* Wed Mar 16 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.2.0-2
- Removed explicit Requires

* Tue Mar 15 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.2.0-1
- Bump release to 1
- Cleaned up %%description

* Thu Mar  3 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0:1.2.0-0.iva.1
- Fixed several packaging errors

* Mon Feb 28 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0:1.2.0-0.iva.0
- Initial RPM release.
