Name: vim-fugitive
Version: 3.7
Release: 8%{?dist}
Summary: A Git wrapper so awesome, it should be illegal
License: Vim
URL: https://github.com/tpope/vim-fugitive
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Plug-in AppData for Gnome Software.
# https://github.com/tpope/vim-fugitive/pull/638
Source1: vim-fugitive.metainfo.xml
Requires: vim-common
%if %{defined el7}
Requires(post): %{_bindir}/vim
Requires(postun): %{_bindir}/vim
%endif
BuildRequires: vim-filesystem
# Needed for AppData check.
BuildRequires: libappstream-glib
BuildArch: noarch


%description
Fugitive is the premier Vim plugin for Git. Or maybe it's the premier Git
plugin for Vim? Either way, it's "so awesome, it should be illegal". That's why
it's called Fugitive.


%prep
%autosetup -p 1 -n %{name}-%{version}


%install
install -D -p -m 0644 autoload/fugitive.vim %{buildroot}%{vimfiles_root}/autoload/fugitive.vim
install -D -p -m 0644 doc/fugitive.txt %{buildroot}%{vimfiles_root}/doc/fugitive.txt
install -D -p -m 0644 ftdetect/fugitive.vim %{buildroot}%{vimfiles_root}/ftdetect/fugitive.vim
install -D -p -m 0644 ftplugin/fugitiveblame.vim %{buildroot}%{vimfiles_root}/ftplugin/fugitiveblame.vim
install -D -p -m 0644 plugin/fugitive.vim %{buildroot}%{vimfiles_root}/plugin/fugitive.vim
install -D -p -m 0644 syntax/fugitive.vim %{buildroot}%{vimfiles_root}/syntax/fugitive.vim
install -D -p -m 0644 syntax/fugitiveblame.vim %{buildroot}%{vimfiles_root}/syntax/fugitiveblame.vim

# Install AppData.
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_metainfodir}/vim-fugitive.metainfo.xml


%check
# Check the AppData add-on to comply with guidelines.
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml


%if %{defined el7}
%post
vim -c ":helptags %{vimfiles_root}/doc" -c :q &> /dev/null


%postun
> %{vimfiles_root}/doc/tags
vim -c ":helptags %{vimfiles_root}/doc" -c :q &> /dev/null
%endif


%files
%doc %{vimfiles_root}/doc/fugitive.txt
%{vimfiles_root}/autoload/fugitive.vim
%{vimfiles_root}/ftdetect/fugitive.vim
%{vimfiles_root}/ftplugin/fugitiveblame.vim
%{vimfiles_root}/plugin/fugitive.vim
%{vimfiles_root}/syntax/fugitive.vim
%{vimfiles_root}/syntax/fugitiveblame.vim
%{_metainfodir}/vim-fugitive.metainfo.xml


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 05 2023 Carl George <carl@george.computer> - 3.7-4
- Fix doc trigger conditional to avoid extra dependency on /usr/bin/vim

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Carl George <carl@george.computer> - 3.7-1
- Latest upstream, resolves rhbz#2000731

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3^1.4cdeff8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3^1.4cdeff8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 11 2021 Carl George <carl@george.computer> - 3.3^1.4cdeff8-1
- Latest upstream snapshot
- Resolves: rhbz#1974644

* Mon May 31 2021 Carl George <carl@george.computer> - 3.3-1
- Latest upstream

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 08 2019 Carl George <carl@george.computer> - 3.0-1
- Latest upstream

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 12 2019 Carl George <carl@george.computer> - 2.5-1
- Latest upstream

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Carl George <carl@george.computer> - 2.4-3
- Include autoload and ftdetect files from upstream for proper functionality

* Wed Jul 18 2018 Carl George <carl@george.computer> - 2.4-2
- Re-add documentation scriptlets for EPEL

* Wed Jul 18 2018 Carl George <carl@george.computer> - 2.4-1
- Latest upstream

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Vít Ondruch <vondruch@redhat.com> - 2.3-2
- Documentation updates are now handled by Vim transfiletriggers.

* Fri Jun 15 2018 Carl George <carl@george.computer> - 2.3-1
- Latest upstream
- Mark documentation file as %%doc

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jun 24 2016 Brad Hubbard <bhubbard@redhat.com> - 2.2-5
- Fix "E117: Unknown function: netrw#NetrwBrowseX" [1349684]

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 12 2015 Vít Ondruch <vondruch@redhat.com> - 2.2-2
- Remove something like RPM macro from description.

* Tue May 12 2015 Vít Ondruch <vondruch@redhat.com> - 2.2-1
- Initial package.
