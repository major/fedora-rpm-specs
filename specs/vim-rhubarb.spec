%global revdate     20191014
%global gitrevision 5130596a65330a4e8523d3ac1582f6c31ea6bc63
%global gitrev      %(full=%gitrevision ; echo ${full:0:6} )
%global posttag     %{revdate}git%{gitrev}

Name: vim-rhubarb
Version: 0
Release: 12.%{posttag}%{?dist}
Summary: GitHub support for vim-fugitive plugin
License: Vim
BuildArch: noarch

URL: https://github.com/tpope/vim-rhubarb
Source0: https://github.com/tpope/%name/archive/%gitrevision/%name-%gitrevision.tar.gz

Requires: vim-common
Requires: vim-fugitive

BuildRequires: vim-filesystem


%description
GitHub support for vim-fugitive plugin.  Enables :Gbrowse from fugitive.vim to
open GitHub URLs.  Sets up :Git to use hub if installed rather than git (when
available).  In commit messages, GitHub issues, issue URLs, and collaborators
can be omni-completed (<C-X><C-O>, see :help compl-omni).


%prep
%autosetup -p1 -n %name-%gitrevision


%install
mkdir -p %{buildroot}%{vimfiles_root}/autoload
mkdir -p %{buildroot}%{vimfiles_root}/doc
mkdir -p %{buildroot}%{vimfiles_root}/plugin

install -p -m 0644 doc/rhubarb.txt %{buildroot}%{vimfiles_root}/doc
install -p -m 0644 plugin/rhubarb.vim %{buildroot}%{vimfiles_root}/plugin
install -p -m 0644 autoload/rhubarb.vim %{buildroot}%{vimfiles_root}/autoload


%files
# license file requested: https://github.com/tpope/vim-rhubarb/issues/55
%doc %{vimfiles_root}/doc/rhubarb.txt
%{vimfiles_root}/plugin/rhubarb.vim
%{vimfiles_root}/autoload/rhubarb.vim


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-12.20191014git513059
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-11.20191014git513059
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-10.20191014git513059
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-9.20191014git513059
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-8.20191014git513059
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-7.20191014git513059
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-6.20191014git513059
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-5.20191014git513059
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-4.20191014git513059
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-3.20191014git513059
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 25 2020 Pavel Raiskup <praiskup@redhat.com> - 0-2.20191014git513059
- put snapshot date into release tag
- install doc into vimfiles root

* Tue Mar 24 2020 Pavel Raiskup <praiskup@redhat.com> - 0-1.git513059
- initial packaging
