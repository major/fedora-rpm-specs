%global debug_package %{nil}

Name:           eglexternalplatform
Version:        1.2
Release:        3%{?dist}
Summary:        EGL External Platform Interface headers
License:        MIT
URL:            https://github.com/NVIDIA
BuildArch:      noarch

Source0:        %url/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-noarch.patch

BuildRequires:  meson

%description
%summary

%package        devel
Summary:        Development files for %{name}

%description    devel
The %{name}-devel package contains the header files for
developing applications that use %{name}.

%prep
%autosetup

%build
%meson

%install
%meson_install

%files devel
%doc README.md samples
%license COPYING
%{_includedir}/*
%{_datadir}/pkgconfig/eglexternalplatform.pc

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Simone Caronni <negativo17@gmail.com> - 1.2-2
- Adjust path of generated pkg-config file so it's still considered noarch.

* Thu Aug 08 2024 Simone Caronni <negativo17@gmail.com> - 1.2-1
- Update to 1.2.

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Sep 07 2023 José Expósito <jexposit@redhat.com> - 1.1-6
- SPDX migration: license is already SPDX compatible

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Sep 18 2021 Leigh Scott <leigh123linux@gmail.com> - 1.1-1
- Switch to release

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.7.20180916git7c8f8e2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.6.20180916git7c8f8e2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.5.20180916git7c8f8e2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.4.20180916git7c8f8e2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.3.20180916git7c8f8e2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.2.20180916git7c8f8e2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 20 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1-0.1.20180916git7c8f8e2
- Update snapshot

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.7.20170201git76e2948
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.6.20170201git76e2948
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.5.20170201git76e2948
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.4.20170201git76e2948
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0-0.3.20170201git76e2948
- Update snapshot
- Change to noarch
- Add license file

* Fri Jan 20 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0-0.2.20170120git53bf47c
- Add date to release

* Thu Jan 19 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0-0.1.git53bf47c
- First build

