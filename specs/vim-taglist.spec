%global baseversion 4.6
%global zipversion 46
%global zipname taglist
#used for pre-releases:
%global vimfiles_root %{_datadir}/vim/vimfiles

Summary:          The taglist plugin for VIM editor
Name:             vim-%{zipname}
Version:          %{baseversion}
Release:          28%{?dist}

License:          Vim
URL:              http://vim-taglist.sourceforge.net/
Source:           http://sourceforge.net/projects/vim-taglist/files/vim-taglist/4.6/taglist_46.zip
Source1:          %{name}.metainfo.xml

Requires:         vim-common
Requires(post):   vim
Requires(postun): vim
Requires:         ctags
BuildRequires:    desktop-file-utils
BuildArch:        noarch

%description
The "Tag List" plugin is a source code browser plugin for vim and provides
an overview of the structure of source code files and allows you to efficiently
browse through source code files for different programming languages.

%prep
%setup -c taglist -q -n %{zipname}

cp %{SOURCE1} .

%build

%install
mkdir -p %{buildroot}/%{vimfiles_root}
cp -ar {doc,plugin} %{buildroot}%{vimfiles_root}
chmod 644 %{buildroot}%{vimfiles_root}/doc/*
mkdir -p %{buildroot}%{_datadir}/appdata
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/appdata/

%post
vim -c ":helptags %{vimfiles_root}/doc" -c :q &> /dev/null

%postun
rm %{vimfiles_root}/doc/tags
vim -c ":helptags %{vimfiles_root}/doc" -c :q &> /dev/null

%files 
%{vimfiles_root}/plugin/*
%doc %{vimfiles_root}/doc/*
%{_datadir}/appdata/%{name}.metainfo.xml

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 25 2015 Petr Hracek <phracek@redhat.com> - 4.6-9
- Add Addon metadata for GNOME Software (#1128813)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 26 2013 Petr Hracek <phracek@redhat.com> - 4.6-7
- Ctags added into requires section (#1010967)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 07 2013 Petr Hracek <phracek@redhat.com> - 4.6-5
- License should be Vim
- Delete the BuildRoot sections

* Tue Apr 30 2013 Petr Hracek <phracek@redhat.com> - 4.6-4
- Correction of License field

* Thu Apr 25 2013 Petr Hracek <phracek@redhat.com> - 4.6-3
- Correction of Requires
- Files are stored in vimfiles directory
- added post and postun sections

* Mon Apr 22 2013 Petr Hracek <phracek@redhat.com> 4.6-2
- Include Source URL

* Mon Apr 22 2013 Petr Hracek <phracek@redhat.com> 4.6-1
- Initial version
