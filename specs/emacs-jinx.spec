%global pkg     jinx
%global emacs_version_with_archsitelispdir 1:30.2-9

Name:           emacs-%{pkg}
Version:        2.4
Release:        %{autorelease}
Summary:        Fast just-in-time spell-checker for Emacs
License:        GPL-3.0-or-later
URL:            https://github.com/minad/%{pkg}
Source:         https://github.com/minad/%{pkg}/archive/refs/tags/%{version}.tar.gz#/%{pkg}-%{version}.tar.gz

BuildRequires:  /usr/bin/pkg-config
BuildRequires:  emacs-devel
BuildRequires:  emacs-nw >= %{emacs_version_with_archsitelispdir}
BuildRequires:  enchant2-devel
BuildRequires:  gcc

Requires:       emacs(bin) >= %{emacs_version_with_archsitelispdir}
Requires:       emacs(bin)%{?_emacs_version: >= 1:%{_emacs_version}}

%description
Jinx is a fast just-in-time spell-checker for Emacs. Jinx highlights
misspelled words in the text of the visible portion of the buffer. For
efficiency, Jinx highlights misspellings lazily, recognizes window
boundaries and text folding, if any.


%prep
%autosetup -n %{pkg}-%{version}


%build
%{_emacs_bytecompile} jinx.el
%{__cc} \
 $(emacs --batch --load=jinx.elc \
         --eval '(dolist (arg jinx--compile-flags) (princ (concat arg " ")))') \
 %{build_cflags} \
 $(pkg-config --cflags --libs enchant-2) \
 -o %{pkg}-mod.so %{pkg}-mod.c
emacs --batch --eval '(loaddefs-generate "." "%{pkg}-autoloads.el")'


%install
install -d %{buildroot}%{_emacs_archsitelispdir}/ \
           %{buildroot}%{_emacs_sitelispdir}/ \
           %{buildroot}%{_emacs_sitelispdir}/site-start.d/
install -m 0644 %{pkg}-autoloads.el \
        %{buildroot}%{_emacs_sitelispdir}/site-start.d/
install -m 0644 %{pkg}.el %{pkg}.elc %{buildroot}%{_emacs_sitelispdir}/
install -m 0755 %{pkg}-mod.so %{buildroot}%{_emacs_archsitelispdir}/


%check
emacs --batch \
      --eval '(add-to-list '"'"'load-path "%{buildroot}%{_emacs_archsitelispdir}")' \
      --load %{buildroot}%{_emacs_sitelispdir}/%{pkg}.elc \
      --funcall jinx-mode


%files
%license LICENSE
%doc CHANGELOG.org
%doc README.org
%{_emacs_archsitelispdir}/%{pkg}-mod.so
%{_emacs_sitelispdir}/%{pkg}.el
%{_emacs_sitelispdir}/%{pkg}.elc
%{_emacs_sitelispdir}/site-start.d/%{pkg}-autoloads.el


%changelog
%{autochangelog}
