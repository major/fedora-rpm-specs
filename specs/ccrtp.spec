Name:          ccrtp
Summary:       Common C++ class framework for RTP/RTCP
Version:       2.1.2
Release:       16%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           http://www.gnu.org/software/commoncpp/
Source0:       http://ftp.gnu.org/pub/gnu/ccrtp/ccrtp-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: commoncpp2-devel >= 1.7.0
BuildRequires: doxygen
BuildRequires: libgcrypt-devel
BuildRequires: ucommon-devel

%description
ccRTP is a generic, extensible and efficient C++ framework for
developing applications based on the Real-Time Transport Protocol
(RTP) from the IETF. It is based on Common C++ and provides a full
RTP/RTCP stack for sending and receiving of realtime data by the use
of send and receive packet queues. ccRTP supports unicast,
multi-unicast and multicast, manages multiple sources, handles RTCP
automatically, supports different threading models and is generic as
for underlying network and transport protocols.


%package devel
Summary: Header files and libraries for %{name} development
# Some of the headers are LGPLv2+
License: GPLv2+ and LGPLv2+
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig, commoncpp2-devel

%description devel
The %{name}-devel package contains the header files and libraries needed
to develop programs that use the %{name} library.


%prep
%autosetup -p1
chmod 644 src/ccrtp/rtp.h


%build
%configure --disable-static
%make_build


%install
%make_install
rm -f %{buildroot}%{_infodir}/dir
find %{buildroot} -name '*.la' -exec rm -f {} \;


%files
%doc README
%license COPYING COPYING.addendum
%{_libdir}/*.so.3*

%files devel
%doc doc/html
%{_includedir}/ccrtp/
%{_libdir}/*.so
%{_libdir}/pkgconfig/libccrtp.pc
%{_infodir}/ccrtp.info*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.2-15
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 31 2019 Sandro Mani <manisandro@gmail.com> - 2.1.2-1
- Update to 2.1.2

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Sandro Mani <manisandro@gmail.com> - 2.0.5-18
- Add missing BR: gcc-c++, make

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 03 2016 Filipe Rosset <rosset.filipe@gmail.com> - 2.0.5-13
- Spec clean up

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 28 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.0.5-11
- Rebuilt for ucommon soname bump

* Thu Aug 06 2015 Dan Horák <dan@danny.cz> - 2.0.5-10
- rebuild for new libucommon

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 19 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/GCC5

* Thu Feb 26 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/GCC5

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 22 2014 Tomáš Mráz <tmraz@redhat.com> - 2.0.5-4
- Rebuild for new libgcrypt

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 21 2012 Kevin Fenzi <kevin@scrye.com> 2.0.5-1
- Upgrade to 2.0.5

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jan 22 2012 Kevin Fenzi <kevin@scrye.com> - 2.0.2-1
- Update to 2.0.2

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 07 2009 Andreas Thienemann <andreas@bawue.net> - 1.7.1-1
- Update to upstream release 1.7.1

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 15 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.6.0-2
- fix license tag

* Wed Feb 06 2008 Andreas Thienemann <andreas@bawue.net> - 1.6.0-1
- Updated to upstream version 1.6.0
- Added patch enabling build with gcc-4.3

* Wed Feb 06 2008 Dennis Gilmore <dennis@ausil.us> - 1.5.1-2
- rebuild for new commoncpp2

* Wed Mar 07 2007 Andreas Thienemann <andreas@bawue.net> - 1.5.1-1
- Updated package to 1.5.1
- Fixed #219396

* Fri Nov 10 2006 Andreas Thienemann <andreas@bawue.net> - 1.5.0-1
- Updated package to 1.5.0, fixing #209026

* Sun Sep 10 2006 Andreas Thienemann <andreas@bawue.net> - 1.4.1-2
- *bump*

* Fri Sep 08 2006 Andreas Thienemann <andreas@bawue.net> - 1.4.1-1
- Updated to 1.4.1

* Sun Jul 23 2006 Andreas Thienemann <andreas@bawue.net> - 1.3.7-2
- Added doxygen BuildRequire

* Mon Apr 24 2006 Andreas Thienemann <andreas@bawue.net> - 1.3.7-1
- Updated to 1.3.7

* Fri Feb 03 2006 Andreas Thienemann <andreas@bawue.net> - 1.3.6-1
- Initial spec.
