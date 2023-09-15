%global commit  71f239af28b7214eebb60d4ea5bd040291fb7e33
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date    20221001

Name:           vim-devicons
Version:        0.11.0
Release:        0.%{date}git%{shortcommit}.%autorelease
Summary:        Adds file type icons to Vim plugins

License:        MIT
URL:            https://github.com/ryanoasis/vim-devicons
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        %{name}.metainfo.xml
BuildArch:      noarch

BuildRequires:  libappstream-glib
BuildRequires:  vim-filesystem

Requires:       vim-enhanced

# Not available in repos
# * https://github.com/ryanoasis/nerd-fonts#font-installation
#Requires:     nerd-fonts

%description
Supports plugins such as NERDTree, vim-airline, CtrlP, powerline, denite,
unite, lightline.vim, vim-startify, vimfiler, vim-buffet and flagship.

Features:

- Adds filetype glyphs (icons) to various vim plugins.
- Customizable and extendable glyphs settings.
- Supports a wide range of file type extensions.
- Supports popular full filenames, like .gitignore, node_modules, .vimrc, and
  many more.
- Supports byte order marker (BOM).
- Works with patched fonts, especially Nerd Fonts.


%prep
%autosetup -n %{name}-%{commit} -p1


%install
mkdir -p                                                %{buildroot}%{vimfiles_root}
cp -r {autoload,nerdtree_plugin,plugin,pythonx,rplugin} %{buildroot}%{vimfiles_root}
install -m 0644 -Dp %{SOURCE1}                          %{buildroot}%{_metainfodir}/%{name}.metainfo.xml


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml


%files
%license LICENSE
%doc README.md CHANGELOG.md DEVELOPER.md CONTRIBUTING.md doc/*
%{vimfiles_root}/autoload/*
%{vimfiles_root}/nerdtree_plugin/*
%{vimfiles_root}/plugin/*
%{vimfiles_root}/pythonx/
%{vimfiles_root}/rplugin/
%{_metainfodir}/*.xml


%changelog
%autochangelog
