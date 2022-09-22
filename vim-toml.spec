%global commit      717bd87ef928293e0cc6cfc12ebf2e007cb25311
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           vim-toml
Version:        0^1.%{shortcommit}
Release:        3%{?dist}
Summary:        Vim syntax for TOML
License:        MIT
URL:            https://github.com/cespare/vim-toml
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildArch:      noarch
# for %%vimfiles_root macro
BuildRequires:  vim-filesystem
Requires:       vim-filesystem


%description
%{summary}.


%prep
%autosetup -n %{name}-%{commit}


%install
install -D -p -m 644 ftdetect/toml.vim %{buildroot}%{vimfiles_root}/ftdetect/toml.vim
install -D -p -m 644 ftplugin/toml.vim %{buildroot}%{vimfiles_root}/ftplugin/toml.vim
install -D -p -m 644 syntax/toml.vim %{buildroot}%{vimfiles_root}/syntax/toml.vim


%files
%license LICENSE
%{vimfiles_root}/ftdetect/toml.vim
%{vimfiles_root}/ftplugin/toml.vim
%{vimfiles_root}/syntax/toml.vim


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0^1.717bd87-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0^1.717bd87-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Oct 29 2021 Carl George <carl@george.computer> - 0^1.717bd87-1
- Latest upstream snapshot

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20201207git3c5face
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 20 2021 Carl George <carl@george.computer> - 0-0.9.20201207git3c5face
- Latest upstream commit

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20180615git85ba827
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20180615git85ba827
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20180615git85ba827
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20180615git85ba827
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20180615git85ba827
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20180615git85ba827
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Carl George <carl@george.computer> - 0-0.2.20180615git85ba827
- Latest upstream commit

* Thu Apr 05 2018 Carl George <carl@george.computer> - 0-0.1.20180306git624f024
- Include snapshot date in release

* Wed Apr 04 2018 Carl George <carl@george.computer> - 0-0.1.git624f024
- Initial package
