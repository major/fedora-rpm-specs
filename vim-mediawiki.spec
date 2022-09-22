%global commit      26e5737264354be41cb11d16d48132779795e168
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           vim-mediawiki
Version:        0.2^1.%{shortcommit}
Release:        %autorelease
Summary:        Vim syntax highlighting for MediaWiki
License:        Public Domain
URL:            https://github.com/chikamichi/mediawiki.vim
Source:         %{url}/archive/%{commit}/mediawiki.vim-%{shortcommit}.tar.gz
BuildArch:      noarch
# for %%vimfiles_root macro
BuildRequires:  vim-filesystem
Requires:       vim-filesystem


%description
Syntax highlighting for MediaWiki-based projects, such as Wikipedia.


%prep
%autosetup -n mediawiki.vim-%{commit}


%install
install -D -p -m 0644 autoload/mediawiki.vim %{buildroot}%{vimfiles_root}/autoload/mediawiki.vim
install -D -p -m 0644 ftdetect/mediawiki.vim %{buildroot}%{vimfiles_root}/ftdetect/mediawiki.vim
install -D -p -m 0644 ftplugin/mediawiki.vim %{buildroot}%{vimfiles_root}/ftplugin/mediawiki.vim
install -D -p -m 0644 syntax/mediawiki.vim   %{buildroot}%{vimfiles_root}/syntax/mediawiki.vim


%files
%doc README.md
%{vimfiles_root}/autoload/mediawiki.vim
%{vimfiles_root}/ftdetect/mediawiki.vim
%{vimfiles_root}/ftplugin/mediawiki.vim
%{vimfiles_root}/syntax/mediawiki.vim


%changelog
%autochangelog
