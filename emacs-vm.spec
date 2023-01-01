# Font-lock support of message bodies was added (Source1) from 
# http://de.geocities.com/ulf_jasper/emacs.html on 10th February 2007.

# Note on building VM with support for bbdb: if support for VM in BBDB is
# required, then the source elisp for VM must be installed at build time. If
# support for BBDB is required in VM, then the BBDB source elisp must be present
# at build time. Hence there is a circular BuildRequires and bootstrapping is
# required. The way to do this is (i) build emacs-vm without BuildRequires:
# emacs-bbdb (ii) build emacs-bbdb with BuildRequires: emacs-vm (iii)
# rebuild emacs-vm with BuildRequires: emacs-bbdb. Or vice versa.
%global bbdbsupport 1

%global pkgdir %{_emacs_sitelispdir}/vm
%global etcdir %{_datadir}/emacs/vm
%global pixmapdir %{etcdir}/pixmaps
%global initfile %{_emacs_sitestartdir}/vm-init.el

Summary: Emacs VM mail reader
Summary(sv): Emacs postläsare VM
Name: emacs-vm
Version: 8.2.0
%global date 20220609
%global bzr 1542
Release: %autorelease -p -s %{date}bzr%{bzr}
License: GPL-2.0-or-later
URL: https://launchpad.net/vm
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#  bzr branch lp:vm emacs-vm-YYYYMMDD
#  tar --exclude=.bzr -cJf emacs-vm-YYYYMMDD.tar.xz emacs-vm-YYYYMMDD
# UPDATE:
# In order to use with Emacs 28, use this branch instead:
#  bzr branch lp:~markd-kermodei/vm/vm-emacs-28 emacs-vm-20220609
Source0: %{name}-%{date}.tar.xz
Source1: emacs-vm.metainfo.xml
# https://bugs.launchpad.net/vm/+bug/1225162/comments/6
Patch: marker-pointer.patch

Requires: emacs(bin) >= %{_emacs_version}
BuildRequires: autoconf
BuildRequires: gcc
BuildRequires: emacs texinfo texinfo-tex
BuildRequires: libappstream-glib
BuildRequires: make

%if %{bbdbsupport}
BuildRequires: emacs-bbdb
Requires: emacs-bbdb
%endif

%description
VM (View Mail) is an Emacs subsystem that allows UNIX mail to be read
and disposed of within Emacs.  Commands exist to do the normal things
expected of a mail user agent, such as generating replies, saving
messages to folders, deleting messages and so on.  There are other
more advanced commands that do tasks like bursting and creating
digests, message forwarding, and organizing message presentation
according to various criteria. 

%description -l sv
VM (View Mail) är ett undersystem för Emacs som gör att UNIX e-post
kan läsas och hanteras inifrån Emacs.  Det finns kommandon för att
göra de vanliga sakerna som förväntas av ett postprogram, såsom skapa
svar, spara meddelanden till mappar, radera meddelanden och så vidare.
Det finns andra mer avancerade kommandon som gör saker som att
splittra upp eller skapa sammandrag, vidarebefordra meddelanden och
organisera presentationen av meddelanden enligt olika kriterier.

%prep
%autosetup -n %{name}-%{date} -p 0

%build
autoupdate
autoconf
%configure --with-etcdir=%{etcdir} --with-docdir=%{_pkgdocdir}
make

%install
make install DESTDIR=%{buildroot}

# Create initialization file.
install -d %{buildroot}/%{_emacs_sitestartdir}
cat > %{buildroot}/%{initfile} <<EOF
;; Startup settings for VM
;;
;; For some reason, native compilation breaks VM. As a workaround until the
;; problem is understood and fixed, disable native compilation of all VM
;; lisp files.
(eval-after-load "comp"
    '(if (boundp 'native-comp-deferred-compilation-deny-list)
        (add-to-list 'native-comp-deferred-compilation-deny-list "/vm.*\.el")))

;; Settings for VM itself
(setq vm-toolbar-pixmap-directory "%{pixmapdir}")
(setq vm-image-directory "%{pixmapdir}")
(require 'vm-autoloads)

;; Settings for u-vm-color.el 
(require 'u-vm-color)
(add-hook 'vm-summary-mode-hook 'u-vm-color-summary-mode)
(add-hook 'vm-select-message-hook 'u-vm-color-fontify-buffer)

(defadvice vm-fill-paragraphs-containing-long-lines
    (after u-vm-color activate)
    (u-vm-color-fontify-buffer))
EOF
# Metainfo
install -d %{buildroot}%{_datadir}/metainfo
cp -p %{SOURCE1} %{buildroot}%{_datadir}/metainfo

%check
appstream-util validate-relax --nonet \
	       %{buildroot}%{_datadir}/metainfo/%{name}.metainfo.xml

%files
%doc README.headers-only
%doc %{_infodir}/*
%license COPYING
%{_bindir}/*
%{pkgdir}
%{etcdir}
%{_pkgdocdir}/*
%{initfile}
%{_datadir}/metainfo/%{name}.metainfo.xml

%changelog
%autochangelog
