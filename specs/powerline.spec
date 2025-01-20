%global debug_package %{nil}

Name:           powerline
Version:        2.8.4
Release:        2%{?dist}

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
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Sep 03 2024 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.8.4-1
- Update to 2.8.4 (#2309573)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.8.3-15
- Rebuilt for Python 3.13

* Wed Jan 31 2024 Christoph Erhardt <fedora@sicherha.de> - 2.8.3-14
- Fix `SyntaxWarning` with Python 3.12 (rhbz#2260646)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Oct 07 2023 Christoph Erhardt <fedora@sicherha.de> - 2.8.3-11
- Review SPDX license identifier; `MIT` is correct
- Make summary and description of `fonts` subpackage more precise (rhbz#2232553)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 2.8.3-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 23 2022 Christoph Erhardt <fedora@sicherha.de> - 2.8.3-6
- Fix build error with Python 3.11 (#2022396)

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.8.3-5
- Rebuilt for Python 3.11

* Sun Jun 05 2022 Christoph Erhardt <fedora@sicherha.de> - 2.8.3-4
- Use correct `%systemd_` RPM macros for user unit (#2093695)

* Fri Jun 03 2022 Christoph Erhardt <fedora@sicherha.de> - 2.8.3-3
- Build `powerline` binary with correct linker flags
- Make Fontconfig symlink relative
- Change fontconfig dependency to fontpackages-filesystem (#2093167)

* Thu May 26 2022 Christoph Erhardt <fedora@sicherha.de> - 2.8.3-2
- Install `powerline-daemon.service` into systemd user directory (#1976191)

* Thu May 19 2022 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.8.3-1
- Update to 2.8.3 (#2088362)

* Thu Feb 10 2022 Timothée Ravier <tim@siosm.fr> - 2.8.2-5
- Move AppStream metadata to metainfo

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.8.2-2
- Rebuilt for Python 3.10

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.8-5
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.8-2
- Rebuilt for Python 3.9

* Fri May 15 2020 Andreas Schneider <asn@redhat.com> - 2.8-1
- Update to version 2.8
  o Added ipython >= 7.0.0 support
  o Various other minor fixes and improvements

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.7-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.7-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 13 2018 Andreas Schneider <asn@redhat.com> - 2.7-1
- Update to version 2.7
  o Added ALE support.
  o Added mocp support.
  o Added awesome 4+ support.
  o Added support for `$pipestatus` in bash.
  o Recognize terminal-job mode.
  o Fixed i3 bindings when both i3-py and i3ipc are installed.
  o Fixed i3 bar bindings.
  o Fixed checking for battery in WSL.
  o Fixed spotify segment on Mac OS.
  o Fixed compiling C client with GCC-7.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.6-8
- Rebuilt for Python 3.7

* Tue Mar 13 2018 Michael Goodwin <xenithorb@fedoraproject.org> - 2.6-7
- Fix mislocated ipython bindings by not moving them (RHBZ #1554741)
  o There's no real justification to move ipython bindings when they're imported
    as python modules by the user anyway.
  o Before this change, importing the powerline.bindings.ipython.since_5 module
    wouldn't work because it couldn't locate the other two files that were
    moved into /usr/share/powerline
  o https://powerline.readthedocs.io/en/master/usage/other.html#ipython-prompt

* Thu Feb 22 2018 Michael Goodwin <xenithorb@fedoraproject.org> - 2.6-3
- Fix powerline requires both python2 and python3 (RHBZ #1546752)
- Add commented Requires for if we have to fall back to bash (RHBZ #1514830)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Andreas Schneider <asn@redhat.com> - 2.6-2
- Fix build with gcc7

* Wed May 10 2017 Andreas Schneider <asn@redhat.com> - 2.6-1
- Update to version 2.6
  o Added support for new Vim modes.
  o Added ability to control output padding.
  o Added iTunes player segment.
  o Added support for tmux development builds.
  o Added a workaround for a fish bug sometimes occurring when using eval from
  o config.fish (upstream status unknown).
  o Added a workaround for tmux 2.4 bug: excessive CPU usage when having multiple
  o panes (also fixed upstream).
  o Fixed clean file status support in mercurial.
  o Fixed error when battery capacity is zero and using DBus.
  o Fixed mercurial command servers leakage.
  o Refactored awesome bindings to use powerline daemon.

* Fri Apr 21 2017 Filipe Rosset <rosset.filipe@gmail.com> - 2.5.2-3
- Attempt to fix FTBFS on rawhide rhbz #1423199

* Fri Apr 21 2017 Filipe Rosset <rosset.filipe@gmail.com> - 2.5.2-2
- Rebuild for tmux 2.4

* Fri Feb 10 2017 Andreas Schneider <asn@redhat.com> - 2.5.2-1
- Update to version 2.5.2
  o Fixed ipython-5.2* support.
  o Made more robust theme default.
  o Made it use hglib in place of unstable mercurial plugin API.
  o Fixed latest fish version support.
  o Some other fixes and documentation adjustments.

* Wed Dec 21 2016 Andreas Schneider <asn@redhat.com> - 2.5-4
- Add upstream work around for gnome-terminal issues, brc#1403133
- Make pygit a recommondation

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.5-3
- Rebuild for Python 3.6

* Wed Nov 09 2016 Andreas Schneider <asn@redhat.com> - 2.5-2
- resolves: #1392619 - Put fonts in its own package
- Add require for pygit2

* Thu Aug 18 2016 Andreas Schneider <asn@redhat.com> - 2.5-1
- Update to version 2.5
  o Fix trailing whitespace segment on Python 3.
  o Fix left segments support in tmux-2.1
  o Add support for IPython-5
  o Increase socket backlog number for `powerline-daemon`
  o Use different query to retrieve weather
  o Implement stash backend for git
  o Provide stash counter
  o Include stash in default shell layout
  o Expose stash to Vim

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jun 17 2016 Andreas Schneider <asn@redhat.com> - 2.4-3
- Add support to start the powerline daemon with systemd
- Fix left segments support in tmux-2.1

* Tue Apr 19 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 2.4-2
- Apply patch to prefer python3 over python2

* Tue Apr 19 2016 Andreas Schneider <asn@redhat.com> - 2.4-1
- Update to version 2.4
  o Added short parameter for system_load segment that leaves only one load
    average number out of three.
  o Added powerline.segments.i3wm.scratchpad segment used to list windows that
    are currently on the scratchpad.
  o Added support for multiple batteries in battery segment.
  o Added .i3wm.workspace segment which describes single i3wm workspace and
    workspaces lister. Old .i3wm.workspaces segment was deprecated.
  o Added support for multiple monitors in lemonbar bindings.
  o Added support for most recent tmux version (2.2).
  o Fixed battery status support on some linux systems.
  o Fixed MPD bindings: they sometimes were not able to handle names if they
    did not fit ASCII.
  o Fixed MPD bindings: they did not correctly get elapsed time.
  o Fixed AttributeError on some systems: LC_MESSAGES is not always available.
  o Fixed Mac OS-specific variant of spotify player support when Python-3 is
    used.
  o Fixed performance of the tabline.

* Sat Apr 16 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 2.3-4
- resolves: #1323828 - Revert move introduced in ceaa583d

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 24 2015 Andreas Schneider <asn@redhat.com> - 2.3-2
- resolves: #1282487 - Switch to python3

* Tue Oct 20 2015 Andreas Schneider <asn@redhat.com> - 2.3-1
- Update to version 2.3
  o Added ability to hide domain part of the user name to common.env.user
    segment.
  o Added ability to show conda environment to virtualenv segment.
  o Added systemd service file.
  o Added ability to detect internal_ip interface using default gateway.
  o Added support for password-protected connections in mpd player bindings.
  o Added `output` option to i3wm.workspaces segment to filter workspaces
    based on their output.
  o Added “charging” indicator to battery segment.
  o Made tmux bindings show zoom indicator in window status.
  o Fixed tmux bindings so that they support tmux-2.1.
  o Fixed support for unicode characters in common.time.date segment.
- resolves: #1272103 - Add missing vim python functions

* Thu Sep 17 2015 Andreas Schneider <asn@redhat.com> - 2.2-2
- resolves: #1246510 - Add appdate metainfo file for Gnome
- resolves: #1260620 - Install vim plugin to correct directory
- resolves: #1260617 - Rename vim plugin to vim-powerline

* Wed Sep 02 2015 Andreas Schneider <asn@redhat.com> - 2.2-1
- Update to version 2.2
  o Added support for newest psutil version.
  o Added support for non-SSL IMAP4 connection.
  o Added support for clickable tab names in Vim.
  o Added support for truncating tmux segments.
  o Added support for new (i3ipc) module that interacts with i3.
  o Added support for i3 modes.
  o Fixed coloring of network_load segment.
  o Fixed dash bindings on OS X.
  o Fixed parsing numbers starting with 2 supplied by POWERLINE_*_OVERRIDES
    environment variables.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 19 2015 Andreas Schneider <asn@redhat.com> - 2.1.4-1
- Update to version 2.1.4
  o Added support for placing powerline on the left in qtile.
  o Added qtile-1.9 support.
  o Fixed tmux-2.0 support.
  o Made it easier to run tests outside of travis.
  o Added some missing highlight groups.
  o Made it omit writing empty above lines.
  o Fixed UnicodeEncodeError when running powerline-lint with
    non-ASCII characters in error messages.
  o Fixed code that replaces &statusline value: it now is able
    to replace non-ASCII &statuslines as well.


* Fri Feb 20 2015 Andreas Schneider <asn@redhat.com> - 2.1-1
- Update to version 2.1
  o Added BAR support.
  o Added support for pdb (Python debugger) prompt.
  o Added more highlight groups to solarized colorscheme.
  o Updated zpython bindings.
  o Fixed C version of the client on non-Linux platforms.
  o Fixed some errors in powerline-lint code.
  o Fixed Python-2.6 incompatibilities in setup.py.

* Tue Jan 20 2015 Andreas Schneider <asn@redhat.com> - 2.0-1
- Update to version 2.0
  o Added fbterm (framebuffer terminal emulator) support.
  o Added theme with unicode-7.0 symbols.
  o Added support for PyPy3.
  o Compiler is now called with CFLAGS from environment in setup.py if present.
  o Added support for pyuv-1.*.
  o Added a way to write error log to Vim global variable.
  o powerline script now supports overrides from $POWERLINE_CONFIG_OVERRIDES,
    $POWERLINE_THEME_OVERRIDES environment variables, so does powerline-config
     script.
  o powerline and powerline-config scripts now support taking paths from
    $POWERLINE_CONFIG_PATHS.
  o powerline-lint is now able to report dictionaries which were merged in to
    form marked dictionary and what were the previous values of overridden
    values.
  o Added support for Byron Rakitzis’ rc shell reimplementation.
  o Added support for querying battery status on cygwin platform.

* Wed Dec 10 2014 Andreas Schneider <asn@redhat.com> - 1.3.1-2
- Update cflags patch.

* Tue Dec 09 2014 Andreas Schneider <asn@redhat.com> - 1.3.1-1
- Update to version 1.3.1.
- resolves: #1171420 - Fix passing optflags to the C compiler.

* Thu Dec 04 2014 Andreas Schneider <asn@redhat.com> - 1.3-2
- Fix powerline-config.

* Wed Dec 03 2014 Andreas Schneider <asn@redhat.com> - 1.3-1
- Update to version 1.3.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-8.20140508git9e7c6c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 08 2014 Andreas Schneider <asn@redhat.com> - 0.0.1-7.20140508git9e7c6c
- Update to revision 0.0.1-7.20140508git9e7c6c

* Wed Mar 12 2014 Andreas Schneider <asn@redhat.com> - 0.0.1-6.20140226git70a94e
- Update to revision 0.0.1-6.20140226git70a94e

* Thu Nov 28 2013 Andreas Schneider <asn@redhat.com> - 0.0.1-6.20131123gitdb80fc
- Remove EPEL support.
- Removed BuildRoot.

* Wed Nov 27 2013 Andreas Schneider <asn@redhat.com> - 0.0.1-5.20131123gitdb80fc
- Remove fontpatcher.py.patch
- Moved BuildReqruies.
- Try to fix build on EPEL5.

* Wed Nov 27 2013 Andreas Schneider <asn@redhat.com> - 0.0.1.20131123gitdb80fc-4
- Added missing vim directories.
- Fixed BuildRoot.
- Use fdupes only on Fedora.
- Use name tag in Requires.

* Mon Nov 25 2013 Andreas Schneider <asn@redhat.com> - 0.0.1.20131123gitdb80fc-3
- Changed define to global
- Moved BuildArch

* Sun Nov 24 2013 Andreas Schneider <asn@redhat.com> - 0.0.1.20131123gitdb80fc-2
- Set checkout.
- Set source URL.
- Fix default configuration path.

* Sun Nov 24 2013 Andreas Schneider <asn@redhat.com> - 0.0.1.20131123gitdb80fc-1
- Initial package.
