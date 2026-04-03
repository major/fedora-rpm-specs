Name:            emacs-php-mode
Version:         1.27.0
Release:         1%{?dist}
Summary:         Major GNU Emacs mode for editing PHP code
License:         GPL-3.0-or-later
URL:             https://github.com/emacs-php/php-mode
Source0:         https://github.com/emacs-php/php-mode/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:         php-mode-init.el
BuildArch:       noarch
BuildRequires:   emacs eask git
Requires:        emacs(bin)%{?_emacs_version: >= %{_emacs_version}}
Requires:        emacs-filesystem

%description
Major GNU Emacs mode for editing PHP code.

%prep
%setup -q -n php-mode-%{version}

%build
make %{?_smp_mflags} all

%install
mkdir -p %{buildroot}/%{_emacs_sitelispdir}/php-mode
install -p -m 644 lisp/*.el %{buildroot}/%{_emacs_sitelispdir}/php-mode/

# Install php-mode-init.el
mkdir -p %{buildroot}%{_emacs_sitestartdir}
install -p -m 644 %SOURCE1 %{buildroot}%{_emacs_sitestartdir}

%check
# we could run "make test" here but it requires internet connection so let's just check if the mode is loadable
emacs --batch -L %{buildroot}%{_emacs_sitestartdir} -l php-mode-init --eval "(if (fboundp 'php-mode) (kill-emacs 0) (kill-emacs 1))"

%files
%doc CHANGELOG.md
%license LICENSE
%{_emacs_sitestartdir}/php-mode-init.el
%dir %{_emacs_sitelispdir}/php-mode
%{_emacs_sitelispdir}/php-mode/*

%changelog
* Mon Mar 09 2026 Ruslan Bekenev <furyinbox@gmail.com> - 1.27.0-1
- Update to 1.27.0
- Use SPDX License Expression for License
- Requires: emacs-filesystem for directory ownership

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 12 2017 Tim Landscheidt <tim@tim-landscheidt.de> - 1.18.2-1
- Package v1.18.2.
- Remove php-ext-path.patch that has been merged upstream.
- Don't try to install non-existing info file.
- Incorporate two upstream patches.
- Accidentally work around #1420129 by moving byte-compilation of
  skeleton/*.el to Makefile.
- Fail on byte-compilation warnings.
- Escape changelog entry for 1.17.0-3.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 18 2015 Petr Hracek <phracek@redhat.com> - 1.17.0-5
- set php-ext-path by default
- include all skeletons on request
- Resolves #1289860

* Mon Dec 14 2015 Petr Hracek <phracek@redhat.com> - 1.17.0-4
- Add php-ext.el{,c} files
- Resolves #1289860

* Thu Dec 10 2015 Petr Hracek <phracek@redhat.com> - 1.17.0-3
- Add -p to install command
- remove %%_emacs_bytecompile php-mode.el

* Wed Dec 09 2015 Petr Hracek <phracek@redhat.com> - 1.17.0-2
- Remove 'auto-mode-alist from php-mode-init.el

* Wed Dec 09 2015 Petr Hracek <phracek@redhat.com> - 1.17.0-1
- Use -p in install commands
- Change Source0 from sourceforge to github

* Wed Dec 09 2015 Petr Hracek <phracek@redhat.com> - 1.5.0-1
- Initial package (#1289860)
