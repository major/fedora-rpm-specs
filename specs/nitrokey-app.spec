Name:           nitrokey-app
Version:        1.4.2
Release:        12%{?dist}
Summary:        Nitrokey's Application

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/Nitrokey/nitrokey-app
Source0:        %{url}/archive/v%{version_no_tilde -}/%{name}-%{version}.tar.gz
# Non-upstreamable, required to unbundle libraries
Patch0001:      0001-don-t-show-information-about-3rd-party-licenses.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.1.0
BuildRequires:  ninja-build
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(libnitrokey-1) >= 3.5
BuildRequires:  pkgconfig(cppcodec-1)
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  /usr/bin/appstream-util
Requires:       hicolor-icon-theme

%description
%{summary}.

%prep
%autosetup -p1
# Remove 3rdparty libraries
rm -vr 3rdparty
# Unbundle libnitrokey
rm -vr libnitrokey

%build
%cmake %{_vpath_srcdir} -B%{_vpath_builddir} -GNinja \
  -DADD_GIT_INFO=FALSE \
  %{nil}
%ninja_build -C %{_vpath_builddir}

%install
%ninja_install -C %{_vpath_builddir}

# We don't need ubuntu icons
rm -vr %{buildroot}%{_datadir}/icons/ubuntu*

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/com.nitrokey.%{name}.appdata.xml

%files
%license LICENSES/GPLv3
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/com.nitrokey.%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/pixmaps/%{name}.png
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4.2-11
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 23 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.4.2-1
- Update to 1.4.2

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4-1
- Update to 1.4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2-2
- Remove obsolete scriptlets

* Sun Dec 24 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2-1
- Update to 1.2

* Tue Oct 17 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2-0.2.beta.3
- Make sure to remove Ubuntism

* Tue Oct 17 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2-0.1.beta.3
- Update to 1.2-beta.3

* Tue Oct 17 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1-2
- Remove nitrokey-app.debug

* Sat Oct 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1-1
- Update to 1.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.6.3-1
- Update to 0.6.3 (RHBZ #1415861)

* Mon Jan 09 2017 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.6.2-1
- Update to 0.6.2 (RHBZ #1409940)

* Fri Dec 02 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.6.1-1
- Update to 0.6.1 (RHBZ #1400736)

* Fri Nov 18 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.5.1-1
- Initial package
