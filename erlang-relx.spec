%global realname relx
%global upstream erlware

Name:     erlang-%{realname}
Version:  4.7.0
Release:  2%{?dist}
BuildArch: noarch
Summary:  Release assembler for Erlang/OTP Releases
License:  ASL 2.0
URL:      https://github.com/%{upstream}/%{realname}
Source0:  https://github.com/%{upstream}/%{realname}/archive/v%{version}/%{realname}-%{version}.tar.gz
BuildRequires:  erlang-rebar3

%description
Relx assembles releases for an Erlang/OTP release. Given a release
specification and a list of directories in which to search for OTP applications
it will generate a release output.

%prep
%autosetup -p1 -n %{realname}-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%license LICENSE.md
%doc README.md
%{erlang_appdir}/

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 23 2022 Peter Lemenkov <lemenkov@gmail.com> - 4.7.0-1
- New version

* Thu Feb 17 2022 Peter Lemenkov <lemenkov@gmail.com> - 4.6.0-2
- Switch to rebar3

* Wed Feb  2 2022 Peter Lemenkov <lemenkov@gmail.com> - 4.6.0-1
- New version

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec  1 2020 Peter Lemenkov <lemenkov@gmail.com> - 4.1.0-1
- New version

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 04 2019 Timothée Floure <fnux@fedoraproject.org> - 3.32.1-1
- New upstream release

* Wed May 15 2019 Timothée Floure <fnux@fedoraproject.org> - 3.31.0-1
- New upstream release

* Tue Feb 05 2019 Timothée Floure <fnux@fedoraproject.org> - 3.28.0-1
- New upstream release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 13 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.26.0-3
- Convert into a noarch package.
- Rebuild against the noarch bbmustache (#1638979).

* Thu Oct 11 2018 Timothée Floure <fnux@fedoraproject.org> - 3.26.0-2
- Fix runtime dependency on bbmustache

* Sun Jul 15 2018 Timothée Floure <fnux@fedoraproject.org> - 3.26.0-1
- Let there be package
