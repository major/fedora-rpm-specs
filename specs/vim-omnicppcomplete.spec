%global vimfiles_root %{_datadir}/vim/vimfiles

Name:             vim-omnicppcomplete
Version:          0.41
Release:          25%{?dist}
Summary:          vim c++ completion omnifunc with a ctags database

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:          GPL-2.0-or-later
URL:              http://www.vim.org/scripts/script.php?script_id=1520
Source0:          http://www.vim.org/scripts/download_script.php?src_id=7722#/omnicppcomplete-%{version}.zip
Patch0:           license.patch

Requires:         ctags
Requires:         vim-filesystem
Requires(post):   vim
Requires(postun): vim

BuildArch:      noarch

%description
This script is for vim 7.0 or higher, it provides C/C++ completion thanks to a
ctags database.

Features :

 - Complete namespaces, classes, structs and union members.
 - Complete inherited members for classes and structs (single and multiple
   inheritance).
 - Complete attribute members eg: myObject->_child->_child etc...
 - Complete type returned by a function eg: myObject->get()->_child.
 - Complete the "this" pointer.
 - Complete a typedef.
 - Complete the current scope (global and class scope).
 - Complete an object after a cast (C and C++ cast).
 - Complete anonymous types (eg: struct {int a; int b;}g_Var; g_Var.???). It
   also works for a typedef of an anonymous type.

Notes :
 - The script manage cached datas for optimization.
 - Ambiguous namespaces are detected and are not included in the context stack.
 - The parsed code is tokenized so you can run a completion even if the current
   instruction has bad indentation, spaces, comments or carriage returns
   between words
   (even if it is not realistic).

%prep
%setup -q -c omnicppcomplete-%{version}
%patch -P0 -p1

%build

%install
mkdir -p %{buildroot}%{vimfiles_root}
cp -ar {after,autoload,doc} %{buildroot}%{vimfiles_root}

%post
vim -c ":helptags %{vimfiles_root}/doc" -c :q &> /dev/null

%postun
rm %{vimfiles_root}/doc/tags
vim -c ":helptags %{vimfiles_root}/doc" -c :q &> /dev/null

%files
%doc %{vimfiles_root}/doc/*
%{vimfiles_root}/after
%{vimfiles_root}/autoload

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.41-24
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 08 2017 Marc Deop <marc@marcdeop.com> - 0.41-8
- Package enhancements
- Max description lines length to 80 chars
- Source0 tag to have full URL
- Remove "Group"

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.41-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 27 2015 Marc Deop <marc@marcdeop.com> - 0.41-4
- Add post and postun and Requires: vim (to generate helptags properly).
* Thu Nov 15 2012 Marc Deop <marc@marcdeop.com> - 0.41-3
- Added patch to include GPLv2+ License (commit da45a4a3eb4ebea6bca7044868b9b4779a0315a0)
* Sat Nov 10 2012 Marc Deop <marc@marcdeop.com> - 0.41-2
- Removed scriptlets and fixed License name
* Tue May 15 2012 Marc Deop <marc@marcdeop.com> - 0.41-1
- Initial package.
