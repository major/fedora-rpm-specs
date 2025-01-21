%if (0%{?rhel} && 0%{?rhel} <= 7) || (0%{?fedora} && 0%{?fedora} > 36)
%global gxvattr 0
%else
%global gxvattr 1
%endif

Summary:    Utility for getting and setting Xv attributes
Name:       xvattr
Version:    1.3
Release:    52%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:    GPL-2.0-or-later
URL:        http://www.dtek.chalmers.se/groups/dvd/
Source:     http://ajax.fedorapeople.org/%{name}/%{name}-%{version}.tar.gz
# Normalize documentation encoding
Patch0:     xvattr-1.3-Convert-documentation-to-UTF-8.patch
# Do not loose system CFLAGS for gxvattr
Patch1:     xvattr-1.3-Use-GTK_CFLAGS-properly.patch
# Allow to disable GTK tools
Patch2:     xvattr-1.3-Make-GTK-tools-optional.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  gcc
%if %{gxvattr}
BuildRequires:  gtk+-devel
%endif
BuildRequires:  libX11-devel
BuildRequires:  libXv-devel
BuildRequires:  make
BuildRequires:  perl-podlators

%description
This program is used for getting and setting Xv attributes such as
XV_BRIGHTNESS, XV_CONTRAST, XV_SATURATION, XV_HUE, XV_COLORKEY.

%package -n gxvattr
Summary: GTK1-based GUI for Xv attributes

%description -n gxvattr
GTK1-based GUI for inspecting and setting Xv attributes.

%prep
%autosetup -p1
autoreconf --install --force

%build
%configure \
%if %{gxvattr}
    --enable-gtk
%else
    --disable-gtk
%endif
%{make_build}

%install
%{make_install}

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/xvattr
%{_mandir}/man1/*

%if %{gxvattr}
%files -n gxvattr
%license COPYING
%{_bindir}/gxvattr
%endif

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3-51
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Mar 17 2022 Petr Pisar <ppisar@redhat.com> - 1.3-45
- Disable gxvattr since Fedora 37

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 02 2018 Troy Dawson <tdawson@redhat.com> - 1.3-35
- Update conditionals

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 26 2015 Petr Pisar <ppisar@redhat.com> - 1.3-30
- Modernize specification file

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 19 2013 Mat Booth <fedora@matbooth.co.uk> - 1.3-26
- Fix pod encoding, rhbz #993161

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 26 2013 Adam Jackson <ajax@redhat.com> 1.3-24
- BuildRequires: perl-podlators for pod2man

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 15 2012 Adam Jackson <ajax@redhat.com> 1.3-22
- Move Source0 to fedorapeople since upstream went away
- Don't built (gtk1-based) gxvattr in RHEL

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Apr 18 2011 Adam Jackson <ajax@redhat.com> 1.3-19
- Split the GTK1 (!) version to a subpackage

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.3-15
- Autorebuild for GCC 4.3

* Thu Aug 23 2007 Matthias Saou <http://freshrpms.net/> 1.3-14
- Rebuild for new BuildID feature.
- Remove dist tag, since the package will seldom change.

* Fri Aug  3 2007 Matthias Saou <http://freshrpms.net/> 1.3-13
- Update License field.

* Tue Jun 19 2007 Matthias Saou <http://freshrpms.net/> 1.3-12
- Switch to using DESTDIR install method.
- Convert man page to UTF-8... not?

* Mon Aug 28 2006 Matthias Saou <http://freshrpms.net/> 1.3-11
- FC6 rebuild.

* Tue May 23 2006 Matthias Saou <http://freshrpms.net/> 1.3-10
- Fix CFLAGS so that our optflags get used too (Ville, #192611).

* Mon Mar  6 2006 Matthias Saou <http://freshrpms.net/> 1.3-9
- FC5 rebuild.

* Thu Feb  9 2006 Matthias Saou <http://freshrpms.net/> 1.3-8
- Rebuild for new gcc/glibc and modular X.

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1.3-7
- rebuild on all arches

* Wed Apr  6 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Tue Nov 16 2004 Matthias Saou <http://freshrpms.net/> 1.3-5
- Bump release to provide Extras upgrade path.

* Wed Mar 24 2004 Matthias Saou <http://freshrpms.net/> 1.3-4
- Remove explicit XFree86 dependency for the binary package.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.3-3
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Fri Oct 4 2002 Matthias Saou <http://freshrpms.net/>
- Initial rpm release.

