Name:           grhino
Version:        0.16.1
Release:        22%{?dist}
Summary:        Reversi game for GNOME, supporting the Go/Game Text Protocol

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://rhino.sourceforge.net/
Source0:        http://downloads.sourceforge.net/rhino/grhino-%{version}.tar.gz
# from https://packages.debian.org/sid/grhino
Patch0:         %{name}-0.16.1-fix-format-security.patch

BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libgnomeui-devel
BuildRequires:  scrollkeeper
BuildRequires: make
#Requires:       
Requires(post):         scrollkeeper
Requires(postun):       scrollkeeper

%description
GRhino, or Rhino its former name, is a Reversi game on Linux and other UNIX-like
systems as long as GNOME 2 libraries are installed. It is currently under
development and a new version is available occasionally.

What distinguish GRhino from most other Reversi games is that GRhino will be
targeted for experienced Reversi players. Strong AI is the main focus with some
additional good, useful features (like an endgame solver) is planned. The
ultimate target strength of the AI is that it should be able to beat the best
human player at the highest difficulty level. Beating Logistello (the strongest
program available) is not in the plan :)

GRhino supports the Go/Game Text Protocol (GTP), allowing it to be used as an
engine for a GTP-compliant controller like Quarry.

%prep
%autosetup -p 1


%build
%configure
%make_build


%install
%make_install

# desktop file
desktop-file-install \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications \
        --remove-key=Version\
        desktop/%{name}.desktop

# Icon
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps

%find_lang %{name}

%post
scrollkeeper-update -q -o %{_datadir}/omf/%{name} || :

%postun
scrollkeeper-update -q || :


%files -f %{name}.lang
%license COPYING
%doc ChangeLog NEWS README TODO
%{_bindir}/grhino
%{_bindir}/gtp-rhino
%{_datadir}/applications/*.desktop
%{_datadir}/gnome/help/grhino/
%{_datadir}/pixmaps/grhino.png
%{_datadir}/grhino-%{version}/
%{_datadir}/omf/grhino/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.16.1-21
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.16.1-7
- Rebuilt with fix for -Wformat-security (from Debian)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jul  3 2016 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.16.1-1
- Update to 0.16.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.16.0-18
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 12 2013 Jon Ciesla <limburgher@gmail.com> - 0.16.0-14
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.0-11
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.16.0-9
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 22 2008 Michel Salim <michel.sylvan@gmail.com> - 0.16.0-5
- Fix incompatibilities with GCC 4.3 (header changes)
- Fix compilation warnings

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.16.0-4
- Autorebuild for GCC 4.3

* Fri Jan 18 2008 Michel Salim <michel.sylvan@gmail.com> - 0.16.0-3
- Rebuild for Fedora 9 (development tree)

* Mon Sep 24 2007 Michel Salim <michel.sylvan@gmail.com> - 0.16.0-2
- License field updated
- Remove invalid Version key from upstream desktop file

* Sat Nov 25 2006 Michel Salim <michel.salim@gmail.com> - 0.16.0-1
- Update to 0.16.0
- Remove unneeded patches

* Fri Nov 10 2006 Michel Salim <michel.salim@gmail.com> - 0.15.2-4
- Add application icon

* Sun Oct 29 2006 Michel Salim <michel.salim@gmail.com> - 0.15.2-3
- Fix incorrect OMF path

* Mon Oct  9 2006 Michel Salim <michel.salim@gmail.com> - 0.15.2-2
- BuildRequire on gettext

* Sun Oct  8 2006 Michel Salim <michel.salim@gmail.com> - 0.15.2-1
- Update to 0.15.2

* Thu Mar  2 2006 Michel Salim <michel.salim@gmail.com> - 0.15.0-5
- Rebuild for Fedora Extras 5

* Sun Nov 13 2005 Michel Salim <michel.salim[AT]gmail.com> - 0.15.0-4
- Reverted game name used in GTP protocol

* Sun Sep  4 2005 Michel Salim <michel.salim[AT]gmail.com> - 0.15.0-3
- removed references to copyrighted name
- packaged modified tarball to prevent trademark infringement
- patched configure to fix gettext detection on x86_64

* Fri Sep  2 2005 Michel Salim <michel.salim[AT]gmail.com> - 0.15.0-2
- changed BuildReq from libgnome-devel to libgnomeui-devel, which requires
  the former

* Sat Aug 20 2005 Michel Salim <michel.salim[AT]gmail.com> - 0.15.0-1
- initial package
