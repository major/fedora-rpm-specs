Name:           diff-pdf
Version:        0.5.2
Release:        4%{?dist}
Summary:        A simple tool for visually comparing two PDF files

# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            http://vslavik.github.io/diff-pdf/
Source0:        https://github.com/vslavik/diff-pdf/archive/v%{version}/diff-pdf-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  automake
BuildRequires:  wxGTK-devel
BuildRequires:  poppler-glib-devel
BuildRequires:  make

%description
%{summary}.

%prep
%autosetup

%build
aclocal ${wx+-I} $wx -I admin
autoconf
automake --add-missing --copy --foreign
%configure --disable-silent-rules
%make_build


%install
%make_install


%files
%license COPYING COPYING.icons
%doc AUTHORS README.md
%{_bindir}/%{name}


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.2-3
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 06 2024 Vasiliy N. Glazov <vascom2@gmail.com> - 0.5.2-1
- Update to 0.5.2

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 30 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 0.5.1-1
- Update to 0.5.1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 04 2022 Scott Talbert <swt@techie.net> - 0.5-5
- Rebuild with wxWidgets 3.2

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 15 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 0.5-1
- Update to 0.5

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Marek Kasik <mkasik@redhat.com> - 0.4.1-5
- Do not require poppler-cairo
- It is not needed and drags in explicit dependency on poppler base library

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 09 2020 Vasiliy Glazov <vascom2@gmail.com> - 0.4.1-3
- Disable silent make rules, thanks Orion Poplawski

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Vasiliy Glazov <vascom2@gmail.com> - 0.4.1-1
- Update to 0.4.1

* Thu Jan 09 2020 Vasiliy Glazov <vascom2@gmail.com> - 0.4-1
- Update to 0.4

* Fri Nov 15 2019 Vasiliy Glazov <vascom2@gmail.com> - 0.3-1
- Initial release
