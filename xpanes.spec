Name:           xpanes
Version:        4.1.3
Release:        5%{?dist}
Summary:        Awesome tmux-based terminal divider
License:        MIT
URL:            https://github.com/greymd/tmux-xpanes
Source0:        %{url}/archive/v%{version}/tmux-xpanes-%{version}.tar.gz
BuildArch:      noarch

Requires:       tmux >= 1.8
Provides:       tmux-xpanes = %{version}-%{release}


%description
Xpanes is the ultimate terminal divider powered by tmux.  It has the following
features:

- Split tmux window into multiple panes
- Construct command lines & execute them on the panes
- Runnable from outside of tmux session
- Runnable from inside of tmux session
- Record operation log
- Flexible layout arrangement for panes
- Select layout presets
- Set columns or rows as you like
- Display pane title on each pane
- Generate command lines from standard input (Pipe mode)


%prep
%autosetup -n tmux-xpanes-%{version}


%install
install -D -p -m 0755 bin/xpanes %{buildroot}%{_bindir}/xpanes
install -D -p -m 0644 man/xpanes.1 %{buildroot}%{_mandir}/man1/xpanes.1
install -D -p -m 0644 completion/zsh/_xpanes %{buildroot}%{_datadir}/zsh/site-functions/_xpanes
ln -s xpanes %{buildroot}%{_bindir}/tmux-xpanes
ln -s xpanes.1 %{buildroot}%{_mandir}/man1/tmux-xpanes.1
ln -s _xpanes %{buildroot}%{_datadir}/zsh/site-functions/_tmux-xpanes


%files
%license LICENSE
%doc README.md
%{_bindir}/xpanes
%{_bindir}/tmux-xpanes
%{_mandir}/man1/xpanes.1*
%{_mandir}/man1/tmux-xpanes.1*
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_xpanes
%{_datadir}/zsh/site-functions/_tmux-xpanes


%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 31 2021 Carl George <carl@george.computer> - 4.1.3-1
- Latest upstream

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 29 2020 Carl George <carl@george.computer> - 4.1.2-1
- Latest upstream

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Carl George <carl@george.computer> - 4.1.1-1
- Initial package rhbz#1759206
