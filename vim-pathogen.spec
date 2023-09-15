%global commit  ac4dd9494fa9008754e49dff85bff1b5746c89b4
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date    20220824

Name:           vim-pathogen
Version:        2.4
Release:        12.%{date}git%{shortcommit}.%autorelease
Summary:        Manage your runtimepath
BuildArch:      noarch

License:        Vim
URL:            https://github.com/tpope/vim-pathogen
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        %{name}.metainfo.xml

BuildRequires:  libappstream-glib
BuildRequires:  vim-filesystem

Requires:       vim-enhanced

%description
Manage your 'runtimepath' with ease. In practical terms, pathogen.vim makes it
super easy to install plugins and runtime files in their own private
directories.

For new users, I recommend using Vim's built-in package management instead:

  :help packages


%prep
%autosetup -n %{name}-%{commit}


%install
mkdir -p        %{buildroot}%{vimfiles_root}
cp -r autoload  %{buildroot}%{vimfiles_root}
install -m 0644 -Dp %{SOURCE1} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml


%files
%license LICENSE
%doc README.markdown CONTRIBUTING.markdown
%{vimfiles_root}/autoload/*
%{_metainfodir}/*.xml


%changelog
%autochangelog
