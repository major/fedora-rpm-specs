%global _description %{expand:
MOD2C is NMODL to C adapted for CoreNEURON simulator.
}

# Using a snapshot: upstream does not tag releases
%global commit 5a7f820748a0ff8443dc7bdabfb371f2a042d053
%global checkoutdate 20201009

Name:       mod2c
Version:    2.1.0
Release:    13.%{checkoutdate}git%{commit}%{?dist}
Summary:    NMODL to C adapted for CoreNEURON simulator

# Automatically converted from old format: BSD - review is highly recommended.
License:    LicenseRef-Callaway-BSD
URL:        https://github.com/BlueBrain/mod2c
Source0:    %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch0:     mod2c-c99.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  bison bison-devel
BuildRequires:  flex
BuildRequires:  (flex-devel or libfl-devel)

%description %_description

%prep
%autosetup -p1 -n %{name}-%{commit}

%build
%cmake -DUNIT_TESTS=ON -DFUNCTIONAL_TESTS=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE.txt
%doc README.md CREDIT.txt
%{_bindir}/mod2c_core
%{_datadir}/nrnunits.lib

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-13.20201009git5a7f820748a0ff8443dc7bdabfb371f2a042d053
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.0-12.20201009git5a7f820748a0ff8443dc7bdabfb371f2a042d053
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-11.20201009git5a7f820748a0ff8443dc7bdabfb371f2a042d053
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-10.20201009git5a7f820748a0ff8443dc7bdabfb371f2a042d053
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-9.20201009git5a7f820748a0ff8443dc7bdabfb371f2a042d053
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8.20201009git5a7f820748a0ff8443dc7bdabfb371f2a042d053
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7.20201009git5a7f820748a0ff8443dc7bdabfb371f2a042d053
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Florian Weimer <fweimer@redhat.com> - 2.1.0-6.20201009git5a7f820748a0ff8443dc7bdabfb371f2a042d053
- C99 compatibility fixes

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5.20201009git5a7f820748a0ff8443dc7bdabfb371f2a042d053
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4.20201009git5a7f820748a0ff8443dc7bdabfb371f2a042d053
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3.20201009git5a7f820748a0ff8443dc7bdabfb371f2a042d053
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2.20201009git5a7f820748a0ff8443dc7bdabfb371f2a042d053
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 09 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.1.0-1.20201009git5a7f820748a0ff8443dc7bdabfb371f2a042d053
- Initial build
