Name:           kaudiocreator
Version:        1.3
Release:        28%{?dist}
Summary:        Program for ripping and encoding Audio-CDs

License:        GPLv2+
URL:            http://kde-apps.org/content/show.php?content=107645
Source0:        http://kde-apps.org/CONTENT/content-files/107645-%{name}-%{version}.tar.bz2

Patch:          kaudiocreator-1.3-deskfile.patch

BuildRequires:  cmake
BuildRequires:  phonon-devel
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  libkcompactdisc-devel
BuildRequires:  libkcddb-devel
BuildRequires:  kdelibs-devel
BuildRequires:  libdiscid-devel
BuildRequires:  taglib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  make

%if 0%{?rhel}
Requires:       kdemultimedia
%else
Requires:       kio_audiocd
%endif


%description
KAudioCreator is a program for ripping and
encoding Audio-CDs, encoding files from disk.

%prep
%setup -q
# fix permisions
%patch -p0


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

desktop-file-validate %{buildroot}%{_kde4_datadir}/applications/kde4/kaudiocreator.desktop

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING COPYING.DOC Changelog
%{_kde4_bindir}/kaudiocreator
%{_kde4_datadir}/applications/kde4/kaudiocreator.desktop
%{_kde4_datadir}/config.kcfg/kaudiocreator.kcfg
%{_kde4_datadir}/config.kcfg/kaudiocreator_encoders.kcfg
%{_kde4_datadir}/kde4/services/ServiceMenus/audiocd_extract.desktop
%{_kde4_appsdir}/kaudiocreator
%{_kde4_appsdir}/kconf_update/kaudiocreator*.upd
%{_kde4_appsdir}/kconf_update/upgrade-kaudiocreator-metadata.sh
%{_kde4_iconsdir}/hicolor/*/apps/kaudiocreator.png


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3-17
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 06 2017 Dmitrij S. kryzhevich <kryzhev@ispms.ru> - 1.3-14
- Fix spec to KDE5.
- Fix bogus dates.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3-10
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 27 2013 Dmitrij S. Kryzhevich <krege@land.ru> 1.3-6
- Add special epel Requires.

* Tue Feb 26 2013 Dmitrij S. Kryzhevich <krege@land.ru> 1.3-5
- Fix audiocd-kio dependency issue again. Now in kio_audiocd way.

* Tue Jan 29 2013 Dmitrij S. Kryzhevich <krege@land.ru> 1.3-4
- Fix audiocd-kio dependency issue.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 05 2011 Dmitrij S. Kryzhevich <krege@land.ru> 1.3-1
- Update to 1.3 release.
- Drop -lib patch.
- Add patch to fix permisions for .desktop file.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 03 2010 Dmitrij S. Kryzhevich <krege@land.ru> 1.2.90-2
- Spec cleanup.
- Remove gtk2 from BR.

* Wed Nov 03 2010 Dmitrij S. Kryzhevich <krege@land.ru> 1.2.90-1
- Initial build.