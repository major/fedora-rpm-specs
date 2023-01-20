%define nameapp pencil2d

Name:           Pencil2D
Version:        0.6.6
Release:        6%{?dist}
Summary:        Animation/drawing software
License:        GPLv2
URL:            https://github.com/pencil2d/pencil
Source0:        %{url}/archive/v%{version}/pencil-%{version}.tar.gz
#  set fixed stack value, because MISIGSTKSZ is no longer constexpr
Patch0:         %{name}-constexpr-sigstacksz-fix.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtxmlpatterns-devel
Requires:       hicolor-icon-theme

%description
Pencil2D lets you create traditional hand-drawn animation

%prep
%setup -q -n pencil-%{version}

%patch -p1

%build
%{qmake_qt5} PREFIX=%{_prefix}
%make_build

%install
export INSTALL_ROOT=%{buildroot}
%make_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

# Run catch tests
./tests/bin/tests

%files
%license LICENSE.TXT
%doc docs/*
%{_bindir}/%{nameapp}
%{_datadir}/applications/*.desktop
%{_datadir}/bash-completion/completions/%{nameapp}
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/metainfo/org.%{nameapp}.*
%{_datadir}/mime/packages/org.%{nameapp}.*
%{_datadir}/zsh/site-functions/_%{nameapp}


%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Aug 22 2021 Andy Mender <andymenderunix@fedoraproject.org> - 0.6.6-3
- Add patch to fix stack size in tests

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Mar 7 2021 Andy Mender <andymenderunix@fedoraproject.org> - 0.6.6-1
- Update to version 0.6.6
- Remove CJK character workaround

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 29 2020 Andy Mender <andymenderunix@fedoraproject.org> - 0.6.5-3
- Re-enable tests

* Mon Nov 23 2020 Andy Mender <andymenderunix@fedoraproject.org> - 0.6.5-2
- Change URL and Source0 to primary upstream URL
- List only mandatory BuildRequires
- Fix buildroot name in %%prep stage
- Clean up %%build stage
- Add locale fix for CJK filenames in test resources
- Add tests to %%check stage (currently disabled)
- Fix %%files paths

* Wed Aug 26 2020 Luis M. Segundo <blackfile@fedoraproject.org> - 0.6.5-1
- Update to 0.6.5

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Marie Loise Nolden <loise@kde.org> - 0.6.4-4
- Fix for Qt 5.15.0 

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 2019 Luis M. Segundo <blackfile@fedoraproject.org> - 0.6.4-1
- Update to 0.6.4

* Thu Mar 21 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.6.3-2
- Fix comment #17 BZ #1632851 and #1691144

* Sun Mar 17 2019 Luis M. Segundo <blackfile@fedoraproject.org> - 0.6.3-1
- Update to 0.6.3

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 16 2018 Luis M. Segundo <blackfile@fedoraproject.org> - 0.6.2-1
- first release
