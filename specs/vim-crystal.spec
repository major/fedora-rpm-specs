%global commit dc21188ec8c2ee77bb81dffca02e1a29d87cfd9f
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20230315

Name:           vim-crystal
Version:        0^%{commitdate}git%{shortcommit}
Release:        %autorelease
Summary:        Vim support for the Crystal programming language

License:        MIT
URL:            https://github.com/vim-crystal/vim-crystal
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       vim-data
Requires:       vim-filesystem
Recommends:     crystal

%description
Vim and Neovim support for the Crystal programming language. This plugin
provides file type detection, syntax highlighting, smart indentation, crystal
tool and crystal spec integration, and Syntastic syntax checkers for Crystal
source files.


%prep
%autosetup -n vim-crystal-%{commit} -p1


%build
# No compilation required for pure Vim runtime files


%install
mkdir -p %{buildroot}%{_datadir}/vim/vimfiles
for dir in autoload ftdetect ftplugin indent plugin syntax syntax_checkers; do
    if [ -d "$dir" ]; then
        cp -a "$dir" %{buildroot}%{_datadir}/vim/vimfiles/
    fi
done


%check
# Upstream does not provide an automated test suite


%files
%license LICENSE.txt
%doc README.md
%{_datadir}/vim/vimfiles/autoload/*
%{_datadir}/vim/vimfiles/ftdetect/*
%{_datadir}/vim/vimfiles/ftplugin/*
%{_datadir}/vim/vimfiles/indent/*
%{_datadir}/vim/vimfiles/plugin/*
%{_datadir}/vim/vimfiles/syntax/*
%dir %{_datadir}/vim/vimfiles/syntax_checkers
%{_datadir}/vim/vimfiles/syntax_checkers/crystal


%changelog
%autochangelog
