%global revdate     20220701
%global gitrevision b73a8e97de95d26280082abb7f51465a3d3b239e
%global gitrev      %(full=%gitrevision ; echo ${full:0:6} )
%global posttag     %{revdate}git%{gitrev}
%global upstream_n  fugitive-gitlab.vim

Name: vim-fugitive-gitlab
Version: 0~%posttag
Release: 2%{?dist}
Summary: GitLab support for vim-fugitive plugin
License: MIT
BuildArch: noarch

URL: https://github.com/shumphrey/%upstream_n.git
Source0: https://github.com/shumphrey/%upstream_n/archive/%gitrevision/%upstream_n-%gitrevision.tar.gz

Requires: vim-fugitive
Requires: vim-filesystem

BuildRequires: vim-filesystem


%description
GitLab support for vim-fugitive plugin.  Enables :Gbrowse from fugitive.vim to
open GitLab URLs.  Sets up :Git to use hub if installed rather than git (when
available).  In commit messages, GitLab issues, issue URLs, and collaborators
can be omni-completed (<C-X><C-O>, see :help compl-omni).


%prep
%autosetup -p1 -n %upstream_n-%gitrevision


%install
mkdir -p %{buildroot}%{vimfiles_root}/autoload/gitlab
mkdir -p %{buildroot}%{vimfiles_root}/doc
mkdir -p %{buildroot}%{vimfiles_root}/plugin

install -p -m 0644 doc/fugitive-gitlab.txt %{buildroot}%{vimfiles_root}/doc
install -p -m 0644 plugin/gitlab.vim %{buildroot}%{vimfiles_root}/plugin
for filename in api fugitive omnifunc utils; do
    install -p -m 0644 autoload/gitlab/$filename.vim %{buildroot}%{vimfiles_root}/autoload/gitlab
done


%files
%license LICENSE
%doc %{vimfiles_root}/doc/*.txt
%{vimfiles_root}/plugin/gitlab.vim
%{vimfiles_root}/autoload/gitlab


%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0~20220701gitb73a8e-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 06 2022 Pavel Raiskup <praiskup@redhat.com> - 0~20220701gitb73a8e-1
- initial packaging, inspiration from vim-rhubarb.spec (rhbz#2103073)
