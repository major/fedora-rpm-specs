%global commit ae8f4d5374f53cd07f965b53b1cf3f9b3254194c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20250403
%global base_name release-keyring

Name:    kde-release-keyring
Version: 0~git%{commitdate}.%{shortcommit}
Release: 7%{?dist}
Summary: Keyring of signing keys from KDE community members

License: CC0-1.0
URL:     https://invent.kde.org/sysadmin/%{base_name}/
Source0: %{url}/-/archive/%{commit}/%{base_name}-%{shortcommit}.tar.gz

BuildArch:     noarch
BuildRequires: gnupg2

%description
%{summary}.

%prep
%autosetup -n %{base_name}-%{commit} -p1


%build
gpg --options /dev/null --no-default-keyring --keyring ./%{base_name}.kbx --import ./keys/*.asc


%install
install -m644 -p -D %{base_name}.kbx %{buildroot}%{_datadir}/%{name}/%{base_name}.kbx
install -d %{buildroot}%{_datadir}/%{name}/keys
install -m644 -p -D keys/* %{buildroot}%{_datadir}/%{name}/keys


%files
%license LICENSES/CC0-1.0.txt
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/keys/
%{_datadir}/%{name}/%{base_name}.kbx
%{_datadir}/%{name}/keys/*.asc


%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0~git20250403.ae8f4d5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon May 05 2025 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 0~git20250403.ae8f4d5-6
- Use 0~ for the versioning and fix changelog entries

* Wed Apr 30 2025 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 0~git20250403.ae8f4d5-5
- Use proper .kbx extension for the keyring

* Sun Apr 27 2025 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 0~git20250403.ae8f4d5-4
- Use proper version in changelog

* Fri Apr 25 2025 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 0~git20250403.ae8f4d5-3
- Reuse %%{url}
- Include individual keys
- Set noarch build
- Improve summary
- Install under %%{_datadir}/%%{name}
- Install CC0-1.0 license file

* Fri Apr 25 2025 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 0~git20250403.ae8f4d5-2
- Fix License field

* Thu Apr 24 2025 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 0~git20250403.ae8f4d5-1
- Initial import
