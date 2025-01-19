Name:		moe
Version:	1.15
Release:	2%{?dist}
Summary:	A powerful clean text editor

License:	GPL-3.0-or-later
URL:		http://www.gnu.org/software/moe/moe.html
Source0:	http://ftp.gnu.org/gnu/moe/moe-%{version}.tar.lz
Patch0:		moe-1.13-configure.patch

BuildRequires: make
BuildRequires:	ncurses-devel lzip gcc-c++

%description
GNU Moe is a powerful, 8-bit clean, text editor for ISO-8859 and ASCII 
character encodings. It has a modeless, user-friendly interface, online 
help, multiple windows, unlimited undo/redo capability, unlimited line 
length, global search/replace (on all buffers at once), block operations, 
automatic indentation, word wrapping, filename completion, directory 
browser, duplicate removal from prompt histories, delimiter matching, etc.

%prep
%setup -q
%patch -P 0 -p0 -b .configure

%build
%configure
make %{?_smp_mflags}

%install
make install INSTALL="%{__install} -p" DESTDIR=$RPM_BUILD_ROOT
%{__install} -p -d $RPM_BUILD_ROOT%{_mandir}/man1 
%{__install} -p -m 644 ./doc/moe.1 $RPM_BUILD_ROOT%{_mandir}/man1/
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%files
%doc AUTHORS README NEWS ChangeLog
%license COPYING
%{_datadir}/info/%{name}.info*
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jan 06 2025 Gwyn Ciesla <gwync@protonmail.com> - 1.15-1
- 1.15

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.14-1
- 1.14

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 28 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.13-2
- migrated to SPDX license

* Tue Feb 21 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.13-1
- 1.13

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.12-1
- 1.12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 04 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.11-1
- 1.11

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.9-1
- 1.9, BZ 1465196.
- Spec cleanup.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 15 2016 Jon Ciesla <limburgher@gmail.com> - 1.8-1
- Latest upstream, BZ 1308503.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 08 2015 Jon Ciesla <limburgher@gmail.com> - 1.7-1
- Latest upstream, BZ 1101203.

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.5-5
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 08 2013 Jon Ciesla <limburgher@gmail.com> - 1.5-1
- Latest upstream, BZ 919547.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Apr 08 2011 Vivek Shah <boni.vivek at gmail.com> - 1.4-3
- Updated to new upstream version
- Fixed configure file

* Fri Apr 08 2011 Vivek Shah <boni.vivek at gmail.com> - 1.4-2
- Updated to new upstream version
- Fixed incorrect upload

* Fri Apr 08 2011 Vivek Shah <boni.vivek at gmail.com> - 1.4-1
- Updated to new upstream version
- Used lz file from gz as source

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 17 2009 Vivek Shah <boni.vivek at gmail.com> -1.3-1
- Updated to new upstream version

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr 19 2009 Debarshi Ray <rishi@fedoraproject.org> 1.0-5
- Fixed configure to respect the environment's CFLAGS and CXXFLAGS settings.

* Sun Mar 01 2009 Caolán McNamara - 1.0-4
- include stdio.h for snprintf

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep 10 2008 Vivek Shah <boni.vivek at gmail.com> 1.0-2
- Fixed build dependencies
- Added removal of infodir/dir to avoid overwriting
- Added target for manpage 

* Sat Aug 23 2008 Vivek Shah <boni.vivek at gmail.com> 1.0-1
- Initial Package
