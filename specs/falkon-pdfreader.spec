%global gitcommit_full dcb8453c21a4562727215e899dad083637bc30d3
%global gitcommit %(c=%{gitcommit_full}; echo ${c:0:7})
%global date 20200924

%global debug_package %{nil}

Name:           falkon-pdfreader
Version:        0
Release:        0.19.%{date}git%{gitcommit}%{?dist}
Summary:        PDF reader extension for Falkon using pdf.js

# Automatically converted from old format: GPLv3+ and ASL 2.0 - review is highly recommended.
License:        GPL-3.0-or-later AND Apache-2.0
URL:            https://github.com/Tarptaeya/PDFReader
Source0:        %{url}/tarball/%{gitcommit_full}


# handled by qt5-srpm-macros, which defines %%qt5_qtwebengine_arches
%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel

Requires:       falkon%{?_isa} >= 3.1.0

%description
%{summary}.

%prep
%autosetup -n Tarptaeya-PDFReader-%{gitcommit}
mv pdfreader/pdfjs/LICENSE LICENSE_pdfjs


%build
%cmake_kf5


%install
%cmake_install


%files
%license LICENSE LICENSE_pdfjs
%doc README.md
%{_kf5_qtplugindir}/falkon/qml/pdfreader



%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19.20200924gitdcb8453
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug  7 2024 Miroslav Suchý <msuchy@redhat.com> - 0-0.18.20200924gitdcb8453
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.20200924gitdcb8453
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.20200924gitdcb8453
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.20200924gitdcb8453
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.20200924gitdcb8453
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20200924gitdcb8453
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jul 26 2022 Vasiliy Glazov <vascom2@gmail.com> - 0-0.12.20200924gitdcb8453
- Fix build

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.20200924gitdcb8453
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20200924gitdcb8453
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20200924gitdcb8453
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20200924gitdcb8453
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 25 2020 Vasiliy Glazov <vascom2@gmail.com> - 0-0.7.20200924gitdcb8453
- Update to latest git

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20200725gita37de6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Vasiliy Glazov <vascom2@gmail.com> - 0-0.4.20200725gita37de6f
- Update to latest git

* Tue Jun 23 2020 Vasiliy Glazov <vascom2@gmail.com> - 0-0.4.20190118giteefc135
- Correct build arches

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20190118giteefc135
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20190118giteefc135
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar  4 2019 Vasiliy Glazov <vascom2@gmail.com> - 0-0.1.20190118giteefc135
- Initial packaging
