Name:           gtypist
Version:        2.10.1
Release:        %autorelease
Summary:        GNU typing tutor
License:        GPL-3.0-or-later AND GFDL-1.3-no-invariants-or-later
Url:            https://www.gnu.org/software/gtypist/
Source:         https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  emacs
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  perl-generators

Requires:       fortune-mod
Requires:       emacs-filesystem >= %{_emacs_version}

%description
GNU Typist (or gtypist) is free software that assists you in learning
to type correctly.

It is intended to be used on a raw terminal without graphics. It has
been compiled and used in Unix (GNU/Linux, Aix, Solaris, openBSD) and
also in DOS/Windows (DOS 6.22, Windows 98, Windows XP).


%prep
%autosetup -p1


%build
%configure --with-lispdir=%{_datadir}/emacs/site-lisp/gtypist
%make_build


%install
%make_install
rm -f %{buildroot}%{_infodir}/dir

%find_lang %{name}

mkdir -p %{buildroot}%{_emacs_sitelispdir}/%{name}
mkdir -p %{buildroot}%{_emacs_sitestartdir}
cat > %{buildroot}%{_emacs_sitestartdir}/gtypist-init.el <<EOF
(autoload 'gtypist-mode "gtypist-mode")
(setq auto-mode-alist (append '(("\\.typ$" . gtypist-mode)) auto-mode-alist))
EOF


%files -f %{name}.lang
%doc AUTHORS NEWS QUESTIONS ChangeLog README THANKS TODO
%license COPYING
%{_bindir}/gtypist
%{_bindir}/typefortune
%{_datadir}/%{name}
%{_infodir}/gtypist.info*
%lang(cs) %{_infodir}/gtypist.cs.info*
%lang(es) %{_infodir}/gtypist.es.info*
%{_mandir}/man1/gtypist.1*
%{_mandir}/man1/typefortune.1*
%{_emacs_sitelispdir}/%{name}
%{_emacs_sitestartdir}/gtypist-init.el


%changelog
%autochangelog
