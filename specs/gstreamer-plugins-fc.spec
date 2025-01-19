Name: gstreamer-plugins-fc
Version: 0.2
Release: 34%{?dist}
Summary: Future Composer input plugin for GStreamer
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://xmms-fc.sourceforge.net
Source0: http://downloads.sourceforge.net/xmms-fc/gstreamer-plugin-fc-%{version}.tar.bz2

BuildRequires: libfc14audiodecoder-devel

%if 0%{?fedora} < 31
BuildRequires: gstreamer-devel >= 0.10
# for %%{_libdir}/gstreamer-0.10
Requires: gstreamer%{?_isa}
%endif

# fixed upstream
Patch0: gstfcdec-0.2-configure.patch
BuildRequires: automake autoconf libtool
# from cvs
Patch1: gstreamer-plugin-fc-0.2-gstreamer1.patch

%description
This is an input plugin for GStreamer which can play back Future Composer
music files from AMIGA. Song-length detection and seek are implemented, too.


%package -n gstreamer1-plugins-fc
Summary: Future Composer input plugin for GStreamer 1.0.x
BuildRequires: gstreamer1-devel >= 1.0
BuildRequires: gstreamer1-plugins-base-devel >= 1.0
BuildRequires: make
# for %%{_libdir}/gstreamer-1.0
Requires: gstreamer1%{?_isa}
%if 0%{?fedora} > 30
Obsoletes: gstreamer-plugins-fc < 0.2-21
%endif

%description -n gstreamer1-plugins-fc
This is an input plugin for GStreamer which can play back Future Composer
music files from AMIGA. Song-length detection and seek are implemented, too.

%prep
%setup -q -n gstreamer-plugin-fc-%{version}
# https://bugzilla.redhat.com/925503
#patch0 -p1
%patch -P1 -p1
mv configure.in configure.ac
libtoolize -f ; autoreconf -f -i


%build
%configure \
    --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%if 0%{?fedora} < 31
%files
%license COPYING
%doc README ChangeLog
%{_libdir}/gstreamer-0.10/*.so
%endif


%files -n gstreamer1-plugins-fc
%license COPYING
%doc README ChangeLog
%{_libdir}/gstreamer-1.0/*.so


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul  26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2-33
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov  4 2019 Michael Schwendt <mschwendt@fedoraproject.org> - 0.2-21
- Declare gstreamer-plugins-fc package obsolete in gstreamer1-plugins-fc.

* Mon Nov  4 2019 Michael Schwendt <mschwendt@fedoraproject.org> - 0.2-20
- Drop GStreamer 0.10.x plugin. No idea why releng rebuilt this
  package before removing the [build] requirements from the distribution.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May  2 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 0.2-7
- BR gstreamer1-devel gstreamer1-plugins-base-devel
  for merged GStreamer 1.0.x plugin libgst1fcdec.so

* Fri Apr 26 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 0.2-6
- BR automake autoconf libtool and reconf for aarch64 updates (#925503).
- Update configure.in and rename it to configure.ac.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan  6 2012 Michael Schwendt <mschwendt@fedoraproject.org> - 0.2-3
- rebuild for GCC 4.7 as requested
- add %%{?_isa} to explicit gstreamer dep

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jun 19 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 0.2-1
- Upgrade to 0.2 and BR libfc14audiodecoder-devel.

* Mon May 31 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 0.1-4
- Set empty list of tags (so e.g. the SoundConverter app doesn't freeze).

* Sat Jan  9 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 0.1-3
- Remove redundant buildroot related spec instructions for
  Fedora 11 and newer.

* Fri Nov 13 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 0.1-2
- Use downloads.sourceforge.net and .tar.bz2

* Thu Jun  4 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 0.1-1
- Initial package for Fedora.
