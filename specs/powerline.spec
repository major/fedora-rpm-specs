%global debug_package %{nil}

Name:           powerline
Version:        2.8.4
Release:        %autorelease

Summary:        The ultimate status-line/prompt utility
License:        MIT
Url:            https://github.com/powerline/powerline

BuildRequires: make
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  python3-devel
BuildRequires:  fdupes
BuildRequires:  fontpackages-filesystem
BuildRequires:  gcc
BuildRequires:  systemd
BuildRequires:  tmux
BuildRequires:  vim-minimal

# Test dependencies:
BuildRequires:  git-core
BuildRequires:  python3dist(pexpect)
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(pytest)
# There are no `python-hglib` and `python3-netifaces` packages for EPEL
%if 0%{?fedora}
BuildRequires:  mercurial
BuildRequires:  python-hglib
BuildRequires:  python3dist(netifaces)
%endif

Requires:       python3
Requires:       powerline-fonts
# Needs these if we have to drop back to bash/socat client due to C compile failure
# Requires:       which socat
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

Recommends:     python3-pygit2

Source0:        https://github.com/powerline/powerline/archive/%{version}/powerline-%{version}.tar.gz
Source1:        vim-powerline.metainfo.xml

# Fix Vim status line for Git repositories
Patch0:         0001-Fix-TypeError-bad-argument-type-for-built-in-operati.patch

# Fix unit tests
Patch1:         0002-Rename-assertion-method.patch

# Fix compatibility with Python 3.14:
# https://bugzilla.redhat.com/show_bug.cgi?id=2336943
Patch2:         0003-Fix-compatibility-with-Python-3.14.patch

%description
Powerline is a status-line plugin for vim, and provides status-lines and prompts
for several other applications, including zsh, bash, tmux, IPython, Awesome and
Qtile.

%package docs
Summary: Powerline Documentation
BuildArch: noarch

%description docs
This package provides the powerline documentation.

%package fonts
Summary: Powerline symbol font
BuildArch: noarch
Requires: fontpackages-filesystem

%description fonts
This package provides the symbol font used by Powerline, plus a fontconfig file
that allows using these symbols as part of common monospaced fonts.

%package -n vim-powerline
Summary: Powerline VIM plugin
BuildArch: noarch
Requires: vim
Requires: %{name} = %{version}-%{release}
Obsoletes: vim-plugin-powerline < %{version}-%{release}
Provides: vim-plugin-powerline = %{version}-%{release}

%description -n vim-powerline
Powerline is a status-line plugin for vim, and provides status-lines and
prompts.

%package -n tmux-powerline
Summary: Powerline for tmux
BuildArch: noarch
Requires: tmux
Requires: %{name} = %{version}-%{release}

%description -n tmux-powerline
Powerline for tmux.

Add

    source /usr/share/tmux/powerline.conf

to your ~/.tmux.conf file.

%prep
%autosetup -p1
find -type f -exec sed -i '1s=^#!/usr/bin/\(python\|env python\)[23]\?=#!%{__python3}=' {} +

%build
# nothing to build

%install
sed -i -e "/DEFAULT_SYSTEM_CONFIG_DIR/ s@None@'%{_sysconfdir}/xdg'@" powerline/config.py
sed -i -e "/TMUX_CONFIG_DIRECTORY/ s@BINDINGS_DIRECTORY@'/usr/share'@" powerline/config.py
# `setup.py` uses `CFLAGS` for both compiler and linker flags
CFLAGS="%{build_cflags} %{build_ldflags}" \
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot} --optimize=1

# Check that the powerline client is an ELF executable
ldd %{buildroot}%{_bindir}/powerline

# build docs
pushd docs
%__make html SPHINXBUILD=/usr/bin/sphinx-build-3
%__rm _build/html/.buildinfo
# A structure gets initialized while building the docs with os.environ.
# This works around an rpmlint error with the build dir being in a file.
sed -i -e 's/abuild/user/g' _build/html/develop/extensions.html

%__make man SPHINXBUILD=/usr/bin/sphinx-build-3
popd

# config
install -d -m0755 %{buildroot}%{_sysconfdir}/xdg/%{name}
cp -a powerline/config_files/* %{buildroot}%{_sysconfdir}/xdg/%{name}/

# fonts
install -d -m0755 %{buildroot}%{_sysconfdir}/fonts/conf.d
install -d -m0755 %{buildroot}%{_datadir}/fonts/truetype
install -d -m0755 %{buildroot}%{_datadir}/fontconfig/conf.avail

install -m0644 font/PowerlineSymbols.otf %{buildroot}%{_datadir}/fonts/truetype/PowerlineSymbols.otf
install -m0644 font/10-powerline-symbols.conf %{buildroot}%{_datadir}/fontconfig/conf.avail/10-powerline-symbols.conf

ln -sr %{buildroot}%{_datadir}/fontconfig/conf.avail/10-powerline-symbols.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/10-powerline-symbols.conf

# manpages
%__install -d -m0755 %{buildroot}%{_datadir}/man/man1
for f in powerline-config.1 powerline-daemon.1 powerline-lint.1 powerline.1; do
%__install -m0644 docs/_build/man/$f %{buildroot}%{_datadir}/man/man1/$f
done

# awesome
install -d -m0755 %{buildroot}%{_datadir}/%{name}/awesome/
mv %{buildroot}%{python3_sitelib}/powerline/bindings/awesome/powerline.lua %{buildroot}%{_datadir}/%{name}/awesome/
mv %{buildroot}%{python3_sitelib}/powerline/bindings/awesome/powerline-awesome.py %{buildroot}%{_datadir}/%{name}/awesome/

# bash bindings
install -d -m0755 %{buildroot}%{_datadir}/%{name}/bash
mv %{buildroot}%{python3_sitelib}/powerline/bindings/bash/powerline.sh %{buildroot}%{_datadir}/%{name}/bash/

# fish
install -d -m0755 %{buildroot}%{_datadir}/%{name}/fish
mv %{buildroot}%{python3_sitelib}/powerline/bindings/fish/powerline-setup.fish %{buildroot}%{_datadir}/%{name}/fish

# i3
install -d -m0755 %{buildroot}%{_datadir}/%{name}/i3
mv %{buildroot}%{python3_sitelib}/powerline/bindings/i3/powerline-i3.py %{buildroot}%{_datadir}/%{name}/i3

# qtile
install -d -m0755 %{buildroot}%{_datadir}/%{name}/qtile
mv %{buildroot}%{python3_sitelib}/powerline/bindings/qtile/widget.py %{buildroot}%{_datadir}/%{name}/qtile

# shell bindings
install -d -m0755 %{buildroot}%{_datadir}/%{name}/shell
mv %{buildroot}%{python3_sitelib}/powerline/bindings/shell/powerline.sh %{buildroot}%{_datadir}/%{name}/shell/

# tcsh
install -d -m0755 %{buildroot}%{_datadir}/%{name}/tcsh
mv %{buildroot}%{python3_sitelib}/powerline/bindings/tcsh/powerline.tcsh %{buildroot}%{_datadir}/%{name}/tcsh

# tmux plugin
install -d -m0755 %{buildroot}%{_datadir}/tmux
mv %{buildroot}%{python3_sitelib}/powerline/bindings/tmux/powerline*.conf %{buildroot}%{_datadir}/tmux/

# vim plugin
install -d -m0755 %{buildroot}%{_datadir}/vim/vimfiles/plugin/
mv %{buildroot}%{python3_sitelib}/powerline/bindings/vim/plugin/powerline.vim %{buildroot}%{_datadir}/vim/vimfiles/plugin/powerline.vim
rm -rf %{buildroot}%{python3_sitelib}/powerline/bindings/vim/plugin
install -d -m0755 %{buildroot}%{_datadir}/vim/vimfiles/autoload/powerline
mv %{buildroot}%{python3_sitelib}/powerline/bindings/vim/autoload/powerline/debug.vim %{buildroot}%{_datadir}/vim/vimfiles/autoload/powerline/debug.vim
rm -rf %{buildroot}%{python3_sitelib}/powerline/bindings/vim/autoload

# zsh
install -d -m0755 %{buildroot}%{_datadir}/%{name}/zsh
mv %{buildroot}%{python3_sitelib}/powerline/bindings/zsh/__init__.py %{buildroot}%{_datadir}/%{name}/zsh
mv %{buildroot}%{python3_sitelib}/powerline/bindings/zsh/powerline.zsh %{buildroot}%{_datadir}/%{name}/zsh

# vim-powerline AppStream metadata
mkdir -p %{buildroot}%{_datadir}/metainfo
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo

# systemd
install -d -m 0755 %{buildroot}%{_userunitdir}
install -m 0644 powerline/dist/systemd/powerline-daemon.service %{buildroot}%{_userunitdir}/powerline.service

# cleanup
%__rm -rf %{buildroot}%{python3_sitelib}/%{name}/config_files

%if 0%{?fedora}
%fdupes %{buildroot}%{python3_sitelib}
%endif

%check
PYTHONPATH=. TEST_ROOT=. \
%pytest -r s -k 'not (test_kw_threaded_segment or test_logger_format or test_system_load or test_threaded_segment or test_top_log_format or test_user)'

%post
%systemd_user_post powerline.service

%preun
%systemd_user_preun powerline.service

%postun
%systemd_user_postun_with_restart powerline.service

%files
%license LICENSE
%doc README.rst
%dir %{_sysconfdir}/xdg/powerline
%config(noreplace) %{_sysconfdir}/xdg/powerline/colors.json
%config(noreplace) %{_sysconfdir}/xdg/powerline/config.json

%dir %{_sysconfdir}/xdg/powerline/colorschemes
%config(noreplace) %{_sysconfdir}/xdg/powerline/colorschemes/default.json
%config(noreplace) %{_sysconfdir}/xdg/powerline/colorschemes/solarized.json

%dir %{_sysconfdir}/xdg/powerline/colorschemes/pdb
%config(noreplace) %{_sysconfdir}/xdg/powerline/colorschemes/pdb/solarized.json
%config(noreplace) %{_sysconfdir}/xdg/powerline/colorschemes/pdb/__main__.json
%config(noreplace) %{_sysconfdir}/xdg/powerline/colorschemes/pdb/default.json

%dir %{_sysconfdir}/xdg/powerline/colorschemes/vim
%config(noreplace) %{_sysconfdir}/xdg/powerline/colorschemes/vim/solarized.json
%config(noreplace) %{_sysconfdir}/xdg/powerline/colorschemes/vim/__main__.json
%config(noreplace) %{_sysconfdir}/xdg/powerline/colorschemes/vim/default.json
%config(noreplace) %{_sysconfdir}/xdg/powerline/colorschemes/vim/solarizedlight.json

%dir %{_sysconfdir}/xdg/powerline/colorschemes/tmux
%config(noreplace) %{_sysconfdir}/xdg/powerline/colorschemes/tmux/solarized.json
%config(noreplace) %{_sysconfdir}/xdg/powerline/colorschemes/tmux/default.json

%dir %{_sysconfdir}/xdg/powerline/colorschemes/shell
%config(noreplace) %{_sysconfdir}/xdg/powerline/colorschemes/shell/solarized.json
%config(noreplace) %{_sysconfdir}/xdg/powerline/colorschemes/shell/__main__.json
%config(noreplace) %{_sysconfdir}/xdg/powerline/colorschemes/shell/default.json

%dir %{_sysconfdir}/xdg/powerline/colorschemes/ipython
%config(noreplace) %{_sysconfdir}/xdg/powerline/colorschemes/ipython/__main__.json

%dir %{_sysconfdir}/xdg/powerline/themes
%config(noreplace) %{_sysconfdir}/xdg/powerline/themes/ascii.json
%config(noreplace) %{_sysconfdir}/xdg/powerline/themes/powerline.json
%config(noreplace) %{_sysconfdir}/xdg/powerline/themes/powerline_terminus.json
%config(noreplace) %{_sysconfdir}/xdg/powerline/themes/powerline_unicode7.json
%config(noreplace) %{_sysconfdir}/xdg/powerline/themes/unicode.json
%config(noreplace) %{_sysconfdir}/xdg/powerline/themes/unicode_terminus.json
%config(noreplace) %{_sysconfdir}/xdg/powerline/themes/unicode_terminus_condensed.json

%dir %{_sysconfdir}/xdg/powerline/themes/ipython
%config(noreplace) %{_sysconfdir}/xdg/powerline/themes/ipython/in2.json
%config(noreplace) %{_sysconfdir}/xdg/powerline/themes/ipython/rewrite.json
%config(noreplace) %{_sysconfdir}/xdg/powerline/themes/ipython/in.json
%config(noreplace) %{_sysconfdir}/xdg/powerline/themes/ipython/out.json
%dir %{_sysconfdir}/xdg/powerline/themes/pdb
%config(noreplace) %{_sysconfdir}/xdg/powerline/themes/pdb/default.json

%dir %{_sysconfdir}/xdg/powerline/themes/shell
%config(noreplace) %{_sysconfdir}/xdg/powerline/themes/shell/__main__.json
%config(noreplace) %{_sysconfdir}/xdg/powerline/themes/shell/select.json
%config(noreplace) %{_sysconfdir}/xdg/powerline/themes/shell/default.json
%config(noreplace) %{_sysconfdir}/xdg/powerline/themes/shell/default_leftonly.json
%config(noreplace) %{_sysconfdir}/xdg/powerline/themes/shell/continuation.json

%dir %{_sysconfdir}/xdg/powerline/themes/tmux
%config(noreplace) %{_sysconfdir}/xdg/powerline/themes/tmux/default.json

%dir %{_sysconfdir}/xdg/powerline/themes/vim
%config(noreplace) %{_sysconfdir}/xdg/powerline/themes/vim/quickfix.json
%config(noreplace) %{_sysconfdir}/xdg/powerline/themes/vim/tabline.json
%config(noreplace) %{_sysconfdir}/xdg/powerline/themes/vim/__main__.json
%config(noreplace) %{_sysconfdir}/xdg/powerline/themes/vim/cmdwin.json
%config(noreplace) %{_sysconfdir}/xdg/powerline/themes/vim/plugin_commandt.json
%config(noreplace) %{_sysconfdir}/xdg/powerline/themes/vim/default.json
%config(noreplace) %{_sysconfdir}/xdg/powerline/themes/vim/plugin_gundo-preview.json
%config(noreplace) %{_sysconfdir}/xdg/powerline/themes/vim/plugin_gundo.json
%config(noreplace) %{_sysconfdir}/xdg/powerline/themes/vim/plugin_nerdtree.json
%config(noreplace) %{_sysconfdir}/xdg/powerline/themes/vim/help.json

%dir %{_sysconfdir}/xdg/powerline/themes/wm
%config(noreplace) %{_sysconfdir}/xdg/powerline/themes/wm/default.json

%{_bindir}/powerline
%{_bindir}/powerline-config
%{_bindir}/powerline-daemon
%{_bindir}/powerline-render
%{_bindir}/powerline-lint
%{_mandir}/man1/powerline.1*
%{_mandir}/man1/powerline-config.1*
%{_mandir}/man1/powerline-daemon.1*
%{_mandir}/man1/powerline-lint.1*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/awesome
%{_datadir}/%{name}/awesome/powerline.lua
%{_datadir}/%{name}/awesome/powerline-awesome.py*
%dir %{_datadir}/%{name}/bash
%{_datadir}/%{name}/bash/powerline.sh
%dir %{_datadir}/%{name}/fish
%{_datadir}/%{name}/fish/powerline-setup.fish
%dir %{_datadir}/%{name}/i3
%{_datadir}/%{name}/i3/powerline-i3.py*
%dir %{_datadir}/%{name}/qtile
%{_datadir}/%{name}/qtile/widget.py*
%dir %{_datadir}/%{name}/shell
%{_datadir}/%{name}/shell/powerline.sh
%dir %{_datadir}/%{name}/tcsh
%{_datadir}/%{name}/tcsh/powerline.tcsh
%dir %{_datadir}/%{name}/zsh
%{_datadir}/%{name}/zsh/__init__.py*
%{_datadir}/%{name}/zsh/powerline.zsh
%{python3_sitelib}/*
%{_userunitdir}/powerline.service

%files docs
%doc docs/_build/html

%files fonts
%doc LICENSE README.rst
%{_sysconfdir}/fonts/conf.d/10-powerline-symbols.conf
%{_datadir}/fontconfig/conf.avail/10-powerline-symbols.conf
%dir %{_datadir}/fonts/truetype
%{_datadir}/fonts/truetype/PowerlineSymbols.otf

%files -n vim-powerline
%doc LICENSE README.rst
%dir %{_datadir}/vim/vimfiles
%dir %{_datadir}/vim/vimfiles/autoload
%dir %{_datadir}/vim/vimfiles/autoload/powerline
%{_datadir}/vim/vimfiles/autoload/powerline/debug.vim
%dir %{_datadir}/vim/vimfiles/plugin
%{_datadir}/vim/vimfiles/plugin/powerline.vim
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/vim-powerline.metainfo.xml

%files -n tmux-powerline
%doc LICENSE README.rst
%dir %{_datadir}/tmux
%{_datadir}/tmux/powerline*.conf

%changelog
%autochangelog
