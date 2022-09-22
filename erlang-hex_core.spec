%global upstream hexpm
%global realname hex_core

Name:     erlang-%{realname}
Version:  0.7.1
Release:  5%{?dist}
Summary:  Reference implementation of Hex specifications
License:  ASL 2.0
URL:      https://github.com/%{upstream}/%{realname}
Source0:  https://github.com/%{upstream}/%{realname}/archive/v%{version}/%{realname}-%{version}.tar.gz
BuildArch:     noarch
BuildRequires: erlang-rebar3
BuildRequires: erlang-proper

%description
%{summary}.

%prep
%autosetup -p1 -n %{realname}-%{version}

%build
{%erlang3_compile}

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%license LICENSE
%doc README.md
%{erlang_appdir}/

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 17 2022 Peter Lemenkov <lemenkov@gmail.com> - 0.7.1-4
- Move to rebar3

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec  1 2020 Peter Lemenkov <lemenkov@gmail.com> - 0.7.1-1
- New version

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Timothée Floure <fnux@fedoraproject.org> - 0.4.0-1
- Let there be package
