# Upstream has not made releases in a while.  Track HEAD instead of trying to
# backport individual patches.
%global commit0 8473c299bc193f44c520c930a72618999ae5bb17
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: Command line multimedia player based on gstreamer
Name: gst123
Version: 0.3.3
Release: 27.1.%{shortcommit0}%{?dist}
URL: http://space.twc.de/~stefan/gst123.php
Source0: http://space.twc.de/cgi-bin/gitweb.cgi?p=gst123.git;a=snapshot;h=%{commit0};sf=tgz#/%{name}-%{shortcommit0}.tgz

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2

# We need to generate configure scripts because upstream does it at release
# time.
BuildRequires:  gcc-c++
BuildRequires: autoconf automake
BuildRequires: gstreamer1-devel
BuildRequires: gstreamer1-plugins-base-devel
BuildRequires: gtk2-devel
BuildRequires: libX11-devel
BuildRequires: ncurses-devel
BuildRequires: make

%description

The program gst123 is designed to be a more flexible command line player 
in the spirit of ogg123 and mpg123, based on gstreamer. It plays all file 
formats gstreamer understands, so if you have a music collection which 
contains different file formats, you can use gst123 to play all your 
music files.

%prep
%autosetup -n %{name}-%{shortcommit0}
./autogen.sh

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files

%{_bindir}/gst123
%{_mandir}/man1/gst123.1.gz
%doc COPYING AUTHORS README NEWS

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-27.1.8473c29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.3-26.1.8473c29
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-25.1.8473c29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-24.1.8473c29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-23.1.8473c29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-22.1.8473c29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-21.1.8473c29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-20.1.8473c29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-19.1.8473c29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-18.1.8473c29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-17.1.8473c29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-16.1.8473c29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-15.1.8473c29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-14.1.8473c29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-13.1.8473c29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-12.1.8473c29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-11.1.8473c29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-10.1.8473c29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-9.1.8473c29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-8.1.8473c29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Mar 02 2016 Siddhesh Poyarekar <sid@reserved-bit.com> - 0.3.3-7.1.8473c29
- Rebase to upstream git HEAD (#1307600).

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.3-5
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 11 2014 Siddhesh Poyarekar <siddhesh@redhat.com> - 0.3.3-2
- Use gstreamer1.

* Tue Feb 11 2014 Siddhesh Poyarekar <siddhesh@redhat.com> - 0.3.3-1
- New upstream 0.3.3

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun  2 2012 Siddhesh Poyarekar <siddhesh@redhat.com> - 0.3.1-1
- New upstream 0.3.1

* Thu Mar 15 2012 Siddhesh Poyarekar <siddhesh@redhat.com> - 0.2.2-2
- Remove unnecessary patches

* Thu Mar 15 2012 Siddhesh Poyarekar <siddhesh@redhat.com> - 0.2.2-1
- New upstream 0.2.2

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-5
- Rebuilt for c++ ABI breakage

* Tue Jan 17 2012 Siddhesh Poyarekar <siddhesh@redhat.com> - 0.2.1-4
- Don't depend on someone else to include unistd.h. Fixes FTBFS on gcc4.7

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.2.1-2
- Rebuild for new libpng

* Sun Jul 31 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 0.2.1-1
- New upstream bug fix release
- Clean up spec to match current guidelines

* Sat Jul 30 2011 Siddhesh Poyarekar <siddhesh@redhat.com> - 0.2.0-1
- New upstream 0.2.0

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan  3 2011 Siddhesh Poyarekar <siddhesh@redhat.com> - 0.1.3-2
- Don't crash with terminals that don't define all escape sequences.
  Closes bz #666059.

* Wed Dec 08 2010 Siddhesh Poyarekar <spoyarek@redhat.com> - 0.1.3-1
- rebase to upstream 0.1.3. Closes bz #611636

* Tue Jul 06 2010 Siddhesh Poyarekar <spoyarek@redhat.com> - 0.1.2-1
- rebase to upstream 0.1.2. Closes bug 611587, 603681

* Thu Jun 10 2010 Siddhesh Poyarekar <spoyarek@redhat.com> - 0.1.0-3
- Add gstreamer-plugins-base-devel to BuildRequires

* Thu Jun 10 2010 Siddhesh Poyarekar <spoyarek@redhat.com> - 0.1.0-2
- Removed the mp3 reference from description. We only play formats 
  gstreamer understands

* Wed Jun 09 2010 Siddhesh Poyarekar <spoyarek@redhat.com> - 0.1.0-1
- New package
- Fix FTBFS with binutils-gold due to indirect link with libX11

