# Disable tests because some of the tools are not available in Fedora
%bcond_with tests

Name:          flacon
Version:       11.4.0
Release:       3%{?dist}
Summary:       Audio File Encoder

License:       LGPL-2.1-or-later
URL:           https://flacon.github.io/
Source0:       https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  uchardet-devel
BuildRequires:  pkgconfig(taglib)
# For %%check
BuildRequires:  %{_bindir}/appstream-util
BuildRequires:  %{_bindir}/desktop-file-validate
%if %{with tests}
# Test deps
BuildRequires:  %{_bindir}/mac
BuildRequires:  %{_bindir}/flac
BuildRequires:  %{_bindir}/wavpack
BuildRequires:  %{_bindir}/ttaenc
%endif
BuildRequires: make
BuildRequires: zlib-devel

# formats/aac.h (encoder)
Recommends:     %{_bindir}/faac
# formats/ape.h (decoder)
Recommends:     %{_bindir}/mac
# formats/flac.h (encoder, decoder)
Recommends:     %{_bindir}/flac
# formats/mp3.h (encoder)
Recommends:     %{_bindir}/lame
# formats/ogg.h (encoder)
Recommends:     %{_bindir}/oggenc
# formats/opus.h (encoder)
Recommends:     %{_bindir}/opusenc
# formats/tta.h (decoder)
Recommends:     %{_bindir}/ttaenc
# formats/wv.h (encoder)
Recommends:     %{_bindir}/wavpack
# formats/wc.h (decoder)
Recommends:     %{_bindir}/wvunpack

%description
Flacon extracts individual tracks from one big audio file containing
the entire album of music and saves them as separate audio files. 
To do this, it uses information from the appropriate CUE file. 
Besides, Flacon makes it possible to conveniently revise or specify 
tags both for all tracks at once or for each tag separately.

%prep
%autosetup -p1

%build
%cmake -DBUILD_TESTS=%{?with_tests:Yes}%{!?with_tests:No}
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-qt

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/com.github.Flacon.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%if %{with tests}
cd %{_target_platform}/tests && ./flacon_test
%endif

%files -f %{name}.lang
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_datadir}/metainfo/com.github.Flacon.metainfo.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_mandir}/man1/%{name}.1*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 11.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed May 29 2024 Ilia Gradina <ilgrad@fedoraproject.org> - 11.4.0-1
- Update to 11.4.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Oct  6 2023 Ilia Gradina <ilgrad@fedoraproject.org> - 11.3.0-1
- Update to 11.3.0

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jun 18 2023 Vasiliy Glazov <vascom2@gmail.com> - 11.2.0-1
- Update to 11.2.0

* Tue May 23 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 11.0.0-1
- Update to 11.0.0

* Mon Jan 23 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 10.0.0-1
- Update to 10.0.0
- Drop unneeded Recommends

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 21 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 9.5.1-1
- Update to 9.5.1

* Fri Nov 18 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 9.5.0-1
- Update to 9.5.0

* Mon Oct 03 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 9.4.0-1
- Update to 9.4.0

* Sat Sep 24 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 9.3.0-1
- Update to 9.3.0

* Tue Aug 30 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 9.2.0-1
- Update to 9.2.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 9.1.0-1
- Update to 9.1.0

* Sat Apr 30 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 9.0.0-1
- Update to 9.0.0

* Tue Feb 08 2022 Timothée Ravier <tim@siosm.fr> - 8.3.0-2
- Use AppStream metadata from upstream

* Fri Feb 04 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 8.3.0-1
- Update to 8.3.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 21 2021 Vasiliy Glazov <vascom2@gmail.com> - 8.2.0-1
- Update to 8.2.0

* Mon Nov 29 2021 Vasiliy Glazov <vascom2@gmail.com> - 8.1.0-1
- Update to 8.1.0

* Tue Nov 16 2021 Vasiliy Glazov <vascom2@gmail.com> - 8.0.0-1
- Update to 8.0.0

* Wed Jul 28 2021 Vasiliy Glazov <vascom2@gmail.com> - 7.0.1-3
- Fix FTBFS

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Apr 26 2021 Vasiliy Glazov <vascom2@gmail.com> - 7.0.1-1
- Update to 7.0.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 21 2020 Vasiliy Glazov <vascom2@gmail.com> - 6.1.0-1
- Update to 6.1.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 23 2019 Ilya Gradina <ilya.gradina@gmail.com> - 5.5.1-1
- Update tp 5.5.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 2019 Ilya Gradina <ilya.gradina@gmail.com> - 5.4.0-1
- Update to 5.4.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 24 2018 Ilya Gradina <ilya.gradina@gmail.com> - 5.0.0-1
- Update to 5.0.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Ilya Gradina <ilya.gradina@gmail.com> - 4.1.0-1
- Update to 4.1.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.0.0-1.1
- Remove obsolete scriptlets

* Sun Dec 24 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.0.0-1
- Update to 4.0.0

* Sun Oct 01 2017 Ilya Gradina <ilya.gradina@gmail.com> - 3.1.1-4
- rebuilt package

* Tue Sep 12 2017 Than Ngo <than@redhat.com> - 3.1.1-3
- enable build on ppc64

* Mon Sep 11 2017 Ilya Gradina <ilya.gradina@gmail.com> - 3.1.1-2
- fix build on ppc64 

* Sat Aug 12 2017 Ilya Gradina <ilya.gradina@gmail.com> - 3.1.1-1
- update to 3.1.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 29 2017 Ilya Gradina <ilya.gradina@gmail.com> - 3.0.0-1
- update to 3.0.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 28 2016 Ilya Gradina <ilya.gradina@gmail.com> - 2.1.1-1
- update to 2.1.1

* Thu Nov 10 2016 Ilya Gradina <ilya.gradina@gmail.com> - 2.1.0-1
- update to 2.1.0

* Wed Aug 17 2016 Ilya Gradina <ilya.gradina@gmail.com> - 2.0.1-5
- changes in appdata file

* Tue May 10 2016 Ilya Gradina <ilya.gradina@gmail.com> - 2.0.1-4
- remove the requires libfishsound
- changes in the appdata.xml file

* Sat May  7 2016 Ilya Gradina <ilya.gradina@gmail.com> - 2.0.1-3
- added xml file

* Sat Apr 30 2016 Ilya Gradina <ilya.gradina@gmail.com> - 2.0.1-2
- changes in the file, thx Jiri Eischmann 1264715#c3

* Wed Apr 27 2016 Ilya Gradina <ilya.gradina@gmail.com> - 2.0.1-1
- update to 2.0.1 
- few small changes

* Mon Sep 21 2015 Ilya Gradina <ilya.gradina@gmail.com> - 1.2.0-1
- Initial package
