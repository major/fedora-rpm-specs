%global commit d3bcbc7f74469b92162ca6995eb8506bf49188c0
%global commitdate 20220522
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		gtk-v4l
Version:	0.4
Release:	33.%{commitdate}git%{shortcommit}%{?dist}
Summary:	Video4Linux Device Preferences
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2+
URL:		https://github.com/jwrdegoede/gtk-v4l/
Source0:	https://github.com/jwrdegoede/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch0: gtk-v4l-c99.patch
BuildRequires:	meson gcc
BuildRequires:	scrollkeeper
BuildRequires:	libv4l-devel >= 0.6
BuildRequires:	gtk3-devel >= 3.0
BuildRequires:	libgudev1-devel >= 151
# No users of the library ever materialized and the new meson buildsystem
# no longer builds the library
Obsoletes:	%{name}-devel < %{version}-%{release}
# No provides since -devel is simply gone, not provided by the main pkg

%description
gtk-v4l is a Video4Linux Web camera control app


%prep
%autosetup -p1 -n %{name}-%{commit}


%build
%meson
%meson_build


%install
%meson_install


%files
%doc *.md
%license COPYING
%{_bindir}/gtk-v4l
%{_datadir}/applications/gtk-v4l.desktop


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-33.20220522gitd3bcbc7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4-32.20220522gitd3bcbc7
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-31.20220522gitd3bcbc7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-30.20220522gitd3bcbc7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-29.20220522gitd3bcbc7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 05 2024 Florian Weimer <fweimer@redhat.com> - 0.4-28.20220522gitd3bcbc7
- Fix C compatibility issues

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-27.20220522gitd3bcbc7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-26.20220522gitd3bcbc7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Dec  4 2022 Hans de Goede <hdegoede@redhat.com> - 0.4-25.20220522gitd3bcbc7
- Update to a git snapshot
- This adds support for v4l-subdevs which is useful for MIPI cameras
- Drop -devel subpackage since gtk-v4l now no longer includes a separate lib

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 10 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.4-8
- Fix FTBFS with -Werror=format-security (#1037113, #1106738)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jul 31 2012 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 0.4.4
- Change of license, from GPLv2+ to LGPLv2+

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May  9 2012 Hans de Goede <hdegoede@redhat.com> - 0.4-2
- Remove glib source on a device unplug, this avoids errors when the fd
  gets reused later

* Fri Jan 20 2012 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 0.4-1
- New upstream release

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.3-5
- Rebuild for new libpng

* Sat Mar 12 2011 Hans de Goede <hdegoede@redhat.com> - 0.3-4
- Don't try to reset inactive controls (avoids error dialogs)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jun 03 2010 Huzaifa Sidhpurwala <huzaifas@redhat.com> 0.3-2
- New upstream, version bump

* Thu Feb 25 2010 Huzaifa Sidhpurwala <huzaifas@redhat.com> 0.1-2
- Correct spelling mistakes, remove Requires

* Wed Feb 24 2010 Huzaifa Sidhpurwala <huzaifas@redhat.com> 0.1-1
- Initial build
