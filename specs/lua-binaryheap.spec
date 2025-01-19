%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))" || echo 0)}
%global luapkgdir %{_datadir}/lua/%{luaver}

%global luacompatver 5.1
%global luacompatpkgdir %{_datadir}/lua/%{luacompatver}

%global majorversion 0
%global minorversion 4
%global tagname version_%{majorversion}v%{minorversion}

%global luapkgname binaryheap

Name:           lua-%{luapkgname}
Version:        %{majorversion}.%{minorversion}
Release:        14%{?dist}
Summary:        Binary heap implementation for Lua

License:        MIT
URL:            https://github.com/Tieske/%{luapkgname}.lua
Source0:        https://github.com/Tieske/%{luapkgname}.lua/archive/%{tagname}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  lua

%description
A Lua library implementing binary heap algorithm.

%if 0%{?fedora} || 0%{?rhel} > 7
%package -n lua%{luacompatver}-%{luapkgname}
Summary:        Binary heap implementation for Lua %{luacompatver}

%description -n lua%{luacompatver}-%{luapkgname}
A Lua library implementing binary heap algorithm.
%endif

%prep
%setup -q -n binaryheap.lua-%{tagname}

%install
install -D -p -m 0644 src/binaryheap.lua %{buildroot}/%{luapkgdir}/binaryheap.lua

%if 0%{?fedora} || 0%{?rhel} > 7
install -D -p -m 0644 src/binaryheap.lua %{buildroot}/%{luacompatpkgdir}/binaryheap.lua
%endif

%files
%doc docs/*
%doc examples
%{luapkgdir}/binaryheap.lua

%if 0%{?fedora} || 0%{?rhel} > 7
%files -n lua%{luacompatver}-%{luapkgname}
%doc docs/*
%doc examples
%{luacompatpkgdir}/binaryheap.lua
%endif

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 03 2019 Tomas Krizek <tomas.krizek@nic.cz> - 0.4-1
- Initial package for Fedora 28+ and EPEL 7
