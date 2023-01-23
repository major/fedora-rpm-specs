Name:           vim-ansible
Version:        3.2
Release:        5%{?dist}
Summary:        Vim plugin for syntax highlighting ansible's common filetypes
License:        MIT and BSD
URL:            https://github.com/pearofducks/ansible-vim
Source0:        %{url}/archive/%{version}/ansible-vim-%{version}.tar.gz
BuildArch:      noarch
# for %%vimfiles_root macro
BuildRequires:  vim-filesystem
Requires:       vim-filesystem


%description
This is a vim syntax plugin for Ansible 2.x, it supports YAML playbooks, Jinja2
templates, and Ansible's hosts files.


%prep
%autosetup -n ansible-vim-%{version}
mv syntax/jinja2.vim_LICENSE LICENSE_jinja2.vim


%install
mkdir -p %{buildroot}%{vimfiles_root}
cp -r --preserve=mode,timestamps ftdetect ftplugin indent syntax %{buildroot}%{vimfiles_root}


%files
%license LICENSE LICENSE_jinja2.vim
%doc README.md
%{vimfiles_root}/ftdetect/ansible.vim
%{vimfiles_root}/ftplugin/ansible.vim
%{vimfiles_root}/ftplugin/ansible_hosts.vim
%{vimfiles_root}/indent/ansible.vim
%{vimfiles_root}/syntax/ansible.vim
%{vimfiles_root}/syntax/ansible_hosts.vim
%{vimfiles_root}/syntax/jinja2.vim


%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 07 2021 Carl George <carl@george.computer> - 3.2-1
- Latest upstream
- Fixes: rhbz#1968145

* Mon Apr 12 2021 Carl George <carl@george.computer> - 3.1-1
- Latest upstream

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 07 2020 Carl George <carl@george.computer> - 3.0-1
- Initial package
