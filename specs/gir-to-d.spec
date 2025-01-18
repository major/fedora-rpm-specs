Name:           gir-to-d
Version:        0.23.2
Release:        5%{?dist}
Summary:        Tool to create D bindings from GObject introspection files

License:        LGPL-3.0-or-later
URL:            https://github.com/gtkd-developers/gir-to-d
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  ldc
BuildRequires:  meson

ExclusiveArch:  %{ldc_arches}

%description
%{name} is a tool to create D bindings using GObject Introspection
repository files, enabling quick and easy use of various libraries
written using GObject conventions with the D language.

%prep
%autosetup -p1


%build
# Pass -allinst to ldc to work around an undefined reference build issue
# https://github.com/ldc-developers/ldc/issues/4000
export DFLAGS="%{_d_optflags} -allinst"
# Drop '-specs=/usr/lib/rpm/redhat/redhat-hardened-ld' as LDC doesn't support it
export LDFLAGS="-Wl,-z,relro"
%meson
%meson_build


%install
%meson_install


%files
%license COPYING
%doc Readme_APILookup
%attr(0755, -, -) %{_bindir}/girtod


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 18 2024 Kalev Lember <klember@redhat.com> - 0.23.2-4
- Rebuilt for ldc 1.40

* Tue Aug 06 2024 Kalev Lember <klember@redhat.com> - 0.23.2-3
- Rebuilt for ldc 1.39

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 13 2024 Neal Gompa <ngompa@fedoraproject.org> - 0.23.2-1
- Update to 0.23.2

* Sun Feb 11 2024 Neal Gompa <ngompa@fedoraproject.org> - 0.23.1-1
- Update to 0.23.1

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 17 2023 Kalev Lember <klember@redhat.com> - 0.22.0-12
- Rebuilt for ldc 1.35

* Mon Jul 24 2023 Kalev Lember <klember@redhat.com> - 0.22.0-11
- Rebuilt for ldc 1.33

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 15 2023 Kalev Lember <klember@redhat.com> - 0.22.0-9
- Rebuilt for ldc 1.32

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 27 2022 Kalev Lember <klember@redhat.com> - 0.22.0-7
- Rebuilt for ldc 1.30

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Apr 16 2022 Neal Gompa <ngompa@fedoraproject.org> - 0.22.0-5
- Backport fix to stop segfaulting with glib 2.72

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 17 2021 Kalev Lember <klember@redhat.com> - 0.22.0-3
- Rebuilt for ldc 1.27

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Feb 28 2021 Neal Gompa <ngompa13@gmail.com> - 0.22.0-1
- Update to 0.22.0 (#1920123)

* Mon Feb 22 2021 Kalev Lember <klember@redhat.com> - 0.21.0-4
- Rebuilt for ldc 1.25

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 21 2020 Neal Gompa <ngompa13@gmail.com> - 0.21.0-2
- Backport fix for new gobject-introspection

* Sun Aug 23 2020 Neal Gompa <ngompa13@gmail.com> - 0.21.0-1
- Update to 0.21.0 (#1813730)

* Fri Aug 21 2020 Kalev Lember <klember@redhat.com> - 0.20.0-3
- Rebuilt for ldc 1.23

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb 23 2020 Neal Gompa <ngompa13@gmail.com> - 0.20.0-1
- Update to 0.20.0 (#1714618)

* Mon Feb 10 2020 Kalev Lember <klember@redhat.com> - 0.19.0-4
- Rebuilt for ldc 1.20

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Neal Gompa <ngompa13@gmail.com> - 0.19.0-1
- Update to 0.19.0 (#1689701)

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 0.18.0-4
- Rebuild with Meson fix for #1699099

* Tue Apr 09 2019 Kalev Lember <klember@redhat.com> - 0.18.0-3
- Rebuilt for ldc 1.15

* Mon Feb 18 2019 Kalev Lember <klember@redhat.com> - 0.18.0-2
- Rebuilt for ldc 1.14

* Fri Feb 01 2019 Neal Gompa <ngompa13@gmail.com> - 0.18.0-1
- Update to 0.18.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Neal Gompa <ngompa13@gmail.com> - 0.17.0-1
- Update to 0.17.0

* Sun Oct 14 2018 Kalev Lember <klember@redhat.com> - 0.15.0-2
- Rebuilt for ldc 1.12

* Sun Jul 22 2018 Neal Gompa <ngompa13@gmail.com> - 0.15.0-1
- Update to 0.15.0 (#1563200)
- Add gcc BR to fix build in F29+ (#1604109)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Kalev Lember <klember@redhat.com> - 0.13.0-4
- Rebuilt for ldc 1.11

* Mon Feb 19 2018 Kalev Lember <klember@redhat.com> - 0.13.0-3
- Rebuilt for ldc 1.8

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 03 2017 Neal Gompa <ngompa13@gmail.com> - 0.13.0-1
- Update to 0.13.0 (#1504366)

* Wed Sep 13 2017 Kalev Lember <klember@redhat.com> - 0.11.0-4
- Rebuilt for ldc 1.4

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 23 2017 Neal Gompa <ngompa13@gmail.com> - 0.11.0-1
- Update to 0.11.0 (#1464388)

* Mon Jun 19 2017 Neal Gompa <ngompa13@gmail.com> - 0.10.0-1
- Initial packaging
