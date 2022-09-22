%global commit 9f96bbdef5cb19daf58449f0fbb597af6fc4c2eb
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20220504

Name: awesome-vim-colorschemes
Version: 0
Release: 15.%{date}git%{shortcommit}.%autorelease
Summary: Collection of color schemes for Neo/vim, merged for quick use
BuildArch: noarch

# You can find the individual license in the actual vim file, or find the
# appropriate README in docs/
# * https://github.com/rafi/awesome-vim-colorschemes/issues/12
License: Vim and MIT and CC-BY

URL: https://github.com/rafi/awesome-vim-colorschemes
Source0: %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1: %{name}.metainfo.xml

# Remove executable bit & Fix wrong file end of line encoding
# * https://github.com/rafi/awesome-vim-colorschemes/pull/13
Patch0: https://github.com/rafi/awesome-vim-colorschemes/pull/13#/remove-executable-bit-&-fix-wrong-file-end-of-line-encoding.patch

BuildRequires: libappstream-glib
BuildRequires: vim-filesystem

Requires: vim-enhanced

%description
Collection of awesome color schemes for Neo/vim, merged for quick use.


%prep
%autosetup -n %{name}-%{commit} -p1


%install
mkdir -p %{buildroot}%{vimfiles_root}
cp -a {autoload,colors} %{buildroot}%{vimfiles_root}
install -Dpm0644 %{SOURCE1} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml


%files
%doc README.md docs/
%{vimfiles_root}/autoload/*
%{vimfiles_root}/colors/*
%{_metainfodir}/*.xml


%changelog
%autochangelog
