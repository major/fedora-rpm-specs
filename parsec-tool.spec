%bcond_without check
%global __cargo_is_lib() 0

Name:          parsec-tool
Version:       0.4.0
Release:       8%{?dist}
Summary:       A PARSEC cli

# ASL 2.0
# BSD
# MIT
# MIT or ASL 2.0
# Unlicense or MIT
# Automatically converted from old format: ASL 2.0 and BSD and MIT - review is highly recommended.
License:       Apache-2.0 AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT
URL:           https://github.com/parallaxsecond/parsec-tool
Source0:       %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:        parsec-tool-fixmetadata.diff

BuildRequires: rust-packaging

%description
A tool to communicate with the Parsec service on the command-line.

%prep
%autosetup -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%{_bindir}/parsec-tool

%changelog
* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4.0-8
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Mar 10 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 0.4.0-6
- Build against parsec 1.3

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 20 2023 Fabio Valentini <decathorpe@gmail.com> - 0.4.0-2
- Simplify spec and update for latest Rust packaging.

* Wed Feb 08 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0

* Tue Feb 07 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 0.3.1-5
- Rebuild for tss-esapi 7.2.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Aug 08 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Mar 20 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 28 13:26:39 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.1.0-2
- Rebuild

* Thu Oct 22 2020 Peter Robinson <pbrobinson@fedoraproject.org> 0.1.0-1
- Initial packaging
