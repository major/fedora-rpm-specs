%global commit  f7b97666ae36c7b3f262f3190dbcd7033845d985
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date    20230901

Name:           vim-gitgutter
Version:        0
Release:        12.%{date}git%{shortcommit}.%autorelease
Summary:        Shows git diff markers in the sign column and stages/previews/undoes hunks

License:        MIT
URL:            https://github.com/airblade/vim-gitgutter
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        %{name}.metainfo.xml
BuildArch:      noarch

BuildRequires:  libappstream-glib
BuildRequires:  vim-filesystem

Requires:       vim-enhanced

%description
A Vim plugin which shows a git diff in the sign column. It shows which lines
have been added, modified, or removed. You can also preview, stage, and undo
individual hunks; and stage partial hunks. The plugin also provides a hunk
text object.

The signs are always up to date and the plugin never saves your buffer.

The name "gitgutter" comes from the Sublime Text 3 plugin which inspired this
in 2013.


%prep
%autosetup -n %{name}-%{commit} -p1


%install
mkdir -p %{buildroot}%{vimfiles_root}
cp -rp {autoload,plugin} %{buildroot}%{vimfiles_root}
install -m 0644 -Dp %{SOURCE1} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml


%files
%license LICENCE
%doc README.mkd doc/* test
%{vimfiles_root}/autoload/*
%{vimfiles_root}/plugin/*
%{_metainfodir}/*.xml


%changelog
%autochangelog
