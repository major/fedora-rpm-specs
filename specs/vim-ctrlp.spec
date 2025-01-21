%global commit 2e773fd8c7548526853fff6ee2e642eafbbe3d04
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapshotdate 20190610

Name:           vim-ctrlp
Version:        1.80
Release:        12.%{snapshotdate}git%{shortcommit}%{?dist}
Summary:        Full path fuzzy file, buffer, mru, tag, ... finder for Vim

License:        Vim
URL:            https://github.com/ctrlpvim/ctrlp.vim
Source0:        https://github.com/ctrlpvim/ctrlp.vim/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        https://raw.githubusercontent.com/osoukup/ctrlp.vim/master/%{name}.metainfo.xml

Requires:       vim-filesystem
Requires:       vim-common
Requires(post): vim
Requires(postun): vim
# Needed for AppData check
BuildRequires:  libappstream-glib
# Defines %%vimfiles_root
BuildRequires:  vim-filesystem
BuildArch:      noarch

%description
Full path fuzzy file, buffer, mru, tag, ... finder with an intuitive interface.
Written in pure Vimscript for MacVim, gVim and Vim version 7.0+. Has full
support for Vim's |regexp| as search pattern, built-in MRU files monitoring,
project's root finder, and more.

%prep
%autosetup -n ctrlp.vim-%{commit}

%build


%install
mkdir -p %{buildroot}%{vimfiles_root}
cp -r {autoload,doc,plugin} %{buildroot}%{vimfiles_root}

# Install AppData
mkdir -p %{buildroot}%{_metainfodir}
install -m 644 %{SOURCE1} %{buildroot}%{_metainfodir}

%check
# Check the AppData add-on to comply with guidelines
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/*.metainfo.xml


%files
%license LICENSE
%doc readme.md
%{vimfiles_root}/autoload/*
%doc %{vimfiles_root}/doc/*
%{vimfiles_root}/plugin/*
%{_metainfodir}/%{name}.metainfo.xml


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-12.20190610git2e773fd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-11.20190610git2e773fd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-10.20190610git2e773fd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-9.20190610git2e773fd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-8.20190610git2e773fd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-7.20190610git2e773fd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-6.20190610git2e773fd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-5.20190610git2e773fd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-4.20190610git2e773fd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-3.20190610git2e773fd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-2.20190610git2e773fd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Feb 26 2019 Ondřej Soukup <osoukup@redhat.com> - 1.80-1.20190610git2e773fd
- Initial package.
