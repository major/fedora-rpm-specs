Name:       pass-otp
Version:    1.2.0
Release:    17%{?dist}
Summary:    A pass extension for managing one-time-password (OTP) tokens
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:    GPL-3.0-or-later
BuildArch:  noarch
URL:        https://github.com/tadfisher/pass-otp
Source:     https://github.com/tadfisher/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# https://bugzilla.redhat.com/show_bug.cgi?id=2136582
Patch0:     %{name}-1.2.0-fix_hotp_counter.patch
BuildRequires: make
BuildRequires: expect
BuildRequires: git
BuildRequires: pass >= 1.7.0
BuildRequires: oathtool
Requires:   pass >= 1.7.0
Requires:   oathtool
Requires:   qrencode
Suggests:   zbar

%description
pass-otp extends the pass utility with the otp command for adding OTP secrets,
generating OTP codes, and displaying secret key URIs using the standard
otpauth:// scheme.

%prep
%autosetup

%build

%install
%make_install

%check
%make_build test

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{_usr}/lib/password-store/extensions/otp.bash
%{_mandir}/man1/%{name}.1*
%{_sysconfdir}/bash_completion.d/pass-otp

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.0-16
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 05 2022 Juan Orti Alcaine <jortialc@redhat.com> - 1.2.0-10
- Add patch to fix RHBZ#2136582

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Juan Orti Alcaine <jortialc@redhat.com> - 1.2.0-3
- Run tests

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 13 2019 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.2.0-1
- Version 1.2.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1.1-1
- Version 1.1.1

* Sun Apr 01 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1.0-2
- Requires: qrencode and pass >= 1.7.0

* Sat Mar 31 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1.0-1
- Initial release
