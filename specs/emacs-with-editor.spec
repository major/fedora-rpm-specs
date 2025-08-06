%global pkg with-editor
%global pkgname With-Editor

Name:           emacs-%{pkg}
Version:        3.4.5
Release:        %autorelease
Summary:        Use Emacsclient as the editor of child processes
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/magit/with-editor
Source0:        %{url}/archive/v%{version}/%{pkg}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  emacs make texinfo texinfo-tex
BuildRequires:  emacs-dash >= 2.13
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-dash >= 2.13

%description
%{pkgname} makes it possible to reliably use the Emacsclient as the editor
of child processes.

%prep
%autosetup -n %{pkg}-%{version}

%build
%make_build

%install
# With-Editor doesn't provide an install target.
install -D -p -m 644 docs/%{pkg}.info %{buildroot}/%{_infodir}/%{pkg}.info
install -D -p -m 644 -t %{buildroot}/%{_emacs_sitelispdir}/%{pkg} \
  lisp/%{pkg}-autoloads.el lisp/%{pkg}.el lisp/%{pkg}.elc

%files
%license LICENSE
%doc README.org
%{_emacs_sitelispdir}/%{pkg}
%{_infodir}/%{pkg}.info.*

%changelog
%autochangelog
