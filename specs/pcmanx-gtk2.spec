Summary:    Telnet client designed for BBS browsing
Name:       pcmanx-gtk2
Version:    1.3
Release:    22%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:    GPL-2.0-or-later
Source0:    https://github.com/pcman-bbs/pcmanx/releases/download/%{version}/%{name}-%{version}.tar.xz
URL:        https://github.com/pcman-bbs/pcmanx
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel libXft-devel libtool-ltdl-devel
BuildRequires:  libnotify-devel >= 0.7.0
BuildRequires:  desktop-file-utils gettext
BuildRequires:  intltool


%description
An easy-to-use telnet client mainly targets BBS users.

PCMan X is a newly developed GPL'd version of PCMan, a full-featured
famous BBS client formerly designed for MS Windows only.  It aimed to
be an easy-to-use yet full-featured telnet client facilitating BBS
browsing with the ability to process double-byte characters.


%prep
tar Jfx %{SOURCE0}
%setup -qDT
# remove the bundled libltdl
rm -fr libltdl
sed -i -e 's/libltdl//' Makefile.in


%build
%configure --enable-proxy --enable-libnotify --enable-iplookup --enable-wget
make %{?_smp_mflags}

%install
make install INSTALL="install -c -p" DESTDIR=$RPM_BUILD_ROOT

desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applications/pcmanx.desktop

%find_lang pcmanx


%files -f pcmanx.lang
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/pcmanx/
%{_datadir}/pixmaps/*
%{_mandir}/man1/pcmanx.1*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3-21
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Robin Lee <cheeselee@fedoraproject.org> - 1.3-6
- BR gcc-c++ for http://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 30 2016 Robin Lee <cheeselee@fedoraproject.org> - 1.3-1
- Update to 1.3

* Tue Feb 16 2016 Robin Lee <cheeselee@fedoraproject.org> - 1.2-8
- Fix FTBFS with GCC 6 (BZ#1307847)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.2-5
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 24 2013 Robin Lee <cheeselee@fedoraproject.org> - 1.2-1
- Update to 1.2

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 30 2012 Robin Lee <cheeselee@fedoraproject.org> - 1.1-1
- Update to 1.1
- Use upstream desktop entry file
- BR: libtool-ltdl-devel
- Untabified

* Thu Jan 12 2012 Robin Lee <cheeselee@fedoraproject.org> - 1.0-1
- Update to 1.0
- Specfile cleanup

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.9-8.20101026svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 08 2010 Chen Lei <supercyper@163.com> - 0.3.9-7.20101026svn
- disable building shared libraries
- svn 529

* Fri Jun 18 2010 Chen Lei <supercyper@163.com> - 0.3.9-6.20100618svn
- several changes according to the review
- disable plugin by default
- svn 525

* Tue Jun 01 2010 Chen Lei <supercyper@163.com> - 0.3.9-5.20100601svn
- svn 523

* Sat Mar 27 2010 Chen Lei <supercyper@163.com> - 0.3.9-4.20100326svn
- svn 514
- remove obsolete patches

* Mon Feb 22 2010 Chen Lei <supercyper@163.com> - 0.3.9-3.20100222svn
- svn 501
- resolves: #513527

* Thu Feb 18 2010 <jhorak@redhat.com> - 0.3.9-2.20100210svn
- Rebuild against newer gecko

* Wed Feb 10 2010 Chen Lei <supercyper@163.com> - 0.3.9-1.20100210svn
- svn 500
- remove obsolete patches

* Wed Dec 16 2009 Jan Horak <jhorak@redhat.com> - 0.3.8-11
- Rebuild against newer gecko

* Thu Nov 05 2009 Jan Horak <jhorak@redhat.com> - 0.3.8-10
- Rebuild against newer gecko

* Tue Oct 27 2009 Jan Horak <jhorak@redhat.com> - 0.3.8-9
- Rebuild against newer gecko

* Wed Sep 09 2009 Jan Horak <jhorak@redhat.com> - 0.3.8-8
- Rebuild against newer gecko

* Tue Aug 04 2009 Jan Horak <jhorak@redhat.com> - 0.3.8-7
- Rebuild against newer gecko

* Thu Jul 23 2009 Jan Horak <jhorak@redhat.com> - 0.3.8-6
- Rebuild against newer gecko

* Wed Mar 5 2009 Caolán McNamara <caolanm@redhat.com> 0.3.8-5
- include stdio.h for perror

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 7 2009 Martin Stransky <stransky@redhat.com> - 0.3.8-3
- updated for xulrunner 1.9.1

* Thu Sep 25 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.3.8-2
- rebuild against xulrunner 1.9.0.2

* Wed Aug 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.3.8-1
- update to 0.3.8
- build and package mozilla/firefox/xulrunner plugin
