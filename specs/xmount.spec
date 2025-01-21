%undefine __cmake_in_source_build

Name:           xmount
Version:        0.7.6
Release:        17%{?dist}
Summary:        A on-the-fly convert for multiple hard disk image types

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://www.pinguin.lu/index.php
Source0:        https://files.pinguin.lu/%{name}-%{version}.tar.gz
Patch0:         xmount-suffix.patch
Patch1:         xmount-cflags.patch

BuildRequires:  gcc-c++
BuildRequires:  fuse-devel
BuildRequires:  libewf-devel
BuildRequires:  afflib-devel
BuildRequires:  zlib-devel
BuildRequires:  cmake

Provides:       bundled(md5-deutsch)

%description
xmount allows you to convert on-the-fly between multiple input
and output hard disk image types. xmount creates a virtual file
system using FUSE (Filesystem in Userspace) that contains a virtual
representation of the input image. The virtual representation can
be in raw DD, VirtualBox's virtual disk file format or in VmWare's
VMDK file format. Input images can be raw DD, EWF (Expert Witness
Compression Format) or AFF (Advanced Forensic Format) files. In
addition, xmount also supports virtual write access to the output
files that is redirected to a cache file. This makes it possible
to boot acquired hard disk images using QEMU, KVM, VirtualBox,
VmWare, or alike.


%prep
%setup -q
%patch -P0 -p1 -b .suffix
# Use std=99 on rhel7, uneeded nowadays
%if 0%{?fedora} || 0%{?rhel} > 7
%patch -P1 -p1 -b .cflags
%endif
# Fix perm
chmod -x src/xmount.*


%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_SKIP_RPATH=ON \
    %{nil}

%cmake_build


%install
%cmake_install


%files
%doc AUTHORS ChangeLog NEWS README ROADMAP TODO
%license COPYING
%{_mandir}/man*/%{name}*.*
%{_bindir}/%{name}
%{_libdir}/xmount


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7.6-16
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 13 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.7.6-3
- Fix build down to epel7
- Add missing hook
- Better space handling

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.6-1
- Update to new upstream version 0.7.6 (rhbz#1316252)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Apr 02 2016 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.3-1
- Update to new upstream version 0.7.3 (rhbz#1316252)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Aug 19 2014 Michal Ambroz <rebus _AT seznam.cz> - 0.6.0-4
- enable build with newer ewf library

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jun 05 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.0-1
- Update to new upstream version 0.6.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 01 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.5.0-4
- Rebuilt for libewf

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Sep 02 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.0-2
- Clean section remove
- BR update

* Mon Aug 06 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.0-1
- Add a provide
- Permissions were fixed upstream 
- Update to new upstream version 0.5.0

* Sat Jun 30 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.7-2
- Leave md5 implementation in place

* Fri Apr 13 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.7-1
- Update to new upstream version 0.4.7

* Tue Oct 18 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.6-1
- Update to new upstream version 0.4.6

* Wed Sep 01 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.2-2
- Add patch from #606073
- Fix permission
- Add needed BRs

* Mon Mar 15 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.2-1
- Initial package for Fedora
