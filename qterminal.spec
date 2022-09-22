%define __cmake_in_source_build 1

Name:		qterminal
Version:	1.1.0
Release:	2%{?dist}
License:	GPLv2
URL:		https://github.com/qterminal/qterminal
Source0:	https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Summary:	Advanced Qt5-based terminal emulator


BuildRequires: make
BuildRequires:	desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(lxqt) >= 1.0.0
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(qtermwidget5) = %{version}
BuildRequires:  qt5-qttools-devel
BuildRequires:  pkgconfig(glib-2.0)
%if 0%{?el7}
BuildRequires:  devtoolset-7-gcc-c++
%endif

# Require qtermwidget to be the same version, as suggested by upstream
Requires:       qtermwidget = %{version}

Provides:       %{name}-common = %{version}-%{release}
Provides:       %{name}-qt5 = %{version}-%{release}
Obsoletes:      %{name}-common < %{version}-%{release}
Obsoletes:      %{name}-qt5 < %{version}-%{release}

%description
Advanced Qt5-based terminal emulator with many useful bells and whistles.


%package l10n
BuildArch:      noarch
Summary:        Translations for qterminal
Requires:       qterminal
%description l10n
This package provides translations for the qterminal package.

%prep
%setup -q


%build
%if 0%{?el7}
scl enable devtoolset-7 - <<\EOF
%endif

%{cmake_lxqt} -DPULL_TRANSLATIONS=NO ..

make %{?_smp_mflags} -C %{_vpath_builddir}

%if 0%{?el7}
EOF
%endif

%install
make install/fast DESTDIR=%{buildroot} -C %{_vpath_builddir}
%find_lang qterminal --with-qt


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-drop.desktop

%post
%if 0%{?el7}
/bin/touch --no-create %{_kf5_datadir}/icons/hicolor &>/dev/null || :
%endif

%postun
%if 0%{?el7}
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
%endif

%posttrans
%if 0%{?el7}
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
%endif

%files
%license LICENSE
%doc AUTHORS CHANGELOG CONTRIBUTING.md README.md
%{_bindir}/%{name}
%{_datadir}/metainfo/qterminal.metainfo.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-drop.desktop
%{_datadir}/icons/*/*
%{_datadir}/%{name}


%files l10n -f qterminal.lang
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%dir %{_datadir}/qterminal/translations

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 16 2022 Zamir SUN <sztsian@gmail.com> - 1.1.0-1
- new version

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 25 2021 zsun <sztsian@gmail.com> - 1.0.0-1
- Update to 1.0.0

* Sat Aug 07 2021 Zamir SUN <sztsian@gmail.com> - 0.17.0-1
- Update to 0.17.0

* Thu Aug 05 2021 Zamir SUN <sztsian@gmail.com> - 0.16.0-4
- Fix FTBFS
- Fixes RHBZ#1987909

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 Zamir SUN <sztsian@gmail.com> - 0.16.0-1
- Update to 0.16.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 03 2020 Zamir SUN <sztsian@gmail.com> - 0.15.0-1
- Update to 0.15.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 15 2019 Zamir SUN <sztsian@gmail.com> - 0.14.1-1
- Update to version 0.14.1

* Wed Feb 13 2019 Zamir SUN <zsun@fedoraproject.org>  - 0.14.0-1
- Prepare for LXQt 0.14.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 04 2018 Zamir SUN <zsun@fedoraproject.org> - 0.9.0-1
- Update to version 0.9.0
bump

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 22 2017 Christian Dersch <lupinix@mailbox.org> - 0.7.1-2
- require qtermwidget to be the same version as qterminal

* Wed Apr 19 2017 Christian Dersch <lupinix@mailbox.org> - 0.7.1-1
- new version
- removed Qt4 build (no longer supported by upstream)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 2 2015 TI_Eugene <ti.eugene@gmail.com> - 0.6.0-4
- Qt5 version added

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 10 2015 TI_Eugene <ti.eugene@gmail.com> - 0.6.0-2
- Rebuild with new qtermwidget

* Tue Nov 04 2014 TI_Eugene <ti.eugene@gmail.com> - 0.6.0-1
- Version bump

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 19 2013 TI_Eugene <ti.eugene@gmail.com> - 0.4.0-5
- Next git snapshot
- Changelog dates (year) fixed

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 07 2013 TI_Eugene <ti.eugene@gmail.com> - 0.4.0-3
- Source URL update
- second desktop validate added

* Mon May 06 2013 TI_Eugene <ti.eugene@gmail.com> - 0.4.0-2
- Source URL update

* Mon May 06 2013 TI_Eugene <ti.eugene@gmail.com> - 0.4.0-1
- initial packaging for Fedora
