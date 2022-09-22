%global _description %{expand:
MOD2C is NMODL to C adapted for CoreNEURON simulator.
}

# Using a snapshot: upstream does not tag releases
%global commit 5a7f820748a0ff8443dc7bdabfb371f2a042d053
%global checkoutdate 20201009

Name:       mod2c
Version:    2.1.0
Release:    5.%{checkoutdate}git%{commit}%{?dist}
Summary:    NMODL to C adapted for CoreNEURON simulator

License:    BSD
URL:        https://github.com/BlueBrain/mod2c
Source0:    %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  bison bison-devel
BuildRequires:  flex
BuildRequires:  (flex-devel or libfl-devel)

%description %_description

%prep
%autosetup -n %{name}-%{commit}

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
