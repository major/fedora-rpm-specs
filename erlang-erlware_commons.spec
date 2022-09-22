%global realname erlware_commons
%global upstream erlware

Name:     erlang-%{realname}
Version:  1.6.0
Release:  2%{?dist}
Summary:  Extension to Erlang's standard library
License:  MIT
URL:      https://github.com/%{upstream}/%{realname}
Source0:  https://github.com/%{upstream}/%{realname}/archive/v%{version}/%{realname}-%{version}.tar.gz
# The "color" test does not play well with Fedora's build system
Patch1:   erlang-erlware_commons-0001-Disable-color-test.patch
Patch2:   erlang-erlware_commons-0002-Use-correct-version-instead-of-relying-to-git-one.patch
Patch3:   erlang-erlware_commons-0003-Disable-git-tests-in-Fedora-Koji.patch
BuildArch:     noarch
BuildRequires: erlang-rebar
BuildRequires: erlang-cf

%description
%{summary}.

%prep
%autosetup -p1 -n %{realname}-%{version}

%build
%{erlang_compile}

%install
%{erlang_install}
cp -arv priv/ %{buildroot}%{erlang_appdir}/

%check
%{erlang_test}

%files
%doc README.md
%{erlang_appdir}/

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Feb  2 2022 Peter Lemenkov <lemenkov@gmail.com> - 1.6.0-1
- Ver. 1.6.0

* Wed Jan 26 2022 Peter Lemenkov <lemenkov@gmail.com> - 1.3.1-8
- Fix FTBFS

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec  1 2020 Peter Lemenkov <lemenkov@gmail.com> - 1.3.1-5
- Don't list deps explicitly

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Timothée Floure <fnux@fedoraproject.org> - 1.3.1-1
- New upstream release
- Use source archive from hex.pm since upstream did not provide 'github release'
- Switch to noarch (Changes/TrueNoarchErlangPackages)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Timothée Floure <fnux@fedoraproject.org> - 1.2.0-1
- Let there be package
