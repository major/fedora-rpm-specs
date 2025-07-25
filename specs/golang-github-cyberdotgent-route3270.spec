# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/cyberdotgent/route3270
%global goipath         github.com/cyberdotgent/route3270
Version:                0.2

%gometa

%global common_description %{expand:
A simple TN3270 router that can be used to route access to several applications
or machines behind a single gateway.

Features:
- Crude access control system for proxied services
- Authentication
- 2FA support using TOTP}

%global golicenses      COPYING
%global godocs          doc README.md

Name:           %{goname}
Release:        14%{?dist}
Summary:        A simple 3270 application/connection router

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  sed
BuildRequires:  golang(github.com/akamensky/argparse)
BuildRequires:  golang(github.com/BurntSushi/toml)
BuildRequires:  golang(github.com/pquerna/otp/totp)
BuildRequires:  golang(github.com/racingmars/go3270)
BuildRequires:  golang(github.com/rs/zerolog)
BuildRequires:  golang(github.com/rs/zerolog/log)

%description
%{common_description}

%package -n     route3270
Summary:        %{summary}

%description -n route3270
%{common_description}

%gopkg

%prep
%goprep
# Fix incorrect end-of-line encoding
sed -i 's/\r$//' README.md example.toml

%build
%gobuild -o %{gobuilddir}/bin/route3270 %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files -n route3270
%license COPYING
%doc doc README.md example.toml
%{_bindir}/*

%gopkgfiles

%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul  29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2-12
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 11 2024 Maxwell G <maxwell@gtmx.me> - 0.2-10
- Rebuild for golang 1.22.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Maxwell G <gotmax@e.email> - 0.2-4
- Rebuild for CVE-2022-{1705,32148,30631,30633,28131,30635,30632,30630,1962} in
  golang

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Apr  3 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.2-1
- Initial package

