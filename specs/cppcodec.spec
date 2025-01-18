%global debug_package %{nil}

Name:           cppcodec
Version:        0.2
Release:        14%{?dist}
Summary:        Header-only C++11 library to encode/decode base64/base64url/base32/base32hex/hex

License:        MIT
URL:            https://github.com/tplgy/cppcodec
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake >= 3.12
BuildRequires:  gcc-c++
BuildRequires:  catch2-devel

%global _description \
Header-only C++11 library to encode/decode base64, base64url, base32, base32hex\
and hex (a.k.a. base16) as specified in RFC 4648, plus Crockford's base32.\
\
MIT licensed with consistent, flexible API. Supports raw pointers,\
std::string and (templated) character vectors without unnecessary allocations.

%description %{_description}

%package        devel
Summary:        %{summary}
Provides:       %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}

%description    devel %{_description}

%prep
%autosetup -p1
# No bundled catch
rm -vrf test/catch

%build
%cmake -DBUILD_TESTING=TRUE
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%license LICENSE
%doc README.md
%{_includedir}/%{name}/
%{_datadir}/pkgconfig/%{name}-1.pc

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 20 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2-1
- Update to 0.2

* Mon Jul 23 2018 Tom Hughes <tom@compton.nu> - 0.1-3
- Patch for changes in catch2 pkg-config module name

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1-1
- Update to 0.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20171003.git.65e512d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 02 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0-0.20171002.git.65e512d
- Update to latest snapshot

* Tue Apr 04 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0-0.20170404.git.61d9b04
- Initial package
