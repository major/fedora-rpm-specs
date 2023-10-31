Name:           vim-ansible
Version:        3.4
Release:        %autorelease
Summary:        Vim plugin for syntax highlighting ansible's common filetypes
License:        MIT AND BSD-3-Clause
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
%autochangelog
